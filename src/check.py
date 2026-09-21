import os,sys,json,re,zipfile,subprocess,hashlib,collections
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent;os.chdir(ROOT)
if sys.prefix==sys.base_prefix and (ROOT/'.venv/bin/python').exists():os.execv(str(ROOT/'.venv/bin/python'),[str(ROOT/'.venv/bin/python'),__file__,*sys.argv[1:]])
import pymupdf as fitz
from markitdown import MarkItDown
converter=MarkItDown()
from lxml import etree
m=json.loads(Path('manifest.json').read_text());repo=Path(os.environ.get('DIAL_REPO',str(ROOT.parent/'ai-dial-chat')));results=[];ns={'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
def clean(s):return re.sub(r'\s+','',s).replace('’',"'").replace('–','-').replace('‑','-')
for e in m['decks']:
 if len(sys.argv)>1 and sys.argv[1] not in [e['id'],e['path'].split('/')[-1]]:continue
 p=Path(e['output']);d=json.loads(Path(e['content']).read_text());errors=[];warnings=[];pdf=Path(e['preview'])/(p.stem+'.pdf')
 extracted=converter.convert(str(p)).text_content
 Path('qa/extracted').mkdir(exist_ok=True)
 Path('qa/extracted',e['id'].replace('/','-')+'.md').write_text(extracted)
 markers=re.findall(r'<!-- Slide number: (\d+) -->',extracted)
 if len(markers)!=len(d['slides']):errors.append('MarkItDown slide count mismatch')
 if e.get('contentSha256')!=hashlib.sha256(Path(e['content']).read_bytes()).hexdigest():errors.append('PPTX is stale for current JSON content')
 validation=subprocess.run([sys.executable,'tools/pptx-skill/scripts/office/validate.py',str(p)],capture_output=True,text=True,timeout=120);Path('qa/structural').mkdir(exist_ok=True);Path('qa/structural',e['id'].replace('/','-')+'.log').write_text((validation.stdout+'\n'+validation.stderr).strip()+'\n')
 if validation.returncode:errors.append('Anthropic structural validation failed')
 doc=fitz.open(pdf) if pdf.exists() else None
 if not doc or len(doc)!=len(d['slides']):errors.append('Missing or wrong-count PDF render')
 z=zipfile.ZipFile(p);slidefiles=sorted([x for x in z.namelist() if re.match(r'ppt/slides/slide\d+.xml$',x)],key=lambda x:int(re.search(r'(\d+)\.xml',x)[1]));notesfiles=[x for x in z.namelist() if re.match(r'ppt/notesSlides/notesSlide\d+.xml$',x)];fonts=set();per=[]
 if len(slidefiles)!=len(d['slides']):errors.append('Slide count differs from content')
 if len(notesfiles)!=len(slidefiles):errors.append('Missing speaker notes')
 for i,(f,s) in enumerate(zip(slidefiles,d['slides'])):
  xml=etree.fromstring(z.read(f));texts=xml.xpath('//a:t/text()',namespaces=ns);text='\n'.join(texts);slideErrors=[]
  if re.search(r'[\u0400-\u04ff]',text+s['notes']):slideErrors.append('Non-English Cyrillic text')
  if re.search(r'\b(?:TODO|FIXME|lorem ipsum)\b|\[insert',text,re.I):slideErrors.append('Template placeholder')
  for source in s['sources']:
   sp=repo/source['file']
   if not sp.exists() or source['start']<1 or source['end']>len(sp.read_text().splitlines()):slideErrors.append('Invalid source range: '+source['file'])
  for sh in xml.xpath('//p:sp|//p:graphicFrame|//p:pic',namespaces=ns):
   off=sh.xpath('.//a:xfrm/a:off|./p:xfrm/a:off',namespaces=ns);ext=sh.xpath('.//a:xfrm/a:ext|./p:xfrm/a:ext',namespaces=ns)
   if off and ext:
    x,y,cx,cy=map(int,[off[0].get('x'),off[0].get('y'),ext[0].get('cx'),ext[0].get('cy')]);
    if x<0 or y<0 or x+cx>12192100 or y+cy>6858100:slideErrors.append('Object exceeds slide boundary')
  if doc and i<len(doc):
   page=doc[i];pdftext=clean(page.get_text());missing=[]
   for t in texts:
    if len(clean(t))>1 and clean(t) not in pdftext:missing.append(t)
   if missing:slideErrors.append('Text missing from PDF: '+json.dumps(missing))
   spans=[sp for b in page.get_text('dict')['blocks'] if 'lines'in b for line in b['lines'] for sp in line['spans']]
   for ai,a in enumerate(spans):
    if not a['text'].strip():continue
    for b in spans[ai+1:]:
     if not b['text'].strip():continue
     inter=fitz.Rect(a['bbox'])&fitz.Rect(b['bbox'])
     if inter.width>2 and inter.height>3 and inter.get_area()>min(fitz.Rect(a['bbox']).get_area(),fitz.Rect(b['bbox']).get_area())*0.12:slideErrors.append('Rendered text overlap: '+a['text']+' / '+b['text'])
   for sp in spans:
    fonts.add(sp['font']);r=sp['bbox']
    if r[0]<-1 or r[1]<-1 or r[2]>page.rect.width+1 or r[3]>page.rect.height+1:slideErrors.append('Rendered text outside page: '+sp['text'])
   # Text should not enter the footer region, except the known footer labels.
   for sp in spans:
    if sp['size']>=16 and sp['bbox'][3]>498:slideErrors.append('Content enters footer region: '+sp['text'])
  per.append({'id':s['id'],'slide':i+1,'errors':slideErrors,'render':f'{e["preview"]}/slide-{i+1:02}.png'})
  errors.extend([s['id']+': '+x for x in slideErrors])
 actual=hashlib.sha256(p.read_bytes()).hexdigest()
 if e.get('renderedPptxSha256')!=actual:errors.append('Preview is stale for current PPTX')
 unexpected=[f for f in fonts if not any(x in f for x in ['Arial','CourierNew'])]
 if unexpected:errors.append('Unexpected rendered fonts: '+','.join(unexpected))
 result={'id':e['id'],'slides':len(slidefiles),'notes':len(notesfiles),'fonts':sorted(fonts),'structuralPassed':validation.returncode==0,'errors':errors,'warnings':warnings,'slideChecks':per};results.append(result)
 e['qaStatus']='passed' if not errors else 'failed';e['status']='checked' if not errors else 'needs-fix';print(e['id'],len(errors),'errors',flush=True)
existing=json.loads(Path('qa/check-results.json').read_text()) if Path('qa/check-results.json').exists() else []
if len(sys.argv)>1:results=[x for x in existing if x['id'] not in {r['id'] for r in results}]+results
Path('qa/check-results.json').write_text(json.dumps(results,indent=2)+'\n');Path('manifest.json').write_text(json.dumps(m,indent=2)+'\n');print('TOTAL',sum(x['slides'] for x in results),'slides;',sum(len(x['errors']) for x in results),'errors')
sys.exit(bool(sum(len(x['errors']) for x in results)))
