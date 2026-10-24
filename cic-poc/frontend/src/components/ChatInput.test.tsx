import { act, fireEvent, render, within } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { ChatInput } from './ChatInput';

describe('ChatInput', () => {
  it('disables Send and the textarea while a turn is in flight', () => {
    const { container } = render(<ChatInput onSend={vi.fn()} placeholder="" label="Ask Theon" disabled />);

    expect(within(container).getByRole('button', { name: 'Sending…' })).toBeDisabled();
    expect(within(container).getByRole('textbox')).toBeDisabled();
  });

  it('names the arrow button Send when it is waiting for words', () => {
    const { container } = render(<ChatInput onSend={vi.fn()} placeholder="Ask Theon…" label="Ask Theon" />);

    expect(within(container).getByRole('button', { name: 'Send' })).toBeDisabled();
    expect(within(container).getByPlaceholderText('Ask Theon…')).toBeEnabled();
  });

  it('gives the box a name that stays when the placeholder goes', () => {
    const { container } = render(<ChatInput onSend={vi.fn()} placeholder="Ask Theon…" label="Ask Theon" />);
    const box = within(container).getByRole('textbox', { name: 'Ask Theon' });
    fireEvent.change(box, { target: { value: 'Who are you?' } });
    expect(within(container).getByRole('textbox', { name: 'Ask Theon' })).toBeInTheDocument();
  });

  it('returns the cursor to the box after a send, once the reply has come', () => {
    const send = vi.fn();
    const view = render(<ChatInput onSend={send} placeholder="Ask Theon…" label="Ask Theon" />);
    const box = within(view.container).getByRole('textbox') as HTMLTextAreaElement;
    box.focus();
    fireEvent.change(box, { target: { value: 'Who are you?' } });
    fireEvent.keyDown(box, { key: 'Enter' });
    expect(send).toHaveBeenCalledWith('Who are you?');
    view.rerender(<ChatInput onSend={send} placeholder="Ask Theon…" label="Ask Theon" disabled />);
    act(() => box.blur());
    view.rerender(<ChatInput onSend={send} placeholder="Ask Theon…" label="Ask Theon" />);
    expect(document.activeElement).toBe(within(view.container).getByRole('textbox'));
  });

  it('does not take the cursor from where the person went in the meantime', () => {
    const send = vi.fn();
    const view = render(
      <>
        <button type="button">Elsewhere</button>
        <ChatInput onSend={send} placeholder="Ask Theon…" label="Ask Theon" />
      </>
    );
    const box = within(view.container).getByRole('textbox') as HTMLTextAreaElement;
    fireEvent.change(box, { target: { value: 'Who are you?' } });
    fireEvent.keyDown(box, { key: 'Enter' });
    const other = within(view.container).getByRole('button', { name: 'Elsewhere' });
    other.focus();
    view.rerender(
      <>
        <button type="button">Elsewhere</button>
        <ChatInput onSend={send} placeholder="Ask Theon…" label="Ask Theon" disabled />
      </>
    );
    view.rerender(
      <>
        <button type="button">Elsewhere</button>
        <ChatInput onSend={send} placeholder="Ask Theon…" label="Ask Theon" />
      </>
    );
    expect(document.activeElement).toBe(other);
  });
});
