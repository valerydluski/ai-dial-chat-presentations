import { useState } from 'react';
import { PromptParametersPopup } from '@epam/ai-dial-prompts';
import { resolvePromptParams } from '@epam/ai-dial-chat-shared';
import '@epam/ai-dial-prompts/styles.css';

export function ParametersDemo({ onText }: { onText: (text: string) => void }) {
  const [open, setOpen] = useState(true);
  const content = 'Summarize {{topic}}';
  return <PromptParametersPopup open={open} promptName="Demo summary" content={content}
    parameters={[{ name: 'topic' }]} onClose={() => setOpen(false)}
    onCancel={() => setOpen(false)} onSubmit={values => {
      onText(resolvePromptParams(content, values)); setOpen(false);
    }} />;
}
