/**
 * Keeps `--app-height` on the root element equal to the height a person can
 * actually see. When a phone keyboard opens, iOS shrinks only the visual
 * viewport, so `100dvh` still reaches under the keyboard; the conversation
 * column sizes itself from this value instead, which keeps the message box
 * sitting just above the keyboard. Pinch-zoom also shrinks the visual
 * viewport, so the height is scaled back up by the zoom level; only the
 * keyboard changes it.
 */
import { useEffect } from 'react';

export function useVisibleHeight() {
  useEffect(() => {
    const root = document.documentElement;
    const viewport = window.visualViewport;
    const update = () => {
      const height = viewport ? viewport.height * viewport.scale : window.innerHeight;
      root.style.setProperty('--app-height', `${Math.round(height)}px`);
    };
    update();
    viewport?.addEventListener('resize', update);
    viewport?.addEventListener('scroll', update);
    window.addEventListener('resize', update);
    return () => {
      viewport?.removeEventListener('resize', update);
      viewport?.removeEventListener('scroll', update);
      window.removeEventListener('resize', update);
      root.style.removeProperty('--app-height');
    };
  }, []);
}
