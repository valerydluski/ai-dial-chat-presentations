<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Conversation panel
Navigate a large conversation history with a small visible list.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-conversation-panel
01
Conversation panel
lib-conversation-panel-01

### Notes:
Slide ID: lib-conversation-panel-01

This session explains navigate a large conversation history with a small visible list. The library is a local private workspace package at libs/conversation-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/conversation-panel/README.md:1-406
libs/conversation-panel/src/index.ts:1-28
libs/conversation-panel/package.json:1-41
libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507 — ConversationPanel
libs/conversation-panel/src/models/panel-props.ts:162-223 — ConversationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Navigate a large conversation history with a small visible list.

01
02
03
Resume work
Find context
Manage history
Select a conversation from a grouped history list.
Search titles and filter by source.
Expose rename, move, pin and transfer actions.
02
Conversation panel
lib-conversation-panel-02

### Notes:
Slide ID: lib-conversation-panel-02

Start with a concrete caller need. Resume work: Select a conversation from a grouped history list. Find context: Search titles and filter by source. Manage history: Expose rename, move, pin and transfer actions. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/conversation-panel/README.md:1-406
libs/conversation-panel/src/index.ts:1-28
libs/conversation-panel/package.json:1-41
libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507 — ConversationPanel
libs/conversation-panel/src/models/panel-props.ts:162-223 — ConversationPanelProps

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
Host history
Conversation Panel
Selection or move
Host state

Conversation Item[]
Grouped visible rows
Id or Conversation Move
Navigate and persist
Library: Windowed rows, grouping, search UI and per-row interaction.
03
Conversation panel
lib-conversation-panel-03

### Notes:
Slide ID: lib-conversation-panel-03

The library owns Windowed rows, grouping, search UI and per-row interaction. The host owns Ordered data, active route, storage changes and action implementations.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/conversation-panel/README.md:1-406
libs/conversation-panel/src/index.ts:1-28
libs/conversation-panel/package.json:1-41
libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507 — ConversationPanel
libs/conversation-panel/src/models/panel-props.ts:162-223 — ConversationPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
ConversationPanel · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| conversations | ConversationItem[] |
| onSelectConversation | (id: string) => void |
| onNewChat | () => void |
| labels | ConversationPanelLabels |
04
Conversation panel
lib-conversation-panel-04

### Notes:
Slide ID: lib-conversation-panel-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/conversation-panel/README.md:1-406
libs/conversation-panel/src/index.ts:1-28
libs/conversation-panel/package.json:1-41
libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507 — ConversationPanel
libs/conversation-panel/src/models/panel-props.ts:162-223 — ConversationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<ConversationPanel
  isOpen
  conversations={[{ id: 'demo', title: 'Demo chat' }]}
  activeConversationId={active}
  onSelectConversation={setActive}
  onNewChat={onNewChat}
  labels={labels}
/>
Full example: examples/conversation-panel.tsx · uses @epam/ai-dial-conversation-panel
05
Conversation panel
lib-conversation-panel-05

### Notes:
Slide ID: lib-conversation-panel-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/conversation-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Select a conversation from a grouped history list. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/conversation-panel/README.md:1-406
libs/conversation-panel/src/index.ts:1-28
libs/conversation-panel/package.json:1-41
libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507 — ConversationPanel
libs/conversation-panel/src/models/panel-props.ts:162-223 — ConversationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep conversation panel focused on its public responsibility.

01
02
03
Load summaries
Handle selection
Load the transcript
Supply conversation ids, titles and the active id.
Use onSelectConversation to choose a host-owned route.
The host loads messages for the selected conversation.
06
Conversation panel
lib-conversation-panel-06

### Notes:
Slide ID: lib-conversation-panel-06

Follow this concrete integration sequence. Load summaries: Supply conversation ids, titles and the active id. Handle selection: Use onSelectConversation to choose a host-owned route. Load the transcript: The host loads messages for the selected conversation. The complete typed module in examples/conversation-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/conversation-panel/README.md:1-406
libs/conversation-panel/src/index.ts:1-28
libs/conversation-panel/package.json:1-41
libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507 — ConversationPanel
libs/conversation-panel/src/models/panel-props.ts:162-223 — ConversationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Stable row data
Action extension
Transfer surfaces
Items carry title, source, pinned state and optional unread/task badges.
getActions and onActionMenuOpen inject row actions.
Transfer queues and rename dialogs are separate public components.
07
Conversation panel
lib-conversation-panel-07

### Notes:
Slide ID: lib-conversation-panel-07

Customization comes from the current exports and prop declarations. Stable row data: Items carry title, source, pinned state and optional unread/task badges. Action extension: getActions and onActionMenuOpen inject row actions. Transfer surfaces: ImportExportQueue and RenameConversationPopup are separate exports. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/conversation-panel/README.md:1-406
libs/conversation-panel/src/index.ts:1-28
libs/conversation-panel/package.json:1-41
libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507 — ConversationPanel
libs/conversation-panel/src/models/panel-props.ts:162-223 — ConversationPanelProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/components/ConversationPanel/ConversationPanelView.tsx |
| Test evidence | renders a tab for each filter |
| Test evidence | renders a skeleton when isIconLoading is true |
08
Conversation panel
lib-conversation-panel-08

### Notes:
Slide ID: lib-conversation-panel-08

Actual consumers: apps/chat/src/components/ConversationPanel/ConversationPanelView.tsx. Existing test evidence: [{"file": "libs/conversation-panel/src/components/FilterTabs/tests/FilterTabs.spec.tsx", "assertions": ["FilterTabs", "renders a tab for each filter", "marks only the active tab as pressed", "names the filter row so the group is announced", "applies flex-1 by default so the tabs fill the row equally", "applies the provided typography class to each tab", "omits a tab listed in hiddenSources"]}, {"file": "libs/conversation-panel/src/components/ConversationRow/tests/ConversationRow.spec.tsx", "assertions": ["ConversationRow", "renders a skeleton when isIconLoading is true", "skeleton has aria-hidden=", "skeleton is rendered with Circular variant at DIAL_ICON_SIZE.LG dimensions", "renders DeploymentIcon when isIconLoading is false and iconUrl is set", "renders DeploymentIcon when isIconLoading is omitted", "renders DeploymentIcon fallback when isIconLoading is false and iconUrl is absent", "exposes the action trigger when its menu opens", "renders the task badge when showTaskBadge is true", "does not render the task badge when showTaskBadge is omitted", "does not render the task badge when showTaskBadge is false", "marks the task badge icon as aria-hidden", "clicking the task badge selects the conversation like any other row click", "unread indicator", "renders the unread dot with an accessible label when isUnread is true"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-conversation-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/conversation-panel/README.md:1-406
libs/conversation-panel/src/index.ts:1-28
libs/conversation-panel/package.json:1-41
libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507 — ConversationPanel
libs/conversation-panel/src/models/panel-props.ts:162-223 — ConversationPanelProps
apps/chat/src/components/ConversationPanel/ConversationPanelView.tsx:1-1510
libs/conversation-panel/src/components/FilterTabs/tests/FilterTabs.spec.tsx:1-61
libs/conversation-panel/src/components/ConversationRow/tests/ConversationRow.spec.tsx:1-356

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Preserve ordering
Selection is not routing
Virtualized content
The host supplies an already-ordered flat list.
onSelectConversation returns an id for the host to interpret.
Only a subset of rows exists in the DOM at a time.
09
Conversation panel
lib-conversation-panel-09

### Notes:
Slide ID: lib-conversation-panel-09

Review these constraints before choosing the library. Preserve ordering: The host supplies an already-ordered flat list. Selection is not routing: onSelectConversation returns an id for the host to interpret. Virtualized content: Only a subset of rows exists in the DOM at a time. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/conversation-panel/README.md:1-406
libs/conversation-panel/src/index.ts:1-28
libs/conversation-panel/package.json:1-41
libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507 — ConversationPanel
libs/conversation-panel/src/models/panel-props.ts:162-223 — ConversationPanelProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.