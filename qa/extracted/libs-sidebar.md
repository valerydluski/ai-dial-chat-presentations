<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Sidebar
Give feature panels a common resizable shell.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-sidebar
01
Sidebar
lib-sidebar-01

### Notes:
Slide ID: lib-sidebar-01

This session explains give feature panels a common resizable shell. The library is a local private workspace package at libs/sidebar. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/sidebar/README.md:1-173
libs/sidebar/src/index.ts:1-14
libs/sidebar/package.json:1-39
libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266 — SidebarPanel
libs/sidebar/src/models/panel-props.ts:51-90 — SidebarPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Give feature panels a common resizable shell.

01
02
03
Add a panel
Resize a workspace
Handle empty data
Compose a header, actions and scrollable content.
Use a bounded width with a resize callback.
Use PanelEmpty or PanelNoResults consistently.
02
Sidebar
lib-sidebar-02

### Notes:
Slide ID: lib-sidebar-02

Start with a concrete caller need. Add a panel: Compose a header, actions and scrollable content. Resize a workspace: Use a bounded width with a resize callback. Handle empty data: Use PanelEmpty or PanelNoResults consistently. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/sidebar/README.md:1-173
libs/sidebar/src/index.ts:1-14
libs/sidebar/package.json:1-39
libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266 — SidebarPanel
libs/sidebar/src/models/panel-props.ts:51-90 — SidebarPanelProps

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
Host layout
Sidebar Panel
on Resize Stop
Host state

Open state and content
Header and resize
Width in pixels
Store or reuse width
Library: Panel structure, resize interaction, visibility and empty-state primitives.
03
Sidebar
lib-sidebar-03

### Notes:
Slide ID: lib-sidebar-03

The library owns Panel structure, resize interaction, visibility and empty-state primitives. The host owns Content, search, durable width storage and feature actions.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/sidebar/README.md:1-173
libs/sidebar/src/index.ts:1-14
libs/sidebar/package.json:1-39
libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266 — SidebarPanel
libs/sidebar/src/models/panel-props.ts:51-90 — SidebarPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
SidebarPanel · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| isOpen | boolean |
| orientation | SidebarOrientation |
| children | ReactNode |
| onResizeStop (optional) | ((width: number) => void) |
04
Sidebar
lib-sidebar-04

### Notes:
Slide ID: lib-sidebar-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/sidebar/README.md:1-173
libs/sidebar/src/index.ts:1-14
libs/sidebar/package.json:1-39
libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266 — SidebarPanel
libs/sidebar/src/models/panel-props.ts:51-90 — SidebarPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<SidebarPanel
  isOpen title="Demo sources"
  orientation={SidebarOrientation.Right}
  resizable defaultWidth={width} onResizeStop={setWidth}
  labels={{ ariaLabel: 'Demo sources', closeLabel: 'Close' }}
>
  <p>Host-provided content</p>
</SidebarPanel>
Full example: examples/sidebar.tsx · uses @epam/ai-dial-sidebar
05
Sidebar
lib-sidebar-05

### Notes:
Slide ID: lib-sidebar-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/sidebar.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Compose a header, actions and scrollable content. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/sidebar/README.md:1-173
libs/sidebar/src/index.ts:1-14
libs/sidebar/package.json:1-39
libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266 — SidebarPanel
libs/sidebar/src/models/panel-props.ts:51-90 — SidebarPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep sidebar focused on its public responsibility.

01
02
03
Open host content
Resize the panel
Retain the width
Supply isOpen, title and the panel’s child view.
Enable resizing and handle onResizeStop.
Store the final width in the host if it must survive remounts.
06
Sidebar
lib-sidebar-06

### Notes:
Slide ID: lib-sidebar-06

Follow this concrete integration sequence. Open host content: Supply isOpen, title and the panel’s child view. Resize the panel: Enable resizing and handle onResizeStop. Retain the width: Store the final width in the host if it must survive remounts. The complete typed module in examples/sidebar.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/sidebar/README.md:1-173
libs/sidebar/src/index.ts:1-14
libs/sidebar/package.json:1-39
libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266 — SidebarPanel
libs/sidebar/src/models/panel-props.ts:51-90 — SidebarPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Logical placement
Header slots
Width bounds
SidebarOrientation selects the desired panel side.
leftActions and rightActions are public API slot names.
defaultWidth, minWidth and maxWidth configure resizing.
07
Sidebar
lib-sidebar-07

### Notes:
Slide ID: lib-sidebar-07

Customization comes from the current exports and prop declarations. Logical placement: SidebarOrientation selects the desired panel side. Header slots: leftActions and rightActions are public API slot names. Width bounds: defaultWidth, minWidth and maxWidth configure resizing. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/sidebar/README.md:1-173
libs/sidebar/src/index.ts:1-14
libs/sidebar/package.json:1-39
libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266 — SidebarPanel
libs/sidebar/src/models/panel-props.ts:51-90 — SidebarPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx |
| Test evidence | renders children in the body |
| Test evidence | marks the aside element found by its role |
08
Sidebar
lib-sidebar-08

### Notes:
Slide ID: lib-sidebar-08

Actual consumers: libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx; libs/source-panel/src/constants/public-class-names.ts; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx; libs/attachment-canvas/src/models/attachment-canvas.ts; libs/attachment-canvas/src/constants/public-class-names.ts. Existing test evidence: [{"file": "libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.spec.tsx", "assertions": ["SidebarPanel", "renders children in the body", "has role=complementary and aria-label", "renders leftActions in the left header group", "renders rightActions in the right header group", "side=right: close button is in the right group (last button)", "side=right: renders without a divider", "side=left: close button is rendered after right actions (last button)", "side=left, open: applies the border-s divider facing the navigation rail", "side=left, closed: renders without a divider", "close button calls onClose", "colors prop emits CSS custom properties", "no inline style when colors and typography are omitted", "w-full className overrides inline width", "applies inline width when w-full className is absent"]}, {"file": "libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.classes.spec.tsx", "assertions": ["SidebarPanel \u2014 public class names", "marks the aside element found by its role", "marks the header bar that carries the title", "keeps the aside addressable when the host localises its label"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-sidebar:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/sidebar/README.md:1-173
libs/sidebar/src/index.ts:1-14
libs/sidebar/package.json:1-39
libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266 — SidebarPanel
libs/sidebar/src/models/panel-props.ts:51-90 — SidebarPanelProps
libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:1-203
libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.spec.tsx:1-312
libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.classes.spec.tsx:1-87

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
No built-in search
Persistence is external
Contextual visibility
Compose search in children or header actions.
onResizeStop reports width; the host decides where to save it.
Keep the parent layout and isOpen state synchronized.
09
Sidebar
lib-sidebar-09

### Notes:
Slide ID: lib-sidebar-09

Review these constraints before choosing the library. No built-in search: Compose search in children or header actions. Persistence is external: onResizeStop reports width; the host decides where to save it. Contextual visibility: Keep the parent layout and isOpen state synchronized. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/sidebar/README.md:1-173
libs/sidebar/src/index.ts:1-14
libs/sidebar/package.json:1-39
libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266 — SidebarPanel
libs/sidebar/src/models/panel-props.ts:51-90 — SidebarPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.