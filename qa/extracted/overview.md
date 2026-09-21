<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
AI DIAL Chat
A modular chat application, a backend edge, and reusable workspace libraries.

4 applications
28 libraries
33 technical sessions
Source snapshot 23fa39459d89 · 2026-09-21
01
AI DIAL Chat
overview-01

### Notes:
Slide ID: overview-01

This series is grounded in the local working tree and Nx graph. It includes one overview plus one deck per application and library. The auxiliary attachment-canvas-consumer-fixture project is in the Nx graph but is not a separate app/library topic. Publishing scripts remain auxiliary tooling. Untracked skill and OpenSpec artifacts are recorded in the manifest. No performance benchmark or production-readiness assertion is made.

Sources:
docs/architecture.md:1-765
package.json:1-199

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Start with the user workflows

01
02
03
Converse with context
Reuse knowledge
Manage shared work
Choose a deployment, attach files, send messages and inspect evidence.
Browse prompts and skills, then apply them to a conversation.
Share or publish resources and inspect scheduled task runs.
02
AI DIAL Chat
overview-02

### Notes:
Slide ID: overview-02

The route tree and conversation assembly expose the user workflows shown here. Individual UI libraries implement parts of these flows, while the app supplies state, permissions and backend behavior. Some capabilities depend on configuration and the selected deployment; route existence is not a guarantee that every user can access every feature.

Sources:
apps/chat/src/types/routes.ts:1-30
apps/chat/src/pages/Conversation/Conversation.tsx:1-757

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 3 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Four apps have different responsibilities
| Application | Responsibility |
| --- | --- |
| chat | React SPA and application integration |
| chat-api | NestJS BFF, auth, persistence and Core access |
| chat-overlay-sandbox | Browser host for overlay integration cases |
| mcp-app-sandbox | Separate-origin sandbox proxy for MCP UI |
03
AI DIAL Chat
overview-03

### Notes:
Slide ID: overview-03

Nx resolves four non-empty projects under apps. The two sandboxes have different purposes: overlay-sandbox is a developer demonstration host, whereas mcp-app-sandbox serves the isolated proxy page required by MCP Apps rendering. Do not merge them into a single deployment assumption.

Sources:
apps/chat/README.md:1-392
apps/chat-api/README.md:1-1047
apps/chat-overlay-sandbox/README.md:1-73
apps/mcp-app-sandbox/README.md:1-60

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Libraries for the conversation workspace

01
02
03
Conversation
Evidence
Navigation
conversation-input, conversation-messages, conversation-panel, conversation-stages
attachment-input, attachment-canvas, source-panel, quotations
navigation-panel, sidebar, starter-buttons, settings-panel
04
AI DIAL Chat
overview-04

### Notes:
Slide ID: overview-04

These twelve libraries form the main conversation workspace. The input emits send intent, messages display state, history selects conversations, and stages display intermediate progress. Evidence viewers are kept distinct from transport and source derivation. Navigation and sidebar shells let an embedding host choose its own routing and layout.

Sources:
libs/conversation-input/src/index.ts:1-35
libs/attachment-canvas/src/index.ts:1-89
libs/navigation-panel/src/index.ts:1-54

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Libraries for knowledge and integration

01
02
03
Author and discover
Automate and distribute
Integrate and share code
catalog, builder-form, prompt-editor, prompts, skill-editor, skills, toolset-editor
scheduled-tasks, share, publish-panel, usage-dashboard
chat-api-client, chat-hooks, chat-shared, chat-overlay, mcp-apps
05
AI DIAL Chat
overview-05

### Notes:
Slide ID: overview-05

These sixteen libraries complete the set of twenty-eight. The editor packages are distinct from pickers; sharing and publication have separate contracts. The generated client, headless hooks and shared foundations form different layers. Overlay and MCP packages cross browser-frame boundaries and therefore deserve protocol-specific treatment.

Sources:
libs/catalog/src/index.ts:1-157
libs/chat-hooks/src/index.ts:1-184
libs/chat-overlay/src/index.ts:1-4
libs/mcp-apps/src/index.ts:1-31

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Application edges connect the layers
A simplified ownership map, not a complete dependency graph.

01
02
03
04
Host / browser
apps/chat
apps/chat-api
External systems

Optional embedding page
Routes, providers, adapters
Auth and domain services
Core, identity and theme services
UI libraries receive data and behavior through public contracts.
06
AI DIAL Chat
overview-06

### Notes:
Slide ID: overview-06

Frontend and backend apps own external integration. Most UI libraries should not know REST paths, identity-provider setup, storage keys or navigation targets. The generated client is a deliberate exception; chat-hooks has a narrower exception for injected generated operations. Some source dependencies currently exceed the stated rule, so the report separates intended isolation from observed dependencies.

Sources:
AGENTS.md:1-176
apps/chat/src/main.tsx:1-108
apps/chat-api/src/app/app.module.ts:1-79

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
One message enters the backend

01
02
03
04
Conversation Input
Conversation page
App stream adapter
Conversation API

on Send intent
Handlers and stream hook
Host paths and CSRF
POST completions
POST /api/v1/conversations/completions
07
AI DIAL Chat
overview-07

### Notes:
Slide ID: overview-07

The browser hands message intent to the app. The app integrates the headless stream behavior and createChatStreamApi, supplying the conversation base path and CSRF callbacks. This endpoint differs from the direct /api/v1/chat/completions proxy. The backend validates the request and owns the persisted conversation lifecycle.

Sources:
apps/chat/src/pages/Conversation/Conversation.tsx:1-757
apps/chat/src/server-api/chat-stream.api.ts:1-17
libs/chat-hooks/src/conversation/create-chat-stream-api.ts:1-242
apps/chat-api/src/conversations/conversation.controller.ts:1-852

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Chunks return through a shared lifecycle

01
02
03
04
DIAL Core
Backend relay
Stream hook
Message components

Upstream response events
Normalize and persist
Merge message changes
Text, stages and citations
Closing the browser connection is different from explicitly stopping generation.
08
AI DIAL Chat
overview-08

### Notes:
Slide ID: overview-08

Conversation generation is registered by principal and conversation. The backend saves initial and final or partial state, even when the originating tab disconnects. A dedicated stop request aborts generation, while attach supports resuming a view of active output. The registry is in memory; this is an operational constraint, not durable distributed execution.

Sources:
apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773
apps/chat-api/src/conversations/conversation.controller.ts:1-852
libs/chat-hooks/src/conversation/useConversationStream/useConversationStream.ts:1-606

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Separate clients, hooks and adapters
| Layer | Concrete role |
| --- | --- |
| Generated API client | Fetch operations and DTO serialization |
| Headless hooks | Request/UI lifecycles with injected dependencies |
| Application adapters | Client configuration, CSRF, origin and route mapping |
| UI libraries | Render state and emit typed user actions |
09
AI DIAL Chat
overview-09

### Notes:
Slide ID: overview-09

The generated client is not the server-side DIAL TypeScript SDK. It targets this chat BFF. The backend separately uses DialClientService and the DIAL SDK to call Core. Hooks can depend on generated operation signatures under the documented exception, while the configured client instance remains app-owned.

Sources:
libs/chat-api-client/src/generated/src/runtime.ts:1-511
libs/chat-hooks/src/useShareLink/useShareLink.ts:1-109
apps/chat/src/server-api/api-client.ts:1-106
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Compose a view from focused parts

01
02
03
04
Application state
Composer + bubbles
Evidence surfaces
Host callbacks

Messages and deployment
Input and transcript
Stages, citations, canvas
Send, load and navigate
A library can be adopted without copying the whole route implementation.
10
AI DIAL Chat
overview-10

### Notes:
Slide ID: overview-10

The application assembles components around its contexts and hooks. AssistantMessageBubble accepts afterContent, so the same message component can display a stages panel without owning stage fetching. The canvas is controlled through a provider at the app root. This demonstrates a concrete modularity benefit: presentation composition can change without moving the HTTP contract into the component.

Sources:
apps/chat/src/components/ConversationView/ConversationView.tsx:1-1263
apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898
apps/chat/src/pages/Conversation/Conversation.tsx:1-757

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 11 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
See three libraries in one host
Reproducible demo · actual workspace source components

![assets/component-demo.png](Image1.jpg)

Compose a screen
The host selects rows, formats amounts and supplies stage data. Each library renders its own part.
DEMO · real components rendered from this source snapshot
11
AI DIAL Chat
overview-21

### Notes:
Slide ID: overview-21

This is a real browser screenshot of the standalone demo in demo/main.tsx, captured by src/capture-demo.mjs. It renders SettingsPanel, UsageLimitCard and StagesPanel directly from the recorded source snapshot with local stylesheet dependencies. It is an illustrative host, not a screenshot of a deployed DIAL product. All data is synthetic and no backend request is made. Run the Vite command in examples/README.md, then the capture script. Expected behavior: Usage starts selected; selecting Profile updates the controlled active row. The amount and stage remain demo data. The host explicitly supplies dark-theme color overrides. Desktop and phone captures are retained under assets/.

Sources:
libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170
libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191
libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 12 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Choose a reuse boundary

01
02
03
Reuse a component
Build a custom UI
Embed the full app
Bring typed data, callbacks, labels and its stylesheet.
Use chat-hooks and configured generated operations.
Use ChatOverlay with an existing chat deployment.
12
AI DIAL Chat
overview-11

### Notes:
Slide ID: overview-11

All twenty-eight source manifests are private in this snapshot. The verified path is the current workspace with its aliases and Nx graph. Publish and pack tooling exists, but a tag or script is not proof of npm availability. For a separate host, validate the produced package and its peer matrix before proposing installation.

Sources:
AGENTS.md:1-176
libs/chat-hooks/package.json:1-266
libs/chat-overlay/README.md:1-307
tools/publish-lib.mjs:1-282

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 13 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Theme tokens travel from host to component

01
02
03
04
Theme service
BFF theme proxy
Theme Provider
Library styles

config.json and images
/api/themes
CSS vars on html
Tokens and overrides
Theme selection is app-owned; reusable libraries consume resolved styling.
13
AI DIAL Chat
overview-12

### Notes:
Slide ID: overview-12

The actual ThemeController is unversioned and exposes /api/themes and /api/themes/icon despite the broader business-route versioning rule. ThemeProvider sets colors as CSS variables. Library props can override local variables, and stable public classes support host styling. The supplied favicon is copied from the adjacent SDK website unchanged.

Sources:
docs/theme-customization.md:1-396
apps/chat-api/src/themes/theme.controller.ts:1-131
apps/chat/src/context/ThemeContext.tsx:1-171
libs/chat-shared/src/utils/build-css-vars.ts:1-14

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 14 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Localization support has a clear current limit

01
02
03
English resources
RTL switching
Host-localized libraries
The current i18n initialization registers en translations.
ar, he, fa and ur set document direction to rtl.
Labels and logical CSS keep language ownership at the edge.
14
AI DIAL Chat
overview-13

### Notes:
Slide ID: overview-13

Do not equate RTL direction handling with a completed Arabic translation. The current config imports only en.json and falls back to English. The direction hook updates both html.lang and html.dir on language changes. The repository instructions require RTL and accessibility support, but this bundle does not claim a full accessibility conformance audit.

Sources:
apps/chat/src/i18n/config.ts:1-32
AGENTS.md:1-176
libs/navigation-panel/src/models/navigation-panel-props.ts:1-73

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 15 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Authentication belongs at the BFF

01
02
03
04
Browser
Session guard
Identity provider
Core request

Opaque session cookie
Validate and refresh
OIDC code flow
Verified user token
Configured clients and session details stay outside ordinary UI libraries.
15
AI DIAL Chat
overview-14

### Notes:
Slide ID: overview-14

The default browser flow uses an encrypted HttpOnly session cookie. The backend performs OIDC and refreshes tokens; JavaScript receives user state rather than access or refresh tokens. A separately configured header-token strategy exists. Secure cookie and same-site behavior depend on deployment and overlay mode. This is a description of this source, not general identity-provider setup guidance.

Sources:
docs/auth/auth-bff-encrypted-cookie.md:1-442
apps/chat-api/src/auth/session/session.guard.ts:1-112
apps/chat-api/src/auth/session/session.service.ts:1-58
apps/chat-api/src/auth/refresh/refresh.service.ts:1-115

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 16 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Two upstream APIs share the browser stream
Server flag: RESPONSES_API_ENABLED · deployment feature: responsesApi
| Server flag and deployment | Upstream path |
| --- | --- |
| Server flag = false | Chat Completions |
| Flag true; capability missing/false | Chat Completions |
| Flag true; responsesApi = true | Responses adapter |
16
AI DIAL Chat
overview-15

### Notes:
Slide ID: overview-15

Both the server operator flag and the deployment capability must be true to select Responses. The resolver function alone checks only the capability, so reading it without its caller gives an incomplete rule. The BFF normalizes upstream events to the browser contract. There is no automatic retry through the other API after an error.

Sources:
docs/responses-api-integration.md:1-460
apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773
apps/chat-api/src/conversations/generation/generation-api.ts:1-27

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 17 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Run the applications locally
From the repository root, after configuring backend environment values.

npm ci
npm run start:all

# Frontend: http://localhost:4207
# Backend:  http://localhost:5000

npm exec nx serve chat-overlay-sandbox
npm run start:mcp-app-sandbox
Use a Node version compatible with the locked Nx/Vite stack.
17
AI DIAL Chat
overview-16

### Notes:
Slide ID: overview-16

These are documented commands, not operations run against the source repository for this task. Configure DIAL_CORE_URL and the required auth/session settings from apps/chat-api/README.md and .env.template. Configure MCP_APP_SANDBOX_ALLOWED_HOST_ORIGINS before using the separate sandbox. npm ci modifies the consuming checkout, so it is shown for reproducibility and was not run here.

Sources:
package.json:1-199
apps/chat/vite.config.mts:1-267
apps/chat-api/README.md:1-1047
apps/mcp-app-sandbox/README.md:1-60

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 18 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Use the checks that match the change
| Purpose | Repository command |
| --- | --- |
| Types, lint and tests | npm run verify:full |
| Build the apps/libraries | npm run build:all |
| Check docs and manifests | npm run validate:docs |
| Check generated client drift | npm run openapi:check |
18
AI DIAL Chat
overview-17

### Notes:
Slide ID: overview-17

The repository scripts use Nx targets and affected project selection. The lint script itself applies fixes, while lint:check is the non-mutating alternative used in verification. Full workspace builds and suites were not run for this output-only task. The presentation bundle has its own generation, structural, rendering and example checks.

Sources:
package.json:1-199
nx.json:1-121

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 19 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Modularity gives specific engineering benefits

01
02
03
One editor field set
Reusable evidence UI
Replaceable host behavior
builder-form validation and fields are reused by multiple editors.
The same canvas displays several typed content kinds.
Callbacks let a host choose its own routing and persistence.
19
AI DIAL Chat
overview-18

### Notes:
Slide ID: overview-18

These are source-backed structural benefits. Shared validation reduces duplicated rule implementations; typed renderers centralize content display; explicit callbacks permit a different host behavior. No speedup, maintenance percentage, adoption count or benchmark is inferred from this structure.

Sources:
libs/builder-form/src/index.ts:1-65
libs/toolset-editor/src/components/GeneralForm/GeneralForm.tsx:1-151
libs/attachment-canvas/src/models/attachment-canvas.ts:1-620
apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 20 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Tradeoffs remain visible

01
02
03
Integration is real work
Boundaries have drift
Runtime state is local
A host must supply data, labels, adapters and the correct peer dependencies.
Some current libs import broader packages than the written rules permit.
Generation and several caches rely on process/browser memory.
20
AI DIAL Chat
overview-19

### Notes:
Slide ID: overview-19

Isolation is a useful design constraint but not a description of every current import. The quality report records concrete counterexamples. Stateful runtime mechanisms also impose deployment and lifecycle concerns. Use these limitations when deciding between component reuse and full-app embedding.

Sources:
AGENTS.md:1-176
libs/toolset-editor/package.json:1-41
libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts:1-494
apps/chat-api/src/conversations/conversation-generation.service.ts:1-340

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 21 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  REPOSITORY OVERVIEW
Start with a vertical path through the code

01
02
03
Understand the assembly
Trace its contract
Reuse one piece
Read main.tsx, app.tsx and one conversation or editor route.
Follow a component prop into the host adapter and backend domain.
Open that library deck, its full example and its source references.
21
AI DIAL Chat
overview-20

### Notes:
Slide ID: overview-20

The series index links all thirty-three decks and their previews. Each library deck includes a diagram, a checked example and source locators. Use manifest.json to see generation and verification status, and qa-report.md to understand the scope and remaining limits. Source paths refer to the recorded working tree snapshot.

Sources:
apps/chat/src/main.tsx:1-108
apps/chat/src/app/app.tsx:1-582
apps/chat/src/server-api/api-client.ts:1-106

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.