import { PublishPanel } from '@epam/ai-dial-publish-panel';
import type { PublishPanelProps } from '@epam/ai-dial-publish-panel';
import '@epam/ai-dial-publish-panel/styles.css';

export function PublishDemo(host: Omit<PublishPanelProps, 'resource'>) {
  return <PublishPanel {...host} resource={{ title: 'Demo planning notes' }} />;
}
