import { NavigationPanel } from '@epam/ai-dial-navigation-panel';
import type { NavigationPanelItem } from '@epam/ai-dial-navigation-panel';
import '@epam/ai-dial-navigation-panel/styles.css';

export function NavigationDemo({ items }: { items: NavigationPanelItem[] }) {
  return <NavigationPanel items={items} labels={{ ariaLabel: 'Demo navigation' }}
    renderLink={(item, children) => <a href={item.id}>{children}</a>} />;
}
