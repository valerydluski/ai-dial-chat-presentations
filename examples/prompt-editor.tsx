import { PromptEditor } from '@epam/ai-dial-prompt-editor';
import type { PromptEditorValues } from '@epam/ai-dial-prompt-editor';
import '@epam/ai-dial-prompt-editor/styles.css';

export function PromptEditorDemo({ save, onCancel }: {
  save: (values: PromptEditorValues) => void; onCancel: () => void;
}) {
  return <PromptEditor initialValues={{ name: 'Demo summary', content: 'Summarize {{topic}}' }}
    onSubmit={save} onCancel={onCancel} />;
}
