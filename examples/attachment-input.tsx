import { useState } from 'react';
import { AttachmentTray } from '@epam/ai-dial-attachment-input';
import type { DisplayAttachment } from '@epam/ai-dial-chat-shared';
import '@epam/ai-dial-attachment-input/styles.css';

export function AttachmentDemo({ initial }: { initial: DisplayAttachment[] }) {
  const [attachments, setAttachments] = useState(initial);
  return <AttachmentTray attachments={attachments}
    onRemove={id => setAttachments(items => items.filter(x => x.id !== id))}
    labels={{ ariaLabel: 'Attached demo files' }} />;
}
