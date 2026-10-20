/**
 * The first screen a load shows before the world list arrives: a deep link
 * holds on the quiet arriving state, never the launch screen's world cards.
 */
import { render, screen, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import App from './App';

const worldSummary = {
  world_key: 'don',
  census_id: 'donatism',
  display_name: 'Donatism',
  card_name: 'Donatist Africa',
  representative: { name: 'Fidelis' },
  time_window: { start: 311, end: 411 },
  place: 'Carthage',
  thinness_statement: '',
  doorway_description: null,
  horizon: null,
  living_tradition_flag: false,
  starters: [],
  app: { order: 1, accent_color: '#000', portrait: '/x.png' },
};

function json(body: unknown) {
  return Promise.resolve(new Response(JSON.stringify(body), { status: 200, headers: { 'Content-Type': 'application/json' } }));
}

let releaseWorlds: () => void;

beforeEach(() => {
  sessionStorage.clear();
  const worldsGate = new Promise<void>((resolve) => {
    releaseWorlds = resolve;
  });
  vi.stubGlobal(
    'fetch',
    vi.fn((url: string) => {
      if (url.endsWith('/api/worlds')) return worldsGate.then(() => json({ worlds: [worldSummary] }));
      if (url.endsWith('/api/session')) return new Promise(() => {});
      return json({});
    }),
  );
});

afterEach(() => {
  vi.unstubAllGlobals();
  window.history.replaceState({}, '', '/');
});

describe('first screen', () => {
  it('holds on the arriving state, not the world cards, while a deep link waits for the world list', async () => {
    window.history.replaceState({}, '', '/?worlds=donatism&mode=interview');
    const { container } = render(<App />);

    expect(screen.getByRole('status')).toHaveTextContent('Opening the conversation');
    expect(container.querySelector('.launch')).toBeNull();

    releaseWorlds();
    await waitFor(() => expect(container.querySelector('.arrival')).not.toBeNull());
    expect(container.querySelector('.launch')).toBeNull();
  });

  it('puts a question carried in as #q= in the message box, unsent, and drops it from the address', async () => {
    window.history.replaceState({}, '', `/?worlds=donatism&mode=interview#q=${encodeURIComponent("What did you make of the Traditores' bishops?")}`);
    const { container } = render(<App />);
    expect(window.location.hash).toBe('');
    expect(window.location.search).toBe('?worlds=donatism&mode=interview');

    releaseWorlds();
    await waitFor(() => expect(container.querySelector('.arrival')).not.toBeNull());
    const box = container.querySelector('.composer-row textarea') as HTMLTextAreaElement;
    expect(box.value).toBe("What did you make of the Traditores' bishops?");
    expect(container.querySelector('.turn--participant')).toBeNull();
  });

  it('falls back to the launch screen when the deep link names no known world', async () => {
    window.history.replaceState({}, '', '/?worlds=nowhere&mode=interview');
    const { container } = render(<App />);
    expect(container.querySelector('.launch')).toBeNull();

    releaseWorlds();
    await waitFor(() => expect(container.querySelector('.launch')).not.toBeNull());
    expect(screen.getByRole('alert')).toHaveTextContent("We couldn't find that world here");
  });

  it('opens on the launch screen when there is no deep link and nothing to resume', () => {
    const { container } = render(<App />);
    expect(container.querySelector('.launch')).not.toBeNull();
  });
});
