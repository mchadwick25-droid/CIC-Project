/**
 * ChatInput component - text input for participant messages.
 */

import { useState, useCallback, useRef, useEffect } from 'react';
import { QuestionSheet } from './QuestionSheet';
import { getGuidedStartersForTable } from '../data/guidedStarters';

interface ChatInputProps {
  onSend: (message: string) => void;
  onEnd: () => void;
  disabled?: boolean;
  isLoading?: boolean;
  /** World(s) seated at this table - resolves which Guided Starters content
   * "Don't know what to ask?" offers. The affordance itself stays hidden
   * (not just disabled) if none of the seated worlds have drafted content. */
  worldIds?: string[];
}

export function ChatInput({
  onSend,
  onEnd,
  disabled = false,
  isLoading = false,
  worldIds = [],
}: ChatInputProps) {
  const [message, setMessage] = useState('');
  const [isQuestionSheetOpen, setIsQuestionSheetOpen] = useState(false);
  const textareaRef = useRef<HTMLTextAreaElement>(null);
  const guidedStarterWorlds = getGuidedStartersForTable(worldIds);

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

  // "Dismisses on typing" (UX Design V1.0 §4.1) - the sheet closes the
  // moment the participant starts typing their own message.
  const handleChange = useCallback((e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setMessage(e.target.value);
    setIsQuestionSheetOpen(false);
  }, []);

  const handleAskGuidedQuestion = useCallback(
    (question: string) => {
      if (!disabled && !isLoading) {
        onSend(question);
      }
    },
    [disabled, isLoading, onSend]
  );

  return (
    <div className="chat-input-container">
      {guidedStarterWorlds.length > 0 && (
        <div className="chat-input__dont-know-row">
          <button
            type="button"
            className="chat-input__dont-know"
            onClick={() => setIsQuestionSheetOpen((v) => !v)}
            disabled={disabled}
          >
            Don't know what to ask?
          </button>
        </div>
      )}
      <form className="chat-form" onSubmit={handleSubmit}>
        <textarea
          ref={textareaRef}
          className="chat-input"
          value={message}
          onChange={handleChange}
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

      {isQuestionSheetOpen && (
        <QuestionSheet
          worlds={guidedStarterWorlds}
          onAsk={handleAskGuidedQuestion}
          onClose={() => setIsQuestionSheetOpen(false)}
        />
      )}
    </div>
  );
}
