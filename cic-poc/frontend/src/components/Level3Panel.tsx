/**
 * Level3Panel - shared container for Level-3 transparency surfaces (Lexicon
 * full entry, citation sources). Desktop: side panel along the transcript
 * column's right edge. Phone (<900px, treated as the non-desktop case since
 * no third "tablet" treatment is designed): bottom sheet over the input
 * area. Participant-opened only (never auto-opened); Esc, the close
 * button, or a tap/click outside the panel dismisses it. Content is
 * unchanged from the old centered modal - only this container differs.
 */

import { useEffect } from 'react';

interface Level3PanelProps {
  onClose: () => void;
  children: React.ReactNode;
}

export function Level3Panel({ onClose, children }: Level3PanelProps) {
  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') {
        onClose();
      }
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [onClose]);

  return (
    <div className="level3-backdrop" onClick={onClose}>
      <div className="level3-panel" onClick={(e) => e.stopPropagation()}>
        <button className="level3-panel__close" onClick={onClose} aria-label="Close">
          &times;
        </button>
        {children}
      </div>
    </div>
  );
}
