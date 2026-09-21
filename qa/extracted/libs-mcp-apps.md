<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
MCP Apps
Connect tool-result UI resources to an inline interactive preview.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-mcp-apps
01
MCP Apps
lib-mcp-apps-01

### Notes:
Slide ID: lib-mcp-apps-01

This session explains connect tool-result ui resources to an inline interactive preview. The library is a local private workspace package at libs/mcp-apps. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/mcp-apps/README.md:1-148
libs/mcp-apps/src/index.ts:1-31
libs/mcp-apps/package.json:1-42
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247 — McpAppInlinePreview
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65 — McpAppInlinePreviewProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Connect tool-result UI resources to an inline interactive preview.

01
02
03
Find a tool UI
Reuse the result
Expand the UI
Match a message to an MCP tool resource.
Seed the preview from the original tool call.
Open the matched application in the attachment canvas.
02
MCP Apps
lib-mcp-apps-02

### Notes:
Slide ID: lib-mcp-apps-02

Start with a concrete caller need. Find a tool UI: Match a message to an MCP tool resource. Reuse the result: Seed the preview from the original tool call. Expand the UI: Open the matched application in the attachment canvas. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/mcp-apps/README.md:1-148
libs/mcp-apps/src/index.ts:1-31
libs/mcp-apps/package.json:1-42
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247 — McpAppInlinePreview
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65 — McpAppInlinePreviewProps

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
Tool evidence
Response cache
Inline preview
Host adapter

Match and call seed
Resource HTML + result
Sandboxed MCP renderer
Calls and expansion
Library: Preview state, matching/seed helpers and a per-conversation response cache.
03
MCP Apps
lib-mcp-apps-03

### Notes:
Slide ID: lib-mcp-apps-03

The library owns Preview state, matching/seed helpers and a per-conversation response cache. The host owns Configured resource/tool calls, sandbox URL, host context and expansion behavior.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/mcp-apps/README.md:1-148
libs/mcp-apps/src/index.ts:1-31
libs/mcp-apps/package.json:1-42
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247 — McpAppInlinePreview
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65 — McpAppInlinePreviewProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
McpAppInlinePreview · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| match | McpAppToolRef |
| cache | McpAppResponseCache |
| hostAdapter | McpAppHostAdapter |
| toolCall (optional) | McpAppToolCallSeed |
04
MCP Apps
lib-mcp-apps-04

### Notes:
Slide ID: lib-mcp-apps-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/mcp-apps/README.md:1-148
libs/mcp-apps/src/index.ts:1-31
libs/mcp-apps/package.json:1-42
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247 — McpAppInlinePreview
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65 — McpAppInlinePreviewProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

const cache = useMcpAppResponseCache('demo-conversation');
<McpAppInlinePreview
  match={match} cache={cache} cacheKey="demo-message"
  hostAdapter={adapter} onExpand={onExpand}
  expandAriaLabel="Expand demo app"
  reloadAriaLabel="Reload"
  loadErrorLabel="Could not load demo app"
  openedInCanvasLabel="Open in preview"
/>
Full example: examples/mcp-apps.tsx · uses @epam/ai-dial-mcp-apps
05
MCP Apps
lib-mcp-apps-05

### Notes:
Slide ID: lib-mcp-apps-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/mcp-apps.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Match a message to an MCP tool resource. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/mcp-apps/README.md:1-148
libs/mcp-apps/src/index.ts:1-31
libs/mcp-apps/package.json:1-42
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247 — McpAppInlinePreview
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65 — McpAppInlinePreviewProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep mcp apps focused on its public responsibility.

01
02
03
Match tool evidence
Inject the host adapter
Reuse cached state
Provide the resource match and a stable cache key.
The host fetches resources and handles tool calls.
Keep response caching scoped to the conversation lifetime.
06
MCP Apps
lib-mcp-apps-06

### Notes:
Slide ID: lib-mcp-apps-06

Follow this concrete integration sequence. Match tool evidence: Provide the resource match and a stable cache key. Inject the host adapter: The host fetches resources and handles tool calls. Reuse cached state: Keep response caching scoped to the conversation lifetime. The complete typed module in examples/mcp-apps.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/mcp-apps/README.md:1-148
libs/mcp-apps/src/index.ts:1-31
libs/mcp-apps/package.json:1-42
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247 — McpAppInlinePreview
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65 — McpAppInlinePreviewProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Explicit host adapter
Cache identity
Lifecycle state
Inject fetchResourceHtml, callTool, hostInfo and sandboxUrl.
Entries are checked against seed identity and expiry.
Loading, Ready, Error and Unavailable are distinct enum values.
07
MCP Apps
lib-mcp-apps-07

### Notes:
Slide ID: lib-mcp-apps-07

Customization comes from the current exports and prop declarations. Explicit host adapter: Inject fetchResourceHtml, callTool, hostInfo and sandboxUrl. Cache identity: Entries are checked against seed identity and expiry. Lifecycle state: Loading, Ready, Error and Unavailable are distinct enum values. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/mcp-apps/README.md:1-148
libs/mcp-apps/src/index.ts:1-31
libs/mcp-apps/package.json:1-42
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247 — McpAppInlinePreview
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65 — McpAppInlinePreviewProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat-hooks/src/mcp-apps/useMcpAppTools/useMcpAppTools.ts |
| Test evidence | stamps the preview card and its header |
08
MCP Apps
lib-mcp-apps-08

### Notes:
Slide ID: lib-mcp-apps-08

Actual consumers: libs/chat-hooks/src/mcp-apps/useMcpAppTools/useMcpAppTools.ts; libs/chat-hooks/src/mcp-apps/mcp-apps-api-client.ts; libs/chat-hooks/src/mcp-apps/useMcpAppHostAdapter/useMcpAppHostAdapter.ts; libs/chat-hooks/src/mcp-apps/useOpenMcpAppCanvas/useOpenMcpAppCanvas.ts; apps/chat/src/components/ConversationView/ConversationMessageItem.tsx; apps/chat/src/components/ConversationView/ConversationView.tsx. Existing test evidence: [{"file": "libs/mcp-apps/src/components/McpAppInlinePreview/tests/McpAppInlinePreview.classes.spec.tsx", "assertions": ["McpAppInlinePreview \u2014 public class names", "stamps the preview card and its header", "forwards every colour override as a CSS custom property"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-mcp-apps:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/mcp-apps/README.md:1-148
libs/mcp-apps/src/index.ts:1-31
libs/mcp-apps/package.json:1-42
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247 — McpAppInlinePreview
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65 — McpAppInlinePreviewProps
libs/chat-hooks/src/mcp-apps/useMcpAppTools/useMcpAppTools.ts:1-118
libs/mcp-apps/src/components/McpAppInlinePreview/tests/McpAppInlinePreview.classes.spec.tsx:1-141

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Origin isolation required
Avoid duplicate side effects
Not a general API client
Configure the separate MCP sandbox deployment.
Indirectly discovered tools are not safe to re-call blindly.
Backend operations enter through the host adapter.
09
MCP Apps
lib-mcp-apps-09

### Notes:
Slide ID: lib-mcp-apps-09

Review these constraints before choosing the library. Origin isolation required: Configure the separate MCP sandbox deployment. Avoid duplicate side effects: Indirectly discovered tools are not safe to re-call blindly. Not a general API client: Backend operations enter through the host adapter. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/mcp-apps/README.md:1-148
libs/mcp-apps/src/index.ts:1-31
libs/mcp-apps/package.json:1-42
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247 — McpAppInlinePreview
libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65 — McpAppInlinePreviewProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.