import { StarterButtons } from '@epam/ai-dial-starter-buttons';
import type { StarterOption } from '@epam/ai-dial-chat-shared';
import '@epam/ai-dial-starter-buttons/styles.css';

export function StartersDemo({ starters, onSelect }: {
  starters: StarterOption[]; onSelect: (starter: StarterOption) => void;
}) {
  return <StarterButtons starters={starters} onSelect={onSelect}
    labels={{ list: 'Demo starters', overflow: 'More starters' }} />;
}
