import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { DeleteConversation } from './DeleteConversation';

describe('DeleteConversation', () => {
  afterEach(cleanup);

  it('asks before deleting and deletes on confirm', async () => {
    const onDelete = vi.fn().mockResolvedValue(undefined);
    render(<DeleteConversation onDelete={onDelete} onCancel={vi.fn()} />);
    expect(screen.getByText('Delete this conversation?')).toBeTruthy();
    expect(screen.getByText(/cannot be recovered\. Copies in our daily backups are gone within 14 days\./)).toBeTruthy();
    expect(onDelete).not.toHaveBeenCalled();
    await act(async () => {
      fireEvent.click(screen.getByText('Delete'));
    });
    expect(onDelete).toHaveBeenCalledTimes(1);
  });

  it('keeps the conversation when the participant chooses Keep it', () => {
    const onDelete = vi.fn();
    const onCancel = vi.fn();
    render(<DeleteConversation onDelete={onDelete} onCancel={onCancel} />);
    fireEvent.click(screen.getByText('Keep it'));
    expect(onDelete).not.toHaveBeenCalled();
    expect(onCancel).toHaveBeenCalledTimes(1);
  });

  it('says nothing was deleted when the request fails', async () => {
    const onDelete = vi.fn().mockRejectedValue(new Error('network'));
    render(<DeleteConversation onDelete={onDelete} onCancel={vi.fn()} />);
    await act(async () => {
      fireEvent.click(screen.getByText('Delete'));
    });
    expect(screen.getByRole('alert').textContent).toContain('nothing was deleted');
  });
});
