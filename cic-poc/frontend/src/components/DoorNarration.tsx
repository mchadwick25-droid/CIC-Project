/**
 * The Facilitator's welcome, spoken. One recorded file per world, made once
 * from the same door text the transcript shows (see
 * Build/tools/generate_door_narration.py), so nothing is generated while the
 * participant waits.
 *
 * It starts by itself a moment after the conversation page loads. A browser
 * may refuse sound that nobody asked for; the participant then sees a plain
 * "Hear the welcome" button, and a tap plays it. It stops when the participant
 * sends a message or leaves the screen. If the file is missing, nothing is
 * shown at all.
 */
import { useEffect, useRef, useState } from 'react';
import { cancelReadAloud } from '../lib/readAloud';

export const DOOR_PAUSE_MS = 1200;

interface DoorNarrationProps {
  worldKey: string;
  // Counts the participant's own messages; the welcome stops when it rises.
  participantTurns: number;
}

type PlayState = 'idle' | 'playing' | 'unavailable';

export function DoorNarration({ worldKey, participantTurns }: DoorNarrationProps) {
  const [state, setState] = useState<PlayState>('idle');
  const audioRef = useRef<HTMLAudioElement | null>(null);

  useEffect(() => {
    const audio = new Audio(`/audio/door/${worldKey}.mp3`);
    audio.preload = 'none';
    audio.addEventListener('ended', () => setState('idle'));
    audio.addEventListener('error', () => setState('unavailable'));
    audioRef.current = audio;
    const timer = window.setTimeout(() => {
      cancelReadAloud();
      audio.play().then(() => setState('playing'), () => setState('idle'));
    }, DOOR_PAUSE_MS);
    return () => {
      window.clearTimeout(timer);
      audio.pause();
      audioRef.current = null;
    };
  }, [worldKey]);

  useEffect(() => {
    const audio = audioRef.current;
    if (participantTurns > 0 && audio && !audio.paused) {
      audio.pause();
      setState('idle');
    }
  }, [participantTurns]);

  if (state === 'unavailable') return null;

  const handleClick = () => {
    const audio = audioRef.current;
    if (!audio) return;
    if (state === 'playing') {
      audio.pause();
      audio.currentTime = 0;
      setState('idle');
      return;
    }
    cancelReadAloud();
    audio.play().then(() => setState('playing'), () => setState('idle'));
  };

  return (
    <div className="door-narration sans">
      <button type="button" className="read-aloud-control sans" onClick={handleClick} aria-pressed={state === 'playing'}>
        {state === 'playing' ? 'Stop the welcome' : 'Hear the welcome'}
      </button>
      <span className="door-narration__note">Synthesized voice — not a recording.</span>
    </div>
  );
}
