import json,re,os,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent;os.chdir(ROOT)
if sys.prefix==sys.base_prefix and (ROOT/'.venv/bin/python').exists():os.execv(str(ROOT/'.venv/bin/python'),[str(ROOT/'.venv/bin/python'),__file__])
import pymupdf as fitz
m=json.load(open('manifest.json'));errors=[]
def clean(s):return re.sub(r'\s+','',s)
for e in m['decks']:
 geo=json.load(open('qa/geometry/'+e['id'].replace('/','-')+'.json'));pdf=fitz.open(Path(e['preview'])/(Path(e['output']).stem+'.pdf'))
 for n,g in enumerate(geo):
  spans=[s for b in pdf[n].get_text('dict')['blocks'] if 'lines'in b for l in b['lines'] for s in l['spans']];joined='';ranges=[]
  for s in spans:
   t=clean(s['text']);ranges.append((len(joined),len(joined)+len(t),s));joined+=t
  for el in g['elements']:
   t=clean(el['text']);starts=[x.start() for x in re.finditer(re.escape(t),joined)] if t else []
   options=[]
   for start in starts:
    ss=[q[2] for q in ranges if q[1]>start and q[0]<start+len(t)];r=fitz.Rect(ss[0]['bbox'])
    for s in ss[1:]:r|=fitz.Rect(s['bbox'])
    options.append((abs(r.x0-el['x']*72)+abs(r.y0-el['y']*72),r))
   if not options:continue
   _,r=min(options,key=lambda x:x[0]);bottom=(el['y']+el['h'])*72
   if r.y1>bottom+5:errors.append({'deck':e['id'],'slide':n+1,'id':g['id'],'text':el['text'],'overflowPt':round(r.y1-bottom,1)})
print(json.dumps(errors,indent=2))
Path('qa/text-fit.json').write_text(json.dumps(errors,indent=2)+'\n')

sys.exit(bool(errors))
