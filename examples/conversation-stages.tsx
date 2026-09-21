import { StagesPanel } from '@epam/ai-dial-conversation-stages';
import '@epam/ai-dial-conversation-stages/styles.css';

export function StagesDemo() {
  return <StagesPanel isStreaming stages={[
    { index: 0, name: 'Read demo sources', status: null, content: 'Retrieving evidence' },
  ]} labels={{ runningAriaLabel: 'Running', failedAriaLabel: 'Failed' }} />;
}
