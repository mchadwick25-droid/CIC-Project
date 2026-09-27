/**
 * ONE global control, in the conversation bar - not a per-turn or
 * per-sentence button. Two reasons, not one:
 *   - VoiceTurnBody.tsx already caps how many on-screen transparency
 *     elements a turn may carry; this feature adds a second axis of
 *     on-screen chrome, and the same minimal-elements ethos argues for
 *     one instance for the whole screen, not one per turn.
 *   - A Facilitator turn (Conversation.tsx/TableRoom.tsx) has no speaker
 *     row at all - it is deliberately unlabeled, so a participant learns
 *     to recognize the voice by how it reads, not by a name tag. A
 *     turn-level button would have to invent a row that design
 *     intentionally left out; a global control never touches Facilitator
 *     markup at all.
 *
 * Always reads the latest completed voice/Facilitator turn (never a
 * participant's own typed text - they just wrote it). Replaying an
 * older turn is out of scope for now.
 *
 * Never auto-plays - the only way this ever speaks is this button's own
 * click. A participant already using a screen reader is therefore never
 * double-spoken: this is simply another button their own reader
 * announces, silent until pressed, same as every other control on the
 * page.
 */
import { useEffect, useRef, useState } from 'react';
import { cancelReadAloud, recordReadAloudPlay, speakText } from '../lib/readAloud';
import { useReadAloudAvailability } from '../hooks/useReadAloudAvailability';

interface ReadAloudControlProps {
  text: string;
  turnKey: string | number;
  // Table sessions pass the speaking Representative's own assigned voice
  // (lib/readAloud.ts's pickVoiceForSeat) so seated voices don't all sound
  // identical; an interview passes nothing and gets the browser's default.
  voice?: SpeechSynthesisVoice;
}

type PlayState = 'idle' | 'playing';

export function ReadAloudControl({ text, turnKey, voice }: ReadAloudControlProps) {
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
    speakText(text, () => setState('idle'), voice);
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
