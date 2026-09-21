from pathlib import Path
import json
replacements={
'AttachmentCanvasProvider and useAttachmentCanvas coordinate a canvas.':'A canvas provider and its context hook coordinate shared preview state.',
'DeploymentCreationForm includes avatar, version, topics and locales.':'The shared creation form includes avatar, version, topics and locales.',
'DeploymentLocalesField hides when no locale options are supplied.':'The locale editor hides when no locale options are supplied.',
'ImportExportQueue and RenameConversationPopup are separate exports.':'Transfer queues and rename dialogs are separate public components.',
'useCitationMarkdownComponents builds citation renderers.':'The citation Markdown hook builds renderer overrides.',
'PromptParametersPopup returns a value map, not a sent message.':'The parameter popup returns a value map for the host to resolve.',
'ScheduledTaskCreateForm and ScheduledTaskDetailView are distinct surfaces.':'Create forms and task detail views are distinct public components.',
'ScheduledTaskRunHistoryList renders host-provided run records.':'The run-history list renders records supplied by the host.',
'mapUsageDataToDashboard and model-limit mappers are public.':'Usage-to-dashboard and model-limit mapping helpers are public exports.',
'Framework-independent':'Any browser framework',
'Separate component and helper':'Components and helpers',
'ConversationMessageItem composes message bubbles and stages.':'The app message container composes bubbles and stages.',
'ConversationSourcesPanel adapts source data and open actions.':'The app sources container adapts evidence data and open actions.',
'ThemeProvider, SourcesSidebarProvider and AttachmentCanvasProvider.':'Theme, sources-sidebar and attachment-canvas providers.',
'OVERLAY_SANDBOX_ENABLED controls exposure of the route.':'The backend sandbox flag controls exposure of the route.',
}
code={
'builder-form':'''<EditorLayout
  title="Create demo deployment" onBack={onBack}
  leftContent={
    <EditorSection title="Metadata">Demo fields</EditorSection>
  }
  rightContent={
    <EditorSection title="Setup">Host setup</EditorSection>
  }
/>''',
'sidebar':'''<SidebarPanel
  isOpen title="Demo sources"
  orientation={SidebarOrientation.Right}
  resizable defaultWidth={width} onResizeStop={setWidth}
  labels={{ ariaLabel: 'Demo sources', closeLabel: 'Close' }}
>
  <p>Host-provided content</p>
</SidebarPanel>''',
'quotations':'''<CitationMarker
  sourceName="demo-report.pdf" annotationCount={2}
  onOpen={() => setOpened(true)}
  labels={{
    ariaLabel: 'Open demo citation',
    label: 'demo-report.pdf',
    labelWithOverflow: 'demo-report.pdf +1',
  }}
/>''',
'prompt-editor':'''<PromptEditor
  initialValues={{
    name: 'Demo summary',
    content: 'Summarize {{topic}}',
  }}
  onSubmit={save}
  onCancel={onCancel}
/>''',
'conversation-stages':'''<StagesPanel
  isStreaming
  stages={[{
    index: 0, name: 'Read demo sources', status: null,
    content: 'Retrieving evidence',
  }]}
  labels={{ runningAriaLabel: 'Running' }}
/>''',
'scheduled-tasks':'''const [query, setQuery] = useState('');
const [sort, setSort] = useState(
  ScheduledTasksSortKey.FirstToRun,
);
<ScheduledTasks
  {...host}
  searchQuery={query} onSearchQueryChange={setQuery}
  sortKey={sort} onSortChange={setSort}
/>
// host supplies items, labels and onCreateClick.''',
'navigation-panel':'''<NavigationPanel
  items={items}
  labels={{ ariaLabel: 'Demo navigation' }}
  renderLink={(item, children) => (
    <a href={item.id}>{children}</a>
  )}
/>''',
'publish-panel':'''function PublishDemo(
  host: Omit<PublishPanelProps, 'resource'>,
) {
  return <PublishPanel
    {...host}
    resource={{ title: 'Demo planning notes' }}
  />;
}''',
'skills':'''<FavoriteSkillsPanel
  {...host}
  favorites={[{
    id: 'skills/demo/review',
    name: 'Demo review',
    description: 'Review demo content',
  }]}
/>
// host supplies select, favorite, browse and detail callbacks.''',
'skill-editor':'''<SkillEditor
  {...host}
  title="Create demo skill"
  initialValues={{
    name: 'demo-skill', description: 'Demo instructions',
  }}
/>
// host supplies files, fileActions and save/navigation callbacks.''',
}
for p in Path('content/decks').glob('*.json'):
 d=json.loads(p.read_text());slug=d['id'].split('/')[-1]
 for s in d['slides']:
  for card in s.get('cards',[]):
   for key in ['title','body']:
    for old,new in replacements.items():card[key]=card[key].replace(old,new)
  if s['id']==f'lib-{slug}-05' and slug in code:s['code']=code[slug]
 p.write_text(json.dumps(d,indent=2)+'\n')
print('Applied readability fixes to current authored content.')
