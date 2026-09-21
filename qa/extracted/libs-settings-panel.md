<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Settings panel
Provide accessible vertical selection for settings pages.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-settings-panel
01
Settings panel
lib-settings-panel-01

### Notes:
Slide ID: lib-settings-panel-01

This session explains provide accessible vertical selection for settings pages. The library is a local private workspace package at libs/settings-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/settings-panel/README.md:1-115
libs/settings-panel/src/index.ts:1-9
libs/settings-panel/package.json:1-37
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170 — SettingsPanel
libs/settings-panel/src/models/settings-panel-props.ts:52-65 — SettingsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Provide accessible vertical selection for settings pages.

01
02
03
Switch settings
Use a keyboard
Keep one selection
Render a compact navigation list beside host content.
Move among enabled rows with arrows, Home and End.
The host controls activeId.
02
Settings panel
lib-settings-panel-02

### Notes:
Slide ID: lib-settings-panel-02

Start with a concrete caller need. Switch settings: Render a compact navigation list beside host content. Use a keyboard: Move among enabled rows with arrows, Home and End. Keep one selection: The host controls activeId. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/settings-panel/README.md:1-115
libs/settings-panel/src/index.ts:1-9
libs/settings-panel/package.json:1-37
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170 — SettingsPanel
libs/settings-panel/src/models/settings-panel-props.ts:52-65 — SettingsPanelProps

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
Host items
Settings Panel
on Select
Host content

Ids and labels
Roving focus
Selected id
Show the matching tab
Library: Vertical tab interactions, focus movement and selected styling.
03
Settings panel
lib-settings-panel-03

### Notes:
Slide ID: lib-settings-panel-03

The library owns Vertical tab interactions, focus movement and selected styling. The host owns Settings content, active state, item labels and navigation effects.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/settings-panel/README.md:1-115
libs/settings-panel/src/index.ts:1-9
libs/settings-panel/package.json:1-37
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170 — SettingsPanel
libs/settings-panel/src/models/settings-panel-props.ts:52-65 — SettingsPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
SettingsPanel · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| items | SettingsPanelItem[] |
| activeId | string |
| onSelect | (id: string) => void |
| sectionLabel (optional) | string |
04
Settings panel
lib-settings-panel-04

### Notes:
Slide ID: lib-settings-panel-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/settings-panel/README.md:1-115
libs/settings-panel/src/index.ts:1-9
libs/settings-panel/package.json:1-37
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170 — SettingsPanel
libs/settings-panel/src/models/settings-panel-props.ts:52-65 — SettingsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function SettingsDemo() {
  const [activeId, setActiveId] = useState('usage');
  return <SettingsPanel sectionLabel="Demo settings" activeId={activeId}
    onSelect={setActiveId} items={[
      { id: 'usage', label: 'Usage' }, { id: 'profile', label: 'Profile' },
    ]} />;
}
Full example: examples/settings-panel.tsx · uses @epam/ai-dial-settings-panel
05
Settings panel
lib-settings-panel-05

### Notes:
Slide ID: lib-settings-panel-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/settings-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Render a compact navigation list beside host content. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/settings-panel/README.md:1-115
libs/settings-panel/src/index.ts:1-9
libs/settings-panel/package.json:1-37
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170 — SettingsPanel
libs/settings-panel/src/models/settings-panel-props.ts:52-65 — SettingsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
See controlled selection in the browser
Reproducible demo · actual workspace source components

![assets/component-demo.png](Image1.jpg)

Host-owned choice
The host passes activeId and updates it through onSelect. Selecting Profile changes the highlighted row.
DEMO · real components rendered from this source snapshot
06
Settings panel
lib-settings-panel-10

### Notes:
Slide ID: lib-settings-panel-10

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
Keep settings panel focused on its public responsibility.

01
02
03
Choose the active item
Handle selection
Show the chosen view
Map application state to the panel’s activeId.
onSelect returns the chosen item id to the host.
The host renders the matching settings content beside it.
07
Settings panel
lib-settings-panel-06

### Notes:
Slide ID: lib-settings-panel-06

Follow this concrete integration sequence. Choose the active item: Map application state to the panel’s activeId. Handle selection: onSelect returns the chosen item id to the host. Show the chosen view: The host renders the matching settings content beside it. The complete typed module in examples/settings-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/settings-panel/README.md:1-115
libs/settings-panel/src/index.ts:1-9
libs/settings-panel/package.json:1-37
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170 — SettingsPanel
libs/settings-panel/src/models/settings-panel-props.ts:52-65 — SettingsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Disabled rows
Automatic activation
Single item state
Keyboard navigation skips disabled items.
Focus movement also invokes selection.
One selected row uses a neutral visual treatment.
08
Settings panel
lib-settings-panel-07

### Notes:
Slide ID: lib-settings-panel-07

Customization comes from the current exports and prop declarations. Disabled rows: Keyboard navigation skips disabled items. Automatic activation: Focus movement also invokes selection. Single item state: One selected row uses a neutral visual treatment. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/settings-panel/README.md:1-115
libs/settings-panel/src/index.ts:1-9
libs/settings-panel/package.json:1-37
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170 — SettingsPanel
libs/settings-panel/src/models/settings-panel-props.ts:52-65 — SettingsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/pages/SettingsPage/SettingsPage.tsx |
| Test evidence | renders one tab per item |
09
Settings panel
lib-settings-panel-08

### Notes:
Slide ID: lib-settings-panel-08

Actual consumers: apps/chat/src/pages/SettingsPage/SettingsPage.tsx; apps/chat/src/hooks/useSettingsTabConfig.tsx. Existing test evidence: [{"file": "libs/settings-panel/src/components/SettingsPanel/tests/SettingsPanel.spec.tsx", "assertions": ["SettingsPanel", "renders one tab per item", "marks the active item as selected", "calls onSelect when an enabled, inactive row is clicked", "does not call onSelect when a disabled row is clicked", "only the active row is in the tab order", "ArrowDown skips a disabled row", "ArrowDown wraps from the last enabled row to the first", "ArrowUp skips a disabled row and wraps at the start", "Home jumps to the first enabled row", "End jumps to the last enabled row", "renders the section label when provided", "renders no section label by default", "applies a custom row focus outline color", "SettingsPanel \u2014 public class names"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-settings-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/settings-panel/README.md:1-115
libs/settings-panel/src/index.ts:1-9
libs/settings-panel/package.json:1-37
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170 — SettingsPanel
libs/settings-panel/src/models/settings-panel-props.ts:52-65 — SettingsPanelProps
apps/chat/src/pages/SettingsPage/SettingsPage.tsx:1-35
libs/settings-panel/src/components/SettingsPanel/tests/SettingsPanel.spec.tsx:1-225

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Panel content is external
Keep ids coherent
No route knowledge
Selection does not create or load a settings page.
activeId must correspond to the intended item.
A route change is the host onSelect implementation.
10
Settings panel
lib-settings-panel-09

### Notes:
Slide ID: lib-settings-panel-09

Review these constraints before choosing the library. Panel content is external: Selection does not create or load a settings page. Keep ids coherent: activeId must correspond to the intended item. No route knowledge: A route change is the host onSelect implementation. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/settings-panel/README.md:1-115
libs/settings-panel/src/index.ts:1-9
libs/settings-panel/package.json:1-37
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170 — SettingsPanel
libs/settings-panel/src/models/settings-panel-props.ts:52-65 — SettingsPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.