import { FavoriteSkillsPanel } from '@epam/ai-dial-skills';
import type { FavoriteSkillsPanelProps } from '@epam/ai-dial-skills';
import '@epam/ai-dial-skills/styles.css';

export function SkillsDemo(host: Omit<FavoriteSkillsPanelProps, 'favorites'>) {
  return <FavoriteSkillsPanel {...host} favorites={[
    { id: 'skills/demo/review', name: 'Demo review', description: 'Review demo content' },
  ]} />;
}
