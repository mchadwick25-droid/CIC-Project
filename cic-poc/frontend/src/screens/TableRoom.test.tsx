/**
 * The seat-identity guard's own
 * exhausted case writes a voice_turn with deliberately empty text -
 * pinned here so a future change can't silently reintroduce a blank
 * "turn--voice" bubble (portrait, name, nothing underneath) where the
 * spec says the voice's text should not be shown at all.
 */
import { act, cleanup, fireEvent, render, screen, within } from '@testing-library/react';
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

const asked: ConversationTurn[] = [{ speaker: 'participant', text: 'Who was Jesus?' }];
// Steps of a tenth of a second, each in its own act, so the screen redraws between ticks as a browser does.
const advance = (ms: number) => {
  for (let t = 0; t < ms; t += 100) {
    act(() => {
      vi.advanceTimersByTime(100);
    });
  }
};
const stream = (speaker: string, text: string) => [{ index: 0, speaker, lead: '', text, text_start: 0, text_end: text.length, elements: [], cards: [] }];
const trio = [
  world({ worldKey: 'alx', representativeName: 'Theon' }),
  world({ worldKey: 'pahc', representativeName: 'Chloe', cardName: 'Early Church' }),
  world({ worldKey: 'desert', representativeName: 'Papnoute', cardName: 'Desert', eraStart: 330 }),
];

afterEach(() => {
  cleanup();
  vi.useRealTimers();
  vi.unstubAllGlobals();
});

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
    const turns: ConversationTurn[] = [...asked, { speaker: 'alx', text: 'We watched them, not counted weeks.' }];
    const { container } = render(<TableRoom {...baseProps} turns={turns} />);
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(1);
  });

  it('renders a modern-term mark for a bridge turn that carries one (OG-13)', () => {
    const turns: ConversationTurn[] = [
      ...asked,
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
      ...asked,
      { speaker: 'facilitator', kind: 'limit', text: 'This sitting has reached its limit for now.', note: 'You do not have enough tokens left for a Table round. Add more to carry on.' },
    ];
    const { container } = render(<TableRoom {...baseProps} turns={turns} />);
    expect(container.querySelector('.turn__note')?.textContent).toBe('You do not have enough tokens left for a Table round. Add more to carry on.');
  });

  it('shows three small cards above one conversation area, with the box under it', () => {
    const { container } = render(<TableRoom {...baseProps} seatedWorlds={trio} turns={[]} />);
    expect(container.querySelector('.conversation__title')?.textContent).toBe('The Table');
    expect(Array.from(container.querySelectorAll('.conv-card__name')).map((n) => n.textContent)).toEqual(['Theon', 'Chloe', 'Papnoute']);
    expect(container.querySelectorAll('.conversation__transcript')).toHaveLength(1);
    expect(container.querySelector('textarea')?.getAttribute('placeholder')).toBe('The table is still speaking…');
  });

  it('shows the engine\'s welcome line until the first question, with no seated-voices disclosure on the page', () => {
    const door: ConversationTurn = { speaker: 'facilitator', text: 'Welcome to the Table.', kind: 'door' };
    const { container } = render(<TableRoom {...baseProps} seatedWorlds={trio} turns={[door]} />);
    expect(container.querySelector('.turn--welcome')?.textContent).toBe('Welcome to the Table.');
    expect(container.querySelector('.arrival__disclosure')).toBeNull();
    expect(container.querySelector('.arrival__thinness')).toBeNull();
  });

  it('says in one small line under the box that the voices are AI, outside the conversation', () => {
    const { container } = render(<TableRoom {...baseProps} seatedWorlds={trio} turns={[]} />);
    const line = container.querySelector('.conversation__ai-line') as HTMLElement;
    expect(line.textContent).toBe('These are AI-generated voices.');
    expect(container.querySelector('.conversation__transcript')?.contains(line)).toBe(false);
    expect(container.querySelector('textarea')?.compareDocumentPosition(line)).toBe(Node.DOCUMENT_POSITION_FOLLOWING);
  });

  it('opens About the table with the seated voices', () => {
    const { container } = render(<TableRoom {...baseProps} seatedWorlds={trio} turns={asked} />);
    fireEvent.click(screen.getByRole('button', { name: 'More' }));
    fireEvent.click(screen.getByRole('menuitem', { name: 'About the table' }));
    const panel = container.querySelector('.conversation__panel') as HTMLElement;
    expect(within(panel).getByText('Papnoute')).toBeInTheDocument();
  });
});

describe('TableRoom streaming', () => {
  it('rolls the speaking voice out under its own name, with its card lifted and no waiting note once words show', () => {
    vi.useFakeTimers();
    const { container, queryByText } = render(<TableRoom {...baseProps} seatedWorlds={trio} turns={asked} isLoading streamed={stream('pahc', 'We told what we had been told by those who saw.')} />);
    expect(queryByText('The table is considering')).not.toBeNull();
    expect(container.querySelector('.conv-card--speaking')).toBeNull();
    advance(500);
    const voice = container.querySelector('.turn--voice');
    expect(voice?.textContent).toContain('Chloe');
    advance(800);
    expect(queryByText('The table is considering')).toBeNull();
    const lit = container.querySelectorAll('.conv-card--speaking');
    expect(lit).toHaveLength(1);
    expect(lit[0].querySelector('.conv-card__name')?.textContent).toBe('Chloe');
  });

  it('hands the lift from one voice to the next, and lets every card rest after the last reply', () => {
    vi.useFakeTimers();
    const first = 'Chloe says this plainly.';
    const second = 'Theon answers in turn.';
    const turns: ConversationTurn[] = [...asked, { speaker: 'pahc', text: first }, { speaker: 'alx', text: second }];
    const { container, rerender } = render(<TableRoom {...baseProps} seatedWorlds={trio} turns={asked} isLoading />);
    rerender(<TableRoom {...baseProps} seatedWorlds={trio} turns={turns} />);
    advance(300);
    expect(container.querySelector('.conv-card--speaking .conv-card__name')?.textContent).toBe('Chloe');
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(1);
    advance(500);
    expect(container.querySelector('.conv-card--speaking .conv-card__name')?.textContent).toBe('Theon');
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(2);
    advance(5000);
    expect(container.querySelector('.conv-card--speaking')).toBeNull();
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(2);
  });

  it('keeps the box shut and says so while a voice is still rolling out its reply', () => {
    vi.useFakeTimers();
    const turns: ConversationTurn[] = [...asked, { speaker: 'alx', text: 'One two three four five six seven eight nine ten eleven twelve.' }];
    const { container, rerender } = render(<TableRoom {...baseProps} seatedWorlds={trio} turns={asked} roundOpen={false} isLoading />);
    rerender(<TableRoom {...baseProps} seatedWorlds={trio} turns={turns} roundOpen={false} />);
    advance(200);
    const box = container.querySelector('textarea') as HTMLTextAreaElement;
    expect(box.disabled).toBe(true);
    expect(box.placeholder).toBe('The table is still speaking…');
    advance(2500);
    expect(box.disabled).toBe(false);
    expect(box.placeholder).toBe('Ask the table…');
  });

  it('keeps every card at rest while the table considers', () => {
    const { container, queryByText } = render(<TableRoom {...baseProps} seatedWorlds={trio} turns={asked} isLoading />);
    expect(queryByText('The table is considering')).not.toBeNull();
    expect(container.querySelector('.conv-card--speaking')).toBeNull();
  });
});

describe('TableRoom - the more menu and feedback', () => {
  it('puts the feedback row under a stored voice turn and not under the streaming reply', () => {
    vi.useFakeTimers();
    const turns: ConversationTurn[] = [...asked, { speaker: 'alx', text: 'We watched them, not counted weeks.' }];
    const { container } = render(<TableRoom {...baseProps} sessionId="s1" turns={turns} streamed={stream('alx', 'Still writing.')} isLoading />);
    advance(1500);
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(2);
    expect(container.querySelectorAll('.turn-feedback')).toHaveLength(1);
  });

  it('posts a problem report with the sorted seats as its page, once the sitting has started', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    render(<TableRoom {...baseProps} turns={asked} />);
    fireEvent.click(screen.getByRole('button', { name: 'More' }));
    fireEvent.click(screen.getByRole('menuitem', { name: 'Report a problem' }));
    fireEvent.click(screen.getByLabelText('Craft'));
    fireEvent.change(screen.getByLabelText('What did you see?'), { target: { value: 'A voice repeated itself.' } });
    await act(async () => {
      fireEvent.click(within(screen.getByRole('dialog')).getByRole('button', { name: 'Send' }));
    });
    const body = JSON.parse(fetchMock.mock.calls[0][1].body);
    expect(body.kind).toBe('report');
    expect(body.page).toMatch(/^table:[A-Za-z0-9._-]+$/);
  });

  it('offers no Report before the first question', () => {
    render(<TableRoom {...baseProps} turns={[]} />);
    fireEvent.click(screen.getByRole('button', { name: 'More' }));
    expect(screen.queryByRole('menuitem', { name: 'Report a problem' })).toBeNull();
  });

  it('posts the sorted table key as the page of an experience comment', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    const seatedWorlds = [world({ worldKey: 'syr' }), world({ worldKey: 'alx' })];
    const { container, getByLabelText } = render(<TableRoom {...baseProps} seatedWorlds={seatedWorlds} turns={[]} />);
    fireEvent.click(screen.getByRole('button', { name: 'More' }));
    fireEvent.click(screen.getByRole('menuitem', { name: 'Tell us what you think' }));
    fireEvent.change(getByLabelText('What was this like for you? What should we do better?'), { target: { value: 'Good.' } });
    await act(async () => {
      fireEvent.click(container.querySelector('#experience-feedback-send') as HTMLElement);
    });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body).page).toBe('table:alx+syr');
  });

  it('keeps Leave for now working while a round is open', () => {
    const onEnd = vi.fn();
    render(<TableRoom {...baseProps} turns={asked} isLoading roundOpen onEnd={onEnd} />);
    fireEvent.click(screen.getByRole('button', { name: 'More' }));
    fireEvent.click(screen.getByRole('menuitem', { name: 'Leave for now' }));
    expect(onEnd).toHaveBeenCalledTimes(1);
  });
});
