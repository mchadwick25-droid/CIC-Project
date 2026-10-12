import { useCallback, useEffect, useState } from 'react';
import type { ConversationTurn } from './useConversation';

const normalise = (text: string) => text.trim().replace(/\s+/g, ' ').toLowerCase();

const isReply = (turn: ConversationTurn) => turn.speaker !== 'participant' && turn.speaker !== 'facilitator' && turn.text !== '';

// True when this exact question was asked before and a voice answered it.
// A question still waiting, turned away, or met only by the Facilitator is
// not answered; the latest time it was asked decides, so a retry after a
// failure is not a repeat.
export function isAnsweredRepeat(turns: ConversationTurn[], text: string): boolean {
  const wanted = normalise(text);
  let latestAnswered = false;
  turns.forEach((turn, i) => {
    if (turn.speaker !== 'participant' || normalise(turn.text) !== wanted) return;
    let answered = false;
    for (let j = i + 1; j < turns.length && turns[j].speaker !== 'participant'; j += 1) {
      if (isReply(turns[j])) answered = true;
    }
    latestAnswered = answered;
  });
  return latestAnswered;
}

export function useAskAgain(turns: ConversationTurn[], send: (text: string) => void) {
  const [pending, setPending] = useState<string | null>(null);

  const submit = useCallback(
    (text: string): boolean => {
      if (isAnsweredRepeat(turns, text)) {
        setPending(text);
        return false;
      }
      send(text);
      return true;
    },
    [turns, send]
  );

  const confirm = useCallback(() => {
    if (pending === null) return;
    setPending(null);
    send(pending);
  }, [pending, send]);

  const decline = useCallback(() => setPending(null), []);

  useEffect(() => {
    if (pending === null) return undefined;
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') setPending(null);
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [pending]);

  return { pending, submit, confirm, decline };
}
