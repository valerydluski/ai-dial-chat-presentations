"""Verify the deployable site without repository, Node, browser or office dependencies."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, re, sys
ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / '_site'
class Document(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]; self.ids=set(); self.lang=None; self.titles=0
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag=='html': self.lang=a.get('lang')
        if tag=='h1': self.titles+=1
        if 'id' in a: self.ids.add(a['id'])
        for k in ['href','src']:
            if k in a: self.links.append(a[k])
errors=[]; links=0; docs={}
for p in SITE.rglob('*.html'):
    d=Document();d.feed(p.read_text());docs[p.resolve()]=d
    if d.lang!='en' or d.titles!=1: errors.append(f'Invalid document language/heading: {p.relative_to(SITE)}')
for p,d in docs.items():
    for target in d.links:
        u=urlsplit(target)
        if u.scheme or u.netloc: continue
        resolved=(p.parent/unquote(u.path)).resolve() if u.path else p
        links+=1
        if not resolved.is_relative_to(SITE.resolve()): errors.append(f'Link escapes public site: {target}')
        elif not resolved.is_file(): errors.append(f'Missing target in {p.relative_to(SITE)}: {target}')
        elif u.fragment and resolved in docs and unquote(u.fragment) not in docs[resolved].ids: errors.append(f'Missing anchor: {target}')
files=[p for p in SITE.rglob('*') if p.is_file()]
for p in files:
    if p.is_symlink(): errors.append('Symlink in deployment: '+str(p))
    if not (p.suffix in ['.html','.css','.png','.pdf','.pptx'] or p.name in ['.nojekyll','UPSTREAM-LICENSE.txt']): errors.append('Unexpected public artifact: '+str(p))
    if p.suffix in ['.html','.css'] and re.search(r'/Users/|/private/tmp|gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{40,}|-----BEGIN .*PRIVATE KEY-----',p.read_text()): errors.append('Local path or credential marker: '+str(p))
m=json.loads((ROOT/'manifest.json').read_text())
counts={'pptx':len(list(SITE.rglob('*.pptx'))),'pdf':len(list(SITE.rglob('*.pdf'))),'slideImages':len(list(SITE.rglob('slide-*.png'))),'htmlPages':len(docs),'localLinksChecked':links}
if counts['pptx']!=len(m['decks']) or counts['pdf']!=len(m['decks']) or counts['slideImages']!=sum(e['slideCount'] for e in m['decks']): errors.append('Public artifact counts differ from manifest')
report={**counts,'errors':errors};(ROOT/'qa').mkdir(exist_ok=True);(ROOT/'qa/site-check.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report,indent=2));sys.exit(bool(errors))
