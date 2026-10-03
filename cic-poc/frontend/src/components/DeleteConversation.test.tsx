import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { DeleteConversation } from './DeleteConversation';

describe('DeleteConversation', () => {
  afterEach(cleanup);

  it('asks before deleting and deletes on confirm', async () => {
    const onDelete = vi.fn().mockResolvedValue(undefined);
    render(<DeleteConversation onDelete={onDelete} />);
    fireEvent.click(screen.getByText('Delete this conversation'));
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
    render(<DeleteConversation onDelete={onDelete} />);
    fireEvent.click(screen.getByText('Delete this conversation'));
    fireEvent.click(screen.getByText('Keep it'));
    expect(onDelete).not.toHaveBeenCalled();
    expect(screen.getByText('Delete this conversation')).toBeTruthy();
  });

  it('says nothing was deleted when the request fails', async () => {
    const onDelete = vi.fn().mockRejectedValue(new Error('network'));
    render(<DeleteConversation onDelete={onDelete} />);
    fireEvent.click(screen.getByText('Delete this conversation'));
    await act(async () => {
      fireEvent.click(screen.getByText('Delete'));
    });
    expect(screen.getByRole('alert').textContent).toContain('nothing was deleted');
  });
});
