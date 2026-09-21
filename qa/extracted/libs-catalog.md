<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Catalog
Browse deployments and reusable assets without owning their storage.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-catalog
01
Catalog
lib-catalog-01

### Notes:
Slide ID: lib-catalog-01

This session explains browse deployments and reusable assets without owning their storage. The library is a local private workspace package at libs/catalog. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Browse deployments and reusable assets without owning their storage.

01
02
03
Find a deployment
Inspect details
Act on a selection
Search, filter and compare models or applications.
Show capabilities, tools, pricing and limits.
Pick, favorite, share or publish through host callbacks.
02
Catalog
lib-catalog-02

### Notes:
Slide ID: lib-catalog-02

Start with a concrete caller need. Find a deployment: Search, filter and compare models or applications. Inspect details: Show capabilities, tools, pricing and limits. Act on a selection: Pick, favorite, share or publish through host callbacks. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps

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
Host adapter
Catalog
Detail request
Host action

Catalog Item[]
Grid or list
Item and selected tab
Use, share or publish
Library: Catalog display, search/filter interactions and composed detail surfaces.
03
Catalog
lib-catalog-03

### Notes:
Slide ID: lib-catalog-03

The library owns Catalog display, search/filter interactions and composed detail surfaces. The host owns Data loading, action permissions, routes, configured API clients and deployment mapping.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
Catalog · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| items | CatalogItem[] |
| favorites | CatalogItem[] |
| onUseInChat (optional) | ((item: CatalogItem) => void) |
| onToggleFavorite (optional) | ((id: string, isStarred: boolean) => void) |
04
Catalog
lib-catalog-04

### Notes:
Slide ID: lib-catalog-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function CatalogDemo({ items, onPick }: {
  items: CatalogItem[]; onPick: (item: CatalogItem) => void;
}) {
  return <Catalog items={items} favorites={[]}
    onUseInChat={onPick} isFavoriteVisible={() => false} />;
}
Full example: examples/catalog.tsx · uses @epam/ai-dial-catalog
05
Catalog
lib-catalog-05

### Notes:
Slide ID: lib-catalog-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/catalog.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Search, filter and compare models or applications. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep catalog focused on its public responsibility.

01
02
03
Prepare catalog items
Connect item actions
Reflect host state
Load deployment data and map it to CatalogItem records.
Supply use, favorite and detail callbacks for the workflow.
Pass updated favorites and item data back to the catalog.
06
Catalog
lib-catalog-06

### Notes:
Slide ID: lib-catalog-06

Follow this concrete integration sequence. Prepare catalog items: Load deployment data and map it to CatalogItem records. Connect item actions: Supply use, favorite and detail callbacks for the workflow. Reflect host state: Pass updated favorites and item data back to the catalog. The complete typed module in examples/catalog.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Choose the headless entry
Mapping consumers can avoid the full catalog UI.

import { filterCatalogItems, CredentialsLevel }
  from '@epam/ai-dial-catalog/mapping';

const matches = filterCatalogItems(items, 'demo');
const level = CredentialsLevel.User;
Focused source-backed example · see examples/ and content/api-index.md.
07
Catalog
lib-catalog-10

### Notes:
Slide ID: lib-catalog-10

This is an import-only example of a genuine public subpath. Function declarations and tests are indexed under src/entry-points/mapping.ts; argument shapes are in the API appendix. The complete module examples/catalog.tsx includes typed input and both exports. filterCatalogItems matches the trimmed query against name, case-insensitively; it does not match description. An empty query returns all items.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps
libs/catalog/src/utils/catalog-filter.ts:37-56

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Two view modes
Headless subpath
Action policies
Card and list views window visible rows.
The /mapping entry exposes catalog mapping helpers and enums.
Callbacks and visibility predicates control available item actions.
08
Catalog
lib-catalog-07

### Notes:
Slide ID: lib-catalog-07

Customization comes from the current exports and prop declarations. Two view modes: Card and list views window visible rows. Headless subpath: The /mapping entry exposes catalog mapping helpers and enums. Action policies: Callbacks and visibility predicates control available item actions. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | skills/src/components/SkillDetailsSidePanel/SkillDetailsSidePanel.tsx |
| Test evidence | renders the My checkbox |
| Test evidence | does not show a selected border or checkmark by default |
09
Catalog
lib-catalog-08

### Notes:
Slide ID: lib-catalog-08

Actual consumers: libs/skills/src/components/SkillDetailsSidePanel/SkillDetailsSidePanel.tsx; libs/skills/src/models/skill-details-side-panel-props.ts; apps/chat/src/pages/AppsEditor/GeneralForm.tsx; apps/chat/src/pages/AppsEditor/AppEditorIframe.tsx; apps/chat/src/hooks/useCatalogSortFilterPreference/useCatalogSortFilterPreference.ts; apps/chat/src/hooks/useCatalogItems/useCatalogItems.ts. Existing test evidence: [{"file": "libs/catalog/src/components/Filter/tests/Filter.spec.tsx", "assertions": ["Filter", "renders the My checkbox", "renders topic checkboxes alphabetically when values are provided", "does not render Topics section when values is undefined", "calls onChange with topic added when an unchecked topic is clicked", "calls onChange with topic removed when a checked topic is clicked", "shows myAppsLabel as button label when only My Apps is active", "shows topic count label when only topics are active", "shows combined label when both My Apps and topics are active", "applies active CSS class to trigger when any filter is on", "does not apply active CSS class when no filter is on", "renders the Apply button"]}, {"file": "libs/catalog/src/components/CardGrid/tests/Card.spec.tsx", "assertions": ["Card \u2014 selected state", "does not show a selected border or checkmark by default", "shows the selected border, tint, and checkmark when isSelected is true", "Card \u2014 long version", "caps the version at 30% of the row so it cannot overlap the name", "lets the name truncate instead of being pushed out", "Card \u2014 favorite visibility", "renders the star button for every entity type, prompts included", "hides the star button and keeps the item non-favoritable when isFavoriteVisible returns false", "renders the star button when isFavoriteVisible returns true", "Card \u2014 favorite revert", "resyncs the star to initialIsStarred when it reverts after a failed toggle", "Card \u2014 credentials badge", "shows the logged-out warning icon for a signed-out toolset, for both API_KEY and OAUTH", "shows no warning icon when signed in or when authenticationType is NONE"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-catalog:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps
libs/skills/src/components/SkillDetailsSidePanel/SkillDetailsSidePanel.tsx:1-13
libs/catalog/src/components/Filter/tests/Filter.spec.tsx:1-190
libs/catalog/src/components/CardGrid/tests/Card.spec.tsx:1-306

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Large prop surface
Dependency boundary
Source beats old docs
Configure the actions required by the host workflow.
The implementation uses the UI Kit grid and catalog/publish composition.
Do not copy the README peer list without checking package.json.
10
Catalog
lib-catalog-09

### Notes:
Slide ID: lib-catalog-09

Review these constraints before choosing the library. Large prop surface: Configure the actions required by the host workflow. Dependency boundary: The implementation uses the UI Kit grid and catalog/publish composition. Source beats old docs: Do not copy the README peer list without checking package.json. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/catalog/README.md:1-973
libs/catalog/src/index.ts:1-157
libs/catalog/package.json:1-51
libs/catalog/src/components/Catalog/Catalog.tsx:57-778 — Catalog
libs/catalog/src/models/catalog-props.ts:89-462 — CatalogProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.