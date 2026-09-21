<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Conversation input
Compose a message with deployment, attachment and voice controls.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-conversation-input
01
Conversation input
lib-conversation-input-01

### Notes:
Slide ID: lib-conversation-input-01

This session explains compose a message with deployment, attachment and voice controls. The library is a local private workspace package at libs/conversation-input. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/conversation-input/README.md:1-355
libs/conversation-input/src/index.ts:1-35
libs/conversation-input/package.json:1-42
libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78 — ConversationInput
libs/conversation-input/src/models/ConversationInput.ts:182-455 — ConversationInputProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Compose a message with deployment, attachment and voice controls.

01
02
03
Send a message
Control generation
Support rich input
Collect text and attachments, then invoke a host callback.
Swap sending for a stop action while streaming.
Wire deployment selection, settings and audio transcription.
02
Conversation input
lib-conversation-input-02

### Notes:
Slide ID: lib-conversation-input-02

Start with a concrete caller need. Send a message: Collect text and attachments, then invoke a host callback. Control generation: Swap sending for a stop action while streaming. Support rich input: Wire deployment selection, settings and audio transcription. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/conversation-input/README.md:1-355
libs/conversation-input/src/index.ts:1-35
libs/conversation-input/package.json:1-42
libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78 — ConversationInput
libs/conversation-input/src/models/ConversationInput.ts:182-455 — ConversationInputProps

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
User input
Conversation Input
on Send
Host workflow

Text, files or voice
Local composition
Text and attachments
Persist and stream
Library: Composer interaction, local text/attachment state and input controls.
03
Conversation input
lib-conversation-input-03

### Notes:
Slide ID: lib-conversation-input-03

The library owns Composer interaction, local text/attachment state and input controls. The host owns Model data, upload and transcription services, sending and generation state.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/conversation-input/README.md:1-355
libs/conversation-input/src/index.ts:1-35
libs/conversation-input/package.json:1-42
libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78 — ConversationInput
libs/conversation-input/src/models/ConversationInput.ts:182-455 — ConversationInputProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
ConversationInput · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| onSend (optional) | ((message: string, attachments: Attachment[]) => void) |
| onUploadAttachment (optional) | ((attachment: Attachment) => Promise<UploadedAttachmentResult>) |
| isStreaming (optional) | boolean |
| onStop (optional) | (() => void) |
04
Conversation input
lib-conversation-input-04

### Notes:
Slide ID: lib-conversation-input-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/conversation-input/README.md:1-355
libs/conversation-input/src/index.ts:1-35
libs/conversation-input/package.json:1-42
libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78 — ConversationInput
libs/conversation-input/src/models/ConversationInput.ts:182-455 — ConversationInputProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function ComposerDemo() {
  const [sent, setSent] = useState('');
  return <>
    <ConversationInput placeholder="Write a demo message"
      onSend={(message) => setSent(message)} />
    <p role="status">{sent ? `Last demo message: ${sent}` : 'Ready'}</p>
  </>;
}
Full example: examples/conversation-input.tsx · uses @epam/ai-dial-conversation-input
05
Conversation input
lib-conversation-input-05

### Notes:
Slide ID: lib-conversation-input-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/conversation-input.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Collect text and attachments, then invoke a host callback. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/conversation-input/README.md:1-355
libs/conversation-input/src/index.ts:1-35
libs/conversation-input/package.json:1-42
libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78 — ConversationInput
libs/conversation-input/src/models/ConversationInput.ts:182-455 — ConversationInputProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep conversation input focused on its public responsibility.

01
02
03
Collect intent
Start the request
Reflect generation
Let the composer gather text and emit onSend.
The host chooses the conversation and calls its adapter.
Pass the current input and generation state back to the UI.
06
Conversation input
lib-conversation-input-06

### Notes:
Slide ID: lib-conversation-input-06

Follow this concrete integration sequence. Collect intent: Let the composer gather text and emit onSend. Start the request: The host chooses the conversation and calls its adapter. Reflect generation: Pass the current input and generation state back to the UI. The complete typed module in examples/conversation-input.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/conversation-input/README.md:1-355
libs/conversation-input/src/index.ts:1-35
libs/conversation-input/package.json:1-42
libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78 — ConversationInput
libs/conversation-input/src/models/ConversationInput.ts:182-455 — ConversationInputProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Controlled updates
Separate attachment UI
Voice extension
messageRevision and textInsertion coordinate host-driven edits.
Import attachment cards and trays from attachment-input.
Inject a transcription callback and supported deployment data.
07
Conversation input
lib-conversation-input-07

### Notes:
Slide ID: lib-conversation-input-07

Customization comes from the current exports and prop declarations. Controlled updates: messageRevision and textInsertion coordinate host-driven edits. Separate attachment UI: Import attachment cards and trays from attachment-input. Voice extension: Inject a transcription callback and supported deployment data. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/conversation-input/README.md:1-355
libs/conversation-input/src/index.ts:1-35
libs/conversation-input/package.json:1-42
libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78 — ConversationInput
libs/conversation-input/src/models/ConversationInput.ts:182-455 — ConversationInputProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/hooks/conversation/useAudioTranscription.ts |
| Test evidence | uses default label when no deployment is selected |
| Test evidence | transcribes actual browser MIME and releases microphone before recognition completes |
08
Conversation input
lib-conversation-input-08

### Notes:
Slide ID: lib-conversation-input-08

Actual consumers: apps/chat/src/hooks/conversation/useAudioTranscription.ts; libs/navigation-panel/src/components/NavigationSheet/NavigableBottomSheet.tsx; apps/chat/src/hooks/keyboard-shortcut/useKeyboardShortcutPreference.ts; apps/chat/src/pages/SettingsPage/PreferencesTab/PreferencesTab.tsx; apps/chat/src/hooks/navigation/useNavigationMenuGroups.tsx; libs/skills/src/hooks/useSkillSelectorOverlay/useSkillSelectorOverlay.tsx. Existing test evidence: [{"file": "libs/conversation-input/src/hooks/tests/useModelSelector.spec.tsx", "assertions": ["useModelSelector \u2014 selectorAriaLabel", "uses default label when no deployment is selected", "appends selected item displayName to the label", "uses custom ariaLabel from modelSelectorLabels", "falls back to item id when displayName is absent", "useModelSelector \u2014 menuItems", "returns empty array when deployments is undefined", "returns empty array when deployments is empty and no state label", "returns seven disabled skeleton items when deployments are loading", "prefers loading label over error and empty labels", "shows skeleton items during a reload even when deployments already exist", "falls back to error label when loading is absent", "returns one item per deployment preserving input order", "updates the active item when selectedDeploymentId changes", "item onClick calls onDeploymentChange with item id"]}, {"file": "libs/conversation-input/src/hooks/tests/useVoiceRecorder.spec.ts", "assertions": ["useVoiceRecorder", "transcribes actual browser MIME and releases microphone before recognition completes", "attaches audio when no recognition callback is provided", "ignores an old result after discard and a new recording", "shows failures and lets discard restore idle state", "releases microphone if permission resolves after unmount", "complete recording", "waits for Stop and sends all blobs as one file exactly once", "does not recognize a discarded recording", "ignores final browser events after cancellation", "releases late microphone permission after Stop without recognition"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-conversation-input:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/conversation-input/README.md:1-355
libs/conversation-input/src/index.ts:1-35
libs/conversation-input/package.json:1-42
libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78 — ConversationInput
libs/conversation-input/src/models/ConversationInput.ts:182-455 — ConversationInputProps
apps/chat/src/hooks/conversation/useAudioTranscription.ts:1-100
libs/conversation-input/src/hooks/tests/useModelSelector.spec.tsx:1-309
libs/conversation-input/src/hooks/tests/useVoiceRecorder.spec.ts:1-265

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
No completion client
Provider assumptions
Avoid state resets
onSend is the integration point for a real generation flow.
Feature-specific settings and menus need caller-supplied data.
Keep initialization and host insertion changes intentional.
09
Conversation input
lib-conversation-input-09

### Notes:
Slide ID: lib-conversation-input-09

Review these constraints before choosing the library. No completion client: onSend is the integration point for a real generation flow. Provider assumptions: Feature-specific settings and menus need caller-supplied data. Avoid state resets: Keep initialization and host insertion changes intentional. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/conversation-input/README.md:1-355
libs/conversation-input/src/index.ts:1-35
libs/conversation-input/package.json:1-42
libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78 — ConversationInput
libs/conversation-input/src/models/ConversationInput.ts:182-455 — ConversationInputProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.