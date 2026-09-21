# QA report — AI DIAL Chat technical series

**33 completed PowerPoint presentations, 329 slides, 329 speaker-note pages.** The series contains one 21-slide overview, four application decks (15, 14, 8 and 8 slides), and 28 library decks (9–10 slides each). Every deck is English and has its own editable PowerPoint file, content JSON, rendered PDF, slide images and HTML preview. The [README](README.md) is the complete file index.

## Verification results

| Check | Result | Evidence |
|---|---|---|
| Filesystem and Nx project coverage | 4 apps + 28 libraries; one additional fixture is auxiliary | [Saved Nx graph](content/nx-graph.json), [manifest](manifest.json) |
| Official Anthropic structural validation | 33/33 pass | [Validation logs](qa/structural), [per-deck results](qa/check-results.json) |
| Actual PPTX rendering | 33 PDFs; all 329 slides rasterized at 150 dpi | [Preview index](index.html), each deck's render.log |
| Slide text and notes | 329/329 contain editable text, English notes and sources | [Extracted text](qa/extracted), [speaker notes](content/speaker-notes.md) |
| Rendered layout | No missing text, detected text overlaps, off-page content or footer collisions | [Per-slide checks](qa/check-results.json) |
| Text-box fit | No detected vertical text overflow beyond the 5 pt measurement tolerance | [Text-fit results](qa/text-fit.json) |
| Fonts | ArialMT, Arial-BoldMT and CourierNewPSMT in final PDFs | [Per-deck font audit](qa/check-results.json) |
| TypeScript examples | 28 full modules; zero example or inherited dependency diagnostics | [TypeScript 6.0.3 results](qa/typescript.json), [examples](examples/README.md) |
| Resume and manual edits | All five checks pass: unchanged skip, changed-input rebuild, and protection of edited PPTX, previews and indexes | [Resume checks](qa/resume-check.json) |
| Source traceability | All 279 cited files match both the original commit and the current working tree | [Source index](sources.md), [source audit](qa/repository-final.json) |
| Final inventory and links | 33 PPTX; all current local links resolve; 4,727 native shapes and 68 native tables | [Bundle check](qa/bundle-check.json) |

The structural validator is the official skill's `scripts/office/validate.py`. `check.py` also uses MarkItDown and reads native slide XML and the rendered PDF. It checks source line bounds, slide/note counts, placeholders, render freshness, text completeness, rendered span overlap, page boundaries and fonts. `check-text-fit.py` compares the generator's text-box geometry with the rendered glyph bounds. These automated measurements complement visual inspection; they are not a claim of pixel-identical rendering in every presentation application.

## Visual review and corrections

Every slide was inspected in rendered contact sheets. Selected dense code, table, diagram and changed slides were also inspected individually at the full 2000 × 1125 PNG resolution. [Visual-review records](qa/visual-review.json) distinguish complete contact-sheet coverage from those close-ups. All 329 individual PNGs are retained for inspection.

Corrections made during review included title wrapping, the chat-stream flow label, configuration-table column widths, a long toolset callback signature, lower-card text overflow, test-caption truncation, and the MCP sandbox success/denial flow. Library workflow slides were revised to describe each library's actual integration. All affected decks were regenerated, rendered and checked again.

The series uses native PowerPoint text, code text boxes, tables, diagram boxes and arrows. The favicon and actual browser screenshots are raster images; no slide is a flattened screenshot. The colors are `0D1117`, `EDF2F7` and `8EBCFF`, with Arial for prose and Courier New for code. Body text is generally 22 pt and code 18 pt; supporting captions, source cues and footer metadata are smaller.

The real DIAL favicon was copied from the adjacent SDK repository and is checked by SHA-256. No PowerPoint presentation was found there during the presentation-file search, so the requested visual palette was used directly.

## Reproducible component demo

[Demo source](demo/main.tsx) renders actual workspace `SettingsPanel`, `UsageLimitCard` and `StagesPanel` components with synthetic values, separately from the product application. Screenshots are explicitly labeled **DEMO** wherever embedded. The local Vite demo made no backend requests.

The browser capture checked a 1440 × 710 desktop viewport, selected the Profile tab and checked its `aria-selected` state, then captured a 390 × 844 mobile viewport and checked for horizontal overflow. No page errors or failed interaction/layout checks were reported. See the [capture script](src/capture-demo.mjs), [browser result](qa/demo-browser.json), [desktop image](assets/component-demo.png) and [mobile image](assets/component-demo-mobile.png). This is evidence for these three rendered components, not a test of the entire chat application or all 28 libraries in a browser.

## Source snapshot and repository changes

The initial audit was taken at **2026-09-21T18:14:40.584272+00:00**, commit **23fa39459d8971c10d5bd1c69734e61b124d249b**. The initial untracked paths were `.claude/skills/pptx/`, `openspec/changes/migrate-nestjs-v12/` and `skills-lock.json`. They are retained in the [snapshot](content/snapshot.json). No uncommitted application or library implementation was used.

During the task, HEAD changed to **71ae573f4bb46b58671dec4791a5c32e584fdc5d**. The changed files concern app-config normalization and OpenSpec artifacts. This presentation task made no source-repository edits, dependency installations, application builds or git writes. The original audit commit remains in the presentations. Every cited source file was compared against both that commit and the later working tree: **279 matches, zero mismatches**. The final observed status and changed-path list are recorded in [repository-final.json](qa/repository-final.json). The app/library inventory remained 4/28. A NestJS 12 migration proposal is not described as implemented code.

All library manifests have `private: true`. The presentations show workspace imports and host integration; they do not claim verified public npm availability or recommend installing these internal libraries from a registry. The existing publication tooling is discussed only as a repository mechanism.

## Documentation drift and implementation qualifications

The source repository was not modified to correct these findings. The decks follow actual exports, manifests and implementations.

| Finding | Evidence and treatment |
|---|---|
| Architecture tree is stale | [architecture.md, lines 41–47](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/docs/architecture.md) lists three apps and 22 libraries. The filesystem and saved Nx graph contain four apps and 28 libraries. |
| OpenSpec stack versions lag the manifests | [config.yaml](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/openspec/config.yaml) names Nx 22, TypeScript 5.9 and React Router 6. The [root manifest](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/package.json) specifies Nx 23.2.1, TypeScript ~6.0.2 and React Router ^8.3.0. The example checker resolved TypeScript 6.0.3. |
| Generated-client README example uses an absent class | [client README, lines 44–46](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/README.md) uses `ModelsApi`. The actual [DeploymentsApi](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts) exposes `listDeployments()`; its Raw counterpart receives `{}`. The checked example uses those real signatures. |
| Shared library has runtime code | The “types only (no logic)” statement in [config.yaml](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/openspec/config.yaml) is outdated. [chat-shared exports](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/chat-shared/src/index.ts) include utilities, UI and shared behavior. The narrow grid-event exception and canonical hook placement are described as implemented. |
| Isolation policy and existing dependencies differ | [toolset-editor GeneralForm](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/toolset-editor/src/components/GeneralForm/GeneralForm.tsx) imports chat-hooks; [usage-dashboard mapping](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts) imports generated client DTOs and an enum. The written exceptions in [AGENTS.md](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/AGENTS.md) do not make all such dependencies a general library pattern. Decks call out this current coupling. |
| “No state of its own” is too broad | [attachment-input README](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/README.md) makes this claim, while [useLazyImageLoad](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/attachment-input/src/hooks/useLazyImageLoad.ts) manages local loading state. Host-owned file data and transport are distinguished from transient library state. |
| Prompt popup returns values | The [prompts README](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/README.md) introduction suggests replacement happens in the popup; its later example is clearer. [PromptParametersPopupProps](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/libs/prompts/src/models/prompt-parameters-popup-props.ts) declares `onSubmit(values)`. The host calls the shared replacement helper to obtain text. |
| Locale support is not complete translation coverage | [i18n/config.ts](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat/src/i18n/config.ts) registers English resources and sets runtime direction for ar/he/fa/ur. Direction switching is implemented; complete Arabic translations are not claimed. |
| Not every controller uses a versioned route | [ThemeController](https://github.com/epam/ai-dial-chat/blob/23fa39459d8971c10d5bd1c69734e61b124d249b/apps/chat-api/src/themes/theme.controller.ts) is public and unversioned: `/api/themes` and `/api/themes/icon`. The blanket controller-versioning description is qualified in the backend material. |

Additional contract checks reflected in the slides: `SharePopover` is a named root export; sidebar width persistence belongs to the host; Responses routing combines the server flag with deployment capability; the main conversation stream has backend-owned persistence; and the generation registry is in-process rather than a durable cross-pod service. Detailed source ranges are in each slide's notes and [sources.md](sources.md).

## Tools and remaining limits

PptxGenJS was initially unavailable in the output directory and was installed there at version 4.0.1. Python tooling lives in the bundle's `.venv`. The official [Anthropic pptx skill](https://github.com/anthropics/skills/tree/main/skills/pptx) was used locally under `tools/pptx-skill/` and is excluded from the GitHub repository. A portable LibreOffice 26.8.0.3 macOS Apple Silicon renderer was downloaded from the official Document Foundation distribution; its DMG SHA-256 was verified as `8858d8058da4f862f47559486814e65efc27294da67c5e4bb56b006b1ee59f89`.

- **Desktop Microsoft PowerPoint was not available.** All decks were structurally validated and rendered through LibreOffice; native PowerPoint opening, interactive editing and presentation-mode behavior were not exercised.
- **Poppler/pdftoppm was unavailable.** PDF rasterization used PyMuPDF at 150 dpi after conversion of the actual PPTX by the official skill's LibreOffice wrapper.
- **Initial font substitution was corrected.** The portable renderer now resolves the installed Arial and Courier New faces using local symlinks. Final PDF font checks pass. No licensed font binaries are redistributed; another machine must provide those fonts. [setup-fonts.py](src/setup-fonts.py) recreates local macOS links.
- **Application build/test suites and live DIAL Core, OIDC and backend workflows were not run.** Existing tests were read and cited as behavioral evidence, never reported as passing runs. Example compilation and the isolated component demo are the executed application-code checks. Runtime commands in the decks come from project configuration.
- **External installation/publication was not verified.** The 28 libraries are private workspace packages. The demos rely on the adjacent repository's existing aliases and dependencies.
- **Visual close-ups are selective.** All slides received contact-sheet review and automated rendered-text checks; individual full-resolution close-ups focused on dense or changed layouts.

## Repeat the checks

From this bundle directory:

```bash
npm run generate
npm run generate -- libs/chat-hooks
npm run render
npm run check:examples
npm run check
npm run index
npm run check:resume
npm run check:bundle
```

Use the [README](README.md) for dependency setup and platform notes. The generator and renderer skip unchanged outputs. Manually changed PowerPoint files, preview artifacts and generated indexes are preserved and reported. Edit the stable-ID JSON content to request an intentional rebuild; manually edited PowerPoint changes are not imported back into that content.

## GitHub publication

The gallery and downloads are published through GitHub Pages. See [PUBLISHING.md](PUBLISHING.md) for repository visibility, deployment, local preview and excluded tooling. Presentation content and artifact hashes were preserved during website packaging. [Site checks](qa/site-check.json) validate the public file set and links.
