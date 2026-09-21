<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Navigation panel
Reuse navigation destinations across desktop and mobile chrome.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-navigation-panel
01
Navigation panel
lib-navigation-panel-01

### Notes:
Slide ID: lib-navigation-panel-01

This session explains reuse navigation destinations across desktop and mobile chrome. The library is a local private workspace package at libs/navigation-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/navigation-panel/README.md:1-208
libs/navigation-panel/src/index.ts:1-54
libs/navigation-panel/package.json:1-40
libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111 — NavigationPanel
libs/navigation-panel/src/models/navigation-panel-props.ts:60-73 — NavigationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Reuse navigation destinations across desktop and mobile chrome.

01
02
03
Navigate an app
Use a phone
Declare settings once
Render a desktop destination rail.
Show destinations and settings inside a bottom sheet.
Share menu groups across rail menus and mobile pages.
02
Navigation panel
lib-navigation-panel-02

### Notes:
Slide ID: lib-navigation-panel-02

Start with a concrete caller need. Navigate an app: Render a desktop destination rail. Use a phone: Show destinations and settings inside a bottom sheet. Declare settings once: Share menu groups across rail menus and mobile pages. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/navigation-panel/README.md:1-208
libs/navigation-panel/src/index.ts:1-54
libs/navigation-panel/package.json:1-40
libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111 — NavigationPanel
libs/navigation-panel/src/models/navigation-panel-props.ts:60-73 — NavigationPanelProps

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
Host destinations
Navigation surface
render Link / callback
Host route

Items and active flags
Rail or sheet
Host-owned behavior
Selected destination
Library: Rail, user menu, mobile sheet and its local page stack.
03
Navigation panel
lib-navigation-panel-03

### Notes:
Slide ID: lib-navigation-panel-03

The library owns Rail, user menu, mobile sheet and its local page stack. The host owns Routes, authentication, active destination, labels and resolved brand assets.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/navigation-panel/README.md:1-208
libs/navigation-panel/src/index.ts:1-54
libs/navigation-panel/package.json:1-40
libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111 — NavigationPanel
libs/navigation-panel/src/models/navigation-panel-props.ts:60-73 — NavigationPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
NavigationPanel · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| items | NavigationPanelItem[] |
| labels | NavigationPanelLabels |
| renderLink (optional) | NavigationLinkRenderer |
| footer (optional) | ReactNode |
04
Navigation panel
lib-navigation-panel-04

### Notes:
Slide ID: lib-navigation-panel-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/navigation-panel/README.md:1-208
libs/navigation-panel/src/index.ts:1-54
libs/navigation-panel/package.json:1-40
libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111 — NavigationPanel
libs/navigation-panel/src/models/navigation-panel-props.ts:60-73 — NavigationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<NavigationPanel
  items={items}
  labels={{ ariaLabel: 'Demo navigation' }}
  renderLink={(item, children) => (
    <a href={item.id}>{children}</a>
  )}
/>
Full example: examples/navigation-panel.tsx · uses @epam/ai-dial-navigation-panel
05
Navigation panel
lib-navigation-panel-05

### Notes:
Slide ID: lib-navigation-panel-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/navigation-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Render a desktop destination rail. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/navigation-panel/README.md:1-208
libs/navigation-panel/src/index.ts:1-54
libs/navigation-panel/package.json:1-40
libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111 — NavigationPanel
libs/navigation-panel/src/models/navigation-panel-props.ts:60-73 — NavigationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep navigation panel focused on its public responsibility.

01
02
03
Prepare destinations
Render host links
Reflect navigation
The host supplies item ids, labels and active state.
Use renderLink to bind each item to the chosen router.
Update active state when the application route changes.
06
Navigation panel
lib-navigation-panel-06

### Notes:
Slide ID: lib-navigation-panel-06

Follow this concrete integration sequence. Prepare destinations: The host supplies item ids, labels and active state. Render host links: Use renderLink to bind each item to the chosen router. Reflect navigation: Update active state when the application route changes. The complete typed module in examples/navigation-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/navigation-panel/README.md:1-208
libs/navigation-panel/src/index.ts:1-54
libs/navigation-panel/package.json:1-40
libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111 — NavigationPanel
libs/navigation-panel/src/models/navigation-panel-props.ts:60-73 — NavigationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Router integration
Mobile stack
Shared menus
renderLink wraps destination children with the host link element.
Use the bottom sheet and its navigation hook for drill-down pages.
NavigationMenuGroup describes selectable settings options.
07
Navigation panel
lib-navigation-panel-07

### Notes:
Slide ID: lib-navigation-panel-07

Customization comes from the current exports and prop declarations. Router integration: renderLink wraps destination children with the host link element. Mobile stack: NavigableBottomSheet and useSheetNavigation manage drill-down pages. Shared menus: NavigationMenuGroup describes selectable settings options. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/navigation-panel/README.md:1-208
libs/navigation-panel/src/index.ts:1-54
libs/navigation-panel/package.json:1-40
libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111 — NavigationPanel
libs/navigation-panel/src/models/navigation-panel-props.ts:60-73 — NavigationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/components/Navigation/Navigation.tsx |
| Test evidence | renders the nav landmark with the given accessible name |
| Test evidence | labels the avatar trigger |
08
Navigation panel
lib-navigation-panel-08

### Notes:
Slide ID: lib-navigation-panel-08

Actual consumers: apps/chat/src/components/Navigation/Navigation.tsx; apps/chat/src/hooks/navigation/useNavigationMenuGroups.tsx; apps/chat/src/hooks/navigation/useNavigationItems.ts; apps/chat/src/hooks/navigation/useNavigationUserProfile.ts. Existing test evidence: [{"file": "libs/navigation-panel/src/components/NavigationPanel/tests/NavigationPanel.spec.tsx", "assertions": ["NavigationPanel", "renders the nav landmark with the given accessible name", "renders one labelled button per item", "marks only the active item with aria-current=", "wraps items in plain anchors carrying their href by default", "delegates link rendering to renderLink when provided", "renders the logo link when a logo is supplied", "omits the logo link when no logo is supplied", "renders the footer slot", "NavigationPanel \u2014 public class names", "stamps the rail and every item"]}, {"file": "libs/navigation-panel/src/components/UserMenu/tests/UserMenu.spec.tsx", "assertions": ["UserMenu", "labels the avatar trigger", "renders the avatar image when an image URL is supplied", "falls back to initials when no image URL is supplied", "reports a broken avatar image through onImageError", "renders each settings group with its options", "marks the applied option as the checked single choice of the menu", "applies an option through its onSelect callback", "skips groups that have no options", "calls onLogout when the log-out entry is clicked", "renders a settings entry when onSettings is provided", "does not render a settings entry when onSettings is omitted", "calls onSettings when the settings entry is clicked"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-navigation-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/navigation-panel/README.md:1-208
libs/navigation-panel/src/index.ts:1-54
libs/navigation-panel/package.json:1-40
libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111 — NavigationPanel
libs/navigation-panel/src/models/navigation-panel-props.ts:60-73 — NavigationPanelProps
apps/chat/src/components/Navigation/Navigation.tsx:1-129
libs/navigation-panel/src/components/NavigationPanel/tests/NavigationPanel.spec.tsx:1-143
libs/navigation-panel/src/components/UserMenu/tests/UserMenu.spec.tsx:1-245

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Responsive selection
No login system
Explicit logos
The host chooses which surface to render.
UserMenu displays supplied profile data and callbacks.
Resolve logo URLs before passing them into NavigationPanel.
09
Navigation panel
lib-navigation-panel-09

### Notes:
Slide ID: lib-navigation-panel-09

Review these constraints before choosing the library. Responsive selection: The host chooses which surface to render. No login system: UserMenu displays supplied profile data and callbacks. Explicit logos: Resolve logo URLs before passing them into NavigationPanel. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/navigation-panel/README.md:1-208
libs/navigation-panel/src/index.ts:1-54
libs/navigation-panel/package.json:1-40
libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111 — NavigationPanel
libs/navigation-panel/src/models/navigation-panel-props.ts:60-73 — NavigationPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.