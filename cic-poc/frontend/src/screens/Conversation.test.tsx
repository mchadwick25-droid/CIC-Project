/**
 * A bridge facilitator turn's own modern-term card (OG-13,
 * Build/worlds/pahc/Open_Gaps_Tracking.md) - pinned here the same way
 * TableRoom.test.tsx pins its own table-route rendering, so the interview
 * route's own facilitator-turn branch is covered too.
 */
import { act, cleanup, fireEvent, render, screen, within } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
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

const openMenu = () => fireEvent.click(screen.getByRole('button', { name: 'More' }));
const choose = (name: string) => {
  openMenu();
  fireEvent.click(screen.getByRole('menuitem', { name }));
};

const asked: ConversationTurn[] = [{ speaker: 'participant', text: 'Who was Jesus?' }];
const sentence = (text: string) => [{ index: 0, speaker: 'fix', lead: '', text, text_start: 0, text_end: text.length, elements: [], cards: [] }];

afterEach(() => {
  cleanup();
  vi.useRealTimers();
  vi.unstubAllGlobals();
});

describe('Conversation - the reply', () => {
  beforeEach(() => vi.useFakeTimers());

  it('rolls the reply out word by word, and keeps the waiting note until the first words show', () => {
    const { container, queryByText } = render(<Conversation {...baseProps} turns={asked} isLoading streamed={sentence('We told what we had been told by those who saw.')} />);
    expect(queryByText(/is considering/)).not.toBeNull();
    expect(container.querySelector('.turn--voice')).toBeNull();
    act(() => {
      vi.advanceTimersByTime(400);
    });
    const shown = container.querySelector('.turn--voice .turn__body')?.textContent ?? '';
    expect(shown.length).toBeGreaterThan(0);
    expect('We told what we had been told by those who saw.'.startsWith(shown)).toBe(true);
    expect(shown).not.toBe('We told what we had been told by those who saw.');
    act(() => {
      vi.advanceTimersByTime(3000);
    });
    expect(container.querySelector('.turn--voice .turn__body')?.textContent).toBe('We told what we had been told by those who saw.');
  });

  it('hands the streamed reply on to the finished turn without starting it over', () => {
    const text = 'We told what we had been told by those who saw.';
    const { container, rerender } = render(<Conversation {...baseProps} turns={asked} isLoading streamed={sentence(text)} />);
    act(() => {
      vi.advanceTimersByTime(600);
    });
    const before = container.querySelector('.turn--voice .turn__body')?.textContent ?? '';
    expect(before.length).toBeGreaterThan(0);
    rerender(<Conversation {...baseProps} sessionId="s1" turns={[...asked, { speaker: 'fix', text }]} streamed={[]} />);
    expect(container.querySelector('.turn--voice')?.closest('.enter')).toHaveClass('enter--open');
    const after = container.querySelector('.turn--voice .turn__body')?.textContent ?? '';
    expect(after.length).toBeGreaterThanOrEqual(before.length);
    expect(after.length).toBeLessThan(text.length);
    act(() => {
      vi.advanceTimersByTime(5000);
    });
    expect(container.querySelector('.turn--voice')?.textContent).toContain(text);
  });

  it('keeps the box shut while a reply is still rolling out, then opens it', () => {
    const text = 'One two three four five six seven eight nine ten eleven twelve.';
    const { container, rerender } = render(<Conversation {...baseProps} turns={asked} isLoading />);
    rerender(<Conversation {...baseProps} turns={[...asked, { speaker: 'fix', text }]} />);
    act(() => {
      vi.advanceTimersByTime(120);
    });
    expect((container.querySelector('textarea') as HTMLTextAreaElement).disabled).toBe(true);
    for (let t = 0; t < 2500; t += 100) {
      act(() => {
        vi.advanceTimersByTime(100);
      });
    }
    expect((container.querySelector('textarea') as HTMLTextAreaElement).disabled).toBe(false);
  });

  it('shows replies already in the record whole, with no rolling out', () => {
    const turns: ConversationTurn[] = [...asked, { speaker: 'fix', text: 'An answer that was already here.' }];
    const { container } = render(<Conversation {...baseProps} turns={turns} />);
    expect(container.querySelector('.turn--voice')?.textContent).toContain('An answer that was already here.');
  });

  it('rolls out a reply that arrives whole after the screen opened', () => {
    const text = 'One two three four five six seven eight nine ten eleven twelve.';
    const { container, rerender } = render(<Conversation {...baseProps} turns={asked} isLoading />);
    rerender(<Conversation {...baseProps} turns={[...asked, { speaker: 'fix', text }]} />);
    act(() => {
      vi.advanceTimersByTime(300);
    });
    const shown = container.querySelector('.turn--voice .turn__body')?.textContent ?? '';
    expect(shown.length).toBeGreaterThan(0);
    expect(shown.length).toBeLessThan(text.length);
  });

  it('shows a reply whole at once when the reader asks for less motion', () => {
    vi.stubGlobal('matchMedia', (query: string) => ({ matches: query.includes('reduce'), media: query, addEventListener() {}, removeEventListener() {}, addListener() {}, removeListener() {}, dispatchEvent: () => false }));
    const text = 'One two three four five six seven eight nine ten eleven twelve.';
    const { container, rerender } = render(<Conversation {...baseProps} turns={asked} isLoading />);
    rerender(<Conversation {...baseProps} turns={[...asked, { speaker: 'fix', text }]} />);
    expect(container.querySelector('.turn--voice')?.textContent).toContain(text);
  });
});

describe('Conversation - the page', () => {
  it('shows one card for the voice, a slim bar, and the box under the conversation', () => {
    const { container } = render(<Conversation {...baseProps} turns={[]} />);
    expect(container.querySelector('.conversation__title')?.textContent).toBe('Church in Conversation');
    expect(container.querySelectorAll('.conv-card')).toHaveLength(1);
    expect(container.querySelector('.conv-card__name')?.textContent).toBe('Vera');
    expect(container.querySelector('.conv-card__band')?.textContent).toBe('I. Early Church');
    expect(container.querySelector('.conversation__transcript')?.nextElementSibling).not.toBeNull();
    expect(container.querySelector('textarea')?.getAttribute('placeholder')).toBe('Ask Vera…');
  });

  it('shows the engine\'s welcome line until the first question, then lets it go', () => {
    vi.useFakeTimers();
    const door: ConversationTurn = { speaker: 'facilitator', text: 'Welcome. Ask anything you like.', kind: 'door' };
    const { container, rerender } = render(<Conversation {...baseProps} turns={[door]} />);
    expect(container.querySelector('.turn--welcome')?.textContent).toBe('Welcome. Ask anything you like.');
    rerender(<Conversation {...baseProps} turns={[door, ...asked]} isLoading />);
    expect(container.querySelector('.enter:not(.enter--open) .turn--welcome')).not.toBeNull();
    act(() => {
      vi.advanceTimersByTime(900);
    });
    expect(container.querySelector('.turn--welcome')).toBeNull();
  });

  it('carries no AI note, no suggested questions and no disclosure paragraphs on the page', () => {
    const starters = [{ cell: 'C-I', text: 'Who was Jesus, to you and your people?' }];
    const { container } = render(<Conversation {...baseProps} world={world({ starters })} turns={[]} />);
    expect(container.querySelector('.ai-note')).toBeNull();
    expect(container.querySelector('.starter-chips')).toBeNull();
    expect(container.querySelector('.arrival__disclosure')).toBeNull();
    expect(container.textContent).not.toMatch(/AI voice|Questions you might ask|Look for the ✲/);
  });

  it('says in one small line under the box that the voice is AI, outside the conversation', () => {
    const { container } = render(<Conversation {...baseProps} turns={[]} />);
    const line = container.querySelector('.conversation__ai-line') as HTMLElement;
    expect(line.textContent).toBe('This is an AI-generated voice.');
    expect(container.querySelector('.conversation__transcript')?.contains(line)).toBe(false);
    expect(container.querySelector('textarea')?.compareDocumentPosition(line)).toBe(Node.DOCUMENT_POSITION_FOLLOWING);
  });

  it('keeps the AI line once the conversation is closed, and drops it when the conversation is deleted', async () => {
    const { container, rerender } = render(<Conversation {...baseProps} turns={asked} closed />);
    expect(container.querySelector('.conversation__ai-line')).not.toBeNull();
    rerender(<Conversation {...baseProps} turns={asked} onDelete={async () => {}} />);
    choose('Delete this conversation');
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Delete' }));
    });
    expect(container.querySelector('.conversation__ai-line')).toBeNull();
  });

  it('lifts the card while a sent question waits for its reply, and lets it rest otherwise', () => {
    const { container, rerender } = render(<Conversation {...baseProps} turns={asked} />);
    expect(container.querySelector('.conv-card--speaking')).toBeNull();
    rerender(<Conversation {...baseProps} turns={asked} isLoading />);
    expect(container.querySelector('.conv-card--speaking')).not.toBeNull();
  });

  it('names the arrow Send, and Sending… while a sent question waits', () => {
    const { container, rerender } = render(<Conversation {...baseProps} turns={[]} isLoading />);
    const send = () => container.querySelector('.composer-row button') as HTMLButtonElement;
    expect(send().getAttribute('aria-label')).toBe('Send');
    expect(send().disabled).toBe(true);
    expect(container.querySelector('.waiting-note')).toBeNull();
    rerender(<Conversation {...baseProps} turns={asked} isLoading />);
    expect(send().getAttribute('aria-label')).toBe('Sending…');
  });

  it('offers a new conversation once it is closed', () => {
    const { getByText } = render(<Conversation {...baseProps} turns={asked} closed />);
    expect(getByText('Meet another world')).toBeInTheDocument();
  });
});

describe('Conversation - the more menu', () => {
  it('opens About with the voice and a way back', () => {
    const { container } = render(<Conversation {...baseProps} turns={asked} />);
    choose('About Vera');
    const panel = container.querySelector('.conversation__panel') as HTMLElement;
    expect(within(panel).getByText('Vera')).toBeInTheDocument();
    expect(panel.textContent).toContain('Not saved to an account');
    fireEvent.click(within(panel).getByText('Back to the conversation'));
    expect(container.querySelector('.conversation__panel')).toBeNull();
    expect(screen.getByRole('button', { name: 'More' })).toHaveFocus();
  });

  it('keeps Leave for now working while a reply is in flight', () => {
    const onEnd = vi.fn();
    render(<Conversation {...baseProps} turns={asked} isLoading onEnd={onEnd} />);
    choose('Leave for now');
    expect(onEnd).toHaveBeenCalledTimes(1);
  });

  it('offers Report a problem and Delete only once the conversation has started', () => {
    const { rerender } = render(<Conversation {...baseProps} turns={[]} onDelete={async () => {}} />);
    openMenu();
    expect(screen.queryByRole('menuitem', { name: 'Report a problem' })).toBeNull();
    expect(screen.queryByRole('menuitem', { name: 'Delete this conversation' })).toBeNull();
    fireEvent.keyDown(screen.getAllByRole('menuitem')[0], { key: 'Escape' });
    rerender(<Conversation {...baseProps} turns={asked} onDelete={async () => {}} />);
    openMenu();
    expect(screen.getByRole('menuitem', { name: 'Report a problem' })).toBeInTheDocument();
    expect(screen.getByRole('menuitem', { name: 'Delete this conversation' })).toBeInTheDocument();
  });

  it('asks before deleting, deletes on confirm, and then says so', async () => {
    const onDelete = vi.fn().mockResolvedValue(undefined);
    const { container } = render(<Conversation {...baseProps} turns={asked} onDelete={onDelete} />);
    choose('Delete this conversation');
    expect(screen.getByText('Delete this conversation?')).toBeInTheDocument();
    expect(onDelete).not.toHaveBeenCalled();
    await act(async () => {
      fireEvent.click(screen.getByRole('button', { name: 'Delete' }));
    });
    expect(onDelete).toHaveBeenCalledTimes(1);
    expect(container.textContent).toContain('The conversation has been deleted.');
  });

  it('posts a problem report against the conversation page', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    render(<Conversation {...baseProps} turns={asked} />);
    choose('Report a problem');
    fireEvent.click(screen.getByLabelText('Accuracy'));
    fireEvent.change(screen.getByLabelText('What did you see?'), { target: { value: 'A date looks wrong.' } });
    await act(async () => {
      fireEvent.click(within(screen.getByRole('dialog')).getByRole('button', { name: 'Send' }));
    });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body)).toMatchObject({ kind: 'report', page: 'conversation:fix', reason: 'accuracy' });
    expect(screen.getByText('Thank you. A person will read it.')).toBeInTheDocument();
  });

  it('posts the world key as the page of an experience comment', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    const { container, getByLabelText } = render(<Conversation {...baseProps} turns={asked} />);
    choose('Tell us what you think');
    fireEvent.change(getByLabelText('What was this like for you? What should we do better?'), { target: { value: 'Good.' } });
    await act(async () => {
      fireEvent.click(container.querySelector('#experience-feedback-send') as HTMLElement);
    });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body).page).toBe('fix');
  });
});

describe('Conversation - facilitator turns', () => {
  it('does not render a modern-term mark for a facilitator turn with no cards', () => {
    const turns: ConversationTurn[] = [...asked, { speaker: 'facilitator', text: 'Welcome.', kind: 'door' }];
    const { container } = render(<Conversation {...baseProps} turns={turns} />);
    expect(container.querySelectorAll('.modern-term-mark')).toHaveLength(0);
  });

  it('renders a modern-term mark with its modern_sense and distinguishing_claim for a bridge turn', () => {
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
    const { container, getByText } = render(<Conversation {...baseProps} turns={turns} />);
    const marks = container.querySelectorAll('.modern-term-mark');
    expect(marks).toHaveLength(1);
    fireEvent.mouseEnter(marks[0]);
    expect(getByText('One God, three persons.')).toBeInTheDocument();
    expect(getByText('The word itself is modern; the claim is not.')).toBeInTheDocument();
  });

  it('never renders a modern-term mark for a non-bridge facilitator turn even if modernTerms is somehow set', () => {
    const turns: ConversationTurn[] = [
      ...asked,
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

  it("shows the Facilitator's pause with the reason beneath it and keeps the room open for another message", () => {
    const turns: ConversationTurn[] = [
      { speaker: 'participant', text: 'May I go on?' },
      { speaker: 'facilitator', kind: 'limit', text: 'This sitting has reached its limit for now.', note: 'Your tokens have run out. Add more to carry on.' },
    ];
    const { container, queryByText } = render(<Conversation {...baseProps} turns={turns} />);
    expect(container.querySelector('.turn__note')?.textContent).toBe('Your tokens have run out. Add more to carry on.');
    expect(container.querySelector('textarea')).not.toBeDisabled();
    expect(queryByText('Meet another tradition')).toBeNull();
  });
});

describe('Conversation - turn feedback', () => {
  const turns: ConversationTurn[] = [...asked, { speaker: 'fix', text: 'We told what we had been told.' }];

  it('puts the feedback row under a finished voice turn only, not under the streaming reply', () => {
    vi.useFakeTimers();
    const { container } = render(<Conversation {...baseProps} sessionId="s1" turns={turns} streamed={sentence('Still writing.')} isLoading />);
    act(() => {
      vi.advanceTimersByTime(1500);
    });
    expect(container.querySelectorAll('.turn--voice')).toHaveLength(2);
    expect(container.querySelectorAll('.turn-feedback')).toHaveLength(1);
  });

  it('shows no feedback row without a session code', () => {
    const { container } = render(<Conversation {...baseProps} sessionId="s1" sessionCode={null} turns={turns} />);
    expect(container.querySelectorAll('.turn-feedback')).toHaveLength(0);
  });

  it('posts the like against the index of the turn in the transcript', async () => {
    const fetchMock = vi.fn().mockResolvedValue({ ok: true, status: 201, json: async () => ({ id: 'x' }) });
    vi.stubGlobal('fetch', fetchMock);
    const { container } = render(<Conversation {...baseProps} sessionId="s1" turns={turns} />);
    await act(async () => {
      fireEvent.click(container.querySelector('.turn--voice .turn-feedback__like') as HTMLElement);
    });
    expect(JSON.parse(fetchMock.mock.calls[0][1].body).turn_index).toBe(1);
  });
});
