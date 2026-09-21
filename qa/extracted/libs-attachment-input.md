<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Attachment input
Turn file state into clear attachment controls.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-attachment-input
01
Attachment input
lib-attachment-input-01

### Notes:
Slide ID: lib-attachment-input-01

This session explains turn file state into clear attachment controls. The library is a local private workspace package at libs/attachment-input. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/attachment-input/README.md:1-264
libs/attachment-input/src/index.ts:1-61
libs/attachment-input/package.json:1-39
libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56 — AttachmentTray
libs/attachment-input/src/models/attachment-tray.ts:24-39 — AttachmentTrayProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Turn file state into clear attachment controls.

01
02
03
Compose with files
Recover from failure
Reuse sent-file UI
Show files before sending a message.
Expose remove and retry actions per attachment.
Render image groups and file rows in transcripts.
02
Attachment input
lib-attachment-input-02

### Notes:
Slide ID: lib-attachment-input-02

Start with a concrete caller need. Compose with files: Show files before sending a message. Recover from failure: Expose remove and retry actions per attachment. Reuse sent-file UI: Render image groups and file rows in transcripts. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/attachment-input/README.md:1-264
libs/attachment-input/src/index.ts:1-61
libs/attachment-input/package.json:1-39
libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56 — AttachmentTray
libs/attachment-input/src/models/attachment-tray.ts:24-39 — AttachmentTrayProps

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
Host file state
Attachment Tray
Callback
Host update

Display Attachment[]
Cards and actions
Attachment identifier
Retry or remove
Library: Cards, trays, file-drop affordances and clipboard handling.
03
Attachment input
lib-attachment-input-03

### Notes:
Slide ID: lib-attachment-input-03

The library owns Cards, trays, file-drop affordances and clipboard handling. The host owns Upload transport, progress state, validation policy and preview URLs.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/attachment-input/README.md:1-264
libs/attachment-input/src/index.ts:1-61
libs/attachment-input/package.json:1-39
libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56 — AttachmentTray
libs/attachment-input/src/models/attachment-tray.ts:24-39 — AttachmentTrayProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
AttachmentTray · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| attachments | DisplayAttachment[] |
| onRemove (optional) | ((id: string) => void) |
| onRetry (optional) | ((id: string) => void) |
| labels (optional) | AttachmentTrayLabels |
04
Attachment input
lib-attachment-input-04

### Notes:
Slide ID: lib-attachment-input-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/attachment-input/README.md:1-264
libs/attachment-input/src/index.ts:1-61
libs/attachment-input/package.json:1-39
libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56 — AttachmentTray
libs/attachment-input/src/models/attachment-tray.ts:24-39 — AttachmentTrayProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function AttachmentDemo({ initial }: { initial: DisplayAttachment[] }) {
  const [attachments, setAttachments] = useState(initial);
  return <AttachmentTray attachments={attachments}
    onRemove={id => setAttachments(items => items.filter(x => x.id !== id))}
    labels={{ ariaLabel: 'Attached demo files' }} />;
}
Full example: examples/attachment-input.tsx · uses @epam/ai-dial-attachment-input
05
Attachment input
lib-attachment-input-05

### Notes:
Slide ID: lib-attachment-input-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/attachment-input.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Show files before sending a message. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/attachment-input/README.md:1-264
libs/attachment-input/src/index.ts:1-61
libs/attachment-input/package.json:1-39
libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56 — AttachmentTray
libs/attachment-input/src/models/attachment-tray.ts:24-39 — AttachmentTrayProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep attachment input focused on its public responsibility.

01
02
03
Accept a file
Reflect progress
Retry or remove
The host starts an upload and creates display data.
Pass current attachments and their upload state into the tray.
Use the attachment id from the callback to update host state.
06
Attachment input
lib-attachment-input-06

### Notes:
Slide ID: lib-attachment-input-06

Follow this concrete integration sequence. Accept a file: The host starts an upload and creates display data. Reflect progress: Pass current attachments and their upload state into the tray. Retry or remove: Use the attachment id from the callback to update host state. The complete typed module in examples/attachment-input.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/attachment-input/README.md:1-264
libs/attachment-input/src/index.ts:1-61
libs/attachment-input/package.json:1-39
libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56 — AttachmentTray
libs/attachment-input/src/models/attachment-tray.ts:24-39 — AttachmentTrayProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Tray and group
Lazy previews
Accessible actions
Use AttachmentTray while composing; AttachmentGroup for sent files.
Image loading has an observable loading and error lifecycle.
Supply localized open, retry, remove and upload labels.
07
Attachment input
lib-attachment-input-07

### Notes:
Slide ID: lib-attachment-input-07

Customization comes from the current exports and prop declarations. Tray and group: Use AttachmentTray while composing; AttachmentGroup for sent files. Lazy previews: Image loading has an observable loading and error lifecycle. Accessible actions: Supply localized open, retry, remove and upload labels. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/attachment-input/README.md:1-264
libs/attachment-input/src/index.ts:1-61
libs/attachment-input/package.json:1-39
libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56 — AttachmentTray
libs/attachment-input/src/models/attachment-tray.ts:24-39 — AttachmentTrayProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | conversation-messages/src/components/MessageBubble/UserMessageBubble.tsx |
| Test evidence | handles null clipboardData without throwing |
| Test evidence | starts in loading state when enabled with a source |
08
Attachment input
lib-attachment-input-08

### Notes:
Slide ID: lib-attachment-input-08

Actual consumers: libs/conversation-messages/src/components/MessageBubble/UserMessageBubble.tsx; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx; libs/source-panel/src/components/FilesSection/FilesSection.tsx; libs/conversation-input/src/hooks/useAttachments.ts; libs/chat-hooks/src/attachment/useAttachmentValidation/useAttachmentValidation.ts; libs/conversation-input/src/components/Input/Input.tsx. Existing test evidence: [{"file": "libs/attachment-input/src/hooks/tests/useClipboardPaste.spec.ts", "assertions": ["useClipboardPaste", "handles null clipboardData without throwing", "image paste creates an Image attachment and prevents default", "stamps a pasted image name with the paste time, keeping base and extension", "gives each image of a multi-image paste a distinct name", "gives images pasted at different times distinct names", "long text creates a Pasted attachment with preview name", "preview name is truncated to 80 chars with ellipsis when text is very long", "ignores the image and pastes text when clipboard contains both image and text", "short text does not create an attachment"]}, {"file": "libs/attachment-input/src/hooks/tests/useLazyImageLoad.spec.tsx", "assertions": ["useLazyImageLoad", "starts in loading state when enabled with a source", "moves to loaded when the image loads", "moves to error when the image fails to load", "resets to idle when disabled", "resets to loading when the source changes"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-attachment-input:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/attachment-input/README.md:1-264
libs/attachment-input/src/index.ts:1-61
libs/attachment-input/package.json:1-39
libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56 — AttachmentTray
libs/attachment-input/src/models/attachment-tray.ts:24-39 — AttachmentTrayProps
libs/conversation-messages/src/components/MessageBubble/UserMessageBubble.tsx:1-184
libs/attachment-input/src/hooks/tests/useClipboardPaste.spec.ts:1-181
libs/attachment-input/src/hooks/tests/useLazyImageLoad.spec.tsx:1-74

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
No uploader in a card
Watch callback shapes
Keep state ownership clear
Showing progress does not perform the network upload.
Tray actions use an id; message bubble callbacks can use an object.
The library has local UI state; the host owns durable file state.
09
Attachment input
lib-attachment-input-09

### Notes:
Slide ID: lib-attachment-input-09

Review these constraints before choosing the library. No uploader in a card: Showing progress does not perform the network upload. Watch callback shapes: Tray actions use an id; message bubble callbacks can use an object. Keep state ownership clear: The library has local UI state; the host owns durable file state. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/attachment-input/README.md:1-264
libs/attachment-input/src/index.ts:1-61
libs/attachment-input/package.json:1-39
libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56 — AttachmentTray
libs/attachment-input/src/models/attachment-tray.ts:24-39 — AttachmentTrayProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.