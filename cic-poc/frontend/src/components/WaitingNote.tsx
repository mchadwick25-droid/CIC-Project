import { useRef } from 'react';
import { Enter } from './Enter';
import { ThinkingBook } from './ThinkingBook';

interface WaitingNoteProps {
  show: boolean;
  label: string;
}

export function WaitingNote({ show, label }: WaitingNoteProps) {
  const shownBefore = useRef(show);
  if (show) shownBefore.current = true;
  if (!shownBefore.current) return null;
  return (
    <Enter shown={show}>
      <p className="waiting-note sans" role={show ? 'status' : undefined}>
        <ThinkingBook />
        {label}
      </p>
    </Enter>
  );
}
