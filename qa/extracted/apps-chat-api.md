<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Chat backend
The NestJS edge that authenticates users, persists conversations and adapts DIAL Core.

Backend contracts
Generation lifecycle
Port 5000
apps/chat-api · @epam/chat-api
01
Chat backend
apps-chat-api-01

### Notes:
Slide ID: apps-chat-api-01

chat-api is the backend-for-frontend for the React application. It also serves production frontend assets and coordinates several external systems. Distinguish its generated browser client from the server-side DIAL TypeScript SDK.

Sources:
apps/chat-api/src/main.ts:1-213
apps/chat-api/src/app/app.module.ts:1-79

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Keep three boundaries explicit

01
02
03
Browser contract
Application services
External systems
Validated HTTP requests, DTOs and SSE responses.
Conversation lifecycle, auth policy and domain coordination.
DIAL Core, OIDC providers, theme host and telemetry exporters.
02
Chat backend
apps-chat-api-02

### Notes:
Slide ID: apps-chat-api-02

Controllers delegate to services. DialClientService centralizes Core SDK configuration and the fetch user-agent behavior. Non-Core integrations can use their own transport where required; do not describe all outbound calls as one SDK operation.

Sources:
apps/chat-api/src/main.ts:1-213
apps/chat-api/src/app/app.module.ts:1-79
apps/chat-api/src/dial/dial-client.service.ts:1-64

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 3 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Bootstrap establishes cross-cutting behavior

01
02
03
04
Telemetry import
Nest application
Middleware / guards
Routes + assets

Before framework loading
Modules and config
Headers and validation
API and SPA responses
Strict ValidationPipe rejects unknown request fields.
03
Chat backend
apps-chat-api-03

### Notes:
Slide ID: apps-chat-api-03

main.ts imports telemetry first, sets validation, CORS, cookie handling, URI versioning and static middleware, and enables graceful shutdown. Source comments explain ordering constraints. The environment schema controls boot-time validation; the source contains both ConfigService reads and some direct process.env reads.

Sources:
apps/chat-api/src/main.ts:1-213
apps/chat-api/src/app/app.module.ts:1-79

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Domain modules organize the backend
| Domain family | Examples |
| --- | --- |
| Conversation execution | conversations, chat, client-channel |
| Knowledge and resources | deployments, applications, files, skills, prompts |
| Sharing and automation | share, publish, scheduled-tasks |
| Platform behavior | auth, app-config, themes, telemetry |
04
Chat backend
apps-chat-api-04

### Notes:
Slide ID: apps-chat-api-04

Domain folders sit directly under src. Auxiliary concerns such as schemas, offline credentials, health and user configuration are also wired by AppModule. The table groups the modules for readability and does not replace the source module index.

Sources:
apps/chat-api/src/app/app.module.ts:1-79

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Representative HTTP contracts
| Operation | Current path |
| --- | --- |
| List deployments | GET /api/v1/deployments |
| Generate a conversation | POST /api/v1/conversations/completions |
| Current user | GET /api/v1/auth/me |
| Theme configuration | GET /api/themes |
05
Chat backend
apps-chat-api-05

### Notes:
Slide ID: apps-chat-api-05

The main business domains use URI versioning, but themes are still unversioned in the implementation. This is a concrete exception to the written rule, not a typo to silently correct in the slides. Swagger handler names feed operation ids and the generated client.

Sources:
apps/chat-api/src/deployments/deployments.controller.ts:1-194
apps/chat-api/src/conversations/conversation.controller.ts:1-852
apps/chat-api/src/auth/auth.controller.ts:1-702
apps/chat-api/src/themes/theme.controller.ts:1-131

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
A completion has a persisted lifecycle

01
02
03
04
Request / principal
Save start state
Relay generation
Save terminal state

Validate and authorize
User and placeholder
Accumulate chunks
Complete, stopped or failed
Backend persistence survives the originating browser disconnect.
06
Chat backend
apps-chat-api-06

### Notes:
Slide ID: apps-chat-api-06

The controller intentionally does not stop generation when the response disconnects. Generation services retain the active operation in memory and persist terminal or partial results. Dedicated stop and attach operations support user control and reopening a running conversation. Process-local state requires deployment consideration.

Sources:
apps/chat-api/src/conversations/conversation.controller.ts:1-852
apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773
apps/chat-api/src/conversations/conversation-generation.service.ts:1-340

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Upstream dispatch is controlled on the server
| Condition | Outcome |
| --- | --- |
| Operator flag disabled | Use Chat Completions |
| Flag enabled; capability absent | Use Chat Completions |
| Flag enabled; responsesApi true | Use ResponsesAdapter |
07
Chat backend
apps-chat-api-07

### Notes:
Slide ID: apps-chat-api-07

The deployment is re-resolved under the current user token. Both the operator flag and capability matter; the small pure resolver by itself shows only the capability check. The browser sees the same normalized completion contract. Failed requests are not automatically retried through another generation API.

Sources:
apps/chat-api/src/conversations/streaming/conversation-streaming.service.ts:1-773
apps/chat-api/src/conversations/generation/generation-api.ts:1-27
docs/responses-api-integration.md:1-460

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Authentication has explicit request scope

01
02
03
04
Browser cookie
Session strategy
Session Guard
Domain service

Encrypted session
Verify / refresh
Set request identity
Call Core with token
Header-token authentication is a separately configured strategy.
08
Chat backend
apps-chat-api-08

### Notes:
Slide ID: apps-chat-api-08

The cookie payload carries encrypted tokens; browser JavaScript does not receive their values. The header strategy is enabled through configuration and verifies allowed issuer/provider identity. Per-request principal and auth data must not be stored in a mutable service singleton.

Sources:
apps/chat-api/src/auth/session/session.guard.ts:1-112
apps/chat-api/src/auth/strategies/cookie-session.strategy.ts:1-147
apps/chat-api/src/auth/strategies/header-token.strategy.ts:1-256
apps/chat-api/src/auth/session/session.service.ts:1-58

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Keep controller and DTO changes synchronized
Source excerpt from ChatController · direct completion proxy.

@Controller({ path: 'chat', version: '1' })
export class ChatController {
  @Post('completions')
  sendCompletion(@Req() req: Request,
                 @Body() dto: ChatCompletionDto) {
    const { at } = req.user as SessionUser;
    return this.chatService.sendCompletion(dto, at);
  }
}
09
Chat backend
apps-chat-api-09

### Notes:
Slide ID: apps-chat-api-09

This is an abridged source excerpt, not a new runnable controller. Imports, constructor injection and Swagger decorators are omitted for readability; the original source contains them. This direct /chat/completions endpoint is distinct from the conversation persistence and streaming workflow. Full source excerpts are retained by path and range in the index.

Sources:
apps/chat-api/src/chat/chat.controller.ts:1-33
apps/chat-api/src/chat/dto/chat-completion.dto.ts:1-104

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Regenerate the contract after API changes

01
02
03
04
Controller + DTO
Open API export
Client generation
Drift check

Swagger annotations
openapi-spec
openapi-sdk
openapi:check
npm run openapi runs the complete regeneration workflow.
10
Chat backend
apps-chat-api-10

### Notes:
Slide ID: apps-chat-api-10

The generated client is checked in. Update server definitions rather than editing generated methods. The operationIdFactory uses handler names, so naming the handler changes the browser-facing method. Commands shown here were not run because they would modify the repository artifacts.

Sources:
package.json:1-199
tools/openapi/check-client.mjs:1-46
apps/chat-api/src/openapi/openapi.config.ts:1-30
libs/chat-api-client/src/index.ts:1-1

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 11 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Configure the runtime deliberately
| Configuration | Responsibility |
| --- | --- |
| DIAL\_CORE\_URL | Core transport endpoint |
| AUTH\_\* settings | Session keys and provider configuration |
| RESPONSES\_API\_ENABLED | Server-only upstream dispatch switch |
| MCP\_APP\_SANDBOX\_URL | Separate-origin MCP proxy URL |
11
Chat backend
apps-chat-api-11

### Notes:
Slide ID: apps-chat-api-11

The exact required fields and defaults are in the backend README and environment schema. Use obvious demo values when experimenting; do not embed real secrets in code examples. Invalid required configuration fails at boot. The runtime also supports feature, theme, cookie and telemetry settings.

Sources:
apps/chat-api/README.md:1-1047
apps/chat-api/src/config/environment.config.ts:1-960

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 12 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Run and verify the backend
From the repository root with configured environment values.

npm run start:api

npm exec nx run @epam/chat-api:typecheck
npm exec nx run @epam/chat-api:test
npm run build:api

# API documentation is configured in main.ts.
# Use the deployment environment reference for auth.
12
Chat backend
apps-chat-api-12

### Notes:
Slide ID: apps-chat-api-12

Nx resolves @epam/chat-api as the project name. The serve target builds/runs the backend, while the separate start:api:dev script uses HMR tooling. These application commands are documented, not run during presentation generation. Backend integration tests use mocked external clients.

Sources:
package.json:1-199
apps/chat-api/src/main.ts:1-213

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 13 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Existing tests exercise contracts and failures
| Area | Source evidence |
| --- | --- |
| Conversation controller | SSE, attach, errors and persistence integration specs |
| Authentication | Session, CSRF and strategy specs |
| Domain transport | Chat controller and service specs |
| Sandbox/static assets | App-owned asset and policy behavior tests |
13
Chat backend
apps-chat-api-13

### Notes:
Slide ID: apps-chat-api-13

The inspected test files provide concrete behavior expectations. Test presence alone is not a passing suite result, and the presentation QA does not substitute for backend security testing. Run focused tests and repository verification for a code change.

Sources:
apps/chat-api/src/conversations/tests/conversation.controller.integration.spec.ts:1-911
apps/chat-api/src/auth/session/tests/session.guard.spec.ts:1-147
apps/chat-api/src/chat/tests/chat.controller.integration.spec.ts:1-117

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 14 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  APPLICATION DEEP DIVE
Operational tradeoffs shape deployment

01
02
03
Process-local state
External dependencies
Policy exceptions exist
Generation registries and caches are not durable cross-pod coordination.
Core and identity-provider availability affect user workflows.
Unversioned themes and documented transport gaps remain in the source.
14
Chat backend
apps-chat-api-14

### Notes:
Slide ID: apps-chat-api-14

Encrypted-cookie authentication enables stateless session decryption across correctly configured pods, but it does not make every runtime mechanism distributed. Distinguish session storage from in-memory active-generation coordination. Use deployment-specific operational checks before adopting a multi-instance topology.

Sources:
apps/chat-api/src/conversations/conversation-generation.service.ts:1-340
apps/chat-api/src/app/cache.config.ts:1-28
apps/chat-api/src/themes/theme.controller.ts:1-131

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.