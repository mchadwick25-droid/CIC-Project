/**
 * Inside the site's frame, the app tells talk.html when a conversation has
 * started, so the page can hide its own bars.
 */
import { render, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const worldSummary = {
  world_key: 'don',
  census_id: 'donatism',
  display_name: 'Donatism',
  card_name: 'Donatist Africa',
  representative: { name: 'Fidelis', role_label: 'Reader' },
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

function transcript(entries: unknown[]) {
  return { session_id: 's1', world_key: 'don', turn_count: entries.length, closed: false, transcript: entries, mode: 'interview', world_keys: null, round_open: false, round_cap: null };
}

const door = { speaker: 'facilitator', kind: 'door', text: 'Welcome.' };

async function renderFramed(entries: unknown[]) {
  sessionStorage.setItem('cic_session', JSON.stringify({ sessionId: 's1', sessionCode: 'CODE', mode: 'interview', worldKey: 'don' }));
  vi.stubGlobal(
    'fetch',
    vi.fn((url: string) => {
      if (url.endsWith('/api/worlds')) return json({ worlds: [worldSummary] });
      if (url.includes('/transcript')) return json(transcript(entries));
      return json({});
    }),
  );
  vi.spyOn(window, 'top', 'get').mockReturnValue({} as Window);
  const post = vi.spyOn(window.parent, 'postMessage').mockImplementation(() => {});
  vi.resetModules();
  const { default: App } = await import('./App');
  const view = render(<App />);
  return { ...view, post };
}

function startedMessages(post: { mock: { calls: unknown[][] } }) {
  return post.mock.calls.map((call) => call[0]).filter((m) => (m as { type?: string }).type === 'cic:started');
}

beforeEach(() => {
  sessionStorage.clear();
});

afterEach(() => {
  vi.restoreAllMocks();
  vi.unstubAllGlobals();
  sessionStorage.clear();
  document.documentElement.classList.remove('is-framed');
});

describe('framed in talk.html', () => {
  it('says the conversation has started once there is a question', async () => {
    const { container, post } = await renderFramed([door, { speaker: 'participant', text: 'Who are you?' }]);
    await waitFor(() => expect(container.querySelector('.conversation__who')).not.toBeNull());
    expect(startedMessages(post).slice(-1)[0]).toEqual({ type: 'cic:started', started: true });
  });

  it('marks the page as framed, so the first-screen bar drops the site\'s duplicates', async () => {
    const { container } = await renderFramed([door]);
    await waitFor(() => expect(container.querySelector('.arrival')).not.toBeNull());
    expect(document.documentElement.classList.contains('is-framed')).toBe(true);
  });

  it('says it has not started while only the welcome is there', async () => {
    const { container, post } = await renderFramed([door]);
    await waitFor(() => expect(container.querySelector('.arrival')).not.toBeNull());
    expect(startedMessages(post).slice(-1)[0]).toEqual({ type: 'cic:started', started: false });
  });
});
