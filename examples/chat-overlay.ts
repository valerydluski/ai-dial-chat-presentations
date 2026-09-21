import { ChatOverlay, OverlayEventType } from '@epam/ai-dial-chat-overlay';

/* Requires an existing #demo-chat element and an overlay-enabled chat deployment. */
export async function mountDemoOverlay(domain: string) {
  const overlay = new ChatOverlay('#demo-chat', { domain, theme: 'dark' });
  await overlay.ready();
  await overlay.setInputContent('Explain the demo architecture');
  const unsubscribe = overlay.subscribe(OverlayEventType.GptStartGenerating,
    () => console.info('Demo generation started'));
  return () => { unsubscribe(); overlay.destroy(); };
}
