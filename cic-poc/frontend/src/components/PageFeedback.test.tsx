import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { PageFeedback } from './PageFeedback';

describe('PageFeedback', () => {
  let fetchMock: ReturnType<typeof vi.fn>;
  beforeEach(() => {
    window.localStorage.clear();
    fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
  });
  afterEach(() => {
    cleanup();
    vi.unstubAllGlobals();
    vi.restoreAllMocks();
  });

  const openCard = () => fireEvent.click(screen.getByRole('button', { name: 'Report a problem' }));
  const send = async () => {
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    });
  };

  it('posts a like with the page id, stays pressed, and remembers it', async () => {
    render(<PageFeedback page="conversation:fix" />);
    const like = screen.getByRole('button', { name: 'This helped' }) as HTMLButtonElement;
    expect(like.getAttribute('aria-pressed')).toBe('false');
    await act(async () => {
      fireEvent.click(like);
    });
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('/api/feedback');
    expect(init.headers.Authorization).toBeUndefined();
    expect(JSON.parse(init.body)).toEqual({ kind: 'like', page: 'conversation:fix' });
    expect(like.getAttribute('aria-pressed')).toBe('true');
    expect(like.disabled).toBe(true);
    fireEvent.click(like);
    expect(fetchMock).toHaveBeenCalledTimes(1);
    cleanup();
    render(<PageFeedback page="conversation:fix" />);
    expect(screen.getByRole('button', { name: 'This helped' }).getAttribute('aria-pressed')).toBe('true');
  });

  it('keeps a like per page', () => {
    window.localStorage.setItem('cic-page-like:table:alx-syr', '1');
    render(<PageFeedback page="conversation:fix" />);
    expect(screen.getByRole('button', { name: 'This helped' }).getAttribute('aria-pressed')).toBe('false');
  });

  it('leaves the like unpressed when sending fails', async () => {
    fetchMock.mockResolvedValue({ ok: false, status: 500, statusText: 'x', json: async () => ({}) });
    render(<PageFeedback page="fix" />);
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'This helped' }));
    });
    expect(screen.getByRole('button', { name: 'This helped' }).getAttribute('aria-pressed')).toBe('false');
    expect(window.localStorage.getItem('cic-page-like:fix')).toBeNull();
  });

  it('still works when localStorage is unavailable', async () => {
    vi.spyOn(Storage.prototype, 'getItem').mockImplementation(() => {
      throw new Error('blocked');
    });
    vi.spyOn(Storage.prototype, 'setItem').mockImplementation(() => {
      throw new Error('blocked');
    });
    render(<PageFeedback page="fix" />);
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'This helped' }));
    });
    expect(screen.getByRole('button', { name: 'This helped' }).getAttribute('aria-pressed')).toBe('true');
  });

  it('opens a dialog, focuses the first choice, and closes on Escape back to the link', () => {
    render(<PageFeedback page="fix" />);
    openCard();
    const dialog = screen.getByRole('dialog');
    expect(dialog.getAttribute('aria-labelledby')).toBe('page-feedback-title');
    expect(document.activeElement).toBe(screen.getByLabelText('Accuracy'));
    fireEvent.keyDown(dialog, { key: 'Escape' });
    expect(screen.queryByRole('dialog')).toBeNull();
    expect(document.activeElement).toBe(screen.getByRole('button', { name: 'Report a problem' }));
  });

  it('needs a choice and a note before Send, and counts what is left', () => {
    render(<PageFeedback page="fix" />);
    openCard();
    const sendButton = screen.getByRole('button', { name: 'Send' }) as HTMLButtonElement;
    expect(sendButton.disabled).toBe(true);
    fireEvent.change(screen.getByLabelText('What did you see?'), { target: { value: 'Wrong date.' } });
    expect(sendButton.disabled).toBe(true);
    expect(screen.getByText('589 characters left')).toBeTruthy();
    fireEvent.click(screen.getByLabelText('Craft'));
    expect(sendButton.disabled).toBe(false);
    fireEvent.change(screen.getByLabelText('What did you see?'), { target: { value: '   ' } });
    expect(sendButton.disabled).toBe(true);
    expect((screen.getByLabelText('What did you see?') as HTMLTextAreaElement).maxLength).toBe(600);
  });

  it('posts the report, thanks the sender through a status line, and returns focus', async () => {
    render(<PageFeedback page="table:alx-syr" />);
    openCard();
    fireEvent.click(screen.getByLabelText('Accuracy'));
    fireEvent.change(screen.getByLabelText('What did you see?'), { target: { value: '  The date is off.  ' } });
    fireEvent.change(screen.getByLabelText('Email (only if you want a reply)'), { target: { value: ' a@b.org ' } });
    await send();
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toEqual({
      kind: 'report', page: 'table:alx-syr', reason: 'accuracy', text: 'The date is off.', email: 'a@b.org',
    });
    expect(screen.getByRole('status').textContent).toBe('Thank you. A person will read it.');
    expect(screen.queryByRole('dialog')).toBeNull();
    expect(document.activeElement).toBe(screen.getByRole('button', { name: 'Report a problem' }));
  });

  it('sends a null email when none is given', async () => {
    render(<PageFeedback page="fix" />);
    openCard();
    fireEvent.click(screen.getByLabelText('Craft'));
    fireEvent.change(screen.getByLabelText('What did you see?'), { target: { value: 'Clumsy.' } });
    await send();
    expect(JSON.parse(fetchMock.mock.calls[0][1].body).email).toBeNull();
  });

  it('shows the alert and keeps the note when sending fails', async () => {
    fetchMock.mockResolvedValue({ ok: false, status: 500, statusText: 'x', json: async () => ({}) });
    render(<PageFeedback page="fix" />);
    openCard();
    fireEvent.click(screen.getByLabelText('Accuracy'));
    const box = screen.getByLabelText('What did you see?') as HTMLTextAreaElement;
    fireEvent.change(box, { target: { value: 'Wrong.' } });
    await send();
    expect(screen.getByRole('alert').textContent).toBe("That didn't go through. Try again in a moment.");
    expect(box.value).toBe('Wrong.');
    expect(screen.getByText(/A person reads these, usually within a week\./)).toBeTruthy();
  });
});
