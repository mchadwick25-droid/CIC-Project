import { useEffect, useLayoutEffect, useRef } from 'react';

const ASKED_TOP_GAP = 16;

/**
 * Keeps the newest question at the top of the transcript once it is sent, and
 * again when the reply begins, so the answer has the screen below it. Room is
 * left under the newest exchange so the question can reach the top; it shrinks
 * as the reply fills the screen. A question stays at rest through height
 * changes (the site's bars fold away, a keyboard opens) until the reader
 * scrolls away from it.
 */
export function useAskedAtRest(participantTurns: number, replyBegun: boolean) {
  const transcriptRef = useRef<HTMLDivElement>(null);
  const askedRef = useRef<HTMLDivElement>(null);
  const roomRef = useRef<HTMLDivElement>(null);
  const restingAt = useRef<number | null>(null);

  const fitRoom = () => {
    const box = transcriptRef.current;
    const asked = askedRef.current;
    const room = roomRef.current;
    if (!box || !asked || !room) return;
    const exchange = room.offsetTop - asked.offsetTop;
    room.style.height = `${Math.max(0, box.clientHeight - exchange - ASKED_TOP_GAP)}px`;
  };
  useLayoutEffect(fitRoom);

  const bringAskedToRest = (smooth: boolean) => {
    const box = transcriptRef.current;
    const asked = askedRef.current;
    if (!box || !asked || typeof box.scrollTo !== 'function') return;
    const top = Math.max(0, asked.offsetTop - ASKED_TOP_GAP);
    restingAt.current = top;
    box.scrollTo({ top, behavior: smooth ? 'smooth' : 'auto' });
  };

  useEffect(() => {
    const still = window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
    bringAskedToRest(!still);
  }, [participantTurns, replyBegun]);

  useEffect(() => {
    const box = transcriptRef.current;
    if (!box || typeof ResizeObserver === 'undefined') return;
    const observer = new ResizeObserver(() => {
      fitRoom();
      if (restingAt.current !== null) bringAskedToRest(false);
    });
    const leaveRest = () => {
      restingAt.current = null;
    };
    const moves = ['wheel', 'touchmove', 'keydown'] as const;
    observer.observe(box);
    moves.forEach((type) => box.addEventListener(type, leaveRest, { passive: true }));
    return () => {
      observer.disconnect();
      moves.forEach((type) => box.removeEventListener(type, leaveRest));
    };
  }, []);

  return { transcriptRef, askedRef, roomRef };
}
