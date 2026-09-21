"""Build a public, dependency-free gallery from the verified presentation artifacts."""
from pathlib import Path
from html import escape
from urllib.parse import quote
import hashlib, json, shutil

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / '_site'
MANIFEST = json.loads((ROOT / 'manifest.json').read_text())
SOURCE = 'https://github.com/epam/ai-dial-chat/blob/' + MANIFEST['snapshot']['commit'] + '/'
CSS = '''
:root{color-scheme:dark;font-family:Arial,sans-serif;background:#0d1117;color:#edf2f7}
*{box-sizing:border-box}body{margin:0}main,header,footer{max-width:1320px;margin:auto;padding:24px}
a{color:#8ebcff;text-underline-offset:4px}a:hover{color:#fff}a:focus-visible,summary:focus-visible{outline:3px solid #8ebcff;outline-offset:5px;border-radius:3px}
h1{font-size:clamp(2rem,5vw,3.5rem);line-height:1.12;margin:24px 0}h2{font-size:1.8rem}h3{font-size:1.25rem;margin:0 0 12px}p{line-height:1.65}small,.muted{color:#bcc9da}.lead{font-size:1.2rem;max-width:850px}
.brand{display:flex;align-items:center;gap:14px;font-weight:bold;font-size:1.1rem}.brand img{width:36px;height:36px}.stats{color:#8ebcff;font-size:1.15rem}
nav,.actions{display:flex;gap:12px;flex-wrap:wrap;align-items:center}nav a,.button{display:inline-flex;align-items:center;min-height:44px;padding:10px 16px;border:1px solid #33455d;border-radius:8px;text-decoration:none}.button.primary{background:#8ebcff;color:#0d1117;font-weight:bold}
.grid{display:grid;grid-template-columns:1fr;gap:22px}.card{border:1px solid #33455d;border-radius:12px;background:#17202c;overflow:hidden}.card img{display:block;width:100%;height:auto;aspect-ratio:16/9;background:#0d1117}.card-body{padding:20px}.card p{margin:12px 0}.project{font-family:monospace;overflow-wrap:anywhere;font-size:.9rem}
section{margin:40px 0 64px;scroll-margin-top:20px}.slide{margin:32px 0 48px;padding-bottom:24px;border-bottom:1px solid #33455d}.slide>img{display:block;width:100%;height:auto;aspect-ratio:16/9}.slide h2{font-size:1.3rem}.slide nav{margin:16px 0}summary{cursor:pointer;color:#8ebcff;min-height:44px;padding:14px 0}details p{white-space:pre-wrap;overflow-wrap:anywhere}li{line-height:1.6;margin:8px 0;overflow-wrap:anywhere}.table-wrap{overflow:auto}table{border-collapse:collapse;width:100%}th,td{border:1px solid #33455d;padding:14px;text-align:start}th{background:#22324a}code{overflow-wrap:anywhere}footer{border-top:1px solid #33455d;color:#bcc9da}.skip{position:absolute;inset-inline-start:-10000px}.skip:focus{position:static;display:block;padding:16px}
@media(min-width:720px){.grid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media(min-width:1120px){.grid{grid-template-columns:repeat(3,minmax(0,1fr))}}
'''

def write(path, content):
    p = SITE / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content)

def copy(path):
    path = Path(path)
    if path.is_absolute() or '..' in path.parts:
        raise ValueError('Public artifact paths must stay inside the bundle')
    src = ROOT / path
    if src.is_symlink() or not src.is_file():
        raise ValueError('Expected a regular public artifact: ' + str(path))
    dest = SITE / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dest)

def page(title, body, prefix=''):
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="description" content="33 English technical presentations about AI DIAL Chat, with editable PowerPoint downloads and source references."><title>{escape(title)} · AI DIAL Chat</title><link rel="icon" href="{prefix}assets/favicon.png"><link rel="stylesheet" href="{prefix}site.css"></head><body><a class="skip" href="#main">Skip to content</a><header><a class="brand" href="{prefix}index.html"><img src="{prefix}assets/favicon.png" alt="">AI DIAL Chat · Technical series</a></header><main id="main">{body}</main><footer>33 presentations · 329 slides · English · Source audit: {escape(MANIFEST['snapshot']['analysisDate'][:10])}<p>Personal technical knowledge-sharing material. <a href="{prefix}qa.html">Verification and limitations</a> · <a href="{prefix}sources.html">Source reference index</a> · <a href="{prefix}UPSTREAM-LICENSE.txt">Upstream license</a></p></footer></body></html>'''

def source_link(source):
    f = source['file']
    url = SOURCE + quote(f, safe='/') + f'#L{source["start"]}-L{source["end"]}'
    return f'<a href="{escape(url)}">{escape(f)}:{source["start"]}–{source["end"]}</a>'

# _site is disposable build output; source artifacts and manual PPTX edits are untouched.
if SITE.exists():
    if SITE.is_symlink(): raise ValueError('_site must not be a symlink')
    shutil.rmtree(SITE)
SITE.mkdir()
write('.nojekyll', '')
write('site.css', CSS)
copy('assets/favicon.png')
copy('UPSTREAM-LICENSE.txt')
checks = {c['id']: c for c in json.loads((ROOT / 'qa/check-results.json').read_text())}
groups = {'overview': [], 'apps': [], 'libs': []}
source_sections = []
for entry in MANIFEST['decks']:
    content_path = ROOT / entry['content']
    if hashlib.sha256(content_path.read_bytes()).hexdigest() != entry['contentSha256']:
        raise ValueError('Slide content changed; regenerate and check before publishing: ' + entry['id'])
    deck = json.loads(content_path.read_text())
    output_hash = hashlib.sha256((ROOT / entry['output']).read_bytes()).hexdigest()
    if output_hash != entry['renderedPptxSha256'] or output_hash != entry['outputSha256']:
        raise ValueError('PPTX and previews must match: ' + entry['id'])
    if entry.get('qaStatus') != 'passed' or checks[entry['id']]['errors']:
        raise ValueError('Deck is not verified: ' + entry['id'])
    copy(entry['output'])
    preview = Path(entry['preview'])
    pdf = preview / (Path(entry['output']).stem + '.pdf')
    if hashlib.sha256((ROOT / pdf).read_bytes()).hexdigest() != entry['previewHashes'][str(pdf)]:
        raise ValueError('PDF preview changed: ' + str(pdf))
    copy(pdf)
    for i in range(1, len(deck['slides']) + 1):
        png = preview / f'slide-{i:02}.png'
        if hashlib.sha256((ROOT / png).read_bytes()).hexdigest() != entry['previewHashes'][str(png)]:
            raise ValueError('Preview changed: ' + str(png))
        copy(png)
    title = escape(deck['shortTitle'])
    group = 'overview' if entry['id'] == 'overview' else entry['id'].split('/')[0]
    groups[group].append(f'''<article class="card"><a href="{preview}/index.html" aria-label="View {title}"><img src="{preview}/slide-01.png" width="2000" height="1125" loading="lazy" alt="{title} presentation cover"></a><div class="card-body"><h3>{title}</h3><span class="muted project">{escape(entry['path'])} · {len(deck['slides'])} slides</span><p>{escape(entry['purpose'])}</p><div class="actions"><a class="button primary" href="{preview}/index.html">View slides</a><a class="button" href="{entry['output']}" download>PowerPoint</a><a class="button" href="{pdf}">PDF</a></div></div></article>''')
    prefix = '../' * len(preview.parts)
    slides = []
    refs = []
    for i, slide in enumerate(deck['slides'], 1):
        anchors = []
        if i > 1: anchors.append(f'<a href="#slide-{i-1}">Previous slide</a>')
        if i < len(deck['slides']): anchors.append(f'<a href="#slide-{i+1}">Next slide</a>')
        anchors.append('<a href="#main">Back to top</a>')
        sources = ''.join('<li>' + source_link(s) + '</li>' for s in slide['sources'])
        slides.append(f'''<article class="slide" id="slide-{i}"><h2>{i:02} · {escape(slide['title'])}</h2><img src="slide-{i:02}.png" width="2000" height="1125" loading="lazy" alt="Slide {i}: {escape(slide['title'])}"><nav aria-label="Slide {i} navigation">{' '.join(anchors)}</nav><details><summary>Speaker notes and sources</summary><p>{escape(slide['notes'])}</p><ul>{sources}</ul></details></article>''')
        refs.append(f'<h3>{escape(slide["id"])} — {escape(slide["title"])}</h3><ul>{sources}</ul>')
    write(preview/'index.html', page(deck['shortTitle'], f'''<h1>{title}</h1><p class="lead">{escape(entry['purpose'])}</p><nav aria-label="Presentation actions"><a href="{prefix}index.html">All presentations</a><a class="button primary" href="{prefix}{entry['output']}" download>Download PowerPoint</a><a href="{pdf.name}">Open PDF</a></nav><p class="muted">{len(deck['slides'])} slides · Expand notes below each slide for the explanation and source references.</p>{''.join(slides)}''', prefix))
    source_sections.append(f'<section id="{escape(entry["id"].replace("/","-"))}"><h2>{title}</h2>{"".join(refs)}</section>')

sections = ''.join(f'<section id="{key}"><h2>{label}</h2><div class="grid">{"".join(groups[key])}</div></section>' for key,label in [('overview','Start with the architecture'),('apps','Applications'),('libs','Libraries')])
write('index.html', page('Presentations', f'''<h1>Explore AI DIAL Chat</h1><p class="lead">Architecture, applications and reusable libraries — explained through source-backed technical presentations.</p><p class="stats">33 presentations · 329 slides · 4 apps · 28 libraries</p><nav aria-label="Browse topics"><a href="#overview">Overview</a><a href="#apps">Applications</a><a href="#libs">Libraries</a><a href="qa.html">QA report</a><a href="sources.html">Sources</a></nav>{sections}'''))
write('sources.html', page('Source reference index', f'''<h1>Source reference index</h1><p>All paths and line ranges point to the audited public <a href="https://github.com/epam/ai-dial-chat/tree/{MANIFEST['snapshot']['commit']}">AI DIAL Chat commit</a>: <code>{MANIFEST['snapshot']['commit']}</code>. Every slide also includes these references in its PowerPoint speaker notes.</p><nav><a href="index.html">All presentations</a></nav>{''.join(source_sections)}'''))
rows = ''.join(f'<tr><th scope="row">{escape(e["id"])}</th><td>{checks[e["id"]]["slides"]}</td><td>Passed</td><td>{checks[e["id"]]["notes"]}</td></tr>' for e in MANIFEST['decks'])
write('qa.html', page('Verification and limitations', f'''<h1>Verification and limitations</h1><p class="lead">All 33 editable PowerPoint files passed structural validation. All 329 slides were rendered, checked for missing text and overlaps, and visually reviewed in contact sheets.</p><ul><li>28 complete TypeScript example modules compiled with zero diagnostics.</li><li>Arial and Courier New were verified in the final rendered PDFs.</li><li>279 cited source files matched the original audited commit.</li><li>Actual component demo images use synthetic data and are labeled DEMO.</li></ul><h2>Checks that were not run</h2><p>Desktop Microsoft PowerPoint and live backend, DIAL Core and OIDC workflows were not tested. Rendering used LibreOffice and PyMuPDF. Existing app test sources were inspected; full app build/test suites were not executed. Individual full-resolution visual close-ups were selective; contact-sheet and automated checks covered every slide.</p><p>The source repository changed HEAD during preparation. All cited files matched both the original commit and the later observed working tree. Libraries are private workspace packages; public npm availability was not claimed.</p><h2>Deck results</h2><div class="table-wrap"><table><thead><tr><th>Topic</th><th>Slides</th><th>Structure / render</th><th>Notes</th></tr></thead><tbody>{rows}</tbody></table></div><p>Source snapshot: <code>{MANIFEST['snapshot']['commit']}</code></p><nav><a href="index.html">All presentations</a><a href="sources.html">Source references</a></nav>'''))
files = [p for p in SITE.rglob('*') if p.is_file()]
print(f'Built {len(MANIFEST["decks"])} presentation pages and {len(files)} public files ({sum(p.stat().st_size for p in files)/1_000_000:.1f} MB) in _site/')
