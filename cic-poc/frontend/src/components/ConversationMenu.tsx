import { useEffect, useRef, useState, type RefObject } from 'react';

interface ConversationMenuProps {
  buttonRef: RefObject<HTMLButtonElement>;
  aboutLabel: string;
  onAbout: () => void;
  onFeedback: () => void;
  onReport?: () => void;
  onLeave: () => void;
  onDelete?: () => void;
  account?: { label: string; onSelect: () => void };
}

export function ConversationMenu({ buttonRef, aboutLabel, onAbout, onFeedback, onReport, onLeave, onDelete, account }: ConversationMenuProps) {
  const [open, setOpen] = useState(false);
  const listRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    if (!open) return undefined;
    listRef.current?.querySelector<HTMLButtonElement>('button')?.focus();
    const onPointer = (event: PointerEvent) => {
      const target = event.target as Node;
      if (!listRef.current?.contains(target) && !buttonRef.current?.contains(target)) setOpen(false);
    };
    document.addEventListener('pointerdown', onPointer);
    return () => document.removeEventListener('pointerdown', onPointer);
  }, [open, buttonRef]);

  const close = () => {
    setOpen(false);
    buttonRef.current?.focus();
  };

  const choose = (action: () => void) => () => {
    setOpen(false);
    action();
  };

  const onKeyDown = (event: React.KeyboardEvent) => {
    if (event.key === 'Escape') {
      event.stopPropagation();
      close();
      return;
    }
    const items = Array.from(listRef.current?.querySelectorAll<HTMLButtonElement>('button') ?? []);
    const at = items.indexOf(document.activeElement as HTMLButtonElement);
    const to = { ArrowDown: at + 1, ArrowUp: at - 1, Home: 0, End: items.length - 1 }[event.key];
    if (to === undefined) return;
    event.preventDefault();
    items[(to + items.length) % items.length]?.focus();
  };

  return (
    <div className="conv-menu" onKeyDown={open ? onKeyDown : undefined}>
      <button
        ref={buttonRef}
        type="button"
        className="conv-menu__button"
        aria-label="More"
        aria-haspopup="menu"
        aria-expanded={open}
        onClick={() => setOpen((o) => !o)}
      >
        <span aria-hidden="true">⋯</span>
      </button>
      {open && (
        <div className="conv-menu__list sans" role="menu" ref={listRef}>
          {account && (
            <button type="button" role="menuitem" className="conv-menu__account" onClick={choose(account.onSelect)}>
              {account.label}
            </button>
          )}
          <button type="button" role="menuitem" onClick={choose(onAbout)}>
            {aboutLabel}
          </button>
          <button type="button" role="menuitem" onClick={choose(onFeedback)}>
            Tell us what you think
          </button>
          {onReport && (
            <button type="button" role="menuitem" onClick={choose(onReport)}>
              Report a problem
            </button>
          )}
          <button type="button" role="menuitem" onClick={choose(onLeave)}>
            Leave for now
          </button>
          {onDelete && (
            <button type="button" role="menuitem" className="conv-menu__delete" onClick={choose(onDelete)}>
              Delete this conversation
            </button>
          )}
        </div>
      )}
    </div>
  );
}
