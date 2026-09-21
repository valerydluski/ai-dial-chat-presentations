from pathlib import Path
import json,re,hashlib
ROOT=Path('../ai-dial-chat').resolve();OUT=Path('.');M=json.loads(Path('manifest.json').read_text());SNAP=M['snapshot'];D={}

def spec(slug,title,primary,purpose,scenario,owns,host,flow,features,limits,contract=None,notes=''):
 D[slug]=dict(title=title,primary=primary,purpose=purpose,scenario=scenario,owns=owns,host=host,flow=flow,features=features,limits=limits,contract=contract,notes=notes)

spec('attachment-input','Attachment input','AttachmentTray','Turn file state into clear attachment controls.',
 ['Compose with files|Show files before sending a message.','Recover from failure|Expose remove and retry actions per attachment.','Reuse sent-file UI|Render image groups and file rows in transcripts.'],
 'Cards, trays, file-drop affordances and clipboard handling.', 'Upload transport, progress state, validation policy and preview URLs.',
 ['Host file state|DisplayAttachment[]','AttachmentTray|Cards and actions','Callback|Attachment identifier','Host update|Retry or remove'],
 ['Tray and group|Use AttachmentTray while composing; AttachmentGroup for sent files.','Lazy previews|Image loading has an observable loading and error lifecycle.','Accessible actions|Supply localized open, retry, remove and upload labels.'],
 ['No uploader in a card|Showing progress does not perform the network upload.','Watch callback shapes|Tray actions use an id; message bubble callbacks can use an object.','Keep state ownership clear|The library has local UI state; the host owns durable file state.'],['attachments','onRemove','onRetry','labels'])
spec('attachment-canvas','Attachment canvas','AttachmentCanvas','Preview heterogeneous content through one typed surface.',
 ['Inspect evidence|Open a cited PDF or uploaded text beside a conversation.','Choose a renderer|A content discriminator selects the appropriate view.','Extend a workspace|Add visualizers or MCP content through explicit inputs.'],
 'Viewer selection, panel layout, lazy renderer loading and optional canvas context.', 'File access, resolved content, authorization, deployment settings and download behavior.',
 ['Host resolver|Content or access failure','Typed content|AttachmentContentType','AttachmentCanvas|Lazy viewer','User action|Close, copy or download'],
 ['Typed content variants|Plain text, code, Markdown, PDF, OOXML, media, HTML and MCP views.','Optional shared context|AttachmentCanvasProvider and useAttachmentCanvas coordinate a canvas.','Host loading hooks|loadPdf and configurePdfWorker support caller-controlled PDF setup.'],
 ['Heavy renderers|PDF, Office, syntax and MCP dependencies affect packaging; several load lazily.','Content errors differ|Unsupported, forbidden and failed loads have distinct display states.','Untrusted content|HTML and MCP views require the documented sandbox and host settings.'],['content','isOpen','onClose','labels'], 'The direct AttachmentCanvas example is controlled and does not require a provider. The provider is needed for useAttachmentCanvas and the context-based opening flow. The host must supply authenticated loading rather than passing session knowledge into ordinary UI code.')
spec('builder-form','Builder form','EditorLayout','Give entity editors a shared structure and validation vocabulary.',
 ['Build an editor|Compose metadata and setup sections in a consistent page.','Share field rules|Use one validator for name and version policies.','Localize metadata|Edit additional deployment names and descriptions by locale.'],
 'Editor shells, field controls and pure validation error codes.', 'Save behavior, routing, translated errors, avatar resolution and file access.',
 ['Host values|Metadata and labels','Editor controls|Field changes','Validation codes|Required or invalid','Host adapter|Translate and persist'],
 ['Layout composition|EditorLayout exposes leftContent, rightContent and actions.','Metadata fields|DeploymentCreationForm includes avatar, version, topics and locales.','Policy switches|Name and version pattern checks are opt-in validator options.'],
 ['Avatar ownership|Resolve iconPreviewUrl and open file selection in the host.','Locale visibility|DeploymentLocalesField hides when no locale options are supplied.','State is mixed|Some controls manage transient state; persistence remains outside.'],['title','onBack','leftContent','rightContent'])
spec('catalog','Catalog','Catalog','Browse deployments and reusable assets without owning their storage.',
 ['Find a deployment|Search, filter and compare models or applications.','Inspect details|Show capabilities, tools, pricing and limits.','Act on a selection|Pick, favorite, share or publish through host callbacks.'],
 'Catalog display, search/filter interactions and composed detail surfaces.', 'Data loading, action permissions, routes, configured API clients and deployment mapping.',
 ['Host adapter|CatalogItem[]','Catalog|Grid or list','Detail request|Item and selected tab','Host action|Use, share or publish'],
 ['Two view modes|Card and list views window visible rows.','Headless subpath|The /mapping entry exposes catalog mapping helpers and enums.','Action policies|Callbacks and visibility predicates control available item actions.'],
 ['Large prop surface|Configure the actions required by the host workflow.','Dependency boundary|The implementation uses the UI Kit grid and catalog/publish composition.','Source beats old docs|Do not copy the README peer list without checking package.json.'],['items','favorites','onUseInChat','onToggleFavorite'])
spec('conversation-input','Conversation input','ConversationInput','Compose a message with deployment, attachment and voice controls.',
 ['Send a message|Collect text and attachments, then invoke a host callback.','Control generation|Swap sending for a stop action while streaming.','Support rich input|Wire deployment selection, settings and audio transcription.'],
 'Composer interaction, local text/attachment state and input controls.', 'Model data, upload and transcription services, sending and generation state.',
 ['User input|Text, files or voice','ConversationInput|Local composition','onSend|Text and attachments','Host workflow|Persist and stream'],
 ['Controlled updates|messageRevision and textInsertion coordinate host-driven edits.','Separate attachment UI|Import attachment cards and trays from attachment-input.','Voice extension|Inject a transcription callback and supported deployment data.'],
 ['No completion client|onSend is the integration point for a real generation flow.','Provider assumptions|Feature-specific settings and menus need caller-supplied data.','Avoid state resets|Keep initialization and host insertion changes intentional.'],['onSend','onUploadAttachment','isStreaming','onStop'])
spec('conversation-messages','Conversation messages','AssistantMessageBubble','Render a transcript from host-owned messages and actions.',
 ['Display roles|Use user, assistant and status bubble variants.','Reveal a response|Render updated Markdown while a generation is active.','Compose evidence|Place stages, citations and attachments beside the answer.'],
 'Bubble layout, Markdown display and action controls.', 'Message ordering, network streams, persistence, ratings and attachment access.',
 ['Host message|Text and display props','Assistant bubble|Markdown and slots','User action|Copy, rate or regenerate','Host callback|Perform domain behavior'],
 ['Extension slots|beforeContent and afterContent add skill chips or stage panels.','Host URL rewriting|markdownUrlTransform maps resource references before rendering.','Transcript controls|Supply MessageActions props and localized action labels.'],
 ['Streaming is visual|isStreaming does not open a network stream.','Status messages|Shared MessageRole.Status is a UI event, not an upstream author role.','Source integrations|Citation components and canvas actions require host wiring.'],['text','isStreaming','afterContent','onAttachmentClick'])
spec('conversation-panel','Conversation panel','ConversationPanel','Navigate a large conversation history with a small visible list.',
 ['Resume work|Select a conversation from a grouped history list.','Find context|Search titles and filter by source.','Manage history|Expose rename, move, pin and transfer actions.'],
 'Windowed rows, grouping, search UI and per-row interaction.', 'Ordered data, active route, storage changes and action implementations.',
 ['Host history|ConversationItem[]','ConversationPanel|Grouped visible rows','Selection or move|Id or ConversationMove','Host state|Navigate and persist'],
 ['Stable row data|Items carry title, source, pinned state and optional unread/task badges.','Action extension|getActions and onActionMenuOpen inject row actions.','Transfer surfaces|ImportExportQueue and RenameConversationPopup are separate exports.'],
 ['Preserve ordering|The host supplies an already-ordered flat list.','Selection is not routing|onSelectConversation returns an id for the host to interpret.','Virtualized content|Only a subset of rows exists in the DOM at a time.'],['conversations','onSelectConversation','onNewChat','labels'])
spec('conversation-stages','Conversation stages','StagesPanel','Make streamed execution progress visible inside a response.',
 ['Explain waiting|Show named running stages while content arrives.','Inspect a step|Expand stage Markdown and copy useful details.','Reduce noise|Collapse related work into a compact group.'],
 'Stage display, expansion, status icons and Markdown details.', 'Receiving and merging stage updates, status truth and generation lifecycle.',
 ['Stream consumer|Merge stage updates','Stage[]|Index, name, status','StagesPanel|Progress display','User inspection|Expand or copy'],
 ['Explicit running state|null status represents a running stage in the shared Stage model.','Streaming awareness|isStreaming controls the active presentation lifecycle.','Grouped detail|CollapsedGroup provides a compact wrapper for related stages.'],
 ['Progress is supplied|The component cannot infer the backend work completed.','Keep identity stable|Stage index is used when upstream updates are merged.','Content sensitivity|Only pass execution details intended for the user to see.'],['stages','isStreaming','labels','styles'])
spec('navigation-panel','Navigation panel','NavigationPanel','Reuse navigation destinations across desktop and mobile chrome.',
 ['Navigate an app|Render a desktop destination rail.','Use a phone|Show destinations and settings inside a bottom sheet.','Declare settings once|Share menu groups across rail menus and mobile pages.'],
 'Rail, user menu, mobile sheet and its local page stack.', 'Routes, authentication, active destination, labels and resolved brand assets.',
 ['Host destinations|Items and active flags','Navigation surface|Rail or sheet','renderLink / callback|Host-owned behavior','Host route|Selected destination'],
 ['Router integration|renderLink wraps destination children with the host link element.','Mobile stack|NavigableBottomSheet and useSheetNavigation manage drill-down pages.','Shared menus|NavigationMenuGroup describes selectable settings options.'],
 ['Responsive selection|The host chooses which surface to render.','No login system|UserMenu displays supplied profile data and callbacks.','Explicit logos|Resolve logo URLs before passing them into NavigationPanel.'],['items','labels','renderLink','footer'])
spec('sidebar','Sidebar','SidebarPanel','Give feature panels a common resizable shell.',
 ['Add a panel|Compose a header, actions and scrollable content.','Resize a workspace|Use a bounded width with a resize callback.','Handle empty data|Use PanelEmpty or PanelNoResults consistently.'],
 'Panel structure, resize interaction, visibility and empty-state primitives.', 'Content, search, durable width storage and feature actions.',
 ['Host layout|Open state and content','SidebarPanel|Header and resize','onResizeStop|Width in pixels','Host state|Store or reuse width'],
 ['Logical placement|SidebarOrientation selects the desired panel side.','Header slots|leftActions and rightActions are public API slot names.','Width bounds|defaultWidth, minWidth and maxWidth configure resizing.'],
 ['No built-in search|Compose search in children or header actions.','Persistence is external|onResizeStop reports width; the host decides where to save it.','Contextual visibility|Keep the parent layout and isOpen state synchronized.'],['isOpen','orientation','children','onResizeStop'])
spec('settings-panel','Settings panel','SettingsPanel','Provide accessible vertical selection for settings pages.',
 ['Switch settings|Render a compact navigation list beside host content.','Use a keyboard|Move among enabled rows with arrows, Home and End.','Keep one selection|The host controls activeId.'],
 'Vertical tab interactions, focus movement and selected styling.', 'Settings content, active state, item labels and navigation effects.',
 ['Host items|Ids and labels','SettingsPanel|Roving focus','onSelect|Selected id','Host content|Show the matching tab'],
 ['Disabled rows|Keyboard navigation skips disabled items.','Automatic activation|Focus movement also invokes selection.','Single item state|One selected row uses a neutral visual treatment.'],
 ['Panel content is external|Selection does not create or load a settings page.','Keep ids coherent|activeId must correspond to the intended item.','No route knowledge|A route change is the host onSelect implementation.'],['items','activeId','onSelect','sectionLabel'])
spec('starter-buttons','Starter buttons','StarterButtons','Offer prompt starters that fit the available space.',
 ['Start a conversation|Expose useful first actions before the user types.','Handle narrow screens|Move excess choices to the overflow menu.','Keep behavior explicit|The host decides what a selected starter does.'],
 'Starter layout, available-space measurement and overflow controls.', 'Starter data, mobile mode when supplied and send/populate behavior.',
 ['Host deployment|StarterOption[]','StarterButtons|Visible and overflow','onSelect|Whole StarterOption','Host composer|Populate or submit'],
 ['Responsive overflow|Measured space determines which options remain visible.','Collapse policy|isCollapsible changes the overflow behavior.','Accessible names|labels names the list and the overflow action.'],
 ['Use the actual shape|StarterOption includes const and dial:widgetOptions.','No completion side effect|Selecting emits a value; the host controls submission.','Layout needs space|Render inside the actual constrained input area.'],['starters','onSelect','labels','isCollapsible'])
spec('source-panel','Source panel','ConversationSourcesPanel','Put uploaded files, generated files and citations in one evidence panel.',
 ['Find evidence|Inspect source material beside the conversation.','Search by name|Narrow attachments and source labels.','Open a reference|Delegate preview or download to the host.'],
 'Evidence sections, filtering and attachment/source interactions.', 'Source derivation, authenticated downloads and canvas loading.',
 ['Host derivation|Files and quotations','Sources panel|Search and sections','Click callback|Source or attachment','Host resolver|Open the right content'],
 ['Separate collections|uploaded, generated and sources retain their distinct roles.','Panel customization|Width bounds, labels and additionalSections are explicit inputs.','Matched text|Search results use the shared highlighting convention.'],
 ['No implicit fetching|Opening a row needs a host callback.','Required labels|The panel contract requires the complete labels object.','Boundary drift|The README peer list differs from current package composition.'],['uploaded','generated','sources','onSourceClick'])
spec('quotations','Quotations','CitationMarker','Connect answer annotations to inspectable evidence.',
 ['Mark a claim|Show an inline source marker in an answer.','Group evidence|Group annotations by source or citation id.','Jump to context|Derive PDF or Office highlight locations.'],
 'Annotation utilities, citation presentation and optional citation state.', 'Fetching sources, opening viewers, Markdown pipeline integration and localized labels.',
 ['Host message|Annotations and references','Grouping helpers|Source or citation id','CitationMarker|Accessible source control','Host opener|Viewer and highlight'],
 ['Multiple citation forms|Utilities support offset annotations and paired cit tags.','Markdown composition|useCitationMarkdownComponents builds citation renderers.','Viewer locations|Helpers derive PDF and supported Office highlight coordinates.'],
 ['Wire the pipeline|Allowed cit tags and renderer overrides must agree.','Streaming fragments|Incomplete citation tags need streaming-aware handling.','No source download|Callbacks and resolvers connect the marker to actual evidence.'],['sourceName','annotationCount','onOpen','labels'])
spec('prompt-editor','Prompt editor','PromptEditor','Author reusable prompt content while leaving persistence to the host.',
 ['Create a prompt|Edit name, description and Markdown content.','Revise a prompt|Seed the form with stable initialValues.','Add folder controls|Compose PromptFolderField separately when needed.'],
 'Prompt form fields, editing state and optional folder-field UI.', 'Save/load operations, validation errors, routes and folder mutations.',
 ['Host load|Initial values and errors','PromptEditor|Local editing','onSubmit|PromptEditorValues','Host save|Validate and persist'],
 ['Load and save states|isLoading, hasLoadError and isSaving drive the form experience.','Editor customization|Pass labels, limits and markdownEditorTheme.','Separate folder field|PromptFolderField delegates mutations through folderActions.'],
 ['No built-in folder picker|PromptEditor itself renders no folder field.','Stable initial values|Changing their identity can reseed editing state.','Host validation|Backend naming and storage rules do not belong in this form.'],['onSubmit','onCancel','initialValues','errors'])
spec('prompts','Prompts','PromptParametersPopup','Pick reusable prompts and collect their parameter values.',
 ['Choose a favorite|Browse FavoritePromptItem data supplied by the host.','Fill placeholders|Collect values for named prompt parameters.','Populate a composer|Resolve values and pass the text to host input state.'],
 'Favorite prompt selection and parameter-entry UI.', 'Loading favorites, deriving parameters, resolving submitted values and sending text.',
 ['Favorite selection|Prompt content','Parameter popup|Named input fields','onSubmit|Record of values','Host resolver|Resolve and insert text'],
 ['Favorite callbacks|Selection, favorite changes and browse actions are caller-owned.','Default values|Shared helpers support tokens with a default value.','Explicit popup state|open, onClose and onCancel are controlled by the host.'],
 ['Submission is values|PromptParametersPopup returns a value map, not a sent message.','Use shared helpers|extractPromptParams and resolvePromptParams implement token semantics.','Syntax matters|Double braces define parameters; ordinary braces remain literal.'],['content','parameters','onSubmit','open'])
spec('skill-editor','Skill editor','SkillEditor','Edit a skill and its supporting file tree through host callbacks.',
 ['Author instructions|Edit skill metadata and Markdown instructions.','Attach supporting files|Select, expand and manage a file tree.','Resolve edits safely|Show validation and conflict state from the host.'],
 'Form editing, file-tree interaction and the protected root SKILL.md node.', 'Path validation, upload/commit operations, ZIP/YAML serialization and persistence.',
 ['Host skill state|Values, files and errors','SkillEditor|Form and tree','fileActions / submit|Typed changes','Host storage|Validate and commit'],
 ['File action interface|Validation and upload callbacks keep storage rules outside the view.','Conflict UI|conflict and onReloadLatest support a host conflict workflow.','Selection control|selectedPath and expandedPaths can be controlled externally.'],
 ['Protected entry file|The root SKILL.md cannot be removed by the tree UI.','No archive writer|The host assembles the persisted skill representation.','Async ownership|Supply meaningful loading, submitting and error states.'],['files','fileActions','onSubmit','conflict'])
spec('skills','Skills','FavoriteSkillsPanel','Select a reusable skill without coupling the picker to sending.',
 ['Choose a favorite|Select a host-resolved favorite skill.','Inspect a skill|Open a host-backed detail panel.','Attach context|Display a selected skill chip next to the composer.'],
 'Favorite list, chip, details composition and selection-overlay state.', 'Skill listing, favorites persistence, capability flag and send-time semantics.',
 ['Host listing|FavoriteSkillItem[]','Skills picker|Select or inspect','Selected skill|Chip and detail state','Host send|Interpret the selection'],
 ['Overlay state hook|useSkillSelectorOverlay coordinates favorites, browse and details.','Capability input|A plain support flag controls skill entry points.','Composable detail view|SkillDetailsSidePanel uses the catalog DetailsPanel contract.'],
 ['Unsupported deployment|A selected chip can remain visible in its error state.','No automatic attachment|The host decides how a skill enters the request.','Keep identifiers intact|The favorite item id is the resource identifier supplied by the host.'],['favorites','onSelect','onViewDetails','onBrowse'])
spec('toolset-editor','Toolset editor','ToolsetEditor','Coordinate MCP toolset editing through an explicit host adapter.',
 ['Create a toolset|Edit metadata, endpoint, transport and authentication settings.','Persist a draft|Reuse the identifier returned by the first successful save.','Authorize access|Delegate login and OAuth to host behavior.'],
 'Form state, dirty/errors state and save orchestration around injected operations.', 'HTTP persistence, OAuth execution, credentials APIs, routes and file-manager integration.',
 ['Editor form|Metadata and setup','onPersist|Create or update','Host authentication|Post-save login / OAuth','Completion callbacks|Refresh and navigate'],
 ['Typed integration|ToolsetEditorProps makes persistence, auth and file dependencies explicit.','Shared metadata|GeneralForm reuses builder-form fields and validation.','MCP URL resolver|buildMcpUrl receives the current draft identifier.'],
 ['No minimal fake backend|A working editor needs the required host callbacks and file component.','Form identity|A new initialForm object reseeds the editing session.','Boundary discrepancy|Current code imports chat-hooks symbols; document this wider dependency.'],['initialForm','onPersist','onOAuthLogin','authActions'])
spec('scheduled-tasks','Scheduled tasks','ScheduledTasks','Render task lists, forms and run history from host-owned schedules.',
 ['Browse automation|Search and sort scheduled task cards.','Create or edit|Collect schedule form values and validation errors.','Inspect execution|Display a task summary and past run statuses.'],
 'List/form/detail UI and user interactions.', 'Scheduling APIs, formatted dates, timezone decisions, sorting/filtering and validation.',
 ['Host task adapter|Preformatted items','ScheduledTasks|Cards and toolbar','Search / sort callback|Query or enum','Host update|Derive next item set'],
 ['List pagination|hasMore, isLoadingMore and onLoadMore support incremental loading.','Form and detail exports|ScheduledTaskCreateForm and ScheduledTaskDetailView are distinct surfaces.','Run status display|ScheduledTaskRunHistoryList renders host-provided run records.'],
 ['No task scheduler|Rendering a schedule does not execute work in the background.','Formatting stays outside|Pass already-formatted labels and timestamps.','Filter intentionally|The controlled search/sort contract requires host updates.'],['items','searchQuery','sortKey','labels'])
spec('share','Share','SharePopover','Present a share link and access choices without issuing the link.',
 ['Share a resource|Show a link or a scannable QR view.','Represent access|Display view/edit access values as a list.','Handle pending work|Show host loading and failure states.'],
 'Link/QR presentation, copy interactions and access controls.', 'Creating or replacing links, permissions and share-URL resolution.',
 ['Host share API|URL and access','SharePopover|Link or QR view','onAccessChange|Access-level array','Host request|Issue a matching link'],
 ['Typed access|ShareLinkAccess represents view and edit levels.','Separate QR component|QrCode can be used outside the popover.','Explicit errors|url may be undefined while loading; error is supplied separately.'],
 ['Access is not cosmetic|Real access changes require the host to request the appropriate link.','No permission enforcement|canEditAccess controls UI, not backend authorization.','Named root export|Import SharePopover by name from the package entry.'],['url','access','onAccessChange','canEditAccess'])
spec('publish-panel','Publish panel','PublishPanel','Reuse the publish-to-folder workflow across different entity types.',
 ['Choose a destination|Search and select a publication folder.','Explain history|Show earlier publications before replacing or versioning.','Share one workflow|Use the same panel for deployments and conversations.'],
 'Folder/history UI and a generic publish-flow state helper.', 'Folder loading, write permissions, publish requests and domain-specific resource mapping.',
 ['Host resources|Folders and history','PublishPanel|Destination and rules','Flow callbacks|Create folder / submit','Host API|Persist publication'],
 ['Generic summary|resource and renderSummary avoid requiring a catalog-specific model.','State helper|usePublishFlow coordinates selection and submission state.','Access-rule controls|Author, rules and rule-source options are explicit inputs.'],
 ['Permission truth|hasWriteAccess must come from a host authorization decision.','Folder mutations|onCreateFolder is asynchronous and can fail.','Version semantics|The host decides whether replacement or a new version is appropriate.'],['folderItems','onCreateFolder','rules','hasWriteAccess'])
spec('usage-dashboard','Usage dashboard','UsageLimitCard','Explain cost and model limits using normalized display data.',
 ['Inspect a budget|Display used, remaining and total amounts.','Compare periods|Show the current UTC day, week and month.','Find constraints|Compare model-token and overall cost limit statuses.'],
 'Usage cards/tables plus exported mapping utilities.', 'Fetching usage, choosing locale/timezone formatting and passing resolved display values.',
 ['Host usage API|Raw counters and limits','Mapping helpers|Display rows and labels','Usage dashboard|Cards and model table','User review|Understand active limits'],
 ['Semantic states|UsageLimitStatus distinguishes normal, warning and reached states.','Accessible progress|Supply preformatted progressAriaLabel and reset text.','Mapping exports|mapUsageDataToDashboard and model-limit mappers are public.'],
 ['Calendar periods|Today/week/month are calendar windows, not rolling durations.','Separate component and helper|Cards consume display data; exported helpers do perform mapping.','Isolation discrepancy|Mapping source imports generated API DTOs outside the documented exception.'],['data','labels','styles'])
spec('mcp-apps','MCP Apps','McpAppInlinePreview','Connect tool-result UI resources to an inline interactive preview.',
 ['Find a tool UI|Match a message to an MCP tool resource.','Reuse the result|Seed the preview from the original tool call.','Expand the UI|Open the matched application in the attachment canvas.'],
 'Preview state, matching/seed helpers and a per-conversation response cache.', 'Configured resource/tool calls, sandbox URL, host context and expansion behavior.',
 ['Tool evidence|Match and call seed','Response cache|Resource HTML + result','Inline preview|Sandboxed MCP renderer','Host adapter|Calls and expansion'],
 ['Explicit host adapter|Inject fetchResourceHtml, callTool, hostInfo and sandboxUrl.','Cache identity|Entries are checked against seed identity and expiry.','Lifecycle state|Loading, Ready, Error and Unavailable are distinct enum values.'],
 ['Origin isolation required|Configure the separate MCP sandbox deployment.','Avoid duplicate side effects|Indirectly discovered tools are not safe to re-call blindly.','Not a general API client|Backend operations enter through the host adapter.'],['match','cache','hostAdapter','toolCall'])
spec('chat-shared','Chat shared','buildCssVars','Share domain vocabulary, utilities and common UI primitives.',
 ['Agree on shapes|Use the same message, stage and attachment types.','Reuse common UI|Share Markdown, icons and resource summaries.','Bridge file managers|Use a typed controller without host persistence knowledge.'],
 'Shared models, pure utilities, UI primitives and narrow file-manager event bindings.', 'App providers, authentication, routing, storage keys and external-system configuration.',
 ['Host domain|Resolved values','Shared contracts|Types and utilities','Feature library|Consistent interpretation','Host composition|One application view'],
 ['Focused entries|/markdown and /file-manager expose narrower entry points.','CSS variable builder|buildCssVars drops undefined and empty values.','Canonical grid hook|useGridEditingScroll lives here and is re-exported by chat-hooks.'],
 ['More than types|The source includes runtime utilities and rendered UI.','Entry-specific peers|The file-manager entry needs its optional peer pair installed.','Legacy boundary assumptions|The old no-dependencies description is not the current graph.'],None)
spec('chat-hooks','Chat hooks','useShareLink','Reuse headless request lifecycles and chat-interface behavior.',
 ['Build a custom chat|Reuse stream state, scrolling and attachment behavior.','Keep rendering separate|Connect returned data and callbacks to your own UI.','Limit imports|Use the dependency-focused public subpaths.'],
 'Reusable hook state, data mapping and permitted thin operation wrappers.', 'Configured clients, authentication setup, routing, app contexts and translated labels.',
 ['Host configuration|Injected API instance','Headless hook|Lifecycle and state','Return values|Data, loading, errors','Host UI|Render and respond'],
 ['Small layout entry|/viewport-layout includes useViewportWidth with listener cleanup.','Request lifecycle|useShareLink manages link loading, access changes and stale response guards.','Broad feature entries|Conversation, files, catalog, OAuth and MCP have explicit subpaths.'],
 ['Stable dependencies|Recreating API instances can retrigger effects.','Browser assumptions|Some hooks use browser globals; pass origin explicitly for share examples.','Boundary audit needed|Some current helpers contain more DIAL-specific knowledge than the narrow rule.'],None)
spec('chat-api-client','Chat API client','DeploymentsApi','Generate typed operations from the backend OpenAPI contract.',
 ['Call the BFF|Use typed API classes from application adapters.','Evolve an endpoint|Change Swagger/DTO sources, then regenerate.','Inspect transport details|Use Raw operations when headers or the Response are needed.'],
 'Generated endpoint paths, DTOs, serializers and Fetch transport runtime.', 'Base URL, credentials, CSRF policy, middleware and application error presentation.',
 ['Nest controllers|Swagger and DTOs','OpenAPI document|Generator input','Generated client|Typed operations','App adapter|Configured calls'],
 ['Normal vs Raw|Normal methods resolve values; Raw methods expose the response wrapper.','Configurable transport|Configuration accepts basePath, credentials and middleware.','Regeneration scripts|npm run openapi and openapi:check maintain the checked-in artifacts.'],
 ['Never hand-edit generated code|Regeneration overwrites manual client edits.','Real API names|Use DeploymentsApi; the README ModelsApi example is stale.','Streaming needs care|Host adapters handle documented raw stream/DTO gaps.'],None)
spec('chat-overlay','Chat overlay','ChatOverlay','Embed a running chat with a typed message protocol.',
 ['Embed a full experience|Mount the chat iframe in a host-owned region.','Control conversations|Set input, send requests and subscribe to events.','Offer floating widgets|Use ChatOverlayManager for toggle/fullscreen chrome.'],
 'Iframe lifecycle, protocol handshake, request correlation and optional widget chrome.', 'Chat deployment, allowed origins, identity-provider policy and host page lifecycle.',
 ['Host page|ChatOverlay instance','Readiness handshake|READY_TO_INTERACT','Embedded chat|Handle typed requests','Events and results|Correlated host callbacks'],
 ['Framework-independent|The overlay implementation uses DOM/TypeScript rather than React.','Lifecycle contract|Await ready, subscribe deliberately and destroy on unmount.','Two integration levels|Direct overlay for a container; manager for floating widgets.'],
 ['Embedding policy|The server must allow the host origin in frame-ancestors.','Auth constraints|Provider iframe behavior varies; configure supported login UI modes.','No server replacement|The overlay still needs a running chat and backend.'],None)

# Every source locator includes a real range from the analyzed working tree.
def source(file,symbol=None):
 p=ROOT/file
 if not p.exists():raise ValueError(file)
 lines=p.read_text().splitlines();start=1;end=len(lines)
 if symbol:
  hits=[i for i,l in enumerate(lines) if symbol in l]
  if hits:start=max(1,hits[0]-2);end=min(len(lines),hits[0]+60)
 return dict(file=file,start=start,end=end,**({'symbol':symbol} if symbol else {}))
def cards(entries):
 return [dict(title=x.split('|',1)[0],body=x.split('|',1)[1]) for x in entries]
def s(id,title,layout='cards',**kw):return dict(id=id,title=title,layout=layout,**kw)
def read_d(slug):return json.loads(Path(f'content/research/{slug}.json').read_text())
def contract(d,name):return next((x for x in sum(d.get('contracts',{}).values(),[]) if x['name']==name),{})
def refs(d,cfg):
 c=contract(d,cfg['primary']);a=[source(d['project']['path']+'/README.md'),source(d['project']['path']+'/src/index.ts'),source(d['project']['path']+'/package.json')]
 if c.get('file'):a.append(dict(file=c['file'],start=c['start'],end=c['end'],symbol=cfg['primary']))
 if c.get('props'):
  for x in sum(d['contracts'].values(),[]):
   if x['name']==cfg['primary']+'Props' and x.get('file'):a.append(dict(file=x['file'],start=x['start'],end=x['end'],symbol=x['name']))
 return a

def build_library(slug,cfg):
 d=read_d(slug);base='lib-'+slug;ss=refs(d,cfg);ex=Path('examples')/(slug+('.ts' if slug in ['chat-api-client','chat-overlay'] else '.tsx'));code=ex.read_text();scope=d['project']['package'];component=cfg['primary'];c=contract(d,component)
 # Display an explicitly abridged, readable excerpt; full source remains alongside the deck.
 lines=code.splitlines();begin=next((i for i,l in enumerate(lines) if l.startswith('export function') or l.startswith('export async function')),0);excerpt='\n'.join(lines[begin:begin+11]);excerpt=re.sub(r'export (async )?function',lambda m:(m.group(1) or '')+'function',excerpt)
 # Keep wide signatures/imports out of slide code; curated excerpts override below.
 excerpts={
 'chat-api-client':"const api = new DeploymentsApi(\n  new Configuration({\n    basePath: '',\n    credentials: 'include',\n  }),\n);\nconst deployments = await api.listDeployments();",
 'chat-shared':"const style = buildCssVars({\n  '--text-primary': '#EDF2F7',\n  '--unused': undefined,\n});\n// Undefined values are omitted.\nconst role = MessageRole.Assistant;",
 'chat-hooks':"function ViewportDemo() {\n  const width = useViewportWidth();\n  return <p>Demo viewport: {width}px</p>;\n}\n// Import from /viewport-layout.\n// The hook removes its resize listener on cleanup.",
 'chat-overlay':"const overlay = new ChatOverlay('#demo-chat', {\n  domain: 'https://chat.example.com',\n  theme: 'dark',\n});\nawait overlay.ready();\nawait overlay.setInputContent('Explain the architecture');\n// On host teardown:\noverlay.destroy();",
 'attachment-canvas':"<AttachmentCanvas\n  isOpen={open}\n  onClose={() => setOpen(false)}\n  content={{\n    type: AttachmentContentType.PlainText,\n    text: 'Demo evidence',\n  }}\n  labels={{ ariaLabel: 'Demo preview' }}\n/>",
 'conversation-panel':"<ConversationPanel\n  isOpen\n  conversations={[{ id: 'demo', title: 'Demo chat' }]}\n  activeConversationId={active}\n  onSelectConversation={setActive}\n  onNewChat={onNewChat}\n  labels={labels}\n/>",
 'source-panel':"<ConversationSourcesPanel\n  isOpen isMobile={false}\n  onClose={onClose}\n  uploaded={[]} generated={[]}\n  sources={sources}\n  labels={labels}\n  onSourceClick={onOpen}\n/>",
 'prompts':"<PromptParametersPopup\n  open={open} promptName=\"Demo summary\"\n  content=\"Summarize {{topic}}\"\n  parameters={[{ name: 'topic' }]}\n  onClose={close} onCancel={close}\n  onSubmit={values => {\n    onText(resolvePromptParams(content, values));\n  }}\n/>",
 'usage-dashboard':"<UsageLimitCard labels={labels} data={{\n  title: 'Today', periodDescription: 'Today',\n  used: 3, total: 10,\n  usedLabel: '$3', totalLabel: '$10',\n  remainingLabel: '$7', usedPercent: 30,\n  status: UsageLimitStatus.Default,\n  progressAriaLabel: 'Demo: 3 of 10, 30 percent used',\n}} />",
 'mcp-apps':"const cache = useMcpAppResponseCache('demo-conversation');\n<McpAppInlinePreview\n  match={match} cache={cache} cacheKey=\"demo-message\"\n  hostAdapter={adapter} onExpand={onExpand}\n  expandAriaLabel=\"Expand demo app\"\n  reloadAriaLabel=\"Reload\"\n  loadErrorLabel=\"Could not load demo app\"\n  openedInCanvasLabel=\"Open in preview\"\n/>",
 'toolset-editor':"function ToolsetEditorDemo(host: ToolsetEditorProps) {\n  return <ToolsetEditor {...host} />;\n}\n\n// host includes required persistence, authentication,\n// notification, file-manager and navigation callbacks.\n// See the complete contract in content/api-index.md."
 }
 excerpt=excerpts.get(slug,excerpt)
 # Wrap hand-authored snippets only at safe whitespace; mark all as excerpts.
 if any(len(l)>83 for l in excerpt.splitlines()):
  excerpt='\n'.join(lines[begin:begin+8])
 slides=[s(base+'-01',cfg['title'],'cover',subtitle=cfg['purpose'],chips=['Problem and boundary','Public contract','Working integration'],caption=scope,notes=f"This session explains {cfg['purpose'].lower()} The library is a local private workspace package at {d['project']['path']}. Its manifest, source exports, tests and actual consumers were inspected. Package publication has not been verified; use the workspace integration shown here.",sources=ss),
 s(base+'-02','When this library is useful',kicker=cfg['purpose'],cards=cards(cfg['scenario']),notes='Start with a concrete caller need. '+ ' '.join(x.replace('|',': ') for x in cfg['scenario'])+' These scenarios describe integration supported by the current public surface; they do not assert measured performance or production certification.',sources=ss),
 s(base+'-03','Follow the ownership boundary','flow',kicker='Inputs and effects stay explicit.',nodes=cards(cfg['flow']),takeaway='Library: '+cfg['owns'],notes='The library owns '+cfg['owns']+' The host owns '+cfg['host']+' '+cfg['notes']+' The arrows show data/callback direction, not an implicit network request. The documented isolation rules and known implementation deviations are listed in qa-report.md.',sources=ss+[source('AGENTS.md')]),
 ]
 props={p['name']:p for p in c.get('props',[])}
 if cfg['contract']:
  rows=[]
  for name in cfg['contract'][:4]:
   p=props.get(name);typ=(p or {}).get('type','See exported type');typ=re.sub(r'import\("[^"]+"\)\.', '',typ);typ=typ.replace(' | undefined','');typ=typ[:65] if len(typ)>65 else typ;rows.append([name+(' (optional)' if p and p['optional'] else ''),typ])
 else:
  special={
   'chat-shared':[['MessageRole / Stage','Shared enums and domain records'],['buildCssVars(vars)','CSSProperties, omitting empty values'],['/markdown','MarkdownRenderer and related exports'],['/file-manager','Shell, controller types and bindings']],
   'chat-hooks':[['useViewportWidth()','number; browser resize lifecycle'],['useShareLink(api, id, origin)','data, isLoading, error, setAccess'],['Injected API','Pick<ShareApi, createShareLink>'],['Subpath entries','Focused public import surfaces']],
   'chat-api-client':[['Configuration','basePath, credentials, middleware'],['DeploymentsApi.listDeployments()','Promise<DeploymentsResponseDto>'],['listDeploymentsRaw({})','Raw response wrapper and value()'],['Generation source','Nest Swagger + openapi.json']],
   'chat-overlay':[['new ChatOverlay(root, options)','Mount and configure one iframe'],['ready()','Promise for the readiness handshake'],['setInputContent(text)','Request to the embedded chat'],['subscribe / destroy','Event lifecycle and cleanup']]}
  rows=special[slug]
 slides.append(s(base+'-04','The public contract to start with','table',kicker=component+' · selected surface; full API index is in the bundle.',headers=['Input or operation','Contract'],rows=rows,notes='These are selected public symbols or props, not a complete API listing. Required versus optional props come from the TypeScript checker over the current source. All declarations, including the source file and line range, are retained in content/api-index.md and the per-project research JSON. '+cfg['notes'],sources=ss))
 slides.append(s(base+'-05','A minimal workspace integration','code',kicker='TypeScript / React example · imports and host setup abridged.',code=excerpt,caption=f'Full example: {ex.as_posix()} · uses {scope}',notes=f'Run this example in the existing React 19 workspace using the package source aliases and its declared peers. For browser-only modules use a browser host. Full imports, types and required props are in {ex.as_posix()}. '+('The stylesheet import must be loaded by the host. ' if 'styles.css' in code else '')+'Host parameters in the complete example are typed integration requirements, not hidden globals. Expected behavior: '+cfg['scenario'][0].split('|')[1]+' Backend-dependent examples require a running configured service; the bundle type-checks them but does not call production services.',sources=ss))
 slides.append(s(base+'-06','Wire a realistic host workflow',kicker='Keep '+cfg['title'].lower()+' focused on its public responsibility.',cards=[dict(title='Prepare the data',body=cfg['flow'][0].split('|')[1]+'. Resolve labels and validate required inputs.'),dict(title='Connect behavior',body=cfg['host'][:155]),dict(title='Reflect the result',body='Update the supplied values and loading/error state after the host action completes.')],notes='In the real application, '+cfg['host']+' belongs at the integration edge. The complete examples make injected callbacks explicit. Handle rejected asynchronous operations at the owner of the operation and feed error/loading state back into the UI. Avoid rebuilding stable inputs on every render when a component uses object identity to seed editing state. '+cfg['notes'],sources=ss))
 slides.append(s(base+'-07','Available customization',cards=cards(cfg['features']),notes='Customization comes from the current exports and prop declarations. '+' '.join(x.replace('|',': ') for x in cfg['features'])+' For UI, import the package stylesheet and use documented props or stable public classes. A component-level color override and inherited theme tokens are different levels of control. Locale strings and direction should be supplied by the host; do not introduce app i18n into a reusable library.',sources=ss))
 consumers=[x for x in d['consumers'] if '.spec.' not in x and '.test.' not in x];tests=d['testEvidence'];sample=tests[:2];consumer=consumers[0] if consumers else None
 rows2=[]
 if consumer:rows2.append(['Real consumer',consumer.replace('apps/chat/src/','chat/').replace('libs/','')])
 for te in sample:
  a=te['assertions'][1] if len(te['assertions'])>1 else (te['assertions'][0] if te['assertions'] else 'Existing source test');rows2.append(['Test evidence',a[:94]])
 if not sample:rows2.append(['Validation workflow','Regeneration, typecheck and downstream consumers'])
 evidence=ss+[source(x) for x in ([consumer] if consumer else [])]+[source(x['file']) for x in sample]
 slides.append(s(base+'-08','Find the integration and its checks','table',kicker='Existing tests are evidence of intended behavior; suite results are not claimed.',headers=['Evidence','Where to look'],rows=rows2,colW=[2.7,9.34],notes='Actual consumers: '+'; '.join(consumers[:6])+'. Existing test evidence: '+json.dumps(sample,ensure_ascii=True)+'. Reproduce project checks from the repository root with npm exec nx run '+d['project']['project']+':typecheck and the available test/lint targets. This documentation task does not rebuild or modify the application repository. The bundle checks its own examples separately.',sources=evidence))
 slides.append(s(base+'-09','Constraints that affect integration',cards=cards(cfg['limits']),notes='Review these constraints before choosing the library. '+' '.join(x.replace('|',': ') for x in cfg['limits'])+' The package is private in this snapshot. The presence of build/publish tooling is not evidence that a compatible release is available from a registry. For externally packed installations, inspect the repository publish tooling and host-install matrix and verify the resulting artifact separately.',sources=ss+[source('AGENTS.md')]))
 # Two focused examples for the largest surfaces, with no padding slides.
 second={
  'attachment-canvas':('Context-based canvas control','AttachmentCanvasProvider owns shared canvas state.','import { AttachmentCanvasProvider }\n  from \'@epam/ai-dial-attachment-canvas\';\n\n<AttachmentCanvasProvider>\n  {children}\n</AttachmentCanvasProvider>', 'The direct controlled example does not need this context. Use the provider when descendants call useAttachmentCanvas or the context-driven opening hook; supply host resolvers for access-dependent content.'),
  'builder-form':('Validate without translating','The host maps error codes into messages.',"const codes = validateDeploymentCreationFields(\n  { name: '', description: '', iconUrl: '',\n    version: '1.0.0', topics: [], otherLocales: [] },\n  { validateNamePattern: true, validateVersionPattern: true },\n);",'An empty name produces a validation error code. No translation service is invoked by the validator. The full example includes this call.'),
  'catalog':('Choose the headless entry','Mapping consumers can avoid the full catalog UI.',"import { filterCatalogItems, CredentialsLevel }\n  from '@epam/ai-dial-catalog/mapping';",'This is an import-only example of a genuine public subpath. Function declarations and tests are indexed under src/entry-points/mapping.ts; argument shapes are in the API appendix.'),
  'chat-hooks':('A request lifecycle with an injected client','The caller configures auth and transport.',"const { data, isLoading, error, setAccess } =\n  useShareLink(\n    api,\n    'demo-item',\n    'https://example.com',\n  );\n// Render data.url, pending state or the error.", 'The full ShareLifecycleDemo example receives Pick<ShareApi, createShareLink>. Changing access requests a new link. The hook uses request identifiers to avoid overwriting newer results with stale responses. Pass origin explicitly when the default browser-global expression is unsuitable.'),
  'chat-api-client':('Preserve transport details when needed','Raw operations keep the underlying Response available.',"const response = await api.listDeploymentsRaw({});\nconst status = response.raw.status;\nconst data = await response.value();",'The Raw signature requires the request object even when every query field is optional. The normal listDeployments method defaults that object. This distinction is enforced by the example TypeScript check.'),
  'chat-overlay':('Subscribe and clean up','Match event ownership to the host page lifecycle.',"const unsubscribe = overlay.subscribe(\n  OverlayEventType.GptStartGenerating,\n  () => console.info('Demo generation started'),\n);\n\n// On host teardown:\nunsubscribe();\noverlay.destroy();",'The full mountDemoOverlay function returns the teardown callback. Await the handshake before issuing normal requests. Destroy the overlay when its host container is no longer valid.'),
  'chat-shared':('Reuse the Markdown entry','A common renderer keeps display behavior consistent.',"import { MarkdownRenderer }\n  from '@epam/ai-dial-chat-shared/markdown';\n\n<MarkdownRenderer\n  content=\"**Demo:** shared Markdown rendering\"\n/>", 'This fragment is part of SharedDemo. The renderer needs the host stylesheet and the dependencies of the selected entry point. Do not treat the shared package as types-only.'),
  'toolset-editor':('Validate a candidate endpoint','Use an exported utility before host persistence.',"const valid = isValidEndpointUrl(\n  'https://example.com/mcp',\n);",'This pure validation example is included in the full module. A valid URL does not establish toolset availability or successful authentication. The complete ToolsetEditor still requires every prop in the exported contract.'),
 }
 if slug in second:
  title,kicker,ex2,exnotes=second[slug];slides.insert(6,s(base+'-10',title,'code',kicker=kicker,code=ex2,caption='Focused source-backed example · see examples/ and content/api-index.md.',notes=exnotes,sources=ss))
 for sl in slides:
  if not sl.get('sources'):raise ValueError(sl['id'])
 deck=dict(id=d['project']['id'],shortTitle=cfg['title'],series='Library deep dive',snapshot=SNAP,slides=slides,output=d['project']['output'])
 return deck

for slug,cfg in D.items():
 deck=build_library(slug,cfg);dest=Path('content/decks')/(slug+'.json');dest.parent.mkdir(exist_ok=True)
 if not dest.exists():dest.write_text(json.dumps(deck,indent=2)+'\n')
 for e in M['decks']:
  if e['id']==deck['id']:e.update(purpose=cfg['purpose'],content=str(dest),status='authored',slideCount=len(deck['slides']))
Path('manifest.json').write_text(json.dumps(M,indent=2)+'\n')
print('Authored',len(D),'library presentations')
