<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Usage dashboard
Explain cost and model limits using normalized display data.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-usage-dashboard
01
Usage dashboard
lib-usage-dashboard-01

### Notes:
Slide ID: lib-usage-dashboard-01

This session explains explain cost and model limits using normalized display data. The library is a local private workspace package at libs/usage-dashboard. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/usage-dashboard/README.md:1-425
libs/usage-dashboard/src/index.ts:1-43
libs/usage-dashboard/package.json:1-42
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191 — UsageLimitCard
libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152 — UsageLimitCardProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Explain cost and model limits using normalized display data.

01
02
03
Inspect a budget
Compare periods
Find constraints
Display used, remaining and total amounts.
Show the current UTC day, week and month.
Compare model-token and overall cost limit statuses.
02
Usage dashboard
lib-usage-dashboard-02

### Notes:
Slide ID: lib-usage-dashboard-02

Start with a concrete caller need. Inspect a budget: Display used, remaining and total amounts. Compare periods: Show the current UTC day, week and month. Find constraints: Compare model-token and overall cost limit statuses. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/usage-dashboard/README.md:1-425
libs/usage-dashboard/src/index.ts:1-43
libs/usage-dashboard/package.json:1-42
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191 — UsageLimitCard
libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152 — UsageLimitCardProps

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
Host usage API
Mapping helpers
Usage dashboard
User review

Raw counters and limits
Display rows and labels
Cards and model table
Understand active limits
Library: Usage cards/tables plus exported mapping utilities.
03
Usage dashboard
lib-usage-dashboard-03

### Notes:
Slide ID: lib-usage-dashboard-03

The library owns Usage cards/tables plus exported mapping utilities. The host owns Fetching usage, choosing locale/timezone formatting and passing resolved display values.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/usage-dashboard/README.md:1-425
libs/usage-dashboard/src/index.ts:1-43
libs/usage-dashboard/package.json:1-42
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191 — UsageLimitCard
libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152 — UsageLimitCardProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
UsageLimitCard · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| data | UsageLimitCardData |
| labels | UsageLimitCardGroupLabels |
| styles (optional) | UsageLimitCardGroupStyles |
04
Usage dashboard
lib-usage-dashboard-04

### Notes:
Slide ID: lib-usage-dashboard-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/usage-dashboard/README.md:1-425
libs/usage-dashboard/src/index.ts:1-43
libs/usage-dashboard/package.json:1-42
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191 — UsageLimitCard
libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152 — UsageLimitCardProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<UsageLimitCard labels={labels} data={{
  title: 'Today', periodDescription: 'Today',
  used: 3, total: 10,
  usedLabel: '$3', totalLabel: '$10',
  remainingLabel: '$7', usedPercent: 30,
  status: UsageLimitStatus.Default,
  progressAriaLabel: 'Demo: 3 of 10, 30 percent used',
}} />
Full example: examples/usage-dashboard.tsx · uses @epam/ai-dial-usage-dashboard
05
Usage dashboard
lib-usage-dashboard-05

### Notes:
Slide ID: lib-usage-dashboard-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/usage-dashboard.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Display used, remaining and total amounts. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/usage-dashboard/README.md:1-425
libs/usage-dashboard/src/index.ts:1-43
libs/usage-dashboard/package.json:1-42
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191 — UsageLimitCard
libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152 — UsageLimitCardProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
See preformatted usage data in context
Reproducible demo · actual workspace source components

![assets/component-demo.png](Image1.jpg)

Host-owned values
The host supplies $3 used, a $10 limit, 30% and a status. The card presents these demo values.
DEMO · real components rendered from this source snapshot
06
Usage dashboard
lib-usage-dashboard-10

### Notes:
Slide ID: lib-usage-dashboard-10

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
Keep usage dashboard focused on its public responsibility.

01
02
03
Prepare usage data
Format the values
Render the summary
The host maps raw usage to the card’s normalized data.
Supply amount labels, percentage, status and optional reset text.
The card presents the values and accessible progress text.
07
Usage dashboard
lib-usage-dashboard-06

### Notes:
Slide ID: lib-usage-dashboard-06

Follow this concrete integration sequence. Prepare usage data: The host maps raw usage to the card’s normalized data. Format the values: Supply amount labels, percentage, status and optional reset text. Render the summary: The card presents the values and accessible progress text. The complete typed module in examples/usage-dashboard.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/usage-dashboard/README.md:1-425
libs/usage-dashboard/src/index.ts:1-43
libs/usage-dashboard/package.json:1-42
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191 — UsageLimitCard
libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152 — UsageLimitCardProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Semantic states
Accessible progress
Mapping exports
UsageLimitStatus distinguishes normal, warning and reached states.
Supply preformatted progressAriaLabel and reset text.
Usage-to-dashboard and model-limit mapping helpers are public exports.
08
Usage dashboard
lib-usage-dashboard-07

### Notes:
Slide ID: lib-usage-dashboard-07

Customization comes from the current exports and prop declarations. Semantic states: UsageLimitStatus distinguishes normal, warning and reached states. Accessible progress: Supply preformatted progressAriaLabel and reset text. Mapping exports: mapUsageDataToDashboard and model-limit mappers are public. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/usage-dashboard/README.md:1-425
libs/usage-dashboard/src/index.ts:1-43
libs/usage-dashboard/package.json:1-42
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191 — UsageLimitCard
libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152 — UsageLimitCardProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/pages/SettingsPage/UsageTab/UsageTab.tsx |
| Test evidence | renders the title, used amount and "used of" caption |
| Test evidence | renders the row count separately in the section heading |
09
Usage dashboard
lib-usage-dashboard-08

### Notes:
Slide ID: lib-usage-dashboard-08

Actual consumers: apps/chat/src/pages/SettingsPage/UsageTab/UsageTab.tsx; apps/chat/src/utils/usage-reset-time.ts. Existing test evidence: [{"file": "libs/usage-dashboard/src/components/UsageLimitCard/tests/UsageLimitCard.spec.tsx", "assertions": ["UsageLimitCard", "renders the title and the prominent used amount with its ", "renders the ", "renders the running-low badge and warning accent at 90% used", "renders the limit-reached badge and error accent at 100% used", "renders the remaining-amount and used-percent captions below the progress bar", "shows only the used amount, with no progress bar, ratio, or badge, when unlimited", "clamps the visual progress fill and the visible percent label at 100%, while the accessible value text keeps the real percentage", "names the progress bar after the card title", "renders long localized labels without breaking the layout query", "exposes the card as an accessible group named with the title and period description", "keeps the same accessible name and value text under an RTL ancestor", "reset line", "renders the reset label in a <time> carrying the original UTC instant", "carries the spoken form on a visually-hidden sibling, not on the <time>"]}, {"file": "libs/usage-dashboard/src/components/ModelLimitsSection/tests/ModelLimitsSection.spec.tsx", "assertions": ["ModelLimitsSection", "renders the row count separately in the section heading", "renders the empty state while preserving the section shell", "renders exactly the fixed comparison headers in order", "renders one semantic row with Item, three period cells, and Status", "vertically centers desktop row content without changing horizontal alignment", "renders token progress followed by attributed Cost in every period cell", "renders unavailable Cost as a value without a visible Cost label", "renders unlimited and unavailable token states without progress bars", "clamps progress visually while retaining the real accessible value", "renders rows in supplied order with avatar fallback and accessible names", "keeps long identity content constrained inside the Item cell", "uses one responsive semantic subtree under an RTL ancestor", "renders accessible overall Cost indicators for affected period headers", "period header reset line"]}]. Reproduce project checks from the repository root with npm exec nx run usage-dashboard:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: renders the title, used amount and "used of" caption.

Sources:
libs/usage-dashboard/README.md:1-425
libs/usage-dashboard/src/index.ts:1-43
libs/usage-dashboard/package.json:1-42
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191 — UsageLimitCard
libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152 — UsageLimitCardProps
apps/chat/src/pages/SettingsPage/UsageTab/UsageTab.tsx:1-264
libs/usage-dashboard/src/components/UsageLimitCard/tests/UsageLimitCard.spec.tsx:1-267
libs/usage-dashboard/src/components/ModelLimitsSection/tests/ModelLimitsSection.spec.tsx:1-517

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Calendar periods
Components and helpers
Isolation discrepancy
Today/week/month are calendar windows, not rolling durations.
Cards consume display data; exported helpers do perform mapping.
Mapping source imports generated API DTOs outside the documented exception.
10
Usage dashboard
lib-usage-dashboard-09

### Notes:
Slide ID: lib-usage-dashboard-09

Review these constraints before choosing the library. Calendar periods: Today/week/month are calendar windows, not rolling durations. Separate component and helper: Cards consume display data; exported helpers do perform mapping. Isolation discrepancy: Mapping source imports generated API DTOs outside the documented exception. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/usage-dashboard/README.md:1-425
libs/usage-dashboard/src/index.ts:1-43
libs/usage-dashboard/package.json:1-42
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191 — UsageLimitCard
libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152 — UsageLimitCardProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.