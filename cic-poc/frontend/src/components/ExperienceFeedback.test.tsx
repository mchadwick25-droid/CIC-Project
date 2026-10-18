import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { useState } from 'react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { ExperienceFeedbackButton, ExperienceFeedbackCard } from './ExperienceFeedback';

function Harness({ page }: { page: string }) {
  const [open, setOpen] = useState(false);
  return (
    <>
      <ExperienceFeedbackButton open={open} onToggle={() => setOpen((o) => !o)} />
      {open && <ExperienceFeedbackCard page={page} onClose={() => setOpen(false)} />}
    </>
  );
}

describe('ExperienceFeedback', () => {
  let fetchMock: ReturnType<typeof vi.fn>;
  beforeEach(() => {
    fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
  });
  afterEach(() => {
    cleanup();
    vi.unstubAllGlobals();
  });

  it('opens a dialog, focuses the first field, and closes on Escape', () => {
    render(<Harness page="fix" />);
    fireEvent.click(screen.getByRole('button', { name: 'Tell us what you think' }));
    const dialog = screen.getByRole('dialog');
    expect(dialog.getAttribute('aria-labelledby')).toBe('experience-feedback-title');
    expect(document.activeElement).toBe(screen.getByLabelText('What was this like for you? What should we do better?'));
    fireEvent.keyDown(dialog, { key: 'Escape' });
    expect(screen.queryByRole('dialog')).toBeNull();
    expect(document.activeElement).toBe(screen.getByRole('button', { name: 'Tell us what you think' }));
  });

  it('defaults consent to No and enables the first name only for that option', () => {
    render(<Harness page="fix" />);
    fireEvent.click(screen.getByRole('button', { name: 'Tell us what you think' }));
    const name = screen.getByLabelText('First name') as HTMLInputElement;
    expect((screen.getByLabelText('No') as HTMLInputElement).checked).toBe(true);
    expect(name.disabled).toBe(true);
    fireEvent.click(screen.getByLabelText('Yes, with my first name:'));
    expect(name.disabled).toBe(false);
    fireEvent.click(screen.getByLabelText('Yes, without my name'));
    expect(name.disabled).toBe(true);
    expect(screen.getByText(/A person reads these, usually within a week\./)).toBeTruthy();
  });

  it('posts the comment with the page id and thanks the sender', async () => {
    render(<Harness page="table:alx+syr" />);
    fireEvent.click(screen.getByRole('button', { name: 'Tell us what you think' }));
    expect((screen.getByRole('button', { name: 'Send' }) as HTMLButtonElement).disabled).toBe(true);
    fireEvent.change(screen.getByLabelText('What was this like for you? What should we do better?'), { target: { value: 'It felt close.' } });
    fireEvent.click(screen.getByLabelText('Yes, with my first name:'));
    fireEvent.change(screen.getByLabelText('First name'), { target: { value: 'Ana' } });
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    });
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('/api/feedback');
    expect(init.headers.Authorization).toBeUndefined();
    expect(JSON.parse(init.body)).toEqual({
      kind: 'comment', page: 'table:alx+syr', text: 'It felt close.', quote_consent: 'first_name', first_name: 'Ana', email: null,
    });
    expect(screen.getByRole('status').textContent).toBe('Thank you. A person reads these each week.');
  });

  it('shows the alert and keeps the text when sending fails', async () => {
    fetchMock.mockResolvedValue({ ok: false, status: 500, statusText: 'x', json: async () => ({}) });
    render(<Harness page="fix" />);
    fireEvent.click(screen.getByRole('button', { name: 'Tell us what you think' }));
    const box = screen.getByLabelText('What was this like for you? What should we do better?') as HTMLTextAreaElement;
    fireEvent.change(box, { target: { value: 'Slow.' } });
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    });
    expect(screen.getByRole('alert').textContent).toBe("That didn't go through. Try again in a moment.");
    expect(box.value).toBe('Slow.');
    expect(JSON.parse(fetchMock.mock.calls[0][1].body).quote_consent).toBe('no');
  });
});
