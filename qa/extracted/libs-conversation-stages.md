<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Conversation stages
Make streamed execution progress visible inside a response.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-conversation-stages
01
Conversation stages
lib-conversation-stages-01

### Notes:
Slide ID: lib-conversation-stages-01

This session explains make streamed execution progress visible inside a response. The library is a local private workspace package at libs/conversation-stages. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/conversation-stages/README.md:1-142
libs/conversation-stages/src/index.ts:1-17
libs/conversation-stages/package.json:1-39
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229 — StagesPanel
libs/conversation-stages/src/models/stages-props.ts:78-89 — StagesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Make streamed execution progress visible inside a response.

01
02
03
Explain waiting
Inspect a step
Reduce noise
Show named running stages while content arrives.
Expand stage Markdown and copy useful details.
Collapse related work into a compact group.
02
Conversation stages
lib-conversation-stages-02

### Notes:
Slide ID: lib-conversation-stages-02

Start with a concrete caller need. Explain waiting: Show named running stages while content arrives. Inspect a step: Expand stage Markdown and copy useful details. Reduce noise: Collapse related work into a compact group. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/conversation-stages/README.md:1-142
libs/conversation-stages/src/index.ts:1-17
libs/conversation-stages/package.json:1-39
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229 — StagesPanel
libs/conversation-stages/src/models/stages-props.ts:78-89 — StagesPanelProps

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
Stream consumer
Stage[]
Stages Panel
User inspection

Merge stage updates
Index, name, status
Progress display
Expand or copy
Library: Stage display, expansion, status icons and Markdown details.
03
Conversation stages
lib-conversation-stages-03

### Notes:
Slide ID: lib-conversation-stages-03

The library owns Stage display, expansion, status icons and Markdown details. The host owns Receiving and merging stage updates, status truth and generation lifecycle.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/conversation-stages/README.md:1-142
libs/conversation-stages/src/index.ts:1-17
libs/conversation-stages/package.json:1-39
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229 — StagesPanel
libs/conversation-stages/src/models/stages-props.ts:78-89 — StagesPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
StagesPanel · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| stages | Stage[] |
| isStreaming | boolean |
| labels (optional) | StagesPanelLabels |
| styles (optional) | StagesPanelStyles |
04
Conversation stages
lib-conversation-stages-04

### Notes:
Slide ID: lib-conversation-stages-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/conversation-stages/README.md:1-142
libs/conversation-stages/src/index.ts:1-17
libs/conversation-stages/package.json:1-39
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229 — StagesPanel
libs/conversation-stages/src/models/stages-props.ts:78-89 — StagesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<StagesPanel
  isStreaming
  stages={[{
    index: 0, name: 'Read demo sources', status: null,
    content: 'Retrieving evidence',
  }]}
  labels={{ runningAriaLabel: 'Running' }}
/>
Full example: examples/conversation-stages.tsx · uses @epam/ai-dial-conversation-stages
05
Conversation stages
lib-conversation-stages-05

### Notes:
Slide ID: lib-conversation-stages-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/conversation-stages.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Show named running stages while content arrives. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/conversation-stages/README.md:1-142
libs/conversation-stages/src/index.ts:1-17
libs/conversation-stages/package.json:1-39
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229 — StagesPanel
libs/conversation-stages/src/models/stages-props.ts:78-89 — StagesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
See a streaming stage in context
Reproducible demo · actual workspace source components

![assets/component-demo.png](Image1.jpg)

Host-owned stream
The host passes one stage and isStreaming. The panel renders its name, running state and Markdown content.
DEMO · real components rendered from this source snapshot
06
Conversation stages
lib-conversation-stages-10

### Notes:
Slide ID: lib-conversation-stages-10

This is a real browser screenshot of the standalone demo in demo/main.tsx, captured by src/capture-demo.mjs. It renders SettingsPanel, UsageLimitCard and StagesPanel directly from the recorded source snapshot with local stylesheet dependencies. It is an illustrative host, not a screenshot of a deployed DIAL product. All data is synthetic and no backend request is made. Run the Vite command in examples/README.md, then the capture script. Expected behavior: Usage starts selected; selecting Profile updates the controlled active row. The amount and stage remain demo data. The host explicitly supplies dark-theme color overrides. Desktop and phone captures are retained under assets/.

Sources:
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep conversation stages focused on its public responsibility.

01
02
03
Read stream updates
Supply stage state
Inspect the details
The host obtains the current stage records.
Pass stages and isStreaming into StagesPanel.
The panel renders stage status and expandable content.
07
Conversation stages
lib-conversation-stages-06

### Notes:
Slide ID: lib-conversation-stages-06

Follow this concrete integration sequence. Read stream updates: The host obtains the current stage records. Supply stage state: Pass stages and isStreaming into StagesPanel. Inspect the details: The panel renders stage status and expandable content. The complete typed module in examples/conversation-stages.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/conversation-stages/README.md:1-142
libs/conversation-stages/src/index.ts:1-17
libs/conversation-stages/package.json:1-39
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229 — StagesPanel
libs/conversation-stages/src/models/stages-props.ts:78-89 — StagesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Explicit running state
Streaming awareness
Grouped detail
null status represents a running stage in the shared Stage model.
isStreaming controls the active presentation lifecycle.
CollapsedGroup provides a compact wrapper for related stages.
08
Conversation stages
lib-conversation-stages-07

### Notes:
Slide ID: lib-conversation-stages-07

Customization comes from the current exports and prop declarations. Explicit running state: null status represents a running stage in the shared Stage model. Streaming awareness: isStreaming controls the active presentation lifecycle. Grouped detail: CollapsedGroup provides a compact wrapper for related stages. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/conversation-stages/README.md:1-142
libs/conversation-stages/src/index.ts:1-17
libs/conversation-stages/package.json:1-39
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229 — StagesPanel
libs/conversation-stages/src/models/stages-props.ts:78-89 — StagesPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/components/ConversationView/ConversationMessageItem.tsx |
| Test evidence | renders nothing for an empty stage list |
| Test evidence | renders all stage rows |
09
Conversation stages
lib-conversation-stages-08

### Notes:
Slide ID: lib-conversation-stages-08

Actual consumers: apps/chat/src/components/ConversationView/ConversationMessageItem.tsx. Existing test evidence: [{"file": "libs/conversation-stages/src/components/CollapsedGroup/tests/CollapsedGroup.spec.tsx", "assertions": ["CollapsedGroup \u2014 collapsed states", "renders nothing for an empty stage list", "renders a single stage directly, with no summary wrapper", "collapses to a finished summary line by default once the run finishes", "collapses to a failed summary with the failed count called out", "shows elapsed time without double-counting parallel stages", "is expanded by default while running, showing progress through the live step", "keeps a long live stage name on one truncated line", "announces the running summary via a polite live region", "CollapsedGroup \u2014 collapse-by-default-when-finished transition", "auto-collapses the moment a running group finishes", "CollapsedGroup \u2014 labels", "uses the supplied executedLabel/stepsLabel for the finished summary", "conversation-stages \u2014 public class names", "stamps the panel root behind a collapsed group"]}, {"file": "libs/conversation-stages/src/components/StagesPanel/tests/StagesPanel.spec.tsx", "assertions": ["StagesPanel", "renders all stage rows", "applies custom className and the new row-level CSS variable colors", "applies typography.fontClassName to each stage row name", "defaults the row name to dial-small-text and expanded content to dial-tiny-text", "defaults every heading level in expanded content to dial-small-semi-text (14px, semibold)", "applies typography.headingClassName to every heading level in expanded content", "renders a stage with content as a disclosure button that toggles the content", "renders a stage without expandable content as a plain row (no button)", "does not show a running spinner for null-status stages when not streaming", "keeps every null-status stage running until its completed status arrives", "collapses repeated identical names into one \u00d7N row that expands to the individual attempts", "keeps a repeated-stage group running while any attempt is unresolved", "does not double-count overlapping attempts in a collapsed stage row"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-conversation-stages:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/conversation-stages/README.md:1-142
libs/conversation-stages/src/index.ts:1-17
libs/conversation-stages/package.json:1-39
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229 — StagesPanel
libs/conversation-stages/src/models/stages-props.ts:78-89 — StagesPanelProps
apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898
libs/conversation-stages/src/components/CollapsedGroup/tests/CollapsedGroup.spec.tsx:1-245
libs/conversation-stages/src/components/StagesPanel/tests/StagesPanel.spec.tsx:1-315

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Progress is supplied
Keep identity stable
Content sensitivity
The component cannot infer the backend work completed.
Stage index is used when upstream updates are merged.
Only pass execution details intended for the user to see.
10
Conversation stages
lib-conversation-stages-09

### Notes:
Slide ID: lib-conversation-stages-09

Review these constraints before choosing the library. Progress is supplied: The component cannot infer the backend work completed. Keep identity stable: Stage index is used when upstream updates are merged. Content sensitivity: Only pass execution details intended for the user to see. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/conversation-stages/README.md:1-142
libs/conversation-stages/src/index.ts:1-17
libs/conversation-stages/package.json:1-39
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229 — StagesPanel
libs/conversation-stages/src/models/stages-props.ts:78-89 — StagesPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.