import { useEffect, useLayoutEffect, useRef, useState, type ReactNode } from 'react';

const CLOSE_MS = 700;

interface EnterProps {
  children: ReactNode;
  // Already on screen when the page opened: no opening motion.
  still?: boolean;
  // Closes the block smoothly when false.
  shown?: boolean;
  // No space left under the block.
  flush?: boolean;
}

/** Opens and closes a block from and to nothing, so what follows it moves smoothly instead of jumping. A closed block leaves the page once it has shut. */
export function Enter({ children, still = false, shown = true, flush = false }: EnterProps) {
  const [ready, setReady] = useState(still);
  const ref = useRef<HTMLDivElement>(null);
  useLayoutEffect(() => {
    // Settle the closed state in a style pass first, or the browser has nothing to open from.
    if (!ready) void ref.current?.offsetHeight;
  }, [ready]);
  useEffect(() => {
    if (ready) return undefined;
    const frame = requestAnimationFrame(() => setReady(true));
    return () => cancelAnimationFrame(frame);
  }, [ready]);
  const [gone, setGone] = useState(false);
  useEffect(() => {
    if (shown) {
      if (gone) {
        setGone(false);
        setReady(false);
      }
      return undefined;
    }
    const timer = window.setTimeout(() => setGone(true), CLOSE_MS);
    return () => window.clearTimeout(timer);
  }, [shown, gone]);
  if (gone) return null;
  return (
    <div ref={ref} className={`enter${ready && shown ? ' enter--open' : ''}${flush ? ' enter--flush' : ''}`}>
      <div className="enter__clip">
        <div className="enter__body">{children}</div>
      </div>
    </div>
  );
}
