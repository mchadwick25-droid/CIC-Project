/**
 * Text input for participant messages.
 *
 * "Leave for now" (not "End the conversation"): MessageRequest is only
 * {text, client_msg_id} - there is no close-intent field, so this can only
 * navigate away client-side. The session is not actually closed server-side
 * and stays resumable by its code, so the label says what really happens.
 */
import { useCallback, useEffect, useRef, useState } from 'react';

interface ChatInputProps {
  onSend: (message: string) => void;
  onEnd: () => void;
  placeholder: string;
  disabled?: boolean;
}

export function ChatInput({ onSend, onEnd, placeholder, disabled = false }: ChatInputProps) {
  const [message, setMessage] = useState('');
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    const textarea = textareaRef.current;
    if (textarea) {
      textarea.style.height = 'auto';
      textarea.style.height = `${Math.min(textarea.scrollHeight, 200)}px`;
    }
  }, [message]);

  const handleSubmit = useCallback(
    (e: React.FormEvent) => {
      e.preventDefault();
      const trimmed = message.trim();
      if (trimmed && !disabled) {
        onSend(trimmed);
        setMessage('');
      }
    },
    [message, disabled, onSend]
  );

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
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder={placeholder}
          disabled={disabled}
          rows={1}
        />
        <button type="submit" disabled={disabled || !message.trim()}>
          {disabled ? 'Sending…' : 'Send'}
        </button>
      </form>
      <div className="conversation__end">
        {/* Stage 0b (Build-Plan.md): Leave never takes `disabled` - a
            participant mid-turn or inside an open Table round must still
            be able to walk away. Only Send/the textarea gate on it. */}
        <button type="button" onClick={onEnd}>
          Leave for now
        </button>
      </div>
    </div>
  );
}
