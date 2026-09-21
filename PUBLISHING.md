# Publishing the presentation gallery

Repository: [valerydluski/ai-dial-chat-presentations](https://github.com/valerydluski/ai-dial-chat-presentations)

Public website: [AI DIAL Chat presentations](https://valerydluski.github.io/ai-dial-chat-presentations/)

The repository is public. GitHub rejected Pages on the initially created private repository because the account plan did not support that combination. The owner then selected a public repository and public Pages site.

The [Pages workflow](.github/workflows/pages.yml) builds and validates the gallery on every push to `main`, then deploys the `_site` artifact. It uses GitHub's built-in token and the `github-pages` environment; no personal access token or deployment key is needed. Repository Settings → Pages must use **GitHub Actions** as its source.

## Build and view locally

Python 3.10 or newer is sufficient. The public site is generated from the committed PPTX, PDFs, PNGs, manifest, slide content and QA results. It does not need the original application repository, a browser, Node, fonts or LibreOffice.

```bash
python3 src/build-site.py
python3 src/check-site.py
python3 -m http.server 8080 --directory _site --bind 127.0.0.1
```

Open `http://127.0.0.1:8080/`. The gallery provides topic navigation, all 33 PowerPoint and PDF downloads, full slide previews, expandable speaker notes, and source links pinned to the public audited commit. The site uses relative local URLs so it works beneath the GitHub Pages project path.

Only the gallery HTML/CSS, favicon, license, PPTX, PDFs and individual slide PNGs are deployed. The research JSON, examples, generator and QA logs remain in the repository. Dependencies, the local demo cache, LibreOffice, fonts and the Anthropic skill are excluded from git. The website and PowerPoint artifacts contain no production user data.

## Update presentations

1. Edit the stable-ID content under `content/decks/`.
2. Run `npm run generate -- <deck-id>` and `npm run render -- <deck-id>`.
3. With the matching adjacent AI DIAL Chat checkout and local verification tools available, run `npm run check`, then `npm run index`.
4. Run `npm run site:build` and `npm run site:check`.
5. Review and commit the updated source/artifacts, then push to `main`.

The workflow publishes committed, already-rendered artifacts. It does not silently regenerate slides using different fonts in CI. A PPTX edit requires new matching previews and passing QA before site generation will accept it.

## Local verification prerequisites

`npm run generate` needs only this repository and `npm ci`. Source research, example checking and the full bundle audit additionally need the original `ai-dial-chat` repository adjacent to this checkout, at the recorded audit commit with its dependencies installed. Source-checking scripts accept `DIAL_REPO` to override that location. The optional component demo expects the adjacent checkout.

The official [Anthropic pptx skill](https://github.com/anthropics/skills/tree/main/skills/pptx) was used locally during authoring. Its files are not redistributed in this repository; install/access it separately under `tools/pptx-skill/` to run the official validator. LibreOffice and licensed Arial/Courier New fonts are also local prerequisites for rendering, rather than git assets. Historical paths and hashes remain in the original QA records as provenance.

## Verification

[Site link and artifact checks](qa/site-check.json) cover every generated HTML document, internal target/anchor, output inventory, and the public artifact allowlist. Browser verification passed at 1440, 390 and 360 px: 33 gallery cards, all 21 overview slides, notes expansion, no horizontal overflow and a matching downloaded PPTX hash. Results are in [site-browser.json](qa/site-browser.json). The original presentation checks and their limits are in [qa-report.md](qa-report.md).
