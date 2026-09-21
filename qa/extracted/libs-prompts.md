<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Prompts
Pick reusable prompts and collect their parameter values.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-prompts
01
Prompts
lib-prompts-01

### Notes:
Slide ID: lib-prompts-01

This session explains pick reusable prompts and collect their parameter values. The library is a local private workspace package at libs/prompts. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/prompts/README.md:1-145
libs/prompts/src/index.ts:1-14
libs/prompts/package.json:1-41
libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174 — PromptParametersPopup
libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69 — PromptParametersPopupProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Pick reusable prompts and collect their parameter values.

01
02
03
Choose a favorite
Fill placeholders
Populate a composer
Browse FavoritePromptItem data supplied by the host.
Collect values for named prompt parameters.
Resolve values and pass the text to host input state.
02
Prompts
lib-prompts-02

### Notes:
Slide ID: lib-prompts-02

Start with a concrete caller need. Choose a favorite: Browse FavoritePromptItem data supplied by the host. Fill placeholders: Collect values for named prompt parameters. Populate a composer: Resolve values and pass the text to host input state. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/prompts/README.md:1-145
libs/prompts/src/index.ts:1-14
libs/prompts/package.json:1-41
libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174 — PromptParametersPopup
libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69 — PromptParametersPopupProps

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
Favorite selection
Parameter popup
on Submit
Host resolver

Prompt content
Named input fields
Record of values
Resolve and insert text
Library: Favorite prompt selection and parameter-entry UI.
03
Prompts
lib-prompts-03

### Notes:
Slide ID: lib-prompts-03

The library owns Favorite prompt selection and parameter-entry UI. The host owns Loading favorites, deriving parameters, resolving submitted values and sending text.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/prompts/README.md:1-145
libs/prompts/src/index.ts:1-14
libs/prompts/package.json:1-41
libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174 — PromptParametersPopup
libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69 — PromptParametersPopupProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
PromptParametersPopup · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| content | string |
| parameters | PromptParameter[] |
| onSubmit | (values: Record<string, string>) => void |
| open | boolean |
04
Prompts
lib-prompts-04

### Notes:
Slide ID: lib-prompts-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/prompts/README.md:1-145
libs/prompts/src/index.ts:1-14
libs/prompts/package.json:1-41
libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174 — PromptParametersPopup
libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69 — PromptParametersPopupProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<PromptParametersPopup
  open={open} promptName="Demo summary"
  content="Summarize {{topic}}"
  parameters={[{ name: 'topic' }]}
  onClose={close} onCancel={close}
  onSubmit={values => {
    onText(resolvePromptParams(content, values));
  }}
/>
Full example: examples/prompts.tsx · uses @epam/ai-dial-prompts
05
Prompts
lib-prompts-05

### Notes:
Slide ID: lib-prompts-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/prompts.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Browse FavoritePromptItem data supplied by the host. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/prompts/README.md:1-145
libs/prompts/src/index.ts:1-14
libs/prompts/package.json:1-41
libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174 — PromptParametersPopup
libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69 — PromptParametersPopupProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep prompts focused on its public responsibility.

01
02
03
Collect parameters
Resolve the template
Apply the text
Open the parameter popup with content and parameter names.
Use the submitted value map with resolvePromptParams.
The host inserts the resolved text into its composer.
06
Prompts
lib-prompts-06

### Notes:
Slide ID: lib-prompts-06

Follow this concrete integration sequence. Collect parameters: Open PromptParametersPopup with content and parameter names. Resolve the template: Use the submitted value map with resolvePromptParams. Apply the text: The host inserts the resolved text into its composer. The complete typed module in examples/prompts.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/prompts/README.md:1-145
libs/prompts/src/index.ts:1-14
libs/prompts/package.json:1-41
libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174 — PromptParametersPopup
libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69 — PromptParametersPopupProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Favorite callbacks
Default values
Explicit popup state
Selection, favorite changes and browse actions are caller-owned.
Shared helpers support tokens with a default value.
open, onClose and onCancel are controlled by the host.
07
Prompts
lib-prompts-07

### Notes:
Slide ID: lib-prompts-07

Customization comes from the current exports and prop declarations. Favorite callbacks: Selection, favorite changes and browse actions are caller-owned. Default values: Shared helpers support tokens with a default value. Explicit popup state: open, onClose and onCancel are controlled by the host. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/prompts/README.md:1-145
libs/prompts/src/index.ts:1-14
libs/prompts/package.json:1-41
libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174 — PromptParametersPopup
libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69 — PromptParametersPopupProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/components/PromptSelector/PromptParametersPopupOverlay.tsx |
| Test evidence | renders the title and one field per parameter |
| Test evidence | renders the "My Collection" header |
08
Prompts
lib-prompts-08

### Notes:
Slide ID: lib-prompts-08

Actual consumers: apps/chat/src/components/PromptSelector/PromptParametersPopupOverlay.tsx; apps/chat/src/components/PromptSelector/PromptSelectorOverlay.tsx; apps/chat/src/components/PromptSelector/usePromptSelectorOverlay.tsx. Existing test evidence: [{"file": "libs/prompts/src/components/PromptParametersPopup/tests/PromptParametersPopup.spec.tsx", "assertions": ["PromptParametersPopup", "renders the title and one field per parameter", "renders one field for a token repeated in the content, via extractPromptParams", "does not render a back chevron when onBack is omitted", "renders a back chevron when onBack is provided", "calls onBack when the back chevron is clicked", "disables Submit until every parameter field is filled", "calls onSubmit with the entered values when Submit is clicked", "opens a defaulted field holding its default value", "labels a defaulted field with the name alone, without the separator", "enables Submit with no typing when every parameter carries a default", "submits the default when a defaulted field is left untouched", "submits the edited value rather than the default when the field is changed", "offers the default again when the same prompt comes back after another", "calls onCancel when Cancel is clicked"]}, {"file": "libs/prompts/src/components/FavoritePromptsPanel/tests/FavoritePromptsPanel.spec.tsx", "assertions": ["FavoritePromptsPanel", "renders the ", "shows the empty-state hint when there are no favorites", "shows the ", "renders a favorite row with its name and a pressed star toggle", "calls onSelect with the item when a row is clicked", "does not call onToggleFavorite synchronously on click", "calls onToggleFavorite with the id once the exit animation finishes", "calls onBrowse when ", "renders the description in the row tooltip when a described row is hovered", "FavoritePromptsPanel \u2014 public class names", "stamps the panel root"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-prompts:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: renders the "My Collection" header.

Sources:
libs/prompts/README.md:1-145
libs/prompts/src/index.ts:1-14
libs/prompts/package.json:1-41
libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174 — PromptParametersPopup
libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69 — PromptParametersPopupProps
apps/chat/src/components/PromptSelector/PromptParametersPopupOverlay.tsx:1-71
libs/prompts/src/components/PromptParametersPopup/tests/PromptParametersPopup.spec.tsx:1-205
libs/prompts/src/components/FavoritePromptsPanel/tests/FavoritePromptsPanel.spec.tsx:1-151

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Submission is values
Use shared helpers
Syntax matters
The parameter popup returns a value map for the host to resolve.
Shared helpers extract and resolve prompt parameters.
Double braces define parameters; ordinary braces remain literal.
09
Prompts
lib-prompts-09

### Notes:
Slide ID: lib-prompts-09

Review these constraints before choosing the library. Submission is values: PromptParametersPopup returns a value map, not a sent message. Use shared helpers: extractPromptParams and resolvePromptParams implement token semantics. Syntax matters: Double braces define parameters; ordinary braces remain literal. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/prompts/README.md:1-145
libs/prompts/src/index.ts:1-14
libs/prompts/package.json:1-41
libs/prompts/src/components/PromptParametersPopup/PromptParametersPopup.tsx:27-174 — PromptParametersPopup
libs/prompts/src/models/prompt-parameters-popup-props.ts:32-69 — PromptParametersPopupProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.