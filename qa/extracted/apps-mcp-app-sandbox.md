<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
MCP sandbox proxy
A separate-origin HTML bridge for the MCP Apps double-iframe boundary.

NestJS proxy page
Port 3100
Allowlist required
apps/mcp-app-sandbox
01
MCP sandbox proxy
apps-mcp-app-sandbox-01

### Notes:
Slide ID: apps-mcp-app-sandbox-01

This small application serves the sandbox-proxy document used by the MCP UI renderer. It must be deployed on an origin distinct from the chat host. It is an infrastructure component of the rendering boundary, not a catalog demo.

Sources:
apps/mcp-app-sandbox/README.md:1-60
apps/mcp-app-sandbox/src/main.ts:1-49

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Why a separate application exists

01
02
03
04
Chat host
Proxy frame
Inner tool frame
Message bridge

Trusted app origin
Distinct host or port
Untrusted UI document
Validated communication
Same-origin hosting would defeat the intended isolation boundary.
02
MCP sandbox proxy
apps-mcp-app-sandbox-02

### Notes:
Slide ID: apps-mcp-app-sandbox-02

The README and implementation adapt the MCP reference double-iframe pattern. A sandbox attribute alone is not the reason for this separate app; the distinct origin keeps the proxy and tool document out of the host origin. The inner document and bridge have their own constraints.

Sources:
apps/mcp-app-sandbox/README.md:1-60
apps/mcp-app-sandbox/src/main.ts:1-49
apps/mcp-app-sandbox/src/app/sandbox-page.ts:1-103

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 3 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Request validation precedes HTML delivery
Allowed request path · invalid origin returns 403 before HTML rendering

01
02
03
04
GET /
Allowlist check
Policy builder
HTML response

Origin or Referer
Verify host origin
Scope the CSP
Return proxy page
No allowlist means no successful page response.
03
MCP sandbox proxy
apps-mcp-app-sandbox-03

### Notes:
Slide ID: apps-mcp-app-sandbox-03

SandboxService uses an Origin header when present, then falls back to the Referer origin. A missing or unapproved origin is rejected. SandboxController sends text/html, CSP, nosniff, cross-origin resource policy and no-store. A raw GET without the required embedding context should fail.

Sources:
apps/mcp-app-sandbox/src/app/sandbox.controller.ts:1-33
apps/mcp-app-sandbox/src/app/sandbox.service.ts:1-56

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Configure two sides of the connection
The sandbox origin must differ from the chat origin.

# Start the sandbox:
MCP_APP_SANDBOX_ALLOWED_HOST_ORIGINS=http://localhost:4207 \
  npm exec nx serve mcp-app-sandbox

# Configure chat-api separately:
MCP_APP_SANDBOX_URL=http://localhost:3100
04
MCP sandbox proxy
apps-mcp-app-sandbox-04

### Notes:
Slide ID: apps-mcp-app-sandbox-04

The frontend receives the sandbox URL through the backend client-configuration pipeline. PORT defaults to 3100. Production should use the actual distinct HTTPS origins and the intended host allowlist. No secret values are required in this example.

Sources:
apps/mcp-app-sandbox/README.md:1-60
apps/mcp-app-sandbox/src/config/environment.config.ts:1-29

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
The page and policy are app-owned

01
02
03
Controller
Service
Page builder
Validates the caller context and sets response headers.
Combines allowed origin, HTML and CSP construction.
Creates the bridge document used by the nested renderer.
05
MCP sandbox proxy
apps-mcp-app-sandbox-05

### Notes:
Slide ID: apps-mcp-app-sandbox-05

main.ts intentionally disables Helmet generic CSP and frame blocking so the route can deliver its custom embedding policy. CORS is explicitly disabled for cross-origin script fetching. This route is designed for iframe navigation with origin validation, not a general data API.

Sources:
apps/mcp-app-sandbox/src/app/sandbox.controller.ts:1-33
apps/mcp-app-sandbox/src/app/sandbox.service.ts:1-56
apps/mcp-app-sandbox/src/app/csp.ts:1-19
apps/mcp-app-sandbox/src/app/sandbox-page.ts:1-103

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
A rendered MCP view needs the whole chain

01
02
03
04
Message evidence
Host adapter
MCP renderer
Proxy page

Tool and resource match
Fetch resource / call tool
Configured sandbox URL
Nested UI lifecycle
Use the mcp-apps and attachment-canvas decks for the frontend contracts.
06
MCP sandbox proxy
apps-mcp-app-sandbox-06

### Notes:
Slide ID: apps-mcp-app-sandbox-06

The sandbox alone does not discover tools or authenticate tool calls. Those operations are supplied by the host adapter and backend. To reproduce a full interaction, use a configured MCP-capable deployment and a real ui:// resource; this bundle does not manufacture a product screenshot of that interaction.

Sources:
libs/mcp-apps/src/models/mcp-apps.ts:1-148
libs/attachment-canvas/src/components/McpAppCanvasRenderer/McpAppCanvasRenderer.tsx:1-150
apps/mcp-app-sandbox/src/app/sandbox-page.ts:1-103

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Build and check what exists
The resolved project has build, serve, lint and typecheck; no test target.

npm exec nx build mcp-app-sandbox
npm exec nx run mcp-app-sandbox:typecheck
npm exec nx run mcp-app-sandbox:lint

docker build -f apps/mcp-app-sandbox/Dockerfile \
  -t mcp-app-sandbox .
07
MCP sandbox proxy
apps-mcp-app-sandbox-07

### Notes:
Slide ID: apps-mcp-app-sandbox-07

No source test files or test target were discovered for this application. Do not invent a passing test result or recommend a nonexistent target. Build/typecheck/lint commands are available; real isolation behavior needs a browser integration exercise with distinct origins.

Sources:
apps/mcp-app-sandbox/package.json:1-103
apps/mcp-app-sandbox/README.md:1-60
apps/mcp-app-sandbox/Dockerfile:1-61

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Limits to carry into operations

01
02
03
Exact origin matters
Not a content service
Validation gap
A host allowlist must match the deployed scheme, hostname and port.
The app serves a proxy document, not Core storage or user files.
No dedicated source tests were discovered in this project.
08
MCP sandbox proxy
apps-mcp-app-sandbox-08

### Notes:
Slide ID: apps-mcp-app-sandbox-08

The small source footprint does not reduce the importance of this boundary. Deployment-origin and browser-policy checks remain necessary. The presentation report records that no full live MCP/Core integration was exercised during this output-only documentation task.

Sources:
apps/mcp-app-sandbox/README.md:1-60
apps/mcp-app-sandbox/src/main.ts:1-49
apps/mcp-app-sandbox/src/app/sandbox.service.ts:1-56

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.