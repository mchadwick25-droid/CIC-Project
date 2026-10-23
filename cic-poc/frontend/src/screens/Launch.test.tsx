import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { Launch } from './Launch';

const props = {
  worlds: [],
  isLoading: false,
  error: null,
  seated: [],
  tableFocus: false,
  convening: false,
  tableError: null,
  onBeginInterview: () => {},
  onToggleSeat: () => {},
  onSeatPairing: () => {},
  onConvene: () => {},
};

describe('Launch feedback', () => {
  afterEach(() => {
    cleanup();
    vi.unstubAllGlobals();
  });

  it('offers "Tell us what you think" and posts the comment with page launch', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    const { container } = render(<Launch {...props} />);
    expect(container.querySelector('.launch__foot')).not.toBeNull();
    fireEvent.click(screen.getByRole('button', { name: 'Tell us what you think' }));
    fireEvent.change(screen.getByLabelText('What was this like for you? What should we do better?'), { target: { value: 'Clear.' } });
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Send' }));
    });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body).page).toBe('launch');
  });
});
