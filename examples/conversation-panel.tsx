import { useState } from 'react';
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
