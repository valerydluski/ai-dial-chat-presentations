<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Prompt editor
Author reusable prompt content while leaving persistence to the host.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-prompt-editor
01
Prompt editor
lib-prompt-editor-01

### Notes:
Slide ID: lib-prompt-editor-01

This session explains author reusable prompt content while leaving persistence to the host. The library is a local private workspace package at libs/prompt-editor. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/prompt-editor/README.md:1-160
libs/prompt-editor/src/index.ts:1-16
libs/prompt-editor/package.json:1-37
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310 — PromptEditor
libs/prompt-editor/src/models/prompt-editor-props.ts:125-162 — PromptEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Author reusable prompt content while leaving persistence to the host.

01
02
03
Create a prompt
Revise a prompt
Add folder controls
Edit name, description and Markdown content.
Seed the form with stable initialValues.
Compose PromptFolderField separately when needed.
02
Prompt editor
lib-prompt-editor-02

### Notes:
Slide ID: lib-prompt-editor-02

Start with a concrete caller need. Create a prompt: Edit name, description and Markdown content. Revise a prompt: Seed the form with stable initialValues. Add folder controls: Compose PromptFolderField separately when needed. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/prompt-editor/README.md:1-160
libs/prompt-editor/src/index.ts:1-16
libs/prompt-editor/package.json:1-37
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310 — PromptEditor
libs/prompt-editor/src/models/prompt-editor-props.ts:125-162 — PromptEditorProps

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
Host load
Prompt Editor
on Submit
Host save

Initial values and errors
Local editing
Prompt Editor Values
Validate and persist
Library: Prompt form fields, editing state and optional folder-field UI.
03
Prompt editor
lib-prompt-editor-03

### Notes:
Slide ID: lib-prompt-editor-03

The library owns Prompt form fields, editing state and optional folder-field UI. The host owns Save/load operations, validation errors, routes and folder mutations.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/prompt-editor/README.md:1-160
libs/prompt-editor/src/index.ts:1-16
libs/prompt-editor/package.json:1-37
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310 — PromptEditor
libs/prompt-editor/src/models/prompt-editor-props.ts:125-162 — PromptEditorProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
PromptEditor · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| onSubmit | (values: PromptEditorValues) => void |
| onCancel | () => void |
| initialValues (optional) | Partial<PromptEditorValues> |
| errors (optional) | PromptEditorErrors |
04
Prompt editor
lib-prompt-editor-04

### Notes:
Slide ID: lib-prompt-editor-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/prompt-editor/README.md:1-160
libs/prompt-editor/src/index.ts:1-16
libs/prompt-editor/package.json:1-37
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310 — PromptEditor
libs/prompt-editor/src/models/prompt-editor-props.ts:125-162 — PromptEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<PromptEditor
  initialValues={{
    name: 'Demo summary',
    content: 'Summarize {{topic}}',
  }}
  onSubmit={save}
  onCancel={onCancel}
/>
Full example: examples/prompt-editor.tsx · uses @epam/ai-dial-prompt-editor
05
Prompt editor
lib-prompt-editor-05

### Notes:
Slide ID: lib-prompt-editor-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/prompt-editor.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Edit name, description and Markdown content. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/prompt-editor/README.md:1-160
libs/prompt-editor/src/index.ts:1-16
libs/prompt-editor/package.json:1-37
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310 — PromptEditor
libs/prompt-editor/src/models/prompt-editor-props.ts:125-162 — PromptEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep prompt editor focused on its public responsibility.

01
02
03
Load a prompt
Edit and submit
Save in the host
Supply initialValues with a name and prompt content.
The editor collects the next values through onSubmit.
Persist through an app adapter and decide where to navigate.
06
Prompt editor
lib-prompt-editor-06

### Notes:
Slide ID: lib-prompt-editor-06

Follow this concrete integration sequence. Load a prompt: Supply initialValues with a name and prompt content. Edit and submit: The editor collects the next values through onSubmit. Save in the host: Persist through an app adapter and decide where to navigate. The complete typed module in examples/prompt-editor.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/prompt-editor/README.md:1-160
libs/prompt-editor/src/index.ts:1-16
libs/prompt-editor/package.json:1-37
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310 — PromptEditor
libs/prompt-editor/src/models/prompt-editor-props.ts:125-162 — PromptEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
Load and save states
Editor customization
Separate folder field
isLoading, hasLoadError and isSaving drive the form experience.
Pass labels, limits and markdownEditorTheme.
PromptFolderField delegates mutations through folderActions.
07
Prompt editor
lib-prompt-editor-07

### Notes:
Slide ID: lib-prompt-editor-07

Customization comes from the current exports and prop declarations. Load and save states: isLoading, hasLoadError and isSaving drive the form experience. Editor customization: Pass labels, limits and markdownEditorTheme. Separate folder field: PromptFolderField delegates mutations through folderActions. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/prompt-editor/README.md:1-160
libs/prompt-editor/src/index.ts:1-16
libs/prompt-editor/package.json:1-37
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310 — PromptEditor
libs/prompt-editor/src/models/prompt-editor-props.ts:125-162 — PromptEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat/pages/PromptEditor/PromptEditor.tsx |
| Test evidence | stamps the form column that holds the fields |
| Test evidence | renders the create heading by default |
08
Prompt editor
lib-prompt-editor-08

### Notes:
Slide ID: lib-prompt-editor-08

Actual consumers: apps/chat/src/pages/PromptEditor/PromptEditor.tsx. Existing test evidence: [{"file": "libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.classes.spec.tsx", "assertions": ["PromptEditor \u2014 public class names", "stamps the form column that holds the fields"]}, {"file": "libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.spec.tsx", "assertions": ["PromptEditor", "renders the create heading by default", "renders a flat form without section headings, a version field, or a folder picker", "renders the edit heading in edit mode", "seeds the fields from initialValues", "re-seeds the fields when initialValues arrives later", "submits the entered values", "does not validate on its own \u2014 the host owns the storage contract", "renders host-supplied inline errors", "blocks submission and announces status while saving", "renders a labelled spinner instead of the form while loading", "renders an error state with retry instead of an empty form on load failure", "omits the retry button when the host cannot retry", "calls onCancel without submitting", "calls the dedicated back callback from the header"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-prompt-editor:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/prompt-editor/README.md:1-160
libs/prompt-editor/src/index.ts:1-16
libs/prompt-editor/package.json:1-37
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310 — PromptEditor
libs/prompt-editor/src/models/prompt-editor-props.ts:125-162 — PromptEditorProps
apps/chat/src/pages/PromptEditor/PromptEditor.tsx:1-282
libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.classes.spec.tsx:1-39
libs/prompt-editor/src/components/PromptEditor/tests/PromptEditor.spec.tsx:1-247

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
No built-in folder picker
Stable initial values
Host validation
PromptEditor itself renders no folder field.
Changing their identity can reseed editing state.
Backend naming and storage rules do not belong in this form.
09
Prompt editor
lib-prompt-editor-09

### Notes:
Slide ID: lib-prompt-editor-09

Review these constraints before choosing the library. No built-in folder picker: PromptEditor itself renders no folder field. Stable initial values: Changing their identity can reseed editing state. Host validation: Backend naming and storage rules do not belong in this form. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/prompt-editor/README.md:1-160
libs/prompt-editor/src/index.ts:1-16
libs/prompt-editor/package.json:1-37
libs/prompt-editor/src/components/PromptEditor/PromptEditor.tsx:68-310 — PromptEditor
libs/prompt-editor/src/models/prompt-editor-props.ts:125-162 — PromptEditorProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.