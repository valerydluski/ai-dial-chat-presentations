"""Check inventory, links, source hashes and editable artifacts without rebuilding."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import datetime, hashlib, json, os, re, sys, zipfile
from xml.etree import ElementTree as ET
ROOT = Path(__file__).resolve().parent.parent
os.chdir(ROOT)
m = json.loads(Path('manifest.json').read_text())
repo = Path(os.environ.get('DIAL_REPO',str(ROOT.parent/'ai-dial-chat')))
errors = []
def require(ok, message):
    if not ok: errors.append(message)
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
projects = {str(p.relative_to(repo)) for group in ['apps', 'libs'] for p in (repo/group).iterdir() if (p/'package.json').is_file()}
require({e['path'] for e in m['decks'] if e['id'] != 'overview'} == projects, 'App/library coverage differs from the filesystem')
require(len(m['decks']) == len(projects)+1, 'Manifest topic count mismatch')
graph = json.loads(Path('content/nx-graph.json').read_text())['graph']
graph_roots = {v['data']['root'] for v in graph['nodes'].values()}
require(projects.issubset(graph_roots), 'Projects missing from saved Nx graph')
require(len(set(e['id'] for e in m['decks'])) == len(m['decks']), 'Duplicate deck IDs')
require({str(p) for p in Path('decks').rglob('*.pptx')} == {e['output'] for e in m['decks']}, 'PPTX inventory differs from manifest')
ids = set(); slides = 0; notes = 0; native_shapes = 0; native_tables = 0; pictures = 0
ns = {'a':'http://schemas.openxmlformats.org/drawingml/2006/main','p':'http://schemas.openxmlformats.org/presentationml/2006/main'}
checks = {r['id']:r for r in json.loads(Path('qa/check-results.json').read_text())}
for e in m['decks']:
    d = json.loads(Path(e['content']).read_text()); count = len(d['slides']); slides += count
    low, high = (18,22) if e['id']=='overview' else ((6,8) if 'sandbox' in e['id'] else ((12,16) if e['id'].startswith('apps/') else (8,16)))
    require(low <= count <= high, e['id']+': unexpected slide count')
    require(e['status']=='checked' and e.get('qaStatus')=='passed', e['id']+': incomplete status')
    require(sha(e['output'])==e['outputSha256']==e['renderedPptxSha256'], e['id']+': stale PPTX or render')
    require(sha(e['content'])==e['contentSha256'], e['id']+': stale content')
    require(len(list(Path(e['preview']).glob('slide-*.png')))==count, e['id']+': PNG count mismatch')
    for p,h in e['previewHashes'].items(): require(Path(p).is_file() and sha(p)==h, 'Modified/missing preview: '+p)
    require(e['id'] in checks and not checks[e['id']]['errors'] and checks[e['id']]['structuralPassed'], e['id']+': structural/render check failed')
    if e['id'].startswith('libs/'):
        layouts = {s['layout'] for s in d['slides']}
        require('code' in layouts and 'flow' in layouts, e['id']+': missing editable example or interaction diagram')
        require(json.loads((repo/e['path']/'package.json').read_text()).get('private') is True, e['id']+': publication status changed')
    for s in d['slides']:
        require(s['id'] not in ids, 'Duplicate stable slide ID: '+s['id']); ids.add(s['id'])
        require(bool(s.get('notes')) and bool(s.get('sources')), s['id']+': missing notes/sources')
    with zipfile.ZipFile(e['output']) as z:
        presentation = ET.fromstring(z.read('ppt/presentation.xml')); size=presentation.find('p:sldSz', ns)
        require(abs(int(size.attrib['cx'])/int(size.attrib['cy'])-16/9)<0.0001, e['id']+': not widescreen')
        for name in z.namelist():
            if re.fullmatch(r'ppt/notesSlides/notesSlide\d+\.xml', name): notes += 1
            if not re.fullmatch(r'ppt/slides/slide\d+\.xml', name): continue
            xml=ET.fromstring(z.read(name)); native_shapes+=len(xml.findall('.//p:sp',ns)); native_tables+=len(xml.findall('.//a:tbl',ns)); pictures+=len(xml.findall('.//p:pic',ns))
            require(bool(xml.findall('.//a:t',ns)), e['id']+': slide lacks native editable text')
for p,h in json.loads(Path('content/source-hashes.json').read_text()).items(): require((repo/p).is_file() and sha(repo/p)==h, 'Source changed: '+p)
for p,h in json.loads(Path('content/index-hashes.json').read_text()).items(): require(Path(p).is_file() and sha(p)==h, 'Modified/missing generated index: '+p)
require(not json.loads(Path('qa/text-fit.json').read_text()), 'Rendered text exceeds text boxes')
typescript=json.loads(Path('qa/typescript.json').read_text())
require(typescript['exampleFiles']==28 and not typescript['exampleErrors'] and not typescript['dependencyErrors'], 'TypeScript example verification failed')
require(all(json.loads(Path('qa/resume-check.json').read_text()).values()), 'Resumability verification failed')
require(not json.loads(Path('qa/repository-final.json').read_text())['initialCommitMismatches'], 'Cited sources differ from initial audit commit')
require(sha('assets/favicon.png')==sha(repo.parent/'ai-dial-typescript-sdk/website/public/favicon.png'), 'Favicon differs from supplied branding asset')
class Links(HTMLParser):
    def __init__(self): super().__init__(); self.links=[]
    def handle_starttag(self,tag,attrs):
        self.links.extend(v for k,v in attrs if k in ['href','src'] and v)
files = [Path(p) for p in ['README.md','PUBLISHING.md','NOTICE.md','sources.md','qa-report.md','index.html','content/api-index.md','content/speaker-notes.md']]
files += sorted(Path('examples').glob('*.md')) + sorted(Path('previews').rglob('index.html'))
link_count=0
for p in files:
    require(p.is_file(), 'Missing required index/report: '+str(p))
    if not p.is_file(): continue
    content=p.read_text(); require(not re.search(r'[\u0400-\u04ff]',content), 'Cyrillic in English material: '+str(p))
    if p.suffix=='.html':
        parser=Links();parser.feed(content); links=parser.links
    else:
        prose=re.sub(r'```[\s\S]*?```','',content)
        links=[x[1] for x in re.findall(r'\[([^\]]+)\]\(([^)]+)\)',prose)]
    for target in links:
        u=urlsplit(target.strip('<>'))
        if u.scheme or u.netloc or not u.path: continue
        link_count+=1
        resolved=(p.parent/unquote(u.path)).resolve()
        require(resolved.exists() or resolved==ROOT/'qa/bundle-check.json', f'Broken link in {p}: {target}')
for p in Path('content/decks').glob('*.json'):
    require(not re.search(r'[\u0400-\u04ff]',p.read_text()), 'Cyrillic in slide data: '+str(p))
result={'checkedAt':datetime.datetime.now(datetime.timezone.utc).isoformat(),'topics':len(m['decks']),'apps':sum(p.startswith('apps/') for p in projects),'libs':sum(p.startswith('libs/') for p in projects),'slides':slides,'speakerNoteSlides':notes,'nativeShapes':native_shapes,'nativeTables':native_tables,'picturesIncludingBranding':pictures,'localLinksChecked':link_count,'allSourcesMatch':not any(x.startswith('Source changed:') for x in errors),'errors':errors}
Path('qa/bundle-check.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2));sys.exit(bool(errors))
