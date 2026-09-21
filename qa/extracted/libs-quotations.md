<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Quotations
Connect answer annotations to inspectable evidence.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-quotations
01
Quotations
lib-quotations-01

### Notes:
Slide ID: lib-quotations-01

This session explains connect answer annotations to inspectable evidence. The library is a local private workspace package at libs/quotations. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/quotations/README.md:1-245
libs/quotations/src/index.ts:1-72
libs/quotations/package.json:1-41
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62 — CitationMarker
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30 — CitationMarkerProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Connect answer annotations to inspectable evidence.

01
02
03
Mark a claim
Group evidence
Jump to context
Show an inline source marker in an answer.
Group annotations by source or citation id.
Derive PDF or Office highlight locations.
02
Quotations
lib-quotations-02

### Notes:
Slide ID: lib-quotations-02

Start with a concrete caller need. Mark a claim: Show an inline source marker in an answer. Group evidence: Group annotations by source or citation id. Jump to context: Derive PDF or Office highlight locations. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/quotations/README.md:1-245
libs/quotations/src/index.ts:1-72
libs/quotations/package.json:1-41
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62 — CitationMarker
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30 — CitationMarkerProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 3 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Follow the ownership boundary
Inputs and effects stay explicit.

01
02
03
04
Host message
Grouping helpers
Citation Marker
Host opener

Annotations and references
Source or citation id
Accessible source control
Viewer and highlight
Library: Annotation utilities, citation presentation and optional citation state.
03
Quotations
lib-quotations-03

### Notes:
Slide ID: lib-quotations-03

The library owns Annotation utilities, citation presentation and optional citation state. The host owns Fetching sources, opening viewers, Markdown pipeline integration and localized labels.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/quotations/README.md:1-245
libs/quotations/src/index.ts:1-72
libs/quotations/package.json:1-41
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62 — CitationMarker
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30 — CitationMarkerProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
CitationMarker · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| sourceName | string |
| annotationCount | number |
| onOpen | () => void |
| labels | CitationMarkerLabels |
04
Quotations
lib-quotations-04

### Notes:
Slide ID: lib-quotations-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/quotations/README.md:1-245
libs/quotations/src/index.ts:1-72
libs/quotations/package.json:1-41
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62 — CitationMarker
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30 — CitationMarkerProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<CitationMarker
  sourceName="demo-report.pdf" annotationCount={2}
  onOpen={() => setOpened(true)}
  labels={{
    ariaLabel: 'Open demo citation',
    label: 'demo-report.pdf',
    labelWithOverflow: 'demo-report.pdf +1',
  }}
/>
Full example: examples/quotations.tsx · uses @epam/ai-dial-quotations
05
Quotations
lib-quotations-05

### Notes:
Slide ID: lib-quotations-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/quotations.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Show an inline source marker in an answer. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/quotations/README.md:1-245
libs/quotations/src/index.ts:1-72
libs/quotations/package.json:1-41
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62 — CitationMarker
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30 — CitationMarkerProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep quotations focused on its public responsibility.

01
02
03
Prepare citation data
Render a marker
Open host evidence
Resolve the source name, count and display labels.
CitationMarker turns that data into a selectable control.
Use onOpen to select a source or display its preview.
06
Quotations
lib-quotations-06

### Notes:
Slide ID: lib-quotations-06

Follow this concrete integration sequence. Prepare citation data: Resolve the source name, count and display labels. Render a marker: CitationMarker turns that data into a selectable control. Open host evidence: Use onOpen to select a source or display its preview. The complete typed module in examples/quotations.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/quotations/README.md:1-245
libs/quotations/src/index.ts:1-72
libs/quotations/package.json:1-41
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62 — CitationMarker
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30 — CitationMarkerProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Multiple citation forms
Markdown composition
Viewer locations
Utilities support offset annotations and paired cit tags.
The citation Markdown hook builds renderer overrides.
Helpers derive PDF and supported Office highlight coordinates.
07
Quotations
lib-quotations-07

### Notes:
Slide ID: lib-quotations-07

Customization comes from the current exports and prop declarations. Multiple citation forms: Utilities support offset annotations and paired cit tags. Markdown composition: useCitationMarkdownComponents builds citation renderers. Viewer locations: Helpers derive PDF and supported Office highlight coordinates. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/quotations/README.md:1-245
libs/quotations/src/index.ts:1-72
libs/quotations/package.json:1-41
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62 — CitationMarker
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30 — CitationMarkerProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat-hooks/src/conversation-sources/useConversationSources/useConversationSources.ts |
| Test evidence | returns content unchanged and renders no marker for uncited content without calling buildLabel |
| Test evidence | uses the single label when annotationCount is 1 |
08
Quotations
lib-quotations-08

### Notes:
Slide ID: lib-quotations-08

Actual consumers: libs/chat-hooks/src/conversation-sources/useConversationSources/useConversationSources.ts; libs/chat-hooks/src/entry-points/file-manager-canvas.ts; libs/chat-shared/src/components/MarkdownRenderer/MarkdownRenderer.tsx; libs/chat-hooks/src/attachment/useAttachmentAction/useAttachmentAction.ts; libs/chat-shared/src/utils/annotation.ts; libs/chat-hooks/src/files/attachment-canvas.ts. Existing test evidence: [{"file": "libs/quotations/src/hooks/useCitationMarkdownComponents/tests/useCitationMarkdownComponents.spec.tsx", "assertions": ["useCitationMarkdownComponents", "returns content unchanged and renders no marker for uncited content without calling buildLabels", "reports the input content unchanged and empty overrides directly from the hook for uncited content", "injects a sentinel and renders a citation marker for cited content", "renders nothing for a sentinel index with no corresponding group entry, without throwing", "defaults the sentinel injection point to the end of content when the primary annotation has no character-range selector", "keeps the same markdownComponents reference across re-renders with unchanged groups emptiness", "recomputes markdownComponents when groups transitions from empty to non-empty", "recomputes markdownComponents when groups transitions from non-empty to empty", "delegates the preview action to onPreview without internal content-type branching", "delegates the open-in-browser action to onOpenInBrowser directly", "calls buildLabels once per rendered marker with the correct group", "useCitationMarkdownComponents \u2014 cit element rendering", "renders a citation marker for a matched <cit> element when not streaming", "renders an unmatched supported <cit> element as literal text"]}, {"file": "libs/quotations/src/components/CitationMarker/tests/CitationMarker.spec.tsx", "assertions": ["CitationMarker", "uses the single label when annotationCount is 1", "uses the overflow label when annotationCount > 1", "calls onOpen when clicked", "renders without an icon by default", "renders the provided icon before the label", "caps the marker width and ellipsises a long source name", "keeps the descriptive aria-label rather than the raw source name", "CitationMarker \u2014 public class names", "stamps the marker pill", "keeps the class on the overflow variant"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-quotations:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/quotations/README.md:1-245
libs/quotations/src/index.ts:1-72
libs/quotations/package.json:1-41
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62 — CitationMarker
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30 — CitationMarkerProps
libs/chat-hooks/src/conversation-sources/useConversationSources/useConversationSources.ts:1-102
libs/quotations/src/hooks/useCitationMarkdownComponents/tests/useCitationMarkdownComponents.spec.tsx:1-545
libs/quotations/src/components/CitationMarker/tests/CitationMarker.spec.tsx:1-107

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Wire the pipeline
Streaming fragments
No source download
Allowed cit tags and renderer overrides must agree.
Incomplete citation tags need streaming-aware handling.
Callbacks and resolvers connect the marker to actual evidence.
09
Quotations
lib-quotations-09

### Notes:
Slide ID: lib-quotations-09

Review these constraints before choosing the library. Wire the pipeline: Allowed cit tags and renderer overrides must agree. Streaming fragments: Incomplete citation tags need streaming-aware handling. No source download: Callbacks and resolvers connect the marker to actual evidence. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/quotations/README.md:1-245
libs/quotations/src/index.ts:1-72
libs/quotations/package.json:1-41
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62 — CitationMarker
libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30 — CitationMarkerProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.