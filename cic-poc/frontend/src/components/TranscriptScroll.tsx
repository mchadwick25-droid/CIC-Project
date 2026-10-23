import { useCallback, useEffect, useRef, useState, type ReactNode } from 'react';

interface TranscriptScrollProps {
  children: ReactNode;
  label: string;
  // Changes when a new question is sent: the page follows the conversation again.
  followSignal: number;
}

const AWAY_FROM_LATEST = 60;
const AT_LATEST = 4;
const THUMB_MIN = 28;

function reducedMotion(): boolean {
  return typeof window !== 'undefined' && Boolean(window.matchMedia?.('(prefers-reduced-motion: reduce)').matches);
}

function ease(x: number): number {
  return x < 0.5 ? 4 * x * x * x : 1 - Math.pow(-2 * x + 2, 3) / 2;
}

/**
 * The conversation's own scroll. It stays with the newest line while replies
 * grow, lets the reader go back up (wheel, finger, keys or the gold bar), and
 * offers a way back to the latest.
 */
export function TranscriptScroll({ children, label, followSignal }: TranscriptScrollProps) {
  const boxRef = useRef<HTMLDivElement>(null);
  const trackRef = useRef<HTMLSpanElement>(null);
  const thumbRef = useRef<HTMLSpanElement>(null);
  const mode = useRef<'follow' | 'free' | 'tween'>('follow');
  const tween = useRef<{ from: number; start: number } | null>(null);
  const [away, setAway] = useState(false);

  const goLatest = useCallback(() => {
    const box = boxRef.current;
    if (!box) return;
    if (reducedMotion()) {
      mode.current = 'follow';
      return;
    }
    tween.current = { from: box.scrollTop, start: performance.now() };
    mode.current = 'tween';
  }, []);

  useEffect(() => {
    mode.current = 'follow';
  }, [followSignal]);

  useEffect(() => {
    const box = boxRef.current;
    if (!box) return undefined;
    let frame = 0;
    let wasAway = false;
    const loop = (now: number) => {
      const bottom = box.scrollHeight - box.clientHeight;
      if (mode.current === 'follow') {
        const gap = bottom - box.scrollTop;
        // A browser rounds a scroll position to whole pixels, so a step under a pixel would never arrive.
        const step = Math.abs(gap * 0.08) < 1 ? Math.sign(gap) * Math.min(Math.abs(gap), 1) : gap * 0.08;
        box.scrollTop += reducedMotion() || Math.abs(gap) < 0.5 ? gap : step;
      } else if (mode.current === 'tween' && tween.current) {
        const x = Math.min(1, (now - tween.current.start) / 1500);
        box.scrollTop = tween.current.from + (bottom - tween.current.from) * ease(x);
        if (x >= 1) mode.current = 'follow';
      }
      const distance = bottom - box.scrollTop;
      const isAway = distance > AWAY_FROM_LATEST;
      if (isAway !== wasAway) {
        wasAway = isAway;
        setAway(isAway);
      }
      const track = trackRef.current;
      const thumb = thumbRef.current;
      if (track && thumb) {
        if (bottom <= 1) {
          track.style.visibility = 'hidden';
        } else {
          track.style.visibility = 'visible';
          const height = Math.max(THUMB_MIN, (track.clientHeight * box.clientHeight) / box.scrollHeight);
          thumb.style.height = `${height}px`;
          thumb.style.top = `${((track.clientHeight - height) * box.scrollTop) / bottom}px`;
        }
      }
      frame = requestAnimationFrame(loop);
    };
    frame = requestAnimationFrame(loop);

    const leave = () => {
      mode.current = 'free';
    };
    const onKey = (event: KeyboardEvent) => {
      if (['ArrowUp', 'PageUp', 'Home'].includes(event.key)) leave();
    };
    const onScroll = () => {
      if (mode.current === 'free' && box.scrollHeight - box.clientHeight - box.scrollTop < AT_LATEST) mode.current = 'follow';
    };
    box.addEventListener('wheel', leave, { passive: true });
    box.addEventListener('touchmove', leave, { passive: true });
    box.addEventListener('keydown', onKey);
    box.addEventListener('scroll', onScroll, { passive: true });
    return () => {
      cancelAnimationFrame(frame);
      box.removeEventListener('wheel', leave);
      box.removeEventListener('touchmove', leave);
      box.removeEventListener('keydown', onKey);
      box.removeEventListener('scroll', onScroll);
    };
  }, []);

  const dragging = useRef<{ y: number; top: number } | null>(null);
  const onThumbDown = (event: React.PointerEvent<HTMLSpanElement>) => {
    dragging.current = { y: event.clientY, top: boxRef.current?.scrollTop ?? 0 };
    mode.current = 'free';
    event.currentTarget.setPointerCapture(event.pointerId);
  };
  const onThumbMove = (event: React.PointerEvent<HTMLSpanElement>) => {
    const drag = dragging.current;
    const box = boxRef.current;
    const track = trackRef.current;
    const thumb = thumbRef.current;
    if (!drag || !box || !track || !thumb) return;
    const room = track.clientHeight - thumb.offsetHeight || 1;
    box.scrollTop = drag.top + ((event.clientY - drag.y) * (box.scrollHeight - box.clientHeight)) / room;
  };
  const onThumbUp = () => {
    dragging.current = null;
  };

  return (
    <div className="conv-scroll">
      <div className="conversation__transcript" role="log" aria-label={label} tabIndex={0} ref={boxRef}>
        {children}
      </div>
      <span className="conv-scroll__track" ref={trackRef} aria-hidden="true">
        <span className="conv-scroll__thumb" ref={thumbRef} onPointerDown={onThumbDown} onPointerMove={onThumbMove} onPointerUp={onThumbUp} onPointerCancel={onThumbUp} />
      </span>
      {away && (
        <button type="button" className="conv-scroll__latest sans" onClick={goLatest}>
          Latest ↓
        </button>
      )}
    </div>
  );
}
