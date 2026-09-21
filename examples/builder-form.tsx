import { EditorLayout, EditorSection, validateDeploymentCreationFields } from '@epam/ai-dial-builder-form';
import '@epam/ai-dial-builder-form/styles.css';

export function BuilderDemo({ onBack }: { onBack: () => void }) {
  return <EditorLayout title="Create demo deployment" onBack={onBack}
    leftContent={<EditorSection title="Metadata">Demo field area</EditorSection>}
    rightContent={<EditorSection title="Setup">Host setup area</EditorSection>} />;
}

export const validationDemo = validateDeploymentCreationFields({
  name: '', description: '', iconUrl: '', version: '1.0.0', topics: [], otherLocales: [],
}, { validateNamePattern: true, validateVersionPattern: true });
