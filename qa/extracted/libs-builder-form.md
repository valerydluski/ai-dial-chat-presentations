<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Builder form
Give entity editors a shared structure and validation vocabulary.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-builder-form
01
Builder form
lib-builder-form-01

### Notes:
Slide ID: lib-builder-form-01

This session explains give entity editors a shared structure and validation vocabulary. The library is a local private workspace package at libs/builder-form. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Give entity editors a shared structure and validation vocabulary.

01
02
03
Build an editor
Share field rules
Localize metadata
Compose metadata and setup sections in a consistent page.
Use one validator for name and version policies.
Edit additional deployment names and descriptions by locale.
02
Builder form
lib-builder-form-02

### Notes:
Slide ID: lib-builder-form-02

Start with a concrete caller need. Build an editor: Compose metadata and setup sections in a consistent page. Share field rules: Use one validator for name and version policies. Localize metadata: Edit additional deployment names and descriptions by locale. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps

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
Host values
Editor controls
Validation codes
Host adapter

Metadata and labels
Field changes
Required or invalid
Translate and persist
Library: Editor shells, field controls and pure validation error codes.
03
Builder form
lib-builder-form-03

### Notes:
Slide ID: lib-builder-form-03

The library owns Editor shells, field controls and pure validation error codes. The host owns Save behavior, routing, translated errors, avatar resolution and file access.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
EditorLayout · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| title | string |
| onBack | () => void |
| leftContent (optional) | ReactNode |
| rightContent (optional) | ReactNode |
04
Builder form
lib-builder-form-04

### Notes:
Slide ID: lib-builder-form-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<EditorLayout
  title="Create demo deployment" onBack={onBack}
  leftContent={
    <EditorSection title="Metadata">Demo fields</EditorSection>
  }
  rightContent={
    <EditorSection title="Setup">Host setup</EditorSection>
  }
/>
Full example: examples/builder-form.tsx · uses @epam/ai-dial-builder-form
05
Builder form
lib-builder-form-05

### Notes:
Slide ID: lib-builder-form-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/builder-form.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Compose metadata and setup sections in a consistent page. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep builder form focused on its public responsibility.

01
02
03
Compose metadata
Validate values
Save through the host
Place shared fields inside the editor sections.
Map validation error codes to localized field messages.
Submit the validated values using the application adapter.
06
Builder form
lib-builder-form-06

### Notes:
Slide ID: lib-builder-form-06

Follow this concrete integration sequence. Compose metadata: Place shared fields inside the editor sections. Validate values: Map validation error codes to localized field messages. Save through the host: Submit the validated values using the application adapter. The complete typed module in examples/builder-form.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Validate without translating
The host maps error codes into messages.

const codes = validateDeploymentCreationFields(
  { name: '', description: '', iconUrl: '',
    version: '1.0.0', topics: [], otherLocales: [] },
  { validateNamePattern: true, validateVersionPattern: true },
);
Focused source-backed example · see examples/ and content/api-index.md.
07
Builder form
lib-builder-form-10

### Notes:
Slide ID: lib-builder-form-10

An empty name produces a validation error code. No translation service is invoked by the validator. The full example includes this call.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Layout composition
Metadata fields
Policy switches
EditorLayout exposes leftContent, rightContent and actions.
The shared creation form includes avatar, version, topics and locales.
Name and version pattern checks are opt-in validator options.
08
Builder form
lib-builder-form-07

### Notes:
Slide ID: lib-builder-form-07

Customization comes from the current exports and prop declarations. Layout composition: EditorLayout exposes leftContent, rightContent and actions. Metadata fields: DeploymentCreationForm includes avatar, version, topics and locales. Policy switches: Name and version pattern checks are opt-in validator options. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | prompt-editor/src/components/PromptEditor/PromptEditor.tsx |
| Test evidence | renders all shared fields |
| Test evidence | renders the host file manager modal when open |
09
Builder form
lib-builder-form-08

### Notes:
Slide ID: lib-builder-form-08

Actual consumers: libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx; libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx; libs/toolset-editor/src/components/GeneralForm/GeneralForm.tsx; libs/toolset-editor/src/components/ToolsetEditor/ToolsetEditor.tsx; libs/toolset-editor/src/models/toolset-editor-props.ts; libs/toolset-editor/src/models/general-form-props.ts. Existing test evidence: [{"file": "libs/builder-form/src/components/DeploymentCreationForm/tests/DeploymentCreationForm.spec.tsx", "assertions": [",", "DeploymentCreationForm", "renders all shared fields", "calls onAddAvatarClick when the Add avatar button is clicked", "calls onChange with a name patch when the name input changes", "calls onChange with a description patch when the textarea changes", "surfaces a passed-in name error without validating itself", "renders no error when none is passed"]}, {"file": "libs/builder-form/src/components/AvatarPickerModal/tests/AvatarPickerModal.spec.tsx", "assertions": ["AvatarPickerModal", "renders the host file manager modal when open", "does not render the host file manager modal when closed", "forwards the file manager attach result to onAttach"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-builder-form:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately. Existing test evidence includes: renders all shared fields.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:1-310
libs/builder-form/src/components/DeploymentCreationForm/tests/DeploymentCreationForm.spec.tsx:1-183
libs/builder-form/src/components/AvatarPickerModal/tests/AvatarPickerModal.spec.tsx:1-95

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 10 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Avatar ownership
Locale visibility
State is mixed
Resolve iconPreviewUrl and open file selection in the host.
The locale editor hides when no locale options are supplied.
Some controls manage transient state; persistence remains outside.
10
Builder form
lib-builder-form-09

### Notes:
Slide ID: lib-builder-form-09

Review these constraints before choosing the library. Avatar ownership: Resolve iconPreviewUrl and open file selection in the host. Locale visibility: DeploymentLocalesField hides when no locale options are supplied. State is mixed: Some controls manage transient state; persistence remains outside. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/builder-form/README.md:1-420
libs/builder-form/src/index.ts:1-65
libs/builder-form/package.json:1-39
libs/builder-form/src/components/EditorLayout/EditorLayout.tsx:18-120 — EditorLayout
libs/builder-form/src/models/editor-layout-props.ts:24-45 — EditorLayoutProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.