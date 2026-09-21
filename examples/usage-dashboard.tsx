import { UsageLimitCard, UsageLimitStatus } from '@epam/ai-dial-usage-dashboard';
import type { UsageLimitCardGroupLabels } from '@epam/ai-dial-usage-dashboard';
import '@epam/ai-dial-usage-dashboard/styles.css';

export const labels: UsageLimitCardGroupLabels = {
  defaultBadgeLabel: 'Within limits', runningLowBadgeLabel: 'Running low',
  limitReachedBadgeLabel: 'Limit reached', usedOfTotalLabel: ({total}) => `used of ${total}`,
  remainingCaptionLabel: ({remaining}) => `${remaining} left`,
  usedPercentLabel: ({percent}) => `${percent}%`,
};
export function UsageDemo() {
  return <UsageLimitCard labels={labels} data={{ title: 'Today', periodDescription: 'Today',
    used: 3, total: 10, usedLabel: '$3', totalLabel: '$10', remainingLabel: '$7',
    usedPercent: 30, status: UsageLimitStatus.Default,
    progressAriaLabel: 'Demo: 3 of 10, 30 percent used' }} />;
}
