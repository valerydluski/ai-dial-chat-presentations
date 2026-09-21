"""Hash-protected generated indexes. Inputs and manual edits stay caller-owned."""
from pathlib import Path
import hashlib,json
LEDGER=Path('content/index-hashes.json')
def digest(p):return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def write(path,value):
 p=Path(path);ledger=json.loads(LEDGER.read_text()) if LEDGER.exists() else {};key=str(p)
 if p.exists() and (key not in ledger or digest(p)!=ledger[key]):
  print('Protected manually edited index:',p);return False
 p.parent.mkdir(parents=True,exist_ok=True);p.write_text(value);ledger[key]=digest(p)
 LEDGER.parent.mkdir(parents=True,exist_ok=True);LEDGER.write_text(json.dumps(ledger,indent=2)+'\n');return True
