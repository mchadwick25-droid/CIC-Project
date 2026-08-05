/**
 * QuestionSheet - the "Don't know what to ask?" content (UX Design V1.0
 * §4.1/§4.6, corrected 2026-08-02 per Mark's direct call: tabs are by
 * depth tier, not by role - the role/walk shape assumed a curriculum this
 * feature doesn't use. See World-Builds/<world>/*Guided_Starters_V0_1_DRAFT.md
 * for the grounded source content, one file per seated world.
 *
 * Behavior, per spec: slides up over the input area only - the transcript
 * stays fully visible and interactive above it (both platforms; desktop
 * does NOT get Level3Panel's right-edge side-panel treatment here, this is
 * a different surface). Tapping any question sends it exactly as written
 * and closes the sheet - the same dismiss-on-transcript-interaction rule
 * as typing. A world already seated needs no picker; if more than one
 * world is seated, a world tab row sits above the depth-tier tabs.
 */

import { useEffect, useState } from 'react';
import type { GuidedStarterWorld, GuidedStarterEntry, GuidedStarterLimitEntry } from '../types/conversation';

const TIER_LABELS: Record<string, string> = {
  first_visit: 'First Visit',
  going_deeper: 'Going Deeper',
  for_the_wrestling: 'For the Wrestling',
  honest_limits: 'Honest Limits',
};

const TIER_ORDER = ['first_visit', 'going_deeper', 'for_the_wrestling', 'honest_limits'];

function isLimitEntry(
  entry: GuidedStarterEntry | GuidedStarterLimitEntry
): entry is GuidedStarterLimitEntry {
  return 'question' in entry;
}

interface QuestionSheetProps {
  worlds: GuidedStarterWorld[];
  onAsk: (question: string) => void;
  onClose: () => void;
}

export function QuestionSheet({ worlds, onAsk, onClose }: QuestionSheetProps) {
  const [activeWorldId, setActiveWorldId] = useState(worlds[0]?.world_id ?? '');
  const [activeTierId, setActiveTierId] = useState('first_visit');

  useEffect(() => {
    const handleKeyDown = (e: KeyboardEvent) => {
      if (e.key === 'Escape') onClose();
    };
    window.addEventListener('keydown', handleKeyDown);
    return () => window.removeEventListener('keydown', handleKeyDown);
  }, [onClose]);

  if (worlds.length === 0) {
    return null;
  }

  const activeWorld = worlds.find((w) => w.world_id === activeWorldId) ?? worlds[0];
  const activeTier =
    activeWorld.tiers.find((t) => t.tier_id === activeTierId) ?? activeWorld.tiers[0];

  const handleAsk = (question: string) => {
    onAsk(question);
    onClose();
  };

  return (
    <div className="question-sheet-backdrop" onClick={onClose}>
      <div
        className="question-sheet"
        role="dialog"
        aria-label="Don't know what to ask?"
        onClick={(e) => e.stopPropagation()}
      >
        <div className="question-sheet__header">
          <span className="question-sheet__title">Don't know what to ask?</span>
          <button className="question-sheet__close" onClick={onClose} aria-label="Close">
            &times;
          </button>
        </div>

        {worlds.length > 1 && (
          <div className="question-sheet__world-tabs">
            {worlds.map((w) => (
              <button
                key={w.world_id}
                className={
                  'question-sheet__world-tab' +
                  (w.world_id === activeWorld.world_id ? ' question-sheet__world-tab--active' : '')
                }
                onClick={() => setActiveWorldId(w.world_id)}
              >
                {w.title.replace(/^Guided Starters\s*[—-]\s*/, '')}
              </button>
            ))}
          </div>
        )}

        <div className="question-sheet__tier-tabs">
          {TIER_ORDER.filter((id) => activeWorld.tiers.some((t) => t.tier_id === id)).map(
            (tierId) => (
              <button
                key={tierId}
                className={
                  'question-sheet__tier-tab' +
                  (tierId === activeTier.tier_id ? ' question-sheet__tier-tab--active' : '')
                }
                onClick={() => setActiveTierId(tierId)}
              >
                {TIER_LABELS[tierId]}
              </button>
            )
          )}
        </div>

        <div className="question-sheet__entries">
          {activeTier.entries.map((entry, i) =>
            isLimitEntry(entry) ? (
              <div key={i} className="question-sheet__entry-group">
                <button
                  className="question-sheet__entry question-sheet__entry--limit"
                  onClick={() => handleAsk(entry.question)}
                >
                  <span className="question-sheet__entry-question">{entry.question}</span>
                </button>
                {entry.citations.length > 0 && (
                  <details className="question-sheet__citations" onClick={(e) => e.stopPropagation()}>
                    <summary>Sources</summary>
                    <p className="question-sheet__citations-list">
                      {entry.citations.join(' · ')}
                    </p>
                  </details>
                )}
              </div>
            ) : (
              <div key={i} className="question-sheet__entry-group">
                <button
                  className="question-sheet__entry"
                  onClick={() => handleAsk(entry.opening_question)}
                >
                  <span className="question-sheet__entry-topic">{entry.topic}</span>
                  {entry.why && (
                    <span className="question-sheet__entry-why">{entry.why}</span>
                  )}
                  <span className="question-sheet__entry-question">
                    {entry.opening_question}
                  </span>
                </button>
                {entry.citations.length > 0 && (
                  <details className="question-sheet__citations" onClick={(e) => e.stopPropagation()}>
                    <summary>Sources</summary>
                    <p className="question-sheet__citations-list">
                      {entry.citations.join(' · ')}
                    </p>
                  </details>
                )}
                {entry.follow_ups.length > 0 && (
                  <div className="question-sheet__followups">
                    {entry.follow_ups.map((f, j) => (
                      <button
                        key={j}
                        className="question-sheet__followup"
                        onClick={() => handleAsk(f)}
                      >
                        {f}
                      </button>
                    ))}
                  </div>
                )}
              </div>
            )
          )}
        </div>
      </div>
    </div>
  );
}
