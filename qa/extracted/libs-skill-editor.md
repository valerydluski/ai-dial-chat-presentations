<!-- Slide number: 1 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Skill editor
Edit a skill and its supporting file tree through host callbacks.

Problem and boundary
Public contract
Working integration
@epam/ai-dial-skill-editor
01
Skill editor
lib-skill-editor-01

### Notes:
Slide ID: lib-skill-editor-01

This session explains edit a skill and its supporting file tree through host callbacks. The library is a local private workspace package at libs/skill-editor. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.

Sources:
libs/skill-editor/README.md:1-176
libs/skill-editor/src/index.ts:1-23
libs/skill-editor/package.json:1-43
libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570 — SkillEditor
libs/skill-editor/src/models/skill-editor-props.ts:236-315 — SkillEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 2 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
When this library is useful
Edit a skill and its supporting file tree through host callbacks.

01
02
03
Author instructions
Attach supporting files
Resolve edits safely
Edit skill metadata and Markdown instructions.
Select, expand and manage a file tree.
Show validation and conflict state from the host.
02
Skill editor
lib-skill-editor-02

### Notes:
Slide ID: lib-skill-editor-02

Start with a concrete caller need. Author instructions: Edit skill metadata and Markdown instructions. Attach supporting files: Select, expand and manage a file tree. Resolve edits safely: Show validation and conflict state from the host. These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.

Sources:
libs/skill-editor/README.md:1-176
libs/skill-editor/src/index.ts:1-23
libs/skill-editor/package.json:1-43
libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570 — SkillEditor
libs/skill-editor/src/models/skill-editor-props.ts:236-315 — SkillEditorProps

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
Host skill state
Skill Editor
file Actions / submit
Host storage

Values, files and errors
Form and tree
Typed changes
Validate and commit
Library: Form editing, file-tree interaction and the protected root SKILL.md node.
03
Skill editor
lib-skill-editor-03

### Notes:
Slide ID: lib-skill-editor-03

The library owns Form editing, file-tree interaction and the protected root SKILL.md node. The host owns Path validation, upload/commit operations, ZIP/YAML serialization and persistence.  The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.

Sources:
libs/skill-editor/README.md:1-176
libs/skill-editor/src/index.ts:1-23
libs/skill-editor/package.json:1-43
libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570 — SkillEditor
libs/skill-editor/src/models/skill-editor-props.ts:236-315 — SkillEditorProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 4 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
The public contract to start with
SkillEditor · selected surface; full API index is in the bundle.
| Input or operation | Contract |
| --- | --- |
| files | SkillFileTreeNode[] |
| fileActions | SkillEditorFileActions |
| onSubmit | (values: SkillEditorValues) => void |
| conflict (optional) | SkillEditorConflict |
04
Skill editor
lib-skill-editor-04

### Notes:
Slide ID: lib-skill-editor-04

These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON.

Sources:
libs/skill-editor/README.md:1-176
libs/skill-editor/src/index.ts:1-23
libs/skill-editor/package.json:1-43
libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570 — SkillEditor
libs/skill-editor/src/models/skill-editor-props.ts:236-315 — SkillEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 5 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
A minimal workspace integration
TypeScript / React example · imports and host setup abridged.

<SkillEditor
  {...host}
  title="Create demo skill"
  initialValues={{
    name: 'demo-skill', description: 'Demo instructions',
  }}
/>
// host supplies files, fileActions and save/navigation callbacks.
Full example: examples/skill-editor.tsx · uses @epam/ai-dial-skill-editor
05
Skill editor
lib-skill-editor-05

### Notes:
Slide ID: lib-skill-editor-05

Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in examples/skill-editor.tsx. The stylesheet import must be loaded by the host. Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: Edit skill metadata and Markdown instructions. Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.

Sources:
libs/skill-editor/README.md:1-176
libs/skill-editor/src/index.ts:1-23
libs/skill-editor/package.json:1-43
libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570 — SkillEditor
libs/skill-editor/src/models/skill-editor-props.ts:236-315 — SkillEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 6 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Wire a realistic host workflow
Keep skill editor focused on its public responsibility.

01
02
03
Load skill inputs
Collect edits
Save the skill
Prepare metadata, files and the required file actions.
The editor returns changes through host callbacks.
The host performs persistence and handles navigation.
06
Skill editor
lib-skill-editor-06

### Notes:
Slide ID: lib-skill-editor-06

Follow this concrete integration sequence. Load skill inputs: Prepare metadata, files and the required file actions. Collect edits: The editor returns changes through host callbacks. Save the skill: The host performs persistence and handles navigation. The complete typed module in examples/skill-editor.tsx shows the required imports and host inputs. Application-owned network, routing and persistence behavior must be supplied by the caller.

Sources:
libs/skill-editor/README.md:1-176
libs/skill-editor/src/index.ts:1-23
libs/skill-editor/package.json:1-43
libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570 — SkillEditor
libs/skill-editor/src/models/skill-editor-props.ts:236-315 — SkillEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 7 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Available customization

01
02
03
File action interface
Conflict UI
Selection control
Validation and upload callbacks keep storage rules outside the view.
conflict and onReloadLatest support a host conflict workflow.
selectedPath and expandedPaths can be controlled externally.
07
Skill editor
lib-skill-editor-07

### Notes:
Slide ID: lib-skill-editor-07

Customization comes from the current exports and prop declarations. File action interface: Validation and upload callbacks keep storage rules outside the view. Conflict UI: conflict and onReloadLatest support a host conflict workflow. Selection control: selectedPath and expandedPaths can be controlled externally. For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.

Sources:
libs/skill-editor/README.md:1-176
libs/skill-editor/src/index.ts:1-23
libs/skill-editor/package.json:1-43
libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570 — SkillEditor
libs/skill-editor/src/models/skill-editor-props.ts:236-315 — SkillEditorProps

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 8 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Find the integration and its checks
Existing tests are evidence of intended behavior; suite results are not claimed.
| Evidence | Where to look |
| --- | --- |
| Real consumer | chat-hooks/src/skill/skill.ts |
| Test evidence | activates on drag-enter |
| Test evidence | renders nothing when not visible |
08
Skill editor
lib-skill-editor-08

### Notes:
Slide ID: lib-skill-editor-08

Actual consumers: libs/chat-hooks/src/skill/skill.ts; apps/chat/src/pages/SkillEditor/SkillEditor.tsx; libs/chat-hooks/src/skill/useSkillEditorSubmit.ts; libs/chat-hooks/src/skill/useSkillEditorLoad.ts; libs/chat-hooks/src/skill/useSkillFileActions.ts; libs/chat-hooks/src/skill/skill-file-batch-validation.ts. Existing test evidence: [{"file": "libs/skill-editor/src/hooks/tests/useSkillFileDropZone.spec.ts", "assertions": ["useSkillFileDropZone", "activates on drag-enter", "does not flicker to inactive on a nested drag-leave while still over the zone", "deactivates once the net enter count returns to zero", "calls preventDefault on dragover for a file drag", "ignores a non-file drag", "calls onFilesDropped with the dropped files and resets drag state"]}, {"file": "libs/skill-editor/src/components/SkillFileDropOverlay/tests/SkillFileDropOverlay.spec.tsx", "assertions": ["SkillFileDropOverlay", "renders nothing when not visible", "shows the default title and subtitle when visible", "renders host-supplied labels"]}]. Reproduce project checks from the repository root with npm exec nx run @epam/ai-dial-skill-editor:typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.

Sources:
libs/skill-editor/README.md:1-176
libs/skill-editor/src/index.ts:1-23
libs/skill-editor/package.json:1-43
libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570 — SkillEditor
libs/skill-editor/src/models/skill-editor-props.ts:236-315 — SkillEditorProps
libs/chat-hooks/src/skill/skill.ts:1-256
libs/skill-editor/src/hooks/tests/useSkillFileDropZone.spec.ts:1-84
libs/skill-editor/src/components/SkillFileDropOverlay/tests/SkillFileDropOverlay.spec.tsx:1-39

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.

<!-- Slide number: 9 -->

![assets/favicon.png](Image0.jpg)
AI DIAL  /  LIBRARY DEEP DIVE
Constraints that affect integration

01
02
03
Protected entry file
No archive writer
Async ownership
The root SKILL.md cannot be removed by the tree UI.
The host assembles the persisted skill representation.
Supply meaningful loading, submitting and error states.
09
Skill editor
lib-skill-editor-09

### Notes:
Slide ID: lib-skill-editor-09

Review these constraints before choosing the library. Protected entry file: The root SKILL.md cannot be removed by the tree UI. No archive writer: The host assembles the persisted skill representation. Async ownership: Supply meaningful loading, submitting and error states. The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.

Sources:
libs/skill-editor/README.md:1-176
libs/skill-editor/src/index.ts:1-23
libs/skill-editor/package.json:1-43
libs/skill-editor/src/components/SkillEditor/SkillEditor.tsx:76-570 — SkillEditor
libs/skill-editor/src/models/skill-editor-props.ts:236-315 — SkillEditorProps
AGENTS.md:1-176

Snapshot: 23fa39459d8971c10d5bd1c69734e61b124d249b; analysis 2026-09-21T18:14:40.584272+00:00. Working tree state is recorded in manifest.json.