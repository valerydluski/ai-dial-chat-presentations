<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Share
Present a share link and access choices without issuing the link.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-share
01
Share
lib-share-01

### Notes:
Slide ID: lib-share-01

This session explains present a share link and access choices without issuing the link. The library is a local private workspace package at libs/share. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/share/README.md:1-123
libs/share/src/index.ts:1-18
libs/share/package.json:1-41
libs/share/src/components/SharePopover/SharePopover.tsx:326-326 — SharePopover
libs/share/src/models/share-popover-props.ts:108-129 — SharePopoverProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Present a share link and access choices without issuing the link.

01
02
03
Share a resource
Represent access
Handle pending work
Show a link or a scannable QR view.
Display view/edit access values as a list.
Show host loading and failure states.
02
Share
lib-share-02

### Notes:
Slide ID: lib-share-02

Start with a concrete caller need. Share a resource: Show a link or a scannable QR view. Represent access: Display view/edit access values as a list. Handle pending work: Show host loading and failure states. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/share/README.md:1-123
libs/share/src/index.ts:1-18
libs/share/package.json:1-41
libs/share/src/components/SharePopover/SharePopover.tsx:326-326 — SharePopover
libs/share/src/models/share-popover-props.ts:108-129 — SharePopoverProps

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
Host share API
Share Popover
on Access Change
Host request

URL and access
Link or QR view
Access-level array
Issue a matching link
Library: Link/QR presentation, copy interactions and access controls.
03
Share
lib-share-03

### Notes:
Slide ID: lib-share-03

The library owns Link/QR presentation, copy interactions and access controls. The host owns Creating or replacing links, permissions and share-URL resolution.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/share/README.md:1-123
libs/share/src/index.ts:1-18
libs/share/package.json:1-41
libs/share/src/components/SharePopover/SharePopover.tsx:326-326 — SharePopover
libs/share/src/models/share-popover-props.ts:108-129 — SharePopoverProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
SharePopover · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| url | string |
| access | ShareLinkAccess[] |
| onAccessChange | (access: ShareLinkAccess[]) => void |
| canEditAccess | boolean |
04
Share
lib-share-04

### Notes:
Slide ID: lib-share-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/share/README.md:1-123
libs/share/src/index.ts:1-18
libs/share/package.json:1-41
libs/share/src/components/SharePopover/SharePopover.tsx:326-326 — SharePopover
libs/share/src/models/share-popover-props.ts:108-129 — SharePopoverProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

function ShareDemo({ onClose }: { onClose: () => void }) {
  const [access, setAccess] = useState([ShareLinkAccess.View]);
  return <SharePopover url="https://example.com/demo-share" isLoading={false}
    error={null} access={access} canEditAccess={false}
    onAccessChange={setAccess} onClose={onClose} />;
}
Full example: examples/share.tsx · uses @epam/ai-dial-share
05
Share
lib-share-05

### Notes:
Slide ID: lib-share-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/share.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Show a link or a scannable QR view. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/share/README.md:1-123
libs/share/src/index.ts:1-18
libs/share/package.json:1-41
libs/share/src/components/SharePopover/SharePopover.tsx:326-326 — SharePopover
libs/share/src/models/share-popover-props.ts:108-129 — SharePopoverProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep share focused on its public responsibility.

01
02
03
Obtain a share link
Control link access
Reflect request state
The host calls its sharing operation and supplies the URL.
Pass allowed access values and permission to edit them.
Pass the updated URL, loading state and any error.
06
Share
lib-share-06

### Notes:
Slide ID: lib-share-06

Follow this concrete integration sequence. Obtain a share link: The host calls its sharing operation and supplies the URL. Control link access: Pass allowed access values and permission to edit them. Reflect request state: Pass the updated URL, loading state and any error. The complete typed module in examples/share.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/share/README.md:1-123
libs/share/src/index.ts:1-18
libs/share/package.json:1-41
libs/share/src/components/SharePopover/SharePopover.tsx:326-326 — SharePopover
libs/share/src/models/share-popover-props.ts:108-129 — SharePopoverProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Typed access
Separate QR component
Explicit errors
ShareLinkAccess represents view and edit levels.
QrCode can be used outside the popover.
url may be undefined while loading; error is supplied separately.
07
Share
lib-share-07

### Notes:
Slide ID: lib-share-07

Customization comes from the current exports and prop declarations. Typed access: ShareLinkAccess represents view and edit levels. Separate QR component: QrCode can be used outside the popover. Explicit errors: url may be undefined while loading; error is supplied separately. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/share/README.md:1-123
libs/share/src/index.ts:1-18
libs/share/package.json:1-41
libs/share/src/components/SharePopover/SharePopover.tsx:326-326 — SharePopover
libs/share/src/models/share-popover-props.ts:108-129 — SharePopoverProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | apps/chat-api/src/share/dto/create-share-link.dto.ts |
| Test evidence | renders the link view by default with Can view access |
08
Share
lib-share-08

### Notes:
Slide ID: lib-share-08

Actual consumers: apps/chat-api/src/share/dto/create-share-link.dto.ts; libs/chat-hooks/src/useShareLink/useShareLink.ts; apps/chat/src/components/SharePopoverContainer/SharePopoverContainer.tsx; libs/attachment-canvas/src/components/VisualizerCanvasRenderer/VisualizerCanvasRenderer.tsx; libs/attachment-canvas/src/utils/vite-external-matcher.ts; apps/chat/src/components/ShareConversationPopoverContainer/ShareConversationPopoverContainer.tsx. Existing test evidence: [{"file": "libs/share/src/components/SharePopover/tests/SharePopover.spec.tsx", "assertions": ["SharePopover", "renders the link view by default with Can view access", "shows the view-access visibility note by default", "shows the edit-access visibility note in both the link and QR views", "calls onAccessChange with Edit when an access option is selected", "shows Can edit as the selected trigger label and checkmark when access starts as Edit", "moves focus between access menu options with Arrow keys", "traps Tab within the open access menu", "shows the interactive access dropdown when canEditAccess is true", "hides the access dropdown and shows a static Can view label when canEditAccess is false", "never shows the edit-access visibility note when canEditAccess is false", "shows the nested-items note only when supplied via labels", "shows a transient Copied confirmation after clicking Copy", "announces Copied via an aria-live region after clicking Copy", "swaps to the QR view and back, moving focus each time"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-share:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/share/README.md:1-123
libs/share/src/index.ts:1-18
libs/share/package.json:1-41
libs/share/src/components/SharePopover/SharePopover.tsx:326-326 — SharePopover
libs/share/src/models/share-popover-props.ts:108-129 — SharePopoverProps
apps/chat-api/src/share/dto/create-share-link.dto.ts:1-43
libs/share/src/components/SharePopover/tests/SharePopover.spec.tsx:1-460

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Access is not cosmetic
No permission enforcement
Named root export
Real access changes require the host to request the appropriate link.
canEditAccess controls UI, not backend authorization.
Import SharePopover by name from the package entry.
09
Share
lib-share-09

### Notes:
Slide ID: lib-share-09

Review these constraints before choosing the library. Access is not cosmetic: Real access changes require the host to request the appropriate link. No permission enforcement: canEditAccess controls UI, not backend authorization. Named root export: Import SharePopover by name from the package entry. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/share/README.md:1-123
libs/share/src/index.ts:1-18
libs/share/package.json:1-41
libs/share/src/components/SharePopover/SharePopover.tsx:326-326 — SharePopover
libs/share/src/models/share-popover-props.ts:108-129 — SharePopoverProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.