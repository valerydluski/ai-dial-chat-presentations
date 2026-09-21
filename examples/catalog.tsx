import { Catalog } from '@epam/ai-dial-catalog';
import type { CatalogItem } from '@epam/ai-dial-catalog';
import '@epam/ai-dial-catalog/styles.css';

export function CatalogDemo({ items, onPick }: {
  items: CatalogItem[]; onPick: (item: CatalogItem) => void;
}) {
  return <Catalog items={items} favorites={[]}
    onUseInChat={onPick} isFavoriteVisible={() => false} />;
}

import { filterCatalogItems, CredentialsLevel } from '@epam/ai-dial-catalog/mapping';

export function filterDemoCatalog(items: CatalogItem[]) {
  return filterCatalogItems(items, 'demo');
}
export const demoCredentialsLevel = CredentialsLevel.User;
