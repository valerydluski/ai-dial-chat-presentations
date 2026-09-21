import { useState } from 'react';
import { SettingsPanel } from '@epam/ai-dial-settings-panel';
import '@epam/ai-dial-settings-panel/styles.css';

export function SettingsDemo() {
  const [activeId, setActiveId] = useState('usage');
  return <SettingsPanel sectionLabel="Demo settings" activeId={activeId}
    onSelect={setActiveId} items={[
      { id: 'usage', label: 'Usage' }, { id: 'profile', label: 'Profile' },
    ]} />;
}
