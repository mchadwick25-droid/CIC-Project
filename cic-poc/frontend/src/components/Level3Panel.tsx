/**
 * Level-3: the full entry (CiC_Full_UX_Design_V1_0.md §2.4, §9.1 DECIDED).
 * A panel, never a centered modal - that correction is explicit and named
 * in the design ("Level-3 surfaces are panels, not centered modals").
 * Desktop: a side panel, 420px, vellum, its own scroll, Esc/× to close,
 * alongside the transcript (never covering it). Phone: a bottom sheet over
 * the input area, ~55% max height, the transcript still visible above it.
 * Participant-initiated only - this never opens itself.
 */
import { useEffect, useRef } from 'react';
import { useIsPhone } from '../hooks/useBreakpoint';

interface Level3PanelProps {
  title: string;
  onClose: () => void;
  children: React.ReactNode;
}

export function Level3Panel({ title, onClose, children }: Level3PanelProps) {
  const isPhone = useIsPhone();
  const closeRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    closeRef.current?.focus();
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape') onClose();
    }
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, [onClose]);

  return (
    <div className={isPhone ? 'level3-sheet' : 'level3-panel'} role="dialog" aria-label={title}>
      <div className="level3__header">
        <h2 className="level3__title">{title}</h2>
        <button type="button" className="level3__close" onClick={onClose} ref={closeRef} aria-label="Close">
          ×
        </button>
      </div>
      <div className="level3__body">{children}</div>
    </div>
  );
}
