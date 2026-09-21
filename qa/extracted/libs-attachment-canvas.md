<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Attachment canvas
Preview heterogeneous content through one typed surface.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-attachment-canvas
01
Attachment canvas
lib-attachment-canvas-01

### Notes:
Slide ID: lib-attachment-canvas-01

This session explains preview heterogeneous content through one typed surface. The library is a local private workspace package at libs/attachment-canvas. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Preview heterogeneous content through one typed surface.

01
02
03
Inspect evidence
Choose a renderer
Extend a workspace
Open a cited PDF or uploaded text beside a conversation.
A content discriminator selects the appropriate view.
Add visualizers or MCP content through explicit inputs.
02
Attachment canvas
lib-attachment-canvas-02

### Notes:
Slide ID: lib-attachment-canvas-02

Start with a concrete caller need. Inspect evidence: Open a cited PDF or uploaded text beside a conversation. Choose a renderer: A content discriminator selects the appropriate view. Extend a workspace: Add visualizers or MCP content through explicit inputs. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps

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
Host resolver
Typed content
Attachment Canvas
User action

Content or access failure
Attachment Content Type
Lazy viewer
Close, copy or download
Library: Viewer selection, panel layout, lazy renderer loading and optional canvas context.
03
Attachment canvas
lib-attachment-canvas-03

### Notes:
Slide ID: lib-attachment-canvas-03

The library owns Viewer selection, panel layout, lazy renderer loading and optional canvas context. The host owns File access, resolved content, authorization, deployment settings and download behavior. The direct AttachmentCanvas example is controlled and does not require a provider. The provider is needed for useAttachmentCanvas and the context-based opening flow. The host must supply authenticated loading rather than passing session knowledge into ordinary UI code. The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
AttachmentCanvas · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| content | AttachmentCanvasContent |
| isOpen | boolean |
| onClose | () => void |
| labels | AttachmentCanvasLabels |
04
Attachment canvas
lib-attachment-canvas-04

### Notes:
Slide ID: lib-attachment-canvas-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON. The direct AttachmentCanvas example is controlled and does not require a provider. The provider is needed for useAttachmentCanvas and the context-based opening flow. The host must supply authenticated loading rather than passing session knowledge into ordinary UI code.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<AttachmentCanvas
  isOpen={open}
  onClose={() => setOpen(false)}
  content={{
    type: AttachmentContentType.PlainText,
    text: 'Demo evidence',
  }}
  labels={{ ariaLabel: 'Demo preview' }}
/>
Full example: examples/attachment-canvas.tsx · uses @epam/ai-dial-attachment-canvas
05
Attachment canvas
lib-attachment-canvas-05

### Notes:
Slide ID: lib-attachment-canvas-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/attachment-canvas.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Open a cited PDF or uploaded text beside a conversation. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep attachment canvas focused on its public responsibility.

01
02
03
Resolve a file
Open the preview
Handle an action
Fetch accessible content in the host and choose its content kind.
Supply content, open state, labels and any renderer setup.
Close locally or download through a host callback.
06
Attachment canvas
lib-attachment-canvas-06

### Notes:
Slide ID: lib-attachment-canvas-06

Follow this concrete integration sequence. Resolve a file: Fetch accessible content in the host and choose its content kind. Open the preview: Supply content, open state, labels and any renderer setup. Handle an action: Close locally or download through a host callback. The complete typed module in examples/attachment-canvas.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Context-based canvas control
AttachmentCanvasProvider owns shared canvas state.

import { AttachmentCanvasProvider }
  from '@epam/ai-dial-attachment-canvas';

<AttachmentCanvasProvider>
  {children}
</AttachmentCanvasProvider>
Focused source-backed example · see examples/ and content/api-index.md.
07
Attachment canvas
lib-attachment-canvas-10

### Notes:
Slide ID: lib-attachment-canvas-10

The direct controlled example does not need this context. Use the provider when descendants call useAttachmentCanvas or the context-driven opening hook; supply host resolvers for access-dependent content.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Typed content variants
Optional shared context
Host loading hooks
Plain text, code, Markdown, PDF, OOXML, media, HTML and MCP views.
A canvas provider and its context hook coordinate shared preview state.
loadPdf and configurePdfWorker support caller-controlled PDF setup.
08
Attachment canvas
lib-attachment-canvas-07

### Notes:
Slide ID: lib-attachment-canvas-07

Customization comes from the current exports and prop declarations. Typed content variants: Plain text, code, Markdown, PDF, OOXML, media, HTML and MCP views. Optional shared context: AttachmentCanvasProvider and useAttachmentCanvas coordinate a canvas. Host loading hooks: loadPdf and configurePdfWorker support caller-controlled PDF setup. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | mcp-apps/src/hooks/useMcpAppInlinePreview/useMcpAppInlinePreview.ts |
| Test evidence | routes an OOXML attachment by extension when its MIME type is generic |
| Test evidence | renders plain text immediately with no syntax highlighter for a plaintext language |
09
Attachment canvas
lib-attachment-canvas-08

### Notes:
Slide ID: lib-attachment-canvas-08

Actual consumers: libs/mcp-apps/src/hooks/useMcpAppInlinePreview/useMcpAppInlinePreview.ts; libs/quotations/src/models/office-highlight.ts; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx; apps/chat/src/pages/SkillEditor/SkillEditor.tsx; apps/chat/src/hooks/attachment/useSkillFilePreviewSync.ts; apps/chat/src/hooks/attachment/useAttachmentCanvasResolvers.ts. Existing test evidence: [{"file": "libs/attachment-canvas/src/hooks/useOpenAttachmentCanvas/tests/useOpenAttachmentCanvas.spec.ts", "assertions": ["useOpenAttachmentCanvas routing", "routes an OOXML attachment by extension when its MIME type is generic", "routes CSV by extension to the @silurus/ooxml resolver instead of the code renderer", "routes an OOXML attachment whose name has no extension by MIME type", "opens the unsupported panel when a recognized OOXML file cannot be resolved", "forwards a Forbidden error from the OOXML resolver to the canvas", "does not route legacy binary Office formats to the OOXML resolver", "routes .md attachments to the markdown resolver", "routes .markdown attachments to the markdown resolver", "routes .json attachments to the JSON resolver", "routes .jsonl attachments to the code resolver (not JSON)", "opens the canvas with the resolved content", "routes text/markdown MIME type to the markdown resolver (ignores .pdf extension in title)", "prefers a known text MIME type over an OOXML-looking title", "routes application/json MIME type to the JSON resolver"]}, {"file": "libs/attachment-canvas/src/components/CodeContent/tests/CodeContent.spec.tsx", "assertions": ["CodeContent", "renders plain text immediately with no syntax highlighter for a plaintext language", "renders plain text immediately with no syntax highlighter when no language is set", "shows the value via a plain fallback, then highlights it once the engine loads for a real language", "announces the pending state via role="]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-attachment-canvas:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps
libs/mcp-apps/src/hooks/useMcpAppInlinePreview/useMcpAppInlinePreview.ts:1-154
libs/attachment-canvas/src/hooks/useOpenAttachmentCanvas/tests/useOpenAttachmentCanvas.spec.ts:1-1174
libs/attachment-canvas/src/components/CodeContent/tests/CodeContent.spec.tsx:1-85

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Heavy renderers
Content errors differ
Untrusted content
PDF, Office, syntax and MCP dependencies affect packaging; several load lazily.
Unsupported, forbidden and failed loads have distinct display states.
HTML and MCP views require the documented sandbox and host settings.
10
Attachment canvas
lib-attachment-canvas-09

### Notes:
Slide ID: lib-attachment-canvas-09

Review these constraints before choosing the library. Heavy renderers: PDF, Office, syntax and MCP dependencies affect packaging; several load lazily. Content errors differ: Unsupported, forbidden and failed loads have distinct display states. Untrusted content: HTML and MCP views require the documented sandbox and host settings. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/attachment-canvas/README.md:1-615
libs/attachment-canvas/src/index.ts:1-89
libs/attachment-canvas/package.json:1-64
libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445 — AttachmentCanvas
libs/attachment-canvas/src/models/attachment-canvas.ts:487-542 — AttachmentCanvasProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.