import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { TurnFeedback } from './TurnFeedback';
import type { TransparencyPlan } from '../types/conversation';

const TEXT = 'The bishop wrote in 180. He named four gospels.';
const PLAN: TransparencyPlan = {
  world_key: 'fix',
  sentences: [
    { index: 0, text_start: 0, text_end: 24 },
    { index: 1, text_start: 25, text_end: 47 },
  ],
  references: [],
  unverified_claims: { count: 0, sentence_indexes: [] },
};

function renderRow(transparency?: TransparencyPlan) {
  return render(
    <TurnFeedback sessionId="s1" sessionCode="CODE1" turnIndex={3} text={TEXT} transparency={transparency} representativeName="Vera" />
  );
}

function ok() {
  return { ok: true, status: 201, json: async () => ({ id: 'x' }) };
}

describe('TurnFeedback', () => {
  let fetchMock: ReturnType<typeof vi.fn>;
  beforeEach(() => {
    fetchMock = vi.fn().mockResolvedValue(ok());
    vi.stubGlobal('fetch', fetchMock);
  });
  afterEach(() => {
    cleanup();
    vi.unstubAllGlobals();
  });

  it('posts a like with the session header and fills the heart', async () => {
    renderRow(PLAN);
    const like = screen.getByRole('button', { name: 'This helped' });
    expect(like.getAttribute('aria-pressed')).toBe('false');
    await act(async () => {
      fireEvent.click(like);
    });
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('/api/session/s1/feedback');
    expect(init.method).toBe('POST');
    expect(init.headers.Authorization).toBe('Session CODE1');
    expect(JSON.parse(init.body)).toEqual({ kind: 'like', turn_index: 3, sentence_index: null, reason: null, text: null, email: null });
    expect(like.getAttribute('aria-pressed')).toBe('true');
    expect((like as HTMLButtonElement).disabled).toBe(true);
  });

  it('changes nothing and shows nothing when a like fails', async () => {
    fetchMock.mockResolvedValue({ ok: false, status: 500, statusText: 'x', json: async () => ({}) });
    renderRow(PLAN);
    const like = screen.getByRole('button', { name: 'This helped' });
    await act(async () => {
      fireEvent.click(like);
    });
    expect(like.getAttribute('aria-pressed')).toBe('false');
    expect((like as HTMLButtonElement).disabled).toBe(false);
    expect(screen.queryByRole('alert')).toBeNull();
  });

  it('lists the plan sentences in the flag card', () => {
    renderRow(PLAN);
    const link = screen.getByRole('button', { name: 'Answer was not clear or accurate' });
    expect(link.getAttribute('aria-expanded')).toBe('false');
    fireEvent.click(link);
    expect(link.getAttribute('aria-expanded')).toBe('true');
    expect(screen.getByText('Tell us what was not clear or accurate')).toBeTruthy();
    expect(screen.getByLabelText('The bishop wrote in 180.')).toBeTruthy();
    expect(screen.getByLabelText('He named four gospels.')).toBeTruthy();
    expect(screen.getByText(/If you disagree with what Vera believes/)).toBeTruthy();
  });

  it('offers the whole reply when the turn has no sentences', async () => {
    renderRow(undefined);
    fireEvent.click(screen.getByRole('button', { name: 'Answer was not clear or accurate' }));
    fireEvent.click(screen.getByLabelText('The whole reply'));
    fireEvent.click(screen.getByLabelText('This is not clear'));
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toEqual({
      kind: 'flag', turn_index: 3, sentence_index: null, reason: 'unclear', text: null, email: null,
    });
  });

  it('blocks Send until a sentence and a reason are chosen, and hides the line until a reason', () => {
    renderRow(PLAN);
    fireEvent.click(screen.getByRole('button', { name: 'Answer was not clear or accurate' }));
    const send = screen.getByRole('button', { name: 'Send' }) as HTMLButtonElement;
    expect(send.disabled).toBe(true);
    expect(screen.queryByLabelText('Add a line if you like (optional)')).toBeNull();
    fireEvent.click(screen.getByLabelText('He named four gospels.'));
    expect(send.disabled).toBe(true);
    fireEvent.click(screen.getByLabelText('I think this fact is wrong'));
    expect(send.disabled).toBe(false);
    expect(screen.getByLabelText('Add a line if you like (optional)')).toBeTruthy();
    expect(screen.getByText(/A person reads these, usually within a week\./)).toBeTruthy();
  });

  it('posts the exact flag body and shows the thank-you line', async () => {
    renderRow(PLAN);
    const link = screen.getByRole('button', { name: 'Answer was not clear or accurate' });
    fireEvent.click(link);
    fireEvent.click(screen.getByLabelText('He named four gospels.'));
    fireEvent.click(screen.getByLabelText('The source shown does not say this'));
    fireEvent.change(screen.getByLabelText('Add a line if you like (optional)'), { target: { value: 'Check Irenaeus.' } });
    fireEvent.change(screen.getByLabelText('Email, if you want to hear what we find (optional)'), { target: { value: 'a@b.org' } });
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    });
    const [url, init] = fetchMock.mock.calls[0];
    expect(url).toBe('/api/session/s1/feedback');
    expect(init.headers.Authorization).toBe('Session CODE1');
    expect(JSON.parse(init.body)).toEqual({
      kind: 'flag', turn_index: 3, sentence_index: 1, reason: 'source_mismatch', text: 'Check Irenaeus.', email: 'a@b.org',
    });
    expect(screen.getByRole('status').textContent).toBe(
      'Thank you. A person will check it against the sources.'
    );
    expect(screen.queryByText('Tell us what was not clear or accurate')).toBeNull();
    expect((link as HTMLButtonElement).disabled).toBe(true);
  });

  it('keeps the card filled in and shows an alert when sending fails', async () => {
    fetchMock.mockResolvedValue({ ok: false, status: 500, statusText: 'x', json: async () => ({}) });
    renderRow(PLAN);
    fireEvent.click(screen.getByRole('button', { name: 'Answer was not clear or accurate' }));
    fireEvent.click(screen.getByLabelText('The bishop wrote in 180.'));
    fireEvent.click(screen.getByLabelText('This is not clear'));
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    });
    expect(screen.getByRole('alert').textContent).toBe("That didn't go through. Try again in a moment.");
    expect((screen.getByLabelText('This is not clear') as HTMLInputElement).checked).toBe(true);
    expect((screen.getByRole('button', { name: 'Send' }) as HTMLButtonElement).disabled).toBe(false);
  });

  it('closes the card on Cancel', () => {
    renderRow(PLAN);
    fireEvent.click(screen.getByRole('button', { name: 'Answer was not clear or accurate' }));
    fireEvent.click(screen.getByRole('button', { name: 'Cancel' }));
    expect(screen.queryByText('Tell us what was not clear or accurate')).toBeNull();
  });
});
