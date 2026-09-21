<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Chat API client
Generate typed operations from the backend OpenAPI contract.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-chat-api-client
01
Chat API client
lib-chat-api-client-01

### Notes:
Slide ID: lib-chat-api-client-01

This session explains generate typed operations from the backend openapi contract. The library is a local private workspace package at libs/chat-api-client. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Generate typed operations from the backend OpenAPI contract.

01
02
03
Call the BFF
Evolve an endpoint
Inspect transport details
Use typed API classes from application adapters.
Change Swagger/DTO sources, then regenerate.
Use Raw operations when headers or the Response are needed.
02
Chat API client
lib-chat-api-client-02

### Notes:
Slide ID: lib-chat-api-client-02

Start with a concrete caller need. Call the BFF: Use typed API classes from application adapters. Evolve an endpoint: Change Swagger/DTO sources, then regenerate. Inspect transport details: Use Raw operations when headers or the Response are needed. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi

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
Nest controllers
Open API document
Generated client
App adapter

Swagger and DTOs
Generator input
Typed operations
Configured calls
Library: Generated endpoint paths, DTOs, serializers and Fetch transport runtime.
03
Chat API client
lib-chat-api-client-03

### Notes:
Slide ID: lib-chat-api-client-03

The library owns Generated endpoint paths, DTOs, serializers and Fetch transport runtime. The host owns Base URL, credentials, CSRF policy, middleware and application error presentation.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
DeploymentsApi · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| Configuration | basePath, credentials, middleware |
| listDeployments() | Promise<DeploymentsResponseDto> |
| listDeploymentsRaw({}) | Raw response wrapper and value() |
| Generation source | Nest Swagger + openapi.json |
04
Chat API client
lib-chat-api-client-04

### Notes:
Slide ID: lib-chat-api-client-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

const api = new DeploymentsApi(
  new Configuration({
    basePath: '',
    credentials: 'include',
  }),
);
const deployments = await api.listDeployments();
Full example: examples/chat-api-client.ts · uses @epam/ai-dial-chat-api-client
05
Chat API client
lib-chat-api-client-05

### Notes:
Slide ID: lib-chat-api-client-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/chat-api-client.ts. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Use typed API classes from application adapters. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep chat api client focused on its public responsibility.

01
02
03
Configure transport
Call an operation
Handle the outcome
Create a stable Configuration with origin and middleware.
Use listDeployments() for the parsed response DTO.
Render the result or handle the rejected request in the host.
06
Chat API client
lib-chat-api-client-06

### Notes:
Slide ID: lib-chat-api-client-06

Follow this concrete integration sequence. Configure transport: Create a stable Configuration with origin and middleware. Call an operation: Use listDeployments() for the parsed response DTO. Handle the outcome: Render the result or handle the rejected request in the host. The complete typed module in examples/chat-api-client.ts shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Preserve transport details when needed
Raw operations keep the underlying Response available.

const response = await api.listDeploymentsRaw({});
const status = response.raw.status;
const data = await response.value();
Focused source-backed example · see examples/ and content/api-index.md.
07
Chat API client
lib-chat-api-client-10

### Notes:
Slide ID: lib-chat-api-client-10

The Raw signature requires the request object even when every query field is optional. The normal listDeployments method defaults that object. This distinction is enforced by the example TypeScript check.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Normal vs Raw
Configurable transport
Regeneration scripts
Normal methods resolve values; Raw methods expose the response wrapper.
Configuration accepts basePath, credentials and middleware.
npm run openapi and openapi:check maintain the checked-in artifacts.
08
Chat API client
lib-chat-api-client-07

### Notes:
Slide ID: lib-chat-api-client-07

Customization comes from the current exports and prop declarations. Normal vs Raw: Normal methods resolve values; Raw methods expose the response wrapper. Configurable transport: Configuration accepts basePath, credentials and middleware. Regeneration scripts: npm run openapi and openapi:check maintain the checked-in artifacts. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | usage-dashboard/src/utils/map-user-usage-to-model-limits.ts |
| Validation workflow | Regeneration, typecheck and downstream consumers |
09
Chat API client
lib-chat-api-client-08

### Notes:
Slide ID: lib-chat-api-client-08

Actual consumers: libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts; libs/usage-dashboard/src/utils/map-usage-data-to-dashboard.ts; apps/chat/src/pages/Conversation/Conversation.tsx; apps/chat/src/pages/ToolsetAuthCallback/ToolsetAuthCallback.tsx; apps/chat/src/pages/ScheduledTaskDetailPage/ScheduledTaskDetailPage.tsx; libs/chat-hooks/src/conversation/create-chat-stream-api.ts. Existing test evidence: []. Reproduce project checks from the repository root with npm exec nx run chat-api-client:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi
libs/usage-dashboard/src/utils/map-user-usage-to-model-limits.ts:1-494

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Never hand-edit generated code
Real API names
Streaming needs care
Regeneration overwrites manual client edits.
Use DeploymentsApi; the README ModelsApi example is stale.
Host adapters handle documented raw stream/DTO gaps.
10
Chat API client
lib-chat-api-client-09

### Notes:
Slide ID: lib-chat-api-client-09

Review these constraints before choosing the library. Never hand-edit generated code: Regeneration overwrites manual client edits. Real API names: Use DeploymentsApi; the README ModelsApi example is stale. Streaming needs care: Host adapters handle documented raw stream/DTO gaps. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/chat-api-client/README.md:1-68
libs/chat-api-client/src/index.ts:1-1
libs/chat-api-client/package.json:1-41
libs/chat-api-client/src/generated/src/apis/DeploymentsApi.ts:43-250 — DeploymentsApi
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.