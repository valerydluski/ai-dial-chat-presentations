<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Chat overlay
Embed a running chat with a typed message protocol.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-chat-overlay
01
Chat overlay
lib-chat-overlay-01

### Notes:
Slide ID: lib-chat-overlay-01

This session explains embed a running chat with a typed message protocol. The library is a local private workspace package at libs/chat-overlay. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Embed a running chat with a typed message protocol.

01
02
03
Embed a full experience
Control conversations
Offer floating widgets
Mount the chat iframe in a host-owned region.
Set input, send requests and subscribe to events.
Use ChatOverlayManager for toggle/fullscreen chrome.
02
Chat overlay
lib-chat-overlay-02

### Notes:
Slide ID: lib-chat-overlay-02

Start with a concrete caller need. Embed a full experience: Mount the chat iframe in a host-owned region. Control conversations: Set input, send requests and subscribe to events. Offer floating widgets: Use ChatOverlayManager for toggle/fullscreen chrome. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay

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
Host page
Readiness handshake
Embedded chat
Events and results

Chat Overlay instance
Readiness event
Handle typed requests
Correlated host callbacks
Library: Iframe lifecycle, protocol handshake, request correlation and optional widget chrome.
03
Chat overlay
lib-chat-overlay-03

### Notes:
Slide ID: lib-chat-overlay-03

The library owns Iframe lifecycle, protocol handshake, request correlation and optional widget chrome. The host owns Chat deployment, allowed origins, identity-provider policy and host page lifecycle.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
ChatOverlay · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| new ChatOverlay(root, options) | Mount and configure one iframe |
| ready() | Promise for the readiness handshake |
| setInputContent(text) | Request to the embedded chat |
| subscribe / destroy | Event lifecycle and cleanup |
04
Chat overlay
lib-chat-overlay-04

### Notes:
Slide ID: lib-chat-overlay-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

const overlay = new ChatOverlay('#demo-chat', {
  domain: 'https://chat.example.com',
  theme: 'dark',
});
await overlay.ready();
await overlay.setInputContent('Explain the architecture');
// On host teardown:
overlay.destroy();
Full example: examples/chat-overlay.ts · uses @epam/ai-dial-chat-overlay
05
Chat overlay
lib-chat-overlay-05

### Notes:
Slide ID: lib-chat-overlay-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/chat-overlay.ts. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Mount the chat iframe in a host-owned region. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep chat overlay focused on its public responsibility.

01
02
03
Mount the iframe
Wait for readiness
Match host lifetime
Create ChatOverlay in an existing host-owned element.
Await ready() before sending the initial input content.
Subscribe to events; unsubscribe and destroy on teardown.
06
Chat overlay
lib-chat-overlay-06

### Notes:
Slide ID: lib-chat-overlay-06

Follow this concrete integration sequence. Mount the iframe: Create ChatOverlay in an existing host-owned element. Wait for readiness: Await ready() before sending the initial input content. Match host lifetime: Subscribe to events; unsubscribe and destroy on teardown. The complete typed module in examples/chat-overlay.ts shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Subscribe and clean up
Match event ownership to the host page lifecycle.

const unsubscribe = overlay.subscribe(
  OverlayEventType.GptStartGenerating,
  () => console.info('Demo generation started'),
);

// On host teardown:
unsubscribe();
overlay.destroy();
Focused source-backed example · see examples/ and content/api-index.md.
07
Chat overlay
lib-chat-overlay-10

### Notes:
Slide ID: lib-chat-overlay-10

The full mountDemoOverlay function returns the teardown callback. Await the handshake before issuing normal requests. Destroy the overlay when its host container is no longer valid.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Any browser framework
Lifecycle contract
Two integration levels
The overlay implementation uses DOM/TypeScript rather than React.
Await ready, subscribe deliberately and destroy on unmount.
Direct overlay for a container; manager for floating widgets.
08
Chat overlay
lib-chat-overlay-07

### Notes:
Slide ID: lib-chat-overlay-07

Customization comes from the current exports and prop declarations. Framework-independent: The overlay implementation uses DOM/TypeScript rather than React. Lifecycle contract: Await ready, subscribe deliberately and destroy on unmount. Two integration levels: Direct overlay for a container; manager for floating widgets. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | apps/chat-overlay-sandbox/src/cases/ConversationListCase/ConversationListCase.tsx |
| Test evidence | throws a descriptive error when the root selector matches nothing |
| Test evidence | throws a descriptive error for an unknown overlayId |
09
Chat overlay
lib-chat-overlay-08

### Notes:
Slide ID: lib-chat-overlay-08

Actual consumers: apps/chat-overlay-sandbox/src/cases/ConversationListCase/ConversationListCase.tsx; apps/chat-overlay-sandbox/src/cases/EnabledFeaturesCase/EnabledFeaturesCase.tsx; apps/chat-overlay-sandbox/src/cases/ManagerOverlayCase/ManagerOverlayCase.tsx; apps/chat-overlay-sandbox/src/cases/DirectOverlayCase/DirectOverlayCase.tsx; apps/chat/src/components/CatalogView/CatalogView.tsx; apps/chat/src/pages/SettingsPage/PreferencesTab/PreferencesTab.tsx. Existing test evidence: [{"file": "libs/chat-overlay/src/lib/tests/ChatOverlay.spec.ts", "assertions": ["ChatOverlay", "throws a descriptive error when the root selector matches nothing", "creates an iframe with a non-empty accessible name", "allows auth popups to open outside the iframe sandbox", "styles the root, iframe, and loader from an injected stylesheet instead of inline styles", "injects the stylesheet once per document", "keeps a host loaderClass alongside the default loader class", "does not add the positioning class to a root with existing non-static positioning", "does not request microphone permission by default", "requests microphone permission when voice input is enabled", "hides the default loader on READY when loaderHideEvent is unset", "keeps the loader visible until the configured loaderHideEvent", "hides the loader even when loaderStyles pins an inline display", "keeps non-display loaderStyles entries after the loader hides", "reads the loader palette from themable custom properties"]}, {"file": "libs/chat-overlay/src/lib/tests/ChatOverlayManager.spec.ts", "assertions": ["ChatOverlayManager", "throws a descriptive error for an unknown overlayId", "creates a toggle button with a non-empty accessible name", "makes toggle, close, and fullscreen buttons keyboard-focusable in DOM order", "grants fullscreen permission to the iframe when allowFullscreen is set", "forwards ready() to the requested overlay", "shows the panel and hides the toggle button on showOverlay", "removes the container and toggle button on removeOverlay, and further calls throw", "destroys all overlays and stops recomputing layout on resize", "conversation-list method forwarding", "throws a descriptive error for an unknown overlayId for each new method", "forwards each new method to the underlying ChatOverlay instance with the same arguments", "forwards setOverlayOptions with enabledFeatures unchanged to the underlying ChatOverlay instance"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-chat-overlay:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay
apps/chat-overlay-sandbox/src/cases/ConversationListCase/ConversationListCase.tsx:1-317
libs/chat-overlay/src/lib/tests/ChatOverlay.spec.ts:1-1060
libs/chat-overlay/src/lib/tests/ChatOverlayManager.spec.ts:1-229

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Embedding policy
Auth constraints
No server replacement
The server must allow the host origin in frame-ancestors.
Provider iframe behavior varies; configure supported login UI modes.
The overlay still needs a running chat and backend.
10
Chat overlay
lib-chat-overlay-09

### Notes:
Slide ID: lib-chat-overlay-09

Review these constraints before choosing the library. Embedding policy: The server must allow the host origin in frame-ancestors. Auth constraints: Provider iframe behavior varies; configure supported login UI modes. No server replacement: The overlay still needs a running chat and backend. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/chat-overlay/README.md:1-307
libs/chat-overlay/src/index.ts:1-4
libs/chat-overlay/package.json:1-30
libs/chat-overlay/src/lib/ChatOverlay.ts:110-494 — ChatOverlay
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.