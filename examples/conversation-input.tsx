import { useState } from 'react';
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
