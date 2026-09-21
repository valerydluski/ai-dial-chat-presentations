import { useState } from 'react';
import { ScheduledTasks, ScheduledTasksSortKey } from '@epam/ai-dial-scheduled-tasks';
import type { ScheduledTasksProps } from '@epam/ai-dial-scheduled-tasks';
import '@epam/ai-dial-scheduled-tasks/styles.css';

export function TasksDemo(host: Pick<ScheduledTasksProps, 'items' | 'labels' | 'onCreateClick'>) {
  const [query, setQuery] = useState('');
  const [sort, setSort] = useState(ScheduledTasksSortKey.FirstToRun);
  return <ScheduledTasks {...host} searchQuery={query} onSearchQueryChange={setQuery}
    sortKey={sort} onSortChange={setSort} />;
}
