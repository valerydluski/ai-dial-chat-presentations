<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Publish panel
Reuse the publish-to-folder workflow across different entity types.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-publish-panel
01
Publish panel
lib-publish-panel-01

### Notes:
Slide ID: lib-publish-panel-01

This session explains reuse the publish-to-folder workflow across different entity types. The library is a local private workspace package at libs/publish-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/publish-panel/README.md:1-350
libs/publish-panel/src/index.ts:1-90
libs/publish-panel/package.json:1-44
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497 — PublishPanel
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193 — PublishPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Reuse the publish-to-folder workflow across different entity types.

01
02
03
Choose a destination
Explain history
Share one workflow
Search and select a publication folder.
Show earlier publications before replacing or versioning.
Use the same panel for deployments and conversations.
02
Publish panel
lib-publish-panel-02

### Notes:
Slide ID: lib-publish-panel-02

Start with a concrete caller need. Choose a destination: Search and select a publication folder. Explain history: Show earlier publications before replacing or versioning. Share one workflow: Use the same panel for deployments and conversations. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/publish-panel/README.md:1-350
libs/publish-panel/src/index.ts:1-90
libs/publish-panel/package.json:1-44
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497 — PublishPanel
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193 — PublishPanelProps

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
Host resources
Publish Panel
Flow callbacks
Host API

Folders and history
Destination and rules
Create folder / submit
Persist publication
Library: Folder/history UI and a generic publish-flow state helper.
03
Publish panel
lib-publish-panel-03

### Notes:
Slide ID: lib-publish-panel-03

The library owns Folder/history UI and a generic publish-flow state helper. The host owns Folder loading, write permissions, publish requests and domain-specific resource mapping.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/publish-panel/README.md:1-350
libs/publish-panel/src/index.ts:1-90
libs/publish-panel/package.json:1-44
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497 — PublishPanel
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193 — PublishPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
PublishPanel · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| folderItems | PublishFolderNode[] |
| onCreateFolder | (parentPath: string[], name: string) => Promise<void> |
| rules | PublicationRule[] |
| hasWriteAccess | boolean |
04
Publish panel
lib-publish-panel-04

### Notes:
Slide ID: lib-publish-panel-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/publish-panel/README.md:1-350
libs/publish-panel/src/index.ts:1-90
libs/publish-panel/package.json:1-44
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497 — PublishPanel
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193 — PublishPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function PublishDemo(
  host: Omit<PublishPanelProps, 'resource'>,
) {
  return <PublishPanel
    {...host}
    resource={{ title: 'Demo planning notes' }}
  />;
}
Full example: examples/publish-panel.tsx · uses @epam/ai-dial-publish-panel
05
Publish panel
lib-publish-panel-05

### Notes:
Slide ID: lib-publish-panel-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/publish-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Search and select a publication folder. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/publish-panel/README.md:1-350
libs/publish-panel/src/index.ts:1-90
libs/publish-panel/package.json:1-44
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497 — PublishPanel
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193 — PublishPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep publish panel focused on its public responsibility.

01
02
03
Prepare the resource
Collect the request
Publish through the host
Supply the resource title, labels and publication controls.
The panel gathers the publication choices.
Run the host callback and reflect its pending or error state.
06
Publish panel
lib-publish-panel-06

### Notes:
Slide ID: lib-publish-panel-06

Follow this concrete integration sequence. Prepare the resource: Supply the resource title, labels and publication controls. Collect the request: The panel gathers the publication choices. Publish through the host: Run the host callback and reflect its pending or error state. The complete typed module in examples/publish-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/publish-panel/README.md:1-350
libs/publish-panel/src/index.ts:1-90
libs/publish-panel/package.json:1-44
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497 — PublishPanel
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193 — PublishPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Generic summary
State helper
Access-rule controls
resource and renderSummary avoid requiring a catalog-specific model.
usePublishFlow coordinates selection and submission state.
Author, rules and rule-source options are explicit inputs.
07
Publish panel
lib-publish-panel-07

### Notes:
Slide ID: lib-publish-panel-07

Customization comes from the current exports and prop declarations. Generic summary: resource and renderSummary avoid requiring a catalog-specific model. State helper: usePublishFlow coordinates selection and submission state. Access-rule controls: Author, rules and rule-source options are explicit inputs. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/publish-panel/README.md:1-350
libs/publish-panel/src/index.ts:1-90
libs/publish-panel/package.json:1-44
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497 — PublishPanel
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193 — PublishPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat-hooks/src/conversation/deriveConversationRowActionState/deriveConversationRowActionState.ts |
| Test evidence | converts folder nodes into a rooted, folder-only file-manager tree |
| Test evidence | renders the empty-state message when there are no entries |
08
Publish panel
lib-publish-panel-08

### Notes:
Slide ID: lib-publish-panel-08

Actual consumers: libs/chat-hooks/src/conversation/deriveConversationRowActionState/deriveConversationRowActionState.ts; libs/chat-hooks/src/catalog/usePublishFolders/usePublishFolders.ts; libs/chat-hooks/src/catalog/create-publish-api.ts; apps/chat/src/hooks/useConversationPublishHistory/useConversationPublishHistory.ts; libs/chat-hooks/src/catalog/publish.ts; apps/chat/src/hooks/useCatalogPublishing/useCatalogPublishing.ts. Existing test evidence: [{"file": "libs/publish-panel/src/components/PublishFoldersTree/tests/PublishFoldersTree.spec.tsx", "assertions": ["PublishFoldersTree", "converts PublishFolderNode[] to DialFile[] with showFiles disabled, wrapped under the root node", "orders folders by name at every level, regardless of the order given", "passes the selected path joined as a string", "selects a folder when clicked", "deselects (undefined) when clicking the already-selected folder", "filters the tree to matching folders when searchQuery is set", "passes a no-results empty state title when search matches nothing, and omits the root node", "creating a folder from a search that matched nothing", "renders the tree with the inline create row instead of the empty state", "pre-fills the new folder name with the unmatched query", "falls back to the default name when the query is not a valid folder name", "keeps the default name when the query did match a folder", "creates the folder under the selected parent and selects it", "restores the filtered empty state when creation is cancelled"]}, {"file": "libs/publish-panel/src/components/PublishHistoryList/tests/PublishHistoryList.spec.tsx", "assertions": ["PublishHistoryList", "renders the empty-state message when there are no entries", "renders a row for each history entry", "marks an entry that carried shared credentials", "uses the host-supplied shared-credentials label", "leaves an entry without the flag unmarked", "renders a relative date within the last week", "renders an exact date once older than a week", "does not render the destination folder path, since this list is already scoped to it", "uses the versionPrefix override", "renders no dividers between rows, using zebra striping instead (matching the Overview tab grid)"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-publish-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: converts folder nodes into a rooted, folder-only file-manager tree.

Sources:
libs/publish-panel/README.md:1-350
libs/publish-panel/src/index.ts:1-90
libs/publish-panel/package.json:1-44
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497 — PublishPanel
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193 — PublishPanelProps
libs/chat-hooks/src/conversation/deriveConversationRowActionState/deriveConversationRowActionState.ts:1-79
libs/publish-panel/src/components/PublishFoldersTree/tests/PublishFoldersTree.spec.tsx:1-503
libs/publish-panel/src/components/PublishHistoryList/tests/PublishHistoryList.spec.tsx:1-97

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Permission truth
Folder mutations
Version semantics
hasWriteAccess must come from a host authorization decision.
onCreateFolder is asynchronous and can fail.
The host decides whether replacement or a new version is appropriate.
09
Publish panel
lib-publish-panel-09

### Notes:
Slide ID: lib-publish-panel-09

Review these constraints before choosing the library. Permission truth: hasWriteAccess must come from a host authorization decision. Folder mutations: onCreateFolder is asynchronous and can fail. Version semantics: The host decides whether replacement or a new version is appropriate. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/publish-panel/README.md:1-350
libs/publish-panel/src/index.ts:1-90
libs/publish-panel/package.json:1-44
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497 — PublishPanel
libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193 — PublishPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.