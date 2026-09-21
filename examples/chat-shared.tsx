import { buildCssVars, MessageRole } from '@epam/ai-dial-chat-shared';
import { MarkdownRenderer } from '@epam/ai-dial-chat-shared/markdown';
import '@epam/ai-dial-chat-shared/styles.css';

export const demoRole = MessageRole.Assistant;
export function SharedDemo() {
  return <section style={buildCssVars({ '--text-primary': '#EDF2F7', '--unused': undefined })}>
    <MarkdownRenderer content="**Demo:** shared Markdown rendering" />
  </section>;
}
