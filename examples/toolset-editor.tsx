import { ToolsetEditor, isValidEndpointUrl } from '@epam/ai-dial-toolset-editor';
import type { ToolsetEditorProps } from '@epam/ai-dial-toolset-editor';
import '@epam/ai-dial-toolset-editor/styles.css';

/* Pass the complete typed host adapter: persistence, auth, files and navigation. */
export function ToolsetEditorDemo(host: ToolsetEditorProps) {
  return <ToolsetEditor {...host} />;
}
export const validDemoEndpoint = isValidEndpointUrl('https://example.com/mcp');
