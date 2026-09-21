import { useState } from 'react';
import { SharePopover, ShareLinkAccess } from '@epam/ai-dial-share';
import '@epam/ai-dial-share/styles.css';

export function ShareDemo({ onClose }: { onClose: () => void }) {
  const [access, setAccess] = useState([ShareLinkAccess.View]);
  return <SharePopover url="https://example.com/demo-share" isLoading={false}
    error={null} access={access} canEditAccess={false}
    onAccessChange={setAccess} onClose={onClose} />;
}
