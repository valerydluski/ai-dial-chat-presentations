import { AssistantMessageBubble } from '@epam/ai-dial-conversation-messages';
import { StagesPanel } from '@epam/ai-dial-conversation-stages';
import '@epam/ai-dial-conversation-messages/styles.css';
import '@epam/ai-dial-conversation-stages/styles.css';

export function MessageDemo() {
  return <AssistantMessageBubble text="**Demo:** evidence collected."
    isStreaming={false} deploymentDisplayName="Demo assistant"
    afterContent={<StagesPanel stages={[]} isStreaming={false} />} />;
}
