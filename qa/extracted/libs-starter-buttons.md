<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Starter buttons
Offer prompt starters that fit the available space.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-starter-buttons
01
Starter buttons
lib-starter-buttons-01

### Notes:
Slide ID: lib-starter-buttons-01

This session explains offer prompt starters that fit the available space. The library is a local private workspace package at libs/starter-buttons. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/starter-buttons/README.md:1-150
libs/starter-buttons/src/index.ts:1-7
libs/starter-buttons/package.json:1-39
libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193 — StarterButtons
libs/starter-buttons/src/models/starter-props.ts:20-38 — StarterButtonsProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Offer prompt starters that fit the available space.

01
02
03
Start a conversation
Handle narrow screens
Keep behavior explicit
Expose useful first actions before the user types.
Move excess choices to the overflow menu.
The host decides what a selected starter does.
02
Starter buttons
lib-starter-buttons-02

### Notes:
Slide ID: lib-starter-buttons-02

Start with a concrete caller need. Start a conversation: Expose useful first actions before the user types. Handle narrow screens: Move excess choices to the overflow menu. Keep behavior explicit: The host decides what a selected starter does. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/starter-buttons/README.md:1-150
libs/starter-buttons/src/index.ts:1-7
libs/starter-buttons/package.json:1-39
libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193 — StarterButtons
libs/starter-buttons/src/models/starter-props.ts:20-38 — StarterButtonsProps

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
Host deployment
Starter Buttons
on Select
Host composer

Starter Option[]
Visible and overflow
Whole Starter Option
Populate or submit
Library: Starter layout, available-space measurement and overflow controls.
03
Starter buttons
lib-starter-buttons-03

### Notes:
Slide ID: lib-starter-buttons-03

The library owns Starter layout, available-space measurement and overflow controls. The host owns Starter data, mobile mode when supplied and send/populate behavior.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/starter-buttons/README.md:1-150
libs/starter-buttons/src/index.ts:1-7
libs/starter-buttons/package.json:1-39
libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193 — StarterButtons
libs/starter-buttons/src/models/starter-props.ts:20-38 — StarterButtonsProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
StarterButtons · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| starters | StarterOption[] |
| onSelect | (starter: StarterOption) => void |
| labels | StarterButtonsLabels |
| isCollapsible (optional) | boolean |
04
Starter buttons
lib-starter-buttons-04

### Notes:
Slide ID: lib-starter-buttons-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/starter-buttons/README.md:1-150
libs/starter-buttons/src/index.ts:1-7
libs/starter-buttons/package.json:1-39
libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193 — StarterButtons
libs/starter-buttons/src/models/starter-props.ts:20-38 — StarterButtonsProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function StartersDemo({ starters, onSelect }: {
  starters: StarterOption[]; onSelect: (starter: StarterOption) => void;
}) {
  return <StarterButtons starters={starters} onSelect={onSelect}
    labels={{ list: 'Demo starters', overflow: 'More starters' }} />;
}
Full example: examples/starter-buttons.tsx · uses @epam/ai-dial-starter-buttons
05
Starter buttons
lib-starter-buttons-05

### Notes:
Slide ID: lib-starter-buttons-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/starter-buttons.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Expose useful first actions before the user types. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/starter-buttons/README.md:1-150
libs/starter-buttons/src/index.ts:1-7
libs/starter-buttons/package.json:1-39
libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193 — StarterButtons
libs/starter-buttons/src/models/starter-props.ts:20-38 — StarterButtonsProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep starter buttons focused on its public responsibility.

01
02
03
Choose starter options
Render choices
Apply the selection
The host supplies the available starter records.
StarterButtons handles the list and overflow presentation.
Use onSelect to fill or send content through the host.
06
Starter buttons
lib-starter-buttons-06

### Notes:
Slide ID: lib-starter-buttons-06

Follow this concrete integration sequence. Choose starter options: The host supplies the available starter records. Render choices: StarterButtons handles the list and overflow presentation. Apply the selection: Use onSelect to fill or send content through the host. The complete typed module in examples/starter-buttons.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/starter-buttons/README.md:1-150
libs/starter-buttons/src/index.ts:1-7
libs/starter-buttons/package.json:1-39
libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193 — StarterButtons
libs/starter-buttons/src/models/starter-props.ts:20-38 — StarterButtonsProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Responsive overflow
Collapse policy
Accessible names
Measured space determines which options remain visible.
isCollapsible changes the overflow behavior.
labels names the list and the overflow action.
07
Starter buttons
lib-starter-buttons-07

### Notes:
Slide ID: lib-starter-buttons-07

Customization comes from the current exports and prop declarations. Responsive overflow: Measured space determines which options remain visible. Collapse policy: isCollapsible changes the overflow behavior. Accessible names: labels names the list and the overflow action. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/starter-buttons/README.md:1-150
libs/starter-buttons/src/index.ts:1-7
libs/starter-buttons/package.json:1-39
libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193 — StarterButtons
libs/starter-buttons/src/models/starter-props.ts:20-38 — StarterButtonsProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/components/StarterButtons/StarterButtons.tsx |
| Test evidence | collapses the starters that do not fit into an overflow menu by default |
| Test evidence | stamps the list and the wrapper around it |
08
Starter buttons
lib-starter-buttons-08

### Notes:
Slide ID: lib-starter-buttons-08

Actual consumers: apps/chat/src/components/StarterButtons/StarterButtons.tsx. Existing test evidence: [{"file": "libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.spec.tsx", "assertions": ["StarterButtons", "collapses the starters that do not fit into an overflow menu by default", "renders every starter and no overflow menu when collapsing is off"]}, {"file": "libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.classes.spec.tsx", "assertions": ["StarterButtons \u2014 public class names", "stamps the list and the wrapper around it", "keeps both classes in the non-collapsible layout"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-starter-buttons:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/starter-buttons/README.md:1-150
libs/starter-buttons/src/index.ts:1-7
libs/starter-buttons/package.json:1-39
libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193 — StarterButtons
libs/starter-buttons/src/models/starter-props.ts:20-38 — StarterButtonsProps
apps/chat/src/components/StarterButtons/StarterButtons.tsx:1-34
libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.spec.tsx:1-48
libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.classes.spec.tsx:1-64

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Use the actual shape
No completion side effect
Layout needs space
StarterOption includes const and dial:widgetOptions.
Selecting emits a value; the host controls submission.
Render inside the actual constrained input area.
09
Starter buttons
lib-starter-buttons-09

### Notes:
Slide ID: lib-starter-buttons-09

Review these constraints before choosing the library. Use the actual shape: StarterOption includes const and dial:widgetOptions. No completion side effect: Selecting emits a value; the host controls submission. Layout needs space: Render inside the actual constrained input area. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/starter-buttons/README.md:1-150
libs/starter-buttons/src/index.ts:1-7
libs/starter-buttons/package.json:1-39
libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193 — StarterButtons
libs/starter-buttons/src/models/starter-props.ts:20-38 — StarterButtonsProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.