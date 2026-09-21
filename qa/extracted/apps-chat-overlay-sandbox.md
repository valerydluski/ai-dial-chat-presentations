<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Overlay sandbox
A real browser host for exercising the chat overlay protocol.

Integration cases
Port 4300
Running chat required
apps/chat-overlay-sandbox
01
Overlay sandbox
apps-chat-overlay-sandbox-01

### Notes:
Slide ID: apps-chat-overlay-sandbox-01

This is a React/Vite demonstration application, not an isolated MCP resource renderer. It hosts existing overlay clients against a running chat instance.

Sources:
apps/chat-overlay-sandbox/README.md:1-73
apps/chat-overlay-sandbox/src/main.tsx:1-15

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Each case demonstrates a distinct contract
| Case | Demonstration |
| --- | --- |
| DirectOverlayCase | Mount into a host-owned region |
| ManagerOverlayCase | Floating widget controls |
| ConversationListCase | List, create, select, rename and delete |
| Features / auth cases | Live options and provider login UI modes |
02
Overlay sandbox
apps-chat-overlay-sandbox-02

### Notes:
Slide ID: apps-chat-overlay-sandbox-02

EnabledFeaturesCase and AuthUiModeCase complete the set. Cases are actual source modules under src/cases. They are useful for reproducing integration behavior before embedding the overlay into a separate product.

Sources:
apps/chat-overlay-sandbox/README.md:1-73

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 3 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Trace the host-to-chat handshake

01
02
03
04
Sandbox page
Chat Overlay
Embedded chat
Host controls

Choose an integration case
Create iframe
Readiness exchange
Send requests / read events
Host allowlisting and overlay mode are prerequisites.
03
Overlay sandbox
apps-chat-overlay-sandbox-03

### Notes:
Slide ID: apps-chat-overlay-sandbox-03

The host API waits for the full ready-to-interact handshake. A blank iframe caused by frame-ancestors policy is not a protocol timeout to fix in the controls. Check server allowlisting and runtime overlay mode first.

Sources:
libs/chat-overlay/src/lib/ChatOverlay.ts:1-494
apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx:1-242

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Reproduce the local scenario
Configure the backend, then run both the chat and this sandbox.

OVERLAY_ENABLED=true
ALLOWED_IFRAME_ORIGINS=http://localhost:4300

# In the shell that starts the sandbox:
VITE_CHAT_OVERLAY_HOST=http://localhost:4207 \
  npm exec nx serve chat-overlay-sandbox
04
Overlay sandbox
apps-chat-overlay-sandbox-04

### Notes:
Slide ID: apps-chat-overlay-sandbox-04

The first two lines are backend environment configuration, not values to set only on the sandbox process. The host override is passed to the Vite sandbox. Run chat at 4207 and its backend at 5000 first. No real user data is required to open the page, but an authenticated deployment may require login for chat actions.

Sources:
apps/chat-overlay-sandbox/README.md:1-73
apps/chat-overlay-sandbox/vite.config.mts:1-59

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
A direct overlay is a small integration
Checked pattern from examples/chat-overlay.ts.

const overlay = new ChatOverlay('#demo-chat', {
  domain: 'http://localhost:4207',
  theme: 'dark',
});
await overlay.ready();
await overlay.setInputContent('Explain the demo');
// Later: overlay.destroy();
05
Overlay sandbox
apps-chat-overlay-sandbox-05

### Notes:
Slide ID: apps-chat-overlay-sandbox-05

The complete example receives domain as a parameter, subscribes to an event and returns cleanup. The container must exist in the page. Changing input is a protocol operation; it does not automatically send a model request.

Sources:
apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx:1-242
libs/chat-overlay/src/lib/ChatOverlay.ts:1-494

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Deployment shares the main chat image

01
02
03
Published route
Enable it explicitly
Separate HTML policy
The backend can serve the sandbox at /overlay-sandbox/.
The backend sandbox flag controls exposure of the route.
The backend supplies the sandbox style nonce and response policy.
06
Overlay sandbox
apps-chat-overlay-sandbox-06

### Notes:
Slide ID: apps-chat-overlay-sandbox-06

The root Dockerfile builds this app with the frontend and backend. The deployed sandbox embeds the current origin. This same-origin deployment is intentional for this demo host and must not be copied to the MCP sandbox architecture.

Sources:
apps/chat-overlay-sandbox/README.md:1-73
Dockerfile:1-70
apps/chat-api/src/app/static-assets.ts:1-215

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Verify cases through the current targets
Nx targets come from the resolved project graph.

npm exec nx test chat-overlay-sandbox
npm exec nx build chat-overlay-sandbox
npm exec nx run chat-overlay-sandbox:typecheck
07
Overlay sandbox
apps-chat-overlay-sandbox-07

### Notes:
Slide ID: apps-chat-overlay-sandbox-07

The source includes seven test files for sandbox behavior. These suites were inspected but not run for the presentation task. The live integration requires the external chat deployment and its server policy, beyond what a mocked test can establish.

Sources:
apps/chat-overlay-sandbox/README.md:1-73
apps/chat-overlay-sandbox/package.json:1-10

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  SANDBOX WALKTHROUGH
Interpret integration failures at the right layer

01
02
03
Blank frame
No ready event
Login cannot complete
Check chat CSP frame-ancestors and allowed host origin.
Inspect protocol readiness after the iframe loads.
Verify the exact provider and configured UI mode.
08
Overlay sandbox
apps-chat-overlay-sandbox-08

### Notes:
Slide ID: apps-chat-overlay-sandbox-08

Same-window identity-provider login in an iframe depends on the provider tenant and browser policy. The sandbox exposes those choices for investigation; it cannot make an incompatible provider embeddable. Use it as a reproducible integration host rather than a proof of production compatibility.

Sources:
apps/chat-overlay-sandbox/README.md:1-73
libs/chat-overlay/src/lib/ChatOverlay.ts:1-494

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.