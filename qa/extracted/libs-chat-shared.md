<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Chat shared
Share domain vocabulary, utilities and common UI primitives.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-chat-shared
01
Chat shared
lib-chat-shared-01

### Notes:
Slide ID: lib-chat-shared-01

This session explains share domain vocabulary, utilities and common ui primitives. The library is a local private workspace package at libs/chat-shared. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Share domain vocabulary, utilities and common UI primitives.

01
02
03
Agree on shapes
Reuse common UI
Bridge file managers
Use the same message, stage and attachment types.
Share Markdown, icons and resource summaries.
Use a typed controller without host persistence knowledge.
02
Chat shared
lib-chat-shared-02

### Notes:
Slide ID: lib-chat-shared-02

Start with a concrete caller need. Agree on shapes: Use the same message, stage and attachment types. Reuse common UI: Share Markdown, icons and resource summaries. Bridge file managers: Use a typed controller without host persistence knowledge. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars

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
Host domain
Shared contracts
Feature library
Host composition

Resolved values
Types and utilities
Consistent interpretation
One application view
Library: Shared models, pure utilities, UI primitives and narrow file-manager event bindings.
03
Chat shared
lib-chat-shared-03

### Notes:
Slide ID: lib-chat-shared-03

The library owns Shared models, pure utilities, UI primitives and narrow file-manager event bindings. The host owns App providers, authentication, routing, storage keys and external-system configuration.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
buildCssVars · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| MessageRole / Stage | Shared enums and domain records |
| buildCssVars(vars) | CSSProperties, omitting empty values |
| /markdown | MarkdownRenderer and related exports |
| /file-manager | Shell, controller types and bindings |
04
Chat shared
lib-chat-shared-04

### Notes:
Slide ID: lib-chat-shared-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

const style = buildCssVars({
  '--text-primary': '#EDF2F7',
  '--unused': undefined,
});
// Undefined values are omitted.
const role = MessageRole.Assistant;
Full example: examples/chat-shared.tsx · uses @epam/ai-dial-chat-shared
05
Chat shared
lib-chat-shared-05

### Notes:
Slide ID: lib-chat-shared-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/chat-shared.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Use the same message, stage and attachment types. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep chat shared focused on its public responsibility.

01
02
03
Resolve host values
Render shared content
Keep integration local
Choose the text and theme values in the application.
Use MarkdownRenderer and buildCssVars in a host view.
Wire file-manager callbacks and persistence in the host.
06
Chat shared
lib-chat-shared-06

### Notes:
Slide ID: lib-chat-shared-06

Follow this concrete integration sequence. Resolve host values: Choose the text and theme values in the application. Render shared content: Use MarkdownRenderer and buildCssVars in a host view. Keep integration local: Wire file-manager callbacks and persistence in the host. The complete typed module in examples/chat-shared.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Reuse the Markdown entry
A common renderer keeps display behavior consistent.

import { MarkdownRenderer }
  from '@epam/ai-dial-chat-shared/markdown';

<MarkdownRenderer
  content="**Demo:** shared Markdown rendering"
/>
Focused source-backed example · see examples/ and content/api-index.md.
07
Chat shared
lib-chat-shared-10

### Notes:
Slide ID: lib-chat-shared-10

This fragment is part of SharedDemo. The renderer needs the host stylesheet and the dependencies of the selected entry point. Do not treat the shared package as types-only.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Focused entries
CSS variable builder
Canonical grid hook
/markdown and /file-manager expose narrower entry points.
buildCssVars drops undefined and empty values.
useGridEditingScroll lives here and is re-exported by chat-hooks.
08
Chat shared
lib-chat-shared-07

### Notes:
Slide ID: lib-chat-shared-07

Customization comes from the current exports and prop declarations. Focused entries: /markdown and /file-manager expose narrower entry points. CSS variable builder: buildCssVars drops undefined and empty values. Canonical grid hook: useGridEditingScroll lives here and is re-exported by chat-hooks. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | prompt-editor/src/components/PromptEditor/PromptEditor.tsx |
| Test evidence | disables the Attach button when no paths are selected |
| Test evidence | calls ensureIndexVisible with the row index when inline rename starts |
09
Chat shared
lib-chat-shared-08

### Notes:
Slide ID: lib-chat-shared-08

Actual consumers: libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx; libs/prompt-editor/src/components/PromptFolderField/PromptFolderField.tsx; libs/skills/src/hooks/useSkillSelectorOverlay/useSkillSelectorOverlay.tsx; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx; libs/skills/src/components/ChatSkill/ChatSkill.tsx; libs/usage-dashboard/src/components/ModelLimitsSection/PeriodStatusIndicator.tsx. Existing test evidence: [{"file": "libs/chat-shared/src/file-manager/FileManagerAttachModal/tests/FileManagerAttachModal.spec.tsx", "assertions": ["FileManagerAttachModal", "Attach button disabled state", "disables the Attach button when no paths are selected", "disables the Attach button while the controller is loading", "disables the Attach button while an operation is in progress", "enables the Attach button when a file is selected and idle", "Attach button click", "calls onAttach with the selected file when Attach is clicked", "calls onAttach with the resolved folder path when a folder is selected", "skips folders whose resolveFolderPath returns null", "count limit exceeded", "calls onCountLimitExceeded and does not call onAttach when the limit is exceeded", "unsupported file type", "calls onSkippedUnsupportedFiles when a file with a disallowed type is selected", "shell callback forwarding"]}, {"file": "libs/chat-shared/src/file-manager/useGridEditingScroll/tests/useGridEditingScroll.spec.ts", "assertions": ["useGridEditingScroll", "calls ensureIndexVisible with the row index when inline rename starts", "does not call ensureIndexVisible when the grid api is destroyed", "seeds known row ids on the first rowDataUpdated after mount without scrolling", "scrolls the temporary new-folder row into view when a new row appears", "does not scroll when rowDataUpdated introduces no new row ids", "removes listeners from the previous grid api when a new api instance is passed", "removes listeners from the subscribed api when the hook unmounts", "does not attach duplicate listeners when the same api instance is passed twice", "treats the first rowDataUpdated after reset() as a fresh seed with no scroll"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-chat-shared:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: disables the Attach button when no paths are selected.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:1-310
libs/chat-shared/src/file-manager/FileManagerAttachModal/tests/FileManagerAttachModal.spec.tsx:1-484
libs/chat-shared/src/file-manager/useGridEditingScroll/tests/useGridEditingScroll.spec.ts:1-258

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
More than types
Entry-specific peers
Legacy boundary assumptions
The source includes runtime utilities and rendered UI.
The file-manager entry needs its optional peer pair installed.
The old no-dependencies description is not the current graph.
10
Chat shared
lib-chat-shared-09

### Notes:
Slide ID: lib-chat-shared-09

Review these constraints before choosing the library. More than types: The source includes runtime utilities and rendered UI. Entry-specific peers: The file-manager entry needs its optional peer pair installed. Legacy boundary assumptions: The old no-dependencies description is not the current graph. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/chat-shared/README.md:1-986
libs/chat-shared/src/index.ts:1-73
libs/chat-shared/package.json:1-80
libs/chat-shared/src/utils/build-css-vars.ts:4-14 — buildCssVars
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.