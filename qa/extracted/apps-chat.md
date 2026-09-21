<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Chat frontend
The React application that assembles reusable features into a coherent workspace.

React SPA
Application adapters
Port 4207
apps/chat · @epam/chat
01
Chat frontend
apps-chat-01

### Notes:
Slide ID: apps-chat-01

This application owns integration, including providers, routing, language, theme, configured API clients and feature availability. Its role is broader than any one component library.

Sources:
apps/chat/src/main.tsx:1-108
apps/chat/src/app/app.tsx:1-582

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
The frontend owns the user workflow

01
02
03
Conversation workspace
Knowledge workflows
Operations for users
Send messages, resume history and inspect sources.
Browse and edit prompts, skills, apps and toolsets.
Inspect usage, manage files and work with scheduled tasks.
02
Chat frontend
apps-chat-02

### Notes:
Slide ID: apps-chat-02

The route enum and app route registration are the current scope. User-visible capabilities can be gated by server configuration and deployment support.

Sources:
apps/chat/src/types/routes.ts:1-30

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 3 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Bootstrap the application once

01
02
03
04
main.tsx
Browser Router
Providers
App

React root and imports
App-owned routes
User, theme and config
Feature route composition
AttachmentCanvasProvider sits above the routed workspace.
03
Chat frontend
apps-chat-03

### Notes:
Slide ID: apps-chat-03

main.tsx imports base styles and i18n, creates the tooltip portal, and nests providers before rendering App. RequireAuth guards the main workspace. Login and overlay-close routes are mounted at the higher routing layer.

Sources:
apps/chat/src/main.tsx:1-108
apps/chat/src/app/app.tsx:1-582

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Providers define state ownership

01
02
03
Identity and configuration
Conversation state
Workspace presentation
UserProvider, AppConfigProvider and UiFeaturesProvider.
ConversationsProvider, GenerationProvider and ClientChannelProvider.
Theme, sources-sidebar and attachment-canvas providers.
04
Chat frontend
apps-chat-04

### Notes:
Slide ID: apps-chat-04

These are actual provider names from the entry point. Do not move them into libraries to simplify imports. When reusing a component independently, replace the relevant application adapter with explicitly supplied data and callbacks.

Sources:
apps/chat/src/main.tsx:1-108

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Routes connect reusable screens
| Route family | Host responsibility |
| --- | --- |
| /conversations | Active conversation and history |
| /catalog, /files | Discovery and file operations |
| /prompt-editor, /skill-editor | Load, validate and save authored entities |
| /scheduled-tasks, /settings | Scheduling and usage/settings views |
05
Chat frontend
apps-chat-05

### Notes:
Slide ID: apps-chat-05

ROUTES declares more specific variants for edit/detail/callback and invitations. Many route components use React.lazy and Suspense; the conversation page is eagerly prefetched before its lazy wrapper. Do not document every route as loaded in the same way.

Sources:
apps/chat/src/types/routes.ts:1-30
apps/chat/src/app/app.tsx:1-582

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Trace a message from UI intent

01
02
03
04
Composer
Conversation Page
Stream hook
chat-stream adapter

Message and attachments
Host handlers
State and updates
Transport dependencies
The backend owns persistent conversation writes.
06
Chat frontend
apps-chat-06

### Notes:
Slide ID: apps-chat-06

The page supplies the stream hook and input components with state derived from app contexts. createChatStreamApi receives host paths and CSRF callbacks from the app adapter. Generation result updates flow back into the message components, while persistence remains in the BFF. The stream-hook node is useConversationStream; the concise node label avoids excessive wrapping.

Sources:
apps/chat/src/pages/Conversation/Conversation.tsx:1-757
apps/chat/src/server-api/chat-stream.api.ts:1-17
libs/chat-hooks/src/conversation/useConversationStream/useConversationStream.ts:1-606

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Configure the generated client at the edge
Source excerpt · createApiConfiguration in server-api/api-client.ts.

new Configuration({
  basePath: '',
  credentials: 'include',
  middleware: [
    csrfMiddleware,
    unauthorizedMiddleware,
    telemetryMiddleware,
  ],
});
07
Chat frontend
apps-chat-07

### Notes:
Slide ID: apps-chat-07

The middleware variables are defined in the source file, not globals. CSRF and unauthorized behavior are supplied through callback-based factories from chat-hooks, with browser/session state remaining app-owned. Full source-linked contract information is in the bundle index.

Sources:
apps/chat/src/server-api/api-client.ts:1-106

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Assemble evidence around each message

01
02
03
Transcript
Sources
Canvas
The app message container composes bubbles and stages.
The app sources container adapts evidence data and open actions.
The app resolves files and passes renderer dependencies.
08
Chat frontend
apps-chat-08

### Notes:
Slide ID: apps-chat-08

These application containers connect source-derived message data to generic display components. URL resolution, PDF worker setup and feature flags should be inspected at this edge rather than inferred from the presentation component alone.

Sources:
apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898
apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:1-354
apps/chat/src/app/app.tsx:1-582

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Theme, locale and viewport are host concerns

01
02
03
ThemeProvider
i18n initialization
Responsive branches
Loads theme configuration and writes CSS variables.
Registers English and updates html direction on language changes.
App hooks provide mobile/desktop decisions to feature surfaces.
09
Chat frontend
apps-chat-09

### Notes:
Slide ID: apps-chat-09

The frontend currently registers only English translations. RTL direction switching exists for four base language codes. This is support infrastructure, not a claim of complete translated Arabic UI. Component demos in this bundle use English and clearly identified synthetic data.

Sources:
apps/chat/src/context/ThemeContext.tsx:1-171
apps/chat/src/i18n/config.ts:1-32
apps/chat/src/hooks/breakpoint/useBreakpoint.ts:1-89

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
A concrete extension: message content slots
Runnable composition pattern from examples/conversation-messages.tsx.

<AssistantMessageBubble
  text="**Demo:** evidence collected."
  isStreaming={false}
  deploymentDisplayName="Demo assistant"
  afterContent={
    <StagesPanel stages={[]} isStreaming={false} />
  }
/>
10
Chat frontend
apps-chat-10

### Notes:
Slide ID: apps-chat-10

The complete checked example imports both components and stylesheets. afterContent renders between the message body and actions. Replace the empty demo stages with the host message stages; no backend code change is required to use the slot.

Sources:
libs/conversation-messages/src/models/message-bubble.ts:1-177
apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 11 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Inspect the reusable pieces in isolation
Reproducible demo · actual workspace source components

![assets/component-demo.png](Image1.jpg)

A focused demo
Use a small host to inspect component contracts before wiring application state and backend behavior.
DEMO · real components rendered from this source snapshot
11
Chat frontend
apps-chat-15

### Notes:
Slide ID: apps-chat-15

This is a real browser screenshot of the standalone demo in demo/main.tsx, captured by src/capture-demo.mjs. It renders SettingsPanel, UsageLimitCard and StagesPanel directly from the recorded source snapshot with local stylesheet dependencies. It is an illustrative host, not a screenshot of a deployed DIAL product. All data is synthetic and no backend request is made. Run the Vite command in examples/README.md, then the capture script. Expected behavior: Usage starts selected; selecting Profile updates the controlled active row. The amount and stage remain demo data. The host explicitly supplies dark-theme color overrides. Desktop and phone captures are retained under assets/.

Sources:
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 12 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Run and build the frontend
Commands run from the repository root.

npm start
# Vite: http://localhost:4207
# /api is proxied to http://localhost:5000

npm exec nx run @epam/chat:build
npm exec nx run @epam/chat:typecheck
npm exec nx run @epam/chat:test
12
Chat frontend
apps-chat-11

### Notes:
Slide ID: apps-chat-11

Nx resolves the application name as @epam/chat. npm start uses the supported chat alias. These commands are provided for the reader; no source build or application dependency installation was performed for this documentation task. Vite configuration and the graph, rather than an old README project count, determine the targets.

Sources:
package.json:1-199
apps/chat/vite.config.mts:1-267

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 13 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Inspect behavior through existing tests
| Test area | Evidence |
| --- | --- |
| Conversation route | ConversationRoute integration and unit specs |
| Message composition | ConversationMessageItem specs |
| Provider behavior | OverlayContext and app-level context specs |
| API adapters | server-api tests for transport integration |
13
Chat frontend
apps-chat-12

### Notes:
Slide ID: apps-chat-12

Tests are inspected evidence, not newly executed application suite results. For a future code change, select the relevant Nx test target or npm run test:file. Presentation example modules were checked independently with strict TypeScript against the same source exports.

Sources:
apps/chat/src/pages/ConversationRoute/ConversationRoute.integration.spec.tsx:1-332
apps/chat/src/components/ConversationView/tests/ConversationMessageItem.spec.tsx:1-1491
apps/chat/src/context/overlay/tests/OverlayContext.spec.tsx:1-1443

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 14 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Integration limits are part of the design

01
02
03
Providers are coupled
Backend required
Some adapter gaps remain
The full app composition has many coordinated state owners.
A running UI alone cannot authenticate or complete conversations.
Audio transcription retains a documented raw DTO wrapper.
14
Chat frontend
apps-chat-13

### Notes:
Slide ID: apps-chat-13

The raw transcription wrapper documents the customContent versus custom_content schema collision. Do not claim every HTTP call is generated. For a smaller host, adopt a component or focused hook entry before copying the entire provider tree.

Sources:
apps/chat/src/main.tsx:1-108
apps/chat/src/server-api/chat.api.ts:1-42
apps/chat-api/README.md:1-1047

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 15 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Follow one feature end to end

01
02
03
04
Route
Container
Library contract
Server adapter

Choose a user workflow
Resolve context and data
Render and emit intent
Perform the operation
Start in apps/chat/src/pages, then follow imports into libs and server-api.
15
Chat frontend
apps-chat-14

### Notes:
Slide ID: apps-chat-14

PromptEditor is a manageable example: the app loads and saves the entity while the library owns the fields. The same tracing method scales to conversations. Consult each library deck for the exact exported prop and callback contract.

Sources:
apps/chat/src/pages/PromptEditor/PromptEditor.tsx:1-282
apps/chat/src/server-api/api-client.ts:1-106
libs/prompt-editor/src/models/prompt-editor-props.ts:1-162

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.