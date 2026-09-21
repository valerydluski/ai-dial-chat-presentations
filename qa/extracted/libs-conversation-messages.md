<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Conversation messages
Render a transcript from host-owned messages and actions.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-conversation-messages
01
Conversation messages
lib-conversation-messages-01

### Notes:
Slide ID: lib-conversation-messages-01

This session explains render a transcript from host-owned messages and actions. The library is a local private workspace package at libs/conversation-messages. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/conversation-messages/README.md:1-236
libs/conversation-messages/src/index.ts:1-35
libs/conversation-messages/package.json:1-41
libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236 — AssistantMessageBubble
libs/conversation-messages/src/models/message-bubble.ts:143-170 — AssistantMessageBubbleProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Render a transcript from host-owned messages and actions.

01
02
03
Display roles
Reveal a response
Compose evidence
Use user, assistant and status bubble variants.
Render updated Markdown while a generation is active.
Place stages, citations and attachments beside the answer.
02
Conversation messages
lib-conversation-messages-02

### Notes:
Slide ID: lib-conversation-messages-02

Start with a concrete caller need. Display roles: Use user, assistant and status bubble variants. Reveal a response: Render updated Markdown while a generation is active. Compose evidence: Place stages, citations and attachments beside the answer. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/conversation-messages/README.md:1-236
libs/conversation-messages/src/index.ts:1-35
libs/conversation-messages/package.json:1-41
libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236 — AssistantMessageBubble
libs/conversation-messages/src/models/message-bubble.ts:143-170 — AssistantMessageBubbleProps

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
Host message
Assistant bubble
User action
Host callback

Text and display props
Markdown and slots
Copy, rate or regenerate
Perform domain behavior
Library: Bubble layout, Markdown display and action controls.
03
Conversation messages
lib-conversation-messages-03

### Notes:
Slide ID: lib-conversation-messages-03

The library owns Bubble layout, Markdown display and action controls. The host owns Message ordering, network streams, persistence, ratings and attachment access.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/conversation-messages/README.md:1-236
libs/conversation-messages/src/index.ts:1-35
libs/conversation-messages/package.json:1-41
libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236 — AssistantMessageBubble
libs/conversation-messages/src/models/message-bubble.ts:143-170 — AssistantMessageBubbleProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
AssistantMessageBubble · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| text (optional) | string |
| isStreaming (optional) | boolean |
| afterContent (optional) | ReactNode |
| onAttachmentClick (optional) | ((attachment: DisplayAttachment) => void) |
04
Conversation messages
lib-conversation-messages-04

### Notes:
Slide ID: lib-conversation-messages-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/conversation-messages/README.md:1-236
libs/conversation-messages/src/index.ts:1-35
libs/conversation-messages/package.json:1-41
libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236 — AssistantMessageBubble
libs/conversation-messages/src/models/message-bubble.ts:143-170 — AssistantMessageBubbleProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function MessageDemo() {
  return <AssistantMessageBubble text="**Demo:** evidence collected."
    isStreaming={false} deploymentDisplayName="Demo assistant"
    afterContent={<StagesPanel stages={[]} isStreaming={false} />} />;
}
Full example: examples/conversation-messages.tsx · uses @epam/ai-dial-conversation-messages
05
Conversation messages
lib-conversation-messages-05

### Notes:
Slide ID: lib-conversation-messages-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/conversation-messages.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Use user, assistant and status bubble variants. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/conversation-messages/README.md:1-236
libs/conversation-messages/src/index.ts:1-35
libs/conversation-messages/package.json:1-41
libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236 — AssistantMessageBubble
libs/conversation-messages/src/models/message-bubble.ts:143-170 — AssistantMessageBubbleProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep conversation messages focused on its public responsibility.

01
02
03
Prepare a message
Compose evidence
Connect actions
The host supplies response text and streaming state.
Insert StagesPanel through the afterContent slot.
Keep regeneration, feedback and persistence in the host.
06
Conversation messages
lib-conversation-messages-06

### Notes:
Slide ID: lib-conversation-messages-06

Follow this concrete integration sequence. Prepare a message: The host supplies response text and streaming state. Compose evidence: Insert StagesPanel through the afterContent slot. Connect actions: Keep regeneration, feedback and persistence in the host. The complete typed module in examples/conversation-messages.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/conversation-messages/README.md:1-236
libs/conversation-messages/src/index.ts:1-35
libs/conversation-messages/package.json:1-41
libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236 — AssistantMessageBubble
libs/conversation-messages/src/models/message-bubble.ts:143-170 — AssistantMessageBubbleProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Extension slots
Host URL rewriting
Transcript controls
beforeContent and afterContent add skill chips or stage panels.
markdownUrlTransform maps resource references before rendering.
Supply MessageActions props and localized action labels.
07
Conversation messages
lib-conversation-messages-07

### Notes:
Slide ID: lib-conversation-messages-07

Customization comes from the current exports and prop declarations. Extension slots: beforeContent and afterContent add skill chips or stage panels. Host URL rewriting: markdownUrlTransform maps resource references before rendering. Transcript controls: Supply MessageActions props and localized action labels. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/conversation-messages/README.md:1-236
libs/conversation-messages/src/index.ts:1-35
libs/conversation-messages/package.json:1-41
libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236 — AssistantMessageBubble
libs/conversation-messages/src/models/message-bubble.ts:143-170 — AssistantMessageBubbleProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/components/ConversationView/ConversationMessageItem.tsx |
| Test evidence | calls onEdit when Edit button is clicked |
| Test evidence | marks the bubble that wraps the message text |
08
Conversation messages
lib-conversation-messages-08

### Notes:
Slide ID: lib-conversation-messages-08

Actual consumers: apps/chat/src/components/ConversationView/ConversationMessageItem.tsx; apps/chat/src/components/ConversationView/ConversationView.tsx; apps/chat/src/components/ConversationView/utils/build-message-actions.ts. Existing test evidence: [{"file": "libs/conversation-messages/src/components/MessageActions/tests/MessageActions.spec.tsx", "assertions": ["MessageActions", "role=User (default)", "renders Edit and Delete buttons", "does not render Agent action buttons", "calls onEdit when Edit button is clicked", "calls onDelete when Delete button is clicked", "role=Assistant", "renders Regenerate, Copy, Markdown, Like, and Dislike buttons", "does not render User action buttons", "calls onRegenerate when Regenerate button is clicked", "calls onCopy when Copy button is clicked", "calls onCopyMarkdown when Markdown button is clicked", "calls onLike when Like button is clicked", "calls onDislike when Dislike button is clicked", "isDisabled"]}, {"file": "libs/conversation-messages/src/components/MessageBubble/tests/MessageBubble.classes.spec.tsx", "assertions": ["UserMessageBubble \u2014 public class names", "marks the bubble that wraps the message text", "emits no bubble class when there is no text or before-content", "keeps a caller-supplied bubbleClassName alongside the public class", "AssistantMessageBubble \u2014 public class names", "marks the live content region for a settled message", "marks the live content region while streaming"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-conversation-messages:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: calls onEdit when Edit button is clicked.

Sources:
libs/conversation-messages/README.md:1-236
libs/conversation-messages/src/index.ts:1-35
libs/conversation-messages/package.json:1-41
libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236 — AssistantMessageBubble
libs/conversation-messages/src/models/message-bubble.ts:143-170 — AssistantMessageBubbleProps
apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898
libs/conversation-messages/src/components/MessageActions/tests/MessageActions.spec.tsx:1-269
libs/conversation-messages/src/components/MessageBubble/tests/MessageBubble.classes.spec.tsx:1-92

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Streaming is visual
Status messages
Source integrations
isStreaming does not open a network stream.
Shared MessageRole.Status is a UI event, not an upstream author role.
Citation components and canvas actions require host wiring.
09
Conversation messages
lib-conversation-messages-09

### Notes:
Slide ID: lib-conversation-messages-09

Review these constraints before choosing the library. Streaming is visual: isStreaming does not open a network stream. Status messages: Shared MessageRole.Status is a UI event, not an upstream author role. Source integrations: Citation components and canvas actions require host wiring. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/conversation-messages/README.md:1-236
libs/conversation-messages/src/index.ts:1-35
libs/conversation-messages/package.json:1-41
libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236 — AssistantMessageBubble
libs/conversation-messages/src/models/message-bubble.ts:143-170 — AssistantMessageBubbleProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.