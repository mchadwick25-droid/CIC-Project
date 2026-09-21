/**
 * Build-Plan.md Stage 0b: "Leave at ~73 must not take `disabled`; only
 * Send does." Done: "Leave clickable during in-flight turns and open
 * rounds in both modes." `disabled` here stands in for either condition
 * (Conversation.tsx passes `isLoading`; TableRoom.tsx passes
 * `isLoading || roundOpen`) - ChatInput itself doesn't know which.
 */
import { fireEvent, render, within } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import { ChatInput } from './ChatInput';

describe('ChatInput - Leave is never disabled', () => {
  it('stays clickable while disabled is true (in-flight turn / open round)', () => {
    const onEnd = vi.fn();
    const { container } = render(<ChatInput onSend={vi.fn()} onEnd={onEnd} placeholder="" disabled />);

    const leave = within(container).getByRole('button', { name: 'Leave for now' });
    expect(leave).not.toBeDisabled();

    fireEvent.click(leave);
    expect(onEnd).toHaveBeenCalledTimes(1);
  });

  it('still disables Send (and the textarea) while disabled is true - only Leave is exempt', () => {
    const { container } = render(<ChatInput onSend={vi.fn()} onEnd={vi.fn()} placeholder="" disabled />);

    expect(within(container).getByRole('button', { name: 'Sending…' })).toBeDisabled();
    expect(within(container).getByRole('textbox')).toBeDisabled();
  });
});
