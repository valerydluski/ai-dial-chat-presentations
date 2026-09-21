"""Exercise resumability and manual-edit protection in an isolated temporary copy."""
from pathlib import Path
import json,tempfile,shutil,subprocess,hashlib,sys,os
ROOT=Path(__file__).resolve().parent.parent
m=json.loads((ROOT/'manifest.json').read_text());original=m['decks'][0];results={}
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
with tempfile.TemporaryDirectory(prefix='dial-presentation-resume-') as td:
 f=Path(td);shutil.copytree(ROOT/'src',f/'src');shutil.copytree(ROOT/'assets',f/'assets');(f/'node_modules').symlink_to(ROOT/'node_modules');e=dict(original);sm={'snapshot':m['snapshot'],'decks':[e]}
 for path in [e['content'],e['output']]:
  (f/path).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/path,f/path)
 def save(): (f/'manifest.json').write_text(json.dumps(sm))
 def run(name):return subprocess.run(['node',str(f/'src'/name)],cwd=f,capture_output=True,text=True,check=True)
 save();before=digest(f/e['output']);r=run('generate.mjs');results['unchangedGenerationSkipped']=digest(f/e['output'])==before and 'Up to date:' in r.stdout
 p=f/e['output'];p.write_bytes(p.read_bytes()+b'\nMANUAL_EDIT_CHECK\n');manual=digest(p);r=run('generate.mjs');results['manualPptxPreserved']=digest(p)==manual and 'Protected manual' in r.stderr
 shutil.copy2(ROOT/e['output'],p);save();c=f/e['content'];d=json.loads(c.read_text());d['slides'][0]['title']='Resume check';c.write_text(json.dumps(d));r=run('generate.mjs');results['changedContentRegenerated']=digest(p)!=before
 sm={'snapshot':m['snapshot'],'decks':[dict(original)]};e=sm['decks'][0];png=next(k for k in e['previewHashes'] if k.endswith('.png'));(f/png).parent.mkdir(parents=True,exist_ok=True);shutil.copy2(ROOT/png,f/png);e['previewHashes']={png:e['previewHashes'][png]};(f/png).write_bytes((f/png).read_bytes()+b'\nMANUAL_PREVIEW\n');manual=digest(f/png);save();r=subprocess.run([str(ROOT/'.venv/bin/python'),str(f/'src/render.py')],cwd=f,capture_output=True,text=True,check=True);results['manualPreviewPreserved']=digest(f/png)==manual and 'Protected manually edited previews:' in r.stdout
 sys.path.insert(0,str(ROOT/'src'));from managed import write
 previous=Path.cwd();os.chdir(f)
 try:
  write('README.md','Generated\n');Path('README.md').write_text('Manual\n');protected=not write('README.md','Overwrite\n');results['manualIndexPreserved']=protected and Path('README.md').read_text()=='Manual\n'
 finally:os.chdir(previous)
(ROOT/'qa/resume-check.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2));sys.exit(not all(results.values()))
