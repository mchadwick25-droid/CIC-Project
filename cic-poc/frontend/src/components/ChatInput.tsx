/**
 * Text input for participant messages.
 *
 * "Leave for now" (not "End the conversation"): MessageRequest is only
 * {text, client_msg_id} - there is no close-intent field, so this can only
 * navigate away client-side. The session is not actually closed server-side
 * and stays resumable by its code, so the label says what really happens.
 */
import { useCallback, useEffect, useRef, useState, type ReactNode } from 'react';
import { GoDeeperPanel } from './GoDeeperPanel';
import { useAskAgain } from '../hooks/useAskAgain';
import type { ConversationTurn } from '../hooks/useConversation';
import { deeperEnabled } from '../lib/deeper';
import { askAgainCopy } from '../lib/deeperCopy';

interface ChatInputProps {
  onSend: (message: string) => void;
  onEnd: () => void;
  placeholder: string;
  disabled?: boolean;
  turns?: ConversationTurn[];
  // Shown beside "Leave for now", under the box.
  endExtra?: ReactNode;
  // Text already in the box when it first appears.
  initialMessage?: string;
  // A sent message is waiting for its reply; without it, a disabled box reads as sending.
  sending?: boolean;
}

export function ChatInput({ onSend, onEnd, placeholder, disabled = false, turns = [], endExtra, initialMessage = '', sending = disabled }: ChatInputProps) {
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
        <button type="submit" disabled={disabled || !message.trim()}>
          {sending ? 'Sending…' : 'Send'}
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
      <div className={endExtra ? 'conversation__end conversation__end--with-extra' : 'conversation__end'}>
        {endExtra}
        {/* Stage 0b (Build-Plan.md): Leave never takes `disabled` - a
            participant mid-turn or inside an open Table round must still
            be able to walk away. Only Send/the textarea gate on it. */}
        <button type="button" onClick={onEnd}>
          Leave for now
        </button>
      </div>
      <GoDeeperPanel />
    </div>
  );
}
