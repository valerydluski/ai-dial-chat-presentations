<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Skills
Select a reusable skill without coupling the picker to sending.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-skills
01
Skills
lib-skills-01

### Notes:
Slide ID: lib-skills-01

This session explains select a reusable skill without coupling the picker to sending. The library is a local private workspace package at libs/skills. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/skills/README.md:1-378
libs/skills/src/index.ts:1-30
libs/skills/package.json:1-42
libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294 — FavoriteSkillsPanel
libs/skills/src/models/favorite-skills-panel-props.ts:34-62 — FavoriteSkillsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Select a reusable skill without coupling the picker to sending.

01
02
03
Choose a favorite
Inspect a skill
Attach context
Select a host-resolved favorite skill.
Open a host-backed detail panel.
Display a selected skill chip next to the composer.
02
Skills
lib-skills-02

### Notes:
Slide ID: lib-skills-02

Start with a concrete caller need. Choose a favorite: Select a host-resolved favorite skill. Inspect a skill: Open a host-backed detail panel. Attach context: Display a selected skill chip next to the composer. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/skills/README.md:1-378
libs/skills/src/index.ts:1-30
libs/skills/package.json:1-42
libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294 — FavoriteSkillsPanel
libs/skills/src/models/favorite-skills-panel-props.ts:34-62 — FavoriteSkillsPanelProps

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
Host listing
Skills picker
Selected skill
Host send

Favorite Skill Item[]
Select or inspect
Chip and detail state
Interpret the selection
Library: Favorite list, chip, details composition and selection-overlay state.
03
Skills
lib-skills-03

### Notes:
Slide ID: lib-skills-03

The library owns Favorite list, chip, details composition and selection-overlay state. The host owns Skill listing, favorites persistence, capability flag and send-time semantics.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/skills/README.md:1-378
libs/skills/src/index.ts:1-30
libs/skills/package.json:1-42
libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294 — FavoriteSkillsPanel
libs/skills/src/models/favorite-skills-panel-props.ts:34-62 — FavoriteSkillsPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
FavoriteSkillsPanel · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| favorites | FavoriteSkillItem[] |
| onSelect | (item: FavoriteSkillItem) => void |
| onViewDetails | (item: FavoriteSkillItem) => void |
| onBrowse | () => void |
04
Skills
lib-skills-04

### Notes:
Slide ID: lib-skills-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/skills/README.md:1-378
libs/skills/src/index.ts:1-30
libs/skills/package.json:1-42
libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294 — FavoriteSkillsPanel
libs/skills/src/models/favorite-skills-panel-props.ts:34-62 — FavoriteSkillsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<FavoriteSkillsPanel
  {...host}
  favorites={[{
    id: 'skills/demo/review',
    name: 'Demo review',
    description: 'Review demo content',
  }]}
/>
// host supplies select, favorite, browse and detail callbacks.
Full example: examples/skills.tsx · uses @epam/ai-dial-skills
05
Skills
lib-skills-05

### Notes:
Slide ID: lib-skills-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/skills.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Select a host-resolved favorite skill. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/skills/README.md:1-378
libs/skills/src/index.ts:1-30
libs/skills/package.json:1-42
libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294 — FavoriteSkillsPanel
libs/skills/src/models/favorite-skills-panel-props.ts:34-62 — FavoriteSkillsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep skills focused on its public responsibility.

01
02
03
Load favorites
Handle selection
Connect discovery
Supply favorite skill records and localized labels.
Use the selection callback to choose a skill in the host.
Browse and detail callbacks open host-owned surfaces.
06
Skills
lib-skills-06

### Notes:
Slide ID: lib-skills-06

Follow this concrete integration sequence. Load favorites: Supply favorite skill records and localized labels. Handle selection: Use the selection callback to choose a skill in the host. Connect discovery: Browse and detail callbacks open host-owned surfaces. The complete typed module in examples/skills.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/skills/README.md:1-378
libs/skills/src/index.ts:1-30
libs/skills/package.json:1-42
libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294 — FavoriteSkillsPanel
libs/skills/src/models/favorite-skills-panel-props.ts:34-62 — FavoriteSkillsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Overlay state hook
Capability input
Composable detail view
useSkillSelectorOverlay coordinates favorites, browse and details.
A plain support flag controls skill entry points.
SkillDetailsSidePanel uses the catalog DetailsPanel contract.
07
Skills
lib-skills-07

### Notes:
Slide ID: lib-skills-07

Customization comes from the current exports and prop declarations. Overlay state hook: useSkillSelectorOverlay coordinates favorites, browse and details. Capability input: A plain support flag controls skill entry points. Composable detail view: SkillDetailsSidePanel uses the catalog DetailsPanel contract. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/skills/README.md:1-378
libs/skills/src/index.ts:1-30
libs/skills/package.json:1-42
libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294 — FavoriteSkillsPanel
libs/skills/src/models/favorite-skills-panel-props.ts:34-62 — FavoriteSkillsPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/components/SkillSelector/useSkillSelectorOverlay.tsx |
| Test evidence | stamps the composer chip |
08
Skills
lib-skills-08

### Notes:
Slide ID: lib-skills-08

Actual consumers: apps/chat/src/components/SkillSelector/useSkillSelectorOverlay.tsx; apps/chat/src/components/SkillSelector/SkillDetailsPanelContainer.tsx. Existing test evidence: [{"file": "libs/skills/src/components/ChatSkill/tests/ChatSkill.classes.spec.tsx", "assertions": ["skills \u2014 public class names", "stamps the composer chip", "keeps the chip class in the unsupported state", "stamps the favorites panel root"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-skills:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/skills/README.md:1-378
libs/skills/src/index.ts:1-30
libs/skills/package.json:1-42
libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294 — FavoriteSkillsPanel
libs/skills/src/models/favorite-skills-panel-props.ts:34-62 — FavoriteSkillsPanelProps
apps/chat/src/components/SkillSelector/useSkillSelectorOverlay.tsx:1-120
libs/skills/src/components/ChatSkill/tests/ChatSkill.classes.spec.tsx:1-72

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Unsupported deployment
No automatic attachment
Keep identifiers intact
A selected chip can remain visible in its error state.
The host decides how a skill enters the request.
The favorite item id is the resource identifier supplied by the host.
09
Skills
lib-skills-09

### Notes:
Slide ID: lib-skills-09

Review these constraints before choosing the library. Unsupported deployment: A selected chip can remain visible in its error state. No automatic attachment: The host decides how a skill enters the request. Keep identifiers intact: The favorite item id is the resource identifier supplied by the host. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/skills/README.md:1-378
libs/skills/src/index.ts:1-30
libs/skills/package.json:1-42
libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294 — FavoriteSkillsPanel
libs/skills/src/models/favorite-skills-panel-props.ts:34-62 — FavoriteSkillsPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.