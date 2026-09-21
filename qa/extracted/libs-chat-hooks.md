<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Chat hooks
Reuse headless request lifecycles and chat-interface behavior.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-chat-hooks
01
Chat hooks
lib-chat-hooks-01

### Notes:
Slide ID: lib-chat-hooks-01

This session explains reuse headless request lifecycles and chat-interface behavior. The library is a local private workspace package at libs/chat-hooks. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Reuse headless request lifecycles and chat-interface behavior.

01
02
03
Build a custom chat
Keep rendering separate
Limit imports
Reuse stream state, scrolling and attachment behavior.
Connect returned data and callbacks to your own UI.
Use the dependency-focused public subpaths.
02
Chat hooks
lib-chat-hooks-02

### Notes:
Slide ID: lib-chat-hooks-02

Start with a concrete caller need. Build a custom chat: Reuse stream state, scrolling and attachment behavior. Keep rendering separate: Connect returned data and callbacks to your own UI. Limit imports: Use the dependency-focused public subpaths. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink

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
Host configuration
Headless hook
Return values
Host UI

Injected API instance
Lifecycle and state
Data, loading, errors
Render and respond
Library: Reusable hook state, data mapping and permitted thin operation wrappers.
03
Chat hooks
lib-chat-hooks-03

### Notes:
Slide ID: lib-chat-hooks-03

The library owns Reusable hook state, data mapping and permitted thin operation wrappers. The host owns Configured clients, authentication setup, routing, app contexts and translated labels.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
useShareLink · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| useViewportWidth() | number; browser resize lifecycle |
| useShareLink(api, id, origin) | data, isLoading, error, setAccess |
| Injected API | Pick<ShareApi, createShareLink> |
| Subpath entries | Focused public import surfaces |
04
Chat hooks
lib-chat-hooks-04

### Notes:
Slide ID: lib-chat-hooks-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function ViewportDemo() {
  const width = useViewportWidth();
  return <p>Demo viewport: {width}px</p>;
}
// Import from /viewport-layout.
// The hook removes its resize listener on cleanup.
Full example: examples/chat-hooks.tsx · uses @epam/ai-dial-chat-hooks
05
Chat hooks
lib-chat-hooks-05

### Notes:
Slide ID: lib-chat-hooks-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/chat-hooks.tsx. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Reuse stream state, scrolling and attachment behavior. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep chat hooks focused on its public responsibility.

01
02
03
Keep the client stable
Render the lifecycle
Change link access
Inject a configured ShareApi operation into useShareLink.
Read data, isLoading and error from the hook result.
Call setAccess to request a link for the new access level.
06
Chat hooks
lib-chat-hooks-06

### Notes:
Slide ID: lib-chat-hooks-06

Follow this concrete integration sequence. Keep the client stable: Inject a configured ShareApi operation into useShareLink. Render the lifecycle: Read data, isLoading and error from the hook result. Change link access: Call setAccess to request a link for the new access level. The complete typed module in examples/chat-hooks.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A request lifecycle with an injected client
The caller configures auth and transport.

const { data, isLoading, error, setAccess } =
  useShareLink(
    api,
    'demo-item',
    'https://example.com',
  );
// Render data.url, pending state or the error.
Focused source-backed example · see examples/ and content/api-index.md.
07
Chat hooks
lib-chat-hooks-10

### Notes:
Slide ID: lib-chat-hooks-10

The full ShareLifecycleDemo example receives Pick<ShareApi, createShareLink>. Changing access requests a new link. The hook uses request identifiers to avoid overwriting newer results with stale responses. Pass origin explicitly when the default browser-global expression is unsuitable.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Small layout entry
Request lifecycle
Broad feature entries
/viewport-layout includes useViewportWidth with listener cleanup.
useShareLink manages link loading, access changes and stale response guards.
Conversation, files, catalog, OAuth and MCP have explicit subpaths.
08
Chat hooks
lib-chat-hooks-07

### Notes:
Slide ID: lib-chat-hooks-07

Customization comes from the current exports and prop declarations. Small layout entry: /viewport-layout includes useViewportWidth with listener cleanup. Request lifecycle: useShareLink manages link loading, access changes and stale response guards. Broad feature entries: Conversation, files, catalog, OAuth and MCP have explicit subpaths. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | toolset-editor/src/components/AuthSection/AuthSection.tsx |
| Test evidence | selects a file and resets the input so the same file can be selected again |
| Test evidence | refreshes once when the active conversation is missing without looping on item changes |
09
Chat hooks
lib-chat-hooks-08

### Notes:
Slide ID: lib-chat-hooks-08

Actual consumers: libs/toolset-editor/src/components/AuthSection/AuthSection.tsx; libs/toolset-editor/src/components/GeneralForm/GeneralForm.tsx; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx; libs/toolset-editor/src/models/toolset-form.ts; libs/toolset-editor/src/utils/toolsets.ts; libs/toolset-editor/src/constants/toolsets.ts. Existing test evidence: [{"file": "libs/chat-hooks/src/conversation/useImportFilePicker/tests/useImportFilePicker.spec.ts", "assertions": ["useImportFilePicker", "selects a file and resets the input so the same file can be selected again", "programmatically clicks the attached input", "applies and clears the host-resolved accept value"]}, {"file": "libs/chat-hooks/src/conversation/useActiveConversationSync/tests/useActiveConversationSync.spec.ts", "assertions": ["useActiveConversationSync", "refreshes once when the active conversation is missing without looping on item changes", "marks the matching raw conversation viewed when it becomes active", "rechecks the active conversation when the injected id matcher changes"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-chat-hooks:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink
libs/toolset-editor/src/components/AuthSection/AuthSection.tsx:1-504
libs/chat-hooks/src/conversation/useImportFilePicker/tests/useImportFilePicker.spec.ts:1-63
libs/chat-hooks/src/conversation/useActiveConversationSync/tests/useActiveConversationSync.spec.ts:1-84

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Stable dependencies
Browser assumptions
Boundary audit needed
Recreating API instances can retrigger effects.
Some hooks use browser globals; pass origin explicitly for share examples.
Some current helpers contain more DIAL-specific knowledge than the narrow rule.
10
Chat hooks
lib-chat-hooks-09

### Notes:
Slide ID: lib-chat-hooks-09

Review these constraints before choosing the library. Stable dependencies: Recreating API instances can retrigger effects. Browser assumptions: Some hooks use browser globals; pass origin explicitly for share examples. Boundary audit needed: Some current helpers contain more DIAL-specific knowledge than the narrow rule. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/chat-hooks/README.md:1-3809
libs/chat-hooks/src/index.ts:1-184
libs/chat-hooks/package.json:1-266
libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109 — useShareLink
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.