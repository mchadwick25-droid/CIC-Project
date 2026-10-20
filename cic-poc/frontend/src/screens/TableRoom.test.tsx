/**
 * The seat-identity guard's own
 * exhausted case writes a voice_turn with deliberately empty text -
 * pinned here so a future change can't silently reintroduce a blank
 * "turn--voice" bubble (portrait, name, nothing underneath) where the
 * spec says the voice's text should not be shown at all.
 */
import { act, cleanup, fireEvent, render } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { TableRoom } from './TableRoom';
import type { WorldEntry } from '../data/worlds';
import type { ConversationTurn } from '../hooks/useConversation';

function world(overrides: Partial<WorldEntry> = {}): WorldEntry {
  return {
    worldKey: 'alx',
    censusId: null,
    displayName: 'Alexandrian Christianity',
    cardName: 'Alexandrian Christianity',
    representativeName: 'Theon',
    place: 'Alexandria',
    eraStart: 150,
    eraEnd: 400,
    thinnessStatement: 'Thin on some things.',
    doorwayDescription: null,
    livingTraditionFlag: false,
    starters: [],
    portraitImage: '/x.png',
    accentColor: '#000',
    ...overrides,
  };
}

const baseProps = {
  seatedWorlds: [world()],
  sessionCode: 'ABC123',
  closed: false,
  roundOpen: true,
  roundCap: 6,
  isLoading: false,
  error: null,
  errorRecoverable: false,
  onSend: () => {},
  onResumeRound: () => {},
  onEnd: () => {},
  onRestart: () => {},
};

describe('TableRoom', () => {
  it('does not render a voice turn whose text is empty (guard-exhausted case)', () => {
    const turns: ConversationTurn[] = [
      { speaker: 'participant', text: 'Who is Jesus?' },
      { speaker: 'alx', text: '' },
      { speaker: 'facilitator', text: "This is the Facilitator, stepping in for a moment - Theon's last answer didn't hold together the way it should have." },
    ];
    const { container, getByText } = render(<TableRoom {...baseProps} turns={turns} />);
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(0);
    expect(getByText(/stepping in for a moment/)).toBeInTheDocument();
  });

  it('still renders a voice turn with real text', () => {
    const turns: ConversationTurn[] = [{ speaker: 'alx', text: 'We watched them, not counted weeks.' }];
    const { container } = render(<TableRoom {...baseProps} turns={turns} />);
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(1);
  });

  it('renders a modern-term mark for a bridge turn that carries one (OG-13)', () => {
    const turns: ConversationTurn[] = [
      {
        speaker: 'facilitator',
        text: "Let me put that in plain terms.",
        kind: 'bridge',
        modernTerms: [
          {
            record_id: '_fleet.modern.trinity',
            record_type: 'modern_term',
            label: 'Trinity',
            sources: [],
            modern_sense: 'One God, three persons.',
            distinguishing_claim: 'The word itself is modern; the claim is not.',
          },
        ],
      },
    ];
    const { container } = render(<TableRoom {...baseProps} turns={turns} />);
    expect(container.querySelectorAll('.modern-term-mark')).toHaveLength(1);
  });

  it('shows the reason under a pause at a limit and keeps the table open', () => {
    const turns: ConversationTurn[] = [
      { speaker: 'facilitator', kind: 'limit', text: 'This sitting has reached its limit for now.', note: 'You do not have enough tokens left for a Table round. Add more to carry on.' },
    ];
    const { container } = render(<TableRoom {...baseProps} turns={turns} />);
    expect(container.querySelector('.turn__note')?.textContent).toBe('You do not have enough tokens left for a Table round. Add more to carry on.');
  });
});

describe('TableRoom streaming', () => {
  it('shows the speaking seat\'s sentences under its own name while it speaks, and drops the waiting note', () => {
    const turns: ConversationTurn[] = [{ speaker: 'participant', text: 'Who was Jesus?' }];
    const streamed = [{ index: 0, speaker: 'alx', lead: '', text: 'We told what we had been told.', text_start: 0, text_end: 30, elements: [], cards: [] }];
    const { container, queryByText } = render(<TableRoom {...baseProps} turns={turns} isLoading streamed={streamed} />);
    const voice = container.querySelector('.turn--voice');
    expect(voice?.textContent).toContain('Theon');
    expect(voice?.textContent).toContain('We told what we had been told.');
    expect(queryByText(/The table is speaking/)).toBeNull();
  });
});

describe('TableRoom feedback controls', () => {
  afterEach(() => {
    cleanup();
    vi.unstubAllGlobals();
  });

  it('puts the feedback row under a stored voice turn and not under the streaming reply', () => {
    const turns: ConversationTurn[] = [
      { speaker: 'participant', text: 'Who was Jesus?' },
      { speaker: 'alx', text: 'We watched them, not counted weeks.' },
    ];
    const streamed = [{ index: 0, speaker: 'alx', lead: '', text: 'Still writing.', text_start: 0, text_end: 14, elements: [], cards: [] }];
    const { container } = render(<TableRoom {...baseProps} sessionId="s1" turns={turns} streamed={streamed} isLoading />);
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(2);
    expect(container.querySelectorAll('.turn-feedback')).toHaveLength(1);
  });

  it('puts the page like and report row at the foot once the sitting has started, with the sorted seats as its page', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    const turns: ConversationTurn[] = [{ speaker: 'participant', text: 'Who was Jesus?' }];
    const { container } = render(<TableRoom {...baseProps} turns={turns} />);
    await act(async () => {
      fireEvent.click(container.querySelector('.page-feedback .turn-feedback__like') as HTMLElement);
    });
    const body = JSON.parse(fetchMock.mock.calls[0][1].body);
    expect(body.kind).toBe('like');
    expect(body.page).toMatch(/^table:[A-Za-z0-9._-]+$/);
    expect(render(<TableRoom {...baseProps} turns={[]} />).container.querySelector('.page-feedback')).toBeNull();
  });

  it('posts the sorted table key as the page of an experience comment', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    const seatedWorlds = [world({ worldKey: 'syr' }), world({ worldKey: 'alx' })];
    const { container, getByLabelText } = render(<TableRoom {...baseProps} seatedWorlds={seatedWorlds} turns={[]} />);
    fireEvent.click(container.querySelector('.conversation__bar-right button') as HTMLElement);
    fireEvent.change(getByLabelText('What was this like for you? What should we do better?'), { target: { value: 'Good.' } });
    await act(async () => {
      fireEvent.click(container.querySelector('#experience-feedback-send') as HTMLElement);
    });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body).page).toBe('table:alx+syr');
  });
});
