/**
 * ChatInput component - text input for participant messages.
 */

import { useState, useCallback, useRef, useEffect } from 'react';

interface ChatInputProps {
  onSend: (message: string) => void;
  onEnd: () => void;
  disabled?: boolean;
  isLoading?: boolean;
}

export function ChatInput({ onSend, onEnd, disabled = false, isLoading = false }: ChatInputProps) {
  const [message, setMessage] = useState('');
  const textareaRef = useRef<HTMLTextAreaElement>(null);

  // Auto-resize textarea
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
      if (trimmed && !disabled && !isLoading) {
        onSend(trimmed);
        setMessage('');
      }
    },
    [message, disabled, isLoading, onSend]
  );

  const handleKeyDown = useCallback(
    (e: React.KeyboardEvent) => {
      // Submit on Enter (without Shift)
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        handleSubmit(e);
      }
    },
    [handleSubmit]
  );

  return (
    <div className="chat-input-container">
      <form className="chat-form" onSubmit={handleSubmit}>
        <textarea
          ref={textareaRef}
          className="chat-input"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyDown={handleKeyDown}
          placeholder="Share your thoughts or ask a question..."
          disabled={disabled || isLoading}
          rows={1}
        />
        <button
          type="submit"
          className="chat-button"
          disabled={disabled || isLoading || !message.trim()}
        >
          {isLoading ? 'Sending...' : 'Send'}
        </button>
        <button
          type="button"
          className="chat-button chat-button--secondary"
          onClick={onEnd}
          disabled={disabled || isLoading}
        >
          End
        </button>
      </form>
    </div>
  );
}
