<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Toolset editor
Coordinate MCP toolset editing through an explicit host adapter.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-toolset-editor
01
Toolset editor
lib-toolset-editor-01

### Notes:
Slide ID: lib-toolset-editor-01

This session explains coordinate mcp toolset editing through an explicit host adapter. The library is a local private workspace package at libs/toolset-editor. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Coordinate MCP toolset editing through an explicit host adapter.

01
02
03
Create a toolset
Persist a draft
Authorize access
Edit metadata, endpoint, transport and authentication settings.
Reuse the identifier returned by the first successful save.
Delegate login and OAuth to host behavior.
02
Toolset editor
lib-toolset-editor-02

### Notes:
Slide ID: lib-toolset-editor-02

Start with a concrete caller need. Create a toolset: Edit metadata, endpoint, transport and authentication settings. Persist a draft: Reuse the identifier returned by the first successful save. Authorize access: Delegate login and OAuth to host behavior. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps

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
Editor form
on Persist
Host authentication
Completion callbacks

Metadata and setup
Create or update
Post-save login / OAuth
Refresh and navigate
Library: Form state, dirty/errors state and save orchestration around injected operations.
03
Toolset editor
lib-toolset-editor-03

### Notes:
Slide ID: lib-toolset-editor-03

The library owns Form state, dirty/errors state and save orchestration around injected operations. The host owns HTTP persistence, OAuth execution, credentials APIs, routes and file-manager integration.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
ToolsetEditor · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| initialForm | ToolsetFormData |
| onPersist | (form: ToolsetFormData, toolsetId: string) => Promise<string | null> |
| onOAuthLogin | ToolsetOAuthLoginHandler |
| authActions | ToolsetAuthActions |
04
Toolset editor
lib-toolset-editor-04

### Notes:
Slide ID: lib-toolset-editor-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function ToolsetEditorDemo(host: ToolsetEditorProps) {
  return <ToolsetEditor {...host} />;
}

// host includes required persistence, authentication,
// notification, file-manager and navigation callbacks.
// See the complete contract in content/api-index.md.
Full example: examples/toolset-editor.tsx · uses @epam/ai-dial-toolset-editor
05
Toolset editor
lib-toolset-editor-05

### Notes:
Slide ID: lib-toolset-editor-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/toolset-editor.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Edit metadata, endpoint, transport and authentication settings. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep toolset editor focused on its public responsibility.

01
02
03
Prepare the adapter
Collect toolset values
Run host operations
Supply the required persistence, file and auth callbacks.
Let the editor coordinate metadata and setup controls.
Keep credential flows, endpoint calls and routing in the host.
06
Toolset editor
lib-toolset-editor-06

### Notes:
Slide ID: lib-toolset-editor-06

Follow this concrete integration sequence. Prepare the adapter: Supply the required persistence, file and auth callbacks. Collect toolset values: Let the editor coordinate metadata and setup controls. Run host operations: Keep credential flows, endpoint calls and routing in the host. The complete typed module in examples/toolset-editor.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Validate a candidate endpoint
Use an exported utility before host persistence.

const valid = isValidEndpointUrl(
  'https://example.com/mcp',
);
Focused source-backed example · see examples/ and content/api-index.md.
07
Toolset editor
lib-toolset-editor-10

### Notes:
Slide ID: lib-toolset-editor-10

This pure validation example is included in the full module. A valid URL does not establish toolset availability or successful authentication. The complete ToolsetEditor still requires every prop in the exported contract.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Typed integration
Shared metadata
MCP URL resolver
ToolsetEditorProps makes persistence, auth and file dependencies explicit.
GeneralForm reuses builder-form fields and validation.
buildMcpUrl receives the current draft identifier.
08
Toolset editor
lib-toolset-editor-07

### Notes:
Slide ID: lib-toolset-editor-07

Customization comes from the current exports and prop declarations. Typed integration: ToolsetEditorProps makes persistence, auth and file dependencies explicit. Shared metadata: GeneralForm reuses builder-form fields and validation. MCP URL resolver: buildMcpUrl receives the current draft identifier. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/pages/ToolsetEditor/ToolsetEditor.tsx |
| Test evidence | renders the default title, description, and copy button |
| Test evidence | calls onAuthChange with ApiKey type when the ApiKey option is clicked |
09
Toolset editor
lib-toolset-editor-08

### Notes:
Slide ID: lib-toolset-editor-08

Actual consumers: apps/chat/src/pages/ToolsetEditor/ToolsetEditor.tsx; apps/chat/src/pages/ToolsetEditor/CustomAppEditorView.tsx; apps/chat/src/hooks/toolsets/useToolsetEditorOAuthLogin.ts; apps/chat/src/models/custom-apps.ts; apps/chat/src/utils/toolsets.ts. Existing test evidence: [{"file": "libs/toolset-editor/src/components/ConnectMcpUrlContent/tests/ConnectMcpUrlContent.spec.tsx", "assertions": ["ConnectMcpUrlContent", "renders the default title, description, and copy button", "renders host-supplied labels instead of the defaults", "copies the endpoint URL to the clipboard", "announces the copy through the polite live region"]}, {"file": "libs/toolset-editor/src/components/AuthSection/tests/AuthSection.spec.tsx", "assertions": [",", "AuthSection", "type selection", "calls onAuthChange with ApiKey type when the ApiKey option is clicked", "calls onAuthChange with OAuth type when the OAuth option is clicked", "disables every non-selected auth-type option while the toolset is logged in, leaving the selected one enabled", "marks the active auth type as checked for assistive technology", "defaults a fresh OAuth selection to WithConfig so config fields are visible immediately", "defaults an OAuth selection to WithLogin when a client is already configured", "API Key conditional fields", "renders key header and API key inputs when ApiKey + WithLogin is active", "masks the API key value and exposes a reveal toggle", "renders only the key header input when ApiKey + WithoutLogin is active", "renders WithLogin and WithoutLogin radio buttons for ApiKey", "OAuth conditional fields"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-toolset-editor:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: calls onAuthChange with ApiKey type when the ApiKey option is clicked.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps
apps/chat/src/pages/ToolsetEditor/ToolsetEditor.tsx:1-463
libs/toolset-editor/src/components/ConnectMcpUrlContent/tests/ConnectMcpUrlContent.spec.tsx:1-63
libs/toolset-editor/src/components/AuthSection/tests/AuthSection.spec.tsx:1-808

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
No minimal fake backend
Form identity
Boundary discrepancy
A working editor needs the required host callbacks and file component.
A new initialForm object reseeds the editing session.
Current code imports chat-hooks symbols; document this wider dependency.
10
Toolset editor
lib-toolset-editor-09

### Notes:
Slide ID: lib-toolset-editor-09

Review these constraints before choosing the library. No minimal fake backend: A working editor needs the required host callbacks and file component. Form identity: A new initialForm object reseeds the editing session. Boundary discrepancy: Current code imports chat-hooks symbols; document this wider dependency. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/toolset-editor/README.md:1-383
libs/toolset-editor/src/index.ts:1-47
libs/toolset-editor/package.json:1-41
libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425 — ToolsetEditor
libs/toolset-editor/src/models/toolset-editor-props.ts:74-150 — ToolsetEditorProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.