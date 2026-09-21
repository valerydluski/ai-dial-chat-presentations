# Speaker notes

English notes for the complete technical series.

## overview-01 — AI DIAL Chat

This series is grounded in the local working tree and Nx graph. It includes one overview plus one deck per application and library. The auxiliary attachment-canvas-consumer-fixture project is in the Nx graph but is not a separate app/library topic. Publishing scripts remain auxiliary tooling. Untracked skill and OpenSpec artifacts are recorded in the manifest. No performance benchmark or production-readiness assertion is made.

Sources: docs/architecture.md:1-765; package.json:1-199

## overview-02 — Start with the user workflows

The route tree and conversation assembly expose the user workflows shown here. Individual UI libraries implement parts of these flows, while the app supplies state, permissions and backend behavior. Some capabilities depend on configuration and the selected deployment; route existence is not a guarantee that every user can access every feature.

Sources: apps/chat/src/types/routes.ts:1-30; apps/chat/src/pages/Conversation/Conversation.tsx:1-757

## overview-03 — Four apps have different responsibilities

Nx resolves four non-empty projects under apps. The two sandboxes have different purposes: overlay-sandbox is a developer demonstration host, whereas mcp-app-sandbox serves the isolated proxy page required by MCP Apps rendering. Do not merge them into a single deployment assumption.

Sources: apps/chat/README.md:1-392; apps/chat-api/README.md:1-1047; apps/chat-overlay-sandbox/README.md:1-73; apps/mcp-app-sandbox/README.md:1-60

## overview-04 — Libraries for the conversation workspace

These twelve libraries form the main conversation workspace. The input emits send intent, messages display state, history selects conversations, and stages display intermediate progress. Evidence viewers are kept distinct from transport and source derivation. Navigation and sidebar shells let an embedding host choose its own routing and layout.

Sources: libs/conversation-input/src/index.ts:1-35; libs/attachment-canvas/src/index.ts:1-89; libs/navigation-panel/src/index.ts:1-54

## overview-05 — Libraries for knowledge and integration

These sixteen libraries complete the set of twenty-eight. The editor packages are distinct from pickers; sharing and publication have separate contracts. The generated client, headless hooks and shared foundations form different layers. Overlay and MCP packages cross browser-frame boundaries and therefore deserve protocol-specific treatment.

Sources: libs/catalog/src/index.ts:1-157; libs/chat-hooks/src/index.ts:1-184; libs/chat-overlay/src/index.ts:1-4; libs/mcp-apps/src/index.ts:1-31

## overview-06 — Application edges connect the layers

Frontend and backend apps own external integration. Most UI libraries should not know REST paths, identity-provider setup, storage keys or navigation targets. The generated client is a deliberate exception; chat-hooks has a narrower exception for injected generated operations. Some source dependencies currently exceed the stated rule, so the report separates intended isolation from observed dependencies.

Sources: AGENTS.md:1-176; apps/chat/src/main.tsx:1-108; apps/chat-api/src/app/app.module.ts:1-79

## overview-07 — One message enters the backend

The browser hands message intent to the app. The app integrates the headless stream behavior and createChatStreamApi, supplying the conversation base path and CSRF callbacks. This endpoint differs from the direct /api/v1/chat/completions proxy. The backend validates the request and owns the persisted conversation lifecycle.

Sources: apps/chat/src/pages/Conversation/Conversation.tsx:1-757; apps/chat/src/server-api/chat-stream.api.ts:1-17; libs/chat-hooks/src/conversation/create-chat-stream-api.ts:1-242; apps/chat-api/src/conversations/conversation.controller.ts:1-852

## overview-08 — Chunks return through a shared lifecycle

Conversation generation is registered by principal and conversation. The backend saves initial and final or partial state, even when the originating tab disconnects. A dedicated stop request aborts generation, while attach supports resuming a view of active output. The registry is in memory; this is an operational constraint, not durable distributed execution.

Sources: apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773; apps/chat-api/src/conversations/conversation.controller.ts:1-852; libs/chat-hooks/src/conversation/useConversationStream/useConversationStream.ts:1-606

## overview-09 — Separate clients, hooks and adapters

The generated client is not the server-side DIAL TypeScript SDK. It targets this chat BFF. The backend separately uses DialClientService and the DIAL SDK to call Core. Hooks can depend on generated operation signatures under the documented exception, while the configured client instance remains app-owned.

Sources: libs/chat-api-client/src/generated/src/runtime.ts:1-511; libs/chat-hooks/src/useShareLink/useShareLink.ts:1-109; apps/chat/src/server-api/api-client.ts:1-106; AGENTS.md:1-176

## overview-10 — Compose a view from focused parts

The application assembles components around its contexts and hooks. AssistantMessageBubble accepts afterContent, so the same message component can display a stages panel without owning stage fetching. The canvas is controlled through a provider at the app root. This demonstrates a concrete modularity benefit: presentation composition can change without moving the HTTP contract into the component.

Sources: apps/chat/src/components/ConversationView/ConversationView.tsx:1-1263; apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898; apps/chat/src/pages/Conversation/Conversation.tsx:1-757

## overview-21 — See three libraries in one host

This is a real browser screenshot of the standalone demo in demo/main.tsx, captured by src/capture-demo.mjs. It renders SettingsPanel, UsageLimitCard and StagesPanel directly from the recorded source snapshot with local stylesheet dependencies. It is an illustrative host, not a screenshot of a deployed DIAL product. All data is synthetic and no backend request is made. Run the Vite command in examples/README.md, then the capture script. Expected behavior: Usage starts selected; selecting Profile updates the controlled active row. The amount and stage remain demo data. The host explicitly supplies dark-theme color overrides. Desktop and phone captures are retained under assets/.

Sources: libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229

## overview-11 — Choose a reuse boundary

All twenty-eight source manifests are private in this snapshot. The verified path is the current workspace with its aliases and Nx graph. Publish and pack tooling exists, but a tag or script is not proof of npm availability. For a separate host, validate the produced package and its peer matrix before proposing installation.

Sources: AGENTS.md:1-176; libs/chat-hooks/package.json:1-266; libs/chat-overlay/README.md:1-307; tools/publish-lib.mjs:1-282

## overview-12 — Theme tokens travel from host to component

The actual ThemeController is unversioned and exposes /api/themes and /api/themes/icon despite the broader business-route versioning rule. ThemeProvider sets colors as CSS variables. Library props can override local variables, and stable public classes support host styling. The supplied favicon is copied from the adjacent SDK website unchanged.

Sources: docs/theme-customization.md:1-396; apps/chat-api/src/themes/theme.controller.ts:1-131; apps/chat/src/context/ThemeContext.tsx:1-171; libs/chat-shared/src/utils/build-css-vars.ts:1-14

## overview-13 — Localization support has a clear current limit

Do not equate RTL direction handling with a completed Arabic translation. The current config imports only en.json and falls back to English. The direction hook updates both html.lang and html.dir on language changes. The repository instructions require RTL and accessibility support, but this bundle does not claim a full accessibility conformance audit.

Sources: apps/chat/src/i18n/config.ts:1-32; AGENTS.md:1-176; libs/navigation-panel/src/models/navigation-panel-props.ts:1-73

## overview-14 — Authentication belongs at the BFF

The default browser flow uses an encrypted HttpOnly session cookie. The backend performs OIDC and refreshes tokens; JavaScript receives user state rather than access or refresh tokens. A separately configured header-token strategy exists. Secure cookie and same-site behavior depend on deployment and overlay mode. This is a description of this source, not general identity-provider setup guidance.

Sources: docs/auth/auth-bff-encrypted-cookie.md:1-442; apps/chat-api/src/auth/session/session.guard.ts:1-112; apps/chat-api/src/auth/session/session.service.ts:1-58; apps/chat-api/src/auth/refresh/refresh.service.ts:1-115

## overview-15 — Two upstream APIs share the browser stream

Both the server operator flag and the deployment capability must be true to select Responses. The resolver function alone checks only the capability, so reading it without its caller gives an incomplete rule. The BFF normalizes upstream events to the browser contract. There is no automatic retry through the other API after an error.

Sources: docs/responses-api-integration.md:1-460; apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773; apps/chat-api/src/conversations/generation/generation-api.ts:1-27

## overview-16 — Run the applications locally

These are documented commands, not operations run against the source repository for this task. Configure DIAL_CORE_URL and the required auth/session settings from apps/chat-api/README.md and .env.template. Configure MCP_APP_SANDBOX_ALLOWED_HOST_ORIGINS before using the separate sandbox. npm ci modifies the consuming checkout, so it is shown for reproducibility and was not run here.

Sources: package.json:1-199; apps/chat/vite.config.mts:1-267; apps/chat-api/README.md:1-1047; apps/mcp-app-sandbox/README.md:1-60

## overview-17 — Use the checks that match the change

The repository scripts use Nx targets and affected project selection. The lint script itself applies fixes, while lint:check is the non-mutating alternative used in verification. Full workspace builds and suites were not run for this output-only task. The presentation bundle has its own generation, structural, rendering and example checks.

Sources: package.json:1-199; nx.json:1-121

## overview-18 — Modularity gives specific engineering benefits

These are source-backed structural benefits. Shared validation reduces duplicated rule implementations; typed renderers centralize content display; explicit callbacks permit a different host behavior. No speedup, maintenance percentage, adoption count or benchmark is inferred from this structure.

Sources: libs/builder-form/src/index.ts:1-65; libs/toolset-editor/src/components/GeneralForm/GeneralForm.tsx:1-151; libs/attachment-canvas/src/models/attachment-canvas.ts:1-620; apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898

## overview-19 — Tradeoffs remain visible

Isolation is a useful design constraint but not a description of every current import. The quality report records concrete counterexamples. Stateful runtime mechanisms also impose deployment and lifecycle concerns. Use these limitations when deciding between component reuse and full-app embedding.

Sources: AGENTS.md:1-176; libs/toolset-editor/package.json:1-41; libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts:1-494; apps/chat-api/src/conversations/conversation-generation.service.ts:1-340

## overview-20 — Start with a vertical path through the code

The series index links all thirty-three decks and their previews. Each library deck includes a diagram, a checked example and source locators. Use manifest.json to see generation and verification status, and qa-report.md to understand the scope and remaining limits. Source paths refer to the recorded working tree snapshot.

Sources: apps/chat/src/main.tsx:1-108; apps/chat/src/app/app.tsx:1-582; apps/chat/src/server-api/api-client.ts:1-106

## apps-chat-01 — Chat frontend

This application owns integration, including providers, routing, language, theme, configured API clients and feature availability. Its role is broader than any one component library.

Sources: apps/chat/src/main.tsx:1-108; apps/chat/src/app/app.tsx:1-582

## apps-chat-02 — The frontend owns the user workflow

The route enum and app route registration are the current scope. User-visible capabilities can be gated by server configuration and deployment support.

Sources: apps/chat/src/types/routes.ts:1-30

## apps-chat-03 — Bootstrap the application once

main.tsx imports base styles and i18n, creates the tooltip portal, and nests providers before rendering App. RequireAuth guards the main workspace. Login and overlay-close routes are mounted at the higher routing layer.

Sources: apps/chat/src/main.tsx:1-108; apps/chat/src/app/app.tsx:1-582

## apps-chat-04 — Providers define state ownership

These are actual provider names from the entry point. Do not move them into libraries to simplify imports. When reusing a component independently, replace the relevant application adapter with explicitly supplied data and callbacks.

Sources: apps/chat/src/main.tsx:1-108

## apps-chat-05 — Routes connect reusable screens

ROUTES declares more specific variants for edit/detail/callback and invitations. Many route components use React.lazy and Suspense; the conversation page is eagerly prefetched before its lazy wrapper. Do not document every route as loaded in the same way.

Sources: apps/chat/src/types/routes.ts:1-30; apps/chat/src/app/app.tsx:1-582

## apps-chat-06 — Trace a message from UI intent

The page supplies the stream hook and input components with state derived from app contexts. createChatStreamApi receives host paths and CSRF callbacks from the app adapter. Generation result updates flow back into the message components, while persistence remains in the BFF. The stream-hook node is useConversationStream; the concise node label avoids excessive wrapping.

Sources: apps/chat/src/pages/Conversation/Conversation.tsx:1-757; apps/chat/src/server-api/chat-stream.api.ts:1-17; libs/chat-hooks/src/conversation/useConversationStream/useConversationStream.ts:1-606

## apps-chat-07 — Configure the generated client at the edge

The middleware variables are defined in the source file, not globals. CSRF and unauthorized behavior are supplied through callback-based factories from chat-hooks, with browser/session state remaining app-owned. Full source-linked contract information is in the bundle index.

Sources: apps/chat/src/server-api/api-client.ts:1-106

## apps-chat-08 — Assemble evidence around each message

These application containers connect source-derived message data to generic display components. URL resolution, PDF worker setup and feature flags should be inspected at this edge rather than inferred from the presentation component alone.

Sources: apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898; apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:1-354; apps/chat/src/app/app.tsx:1-582

## apps-chat-09 — Theme, locale and viewport are host concerns

The frontend currently registers only English translations. RTL direction switching exists for four base language codes. This is support infrastructure, not a claim of complete translated Arabic UI. Component demos in this bundle use English and clearly identified synthetic data.

Sources: apps/chat/src/context/ThemeContext.tsx:1-171; apps/chat/src/i18n/config.ts:1-32; apps/chat/src/hooks/breakpoint/useBreakpoint.ts:1-89

## apps-chat-10 — A concrete extension: message content slots

The complete checked example imports both components and stylesheets. afterContent renders between the message body and actions. Replace the empty demo stages with the host message stages; no backend code change is required to use the slot.

Sources: libs/conversation-messages/src/models/message-bubble.ts:1-177; apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898

## apps-chat-15 — Inspect the reusable pieces in isolation

This is a real browser screenshot of the standalone demo in demo/main.tsx, captured by src/capture-demo.mjs. It renders SettingsPanel, UsageLimitCard and StagesPanel directly from the recorded source snapshot with local stylesheet dependencies. It is an illustrative host, not a screenshot of a deployed DIAL product. All data is synthetic and no backend request is made. Run the Vite command in examples/README.md, then the capture script. Expected behavior: Usage starts selected; selecting Profile updates the controlled active row. The amount and stage remain demo data. The host explicitly supplies dark-theme color overrides. Desktop and phone captures are retained under assets/.

Sources: libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229

## apps-chat-11 — Run and build the frontend

Nx resolves the application name as @epam/chat. npm start uses the supported chat alias. These commands are provided for the reader; no source build or application dependency installation was performed for this documentation task. Vite configuration and the graph, rather than an old README project count, determine the targets.

Sources: package.json:1-199; apps/chat/vite.config.mts:1-267

## apps-chat-12 — Inspect behavior through existing tests

Tests are inspected evidence, not newly executed application suite results. For a future code change, select the relevant Nx test target or npm run test:file. Presentation example modules were checked independently with strict TypeScript against the same source exports.

Sources: apps/chat/src/pages/ConversationRoute/ConversationRoute.integration.spec.tsx:1-332; apps/chat/src/components/ConversationView/tests/ConversationMessageItem.spec.tsx:1-1491; apps/chat/src/context/overlay/tests/OverlayContext.spec.tsx:1-1443

## apps-chat-13 — Integration limits are part of the design

The raw transcription wrapper documents the customContent versus custom_content schema collision. Do not claim every HTTP call is generated. For a smaller host, adopt a component or focused hook entry before copying the entire provider tree.

Sources: apps/chat/src/main.tsx:1-108; apps/chat/src/server-api/chat.api.ts:1-42; apps/chat-api/README.md:1-1047

## apps-chat-14 — Follow one feature end to end

PromptEditor is a manageable example: the app loads and saves the entity while the library owns the fields. The same tracing method scales to conversations. Consult each library deck for the exact exported prop and callback contract.

Sources: apps/chat/src/pages/PromptEditor/PromptEditor.tsx:1-282; apps/chat/src/server-api/api-client.ts:1-106; libs/prompt-editor/src/models/prompt-editor-props.ts:1-162

## apps-chat-api-01 — Chat backend

chat-api is the backend-for-frontend for the React application. It also serves production frontend assets and coordinates several external systems. Distinguish its generated browser client from the server-side DIAL TypeScript SDK.

Sources: apps/chat-api/src/main.ts:1-213; apps/chat-api/src/app/app.module.ts:1-79

## apps-chat-api-02 — Keep three boundaries explicit

Controllers delegate to services. DialClientService centralizes Core SDK configuration and the fetch user-agent behavior. Non-Core integrations can use their own transport where required; do not describe all outbound calls as one SDK operation.

Sources: apps/chat-api/src/main.ts:1-213; apps/chat-api/src/app/app.module.ts:1-79; apps/chat-api/src/dial/dial-client.service.ts:1-64

## apps-chat-api-03 — Bootstrap establishes cross-cutting behavior

main.ts imports telemetry first, sets validation, CORS, cookie handling, URI versioning and static middleware, and enables graceful shutdown. Source comments explain ordering constraints. The environment schema controls boot-time validation; the source contains both ConfigService reads and some direct process.env reads.

Sources: apps/chat-api/src/main.ts:1-213; apps/chat-api/src/app/app.module.ts:1-79

## apps-chat-api-04 — Domain modules organize the backend

Domain folders sit directly under src. Auxiliary concerns such as schemas, offline credentials, health and user configuration are also wired by AppModule. The table groups the modules for readability and does not replace the source module index.

Sources: apps/chat-api/src/app/app.module.ts:1-79

## apps-chat-api-05 — Representative HTTP contracts

The main business domains use URI versioning, but themes are still unversioned in the implementation. This is a concrete exception to the written rule, not a typo to silently correct in the slides. Swagger handler names feed operation ids and the generated client.

Sources: apps/chat-api/src/deployments/deployments.controller.ts:1-194; apps/chat-api/src/conversations/conversation.controller.ts:1-852; apps/chat-api/src/auth/auth.controller.ts:1-702; apps/chat-api/src/themes/theme.controller.ts:1-131

## apps-chat-api-06 — A completion has a persisted lifecycle

The controller intentionally does not stop generation when the response disconnects. Generation services retain the active operation in memory and persist terminal or partial results. Dedicated stop and attach operations support user control and reopening a running conversation. Process-local state requires deployment consideration.

Sources: apps/chat-api/src/conversations/conversation.controller.ts:1-852; apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773; apps/chat-api/src/conversations/conversation-generation.service.ts:1-340

## apps-chat-api-07 — Upstream dispatch is controlled on the server

The deployment is re-resolved under the current user token. Both the operator flag and capability matter; the small pure resolver by itself shows only the capability check. The browser sees the same normalized completion contract. Failed requests are not automatically retried through another generation API.

Sources: apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773; apps/chat-api/src/conversations/generation/generation-api.ts:1-27; docs/responses-api-integration.md:1-460

## apps-chat-api-08 — Authentication has explicit request scope

The cookie payload carries encrypted tokens; browser JavaScript does not receive their values. The header strategy is enabled through configuration and verifies allowed issuer/provider identity. Per-request principal and auth data must not be stored in a mutable service singleton.

Sources: apps/chat-api/src/auth/session/session.guard.ts:1-112; apps/chat-api/src/auth/strategies/cookie-session.strategy.ts:1-147; apps/chat-api/src/auth/strategies/header-token.strategy.ts:1-256; apps/chat-api/src/auth/session/session.service.ts:1-58

## apps-chat-api-09 — Keep controller and DTO changes synchronized

This is an abridged source excerpt, not a new runnable controller. Imports, constructor injection and Swagger decorators are omitted for readability; the original source contains them. This direct /chat/completions endpoint is distinct from the conversation persistence and streaming workflow. Full source excerpts are retained by path and range in the index.

Sources: apps/chat-api/src/chat/chat.controller.ts:1-33; apps/chat-api/src/chat/dto/chat-completion.dto.ts:1-104

## apps-chat-api-10 — Regenerate the contract after API changes

The generated client is checked in. Update server definitions rather than editing generated methods. The operationIdFactory uses handler names, so naming the handler changes the browser-facing method. Commands shown here were not run because they would modify the repository artifacts.

Sources: package.json:1-199; tools/openapi/check-client.mjs:1-46; apps/chat-api/src/openapi/openapi.config.ts:1-30; libs/chat-api-client/src/index.ts:1-1

## apps-chat-api-11 — Configure the runtime deliberately

The exact required fields and defaults are in the backend README and environment schema. Use obvious demo values when experimenting; do not embed real secrets in code examples. Invalid required configuration fails at boot. The runtime also supports feature, theme, cookie and telemetry settings.

Sources: apps/chat-api/README.md:1-1047; apps/chat-api/src/config/environment.config.ts:1-960

## apps-chat-api-12 — Run and verify the backend

Nx resolves @epam/chat-api as the project name. The serve target builds/runs the backend, while the separate start:api:dev script uses HMR tooling. These application commands are documented, not run during presentation generation. Backend integration tests use mocked external clients.

Sources: package.json:1-199; apps/chat-api/src/main.ts:1-213

## apps-chat-api-13 — Existing tests exercise contracts and failures

The inspected test files provide concrete behavior expectations. Test presence alone is not a passing suite result, and the presentation QA does not substitute for backend security testing. Run focused tests and repository verification for a code change.

Sources: apps/chat-api/src/conversations/tests/conversation.controller.integration.spec.ts:1-911; apps/chat-api/src/auth/session/tests/session.guard.spec.ts:1-147; apps/chat-api/src/chat/tests/chat.controller.integration.spec.ts:1-117

## apps-chat-api-14 — Operational tradeoffs shape deployment

Encrypted-cookie authentication enables stateless session decryption across correctly configured pods, but it does not make every runtime mechanism distributed. Distinguish session storage from in-memory active-generation coordination. Use deployment-specific operational checks before adopting a multi-instance topology.

Sources: apps/chat-api/src/conversations/conversation-generation.service.ts:1-340; apps/chat-api/src/app/cache.config.ts:1-28; apps/chat-api/src/themes/theme.controller.ts:1-131

## apps-chat-overlay-sandbox-01 — Overlay sandbox

This is a React/Vite demonstration application, not an isolated MCP resource renderer. It hosts existing overlay clients against a running chat instance.

Sources: apps/chat-overlay-sandbox/README.md:1-73; apps/chat-overlay-sandbox/src/main.tsx:1-15

## apps-chat-overlay-sandbox-02 — Each case demonstrates a distinct contract

EnabledFeaturesCase and AuthUiModeCase complete the set. Cases are actual source modules under src/cases. They are useful for reproducing integration behavior before embedding the overlay into a separate product.

Sources: apps/chat-overlay-sandbox/README.md:1-73

## apps-chat-overlay-sandbox-03 — Trace the host-to-chat handshake

The host API waits for the full ready-to-interact handshake. A blank iframe caused by frame-ancestors policy is not a protocol timeout to fix in the controls. Check server allowlisting and runtime overlay mode first.

Sources: libs/chat-overlay/src/lib/ChatOverlay.ts:1-494; apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx:1-242

## apps-chat-overlay-sandbox-04 — Reproduce the local scenario

The first two lines are backend environment configuration, not values to set only on the sandbox process. The host override is passed to the Vite sandbox. Run chat at 4207 and its backend at 5000 first. No real user data is required to open the page, but an authenticated deployment may require login for chat actions.

Sources: apps/chat-overlay-sandbox/README.md:1-73; apps/chat-overlay-sandbox/vite.config.mts:1-59

## apps-chat-overlay-sandbox-05 — A direct overlay is a small integration

The complete example receives domain as a parameter, subscribes to an event and returns cleanup. The container must exist in the page. Changing input is a protocol operation; it does not automatically send a model request.

Sources: apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx:1-242; libs/chat-overlay/src/lib/ChatOverlay.ts:1-494

## apps-chat-overlay-sandbox-06 — Deployment shares the main chat image

The root Dockerfile builds this app with the frontend and backend. The deployed sandbox embeds the current origin. This same-origin deployment is intentional for this demo host and must not be copied to the MCP sandbox architecture.

Sources: apps/chat-overlay-sandbox/README.md:1-73; Dockerfile:1-70; apps/chat-api/src/app/static-assets.ts:1-215

## apps-chat-overlay-sandbox-07 — Verify cases through the current targets

The source includes seven test files for sandbox behavior. These suites were inspected but not run for the presentation task. The live integration requires the external chat deployment and its server policy, beyond what a mocked test can establish.

Sources: apps/chat-overlay-sandbox/README.md:1-73; apps/chat-overlay-sandbox/package.json:1-10

## apps-chat-overlay-sandbox-08 — Interpret integration failures at the right layer

Same-window identity-provider login in an iframe depends on the provider tenant and browser policy. The sandbox exposes those choices for investigation; it cannot make an incompatible provider embeddable. Use it as a reproducible integration host rather than a proof of production compatibility.

Sources: apps/chat-overlay-sandbox/README.md:1-73; libs/chat-overlay/src/lib/ChatOverlay.ts:1-494

## apps-mcp-app-sandbox-01 — MCP sandbox proxy

This small application serves the sandbox-proxy document used by the MCP UI renderer. It must be deployed on an origin distinct from the chat host. It is an infrastructure component of the rendering boundary, not a catalog demo.

Sources: apps/mcp-app-sandbox/README.md:1-60; apps/mcp-app-sandbox/src/main.ts:1-49

## apps-mcp-app-sandbox-02 — Why a separate application exists

The README and implementation adapt the MCP reference double-iframe pattern. A sandbox attribute alone is not the reason for this separate app; the distinct origin keeps the proxy and tool document out of the host origin. The inner document and bridge have their own constraints.

Sources: apps/mcp-app-sandbox/README.md:1-60; apps/mcp-app-sandbox/src/main.ts:1-49; apps/mcp-app-sandbox/src/app/sandbox-page.ts:1-103

## apps-mcp-app-sandbox-03 — Request validation precedes HTML delivery

SandboxService uses an Origin header when present, then falls back to the Referer origin. A missing or unapproved origin is rejected. SandboxController sends text/html, CSP, nosniff, cross-origin resource policy and no-store. A raw GET without the required embedding context should fail.

Sources: apps/mcp-app-sandbox/src/app/sandbox.controller.ts:1-33; apps/mcp-app-sandbox/src/app/sandbox.service.ts:1-56

## apps-mcp-app-sandbox-04 — Configure two sides of the connection

The frontend receives the sandbox URL through the backend client-configuration pipeline. PORT defaults to 3100. Production should use the actual distinct HTTPS origins and the intended host allowlist. No secret values are required in this example.

Sources: apps/mcp-app-sandbox/README.md:1-60; apps/mcp-app-sandbox/src/config/environment.config.ts:1-29

## apps-mcp-app-sandbox-05 — The page and policy are app-owned

main.ts intentionally disables Helmet generic CSP and frame blocking so the route can deliver its custom embedding policy. CORS is explicitly disabled for cross-origin script fetching. This route is designed for iframe navigation with origin validation, not a general data API.

Sources: apps/mcp-app-sandbox/src/app/sandbox.controller.ts:1-33; apps/mcp-app-sandbox/src/app/sandbox.service.ts:1-56; apps/mcp-app-sandbox/src/app/csp.ts:1-19; apps/mcp-app-sandbox/src/app/sandbox-page.ts:1-103

## apps-mcp-app-sandbox-06 — A rendered MCP view needs the whole chain

The sandbox alone does not discover tools or authenticate tool calls. Those operations are supplied by the host adapter and backend. To reproduce a full interaction, use a configured MCP-capable deployment and a real ui:// resource; this bundle does not manufacture a product screenshot of that interaction.

Sources: libs/mcp-apps/src/models/mcp-apps.ts:1-148; libs/attachment-canvas/src/components/McpAppCanvasRenderer/McpAppCanvasRenderer.tsx:1-150; apps/mcp-app-sandbox/src/app/sandbox-page.ts:1-103

## apps-mcp-app-sandbox-07 — Build and check what exists

No source test files or test target were discovered for this application. Do not invent a passing test result or recommend a nonexistent target. Build/typecheck/lint commands are available; real isolation behavior needs a browser integration exercise with distinct origins.

Sources: apps/mcp-app-sandbox/package.json:1-103; apps/mcp-app-sandbox/README.md:1-60; apps/mcp-app-sandbox/Dockerfile:1-61

## apps-mcp-app-sandbox-08 — Limits to carry into operations

The small source footprint does not reduce the importance of this boundary. Deployment-origin and browser-policy checks remain necessary. The presentation report records that no full live MCP/Core integration was exercised during this output-only documentation task.

Sources: apps/mcp-app-sandbox/README.md:1-60; apps/mcp-app-sandbox/src/main.ts:1-49; apps/mcp-app-sandbox/src/app/sandbox.service.ts:1-56

## lib-attachment-canvas-01 — Attachment canvas

This session explains preview heterogeneous content through one typed surface. The library is a local private workspace package at libs/attachment-canvas. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542

## lib-attachment-canvas-02 — When this library is useful

Start with a concrete caller need. Inspect evidence: Open a cited PDF or uploaded text beside a conversation. Choose a renderer: A content discriminator selects the appropriate view. Extend a workspace: Add visualizers or MCP content through explicit inputs. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542

## lib-attachment-canvas-03 — Follow the ownership boundary

The library owns Viewer selection, panel layout, lazy renderer loading and optional canvas context. The host owns File access, resolved content, authorization, deployment settings and download behavior. The direct AttachmentCanvas example is controlled and does not require a provider. The provider is needed for useAttachmentCanvas and the context-based opening flow. The host must supply authenticated loading rather than passing session knowledge into ordinary UI code. The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542; AGENTS.md:1-176

## lib-attachment-canvas-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON. The direct AttachmentCanvas example is controlled and does not require a provider. The provider is needed for useAttachmentCanvas and the context-based opening flow. The host must supply authenticated loading rather than passing session knowledge into ordinary UI code.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542

## lib-attachment-canvas-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/attachment-canvas.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Open a cited PDF or uploaded text beside a conversation. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542

## lib-attachment-canvas-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Resolve a file: Fetch accessible content in the host and choose its content kind. Open the preview: Supply content, open state, labels and any renderer setup. Handle an action: Close locally or download through a host callback. The complete typed module in examples/attachment-canvas.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542

## lib-attachment-canvas-10 — Context-based canvas control

The direct controlled example does not need this context. Use the provider when descendants call useAttachmentCanvas or the context-driven opening hook; supply host resolvers for access-dependent content.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542

## lib-attachment-canvas-07 — Available customization

Customization comes from the current exports and prop declarations. Typed content variants: Plain text, code, Markdown, PDF, OOXML, media, HTML and MCP views. Optional shared context: AttachmentCanvasProvider and useAttachmentCanvas coordinate a canvas. Host loading hooks: loadPdf and configurePdfWorker support caller-controlled PDF setup. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542

## lib-attachment-canvas-08 — Find the integration and its checks

Actual consumers: libs/mcp-apps/src/hooks/useMcpAppInlinePreview/useMcpAppInlinePreview.ts; libs/quotations/src/models/office-highlight.ts; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx; apps/chat/src/pages/SkillEditor/SkillEditor.tsx; apps/chat/src/hooks/attachment/useSkillFilePreviewSync.ts; apps/chat/src/hooks/attachment/useAttachmentCanvasResolvers.ts. Existing test evidence: [{"file": "libs/attachment-canvas/src/hooks/useOpenAttachmentCanvas/tests/useOpenAttachmentCanvas.spec.ts", "assertions": ["useOpenAttachmentCanvas routing", "routes an OOXML attachment by extension when its MIME type is generic", "routes CSV by extension to the @silurus/ooxml resolver instead of the code renderer", "routes an OOXML attachment whose name has no extension by MIME type", "opens the unsupported panel when a recognized OOXML file cannot be resolved", "forwards a Forbidden error from the OOXML resolver to the canvas", "does not route legacy binary Office formats to the OOXML resolver", "routes .md attachments to the markdown resolver", "routes .markdown attachments to the markdown resolver", "routes .json attachments to the JSON resolver", "routes .jsonl attachments to the code resolver (not JSON)", "opens the canvas with the resolved content", "routes text/markdown MIME type to the markdown resolver (ignores .pdf extension in title)", "prefers a known text MIME type over an OOXML-looking title", "routes application/json MIME type to the JSON resolver"]}, {"file": "libs/attachment-canvas/src/components/CodeContent/tests/CodeContent.spec.tsx", "assertions": ["CodeContent", "renders plain text immediately with no syntax highlighter for a plaintext language", "renders plain text immediately with no syntax highlighter when no language is set", "shows the value via a plain fallback, then highlights it once the engine loads for a real language", "announces the pending state via role="]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-attachment-canvas:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542; libs/mcp-apps/src/hooks/useMcpAppInlinePreview/useMcpAppInlinePreview.ts:1-154; libs/attachment-canvas/src/hooks/useOpenAttachmentCanvas/tests/useOpenAttachmentCanvas.spec.ts:1-1174; libs/attachment-canvas/src/components/CodeContent/tests/CodeContent.spec.tsx:1-85

## lib-attachment-canvas-09 — Constraints that affect integration

Review these constraints before choosing the library. Heavy renderers: PDF, Office, syntax and MCP dependencies affect packaging; several load lazily. Content errors differ: Unsupported, forbidden and failed loads have distinct display states. Untrusted content: HTML and MCP views require the documented sandbox and host settings. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/attachment-canvas/README.md:1-615; libs/attachment-canvas/src/index.ts:1-89; libs/attachment-canvas/package.json:1-64; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx:445-445; libs/attachment-canvas/src/models/attachment-canvas.ts:487-542; AGENTS.md:1-176

## lib-attachment-input-01 — Attachment input

This session explains turn file state into clear attachment controls. The library is a local private workspace package at libs/attachment-input. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/attachment-input/README.md:1-264; libs/attachment-input/src/index.ts:1-61; libs/attachment-input/package.json:1-39; libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56; libs/attachment-input/src/models/attachment-tray.ts:24-39

## lib-attachment-input-02 — When this library is useful

Start with a concrete caller need. Compose with files: Show files before sending a message. Recover from failure: Expose remove and retry actions per attachment. Reuse sent-file UI: Render image groups and file rows in transcripts. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/attachment-input/README.md:1-264; libs/attachment-input/src/index.ts:1-61; libs/attachment-input/package.json:1-39; libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56; libs/attachment-input/src/models/attachment-tray.ts:24-39

## lib-attachment-input-03 — Follow the ownership boundary

The library owns Cards, trays, file-drop affordances and clipboard handling. The host owns Upload transport, progress state, validation policy and preview URLs.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/attachment-input/README.md:1-264; libs/attachment-input/src/index.ts:1-61; libs/attachment-input/package.json:1-39; libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56; libs/attachment-input/src/models/attachment-tray.ts:24-39; AGENTS.md:1-176

## lib-attachment-input-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/attachment-input/README.md:1-264; libs/attachment-input/src/index.ts:1-61; libs/attachment-input/package.json:1-39; libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56; libs/attachment-input/src/models/attachment-tray.ts:24-39

## lib-attachment-input-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/attachment-input.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Show files before sending a message. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/attachment-input/README.md:1-264; libs/attachment-input/src/index.ts:1-61; libs/attachment-input/package.json:1-39; libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56; libs/attachment-input/src/models/attachment-tray.ts:24-39

## lib-attachment-input-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Accept a file: The host starts an upload and creates display data. Reflect progress: Pass current attachments and their upload state into the tray. Retry or remove: Use the attachment id from the callback to update host state. The complete typed module in examples/attachment-input.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/attachment-input/README.md:1-264; libs/attachment-input/src/index.ts:1-61; libs/attachment-input/package.json:1-39; libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56; libs/attachment-input/src/models/attachment-tray.ts:24-39

## lib-attachment-input-07 — Available customization

Customization comes from the current exports and prop declarations. Tray and group: Use AttachmentTray while composing; AttachmentGroup for sent files. Lazy previews: Image loading has an observable loading and error lifecycle. Accessible actions: Supply localized open, retry, remove and upload labels. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/attachment-input/README.md:1-264; libs/attachment-input/src/index.ts:1-61; libs/attachment-input/package.json:1-39; libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56; libs/attachment-input/src/models/attachment-tray.ts:24-39

## lib-attachment-input-08 — Find the integration and its checks

Actual consumers: libs/conversation-messages/src/components/MessageBubble/UserMessageBubble.tsx; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx; libs/source-panel/src/components/FilesSection/FilesSection.tsx; libs/conversation-input/src/hooks/useAttachments.ts; libs/chat-hooks/src/attachment/useAttachmentValidation/useAttachmentValidation.ts; libs/conversation-input/src/components/Input/Input.tsx. Existing test evidence: [{"file": "libs/attachment-input/src/hooks/tests/useClipboardPaste.spec.ts", "assertions": ["useClipboardPaste", "handles null clipboardData without throwing", "image paste creates an Image attachment and prevents default", "stamps a pasted image name with the paste time, keeping base and extension", "gives each image of a multi-image paste a distinct name", "gives images pasted at different times distinct names", "long text creates a Pasted attachment with preview name", "preview name is truncated to 80 chars with ellipsis when text is very long", "ignores the image and pastes text when clipboard contains both image and text", "short text does not create an attachment"]}, {"file": "libs/attachment-input/src/hooks/tests/useLazyImageLoad.spec.tsx", "assertions": ["useLazyImageLoad", "starts in loading state when enabled with a source", "moves to loaded when the image loads", "moves to error when the image fails to load", "resets to idle when disabled", "resets to loading when the source changes"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-attachment-input:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/attachment-input/README.md:1-264; libs/attachment-input/src/index.ts:1-61; libs/attachment-input/package.json:1-39; libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56; libs/attachment-input/src/models/attachment-tray.ts:24-39; libs/conversation-messages/src/components/MessageBubble/UserMessageBubble.tsx:1-184; libs/attachment-input/src/hooks/tests/useClipboardPaste.spec.ts:1-181; libs/attachment-input/src/hooks/tests/useLazyImageLoad.spec.tsx:1-74

## lib-attachment-input-09 — Constraints that affect integration

Review these constraints before choosing the library. No uploader in a card: Showing progress does not perform the network upload. Watch callback shapes: Tray actions use an id; message bubble callbacks can use an object. Keep state ownership clear: The library has local UI state; the host owns durable file state. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/attachment-input/README.md:1-264; libs/attachment-input/src/index.ts:1-61; libs/attachment-input/package.json:1-39; libs/attachment-input/src/components/AttachmentTray/AttachmentTray.tsx:8-56; libs/attachment-input/src/models/attachment-tray.ts:24-39; AGENTS.md:1-176

## lib-builder-form-01 — Builder form

This session explains give entity editors a shared structure and validation vocabulary. The library is a local private workspace package at libs/builder-form. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45

## lib-builder-form-02 — When this library is useful

Start with a concrete caller need. Build an editor: Compose metadata and setup sections in a consistent page. Share field rules: Use one validator for name and version policies. Localize metadata: Edit additional deployment names and descriptions by locale. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45

## lib-builder-form-03 — Follow the ownership boundary

The library owns Editor shells, field controls and pure validation error codes. The host owns Save behavior, routing, translated errors, avatar resolution and file access.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45; AGENTS.md:1-176

## lib-builder-form-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45

## lib-builder-form-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/builder-form.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Compose metadata and setup sections in a consistent page. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45

## lib-builder-form-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Compose metadata: Place shared fields inside the editor sections. Validate values: Map validation error codes to localized field messages. Save through the host: Submit the validated values using the application adapter. The complete typed module in examples/builder-form.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45

## lib-builder-form-10 — Validate without translating

An empty name produces a validation error code. No translation service is invoked by the validator. The full example includes this call.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45

## lib-builder-form-07 — Available customization

Customization comes from the current exports and prop declarations. Layout composition: EditorLayout exposes leftContent, rightContent and actions. Metadata fields: DeploymentCreationForm includes avatar, version, topics and locales. Policy switches: Name and version pattern checks are opt-in validator options. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45

## lib-builder-form-08 — Find the integration and its checks

Actual consumers: libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx; libs/toolset-editor/src/components/GeneralForm/GeneralForm.tsx; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx; libs/toolset-editor/src/models/toolset-editor-props.ts; libs/toolset-editor/src/models/general-form-props.ts. Existing test evidence: [{"file": "libs/builder-form/src/components/DeploymentCreationForm/tests/DeploymentCreationForm.spec.tsx", "assertions": [",", "DeploymentCreationForm", "renders all shared fields", "calls onAddAvatarClick when the Add avatar button is clicked", "calls onChange with a name patch when the name input changes", "calls onChange with a description patch when the textarea changes", "surfaces a passed-in name error without validating itself", "renders no error when none is passed"]}, {"file": "libs/builder-form/src/components/AvatarPickerModal/tests/AvatarPickerModal.spec.tsx", "assertions": ["AvatarPickerModal", "renders the host file manager modal when open", "does not render the host file manager modal when closed", "forwards the file manager attach result to onAttach"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-builder-form:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: renders all shared fields.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:1-310; libs/builder-form/src/components/DeploymentCreationForm/tests/DeploymentCreationForm.spec.tsx:1-183; libs/builder-form/src/components/AvatarPickerModal/tests/AvatarPickerModal.spec.tsx:1-95

## lib-builder-form-09 — Constraints that affect integration

Review these constraints before choosing the library. Avatar ownership: Resolve iconPreviewUrl and open file selection in the host. Locale visibility: DeploymentLocalesField hides when no locale options are supplied. State is mixed: Some controls manage transient state; persistence remains outside. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/builder-form/README.md:1-420; libs/builder-form/src/index.ts:1-65; libs/builder-form/package.json:1-39; libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120; libs/builder-form/src/models/editor-layout-props.ts:24-45; AGENTS.md:1-176

## lib-catalog-01 — Catalog

This session explains browse deployments and reusable assets without owning their storage. The library is a local private workspace package at libs/catalog. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462

## lib-catalog-02 — When this library is useful

Start with a concrete caller need. Find a deployment: Search, filter and compare models or applications. Inspect details: Show capabilities, tools, pricing and limits. Act on a selection: Pick, favorite, share or publish through host callbacks. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462

## lib-catalog-03 — Follow the ownership boundary

The library owns Catalog display, search/filter interactions and composed detail surfaces. The host owns Data loading, action permissions, routes, configured API clients and deployment mapping.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462; AGENTS.md:1-176

## lib-catalog-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462

## lib-catalog-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/catalog.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Search, filter and compare models or applications. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462

## lib-catalog-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Prepare catalog items: Load deployment data and map it to CatalogItem records. Connect item actions: Supply use, favorite and detail callbacks for the workflow. Reflect host state: Pass updated favorites and item data back to the catalog. The complete typed module in examples/catalog.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462

## lib-catalog-10 — Choose the headless entry

This is an import-only example of a genuine public subpath. Function declarations and tests are indexed under src/entry-points/mapping.ts; argument shapes are in the API appendix. The complete module examples/catalog.tsx includes typed input and both exports. filterCatalogItems matches the trimmed query against name, case-insensitively; it does not match description. An empty query returns all items.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462; libs/catalog/src/utils/catalog-filter.ts:37-56

## lib-catalog-07 — Available customization

Customization comes from the current exports and prop declarations. Two view modes: Card and list views window visible rows. Headless subpath: The /mapping entry exposes catalog mapping helpers and enums. Action policies: Callbacks and visibility predicates control available item actions. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462

## lib-catalog-08 — Find the integration and its checks

Actual consumers: libs/skills/src/components/SkillDetailsSidePanel/SkillDetailsSidePanel.tsx; libs/skills/src/models/skill-details-side-panel-props.ts; apps/chat/src/pages/AppsEditor/GeneralForm.tsx; apps/chat/src/pages/AppsEditor/AppEditorIframe.tsx; apps/chat/src/hooks/useCatalogSortFilterPreference/useCatalogSortFilterPreference.ts; apps/chat/src/hooks/useCatalogItems/useCatalogItems.ts. Existing test evidence: [{"file": "libs/catalog/src/components/Filter/tests/Filter.spec.tsx", "assertions": ["Filter", "renders the My checkbox", "renders topic checkboxes alphabetically when values are provided", "does not render Topics section when values is undefined", "calls onChange with topic added when an unchecked topic is clicked", "calls onChange with topic removed when a checked topic is clicked", "shows myAppsLabel as button label when only My Apps is active", "shows topic count label when only topics are active", "shows combined label when both My Apps and topics are active", "applies active CSS class to trigger when any filter is on", "does not apply active CSS class when no filter is on", "renders the Apply button"]}, {"file": "libs/catalog/src/components/CardGrid/tests/Card.spec.tsx", "assertions": ["Card \u2014 selected state", "does not show a selected border or checkmark by default", "shows the selected border, tint, and checkmark when isSelected is true", "Card \u2014 long version", "caps the version at 30% of the row so it cannot overlap the name", "lets the name truncate instead of being pushed out", "Card \u2014 favorite visibility", "renders the star button for every entity type, prompts included", "hides the star button and keeps the item non-favoritable when isFavoriteVisible returns false", "renders the star button when isFavoriteVisible returns true", "Card \u2014 favorite revert", "resyncs the star to initialIsStarred when it reverts after a failed toggle", "Card \u2014 credentials badge", "shows the logged-out warning icon for a signed-out toolset, for both API_KEY and OAUTH", "shows no warning icon when signed in or when authenticationType is NONE"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-catalog:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462; libs/skills/src/components/SkillDetailsSidePanel/SkillDetailsSidePanel.tsx:1-13; libs/catalog/src/components/Filter/tests/Filter.spec.tsx:1-190; libs/catalog/src/components/CardGrid/tests/Card.spec.tsx:1-306

## lib-catalog-09 — Constraints that affect integration

Review these constraints before choosing the library. Large prop surface: Configure the actions required by the host workflow. Dependency boundary: The implementation uses the UI Kit grid and catalog/publish composition. Source beats old docs: Do not copy the README peer list without checking package.json. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/catalog/README.md:1-973; libs/catalog/src/index.ts:1-157; libs/catalog/package.json:1-51; libs/catalog/src/components/Catalog/Catalog.tsx:57-778; libs/catalog/src/models/catalog-props.ts:89-462; AGENTS.md:1-176

## lib-chat-api-client-01 — Chat API client

This session explains generate typed operations from the backend openapi contract. The library is a local private workspace package at libs/chat-api-client. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250

## lib-chat-api-client-02 — When this library is useful

Start with a concrete caller need. Call the BFF: Use typed API classes from application adapters. Evolve an endpoint: Change Swagger/DTO sources, then regenerate. Inspect transport details: Use Raw operations when headers or the Response are needed. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250

## lib-chat-api-client-03 — Follow the ownership boundary

The library owns Generated endpoint paths, DTOs, serializers and Fetch transport runtime. The host owns Base URL, credentials, CSRF policy, middleware and application error presentation.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250; AGENTS.md:1-176

## lib-chat-api-client-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250

## lib-chat-api-client-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/chat-api-client.ts. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Use typed API classes from application adapters. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250

## lib-chat-api-client-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Configure transport: Create a stable Configuration with origin and middleware. Call an operation: Use listDeployments() for the parsed response DTO. Handle the outcome: Render the result or handle the rejected request in the host. The complete typed module in examples/chat-api-client.ts shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250

## lib-chat-api-client-10 — Preserve transport details when needed

The Raw signature requires the request object even when every query field is optional. The normal listDeployments method defaults that object. This distinction is enforced by the example TypeScript check.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250

## lib-chat-api-client-07 — Available customization

Customization comes from the current exports and prop declarations. Normal vs Raw: Normal methods resolve values; Raw methods expose the response wrapper. Configurable transport: Configuration accepts basePath, credentials and middleware. Regeneration scripts: npm run openapi and openapi:check maintain the checked-in artifacts. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250

## lib-chat-api-client-08 — Find the integration and its checks

Actual consumers: libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts; libs/usage-dashboard/src/utils/map-usage-data-to-dashboard.ts; apps/chat/src/pages/Conversation/Conversation.tsx; apps/chat/src/pages/ToolsetAuthCallback/ToolsetAuthCallback.tsx; apps/chat/src/pages/ScheduledTaskDetailPage/ScheduledTaskDetailPage.tsx; libs/chat-hooks/src/conversation/create-chat-stream-api.ts. Existing test evidence: []. Reproduce project checks from the repository root with npm exec nx run chat-api-client:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250; libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts:1-494

## lib-chat-api-client-09 — Constraints that affect integration

Review these constraints before choosing the library. Never hand-edit generated code: Regeneration overwrites manual client edits. Real API names: Use DeploymentsApi; the README ModelsApi example is stale. Streaming needs care: Host adapters handle documented raw stream/DTO gaps. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/chat-api-client/README.md:1-68; libs/chat-api-client/src/index.ts:1-1; libs/chat-api-client/package.json:1-41; libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250; AGENTS.md:1-176

## lib-chat-hooks-01 — Chat hooks

This session explains reuse headless request lifecycles and chat-interface behavior. The library is a local private workspace package at libs/chat-hooks. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109

## lib-chat-hooks-02 — When this library is useful

Start with a concrete caller need. Build a custom chat: Reuse stream state, scrolling and attachment behavior. Keep rendering separate: Connect returned data and callbacks to your own UI. Limit imports: Use the dependency-focused public subpaths. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109

## lib-chat-hooks-03 — Follow the ownership boundary

The library owns Reusable hook state, data mapping and permitted thin operation wrappers. The host owns Configured clients, authentication setup, routing, app contexts and translated labels.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109; AGENTS.md:1-176

## lib-chat-hooks-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109

## lib-chat-hooks-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/chat-hooks.tsx. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Reuse stream state, scrolling and attachment behavior. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109

## lib-chat-hooks-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Keep the client stable: Inject a configured ShareApi operation into useShareLink. Render the lifecycle: Read data, isLoading and error from the hook result. Change link access: Call setAccess to request a link for the new access level. The complete typed module in examples/chat-hooks.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109

## lib-chat-hooks-10 — A request lifecycle with an injected client

The full ShareLifecycleDemo example receives Pick<ShareApi, createShareLink>. Changing access requests a new link. The hook uses request identifiers to avoid overwriting newer results with stale responses. Pass origin explicitly when the default browser-global expression is unsuitable.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109

## lib-chat-hooks-07 — Available customization

Customization comes from the current exports and prop declarations. Small layout entry: /viewport-layout includes useViewportWidth with listener cleanup. Request lifecycle: useShareLink manages link loading, access changes and stale response guards. Broad feature entries: Conversation, files, catalog, OAuth and MCP have explicit subpaths. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109

## lib-chat-hooks-08 — Find the integration and its checks

Actual consumers: libs/toolset-editor/src/components/AuthSection/AuthSection.tsx; libs/toolset-editor/src/components/GeneralForm/GeneralForm.tsx; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx; libs/toolset-editor/src/models/toolset-form.ts; libs/toolset-editor/src/utils/toolsets.ts; libs/toolset-editor/src/constants/toolsets.ts. Existing test evidence: [{"file": "libs/chat-hooks/src/conversation/useImportFilePicker/tests/useImportFilePicker.spec.ts", "assertions": ["useImportFilePicker", "selects a file and resets the input so the same file can be selected again", "programmatically clicks the attached input", "applies and clears the host-resolved accept value"]}, {"file": "libs/chat-hooks/src/conversation/useActiveConversationSync/tests/useActiveConversationSync.spec.ts", "assertions": ["useActiveConversationSync", "refreshes once when the active conversation is missing without looping on item changes", "marks the matching raw conversation viewed when it becomes active", "rechecks the active conversation when the injected id matcher changes"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-chat-hooks:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109; libs/toolset-editor/src/components/AuthSection/AuthSection.tsx:1-504; libs/chat-hooks/src/conversation/useImportFilePicker/tests/useImportFilePicker.spec.ts:1-63; libs/chat-hooks/src/conversation/useActiveConversationSync/tests/useActiveConversationSync.spec.ts:1-84

## lib-chat-hooks-09 — Constraints that affect integration

Review these constraints before choosing the library. Stable dependencies: Recreating API instances can retrigger effects. Browser assumptions: Some hooks use browser globals; pass origin explicitly for share examples. Boundary audit needed: Some current helpers contain more DIAL-specific knowledge than the narrow rule. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/chat-hooks/README.md:1-3809; libs/chat-hooks/src/index.ts:1-184; libs/chat-hooks/package.json:1-266; libs/chat-hooks/src/useShareLink/useShareLink.ts:49-109; AGENTS.md:1-176

## lib-chat-overlay-01 — Chat overlay

This session explains embed a running chat with a typed message protocol. The library is a local private workspace package at libs/chat-overlay. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494

## lib-chat-overlay-02 — When this library is useful

Start with a concrete caller need. Embed a full experience: Mount the chat iframe in a host-owned region. Control conversations: Set input, send requests and subscribe to events. Offer floating widgets: Use ChatOverlayManager for toggle/fullscreen chrome. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494

## lib-chat-overlay-03 — Follow the ownership boundary

The library owns Iframe lifecycle, protocol handshake, request correlation and optional widget chrome. The host owns Chat deployment, allowed origins, identity-provider policy and host page lifecycle.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494; AGENTS.md:1-176

## lib-chat-overlay-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494

## lib-chat-overlay-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/chat-overlay.ts. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Mount the chat iframe in a host-owned region. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494

## lib-chat-overlay-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Mount the iframe: Create ChatOverlay in an existing host-owned element. Wait for readiness: Await ready() before sending the initial input content. Match host lifetime: Subscribe to events; unsubscribe and destroy on teardown. The complete typed module in examples/chat-overlay.ts shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494

## lib-chat-overlay-10 — Subscribe and clean up

The full mountDemoOverlay function returns the teardown callback. Await the handshake before issuing normal requests. Destroy the overlay when its host container is no longer valid.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494

## lib-chat-overlay-07 — Available customization

Customization comes from the current exports and prop declarations. Framework-independent: The overlay implementation uses DOM/TypeScript rather than React. Lifecycle contract: Await ready, subscribe deliberately and destroy on unmount. Two integration levels: Direct overlay for a container; manager for floating widgets. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494

## lib-chat-overlay-08 — Find the integration and its checks

Actual consumers: apps/chat-overlay-sandbox/src/cases/ConversationListCase/ConversationListCase.tsx; apps/chat-overlay-sandbox/src/cases/EnabledFeaturesCase/EnabledFeaturesCase.tsx; apps/chat-overlay-sandbox/src/cases/ManagerOverlayCase/ManagerOverlayCase.tsx; apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx; apps/chat/src/components/CatalogView/CatalogView.tsx; apps/chat/src/pages/SettingsPage/PreferencesTab/PreferencesTab.tsx. Existing test evidence: [{"file": "libs/chat-overlay/src/lib/tests/ChatOverlay.spec.ts", "assertions": ["ChatOverlay", "throws a descriptive error when the root selector matches nothing", "creates an iframe with a non-empty accessible name", "allows auth popups to open outside the iframe sandbox", "styles the root, iframe, and loader from an injected stylesheet instead of inline styles", "injects the stylesheet once per document", "keeps a host loaderClass alongside the default loader class", "does not add the positioning class to a root with existing non-static positioning", "does not request microphone permission by default", "requests microphone permission when voice input is enabled", "hides the default loader on READY when loaderHideEvent is unset", "keeps the loader visible until the configured loaderHideEvent", "hides the loader even when loaderStyles pins an inline display", "keeps non-display loaderStyles entries after the loader hides", "reads the loader palette from themable custom properties"]}, {"file": "libs/chat-overlay/src/lib/tests/ChatOverlayManager.spec.ts", "assertions": ["ChatOverlayManager", "throws a descriptive error for an unknown overlayId", "creates a toggle button with a non-empty accessible name", "makes toggle, close, and fullscreen buttons keyboard-focusable in DOM order", "grants fullscreen permission to the iframe when allowFullscreen is set", "forwards ready() to the requested overlay", "shows the panel and hides the toggle button on showOverlay", "removes the container and toggle button on removeOverlay, and further calls throw", "destroys all overlays and stops recomputing layout on resize", "conversation-list method forwarding", "throws a descriptive error for an unknown overlayId for each new method", "forwards each new method to the underlying ChatOverlay instance with the same arguments", "forwards setOverlayOptions with enabledFeatures unchanged to the underlying ChatOverlay instance"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-chat-overlay:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494; apps/chat-overlay-sandbox/src/cases/ConversationListCase/ConversationListCase.tsx:1-317; libs/chat-overlay/src/lib/tests/ChatOverlay.spec.ts:1-1060; libs/chat-overlay/src/lib/tests/ChatOverlayManager.spec.ts:1-229

## lib-chat-overlay-09 — Constraints that affect integration

Review these constraints before choosing the library. Embedding policy: The server must allow the host origin in frame-ancestors. Auth constraints: Provider iframe behavior varies; configure supported login UI modes. No server replacement: The overlay still needs a running chat and backend. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/chat-overlay/README.md:1-307; libs/chat-overlay/src/index.ts:1-4; libs/chat-overlay/package.json:1-30; libs/chat-overlay/src/lib/ChatOverlay.ts:110-494; AGENTS.md:1-176

## lib-chat-shared-01 — Chat shared

This session explains share domain vocabulary, utilities and common ui primitives. The library is a local private workspace package at libs/chat-shared. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14

## lib-chat-shared-02 — When this library is useful

Start with a concrete caller need. Agree on shapes: Use the same message, stage and attachment types. Reuse common UI: Share Markdown, icons and resource summaries. Bridge file managers: Use a typed controller without host persistence knowledge. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14

## lib-chat-shared-03 — Follow the ownership boundary

The library owns Shared models, pure utilities, UI primitives and narrow file-manager event bindings. The host owns App providers, authentication, routing, storage keys and external-system configuration.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14; AGENTS.md:1-176

## lib-chat-shared-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14

## lib-chat-shared-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/chat-shared.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Use the same message, stage and attachment types. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14

## lib-chat-shared-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Resolve host values: Choose the text and theme values in the application. Render shared content: Use MarkdownRenderer and buildCssVars in a host view. Keep integration local: Wire file-manager callbacks and persistence in the host. The complete typed module in examples/chat-shared.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14

## lib-chat-shared-10 — Reuse the Markdown entry

This fragment is part of SharedDemo. The renderer needs the host stylesheet and the dependencies of the selected entry point. Do not treat the shared package as types-only.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14

## lib-chat-shared-07 — Available customization

Customization comes from the current exports and prop declarations. Focused entries: /markdown and /file-manager expose narrower entry points. CSS variable builder: buildCssVars drops undefined and empty values. Canonical grid hook: useGridEditingScroll lives here and is re-exported by chat-hooks. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14

## lib-chat-shared-08 — Find the integration and its checks

Actual consumers: libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx; libs/prompt-editor/src/components/PromptFolderField/PromptFolderField.tsx; libs/skills/src/hooks/useSkillSelectorOverlay/useSkillSelectorOverlay.tsx; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx; libs/skills/src/components/ChatSkill/ChatSkill.tsx; libs/usage-dashboard/src/components/ModelLimitsSection/PeriodStatusIndicator.tsx. Existing test evidence: [{"file": "libs/chat-shared/src/file-manager/FileManagerAttachModal/tests/FileManagerAttachModal.spec.tsx", "assertions": ["FileManagerAttachModal", "Attach button disabled state", "disables the Attach button when no paths are selected", "disables the Attach button while the controller is loading", "disables the Attach button while an operation is in progress", "enables the Attach button when a file is selected and idle", "Attach button click", "calls onAttach with the selected file when Attach is clicked", "calls onAttach with the resolved folder path when a folder is selected", "skips folders whose resolveFolderPath returns null", "count limit exceeded", "calls onCountLimitExceeded and does not call onAttach when the limit is exceeded", "unsupported file type", "calls onSkippedUnsupportedFiles when a file with a disallowed type is selected", "shell callback forwarding"]}, {"file": "libs/chat-shared/src/file-manager/useGridEditingScroll/tests/useGridEditingScroll.spec.ts", "assertions": ["useGridEditingScroll", "calls ensureIndexVisible with the row index when inline rename starts", "does not call ensureIndexVisible when the grid api is destroyed", "seeds known row ids on the first rowDataUpdated after mount without scrolling", "scrolls the temporary new-folder row into view when a new row appears", "does not scroll when rowDataUpdated introduces no new row ids", "removes listeners from the previous grid api when a new api instance is passed", "removes listeners from the subscribed api when the hook unmounts", "does not attach duplicate listeners when the same api instance is passed twice", "treats the first rowDataUpdated after reset() as a fresh seed with no scroll"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-chat-shared:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: disables the Attach button when no paths are selected.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:1-310; libs/chat-shared/src/file-manager/FileManagerAttachModal/tests/FileManagerAttachModal.spec.tsx:1-484; libs/chat-shared/src/file-manager/useGridEditingScroll/tests/useGridEditingScroll.spec.ts:1-258

## lib-chat-shared-09 — Constraints that affect integration

Review these constraints before choosing the library. More than types: The source includes runtime utilities and rendered UI. Entry-specific peers: The file-manager entry needs its optional peer pair installed. Legacy boundary assumptions: The old no-dependencies description is not the current graph. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/chat-shared/README.md:1-986; libs/chat-shared/src/index.ts:1-73; libs/chat-shared/package.json:1-80; libs/chat-shared/src/utils/build-css-vars.ts:4-14; AGENTS.md:1-176

## lib-conversation-input-01 — Conversation input

This session explains compose a message with deployment, attachment and voice controls. The library is a local private workspace package at libs/conversation-input. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/conversation-input/README.md:1-355; libs/conversation-input/src/index.ts:1-35; libs/conversation-input/package.json:1-42; libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78; libs/conversation-input/src/models/ConversationInput.ts:182-455

## lib-conversation-input-02 — When this library is useful

Start with a concrete caller need. Send a message: Collect text and attachments, then invoke a host callback. Control generation: Swap sending for a stop action while streaming. Support rich input: Wire deployment selection, settings and audio transcription. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/conversation-input/README.md:1-355; libs/conversation-input/src/index.ts:1-35; libs/conversation-input/package.json:1-42; libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78; libs/conversation-input/src/models/ConversationInput.ts:182-455

## lib-conversation-input-03 — Follow the ownership boundary

The library owns Composer interaction, local text/attachment state and input controls. The host owns Model data, upload and transcription services, sending and generation state.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/conversation-input/README.md:1-355; libs/conversation-input/src/index.ts:1-35; libs/conversation-input/package.json:1-42; libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78; libs/conversation-input/src/models/ConversationInput.ts:182-455; AGENTS.md:1-176

## lib-conversation-input-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/conversation-input/README.md:1-355; libs/conversation-input/src/index.ts:1-35; libs/conversation-input/package.json:1-42; libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78; libs/conversation-input/src/models/ConversationInput.ts:182-455

## lib-conversation-input-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/conversation-input.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Collect text and attachments, then invoke a host callback. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/conversation-input/README.md:1-355; libs/conversation-input/src/index.ts:1-35; libs/conversation-input/package.json:1-42; libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78; libs/conversation-input/src/models/ConversationInput.ts:182-455

## lib-conversation-input-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Collect intent: Let the composer gather text and emit onSend. Start the request: The host chooses the conversation and calls its adapter. Reflect generation: Pass the current input and generation state back to the UI. The complete typed module in examples/conversation-input.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/conversation-input/README.md:1-355; libs/conversation-input/src/index.ts:1-35; libs/conversation-input/package.json:1-42; libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78; libs/conversation-input/src/models/ConversationInput.ts:182-455

## lib-conversation-input-07 — Available customization

Customization comes from the current exports and prop declarations. Controlled updates: messageRevision and textInsertion coordinate host-driven edits. Separate attachment UI: Import attachment cards and trays from attachment-input. Voice extension: Inject a transcription callback and supported deployment data. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/conversation-input/README.md:1-355; libs/conversation-input/src/index.ts:1-35; libs/conversation-input/package.json:1-42; libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78; libs/conversation-input/src/models/ConversationInput.ts:182-455

## lib-conversation-input-08 — Find the integration and its checks

Actual consumers: apps/chat/src/hooks/conversation/useAudioTranscription.ts; libs/navigation-panel/src/components/NavigationSheet/NavigableBottomSheet.tsx; apps/chat/src/hooks/keyboard-shortcut/useKeyboardShortcutPreference.ts; apps/chat/src/pages/SettingsPage/PreferencesTab/PreferencesTab.tsx; apps/chat/src/hooks/navigation/useNavigationMenuGroups.tsx; libs/skills/src/hooks/useSkillSelectorOverlay/useSkillSelectorOverlay.tsx. Existing test evidence: [{"file": "libs/conversation-input/src/hooks/tests/useModelSelector.spec.tsx", "assertions": ["useModelSelector \u2014 selectorAriaLabel", "uses default label when no deployment is selected", "appends selected item displayName to the label", "uses custom ariaLabel from modelSelectorLabels", "falls back to item id when displayName is absent", "useModelSelector \u2014 menuItems", "returns empty array when deployments is undefined", "returns empty array when deployments is empty and no state label", "returns seven disabled skeleton items when deployments are loading", "prefers loading label over error and empty labels", "shows skeleton items during a reload even when deployments already exist", "falls back to error label when loading is absent", "returns one item per deployment preserving input order", "updates the active item when selectedDeploymentId changes", "item onClick calls onDeploymentChange with item id"]}, {"file": "libs/conversation-input/src/hooks/tests/useVoiceRecorder.spec.ts", "assertions": ["useVoiceRecorder", "transcribes actual browser MIME and releases microphone before recognition completes", "attaches audio when no recognition callback is provided", "ignores an old result after discard and a new recording", "shows failures and lets discard restore idle state", "releases microphone if permission resolves after unmount", "complete recording", "waits for Stop and sends all blobs as one file exactly once", "does not recognize a discarded recording", "ignores final browser events after cancellation", "releases late microphone permission after Stop without recognition"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-conversation-input:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/conversation-input/README.md:1-355; libs/conversation-input/src/index.ts:1-35; libs/conversation-input/package.json:1-42; libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78; libs/conversation-input/src/models/ConversationInput.ts:182-455; apps/chat/src/hooks/conversation/useAudioTranscription.ts:1-100; libs/conversation-input/src/hooks/tests/useModelSelector.spec.tsx:1-309; libs/conversation-input/src/hooks/tests/useVoiceRecorder.spec.ts:1-265

## lib-conversation-input-09 — Constraints that affect integration

Review these constraints before choosing the library. No completion client: onSend is the integration point for a real generation flow. Provider assumptions: Feature-specific settings and menus need caller-supplied data. Avoid state resets: Keep initialization and host insertion changes intentional. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/conversation-input/README.md:1-355; libs/conversation-input/src/index.ts:1-35; libs/conversation-input/package.json:1-42; libs/conversation-input/src/components/ConversationInput/ConversationInput.tsx:8-78; libs/conversation-input/src/models/ConversationInput.ts:182-455; AGENTS.md:1-176

## lib-conversation-messages-01 — Conversation messages

This session explains render a transcript from host-owned messages and actions. The library is a local private workspace package at libs/conversation-messages. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/conversation-messages/README.md:1-236; libs/conversation-messages/src/index.ts:1-35; libs/conversation-messages/package.json:1-41; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236; libs/conversation-messages/src/models/message-bubble.ts:143-170

## lib-conversation-messages-02 — When this library is useful

Start with a concrete caller need. Display roles: Use user, assistant and status bubble variants. Reveal a response: Render updated Markdown while a generation is active. Compose evidence: Place stages, citations and attachments beside the answer. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/conversation-messages/README.md:1-236; libs/conversation-messages/src/index.ts:1-35; libs/conversation-messages/package.json:1-41; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236; libs/conversation-messages/src/models/message-bubble.ts:143-170

## lib-conversation-messages-03 — Follow the ownership boundary

The library owns Bubble layout, Markdown display and action controls. The host owns Message ordering, network streams, persistence, ratings and attachment access.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/conversation-messages/README.md:1-236; libs/conversation-messages/src/index.ts:1-35; libs/conversation-messages/package.json:1-41; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236; libs/conversation-messages/src/models/message-bubble.ts:143-170; AGENTS.md:1-176

## lib-conversation-messages-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/conversation-messages/README.md:1-236; libs/conversation-messages/src/index.ts:1-35; libs/conversation-messages/package.json:1-41; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236; libs/conversation-messages/src/models/message-bubble.ts:143-170

## lib-conversation-messages-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/conversation-messages.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Use user, assistant and status bubble variants. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/conversation-messages/README.md:1-236; libs/conversation-messages/src/index.ts:1-35; libs/conversation-messages/package.json:1-41; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236; libs/conversation-messages/src/models/message-bubble.ts:143-170

## lib-conversation-messages-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Prepare a message: The host supplies response text and streaming state. Compose evidence: Insert StagesPanel through the afterContent slot. Connect actions: Keep regeneration, feedback and persistence in the host. The complete typed module in examples/conversation-messages.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/conversation-messages/README.md:1-236; libs/conversation-messages/src/index.ts:1-35; libs/conversation-messages/package.json:1-41; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236; libs/conversation-messages/src/models/message-bubble.ts:143-170

## lib-conversation-messages-07 — Available customization

Customization comes from the current exports and prop declarations. Extension slots: beforeContent and afterContent add skill chips or stage panels. Host URL rewriting: markdownUrlTransform maps resource references before rendering. Transcript controls: Supply MessageActions props and localized action labels. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/conversation-messages/README.md:1-236; libs/conversation-messages/src/index.ts:1-35; libs/conversation-messages/package.json:1-41; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236; libs/conversation-messages/src/models/message-bubble.ts:143-170

## lib-conversation-messages-08 — Find the integration and its checks

Actual consumers: apps/chat/src/components/ConversationView/ConversationMessageItem.tsx; apps/chat/src/components/ConversationView/ConversationView.tsx; apps/chat/src/components/ConversationView/utils/build-message-actions.ts. Existing test evidence: [{"file": "libs/conversation-messages/src/components/MessageActions/tests/MessageActions.spec.tsx", "assertions": ["MessageActions", "role=User (default)", "renders Edit and Delete buttons", "does not render Agent action buttons", "calls onEdit when Edit button is clicked", "calls onDelete when Delete button is clicked", "role=Assistant", "renders Regenerate, Copy, Markdown, Like, and Dislike buttons", "does not render User action buttons", "calls onRegenerate when Regenerate button is clicked", "calls onCopy when Copy button is clicked", "calls onCopyMarkdown when Markdown button is clicked", "calls onLike when Like button is clicked", "calls onDislike when Dislike button is clicked", "isDisabled"]}, {"file": "libs/conversation-messages/src/components/MessageBubble/tests/MessageBubble.classes.spec.tsx", "assertions": ["UserMessageBubble \u2014 public class names", "marks the bubble that wraps the message text", "emits no bubble class when there is no text or before-content", "keeps a caller-supplied bubbleClassName alongside the public class", "AssistantMessageBubble \u2014 public class names", "marks the live content region for a settled message", "marks the live content region while streaming"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-conversation-messages:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: calls onEdit when Edit button is clicked.

Sources: libs/conversation-messages/README.md:1-236; libs/conversation-messages/src/index.ts:1-35; libs/conversation-messages/package.json:1-41; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236; libs/conversation-messages/src/models/message-bubble.ts:143-170; apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898; libs/conversation-messages/src/components/MessageActions/tests/MessageActions.spec.tsx:1-269; libs/conversation-messages/src/components/MessageBubble/tests/MessageBubble.classes.spec.tsx:1-92

## lib-conversation-messages-09 — Constraints that affect integration

Review these constraints before choosing the library. Streaming is visual: isStreaming does not open a network stream. Status messages: Shared MessageRole.Status is a UI event, not an upstream author role. Source integrations: Citation components and canvas actions require host wiring. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/conversation-messages/README.md:1-236; libs/conversation-messages/src/index.ts:1-35; libs/conversation-messages/package.json:1-41; libs/conversation-messages/src/components/MessageBubble/AssistantMessageBubble.tsx:28-236; libs/conversation-messages/src/models/message-bubble.ts:143-170; AGENTS.md:1-176

## lib-conversation-panel-01 — Conversation panel

This session explains navigate a large conversation history with a small visible list. The library is a local private workspace package at libs/conversation-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/conversation-panel/README.md:1-406; libs/conversation-panel/src/index.ts:1-28; libs/conversation-panel/package.json:1-41; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507; libs/conversation-panel/src/models/panel-props.ts:162-223

## lib-conversation-panel-02 — When this library is useful

Start with a concrete caller need. Resume work: Select a conversation from a grouped history list. Find context: Search titles and filter by source. Manage history: Expose rename, move, pin and transfer actions. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/conversation-panel/README.md:1-406; libs/conversation-panel/src/index.ts:1-28; libs/conversation-panel/package.json:1-41; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507; libs/conversation-panel/src/models/panel-props.ts:162-223

## lib-conversation-panel-03 — Follow the ownership boundary

The library owns Windowed rows, grouping, search UI and per-row interaction. The host owns Ordered data, active route, storage changes and action implementations.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/conversation-panel/README.md:1-406; libs/conversation-panel/src/index.ts:1-28; libs/conversation-panel/package.json:1-41; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507; libs/conversation-panel/src/models/panel-props.ts:162-223; AGENTS.md:1-176

## lib-conversation-panel-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/conversation-panel/README.md:1-406; libs/conversation-panel/src/index.ts:1-28; libs/conversation-panel/package.json:1-41; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507; libs/conversation-panel/src/models/panel-props.ts:162-223

## lib-conversation-panel-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/conversation-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Select a conversation from a grouped history list. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/conversation-panel/README.md:1-406; libs/conversation-panel/src/index.ts:1-28; libs/conversation-panel/package.json:1-41; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507; libs/conversation-panel/src/models/panel-props.ts:162-223

## lib-conversation-panel-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Load summaries: Supply conversation ids, titles and the active id. Handle selection: Use onSelectConversation to choose a host-owned route. Load the transcript: The host loads messages for the selected conversation. The complete typed module in examples/conversation-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/conversation-panel/README.md:1-406; libs/conversation-panel/src/index.ts:1-28; libs/conversation-panel/package.json:1-41; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507; libs/conversation-panel/src/models/panel-props.ts:162-223

## lib-conversation-panel-07 — Available customization

Customization comes from the current exports and prop declarations. Stable row data: Items carry title, source, pinned state and optional unread/task badges. Action extension: getActions and onActionMenuOpen inject row actions. Transfer surfaces: ImportExportQueue and RenameConversationPopup are separate exports. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/conversation-panel/README.md:1-406; libs/conversation-panel/src/index.ts:1-28; libs/conversation-panel/package.json:1-41; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507; libs/conversation-panel/src/models/panel-props.ts:162-223

## lib-conversation-panel-08 — Find the integration and its checks

Actual consumers: apps/chat/src/components/ConversationPanel/ConversationPanelView.tsx. Existing test evidence: [{"file": "libs/conversation-panel/src/components/FilterTabs/tests/FilterTabs.spec.tsx", "assertions": ["FilterTabs", "renders a tab for each filter", "marks only the active tab as pressed", "names the filter row so the group is announced", "applies flex-1 by default so the tabs fill the row equally", "applies the provided typography class to each tab", "omits a tab listed in hiddenSources"]}, {"file": "libs/conversation-panel/src/components/ConversationRow/tests/ConversationRow.spec.tsx", "assertions": ["ConversationRow", "renders a skeleton when isIconLoading is true", "skeleton has aria-hidden=", "skeleton is rendered with Circular variant at DIAL_ICON_SIZE.LG dimensions", "renders DeploymentIcon when isIconLoading is false and iconUrl is set", "renders DeploymentIcon when isIconLoading is omitted", "renders DeploymentIcon fallback when isIconLoading is false and iconUrl is absent", "exposes the action trigger when its menu opens", "renders the task badge when showTaskBadge is true", "does not render the task badge when showTaskBadge is omitted", "does not render the task badge when showTaskBadge is false", "marks the task badge icon as aria-hidden", "clicking the task badge selects the conversation like any other row click", "unread indicator", "renders the unread dot with an accessible label when isUnread is true"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-conversation-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/conversation-panel/README.md:1-406; libs/conversation-panel/src/index.ts:1-28; libs/conversation-panel/package.json:1-41; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507; libs/conversation-panel/src/models/panel-props.ts:162-223; apps/chat/src/components/ConversationPanel/ConversationPanelView.tsx:1-1510; libs/conversation-panel/src/components/FilterTabs/tests/FilterTabs.spec.tsx:1-61; libs/conversation-panel/src/components/ConversationRow/tests/ConversationRow.spec.tsx:1-356

## lib-conversation-panel-09 — Constraints that affect integration

Review these constraints before choosing the library. Preserve ordering: The host supplies an already-ordered flat list. Selection is not routing: onSelectConversation returns an id for the host to interpret. Virtualized content: Only a subset of rows exists in the DOM at a time. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/conversation-panel/README.md:1-406; libs/conversation-panel/src/index.ts:1-28; libs/conversation-panel/package.json:1-41; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx:52-507; libs/conversation-panel/src/models/panel-props.ts:162-223; AGENTS.md:1-176

## lib-conversation-stages-01 — Conversation stages

This session explains make streamed execution progress visible inside a response. The library is a local private workspace package at libs/conversation-stages. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/conversation-stages/README.md:1-142; libs/conversation-stages/src/index.ts:1-17; libs/conversation-stages/package.json:1-39; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229; libs/conversation-stages/src/models/stages-props.ts:78-89

## lib-conversation-stages-02 — When this library is useful

Start with a concrete caller need. Explain waiting: Show named running stages while content arrives. Inspect a step: Expand stage Markdown and copy useful details. Reduce noise: Collapse related work into a compact group. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/conversation-stages/README.md:1-142; libs/conversation-stages/src/index.ts:1-17; libs/conversation-stages/package.json:1-39; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229; libs/conversation-stages/src/models/stages-props.ts:78-89

## lib-conversation-stages-03 — Follow the ownership boundary

The library owns Stage display, expansion, status icons and Markdown details. The host owns Receiving and merging stage updates, status truth and generation lifecycle.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/conversation-stages/README.md:1-142; libs/conversation-stages/src/index.ts:1-17; libs/conversation-stages/package.json:1-39; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229; libs/conversation-stages/src/models/stages-props.ts:78-89; AGENTS.md:1-176

## lib-conversation-stages-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/conversation-stages/README.md:1-142; libs/conversation-stages/src/index.ts:1-17; libs/conversation-stages/package.json:1-39; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229; libs/conversation-stages/src/models/stages-props.ts:78-89

## lib-conversation-stages-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/conversation-stages.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Show named running stages while content arrives. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/conversation-stages/README.md:1-142; libs/conversation-stages/src/index.ts:1-17; libs/conversation-stages/package.json:1-39; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229; libs/conversation-stages/src/models/stages-props.ts:78-89

## lib-conversation-stages-10 — See a streaming stage in context

This is a real browser screenshot of the standalone demo in demo/main.tsx, captured by src/capture-demo.mjs. It renders SettingsPanel, UsageLimitCard and StagesPanel directly from the recorded source snapshot with local stylesheet dependencies. It is an illustrative host, not a screenshot of a deployed DIAL product. All data is synthetic and no backend request is made. Run the Vite command in examples/README.md, then the capture script. Expected behavior: Usage starts selected; selecting Profile updates the controlled active row. The amount and stage remain demo data. The host explicitly supplies dark-theme color overrides. Desktop and phone captures are retained under assets/.

Sources: libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229

## lib-conversation-stages-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Read stream updates: The host obtains the current stage records. Supply stage state: Pass stages and isStreaming into StagesPanel. Inspect the details: The panel renders stage status and expandable content. The complete typed module in examples/conversation-stages.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/conversation-stages/README.md:1-142; libs/conversation-stages/src/index.ts:1-17; libs/conversation-stages/package.json:1-39; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229; libs/conversation-stages/src/models/stages-props.ts:78-89

## lib-conversation-stages-07 — Available customization

Customization comes from the current exports and prop declarations. Explicit running state: null status represents a running stage in the shared Stage model. Streaming awareness: isStreaming controls the active presentation lifecycle. Grouped detail: CollapsedGroup provides a compact wrapper for related stages. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/conversation-stages/README.md:1-142; libs/conversation-stages/src/index.ts:1-17; libs/conversation-stages/package.json:1-39; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229; libs/conversation-stages/src/models/stages-props.ts:78-89

## lib-conversation-stages-08 — Find the integration and its checks

Actual consumers: apps/chat/src/components/ConversationView/ConversationMessageItem.tsx. Existing test evidence: [{"file": "libs/conversation-stages/src/components/CollapsedGroup/tests/CollapsedGroup.spec.tsx", "assertions": ["CollapsedGroup \u2014 collapsed states", "renders nothing for an empty stage list", "renders a single stage directly, with no summary wrapper", "collapses to a finished summary line by default once the run finishes", "collapses to a failed summary with the failed count called out", "shows elapsed time without double-counting parallel stages", "is expanded by default while running, showing progress through the live step", "keeps a long live stage name on one truncated line", "announces the running summary via a polite live region", "CollapsedGroup \u2014 collapse-by-default-when-finished transition", "auto-collapses the moment a running group finishes", "CollapsedGroup \u2014 labels", "uses the supplied executedLabel/stepsLabel for the finished summary", "conversation-stages \u2014 public class names", "stamps the panel root behind a collapsed group"]}, {"file": "libs/conversation-stages/src/components/StagesPanel/tests/StagesPanel.spec.tsx", "assertions": ["StagesPanel", "renders all stage rows", "applies custom className and the new row-level CSS variable colors", "applies typography.fontClassName to each stage row name", "defaults the row name to dial-small-text and expanded content to dial-tiny-text", "defaults every heading level in expanded content to dial-small-semi-text (14px, semibold)", "applies typography.headingClassName to every heading level in expanded content", "renders a stage with content as a disclosure button that toggles the content", "renders a stage without expandable content as a plain row (no button)", "does not show a running spinner for null-status stages when not streaming", "keeps every null-status stage running until its completed status arrives", "collapses repeated identical names into one \u00d7N row that expands to the individual attempts", "keeps a repeated-stage group running while any attempt is unresolved", "does not double-count overlapping attempts in a collapsed stage row"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-conversation-stages:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/conversation-stages/README.md:1-142; libs/conversation-stages/src/index.ts:1-17; libs/conversation-stages/package.json:1-39; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229; libs/conversation-stages/src/models/stages-props.ts:78-89; apps/chat/src/components/ConversationView/ConversationMessageItem.tsx:1-898; libs/conversation-stages/src/components/CollapsedGroup/tests/CollapsedGroup.spec.tsx:1-245; libs/conversation-stages/src/components/StagesPanel/tests/StagesPanel.spec.tsx:1-315

## lib-conversation-stages-09 — Constraints that affect integration

Review these constraints before choosing the library. Progress is supplied: The component cannot infer the backend work completed. Keep identity stable: Stage index is used when upstream updates are merged. Content sensitivity: Only pass execution details intended for the user to see. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/conversation-stages/README.md:1-142; libs/conversation-stages/src/index.ts:1-17; libs/conversation-stages/package.json:1-39; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:161-229; libs/conversation-stages/src/models/stages-props.ts:78-89; AGENTS.md:1-176

## lib-mcp-apps-01 — MCP Apps

This session explains connect tool-result ui resources to an inline interactive preview. The library is a local private workspace package at libs/mcp-apps. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/mcp-apps/README.md:1-148; libs/mcp-apps/src/index.ts:1-31; libs/mcp-apps/package.json:1-42; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65

## lib-mcp-apps-02 — When this library is useful

Start with a concrete caller need. Find a tool UI: Match a message to an MCP tool resource. Reuse the result: Seed the preview from the original tool call. Expand the UI: Open the matched application in the attachment canvas. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/mcp-apps/README.md:1-148; libs/mcp-apps/src/index.ts:1-31; libs/mcp-apps/package.json:1-42; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65

## lib-mcp-apps-03 — Follow the ownership boundary

The library owns Preview state, matching/seed helpers and a per-conversation response cache. The host owns Configured resource/tool calls, sandbox URL, host context and expansion behavior.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/mcp-apps/README.md:1-148; libs/mcp-apps/src/index.ts:1-31; libs/mcp-apps/package.json:1-42; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65; AGENTS.md:1-176

## lib-mcp-apps-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/mcp-apps/README.md:1-148; libs/mcp-apps/src/index.ts:1-31; libs/mcp-apps/package.json:1-42; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65

## lib-mcp-apps-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/mcp-apps.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Match a message to an MCP tool resource. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/mcp-apps/README.md:1-148; libs/mcp-apps/src/index.ts:1-31; libs/mcp-apps/package.json:1-42; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65

## lib-mcp-apps-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Match tool evidence: Provide the resource match and a stable cache key. Inject the host adapter: The host fetches resources and handles tool calls. Reuse cached state: Keep response caching scoped to the conversation lifetime. The complete typed module in examples/mcp-apps.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/mcp-apps/README.md:1-148; libs/mcp-apps/src/index.ts:1-31; libs/mcp-apps/package.json:1-42; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65

## lib-mcp-apps-07 — Available customization

Customization comes from the current exports and prop declarations. Explicit host adapter: Inject fetchResourceHtml, callTool, hostInfo and sandboxUrl. Cache identity: Entries are checked against seed identity and expiry. Lifecycle state: Loading, Ready, Error and Unavailable are distinct enum values. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/mcp-apps/README.md:1-148; libs/mcp-apps/src/index.ts:1-31; libs/mcp-apps/package.json:1-42; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65

## lib-mcp-apps-08 — Find the integration and its checks

Actual consumers: libs/chat-hooks/src/mcp-apps/useMcpAppTools/useMcpAppTools.ts; libs/chat-hooks/src/mcp-apps/mcp-apps-api-client.ts; libs/chat-hooks/src/mcp-apps/useMcpAppHostAdapter/useMcpAppHostAdapter.ts; libs/chat-hooks/src/mcp-apps/useOpenMcpAppCanvas/useOpenMcpAppCanvas.ts; apps/chat/src/components/ConversationView/ConversationMessageItem.tsx; apps/chat/src/components/ConversationView/ConversationView.tsx. Existing test evidence: [{"file": "libs/mcp-apps/src/components/McpAppInlinePreview/tests/McpAppInlinePreview.classes.spec.tsx", "assertions": ["McpAppInlinePreview \u2014 public class names", "stamps the preview card and its header", "forwards every colour override as a CSS custom property"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-mcp-apps:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/mcp-apps/README.md:1-148; libs/mcp-apps/src/index.ts:1-31; libs/mcp-apps/package.json:1-42; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65; libs/chat-hooks/src/mcp-apps/useMcpAppTools/useMcpAppTools.ts:1-118; libs/mcp-apps/src/components/McpAppInlinePreview/tests/McpAppInlinePreview.classes.spec.tsx:1-141

## lib-mcp-apps-09 — Constraints that affect integration

Review these constraints before choosing the library. Origin isolation required: Configure the separate MCP sandbox deployment. Avoid duplicate side effects: Indirectly discovered tools are not safe to re-call blindly. Not a general API client: Backend operations enter through the host adapter. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/mcp-apps/README.md:1-148; libs/mcp-apps/src/index.ts:1-31; libs/mcp-apps/package.json:1-42; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:247-247; libs/mcp-apps/src/components/McpAppInlinePreview/McpAppInlinePreview.tsx:33-65; AGENTS.md:1-176

## lib-navigation-panel-01 — Navigation panel

This session explains reuse navigation destinations across desktop and mobile chrome. The library is a local private workspace package at libs/navigation-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/navigation-panel/README.md:1-208; libs/navigation-panel/src/index.ts:1-54; libs/navigation-panel/package.json:1-40; libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111; libs/navigation-panel/src/models/navigation-panel-props.ts:60-73

## lib-navigation-panel-02 — When this library is useful

Start with a concrete caller need. Navigate an app: Render a desktop destination rail. Use a phone: Show destinations and settings inside a bottom sheet. Declare settings once: Share menu groups across rail menus and mobile pages. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/navigation-panel/README.md:1-208; libs/navigation-panel/src/index.ts:1-54; libs/navigation-panel/package.json:1-40; libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111; libs/navigation-panel/src/models/navigation-panel-props.ts:60-73

## lib-navigation-panel-03 — Follow the ownership boundary

The library owns Rail, user menu, mobile sheet and its local page stack. The host owns Routes, authentication, active destination, labels and resolved brand assets.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/navigation-panel/README.md:1-208; libs/navigation-panel/src/index.ts:1-54; libs/navigation-panel/package.json:1-40; libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111; libs/navigation-panel/src/models/navigation-panel-props.ts:60-73; AGENTS.md:1-176

## lib-navigation-panel-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/navigation-panel/README.md:1-208; libs/navigation-panel/src/index.ts:1-54; libs/navigation-panel/package.json:1-40; libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111; libs/navigation-panel/src/models/navigation-panel-props.ts:60-73

## lib-navigation-panel-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/navigation-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Render a desktop destination rail. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/navigation-panel/README.md:1-208; libs/navigation-panel/src/index.ts:1-54; libs/navigation-panel/package.json:1-40; libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111; libs/navigation-panel/src/models/navigation-panel-props.ts:60-73

## lib-navigation-panel-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Prepare destinations: The host supplies item ids, labels and active state. Render host links: Use renderLink to bind each item to the chosen router. Reflect navigation: Update active state when the application route changes. The complete typed module in examples/navigation-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/navigation-panel/README.md:1-208; libs/navigation-panel/src/index.ts:1-54; libs/navigation-panel/package.json:1-40; libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111; libs/navigation-panel/src/models/navigation-panel-props.ts:60-73

## lib-navigation-panel-07 — Available customization

Customization comes from the current exports and prop declarations. Router integration: renderLink wraps destination children with the host link element. Mobile stack: NavigableBottomSheet and useSheetNavigation manage drill-down pages. Shared menus: NavigationMenuGroup describes selectable settings options. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/navigation-panel/README.md:1-208; libs/navigation-panel/src/index.ts:1-54; libs/navigation-panel/package.json:1-40; libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111; libs/navigation-panel/src/models/navigation-panel-props.ts:60-73

## lib-navigation-panel-08 — Find the integration and its checks

Actual consumers: apps/chat/src/components/Navigation/Navigation.tsx; apps/chat/src/hooks/navigation/useNavigationMenuGroups.tsx; apps/chat/src/hooks/navigation/useNavigationItems.ts; apps/chat/src/hooks/navigation/useNavigationUserProfile.ts. Existing test evidence: [{"file": "libs/navigation-panel/src/components/NavigationPanel/tests/NavigationPanel.spec.tsx", "assertions": ["NavigationPanel", "renders the nav landmark with the given accessible name", "renders one labelled button per item", "marks only the active item with aria-current=", "wraps items in plain anchors carrying their href by default", "delegates link rendering to renderLink when provided", "renders the logo link when a logo is supplied", "omits the logo link when no logo is supplied", "renders the footer slot", "NavigationPanel \u2014 public class names", "stamps the rail and every item"]}, {"file": "libs/navigation-panel/src/components/UserMenu/tests/UserMenu.spec.tsx", "assertions": ["UserMenu", "labels the avatar trigger", "renders the avatar image when an image URL is supplied", "falls back to initials when no image URL is supplied", "reports a broken avatar image through onImageError", "renders each settings group with its options", "marks the applied option as the checked single choice of the menu", "applies an option through its onSelect callback", "skips groups that have no options", "calls onLogout when the log-out entry is clicked", "renders a settings entry when onSettings is provided", "does not render a settings entry when onSettings is omitted", "calls onSettings when the settings entry is clicked"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-navigation-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/navigation-panel/README.md:1-208; libs/navigation-panel/src/index.ts:1-54; libs/navigation-panel/package.json:1-40; libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111; libs/navigation-panel/src/models/navigation-panel-props.ts:60-73; apps/chat/src/components/Navigation/Navigation.tsx:1-129; libs/navigation-panel/src/components/NavigationPanel/tests/NavigationPanel.spec.tsx:1-143; libs/navigation-panel/src/components/UserMenu/tests/UserMenu.spec.tsx:1-245

## lib-navigation-panel-09 — Constraints that affect integration

Review these constraints before choosing the library. Responsive selection: The host chooses which surface to render. No login system: UserMenu displays supplied profile data and callbacks. Explicit logos: Resolve logo URLs before passing them into NavigationPanel. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/navigation-panel/README.md:1-208; libs/navigation-panel/src/index.ts:1-54; libs/navigation-panel/package.json:1-40; libs/navigation-panel/src/components/NavigationPanel/NavigationPanel.tsx:29-111; libs/navigation-panel/src/models/navigation-panel-props.ts:60-73; AGENTS.md:1-176

## lib-prompt-editor-01 — Prompt editor

This session explains author reusable prompt content while leaving persistence to the host. The library is a local private workspace package at libs/prompt-editor. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/prompt-editor/README.md:1-160; libs/prompt-editor/src/index.ts:1-16; libs/prompt-editor/package.json:1-37; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310; libs/prompt-editor/src/models/prompt-editor-props.ts:125-162

## lib-prompt-editor-02 — When this library is useful

Start with a concrete caller need. Create a prompt: Edit name, description and Markdown content. Revise a prompt: Seed the form with stable initialValues. Add folder controls: Compose PromptFolderField separately when needed. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/prompt-editor/README.md:1-160; libs/prompt-editor/src/index.ts:1-16; libs/prompt-editor/package.json:1-37; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310; libs/prompt-editor/src/models/prompt-editor-props.ts:125-162

## lib-prompt-editor-03 — Follow the ownership boundary

The library owns Prompt form fields, editing state and optional folder-field UI. The host owns Save/load operations, validation errors, routes and folder mutations.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/prompt-editor/README.md:1-160; libs/prompt-editor/src/index.ts:1-16; libs/prompt-editor/package.json:1-37; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310; libs/prompt-editor/src/models/prompt-editor-props.ts:125-162; AGENTS.md:1-176

## lib-prompt-editor-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/prompt-editor/README.md:1-160; libs/prompt-editor/src/index.ts:1-16; libs/prompt-editor/package.json:1-37; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310; libs/prompt-editor/src/models/prompt-editor-props.ts:125-162

## lib-prompt-editor-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/prompt-editor.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Edit name, description and Markdown content. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/prompt-editor/README.md:1-160; libs/prompt-editor/src/index.ts:1-16; libs/prompt-editor/package.json:1-37; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310; libs/prompt-editor/src/models/prompt-editor-props.ts:125-162

## lib-prompt-editor-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Load a prompt: Supply initialValues with a name and prompt content. Edit and submit: The editor collects the next values through onSubmit. Save in the host: Persist through an app adapter and decide where to navigate. The complete typed module in examples/prompt-editor.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/prompt-editor/README.md:1-160; libs/prompt-editor/src/index.ts:1-16; libs/prompt-editor/package.json:1-37; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310; libs/prompt-editor/src/models/prompt-editor-props.ts:125-162

## lib-prompt-editor-07 — Available customization

Customization comes from the current exports and prop declarations. Load and save states: isLoading, hasLoadError and isSaving drive the form experience. Editor customization: Pass labels, limits and markdownEditorTheme. Separate folder field: PromptFolderField delegates mutations through folderActions. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/prompt-editor/README.md:1-160; libs/prompt-editor/src/index.ts:1-16; libs/prompt-editor/package.json:1-37; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310; libs/prompt-editor/src/models/prompt-editor-props.ts:125-162

## lib-prompt-editor-08 — Find the integration and its checks

Actual consumers: apps/chat/src/pages/PromptEditor/PromptEditor.tsx. Existing test evidence: [{"file": "libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.classes.spec.tsx", "assertions": ["PromptEditor \u2014 public class names", "stamps the form column that holds the fields"]}, {"file": "libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.spec.tsx", "assertions": ["PromptEditor", "renders the create heading by default", "renders a flat form without section headings, a version field, or a folder picker", "renders the edit heading in edit mode", "seeds the fields from initialValues", "re-seeds the fields when initialValues arrives later", "submits the entered values", "does not validate on its own \u2014 the host owns the storage contract", "renders host-supplied inline errors", "blocks submission and announces status while saving", "renders a labelled spinner instead of the form while loading", "renders an error state with retry instead of an empty form on load failure", "omits the retry button when the host cannot retry", "calls onCancel without submitting", "calls the dedicated back callback from the header"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-prompt-editor:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/prompt-editor/README.md:1-160; libs/prompt-editor/src/index.ts:1-16; libs/prompt-editor/package.json:1-37; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310; libs/prompt-editor/src/models/prompt-editor-props.ts:125-162; apps/chat/src/pages/PromptEditor/PromptEditor.tsx:1-282; libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.classes.spec.tsx:1-39; libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.spec.tsx:1-247

## lib-prompt-editor-09 — Constraints that affect integration

Review these constraints before choosing the library. No built-in folder picker: PromptEditor itself renders no folder field. Stable initial values: Changing their identity can reseed editing state. Host validation: Backend naming and storage rules do not belong in this form. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/prompt-editor/README.md:1-160; libs/prompt-editor/src/index.ts:1-16; libs/prompt-editor/package.json:1-37; libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310; libs/prompt-editor/src/models/prompt-editor-props.ts:125-162; AGENTS.md:1-176

## lib-prompts-01 — Prompts

This session explains pick reusable prompts and collect their parameter values. The library is a local private workspace package at libs/prompts. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/prompts/README.md:1-145; libs/prompts/src/index.ts:1-14; libs/prompts/package.json:1-41; libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174; libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69

## lib-prompts-02 — When this library is useful

Start with a concrete caller need. Choose a favorite: Browse FavoritePromptItem data supplied by the host. Fill placeholders: Collect values for named prompt parameters. Populate a composer: Resolve values and pass the text to host input state. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/prompts/README.md:1-145; libs/prompts/src/index.ts:1-14; libs/prompts/package.json:1-41; libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174; libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69

## lib-prompts-03 — Follow the ownership boundary

The library owns Favorite prompt selection and parameter-entry UI. The host owns Loading favorites, deriving parameters, resolving submitted values and sending text.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/prompts/README.md:1-145; libs/prompts/src/index.ts:1-14; libs/prompts/package.json:1-41; libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174; libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69; AGENTS.md:1-176

## lib-prompts-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/prompts/README.md:1-145; libs/prompts/src/index.ts:1-14; libs/prompts/package.json:1-41; libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174; libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69

## lib-prompts-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/prompts.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Browse FavoritePromptItem data supplied by the host. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/prompts/README.md:1-145; libs/prompts/src/index.ts:1-14; libs/prompts/package.json:1-41; libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174; libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69

## lib-prompts-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Collect parameters: Open PromptParametersPopup with content and parameter names. Resolve the template: Use the submitted value map with resolvePromptParams. Apply the text: The host inserts the resolved text into its composer. The complete typed module in examples/prompts.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/prompts/README.md:1-145; libs/prompts/src/index.ts:1-14; libs/prompts/package.json:1-41; libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174; libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69

## lib-prompts-07 — Available customization

Customization comes from the current exports and prop declarations. Favorite callbacks: Selection, favorite changes and browse actions are caller-owned. Default values: Shared helpers support tokens with a default value. Explicit popup state: open, onClose and onCancel are controlled by the host. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/prompts/README.md:1-145; libs/prompts/src/index.ts:1-14; libs/prompts/package.json:1-41; libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174; libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69

## lib-prompts-08 — Find the integration and its checks

Actual consumers: apps/chat/src/components/PromptSelector/PromptParametersPopupOverlay.tsx; apps/chat/src/components/PromptSelector/PromptSelectorOverlay.tsx; apps/chat/src/components/PromptSelector/usePromptSelectorOverlay.tsx. Existing test evidence: [{"file": "libs/prompts/src/components/PromptParametersPopup/tests/PromptParametersPopup.spec.tsx", "assertions": ["PromptParametersPopup", "renders the title and one field per parameter", "renders one field for a token repeated in the content, via extractPromptParams", "does not render a back chevron when onBack is omitted", "renders a back chevron when onBack is provided", "calls onBack when the back chevron is clicked", "disables Submit until every parameter field is filled", "calls onSubmit with the entered values when Submit is clicked", "opens a defaulted field holding its default value", "labels a defaulted field with the name alone, without the separator", "enables Submit with no typing when every parameter carries a default", "submits the default when a defaulted field is left untouched", "submits the edited value rather than the default when the field is changed", "offers the default again when the same prompt comes back after another", "calls onCancel when Cancel is clicked"]}, {"file": "libs/prompts/src/components/FavoritePromptsPanel/tests/FavoritePromptsPanel.spec.tsx", "assertions": ["FavoritePromptsPanel", "renders the ", "shows the empty-state hint when there are no favorites", "shows the ", "renders a favorite row with its name and a pressed star toggle", "calls onSelect with the item when a row is clicked", "does not call onToggleFavorite synchronously on click", "calls onToggleFavorite with the id once the exit animation finishes", "calls onBrowse when ", "renders the description in the row tooltip when a described row is hovered", "FavoritePromptsPanel \u2014 public class names", "stamps the panel root"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-prompts:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: renders the "My Collection" header.

Sources: libs/prompts/README.md:1-145; libs/prompts/src/index.ts:1-14; libs/prompts/package.json:1-41; libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174; libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69; apps/chat/src/components/PromptSelector/PromptParametersPopupOverlay.tsx:1-71; libs/prompts/src/components/PromptParametersPopup/tests/PromptParametersPopup.spec.tsx:1-205; libs/prompts/src/components/FavoritePromptsPanel/tests/FavoritePromptsPanel.spec.tsx:1-151

## lib-prompts-09 — Constraints that affect integration

Review these constraints before choosing the library. Submission is values: PromptParametersPopup returns a value map, not a sent message. Use shared helpers: extractPromptParams and resolvePromptParams implement token semantics. Syntax matters: Double braces define parameters; ordinary braces remain literal. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/prompts/README.md:1-145; libs/prompts/src/index.ts:1-14; libs/prompts/package.json:1-41; libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174; libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69; AGENTS.md:1-176

## lib-publish-panel-01 — Publish panel

This session explains reuse the publish-to-folder workflow across different entity types. The library is a local private workspace package at libs/publish-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/publish-panel/README.md:1-350; libs/publish-panel/src/index.ts:1-90; libs/publish-panel/package.json:1-44; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193

## lib-publish-panel-02 — When this library is useful

Start with a concrete caller need. Choose a destination: Search and select a publication folder. Explain history: Show earlier publications before replacing or versioning. Share one workflow: Use the same panel for deployments and conversations. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/publish-panel/README.md:1-350; libs/publish-panel/src/index.ts:1-90; libs/publish-panel/package.json:1-44; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193

## lib-publish-panel-03 — Follow the ownership boundary

The library owns Folder/history UI and a generic publish-flow state helper. The host owns Folder loading, write permissions, publish requests and domain-specific resource mapping.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/publish-panel/README.md:1-350; libs/publish-panel/src/index.ts:1-90; libs/publish-panel/package.json:1-44; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193; AGENTS.md:1-176

## lib-publish-panel-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/publish-panel/README.md:1-350; libs/publish-panel/src/index.ts:1-90; libs/publish-panel/package.json:1-44; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193

## lib-publish-panel-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/publish-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Search and select a publication folder. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/publish-panel/README.md:1-350; libs/publish-panel/src/index.ts:1-90; libs/publish-panel/package.json:1-44; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193

## lib-publish-panel-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Prepare the resource: Supply the resource title, labels and publication controls. Collect the request: The panel gathers the publication choices. Publish through the host: Run the host callback and reflect its pending or error state. The complete typed module in examples/publish-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/publish-panel/README.md:1-350; libs/publish-panel/src/index.ts:1-90; libs/publish-panel/package.json:1-44; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193

## lib-publish-panel-07 — Available customization

Customization comes from the current exports and prop declarations. Generic summary: resource and renderSummary avoid requiring a catalog-specific model. State helper: usePublishFlow coordinates selection and submission state. Access-rule controls: Author, rules and rule-source options are explicit inputs. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/publish-panel/README.md:1-350; libs/publish-panel/src/index.ts:1-90; libs/publish-panel/package.json:1-44; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193

## lib-publish-panel-08 — Find the integration and its checks

Actual consumers: libs/chat-hooks/src/conversation/deriveConversationRowActionState/deriveConversationRowActionState.ts; libs/chat-hooks/src/catalog/usePublishFolders/usePublishFolders.ts; libs/chat-hooks/src/catalog/create-publish-api.ts; apps/chat/src/hooks/useConversationPublishHistory/useConversationPublishHistory.ts; libs/chat-hooks/src/catalog/publish.ts; apps/chat/src/hooks/useCatalogPublishing/useCatalogPublishing.ts. Existing test evidence: [{"file": "libs/publish-panel/src/components/PublishFoldersTree/tests/PublishFoldersTree.spec.tsx", "assertions": ["PublishFoldersTree", "converts PublishFolderNode[] to DialFile[] with showFiles disabled, wrapped under the root node", "orders folders by name at every level, regardless of the order given", "passes the selected path joined as a string", "selects a folder when clicked", "deselects (undefined) when clicking the already-selected folder", "filters the tree to matching folders when searchQuery is set", "passes a no-results empty state title when search matches nothing, and omits the root node", "creating a folder from a search that matched nothing", "renders the tree with the inline create row instead of the empty state", "pre-fills the new folder name with the unmatched query", "falls back to the default name when the query is not a valid folder name", "keeps the default name when the query did match a folder", "creates the folder under the selected parent and selects it", "restores the filtered empty state when creation is cancelled"]}, {"file": "libs/publish-panel/src/components/PublishHistoryList/tests/PublishHistoryList.spec.tsx", "assertions": ["PublishHistoryList", "renders the empty-state message when there are no entries", "renders a row for each history entry", "marks an entry that carried shared credentials", "uses the host-supplied shared-credentials label", "leaves an entry without the flag unmarked", "renders a relative date within the last week", "renders an exact date once older than a week", "does not render the destination folder path, since this list is already scoped to it", "uses the versionPrefix override", "renders no dividers between rows, using zebra striping instead (matching the Overview tab grid)"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-publish-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: converts folder nodes into a rooted, folder-only file-manager tree.

Sources: libs/publish-panel/README.md:1-350; libs/publish-panel/src/index.ts:1-90; libs/publish-panel/package.json:1-44; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193; libs/chat-hooks/src/conversation/deriveConversationRowActionState/deriveConversationRowActionState.ts:1-79; libs/publish-panel/src/components/PublishFoldersTree/tests/PublishFoldersTree.spec.tsx:1-503; libs/publish-panel/src/components/PublishHistoryList/tests/PublishHistoryList.spec.tsx:1-97

## lib-publish-panel-09 — Constraints that affect integration

Review these constraints before choosing the library. Permission truth: hasWriteAccess must come from a host authorization decision. Folder mutations: onCreateFolder is asynchronous and can fail. Version semantics: The host decides whether replacement or a new version is appropriate. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/publish-panel/README.md:1-350; libs/publish-panel/src/index.ts:1-90; libs/publish-panel/package.json:1-44; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:196-497; libs/publish-panel/src/components/PublishPanel/PublishPanel.tsx:93-193; AGENTS.md:1-176

## lib-quotations-01 — Quotations

This session explains connect answer annotations to inspectable evidence. The library is a local private workspace package at libs/quotations. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/quotations/README.md:1-245; libs/quotations/src/index.ts:1-72; libs/quotations/package.json:1-41; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30

## lib-quotations-02 — When this library is useful

Start with a concrete caller need. Mark a claim: Show an inline source marker in an answer. Group evidence: Group annotations by source or citation id. Jump to context: Derive PDF or Office highlight locations. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/quotations/README.md:1-245; libs/quotations/src/index.ts:1-72; libs/quotations/package.json:1-41; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30

## lib-quotations-03 — Follow the ownership boundary

The library owns Annotation utilities, citation presentation and optional citation state. The host owns Fetching sources, opening viewers, Markdown pipeline integration and localized labels.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/quotations/README.md:1-245; libs/quotations/src/index.ts:1-72; libs/quotations/package.json:1-41; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30; AGENTS.md:1-176

## lib-quotations-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/quotations/README.md:1-245; libs/quotations/src/index.ts:1-72; libs/quotations/package.json:1-41; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30

## lib-quotations-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/quotations.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Show an inline source marker in an answer. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/quotations/README.md:1-245; libs/quotations/src/index.ts:1-72; libs/quotations/package.json:1-41; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30

## lib-quotations-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Prepare citation data: Resolve the source name, count and display labels. Render a marker: CitationMarker turns that data into a selectable control. Open host evidence: Use onOpen to select a source or display its preview. The complete typed module in examples/quotations.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/quotations/README.md:1-245; libs/quotations/src/index.ts:1-72; libs/quotations/package.json:1-41; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30

## lib-quotations-07 — Available customization

Customization comes from the current exports and prop declarations. Multiple citation forms: Utilities support offset annotations and paired cit tags. Markdown composition: useCitationMarkdownComponents builds citation renderers. Viewer locations: Helpers derive PDF and supported Office highlight coordinates. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/quotations/README.md:1-245; libs/quotations/src/index.ts:1-72; libs/quotations/package.json:1-41; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30

## lib-quotations-08 — Find the integration and its checks

Actual consumers: libs/chat-hooks/src/conversation-sources/useConversationSources/useConversationSources.ts; libs/chat-hooks/src/entry-points/file-manager-canvas.ts; libs/chat-shared/src/components/MarkdownRenderer/MarkdownRenderer.tsx; libs/chat-hooks/src/attachment/useAttachmentAction/useAttachmentAction.ts; libs/chat-shared/src/utils/annotation.ts; libs/chat-hooks/src/files/attachment-canvas.ts. Existing test evidence: [{"file": "libs/quotations/src/hooks/useCitationMarkdownComponents/tests/useCitationMarkdownComponents.spec.tsx", "assertions": ["useCitationMarkdownComponents", "returns content unchanged and renders no marker for uncited content without calling buildLabels", "reports the input content unchanged and empty overrides directly from the hook for uncited content", "injects a sentinel and renders a citation marker for cited content", "renders nothing for a sentinel index with no corresponding group entry, without throwing", "defaults the sentinel injection point to the end of content when the primary annotation has no character-range selector", "keeps the same markdownComponents reference across re-renders with unchanged groups emptiness", "recomputes markdownComponents when groups transitions from empty to non-empty", "recomputes markdownComponents when groups transitions from non-empty to empty", "delegates the preview action to onPreview without internal content-type branching", "delegates the open-in-browser action to onOpenInBrowser directly", "calls buildLabels once per rendered marker with the correct group", "useCitationMarkdownComponents \u2014 cit element rendering", "renders a citation marker for a matched <cit> element when not streaming", "renders an unmatched supported <cit> element as literal text"]}, {"file": "libs/quotations/src/components/CitationMarker/tests/CitationMarker.spec.tsx", "assertions": ["CitationMarker", "uses the single label when annotationCount is 1", "uses the overflow label when annotationCount > 1", "calls onOpen when clicked", "renders without an icon by default", "renders the provided icon before the label", "caps the marker width and ellipsises a long source name", "keeps the descriptive aria-label rather than the raw source name", "CitationMarker \u2014 public class names", "stamps the marker pill", "keeps the class on the overflow variant"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-quotations:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/quotations/README.md:1-245; libs/quotations/src/index.ts:1-72; libs/quotations/package.json:1-41; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30; libs/chat-hooks/src/conversation-sources/useConversationSources/useConversationSources.ts:1-102; libs/quotations/src/hooks/useCitationMarkdownComponents/tests/useCitationMarkdownComponents.spec.tsx:1-545; libs/quotations/src/components/CitationMarker/tests/CitationMarker.spec.tsx:1-107

## lib-quotations-09 — Constraints that affect integration

Review these constraints before choosing the library. Wire the pipeline: Allowed cit tags and renderer overrides must agree. Streaming fragments: Incomplete citation tags need streaming-aware handling. No source download: Callbacks and resolvers connect the marker to actual evidence. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/quotations/README.md:1-245; libs/quotations/src/index.ts:1-72; libs/quotations/package.json:1-41; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:33-62; libs/quotations/src/components/CitationMarker/CitationMarker.tsx:17-30; AGENTS.md:1-176

## lib-scheduled-tasks-01 — Scheduled tasks

This session explains render task lists, forms and run history from host-owned schedules. The library is a local private workspace package at libs/scheduled-tasks. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/scheduled-tasks/README.md:1-215; libs/scheduled-tasks/src/index.ts:1-68; libs/scheduled-tasks/package.json:1-42; libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350; libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110

## lib-scheduled-tasks-02 — When this library is useful

Start with a concrete caller need. Browse automation: Search and sort scheduled task cards. Create or edit: Collect schedule form values and validation errors. Inspect execution: Display a task summary and past run statuses. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/scheduled-tasks/README.md:1-215; libs/scheduled-tasks/src/index.ts:1-68; libs/scheduled-tasks/package.json:1-42; libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350; libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110

## lib-scheduled-tasks-03 — Follow the ownership boundary

The library owns List/form/detail UI and user interactions. The host owns Scheduling APIs, formatted dates, timezone decisions, sorting/filtering and validation.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/scheduled-tasks/README.md:1-215; libs/scheduled-tasks/src/index.ts:1-68; libs/scheduled-tasks/package.json:1-42; libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350; libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110; AGENTS.md:1-176

## lib-scheduled-tasks-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/scheduled-tasks/README.md:1-215; libs/scheduled-tasks/src/index.ts:1-68; libs/scheduled-tasks/package.json:1-42; libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350; libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110

## lib-scheduled-tasks-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/scheduled-tasks.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Search and sort scheduled task cards. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/scheduled-tasks/README.md:1-215; libs/scheduled-tasks/src/index.ts:1-68; libs/scheduled-tasks/package.json:1-42; libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350; libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110

## lib-scheduled-tasks-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Load task records: The host supplies task items, labels and action callbacks. Control the view: Manage the search query and sort key in the host. Handle a task action: Use the host adapter to create or update task data. The complete typed module in examples/scheduled-tasks.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/scheduled-tasks/README.md:1-215; libs/scheduled-tasks/src/index.ts:1-68; libs/scheduled-tasks/package.json:1-42; libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350; libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110

## lib-scheduled-tasks-07 — Available customization

Customization comes from the current exports and prop declarations. List pagination: hasMore, isLoadingMore and onLoadMore support incremental loading. Form and detail exports: ScheduledTaskCreateForm and ScheduledTaskDetailView are distinct surfaces. Run status display: ScheduledTaskRunHistoryList renders host-provided run records. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/scheduled-tasks/README.md:1-215; libs/scheduled-tasks/src/index.ts:1-68; libs/scheduled-tasks/package.json:1-42; libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350; libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110

## lib-scheduled-tasks-08 — Find the integration and its checks

Actual consumers: apps/chat/src/pages/ScheduledTaskDetailPage/ScheduledTaskDetailPage.tsx; apps/chat/src/pages/ScheduledTaskEditPage/ScheduledTaskEditPage.tsx; apps/chat/src/hooks/scheduled-tasks/useScheduledTasks.ts; apps/chat/src/pages/ScheduledTasksPage/ScheduledTasksPage.tsx; apps/chat/src/pages/ScheduledTaskCreatePage/ScheduledTaskCreatePage.tsx; apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx. Existing test evidence: [{"file": "libs/scheduled-tasks/src/components/ScheduledTaskCard/tests/ScheduledTaskCard.spec.tsx", "assertions": ["ScheduledTaskCard", "highlights the matching substring of the title", "renders the schedule pill and location breadcrumb verbatim", "renders no interactive control when onCardClick is omitted", "renders the ", "renders the card with a fixed height", "clamps a long description instead of growing the card", "invokes onCardClick with the item id when the card body is clicked", "invokes onCardClick on Enter/Space keyboard activation", "renders no added interactive semantics when onCardClick is omitted", "renders the ", "renders the schedule pill when isActive is true or omitted", "pins the schedule pill to the bottom of the card regardless of description length", "ScheduledTaskCard \u2014 public class names", "stamps the card whether or not it is clickable"]}, {"file": "libs/scheduled-tasks/src/components/ScheduledTaskDetailsSummary/tests/ScheduledTaskDetailsSummary.spec.tsx", "assertions": ["ScheduledTaskDetailsSummary", "renders the resolved model display name", "renders the raw model id when no display name is resolved but one is supplied as the value", "hides the model field entirely when modelDisplayName is omitted", "renders instructions markdown via the injected renderInstructions callback", "falls back to MDMessageViewer when renderInstructions is not supplied", "renders no edit affordance"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-scheduled-tasks:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/scheduled-tasks/README.md:1-215; libs/scheduled-tasks/src/index.ts:1-68; libs/scheduled-tasks/package.json:1-42; libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350; libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110; apps/chat/src/pages/ScheduledTaskDetailPage/ScheduledTaskDetailPage.tsx:1-413; libs/scheduled-tasks/src/components/ScheduledTaskCard/tests/ScheduledTaskCard.spec.tsx:1-201; libs/scheduled-tasks/src/components/ScheduledTaskDetailsSummary/tests/ScheduledTaskDetailsSummary.spec.tsx:1-89

## lib-scheduled-tasks-09 — Constraints that affect integration

Review these constraints before choosing the library. No task scheduler: Rendering a schedule does not execute work in the background. Formatting stays outside: Pass already-formatted labels and timestamps. Filter intentionally: The controlled search/sort contract requires host updates. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/scheduled-tasks/README.md:1-215; libs/scheduled-tasks/src/index.ts:1-68; libs/scheduled-tasks/package.json:1-42; libs/scheduled-tasks/src/components/ScheduledTasks/ScheduledTasks.tsx:77-350; libs/scheduled-tasks/src/models/scheduled-tasks-props.ts:75-110; AGENTS.md:1-176

## lib-settings-panel-01 — Settings panel

This session explains provide accessible vertical selection for settings pages. The library is a local private workspace package at libs/settings-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/settings-panel/README.md:1-115; libs/settings-panel/src/index.ts:1-9; libs/settings-panel/package.json:1-37; libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170; libs/settings-panel/src/models/settings-panel-props.ts:52-65

## lib-settings-panel-02 — When this library is useful

Start with a concrete caller need. Switch settings: Render a compact navigation list beside host content. Use a keyboard: Move among enabled rows with arrows, Home and End. Keep one selection: The host controls activeId. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/settings-panel/README.md:1-115; libs/settings-panel/src/index.ts:1-9; libs/settings-panel/package.json:1-37; libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170; libs/settings-panel/src/models/settings-panel-props.ts:52-65

## lib-settings-panel-03 — Follow the ownership boundary

The library owns Vertical tab interactions, focus movement and selected styling. The host owns Settings content, active state, item labels and navigation effects.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/settings-panel/README.md:1-115; libs/settings-panel/src/index.ts:1-9; libs/settings-panel/package.json:1-37; libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170; libs/settings-panel/src/models/settings-panel-props.ts:52-65; AGENTS.md:1-176

## lib-settings-panel-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/settings-panel/README.md:1-115; libs/settings-panel/src/index.ts:1-9; libs/settings-panel/package.json:1-37; libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170; libs/settings-panel/src/models/settings-panel-props.ts:52-65

## lib-settings-panel-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/settings-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Render a compact navigation list beside host content. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/settings-panel/README.md:1-115; libs/settings-panel/src/index.ts:1-9; libs/settings-panel/package.json:1-37; libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170; libs/settings-panel/src/models/settings-panel-props.ts:52-65

## lib-settings-panel-10 — See controlled selection in the browser

This is a real browser screenshot of the standalone demo in demo/main.tsx, captured by src/capture-demo.mjs. It renders SettingsPanel, UsageLimitCard and StagesPanel directly from the recorded source snapshot with local stylesheet dependencies. It is an illustrative host, not a screenshot of a deployed DIAL product. All data is synthetic and no backend request is made. Run the Vite command in examples/README.md, then the capture script. Expected behavior: Usage starts selected; selecting Profile updates the controlled active row. The amount and stage remain demo data. The host explicitly supplies dark-theme color overrides. Desktop and phone captures are retained under assets/.

Sources: libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229

## lib-settings-panel-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Choose the active item: Map application state to the panel’s activeId. Handle selection: onSelect returns the chosen item id to the host. Show the chosen view: The host renders the matching settings content beside it. The complete typed module in examples/settings-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/settings-panel/README.md:1-115; libs/settings-panel/src/index.ts:1-9; libs/settings-panel/package.json:1-37; libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170; libs/settings-panel/src/models/settings-panel-props.ts:52-65

## lib-settings-panel-07 — Available customization

Customization comes from the current exports and prop declarations. Disabled rows: Keyboard navigation skips disabled items. Automatic activation: Focus movement also invokes selection. Single item state: One selected row uses a neutral visual treatment. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/settings-panel/README.md:1-115; libs/settings-panel/src/index.ts:1-9; libs/settings-panel/package.json:1-37; libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170; libs/settings-panel/src/models/settings-panel-props.ts:52-65

## lib-settings-panel-08 — Find the integration and its checks

Actual consumers: apps/chat/src/pages/SettingsPage/SettingsPage.tsx; apps/chat/src/hooks/useSettingsTabConfig.tsx. Existing test evidence: [{"file": "libs/settings-panel/src/components/SettingsPanel/tests/SettingsPanel.spec.tsx", "assertions": ["SettingsPanel", "renders one tab per item", "marks the active item as selected", "calls onSelect when an enabled, inactive row is clicked", "does not call onSelect when a disabled row is clicked", "only the active row is in the tab order", "ArrowDown skips a disabled row", "ArrowDown wraps from the last enabled row to the first", "ArrowUp skips a disabled row and wraps at the start", "Home jumps to the first enabled row", "End jumps to the last enabled row", "renders the section label when provided", "renders no section label by default", "applies a custom row focus outline color", "SettingsPanel \u2014 public class names"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-settings-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/settings-panel/README.md:1-115; libs/settings-panel/src/index.ts:1-9; libs/settings-panel/package.json:1-37; libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170; libs/settings-panel/src/models/settings-panel-props.ts:52-65; apps/chat/src/pages/SettingsPage/SettingsPage.tsx:1-35; libs/settings-panel/src/components/SettingsPanel/tests/SettingsPanel.spec.tsx:1-225

## lib-settings-panel-09 — Constraints that affect integration

Review these constraints before choosing the library. Panel content is external: Selection does not create or load a settings page. Keep ids coherent: activeId must correspond to the intended item. No route knowledge: A route change is the host onSelect implementation. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/settings-panel/README.md:1-115; libs/settings-panel/src/index.ts:1-9; libs/settings-panel/package.json:1-37; libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:34-170; libs/settings-panel/src/models/settings-panel-props.ts:52-65; AGENTS.md:1-176

## lib-share-01 — Share

This session explains present a share link and access choices without issuing the link. The library is a local private workspace package at libs/share. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/share/README.md:1-123; libs/share/src/index.ts:1-18; libs/share/package.json:1-41; libs/share/src/components/SharePopover/SharePopover.tsx:326-326; libs/share/src/models/share-popover-props.ts:108-129

## lib-share-02 — When this library is useful

Start with a concrete caller need. Share a resource: Show a link or a scannable QR view. Represent access: Display view/edit access values as a list. Handle pending work: Show host loading and failure states. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/share/README.md:1-123; libs/share/src/index.ts:1-18; libs/share/package.json:1-41; libs/share/src/components/SharePopover/SharePopover.tsx:326-326; libs/share/src/models/share-popover-props.ts:108-129

## lib-share-03 — Follow the ownership boundary

The library owns Link/QR presentation, copy interactions and access controls. The host owns Creating or replacing links, permissions and share-URL resolution.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/share/README.md:1-123; libs/share/src/index.ts:1-18; libs/share/package.json:1-41; libs/share/src/components/SharePopover/SharePopover.tsx:326-326; libs/share/src/models/share-popover-props.ts:108-129; AGENTS.md:1-176

## lib-share-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/share/README.md:1-123; libs/share/src/index.ts:1-18; libs/share/package.json:1-41; libs/share/src/components/SharePopover/SharePopover.tsx:326-326; libs/share/src/models/share-popover-props.ts:108-129

## lib-share-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/share.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Show a link or a scannable QR view. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/share/README.md:1-123; libs/share/src/index.ts:1-18; libs/share/package.json:1-41; libs/share/src/components/SharePopover/SharePopover.tsx:326-326; libs/share/src/models/share-popover-props.ts:108-129

## lib-share-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Obtain a share link: The host calls its sharing operation and supplies the URL. Control link access: Pass allowed access values and permission to edit them. Reflect request state: Pass the updated URL, loading state and any error. The complete typed module in examples/share.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/share/README.md:1-123; libs/share/src/index.ts:1-18; libs/share/package.json:1-41; libs/share/src/components/SharePopover/SharePopover.tsx:326-326; libs/share/src/models/share-popover-props.ts:108-129

## lib-share-07 — Available customization

Customization comes from the current exports and prop declarations. Typed access: ShareLinkAccess represents view and edit levels. Separate QR component: QrCode can be used outside the popover. Explicit errors: url may be undefined while loading; error is supplied separately. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/share/README.md:1-123; libs/share/src/index.ts:1-18; libs/share/package.json:1-41; libs/share/src/components/SharePopover/SharePopover.tsx:326-326; libs/share/src/models/share-popover-props.ts:108-129

## lib-share-08 — Find the integration and its checks

Actual consumers: apps/chat-api/src/share/dto/create-share-link.dto.ts; libs/chat-hooks/src/useShareLink/useShareLink.ts; apps/chat/src/components/SharePopoverContainer/SharePopoverContainer.tsx; libs/attachment-canvas/src/components/VisualizerCanvasRenderer/VisualizerCanvasRenderer.tsx; libs/attachment-canvas/src/utils/vite-external-matcher.ts; apps/chat/src/components/ShareConversationPopoverContainer/ShareConversationPopoverContainer.tsx. Existing test evidence: [{"file": "libs/share/src/components/SharePopover/tests/SharePopover.spec.tsx", "assertions": ["SharePopover", "renders the link view by default with Can view access", "shows the view-access visibility note by default", "shows the edit-access visibility note in both the link and QR views", "calls onAccessChange with Edit when an access option is selected", "shows Can edit as the selected trigger label and checkmark when access starts as Edit", "moves focus between access menu options with Arrow keys", "traps Tab within the open access menu", "shows the interactive access dropdown when canEditAccess is true", "hides the access dropdown and shows a static Can view label when canEditAccess is false", "never shows the edit-access visibility note when canEditAccess is false", "shows the nested-items note only when supplied via labels", "shows a transient Copied confirmation after clicking Copy", "announces Copied via an aria-live region after clicking Copy", "swaps to the QR view and back, moving focus each time"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-share:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/share/README.md:1-123; libs/share/src/index.ts:1-18; libs/share/package.json:1-41; libs/share/src/components/SharePopover/SharePopover.tsx:326-326; libs/share/src/models/share-popover-props.ts:108-129; apps/chat-api/src/share/dto/create-share-link.dto.ts:1-43; libs/share/src/components/SharePopover/tests/SharePopover.spec.tsx:1-460

## lib-share-09 — Constraints that affect integration

Review these constraints before choosing the library. Access is not cosmetic: Real access changes require the host to request the appropriate link. No permission enforcement: canEditAccess controls UI, not backend authorization. Named root export: Import SharePopover by name from the package entry. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/share/README.md:1-123; libs/share/src/index.ts:1-18; libs/share/package.json:1-41; libs/share/src/components/SharePopover/SharePopover.tsx:326-326; libs/share/src/models/share-popover-props.ts:108-129; AGENTS.md:1-176

## lib-sidebar-01 — Sidebar

This session explains give feature panels a common resizable shell. The library is a local private workspace package at libs/sidebar. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/sidebar/README.md:1-173; libs/sidebar/src/index.ts:1-14; libs/sidebar/package.json:1-39; libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266; libs/sidebar/src/models/panel-props.ts:51-90

## lib-sidebar-02 — When this library is useful

Start with a concrete caller need. Add a panel: Compose a header, actions and scrollable content. Resize a workspace: Use a bounded width with a resize callback. Handle empty data: Use PanelEmpty or PanelNoResults consistently. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/sidebar/README.md:1-173; libs/sidebar/src/index.ts:1-14; libs/sidebar/package.json:1-39; libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266; libs/sidebar/src/models/panel-props.ts:51-90

## lib-sidebar-03 — Follow the ownership boundary

The library owns Panel structure, resize interaction, visibility and empty-state primitives. The host owns Content, search, durable width storage and feature actions.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/sidebar/README.md:1-173; libs/sidebar/src/index.ts:1-14; libs/sidebar/package.json:1-39; libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266; libs/sidebar/src/models/panel-props.ts:51-90; AGENTS.md:1-176

## lib-sidebar-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/sidebar/README.md:1-173; libs/sidebar/src/index.ts:1-14; libs/sidebar/package.json:1-39; libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266; libs/sidebar/src/models/panel-props.ts:51-90

## lib-sidebar-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/sidebar.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Compose a header, actions and scrollable content. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/sidebar/README.md:1-173; libs/sidebar/src/index.ts:1-14; libs/sidebar/package.json:1-39; libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266; libs/sidebar/src/models/panel-props.ts:51-90

## lib-sidebar-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Open host content: Supply isOpen, title and the panel’s child view. Resize the panel: Enable resizing and handle onResizeStop. Retain the width: Store the final width in the host if it must survive remounts. The complete typed module in examples/sidebar.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/sidebar/README.md:1-173; libs/sidebar/src/index.ts:1-14; libs/sidebar/package.json:1-39; libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266; libs/sidebar/src/models/panel-props.ts:51-90

## lib-sidebar-07 — Available customization

Customization comes from the current exports and prop declarations. Logical placement: SidebarOrientation selects the desired panel side. Header slots: leftActions and rightActions are public API slot names. Width bounds: defaultWidth, minWidth and maxWidth configure resizing. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/sidebar/README.md:1-173; libs/sidebar/src/index.ts:1-14; libs/sidebar/package.json:1-39; libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266; libs/sidebar/src/models/panel-props.ts:51-90

## lib-sidebar-08 — Find the integration and its checks

Actual consumers: libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx; libs/source-panel/src/constants/public-class-names.ts; libs/conversation-panel/src/components/ConversationPanel/ConversationPanel.tsx; libs/attachment-canvas/src/components/AttachmentCanvas/AttachmentCanvas.tsx; libs/attachment-canvas/src/models/attachment-canvas.ts; libs/attachment-canvas/src/constants/public-class-names.ts. Existing test evidence: [{"file": "libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.spec.tsx", "assertions": ["SidebarPanel", "renders children in the body", "has role=complementary and aria-label", "renders leftActions in the left header group", "renders rightActions in the right header group", "side=right: close button is in the right group (last button)", "side=right: renders without a divider", "side=left: close button is rendered after right actions (last button)", "side=left, open: applies the border-s divider facing the navigation rail", "side=left, closed: renders without a divider", "close button calls onClose", "colors prop emits CSS custom properties", "no inline style when colors and typography are omitted", "w-full className overrides inline width", "applies inline width when w-full className is absent"]}, {"file": "libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.classes.spec.tsx", "assertions": ["SidebarPanel \u2014 public class names", "marks the aside element found by its role", "marks the header bar that carries the title", "keeps the aside addressable when the host localises its label"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-sidebar:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/sidebar/README.md:1-173; libs/sidebar/src/index.ts:1-14; libs/sidebar/package.json:1-39; libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266; libs/sidebar/src/models/panel-props.ts:51-90; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:1-203; libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.spec.tsx:1-312; libs/sidebar/src/components/SidebarPanel/tests/SidebarPanel.classes.spec.tsx:1-87

## lib-sidebar-09 — Constraints that affect integration

Review these constraints before choosing the library. No built-in search: Compose search in children or header actions. Persistence is external: onResizeStop reports width; the host decides where to save it. Contextual visibility: Keep the parent layout and isOpen state synchronized. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/sidebar/README.md:1-173; libs/sidebar/src/index.ts:1-14; libs/sidebar/package.json:1-39; libs/sidebar/src/components/SidebarPanel/SidebarPanel.tsx:25-266; libs/sidebar/src/models/panel-props.ts:51-90; AGENTS.md:1-176

## lib-skill-editor-01 — Skill editor

This session explains edit a skill and its supporting file tree through host callbacks. The library is a local private workspace package at libs/skill-editor. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/skill-editor/README.md:1-176; libs/skill-editor/src/index.ts:1-23; libs/skill-editor/package.json:1-43; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570; libs/skill-editor/src/models/skill-editor-props.ts:236-315

## lib-skill-editor-02 — When this library is useful

Start with a concrete caller need. Author instructions: Edit skill metadata and Markdown instructions. Attach supporting files: Select, expand and manage a file tree. Resolve edits safely: Show validation and conflict state from the host. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/skill-editor/README.md:1-176; libs/skill-editor/src/index.ts:1-23; libs/skill-editor/package.json:1-43; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570; libs/skill-editor/src/models/skill-editor-props.ts:236-315

## lib-skill-editor-03 — Follow the ownership boundary

The library owns Form editing, file-tree interaction and the protected root SKILL.md node. The host owns Path validation, upload/commit operations, ZIP/YAML serialization and persistence.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/skill-editor/README.md:1-176; libs/skill-editor/src/index.ts:1-23; libs/skill-editor/package.json:1-43; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570; libs/skill-editor/src/models/skill-editor-props.ts:236-315; AGENTS.md:1-176

## lib-skill-editor-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/skill-editor/README.md:1-176; libs/skill-editor/src/index.ts:1-23; libs/skill-editor/package.json:1-43; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570; libs/skill-editor/src/models/skill-editor-props.ts:236-315

## lib-skill-editor-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/skill-editor.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Edit skill metadata and Markdown instructions. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/skill-editor/README.md:1-176; libs/skill-editor/src/index.ts:1-23; libs/skill-editor/package.json:1-43; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570; libs/skill-editor/src/models/skill-editor-props.ts:236-315

## lib-skill-editor-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Load skill inputs: Prepare metadata, files and the required file actions. Collect edits: The editor returns changes through host callbacks. Save the skill: The host performs persistence and handles navigation. The complete typed module in examples/skill-editor.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/skill-editor/README.md:1-176; libs/skill-editor/src/index.ts:1-23; libs/skill-editor/package.json:1-43; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570; libs/skill-editor/src/models/skill-editor-props.ts:236-315

## lib-skill-editor-07 — Available customization

Customization comes from the current exports and prop declarations. File action interface: Validation and upload callbacks keep storage rules outside the view. Conflict UI: conflict and onReloadLatest support a host conflict workflow. Selection control: selectedPath and expandedPaths can be controlled externally. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/skill-editor/README.md:1-176; libs/skill-editor/src/index.ts:1-23; libs/skill-editor/package.json:1-43; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570; libs/skill-editor/src/models/skill-editor-props.ts:236-315

## lib-skill-editor-08 — Find the integration and its checks

Actual consumers: libs/chat-hooks/src/skill/skill.ts; apps/chat/src/pages/SkillEditor/SkillEditor.tsx; libs/chat-hooks/src/skill/useSkillEditorSubmit.ts; libs/chat-hooks/src/skill/useSkillEditorLoad.ts; libs/chat-hooks/src/skill/useSkillFileActions.ts; libs/chat-hooks/src/skill/skill-file-batch-validation.ts. Existing test evidence: [{"file": "libs/skill-editor/src/hooks/tests/useSkillFileDropZone.spec.ts", "assertions": ["useSkillFileDropZone", "activates on drag-enter", "does not flicker to inactive on a nested drag-leave while still over the zone", "deactivates once the net enter count returns to zero", "calls preventDefault on dragover for a file drag", "ignores a non-file drag", "calls onFilesDropped with the dropped files and resets drag state"]}, {"file": "libs/skill-editor/src/components/SkillFileDropOverlay/tests/SkillFileDropOverlay.spec.tsx", "assertions": ["SkillFileDropOverlay", "renders nothing when not visible", "shows the default title and subtitle when visible", "renders host-supplied labels"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-skill-editor:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/skill-editor/README.md:1-176; libs/skill-editor/src/index.ts:1-23; libs/skill-editor/package.json:1-43; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570; libs/skill-editor/src/models/skill-editor-props.ts:236-315; libs/chat-hooks/src/skill/skill.ts:1-256; libs/skill-editor/src/hooks/tests/useSkillFileDropZone.spec.ts:1-84; libs/skill-editor/src/components/SkillFileDropOverlay/tests/SkillFileDropOverlay.spec.tsx:1-39

## lib-skill-editor-09 — Constraints that affect integration

Review these constraints before choosing the library. Protected entry file: The root SKILL.md cannot be removed by the tree UI. No archive writer: The host assembles the persisted skill representation. Async ownership: Supply meaningful loading, submitting and error states. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/skill-editor/README.md:1-176; libs/skill-editor/src/index.ts:1-23; libs/skill-editor/package.json:1-43; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570; libs/skill-editor/src/models/skill-editor-props.ts:236-315; AGENTS.md:1-176

## lib-skills-01 — Skills

This session explains select a reusable skill without coupling the picker to sending. The library is a local private workspace package at libs/skills. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/skills/README.md:1-378; libs/skills/src/index.ts:1-30; libs/skills/package.json:1-42; libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294; libs/skills/src/models/favorite-skills-panel-props.ts:34-62

## lib-skills-02 — When this library is useful

Start with a concrete caller need. Choose a favorite: Select a host-resolved favorite skill. Inspect a skill: Open a host-backed detail panel. Attach context: Display a selected skill chip next to the composer. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/skills/README.md:1-378; libs/skills/src/index.ts:1-30; libs/skills/package.json:1-42; libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294; libs/skills/src/models/favorite-skills-panel-props.ts:34-62

## lib-skills-03 — Follow the ownership boundary

The library owns Favorite list, chip, details composition and selection-overlay state. The host owns Skill listing, favorites persistence, capability flag and send-time semantics.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/skills/README.md:1-378; libs/skills/src/index.ts:1-30; libs/skills/package.json:1-42; libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294; libs/skills/src/models/favorite-skills-panel-props.ts:34-62; AGENTS.md:1-176

## lib-skills-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/skills/README.md:1-378; libs/skills/src/index.ts:1-30; libs/skills/package.json:1-42; libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294; libs/skills/src/models/favorite-skills-panel-props.ts:34-62

## lib-skills-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/skills.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Select a host-resolved favorite skill. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/skills/README.md:1-378; libs/skills/src/index.ts:1-30; libs/skills/package.json:1-42; libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294; libs/skills/src/models/favorite-skills-panel-props.ts:34-62

## lib-skills-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Load favorites: Supply favorite skill records and localized labels. Handle selection: Use the selection callback to choose a skill in the host. Connect discovery: Browse and detail callbacks open host-owned surfaces. The complete typed module in examples/skills.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/skills/README.md:1-378; libs/skills/src/index.ts:1-30; libs/skills/package.json:1-42; libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294; libs/skills/src/models/favorite-skills-panel-props.ts:34-62

## lib-skills-07 — Available customization

Customization comes from the current exports and prop declarations. Overlay state hook: useSkillSelectorOverlay coordinates favorites, browse and details. Capability input: A plain support flag controls skill entry points. Composable detail view: SkillDetailsSidePanel uses the catalog DetailsPanel contract. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/skills/README.md:1-378; libs/skills/src/index.ts:1-30; libs/skills/package.json:1-42; libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294; libs/skills/src/models/favorite-skills-panel-props.ts:34-62

## lib-skills-08 — Find the integration and its checks

Actual consumers: apps/chat/src/components/SkillSelector/useSkillSelectorOverlay.tsx; apps/chat/src/components/SkillSelector/SkillDetailsPanelContainer.tsx. Existing test evidence: [{"file": "libs/skills/src/components/ChatSkill/tests/ChatSkill.classes.spec.tsx", "assertions": ["skills \u2014 public class names", "stamps the composer chip", "keeps the chip class in the unsupported state", "stamps the favorites panel root"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-skills:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/skills/README.md:1-378; libs/skills/src/index.ts:1-30; libs/skills/package.json:1-42; libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294; libs/skills/src/models/favorite-skills-panel-props.ts:34-62; apps/chat/src/components/SkillSelector/useSkillSelectorOverlay.tsx:1-120; libs/skills/src/components/ChatSkill/tests/ChatSkill.classes.spec.tsx:1-72

## lib-skills-09 — Constraints that affect integration

Review these constraints before choosing the library. Unsupported deployment: A selected chip can remain visible in its error state. No automatic attachment: The host decides how a skill enters the request. Keep identifiers intact: The favorite item id is the resource identifier supplied by the host. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/skills/README.md:1-378; libs/skills/src/index.ts:1-30; libs/skills/package.json:1-42; libs/skills/src/components/FavoriteSkillsPanel/FavoriteSkillsPanel.tsx:37-294; libs/skills/src/models/favorite-skills-panel-props.ts:34-62; AGENTS.md:1-176

## lib-source-panel-01 — Source panel

This session explains put uploaded files, generated files and citations in one evidence panel. The library is a local private workspace package at libs/source-panel. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/source-panel/README.md:1-142; libs/source-panel/src/index.ts:1-10; libs/source-panel/package.json:1-41; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203; libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107

## lib-source-panel-02 — When this library is useful

Start with a concrete caller need. Find evidence: Inspect source material beside the conversation. Search by name: Narrow attachments and source labels. Open a reference: Delegate preview or download to the host. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/source-panel/README.md:1-142; libs/source-panel/src/index.ts:1-10; libs/source-panel/package.json:1-41; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203; libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107

## lib-source-panel-03 — Follow the ownership boundary

The library owns Evidence sections, filtering and attachment/source interactions. The host owns Source derivation, authenticated downloads and canvas loading.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/source-panel/README.md:1-142; libs/source-panel/src/index.ts:1-10; libs/source-panel/package.json:1-41; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203; libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107; AGENTS.md:1-176

## lib-source-panel-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/source-panel/README.md:1-142; libs/source-panel/src/index.ts:1-10; libs/source-panel/package.json:1-41; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203; libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107

## lib-source-panel-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/source-panel.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Inspect source material beside the conversation. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/source-panel/README.md:1-142; libs/source-panel/src/index.ts:1-10; libs/source-panel/package.json:1-41; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203; libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107

## lib-source-panel-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Group the evidence: Supply uploaded, generated and source records. Open the panel: The host controls open state and mobile presentation. Handle a source click: Resolve the selected item and open its host-owned preview. The complete typed module in examples/source-panel.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/source-panel/README.md:1-142; libs/source-panel/src/index.ts:1-10; libs/source-panel/package.json:1-41; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203; libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107

## lib-source-panel-07 — Available customization

Customization comes from the current exports and prop declarations. Separate collections: uploaded, generated and sources retain their distinct roles. Panel customization: Width bounds, labels and additionalSections are explicit inputs. Matched text: Search results use the shared highlighting convention. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/source-panel/README.md:1-142; libs/source-panel/src/index.ts:1-10; libs/source-panel/package.json:1-41; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203; libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107

## lib-source-panel-08 — Find the integration and its checks

Actual consumers: apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx; libs/chat-hooks/src/conversation-sources/useConversationSources/useConversationSources.ts; libs/sidebar/src/constants/public-class-names.ts. Existing test evidence: [{"file": "libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.classes.spec.tsx", "assertions": ["ConversationSourcesPanel \u2014 public class names", "stamps the panel on the desktop layout", "keeps the class beside the mobile full-width utility", "stamps the panel while it is closed"]}, {"file": "libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.spec.tsx", "assertions": ["ConversationSourcesPanel", "renders uploaded attachments", "renders generated attachments", "close button calls onClose", "renders empty state when no data", "renders uploaded and generated sections in order", "renders sources section", "renders the download-all button disabled when onDownloadAll is omitted", "renders the download-all button enabled and wired to onDownloadAll", "ConversationSourcesPanel \u2014 search", "typing a partial name filters uploaded and generated sections", "shows no-results state when query matches nothing", "clearing the query restores all attachments", "filters sources by title, url, and quote", "ConversationSourcesPanel \u2014 title and additionalSections (optional, additive)"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-source-panel:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/source-panel/README.md:1-142; libs/source-panel/src/index.ts:1-10; libs/source-panel/package.json:1-41; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203; libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107; apps/chat/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:1-354; libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.classes.spec.tsx:1-116; libs/source-panel/src/components/ConversationSourcesPanel/tests/ConversationSourcesPanel.spec.tsx:1-383

## lib-source-panel-09 — Constraints that affect integration

Review these constraints before choosing the library. No implicit fetching: Opening a row needs a host callback. Required labels: The panel contract requires the complete labels object. Boundary drift: The README peer list differs from current package composition. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/source-panel/README.md:1-142; libs/source-panel/src/index.ts:1-10; libs/source-panel/package.json:1-41; libs/source-panel/src/components/ConversationSourcesPanel/ConversationSourcesPanel.tsx:203-203; libs/source-panel/src/models/conversation-sources-panel-props.ts:64-107; AGENTS.md:1-176

## lib-starter-buttons-01 — Starter buttons

This session explains offer prompt starters that fit the available space. The library is a local private workspace package at libs/starter-buttons. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/starter-buttons/README.md:1-150; libs/starter-buttons/src/index.ts:1-7; libs/starter-buttons/package.json:1-39; libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193; libs/starter-buttons/src/models/starter-props.ts:20-38

## lib-starter-buttons-02 — When this library is useful

Start with a concrete caller need. Start a conversation: Expose useful first actions before the user types. Handle narrow screens: Move excess choices to the overflow menu. Keep behavior explicit: The host decides what a selected starter does. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/starter-buttons/README.md:1-150; libs/starter-buttons/src/index.ts:1-7; libs/starter-buttons/package.json:1-39; libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193; libs/starter-buttons/src/models/starter-props.ts:20-38

## lib-starter-buttons-03 — Follow the ownership boundary

The library owns Starter layout, available-space measurement and overflow controls. The host owns Starter data, mobile mode when supplied and send/populate behavior.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/starter-buttons/README.md:1-150; libs/starter-buttons/src/index.ts:1-7; libs/starter-buttons/package.json:1-39; libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193; libs/starter-buttons/src/models/starter-props.ts:20-38; AGENTS.md:1-176

## lib-starter-buttons-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/starter-buttons/README.md:1-150; libs/starter-buttons/src/index.ts:1-7; libs/starter-buttons/package.json:1-39; libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193; libs/starter-buttons/src/models/starter-props.ts:20-38

## lib-starter-buttons-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/starter-buttons.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Expose useful first actions before the user types. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/starter-buttons/README.md:1-150; libs/starter-buttons/src/index.ts:1-7; libs/starter-buttons/package.json:1-39; libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193; libs/starter-buttons/src/models/starter-props.ts:20-38

## lib-starter-buttons-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Choose starter options: The host supplies the available starter records. Render choices: StarterButtons handles the list and overflow presentation. Apply the selection: Use onSelect to fill or send content through the host. The complete typed module in examples/starter-buttons.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/starter-buttons/README.md:1-150; libs/starter-buttons/src/index.ts:1-7; libs/starter-buttons/package.json:1-39; libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193; libs/starter-buttons/src/models/starter-props.ts:20-38

## lib-starter-buttons-07 — Available customization

Customization comes from the current exports and prop declarations. Responsive overflow: Measured space determines which options remain visible. Collapse policy: isCollapsible changes the overflow behavior. Accessible names: labels names the list and the overflow action. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/starter-buttons/README.md:1-150; libs/starter-buttons/src/index.ts:1-7; libs/starter-buttons/package.json:1-39; libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193; libs/starter-buttons/src/models/starter-props.ts:20-38

## lib-starter-buttons-08 — Find the integration and its checks

Actual consumers: apps/chat/src/components/StarterButtons/StarterButtons.tsx. Existing test evidence: [{"file": "libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.spec.tsx", "assertions": ["StarterButtons", "collapses the starters that do not fit into an overflow menu by default", "renders every starter and no overflow menu when collapsing is off"]}, {"file": "libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.classes.spec.tsx", "assertions": ["StarterButtons \u2014 public class names", "stamps the list and the wrapper around it", "keeps both classes in the non-collapsible layout"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-starter-buttons:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources: libs/starter-buttons/README.md:1-150; libs/starter-buttons/src/index.ts:1-7; libs/starter-buttons/package.json:1-39; libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193; libs/starter-buttons/src/models/starter-props.ts:20-38; apps/chat/src/components/StarterButtons/StarterButtons.tsx:1-34; libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.spec.tsx:1-48; libs/starter-buttons/src/components/StarterButtons/tests/StarterButtons.classes.spec.tsx:1-64

## lib-starter-buttons-09 — Constraints that affect integration

Review these constraints before choosing the library. Use the actual shape: StarterOption includes const and dial:widgetOptions. No completion side effect: Selecting emits a value; the host controls submission. Layout needs space: Render inside the actual constrained input area. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/starter-buttons/README.md:1-150; libs/starter-buttons/src/index.ts:1-7; libs/starter-buttons/package.json:1-39; libs/starter-buttons/src/components/StarterButtons/StarterButtons.tsx:26-193; libs/starter-buttons/src/models/starter-props.ts:20-38; AGENTS.md:1-176

## lib-toolset-editor-01 — Toolset editor

This session explains coordinate mcp toolset editing through an explicit host adapter. The library is a local private workspace package at libs/toolset-editor. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150

## lib-toolset-editor-02 — When this library is useful

Start with a concrete caller need. Create a toolset: Edit metadata, endpoint, transport and authentication settings. Persist a draft: Reuse the identifier returned by the first successful save. Authorize access: Delegate login and OAuth to host behavior. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150

## lib-toolset-editor-03 — Follow the ownership boundary

The library owns Form state, dirty/errors state and save orchestration around injected operations. The host owns HTTP persistence, OAuth execution, credentials APIs, routes and file-manager integration.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150; AGENTS.md:1-176

## lib-toolset-editor-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150

## lib-toolset-editor-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/toolset-editor.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Edit metadata, endpoint, transport and authentication settings. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150

## lib-toolset-editor-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Prepare the adapter: Supply the required persistence, file and auth callbacks. Collect toolset values: Let the editor coordinate metadata and setup controls. Run host operations: Keep credential flows, endpoint calls and routing in the host. The complete typed module in examples/toolset-editor.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150

## lib-toolset-editor-10 — Validate a candidate endpoint

This pure validation example is included in the full module. A valid URL does not establish toolset availability or successful authentication. The complete ToolsetEditor still requires every prop in the exported contract.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150

## lib-toolset-editor-07 — Available customization

Customization comes from the current exports and prop declarations. Typed integration: ToolsetEditorProps makes persistence, auth and file dependencies explicit. Shared metadata: GeneralForm reuses builder-form fields and validation. MCP URL resolver: buildMcpUrl receives the current draft identifier. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150

## lib-toolset-editor-08 — Find the integration and its checks

Actual consumers: apps/chat/src/pages/ToolsetEditor/ToolsetEditor.tsx; apps/chat/src/pages/ToolsetEditor/CustomAppEditorView.tsx; apps/chat/src/hooks/toolsets/useToolsetEditorOAuthLogin.ts; apps/chat/src/models/custom-apps.ts; apps/chat/src/utils/toolsets.ts. Existing test evidence: [{"file": "libs/toolset-editor/src/components/ConnectMcpUrlContent/tests/ConnectMcpUrlContent.spec.tsx", "assertions": ["ConnectMcpUrlContent", "renders the default title, description, and copy button", "renders host-supplied labels instead of the defaults", "copies the endpoint URL to the clipboard", "announces the copy through the polite live region"]}, {"file": "libs/toolset-editor/src/components/AuthSection/tests/AuthSection.spec.tsx", "assertions": [",", "AuthSection", "type selection", "calls onAuthChange with ApiKey type when the ApiKey option is clicked", "calls onAuthChange with OAuth type when the OAuth option is clicked", "disables every non-selected auth-type option while the toolset is logged in, leaving the selected one enabled", "marks the active auth type as checked for assistive technology", "defaults a fresh OAuth selection to WithConfig so config fields are visible immediately", "defaults an OAuth selection to WithLogin when a client is already configured", "API Key conditional fields", "renders key header and API key inputs when ApiKey + WithLogin is active", "masks the API key value and exposes a reveal toggle", "renders only the key header input when ApiKey + WithoutLogin is active", "renders WithLogin and WithoutLogin radio buttons for ApiKey", "OAuth conditional fields"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-toolset-editor:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: calls onAuthChange with ApiKey type when the ApiKey option is clicked.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150; apps/chat/src/pages/ToolsetEditor/ToolsetEditor.tsx:1-463; libs/toolset-editor/src/components/ConnectMcpUrlContent/tests/ConnectMcpUrlContent.spec.tsx:1-63; libs/toolset-editor/src/components/AuthSection/tests/AuthSection.spec.tsx:1-808

## lib-toolset-editor-09 — Constraints that affect integration

Review these constraints before choosing the library. No minimal fake backend: A working editor needs the required host callbacks and file component. Form identity: A new initialForm object reseeds the editing session. Boundary discrepancy: Current code imports chat-hooks symbols; document this wider dependency. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/toolset-editor/README.md:1-383; libs/toolset-editor/src/index.ts:1-47; libs/toolset-editor/package.json:1-41; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx:58-425; libs/toolset-editor/src/models/toolset-editor-props.ts:74-150; AGENTS.md:1-176

## lib-usage-dashboard-01 — Usage dashboard

This session explains explain cost and model limits using normalized display data. The library is a local private workspace package at libs/usage-dashboard. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources: libs/usage-dashboard/README.md:1-425; libs/usage-dashboard/src/index.ts:1-43; libs/usage-dashboard/package.json:1-42; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191; libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152

## lib-usage-dashboard-02 — When this library is useful

Start with a concrete caller need. Inspect a budget: Display used, remaining and total amounts. Compare periods: Show the current UTC day, week and month. Find constraints: Compare model-token and overall cost limit statuses. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources: libs/usage-dashboard/README.md:1-425; libs/usage-dashboard/src/index.ts:1-43; libs/usage-dashboard/package.json:1-42; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191; libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152

## lib-usage-dashboard-03 — Follow the ownership boundary

The library owns Usage cards/tables plus exported mapping utilities. The host owns Fetching usage, choosing locale/timezone formatting and passing resolved display values.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources: libs/usage-dashboard/README.md:1-425; libs/usage-dashboard/src/index.ts:1-43; libs/usage-dashboard/package.json:1-42; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191; libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152; AGENTS.md:1-176

## lib-usage-dashboard-04 — The public contract to start with

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources: libs/usage-dashboard/README.md:1-425; libs/usage-dashboard/src/index.ts:1-43; libs/usage-dashboard/package.json:1-42; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191; libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152

## lib-usage-dashboard-05 — A minimal workspace integration

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/usage-dashboard.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Display used, remaining and total amounts. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources: libs/usage-dashboard/README.md:1-425; libs/usage-dashboard/src/index.ts:1-43; libs/usage-dashboard/package.json:1-42; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191; libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152

## lib-usage-dashboard-10 — See preformatted usage data in context

This is a real browser screenshot of the standalone demo in demo/main.tsx, captured by src/capture-demo.mjs. It renders SettingsPanel, UsageLimitCard and StagesPanel directly from the recorded source snapshot with local stylesheet dependencies. It is an illustrative host, not a screenshot of a deployed DIAL product. All data is synthetic and no backend request is made. Run the Vite command in examples/README.md, then the capture script. Expected behavior: Usage starts selected; selecting Profile updates the controlled active row. The amount and stage remain demo data. The host explicitly supplies dark-theme color overrides. Desktop and phone captures are retained under assets/.

Sources: libs/settings-panel/src/components/SettingsPanel/SettingsPanel.tsx:1-170; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:1-191; libs/conversation-stages/src/components/StagesPanel/StagesPanel.tsx:1-229

## lib-usage-dashboard-06 — Wire a realistic host workflow

Follow this concrete integration sequence. Prepare usage data: The host maps raw usage to the card’s normalized data. Format the values: Supply amount labels, percentage, status and optional reset text. Render the summary: The card presents the values and accessible progress text. The complete typed module in examples/usage-dashboard.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources: libs/usage-dashboard/README.md:1-425; libs/usage-dashboard/src/index.ts:1-43; libs/usage-dashboard/package.json:1-42; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191; libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152

## lib-usage-dashboard-07 — Available customization

Customization comes from the current exports and prop declarations. Semantic states: UsageLimitStatus distinguishes normal, warning and reached states. Accessible progress: Supply preformatted progressAriaLabel and reset text. Mapping exports: mapUsageDataToDashboard and model-limit mappers are public. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources: libs/usage-dashboard/README.md:1-425; libs/usage-dashboard/src/index.ts:1-43; libs/usage-dashboard/package.json:1-42; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191; libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152

## lib-usage-dashboard-08 — Find the integration and its checks

Actual consumers: apps/chat/src/pages/SettingsPage/UsageTab/UsageTab.tsx; apps/chat/src/utils/usage-reset-time.ts. Existing test evidence: [{"file": "libs/usage-dashboard/src/components/UsageLimitCard/tests/UsageLimitCard.spec.tsx", "assertions": ["UsageLimitCard", "renders the title and the prominent used amount with its ", "renders the ", "renders the running-low badge and warning accent at 90% used", "renders the limit-reached badge and error accent at 100% used", "renders the remaining-amount and used-percent captions below the progress bar", "shows only the used amount, with no progress bar, ratio, or badge, when unlimited", "clamps the visual progress fill and the visible percent label at 100%, while the accessible value text keeps the real percentage", "names the progress bar after the card title", "renders long localized labels without breaking the layout query", "exposes the card as an accessible group named with the title and period description", "keeps the same accessible name and value text under an RTL ancestor", "reset line", "renders the reset label in a <time> carrying the original UTC instant", "carries the spoken form on a visually-hidden sibling, not on the <time>"]}, {"file": "libs/usage-dashboard/src/components/ModelLimitsSection/tests/ModelLimitsSection.spec.tsx", "assertions": ["ModelLimitsSection", "renders the row count separately in the section heading", "renders the empty state while preserving the section shell", "renders exactly the fixed comparison headers in order", "renders one semantic row with Item, three period cells, and Status", "vertically centers desktop row content without changing horizontal alignment", "renders token progress followed by attributed Cost in every period cell", "renders unavailable Cost as a value without a visible Cost label", "renders unlimited and unavailable token states without progress bars", "clamps progress visually while retaining the real accessible value", "renders rows in supplied order with avatar fallback and accessible names", "keeps long identity content constrained inside the Item cell", "uses one responsive semantic subtree under an RTL ancestor", "renders accessible overall Cost indicators for affected period headers", "period header reset line"]}]. Reproduce project checks from the repository root with npm exec nx run usage-dashboard:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: renders the title, used amount and "used of" caption.

Sources: libs/usage-dashboard/README.md:1-425; libs/usage-dashboard/src/index.ts:1-43; libs/usage-dashboard/package.json:1-42; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191; libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152; apps/chat/src/pages/SettingsPage/UsageTab/UsageTab.tsx:1-264; libs/usage-dashboard/src/components/UsageLimitCard/tests/UsageLimitCard.spec.tsx:1-267; libs/usage-dashboard/src/components/ModelLimitsSection/tests/ModelLimitsSection.spec.tsx:1-517

## lib-usage-dashboard-09 — Constraints that affect integration

Review these constraints before choosing the library. Calendar periods: Today/week/month are calendar windows, not rolling durations. Separate component and helper: Cards consume display data; exported helpers do perform mapping. Isolation discrepancy: Mapping source imports generated API DTOs outside the documented exception. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources: libs/usage-dashboard/README.md:1-425; libs/usage-dashboard/src/index.ts:1-43; libs/usage-dashboard/package.json:1-42; libs/usage-dashboard/src/components/UsageLimitCard/UsageLimitCard.tsx:26-191; libs/usage-dashboard/src/models/usage-limit-card-props.ts:145-152; AGENTS.md:1-176
