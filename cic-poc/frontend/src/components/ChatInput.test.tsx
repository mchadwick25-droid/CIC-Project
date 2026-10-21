import { render, within } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { ChatInput } from './ChatInput';

describe('ChatInput', () => {
  it('disables Send and the textarea while a turn is in flight', () => {
    const { container } = render(<ChatInput onSend={vi.fn()} placeholder="" disabled />);

    expect(within(container).getByRole('button', { name: 'Sending…' })).toBeDisabled();
    expect(within(container).getByRole('textbox')).toBeDisabled();
  });

  it('names the arrow button Send when it is waiting for words', () => {
    const { container } = render(<ChatInput onSend={vi.fn()} placeholder="Ask Theon…" />);

    expect(within(container).getByRole('button', { name: 'Send' })).toBeDisabled();
    expect(within(container).getByPlaceholderText('Ask Theon…')).toBeEnabled();
  });
});
