import { McpAppInlinePreview, useMcpAppResponseCache } from '@epam/ai-dial-mcp-apps';
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
