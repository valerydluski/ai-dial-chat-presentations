import { useState, type ReactNode } from 'react';
import { AttachmentCanvas, AttachmentContentType, AttachmentCanvasProvider, useAttachmentCanvas } from '@epam/ai-dial-attachment-canvas';
import '@epam/ai-dial-attachment-canvas/styles.css';

export function CanvasDemo() {
  const [open, setOpen] = useState(true);
  return <AttachmentCanvas isOpen={open} onClose={() => setOpen(false)}
    content={{ type: AttachmentContentType.PlainText, text: 'Demo evidence' }}
    fileName="demo.txt" labels={{ ariaLabel: 'Demo preview' }} />;
}

export function ContextCanvasDemo({ children }: { children: ReactNode }) {
  return <AttachmentCanvasProvider>{children}<CanvasControls /></AttachmentCanvasProvider>;
}
function CanvasControls() {
  const canvas = useAttachmentCanvas();
  return <>
    <button onClick={() => canvas.openCanvas({type: AttachmentContentType.PlainText, text: 'Demo evidence'}, 'demo.txt')}>Open demo</button>
    <AttachmentCanvas isOpen={canvas.isOpen} content={canvas.content}
      isLoading={canvas.isLoading} fileName={canvas.fileName} onClose={canvas.closeCanvas}
      labels={{ariaLabel: 'Demo context preview'}} />
  </>;
}
