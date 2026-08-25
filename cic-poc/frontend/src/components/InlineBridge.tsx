/**
 * One reusable inline disclosure mark for the transparency apparatus's
 * shared grammar (CiC_Full_UX_Design_V1_0.md §2.4, §5.7: "one grammar,
 * five applications, no feature may introduce a sixth verb"). Used first
 * by the name/figure bridge; the same component is meant to carry lexicon
 * glosses when that track is built, rather than a second implementation
 * of the same two verbs.
 *
 * Desktop: hover opens Level 2, click opens Level 3, mouse-leave closes
 * Level 2 (never Level 3 - only the panel's own close/Esc does that).
 * Phone: tap opens Level 2 (with its one "Full entry →" action to reach
 * Level 3); tapping outside the mark dismisses it.
 */
import { useEffect, useRef, useState } from 'react';
import { useIsPhone } from '../hooks/useBreakpoint';
import { Level2Card } from './Level2Card';
import { Level3Panel } from './Level3Panel';

type OpenState = 'closed' | 'level2' | 'level3';

interface InlineBridgeProps {
  label: string;
  markClassName: string;
  level2: React.ReactNode;
  level3Title: string;
  level3: React.ReactNode;
  ariaLabel?: string;
}

export function InlineBridge({ label, markClassName, level2, level3Title, level3, ariaLabel }: InlineBridgeProps) {
  const isPhone = useIsPhone();
  const [open, setOpen] = useState<OpenState>('closed');
  const [anchor, setAnchor] = useState<DOMRect | null>(null);
  const wrapperRef = useRef<HTMLSpanElement>(null);
  const markRef = useRef<HTMLButtonElement>(null);

  useEffect(() => {
    if (open !== 'level2' || !isPhone) return;
    function onOutside(e: MouseEvent) {
      if (wrapperRef.current && !wrapperRef.current.contains(e.target as Node)) setOpen('closed');
    }
    document.addEventListener('mousedown', onOutside);
    return () => document.removeEventListener('mousedown', onOutside);
  }, [open, isPhone]);

  // Measured once per open, not tracked continuously - the mark is
  // static text in a paragraph, not something that moves while its own
  // card is showing (Level 2 closes on hover-out/tap-elsewhere well
  // before a reflow would matter).
  const openLevel2 = () => {
    if (markRef.current) setAnchor(markRef.current.getBoundingClientRect());
    setOpen((o) => (o === 'level3' ? o : 'level2'));
  };

  const deskHandlers = isPhone
    ? {}
    : {
        onMouseEnter: openLevel2,
        onMouseLeave: () => setOpen((o) => (o === 'level3' ? o : 'closed')),
        onFocus: openLevel2,
        onBlur: () => setOpen((o) => (o === 'level3' ? o : 'closed')),
      };

  const handleClick = () => {
    if (isPhone) {
      if (open === 'closed') openLevel2();
    } else {
      setOpen('level3');
    }
  };

  return (
    <span className="inline-bridge" ref={wrapperRef}>
      <button type="button" className={markClassName} onClick={handleClick} ref={markRef} aria-label={ariaLabel} {...deskHandlers}>
        {label}
      </button>
      {open === 'level2' && anchor && (
        <Level2Card showFullEntry={isPhone} onFullEntry={() => setOpen('level3')} anchor={anchor}>
          {level2}
        </Level2Card>
      )}
      {open === 'level3' && (
        <Level3Panel title={level3Title} onClose={() => setOpen('closed')}>
          {level3}
        </Level3Panel>
      )}
    </span>
  );
}
