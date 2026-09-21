<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Source panel
Put uploaded files, generated files and citations in one evidence panel.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-source-panel
01
Source panel
lib-source-panel-01

### Notes:
Slide ID: lib-source-panel-01

This session explains put uploaded files, generated files and citations in one evidence panel. The library is a local private workspace package at libs/source-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/source-panel/README.md:1-142
libs/source-panel/src/index.ts:1-10
libs/source-panel/package.json:1-41
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203 — ConversationSourcesPanel
libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107 — ConversationSourcesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Put uploaded files, generated files and citations in one evidence panel.

01
02
03
Find evidence
Search by name
Open a reference
Inspect source material beside the conversation.
Narrow attachments and source labels.
Delegate preview or download to the host.
02
Source panel
lib-source-panel-02

### Notes:
Slide ID: lib-source-panel-02

Start with a concrete caller need. Find evidence: Inspect source material beside the conversation. Search by name: Narrow attachments and source labels. Open a reference: Delegate preview or download to the host. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/source-panel/README.md:1-142
libs/source-panel/src/index.ts:1-10
libs/source-panel/package.json:1-41
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203 — ConversationSourcesPanel
libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107 — ConversationSourcesPanelProps

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
Host derivation
Sources panel
Click callback
Host resolver

Files and quotations
Search and sections
Source or attachment
Open the right content
Library: Evidence sections, filtering and attachment/source interactions.
03
Source panel
lib-source-panel-03

### Notes:
Slide ID: lib-source-panel-03

The library owns Evidence sections, filtering and attachment/source interactions. The host owns Source derivation, authenticated downloads and canvas loading.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/source-panel/README.md:1-142
libs/source-panel/src/index.ts:1-10
libs/source-panel/package.json:1-41
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203 — ConversationSourcesPanel
libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107 — ConversationSourcesPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
ConversationSourcesPanel · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| uploaded | DisplayAttachment[] |
| generated | DisplayAttachment[] |
| sources | QuotationSource[] |
| onSourceClick (optional) | ((source: QuotationSource) => void) |
04
Source panel
lib-source-panel-04

### Notes:
Slide ID: lib-source-panel-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/source-panel/README.md:1-142
libs/source-panel/src/index.ts:1-10
libs/source-panel/package.json:1-41
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203 — ConversationSourcesPanel
libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107 — ConversationSourcesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<ConversationSourcesPanel
  isOpen isMobile={false}
  onClose={onClose}
  uploaded={[]} generated={[]}
  sources={sources}
  labels={labels}
  onSourceClick={onOpen}
/>
Full example: examples/source-panel.tsx · uses @epam/ai-dial-source-panel
05
Source panel
lib-source-panel-05

### Notes:
Slide ID: lib-source-panel-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/source-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Inspect source material beside the conversation. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/source-panel/README.md:1-142
libs/source-panel/src/index.ts:1-10
libs/source-panel/package.json:1-41
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203 — ConversationSourcesPanel
libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107 — ConversationSourcesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep source panel focused on its public responsibility.

01
02
03
Group the evidence
Open the panel
Handle a source click
Supply uploaded, generated and source records.
The host controls open state and mobile presentation.
Resolve the selected item and open its host-owned preview.
06
Source panel
lib-source-panel-06

### Notes:
Slide ID: lib-source-panel-06

Follow this concrete integration sequence. Group the evidence: Supply uploaded, generated and source records. Open the panel: The host controls open state and mobile presentation. Handle a source click: Resolve the selected item and open its host-owned preview. The complete typed module in examples/source-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/source-panel/README.md:1-142
libs/source-panel/src/index.ts:1-10
libs/source-panel/package.json:1-41
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203 — ConversationSourcesPanel
libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107 — ConversationSourcesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Separate collections
Panel customization
Matched text
uploaded, generated and sources retain their distinct roles.
Width bounds, labels and additionalSections are explicit inputs.
Search results use the shared highlighting convention.
07
Source panel
lib-source-panel-07

### Notes:
Slide ID: lib-source-panel-07

Customization comes from the current exports and prop declarations. Separate collections: uploaded, generated and sources retain their distinct roles. Panel customization: Width bounds, labels and additionalSections are explicit inputs. Matched text: Search results use the shared highlighting convention. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/source-panel/README.md:1-142
libs/source-panel/src/index.ts:1-10
libs/source-panel/package.json:1-41
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203 — ConversationSourcesPanel
libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107 — ConversationSourcesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx |
| Test evidence | stamps the panel on the desktop layout |
| Test evidence | renders uploaded attachments |
08
Source panel
lib-source-panel-08

### Notes:
Slide ID: lib-source-panel-08

Actual consumers: apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx; libs/chat-hooks/src/conversation-sources/useConversationSources/useConversationSources.ts; libs/sidebar/src/constants/public-class-names.ts. Existing test evidence: [{"file": "libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.classes.spec.tsx", "assertions": ["ConversationSourcesPanel \u2014 public class names", "stamps the panel on the desktop layout", "keeps the class beside the mobile full-width utility", "stamps the panel while it is closed"]}, {"file": "libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.spec.tsx", "assertions": ["ConversationSourcesPanel", "renders uploaded attachments", "renders generated attachments", "close button calls onClose", "renders empty state when no data", "renders uploaded and generated sections in order", "renders sources section", "renders the download-all button disabled when onDownloadAll is omitted", "renders the download-all button enabled and wired to onDownloadAll", "ConversationSourcesPanel \u2014 search", "typing a partial name filters uploaded and generated sections", "shows no-results state when query matches nothing", "clearing the query restores all attachments", "filters sources by title, url, and quote", "ConversationSourcesPanel \u2014 title and additionalSections (optional, additive)"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-source-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/source-panel/README.md:1-142
libs/source-panel/src/index.ts:1-10
libs/source-panel/package.json:1-41
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203 — ConversationSourcesPanel
libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107 — ConversationSourcesPanelProps
apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:1-354
libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.classes.spec.tsx:1-116
libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.spec.tsx:1-383

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
No implicit fetching
Required labels
Boundary drift
Opening a row needs a host callback.
The panel contract requires the complete labels object.
The README peer list differs from current package composition.
09
Source panel
lib-source-panel-09

### Notes:
Slide ID: lib-source-panel-09

Review these constraints before choosing the library. No implicit fetching: Opening a row needs a host callback. Required labels: The panel contract requires the complete labels object. Boundary drift: The README peer list differs from current package composition. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/source-panel/README.md:1-142
libs/source-panel/src/index.ts:1-10
libs/source-panel/package.json:1-41
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203 — ConversationSourcesPanel
libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107 — ConversationSourcesPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.