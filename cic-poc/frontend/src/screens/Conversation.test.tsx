/**
 * A bridge facilitator turn's own modern-term card (OG-13,
 * Build/worlds/pahc/Open_Gaps_Tracking.md) - pinned here the same way
 * TableRoom.test.tsx pins its own table-route rendering, so the interview
 * route's own facilitator-turn branch is covered too.
 */
import { act, cleanup, fireEvent, render } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { Conversation } from './Conversation';
import type { WorldEntry } from '../data/worlds';
import type { ConversationTurn } from '../hooks/useConversation';

function world(overrides: Partial<WorldEntry> = {}): WorldEntry {
  return {
    worldKey: 'fix',
    censusId: null,
    displayName: 'Fixture World',
    cardName: 'Fixture',
    representativeName: 'Vera',
    roleLabel: 'Witness',
    place: 'Nowhere',
    eraStart: 100,
    eraEnd: 200,
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
  world: world(),
  sessionCode: 'ABC123',
  closed: false,
  isLoading: false,
  error: null,
  errorRecoverable: false,
  onSend: () => {},
  onEnd: () => {},
  onRestart: () => {},
};

describe('Conversation', () => {
  it('shows the reply so far while the voice is still writing, and drops the waiting note', () => {
    const turns: ConversationTurn[] = [{ speaker: 'participant', text: 'Who was Jesus?' }];
    const { container, queryByText } = render(
      <Conversation {...baseProps} turns={turns} isLoading streamed={[{ index: 0, speaker: 'w', lead: '', text: 'We told what we had been told.', text_start: 0, text_end: 30, elements: [], cards: [] }]} />
    );
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(1);
    expect(container.querySelector('.turn--voice')?.textContent).toContain('We told what we had been told.');
    expect(queryByText(/is considering/)).toBeNull();
  });

  it('keeps the waiting note until the first sentence of the reply arrives', () => {
    const turns: ConversationTurn[] = [{ speaker: 'participant', text: 'Who was Jesus?' }];
    const { container, queryByText } = render(<Conversation {...baseProps} turns={turns} isLoading streamed={[]} />);
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(0);
    expect(queryByText(/is considering/)).not.toBeNull();
  });

  it('does not render a modern-term mark for a facilitator turn with no cards', () => {
    const turns: ConversationTurn[] = [{ speaker: 'facilitator', text: 'Welcome.', kind: 'door' }];
    const { container } = render(<Conversation {...baseProps} turns={turns} />);
    expect(container.querySelectorAll('.modern-term-mark')).toHaveLength(0);
  });

  it('renders a modern-term mark with its modern_sense and distinguishing_claim for a bridge turn', () => {
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
    const { container, getByText } = render(<Conversation {...baseProps} turns={turns} />);
    const marks = container.querySelectorAll('.modern-term-mark');
    expect(marks).toHaveLength(1);
    fireEvent.mouseEnter(marks[0]);
    expect(getByText('One God, three persons.')).toBeInTheDocument();
    expect(getByText('The word itself is modern; the claim is not.')).toBeInTheDocument();
  });

  it('never renders a modern-term mark for a non-bridge facilitator turn even if modernTerms is somehow set', () => {
    const turns: ConversationTurn[] = [
      {
        speaker: 'facilitator',
        text: 'This conversation is closed.',
        kind: 'close',
        modernTerms: [{ record_id: '_fleet.modern.trinity', record_type: 'modern_term', label: 'Trinity', sources: [] }],
      },
    ];
    const { container } = render(<Conversation {...baseProps} turns={turns} />);
    expect(container.querySelectorAll('.modern-term-mark')).toHaveLength(0);
  });

  it('states that the voice is AI before the first message, and not after', () => {
    const { container, rerender } = render(<Conversation {...baseProps} turns={[]} />);
    expect(container.querySelector('.ai-note')?.textContent).toContain('Vera is an AI voice');
    const turns: ConversationTurn[] = [{ speaker: 'participant', text: 'Hello' }];
    rerender(<Conversation {...baseProps} turns={turns} />);
    expect(container.querySelector('.ai-note')).toBeNull();
  });
});

describe('Conversation - the screen once the conversation starts', () => {
  afterEach(() => {
    cleanup();
  });

  const asked: ConversationTurn[] = [{ speaker: 'participant', text: 'Who was Jesus?' }];

  it('keeps the brand bar and the feedback button at the top before the first message', () => {
    const { container } = render(<Conversation {...baseProps} turns={[]} />);
    expect(container.querySelector('.conversation__bar-right .experience-feedback__toggle')).not.toBeNull();
    expect(container.querySelector('.conversation__who')).toBeNull();
  });

  it('shows only the portrait and the two names at the top after the first message', () => {
    const { container } = render(<Conversation {...baseProps} turns={asked} />);
    const who = container.querySelector('.conversation__who') as HTMLElement;
    expect(who.textContent).toBe('VeraFixture');
    expect(who.querySelector('img')?.getAttribute('src')).toBe('/x.png');
    expect(container.querySelector('.conversation__bar')).toBeNull();
    expect(container.querySelector('.conversation__end .experience-feedback__toggle')).not.toBeNull();
    expect(container.querySelector('.conversation__end')?.textContent).toContain('Leave for now');
  });

  it('opens and closes the arrival again from the portrait', () => {
    const { container, getByText } = render(<Conversation {...baseProps} turns={asked} />);
    const who = container.querySelector('.conversation__who') as HTMLElement;
    fireEvent.click(who);
    expect(who.getAttribute('aria-expanded')).toBe('true');
    expect(container.querySelector('#conversation-about .arrival__disclosure')).not.toBeNull();
    fireEvent.click(getByText('Back to the conversation'));
    expect(container.querySelector('#conversation-about')).toBeNull();
  });

  it('raises the newest question to the top of the transcript', () => {
    const scrollTo = vi.fn();
    const original = HTMLElement.prototype.scrollTo;
    HTMLElement.prototype.scrollTo = scrollTo as unknown as typeof original;
    try {
      const { rerender } = render(<Conversation {...baseProps} turns={[]} />);
      expect(scrollTo).not.toHaveBeenCalled();
      rerender(<Conversation {...baseProps} turns={asked} />);
      expect(scrollTo).toHaveBeenCalledTimes(1);
      expect(scrollTo.mock.calls[0][0]).toMatchObject({ top: 0 });
    } finally {
      HTMLElement.prototype.scrollTo = original;
    }
  });

  it('keeps the question at rest when the screen changes height, until the reader scrolls', () => {
    const scrollTo = vi.fn();
    const original = HTMLElement.prototype.scrollTo;
    HTMLElement.prototype.scrollTo = scrollTo as unknown as typeof original;
    let resized = () => {};
    vi.stubGlobal(
      'ResizeObserver',
      class {
        constructor(callback: () => void) {
          resized = callback;
        }
        observe() {}
        disconnect() {}
      },
    );
    try {
      const { container } = render(<Conversation {...baseProps} turns={asked} />);
      const calls = scrollTo.mock.calls.length;
      resized();
      expect(scrollTo.mock.calls.length).toBe(calls + 1);
      fireEvent.wheel(container.querySelector('.conversation__transcript') as HTMLElement);
      resized();
      expect(scrollTo.mock.calls.length).toBe(calls + 1);
    } finally {
      HTMLElement.prototype.scrollTo = original;
      vi.unstubAllGlobals();
    }
  });

  it('keeps the feedback button once the conversation is closed', () => {
    const { container } = render(<Conversation {...baseProps} turns={asked} closed />);
    expect(container.querySelector('.conversation__composer .experience-feedback__toggle')).not.toBeNull();
  });

  it('lays the suggested questions in one row', () => {
    const starters = [
      { cell: 'C-I', text: 'Who was Jesus, to you and your people?' },
      { cell: 'C-P', text: 'How did you come to believe in Jesus?' },
      { cell: 'C-E', text: 'How did it reach you?' },
    ];
    const { container } = render(<Conversation {...baseProps} world={world({ starters })} turns={[]} />);
    expect(container.querySelectorAll('.starter-chips__row .starter-chip')).toHaveLength(3);
  });
});

describe('Conversation - a pause at a limit', () => {
  it('shows the Facilitator\'s pause with the reason beneath it and keeps the room open for another message', () => {
    const turns: ConversationTurn[] = [
      { speaker: 'participant', text: 'May I go on?' },
      { speaker: 'facilitator', kind: 'limit', text: 'This sitting has reached its limit for now.', note: 'Your tokens have run out. Add more to carry on.' },
    ];
    const { container, queryByText } = render(<Conversation {...baseProps} turns={turns} />);
    expect(container.querySelector('.turn__note')?.textContent).toBe('Your tokens have run out. Add more to carry on.');
    expect(container.querySelector('textarea')).not.toBeDisabled();
    expect(queryByText('Meet another world')).toBeNull();
  });
});

describe('Conversation - feedback controls', () => {
  afterEach(() => {
    cleanup();
    vi.unstubAllGlobals();
  });

  const turns: ConversationTurn[] = [
    { speaker: 'participant', text: 'Who was Jesus?' },
    { speaker: 'fix', text: 'We told what we had been told.' },
  ];
  const streamed = [{ index: 0, speaker: 'fix', lead: '', text: 'Still writing.', text_start: 0, text_end: 14, elements: [], cards: [] }];

  it('puts the feedback row under a finished voice turn only, not under the streaming reply', () => {
    const { container, getByText } = render(<Conversation {...baseProps} sessionId="s1" turns={turns} streamed={streamed} isLoading />);
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(2);
    expect(container.querySelectorAll('.turn-feedback')).toHaveLength(1);
    expect(container.querySelector('.turn--voice .turn-feedback')).not.toBeNull();
    expect(getByText('This helped')).toBeInTheDocument();
  });

  it('shows no feedback row without a session code', () => {
    const { container } = render(<Conversation {...baseProps} sessionId="s1" sessionCode={null} turns={turns} />);
    expect(container.querySelectorAll('.turn-feedback')).toHaveLength(0);
  });

  it('posts the like against the index of the turn in the transcript', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    const { getByText } = render(<Conversation {...baseProps} sessionId="s1" turns={turns} />);
    await act(async () => {
      fireEvent.click(getByText('This helped'));
    });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body).turn_index).toBe(1);
  });

  it('opens the experience card from the bar and posts the world key as the page', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    const { container, getByLabelText } = render(<Conversation {...baseProps} turns={turns} />);
    fireEvent.click(container.querySelector('.conversation__end .experience-feedback__toggle') as HTMLElement);
    fireEvent.change(getByLabelText('What was this like for you? What should we do better?'), { target: { value: 'Good.' } });
    await act(async () => {
      fireEvent.click(container.querySelector('#experience-feedback-send') as HTMLElement);
    });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body).page).toBe('fix');
  });
});
