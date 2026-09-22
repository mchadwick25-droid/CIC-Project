/**
 * Read-aloud step 1 (design note: Ministry/Technology/
 * CiC_ReadAloud_Step1_Design_Note.md). ONE global control, in the
 * conversation bar - not a per-turn or per-sentence button. Two reasons,
 * not one:
 *   - R17 already caps how many on-screen transparency elements a turn
 *     may carry (VoiceTurnBody.tsx); this feature adds a second axis of
 *     on-screen chrome, and the same minimal-elements ethos argues for
 *     one instance for the whole screen, not one per turn.
 *   - A Facilitator turn (Conversation.tsx/TableRoom.tsx) has no speaker
 *     row at all - it is DELIBERATELY unlabeled (CiC_Full_UX_Design_V1_0
 *     .md: "a participant learns to recognize the voice by how it reads,
 *     not by a name tag"). A turn-level button would have to invent a row
 *     that design intentionally left out; a global control never touches
 *     Facilitator markup at all.
 *
 * Always reads the latest completed voice/Facilitator turn (never a
 * participant's own typed text - they just wrote it). Replaying an
 * older turn is out of this step's scope; Q8's usage metric is exactly
 * what would justify building that later.
 *
 * Never auto-plays - the only way this ever speaks is this button's own
 * click. A participant already using a screen reader is therefore never
 * double-spoken: this is simply another button their own reader
 * announces, silent until pressed, same as every other control on the
 * page (design note Q4).
 *
 * Disclosure copy (design note Q7 - what tells a participant "this is
 * your browser reading, not {representative_name} speaking") is drafted
 * in the design note and escalated to Mark, not shipped here. Do not add
 * participant-facing disclosure text to this component until that
 * ruling lands, even behind the flag.
 */
import { useEffect, useRef, useState } from 'react';
import { cancelReadAloud, recordReadAloudPlay, speakText } from '../lib/readAloud';
import { useReadAloudAvailability } from '../hooks/useReadAloudAvailability';

interface ReadAloudControlProps {
  text: string;
  turnKey: string | number;
}

type PlayState = 'idle' | 'playing';

export function ReadAloudControl({ text, turnKey }: ReadAloudControlProps) {
  const available = useReadAloudAvailability();
  const [state, setState] = useState<PlayState>('idle');
  const lastKeyRef = useRef(turnKey);

  // A new turn arriving mid-playback (the participant sent another
  // message while an earlier answer was still being read) stops the
  // earlier one rather than letting two turns' audio ever overlap - the
  // same "only one thing speaks at a time" guarantee a single global
  // control exists to buy.
  useEffect(() => {
    if (lastKeyRef.current !== turnKey) {
      lastKeyRef.current = turnKey;
      cancelReadAloud();
      setState('idle');
    }
  }, [turnKey]);

  // Leaving the screen (or the flag turning this control off mid-session
  // via HMR) must not leave the browser talking to an empty page.
  useEffect(() => () => cancelReadAloud(), []);

  if (!available) return null;

  const handleClick = () => {
    if (state === 'playing') {
      cancelReadAloud();
      setState('idle');
      return;
    }
    setState('playing');
    recordReadAloudPlay();
    speakText(text, () => setState('idle'));
  };

  return (
    <button
      type="button"
      className="read-aloud-control sans"
      onClick={handleClick}
      aria-pressed={state === 'playing'}
    >
      {state === 'playing' ? 'Stop reading' : 'Read aloud'}
    </button>
  );
}
