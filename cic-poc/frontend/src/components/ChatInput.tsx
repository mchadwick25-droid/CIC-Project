/** Text input for participant messages. */
import { useCallback, useEffect, useRef, useState } from 'react';
import { useAskAgain } from '../hooks/useAskAgain';
import type { ConversationTurn } from '../hooks/useConversation';
import { deeperEnabled } from '../lib/deeper';
import { askAgainCopy } from '../lib/deeperCopy';

interface ChatInputProps {
  onSend: (message: string) => void;
  placeholder: string;
  disabled?: boolean;
  turns?: ConversationTurn[];
  // Text already in the box when it first appears.
  initialMessage?: string;
  // A sent message is waiting for its reply; without it, a disabled box reads as sending.
  sending?: boolean;
}

export function ChatInput({ onSend, placeholder, disabled = false, turns = [], initialMessage = '', sending = disabled }: ChatInputProps) {
  const [message, setMessage] = useState(initialMessage);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const askAgainRef = useRef<HTMLButtonElement>(null);
  const { pending, submit, confirm, decline } = useAskAgain(turns, onSend);

  const fitHeight = useCallback(() => {
    const textarea = textareaRef.current;
    if (!textarea) return;
    textarea.style.height = 'auto';
    const border = textarea.offsetHeight - textarea.clientHeight;
    textarea.style.height = `${Math.min(textarea.scrollHeight + border, 200)}px`;
  }, []);

  useEffect(fitHeight, [message, fitHeight]);

  // The first measure can run before the web font arrives; measure again then.
  useEffect(() => {
    let live = true;
    document.fonts?.ready.then(() => {
      if (live) fitHeight();
    });
    return () => {
      live = false;
    };
  }, [fitHeight]);

  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      const trimmed = message.trim();
      if (trimmed && !disabled) {
        if (submit(trimmed)) setMessage('');
      }
    },
    [message, disabled, submit]
  );

  const wasAsking = useRef(false);
  useEffect(() => {
    if (pending !== null) askAgainRef.current?.focus();
    else if (wasAsking.current) textareaRef.current?.focus();
    wasAsking.current = pending !== null;
  }, [pending]);

  const keepAsking = () => {
    confirm();
    setMessage('');
  };

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSubmit(e);
      }
    },
    [handleSubmit]
  );

  return (
    <div className="conversation__composer">
      <form className="composer-row" onSubmit={handleSubmit}>
        <textarea
          ref={textareaRef}
          value={message}
          onChange={(e) => {
            setMessage(e.target.value);
            decline();
          }}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          disabled={disabled}
          rows={1}
        />
        <button type="submit" aria-label={sending ? 'Sending…' : 'Send'} disabled={disabled || !message.trim()}>
          <span aria-hidden="true">↑</span>
        </button>
      </form>
      {pending !== null && (
        <div className="ask-again sans" role="group" aria-label={askAgainCopy.body}>
          <p>{deeperEnabled ? askAgainCopy.body : askAgainCopy.bodyFree}</p>
          <div className="ask-again__actions">
            <button ref={askAgainRef} type="button" onClick={keepAsking} disabled={disabled}>
              {askAgainCopy.ask}
            </button>
            <button type="button" onClick={decline}>
              {askAgainCopy.decline}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}
