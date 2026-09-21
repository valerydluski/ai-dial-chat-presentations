import { ConversationSourcesPanel } from '@epam/ai-dial-source-panel';
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
