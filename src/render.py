import os,sys,json,subprocess,hashlib
from pathlib import Path
ROOT=Path(__file__).resolve().parent.parent;os.chdir(ROOT)
if sys.prefix==sys.base_prefix and (ROOT/'.venv/bin/python').exists():os.execv(str(ROOT/'.venv/bin/python'),[str(ROOT/'.venv/bin/python'),__file__,*sys.argv[1:]])
import pymupdf as fitz
from PIL import Image,ImageDraw,ImageFont
def sha(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
m=json.loads(Path('manifest.json').read_text());arg=sys.argv[1] if len(sys.argv)>1 else None
lo=ROOT/'tools/LibreOffice.app/Contents/MacOS';os.environ['PATH']=str(lo)+os.pathsep+os.environ['PATH']
for e in m['decks']:
 if arg and arg not in [e['id'],e['path'].split('/')[-1]]:continue
 deck=ROOT/e['output']
 if not deck.exists():continue
 dest=ROOT/e['preview'];dest.mkdir(parents=True,exist_ok=True)
 pdf=dest/(deck.stem+'.pdf')
 fingerprint=sha(__file__)
 existing=e.get('previewHashes',{})
 changed=[f for f,h in existing.items() if Path(f).exists() and sha(f)!=h]
 if changed:
  print('Protected manually edited previews:',changed,flush=True);e['status']='protected-manual-preview';continue
 if e.get('renderedPptxSha256')==sha(deck) and e.get('rendererFingerprint')==fingerprint and existing and all(Path(f).exists() for f in existing):
  print('Preview up to date:',e['id'],flush=True);continue
 result=subprocess.run([sys.executable,'tools/pptx-skill/scripts/office/soffice.py','--headless','--convert-to','pdf','--outdir',str(dest),str(deck)],capture_output=True,text=True,timeout=180)
 (dest/'render.log').write_text(result.stdout+'\n'+result.stderr)
 if result.returncode or not pdf.exists():print('Render failed',e['id'],result.stderr);e['status']='render-failed';continue
 document=fitz.open(pdf)
 for i,page in enumerate(document):
  pix=page.get_pixmap(matrix=fitz.Matrix(150/72,150/72),alpha=False);pix.save(dest/f'slide-{i+1:02}.png')
 # Contact sheets accompany full-resolution slides; they do not replace them.
 for start in range(0,len(document),6):
  sheet=Image.new('RGB',(1600,3*475),'#0D1117');draw=ImageDraw.Draw(sheet)
  for k in range(start,min(start+6,len(document))):
   im=Image.open(dest/f'slide-{k+1:02}.png');im.thumbnail((780,440));x=10+(k-start)%2*800;y=10+(k-start)//2*475;sheet.paste(im,(x,y));draw.text((x+8,y+443),f'{e["id"]} / {k+1:02}',fill='#EDF2F7')
  sheet.save(dest/f'contact-{start//6+1:02}.jpg',quality=91)
 e['rendererFingerprint']=fingerprint;e['previewHashes']={str(f.relative_to(ROOT)):sha(f) for f in dest.iterdir() if f.suffix in ['.png','.pdf','.jpg']}
 e['renderedSlideCount']=len(document);e['renderedPptxSha256']=hashlib.sha256(deck.read_bytes()).hexdigest();e['status']='rendered'
 Path('manifest.json').write_text(json.dumps(m,indent=2)+'\n');print('Rendered',e['id'],len(document),'slides',flush=True)

Path("manifest.json").write_text(json.dumps(m,indent=2)+"\n")
