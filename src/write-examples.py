from pathlib import Path
import json
P=Path('examples');P.mkdir(exist_ok=True)
examples={
'attachment-input':'''import { useState } from 'react';
import { AttachmentTray } from '@epam/ai-dial-attachment-input';
import type { DisplayAttachment } from '@epam/ai-dial-chat-shared';
import '@epam/ai-dial-attachment-input/styles.css';

export function AttachmentDemo({ initial }: { initial: DisplayAttachment[] }) {
  const [attachments, setAttachments] = useState(initial);
  return <AttachmentTray attachments={attachments}
    onRemove={id => setAttachments(items => items.filter(x => x.id !== id))}
    labels={{ ariaLabel: 'Attached demo files' }} />;
}
''',
'attachment-canvas':'''import { useState } from 'react';
import { AttachmentCanvas, AttachmentContentType } from '@epam/ai-dial-attachment-canvas';
import '@epam/ai-dial-attachment-canvas/styles.css';

export function CanvasDemo() {
  const [open, setOpen] = useState(true);
  return <AttachmentCanvas isOpen={open} onClose={() => setOpen(false)}
    content={{ type: AttachmentContentType.PlainText, text: 'Demo evidence' }}
    fileName="demo.txt" labels={{ ariaLabel: 'Demo preview' }} />;
}
''',
'builder-form':'''import { EditorLayout, EditorSection, validateDeploymentCreationFields } from '@epam/ai-dial-builder-form';
import '@epam/ai-dial-builder-form/styles.css';

export function BuilderDemo({ onBack }: { onBack: () => void }) {
  return <EditorLayout title="Create demo deployment" onBack={onBack}
    leftContent={<EditorSection title="Metadata">Demo field area</EditorSection>}
    rightContent={<EditorSection title="Setup">Host setup area</EditorSection>} />;
}

export const validationDemo = validateDeploymentCreationFields({
  name: '', description: '', iconUrl: '', version: '1.0.0', topics: [], otherLocales: [],
}, { validateNamePattern: true, validateVersionPattern: true });
''',
'catalog':'''import { Catalog } from '@epam/ai-dial-catalog';
import type { CatalogItem } from '@epam/ai-dial-catalog';
import '@epam/ai-dial-catalog/styles.css';

export function CatalogDemo({ items, onPick }: {
  items: CatalogItem[]; onPick: (item: CatalogItem) => void;
}) {
  return <Catalog items={items} favorites={[]}
    onUseInChat={onPick} isFavoriteVisible={() => false} />;
}
''',
'conversation-input':'''import { useState } from 'react';
import { ConversationInput } from '@epam/ai-dial-conversation-input';
import '@epam/ai-dial-conversation-input/styles.css';

export function ComposerDemo() {
  const [sent, setSent] = useState('');
  return <>
    <ConversationInput placeholder="Write a demo message"
      onSend={(message) => setSent(message)} />
    <p role="status">{sent ? `Last demo message: ${sent}` : 'Ready'}</p>
  </>;
}
''',
'conversation-messages':'''import { AssistantMessageBubble } from '@epam/ai-dial-conversation-messages';
import { StagesPanel } from '@epam/ai-dial-conversation-stages';
import '@epam/ai-dial-conversation-messages/styles.css';
import '@epam/ai-dial-conversation-stages/styles.css';

export function MessageDemo() {
  return <AssistantMessageBubble text="**Demo:** evidence collected."
    isStreaming={false} deploymentDisplayName="Demo assistant"
    afterContent={<StagesPanel stages={[]} isStreaming={false} />} />;
}
''',
'conversation-panel':'''import { useState } from 'react';
import { ConversationPanel } from '@epam/ai-dial-conversation-panel';
import type { ConversationPanelLabels } from '@epam/ai-dial-conversation-panel';
import '@epam/ai-dial-conversation-panel/styles.css';

export const labels: ConversationPanelLabels = {
  title: 'Chats', emptyLabel: 'No chats', noResultsLabel: 'No matches',
  newChatLabel: 'New chat', searchPlaceholder: 'Search chats', searchClearLabel: 'Clear',
  filterLabels: { all: 'All', myChats: 'My chats', shared: 'Shared',
    organization: 'Organization', groupAriaLabel: 'Filter chats' },
};
export function HistoryDemo({ onNewChat }: { onNewChat: () => void }) {
  const [active, setActive] = useState('demo');
  return <ConversationPanel isOpen conversations={[{ id: 'demo', title: 'Demo chat' }]}
    activeConversationId={active} onSelectConversation={setActive}
    onNewChat={onNewChat} labels={labels} />;
}
''',
'conversation-stages':'''import { StagesPanel } from '@epam/ai-dial-conversation-stages';
import '@epam/ai-dial-conversation-stages/styles.css';

export function StagesDemo() {
  return <StagesPanel isStreaming stages={[
    { index: 0, name: 'Read demo sources', status: null, content: 'Retrieving evidence' },
  ]} labels={{ runningAriaLabel: 'Running', failedAriaLabel: 'Failed' }} />;
}
''',
'navigation-panel':'''import { NavigationPanel } from '@epam/ai-dial-navigation-panel';
import type { NavigationPanelItem } from '@epam/ai-dial-navigation-panel';
import '@epam/ai-dial-navigation-panel/styles.css';

export function NavigationDemo({ items }: { items: NavigationPanelItem[] }) {
  return <NavigationPanel items={items} labels={{ ariaLabel: 'Demo navigation' }}
    renderLink={(item, children) => <a href={item.id}>{children}</a>} />;
}
''',
'sidebar':'''import { useState } from 'react';
import { SidebarPanel, SidebarOrientation } from '@epam/ai-dial-sidebar';
import '@epam/ai-dial-sidebar/styles.css';

export function SidebarDemo() {
  const [width, setWidth] = useState(360);
  return <SidebarPanel isOpen title="Demo sources"
    orientation={SidebarOrientation.Right} resizable defaultWidth={width}
    onResizeStop={setWidth} labels={{ ariaLabel: 'Demo sources', closeLabel: 'Close' }}>
    <p>Host-provided content</p>
  </SidebarPanel>;
}
''',
'settings-panel':'''import { useState } from 'react';
import { SettingsPanel } from '@epam/ai-dial-settings-panel';
import '@epam/ai-dial-settings-panel/styles.css';

export function SettingsDemo() {
  const [activeId, setActiveId] = useState('usage');
  return <SettingsPanel sectionLabel="Demo settings" activeId={activeId}
    onSelect={setActiveId} items={[
      { id: 'usage', label: 'Usage' }, { id: 'profile', label: 'Profile' },
    ]} />;
}
''',
'starter-buttons':'''import { StarterButtons } from '@epam/ai-dial-starter-buttons';
import type { StarterOption } from '@epam/ai-dial-chat-shared';
import '@epam/ai-dial-starter-buttons/styles.css';

export function StartersDemo({ starters, onSelect }: {
  starters: StarterOption[]; onSelect: (starter: StarterOption) => void;
}) {
  return <StarterButtons starters={starters} onSelect={onSelect}
    labels={{ list: 'Demo starters', overflow: 'More starters' }} />;
}
''',
'source-panel':'''import { ConversationSourcesPanel } from '@epam/ai-dial-source-panel';
import type { ConversationSourcesPanelLabels, QuotationSource } from '@epam/ai-dial-source-panel';
import '@epam/ai-dial-source-panel/styles.css';

export const labels: ConversationSourcesPanelLabels = {
  ariaLabel: 'Sources', closeLabel: 'Close', searchPlaceholder: 'Search sources',
  searchClearLabel: 'Clear', noDataLabel: 'No sources', noResultsLabel: 'No matches',
  downloadAllLabel: 'Download all', uploadedSectionTitle: 'Uploaded',
  generatedSectionTitle: 'Generated', sourcesSectionTitle: 'Sources',
  copySourceLabel: 'Copy source', attachmentClickLabel: 'Open attachment',
};
export function SourcesDemo({ sources, onOpen, onClose }: {
  sources: QuotationSource[]; onOpen: (source: QuotationSource) => void; onClose: () => void;
}) {
  return <ConversationSourcesPanel isOpen isMobile={false} onClose={onClose}
    uploaded={[]} generated={[]} sources={sources} labels={labels} onSourceClick={onOpen} />;
}
''',
'quotations':'''import { useState } from 'react';
import { CitationMarker } from '@epam/ai-dial-quotations';
import '@epam/ai-dial-quotations/styles.css';

export function CitationDemo() {
  const [opened, setOpened] = useState(false);
  return <>
    <CitationMarker sourceName="demo-report.pdf" annotationCount={2}
      onOpen={() => setOpened(true)} labels={{ ariaLabel: 'Open demo citation',
        label: 'demo-report.pdf', labelWithOverflow: 'demo-report.pdf +1' }} />
    <p role="status">{opened ? 'Demo citation selected' : ''}</p>
  </>;
}
''',
'prompt-editor':'''import { PromptEditor } from '@epam/ai-dial-prompt-editor';
import type { PromptEditorValues } from '@epam/ai-dial-prompt-editor';
import '@epam/ai-dial-prompt-editor/styles.css';

export function PromptEditorDemo({ save, onCancel }: {
  save: (values: PromptEditorValues) => void; onCancel: () => void;
}) {
  return <PromptEditor initialValues={{ name: 'Demo summary', content: 'Summarize {{topic}}' }}
    onSubmit={save} onCancel={onCancel} />;
}
''',
'prompts':'''import { useState } from 'react';
import { PromptParametersPopup } from '@epam/ai-dial-prompts';
import { resolvePromptParams } from '@epam/ai-dial-chat-shared';
import '@epam/ai-dial-prompts/styles.css';

export function ParametersDemo({ onText }: { onText: (text: string) => void }) {
  const [open, setOpen] = useState(true);
  const content = 'Summarize {{topic}}';
  return <PromptParametersPopup open={open} promptName="Demo summary" content={content}
    parameters={[{ name: 'topic' }]} onClose={() => setOpen(false)}
    onCancel={() => setOpen(false)} onSubmit={values => {
      onText(resolvePromptParams(content, values)); setOpen(false);
    }} />;
}
''',
'skill-editor':'''import { SkillEditor } from '@epam/ai-dial-skill-editor';
import type { SkillEditorProps } from '@epam/ai-dial-skill-editor';
import '@epam/ai-dial-skill-editor/styles.css';

/* The host supplies real file validation, upload and persistence behavior. */
export function SkillEditorDemo(host: Pick<SkillEditorProps,
  'files' | 'fileActions' | 'onSubmit' | 'onCancel' | 'onBack'>) {
  return <SkillEditor {...host} title="Create demo skill"
    initialValues={{ name: 'demo-skill', description: 'Demo instructions' }} />;
}
''',
'skills':'''import { FavoriteSkillsPanel } from '@epam/ai-dial-skills';
import type { FavoriteSkillsPanelProps } from '@epam/ai-dial-skills';
import '@epam/ai-dial-skills/styles.css';

export function SkillsDemo(host: Omit<FavoriteSkillsPanelProps, 'favorites'>) {
  return <FavoriteSkillsPanel {...host} favorites={[
    { id: 'skills/demo/review', name: 'Demo review', description: 'Review demo content' },
  ]} />;
}
''',
'scheduled-tasks':'''import { useState } from 'react';
import { ScheduledTasks, ScheduledTasksSortKey } from '@epam/ai-dial-scheduled-tasks';
import type { ScheduledTasksProps } from '@epam/ai-dial-scheduled-tasks';
import '@epam/ai-dial-scheduled-tasks/styles.css';

export function TasksDemo(host: Pick<ScheduledTasksProps, 'items' | 'labels' | 'onCreateClick'>) {
  const [query, setQuery] = useState('');
  const [sort, setSort] = useState(ScheduledTasksSortKey.FirstToRun);
  return <ScheduledTasks {...host} searchQuery={query} onSearchQueryChange={setQuery}
    sortKey={sort} onSortChange={setSort} />;
}
''',
'share':'''import { useState } from 'react';
import { SharePopover, ShareLinkAccess } from '@epam/ai-dial-share';
import '@epam/ai-dial-share/styles.css';

export function ShareDemo({ onClose }: { onClose: () => void }) {
  const [access, setAccess] = useState([ShareLinkAccess.View]);
  return <SharePopover url="https://example.com/demo-share" isLoading={false}
    error={null} access={access} canEditAccess={false}
    onAccessChange={setAccess} onClose={onClose} />;
}
''',
'publish-panel':'''import { PublishPanel } from '@epam/ai-dial-publish-panel';
import type { PublishPanelProps } from '@epam/ai-dial-publish-panel';
import '@epam/ai-dial-publish-panel/styles.css';

export function PublishDemo(host: Omit<PublishPanelProps, 'resource'>) {
  return <PublishPanel {...host} resource={{ title: 'Demo planning notes' }} />;
}
''',
'usage-dashboard':'''import { UsageLimitCard, UsageLimitStatus } from '@epam/ai-dial-usage-dashboard';
import type { UsageLimitCardGroupLabels } from '@epam/ai-dial-usage-dashboard';
import '@epam/ai-dial-usage-dashboard/styles.css';

export const labels: UsageLimitCardGroupLabels = {
  defaultBadgeLabel: 'Within limits', runningLowBadgeLabel: 'Running low',
  limitReachedBadgeLabel: 'Limit reached', usedOfTotalLabel: ({total}) => `used of ${total}`,
  remainingCaptionLabel: ({remaining}) => `${remaining} left`,
  usedPercentLabel: ({percent}) => `${percent}%`,
};
export function UsageDemo() {
  return <UsageLimitCard labels={labels} data={{ title: 'Today', periodDescription: 'Today',
    used: 3, total: 10, usedLabel: '$3', totalLabel: '$10', remainingLabel: '$7',
    usedPercent: 30, status: UsageLimitStatus.Default,
    progressAriaLabel: 'Demo: 3 of 10, 30 percent used' }} />;
}
''',
'mcp-apps':'''import { McpAppInlinePreview, useMcpAppResponseCache } from '@epam/ai-dial-mcp-apps';
import type { McpAppHostAdapter, McpAppToolRef } from '@epam/ai-dial-mcp-apps';
import '@epam/ai-dial-mcp-apps/styles.css';

export function McpPreviewDemo({ adapter, match, onExpand }: {
  adapter: McpAppHostAdapter; match: McpAppToolRef; onExpand: () => void;
}) {
  const cache = useMcpAppResponseCache('demo-conversation');
  return <McpAppInlinePreview match={match} cache={cache} cacheKey="demo-message"
    hostAdapter={adapter} onExpand={onExpand} expandAriaLabel="Expand demo app"
    reloadAriaLabel="Reload" loadErrorLabel="Could not load demo app"
    openedInCanvasLabel="Open in preview" />;
}
''',
'chat-shared':'''import { buildCssVars, MessageRole } from '@epam/ai-dial-chat-shared';
import { MarkdownRenderer } from '@epam/ai-dial-chat-shared/markdown';
import '@epam/ai-dial-chat-shared/styles.css';

export const demoRole = MessageRole.Assistant;
export function SharedDemo() {
  return <section style={buildCssVars({ '--text-primary': '#EDF2F7', '--unused': undefined })}>
    <MarkdownRenderer content="**Demo:** shared Markdown rendering" />
  </section>;
}
''',
'chat-hooks':'''import { useViewportWidth } from '@epam/ai-dial-chat-hooks/viewport-layout';
import { useShareLink } from '@epam/ai-dial-chat-hooks/sharing';
import type { ShareApi } from '@epam/ai-dial-chat-api-client';

export function ViewportDemo() {
  const width = useViewportWidth();
  return <p>Demo viewport: {width}px</p>;
}

export function ShareLifecycleDemo({ api }: { api: Pick<ShareApi, 'createShareLink'> }) {
  const { data, isLoading, error } = useShareLink(api, 'demo-item', 'https://example.com');
  return <p role="status">{isLoading ? 'Loading demo link' : error?.message ?? data?.url}</p>;
}
''',
'chat-api-client':'''import { Configuration, DeploymentsApi } from '@epam/ai-dial-chat-api-client';

/* Run from an authenticated host page against a running chat-api. */
export function createDemoApi() {
  return new DeploymentsApi(new Configuration({ basePath: '', credentials: 'include' }));
}
export async function listDemoDeployments() {
  const api = createDemoApi();
  return await api.listDeployments();
}
export async function readDemoHeaders() {
  const response = await createDemoApi().listDeploymentsRaw({});
  return { status: response.raw.status, data: await response.value() };
}
''',
'chat-overlay':'''import { ChatOverlay, OverlayEventType } from '@epam/ai-dial-chat-overlay';

/* Requires an existing #demo-chat element and an overlay-enabled chat deployment. */
export async function mountDemoOverlay(domain: string) {
  const overlay = new ChatOverlay('#demo-chat', { domain, theme: 'dark' });
  await overlay.ready();
  await overlay.setInputContent('Explain the demo architecture');
  const unsubscribe = overlay.subscribe(OverlayEventType.GptStartGenerating,
    () => console.info('Demo generation started'));
  return () => { unsubscribe(); overlay.destroy(); };
}
''',
 'toolset-editor':'''import { ToolsetEditor, isValidEndpointUrl } from '@epam/ai-dial-toolset-editor';
import type { ToolsetEditorProps } from '@epam/ai-dial-toolset-editor';
import '@epam/ai-dial-toolset-editor/styles.css';

/* Pass the complete typed host adapter: persistence, auth, files and navigation. */
export function ToolsetEditorDemo(host: ToolsetEditorProps) {
  return <ToolsetEditor {...host} />;
}
export const validDemoEndpoint = isValidEndpointUrl('https://example.com/mcp');
'''
}
for slug,code in examples.items():
 f=P/(slug+('.ts' if slug in ['chat-api-client','chat-overlay'] else '.tsx'))
 if not f.exists():f.write_text(code)
print(len(examples),'example modules')
