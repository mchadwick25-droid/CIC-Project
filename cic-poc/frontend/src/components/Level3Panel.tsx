/**
 * Level3Panel - shared container for Level-3 transparency surfaces (Lexicon
 * full entry, citation sources). Desktop: side panel along the transcript
 * column's right edge. Phone (<900px, treated as the non-desktop case since
 * no third "tablet" treatment is designed): bottom sheet over the input
 * area. Participant-opened only (never auto-opened); Esc, the close
 * button, or a tap/click outside the panel dismisses it. Content is
 * unchanged from the old centered modal - only this container differs.
 */

import { useEffect, useState } from 'react';
import type { Level3Face } from '../types/conversation';

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

/**
 * ORQScaffold - S5.4's genuinely new piece (Pass 1 §5.6): the
 * Observe → Reflect → Question layer that sits on top of a record's full
 * scholarly apparatus, with the complete record reachable beneath.
 * Explicitly a starting shape being tested - the payload's own
 * scaffold_note says so and is rendered, not hidden. Shared here (the
 * Level-3 container module) so every Level-3 surface presents records
 * the same way.
 */
const SCAFFOLD_STAGES: Array<{ key: 'observe' | 'reflect' | 'question'; label: string; lead: string }> = [
  { key: 'observe', label: 'Observe', lead: 'What the record holds' },
  { key: 'reflect', label: 'Reflect', lead: 'What kind of claim it is' },
  { key: 'question', label: 'Question', lead: 'What the record leaves open' },
];

export function ORQScaffold({ face }: { face: Level3Face }) {
  const [showFullRecord, setShowFullRecord] = useState(false);

  return (
    <div className="orq-scaffold">
      {SCAFFOLD_STAGES.map(({ key, label, lead }) => {
        const lines = face[key];
        if (!lines || lines.length === 0) return null;
        return (
          <div key={key} className={`orq-scaffold__stage orq-scaffold__stage--${key}`}>
            <h3 className="orq-scaffold__stage-title">
              {label}
              <span className="orq-scaffold__stage-lead">{lead}</span>
            </h3>
            {lines.map((line, i) => (
              <p key={i} className="orq-scaffold__line">{line}</p>
            ))}
          </div>
        );
      })}

      <p className="orq-scaffold__note">{face.scaffold_note}</p>

      <button
        className="orq-scaffold__full-toggle"
        onClick={() => setShowFullRecord((v) => !v)}
      >
        {showFullRecord ? 'Hide the full record' : 'Show the full record'}
      </button>
      {showFullRecord && (
        <pre className="orq-scaffold__full-record">
          {JSON.stringify(face.full_record, null, 2)}
        </pre>
      )}
    </div>
  );
}
