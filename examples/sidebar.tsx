import { useState } from 'react';
import { SidebarPanel, SidebarOrientation } from '@epam/ai-dial-sidebar';
import '@epam/ai-dial-sidebar/styles.css';

export function SidebarDemo() {
  const [width, setWidth] = useState(360);
  return <SidebarPanel isOpen title="Demo sources"
    orientation={SidebarOrientation.Right} resizable defaultWidth={width}
    onResizeStop={setWidth} labels={{ ariaLabel: 'Demo sources', closeLabel: 'Close' }}>
    <p>Host-provided content</p>
  </SidebarPanel>;
}
