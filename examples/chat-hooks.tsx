import { useViewportWidth } from '@epam/ai-dial-chat-hooks/viewport-layout';
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
