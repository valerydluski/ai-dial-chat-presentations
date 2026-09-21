<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Scheduled tasks
Render task lists, forms and run history from host-owned schedules.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-scheduled-tasks
01
Scheduled tasks
lib-scheduled-tasks-01

### Notes:
Slide ID: lib-scheduled-tasks-01

This session explains render task lists, forms and run history from host-owned schedules. The library is a local private workspace package at libs/scheduled-tasks. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/scheduled-tasks/README.md:1-215
libs/scheduled-tasks/src/index.ts:1-68
libs/scheduled-tasks/package.json:1-42
libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350 — ScheduledTasks
libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110 — ScheduledTasksProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Render task lists, forms and run history from host-owned schedules.

01
02
03
Browse automation
Create or edit
Inspect execution
Search and sort scheduled task cards.
Collect schedule form values and validation errors.
Display a task summary and past run statuses.
02
Scheduled tasks
lib-scheduled-tasks-02

### Notes:
Slide ID: lib-scheduled-tasks-02

Start with a concrete caller need. Browse automation: Search and sort scheduled task cards. Create or edit: Collect schedule form values and validation errors. Inspect execution: Display a task summary and past run statuses. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/scheduled-tasks/README.md:1-215
libs/scheduled-tasks/src/index.ts:1-68
libs/scheduled-tasks/package.json:1-42
libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350 — ScheduledTasks
libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110 — ScheduledTasksProps

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
Host task adapter
Scheduled Tasks
Search / sort callback
Host update

Preformatted items
Cards and toolbar
Query or enum
Derive next item set
Library: List/form/detail UI and user interactions.
03
Scheduled tasks
lib-scheduled-tasks-03

### Notes:
Slide ID: lib-scheduled-tasks-03

The library owns List/form/detail UI and user interactions. The host owns Scheduling APIs, formatted dates, timezone decisions, sorting/filtering and validation.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/scheduled-tasks/README.md:1-215
libs/scheduled-tasks/src/index.ts:1-68
libs/scheduled-tasks/package.json:1-42
libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350 — ScheduledTasks
libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110 — ScheduledTasksProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
ScheduledTasks · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| items | ScheduledTaskItem[] |
| searchQuery | string |
| sortKey | ScheduledTasksSortKey |
| labels | ScheduledTasksLabels |
04
Scheduled tasks
lib-scheduled-tasks-04

### Notes:
Slide ID: lib-scheduled-tasks-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/scheduled-tasks/README.md:1-215
libs/scheduled-tasks/src/index.ts:1-68
libs/scheduled-tasks/package.json:1-42
libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350 — ScheduledTasks
libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110 — ScheduledTasksProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

const [query, setQuery] = useState('');
const [sort, setSort] = useState(
  ScheduledTasksSortKey.FirstToRun,
);
<ScheduledTasks
  {...host}
  searchQuery={query} onSearchQueryChange={setQuery}
  sortKey={sort} onSortChange={setSort}
/>
// host supplies items, labels and onCreateClick.
Full example: examples/scheduled-tasks.tsx · uses @epam/ai-dial-scheduled-tasks
05
Scheduled tasks
lib-scheduled-tasks-05

### Notes:
Slide ID: lib-scheduled-tasks-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/scheduled-tasks.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Search and sort scheduled task cards. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/scheduled-tasks/README.md:1-215
libs/scheduled-tasks/src/index.ts:1-68
libs/scheduled-tasks/package.json:1-42
libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350 — ScheduledTasks
libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110 — ScheduledTasksProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep scheduled tasks focused on its public responsibility.

01
02
03
Load task records
Control the view
Handle a task action
The host supplies task items, labels and action callbacks.
Manage the search query and sort key in the host.
Use the host adapter to create or update task data.
06
Scheduled tasks
lib-scheduled-tasks-06

### Notes:
Slide ID: lib-scheduled-tasks-06

Follow this concrete integration sequence. Load task records: The host supplies task items, labels and action callbacks. Control the view: Manage the search query and sort key in the host. Handle a task action: Use the host adapter to create or update task data. The complete typed module in examples/scheduled-tasks.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/scheduled-tasks/README.md:1-215
libs/scheduled-tasks/src/index.ts:1-68
libs/scheduled-tasks/package.json:1-42
libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350 — ScheduledTasks
libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110 — ScheduledTasksProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
List pagination
Form and detail exports
Run status display
hasMore, isLoadingMore and onLoadMore support incremental loading.
Create forms and task detail views are distinct public components.
The run-history list renders records supplied by the host.
07
Scheduled tasks
lib-scheduled-tasks-07

### Notes:
Slide ID: lib-scheduled-tasks-07

Customization comes from the current exports and prop declarations. List pagination: hasMore, isLoadingMore and onLoadMore support incremental loading. Form and detail exports: ScheduledTaskCreateForm and ScheduledTaskDetailView are distinct surfaces. Run status display: ScheduledTaskRunHistoryList renders host-provided run records. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/scheduled-tasks/README.md:1-215
libs/scheduled-tasks/src/index.ts:1-68
libs/scheduled-tasks/package.json:1-42
libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350 — ScheduledTasks
libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110 — ScheduledTasksProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/pages/ScheduledTaskDetailPage/ScheduledTaskDetailPage.tsx |
| Test evidence | highlights the matching substring of the title |
| Test evidence | renders the resolved model display name |
08
Scheduled tasks
lib-scheduled-tasks-08

### Notes:
Slide ID: lib-scheduled-tasks-08

Actual consumers: apps/chat/src/pages/ScheduledTaskDetailPage/ScheduledTaskDetailPage.tsx; apps/chat/src/pages/ScheduledTaskEditPage/ScheduledTaskEditPage.tsx; apps/chat/src/hooks/scheduled-tasks/useScheduledTasks.ts; apps/chat/src/pages/ScheduledTasksPage/ScheduledTasksPage.tsx; apps/chat/src/pages/ScheduledTaskCreatePage/ScheduledTaskCreatePage.tsx; apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx. Existing test evidence: [{"file": "libs/scheduled-tasks/src/components/ScheduledTaskCard/tests/ScheduledTaskCard.spec.tsx", "assertions": ["ScheduledTaskCard", "highlights the matching substring of the title", "renders the schedule pill and location breadcrumb verbatim", "renders no interactive control when onCardClick is omitted", "renders the ", "renders the card with a fixed height", "clamps a long description instead of growing the card", "invokes onCardClick with the item id when the card body is clicked", "invokes onCardClick on Enter/Space keyboard activation", "renders no added interactive semantics when onCardClick is omitted", "renders the ", "renders the schedule pill when isActive is true or omitted", "pins the schedule pill to the bottom of the card regardless of description length", "ScheduledTaskCard \u2014 public class names", "stamps the card whether or not it is clickable"]}, {"file": "libs/scheduled-tasks/src/components/ScheduledTaskDetailsSummary/tests/ScheduledTaskDetailsSummary.spec.tsx", "assertions": ["ScheduledTaskDetailsSummary", "renders the resolved model display name", "renders the raw model id when no display name is resolved but one is supplied as the value", "hides the model field entirely when modelDisplayName is omitted", "renders instructions markdown via the injected renderInstructions callback", "falls back to MDMessageViewer when renderInstructions is not supplied", "renders no edit affordance"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-scheduled-tasks:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/scheduled-tasks/README.md:1-215
libs/scheduled-tasks/src/index.ts:1-68
libs/scheduled-tasks/package.json:1-42
libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350 — ScheduledTasks
libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110 — ScheduledTasksProps
apps/chat/src/pages/ScheduledTaskDetailPage/ScheduledTaskDetailPage.tsx:1-413
libs/scheduled-tasks/src/components/ScheduledTaskCard/tests/ScheduledTaskCard.spec.tsx:1-201
libs/scheduled-tasks/src/components/ScheduledTaskDetailsSummary/tests/ScheduledTaskDetailsSummary.spec.tsx:1-89

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
No task scheduler
Formatting stays outside
Filter intentionally
Rendering a schedule does not execute work in the background.
Pass already-formatted labels and timestamps.
The controlled search/sort contract requires host updates.
09
Scheduled tasks
lib-scheduled-tasks-09

### Notes:
Slide ID: lib-scheduled-tasks-09

Review these constraints before choosing the library. No task scheduler: Rendering a schedule does not execute work in the background. Formatting stays outside: Pass already-formatted labels and timestamps. Filter intentionally: The controlled search/sort contract requires host updates. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/scheduled-tasks/README.md:1-215
libs/scheduled-tasks/src/index.ts:1-68
libs/scheduled-tasks/package.json:1-42
libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350 — ScheduledTasks
libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110 — ScheduledTasksProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.