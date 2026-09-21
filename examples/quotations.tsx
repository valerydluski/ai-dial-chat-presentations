import { useState } from 'react';
import { CitationMarker } from '@epam/ai-dial-quotations';
import '@epam/ai-dial-quotations/styles.css';

export function CitationDemo() {
  const [opened, setOpened] = useState(false);
  return <>
    <CitationMarker sourceName="demo-report.pdf" annotationCount={2}
      onOpen={() => setOpened(true)} labels={{ ariaLabel: 'Open demo citation',
        label: 'demo-report.pdf', labelWithOverflow: 'demo-report.pdf +1' }} />
    <p role="status">{opened ? 'Demo citation selected' : ''}</p>
  </>;
}
