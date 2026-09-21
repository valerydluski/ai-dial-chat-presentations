import { SkillEditor } from '@epam/ai-dial-skill-editor';
import type { SkillEditorProps } from '@epam/ai-dial-skill-editor';
import '@epam/ai-dial-skill-editor/styles.css';

/* The host supplies real file validation, upload and persistence behavior. */
export function SkillEditorDemo(host: Pick<SkillEditorProps,
  'files' | 'fileActions' | 'onSubmit' | 'onCancel' | 'onBack'>) {
  return <SkillEditor {...host} title="Create demo skill"
    initialValues={{ name: 'demo-skill', description: 'Demo instructions' }} />;
}
