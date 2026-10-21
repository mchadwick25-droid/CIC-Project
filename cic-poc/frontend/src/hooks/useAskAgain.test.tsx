import { act, cleanup, fireEvent, render, screen, waitFor } from '@testing-library/react';
import { useEffect } from 'react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { ChatInput } from '../components/ChatInput';
import { Conversation } from '../screens/Conversation';
import { TableRoom } from '../screens/TableRoom';
import type { WorldEntry } from '../data/worlds';
import type { ConversationTurn } from './useConversation';
import { isAnsweredRepeat } from './useAskAgain';
import { askAgainCopy } from '../lib/deeperCopy';

afterEach(cleanup);

const ask = 'What did you believe?';
const answered: ConversationTurn[] = [
  { speaker: 'participant', text: ask },
  { speaker: 'fix', text: 'An answer.' },
];
const limited: ConversationTurn[] = [
  { speaker: 'participant', text: ask },
  { speaker: 'facilitator', text: 'Paused.', kind: 'limit' },
];
const safety: ConversationTurn[] = [
  { speaker: 'participant', text: ask },
  { speaker: 'facilitator', text: 'Are you all right?', kind: 'safety' },
];

function world(key: string): WorldEntry {
  return {
    worldKey: key, censusId: null, displayName: 'Fixture', cardName: 'Fixture', representativeName: 'Vera', place: 'Nowhere',
    eraStart: 100, eraEnd: 200, thinnessStatement: 'Thin.', doorwayDescription: null, livingTraditionFlag: false, starters: [], portraitImage: '/x.png', accentColor: '#000',
  };
}

const roomProps = {
  sessionCode: 'ABC123', closed: false, isLoading: false, error: null, errorRecoverable: false, onEnd: () => {}, onRestart: () => {},
};

function room(kind: 'interview' | 'table', turns: ConversationTurn[], onSend: (text: string) => void) {
  return kind === 'interview' ? (
    <Conversation {...roomProps} world={world('fix')} turns={turns} onSend={onSend} />
  ) : (
    <TableRoom {...roomProps} seatedWorlds={[world('fix')]} turns={turns} roundOpen={false} roundCap={6} onResumeRound={() => {}} onSend={onSend} />
  );
}

function type(text: string) {
  const box = screen.getByRole('textbox');
  fireEvent.change(box, { target: { value: text } });
  fireEvent.submit(box.closest('form') as HTMLFormElement);
  return box as HTMLTextAreaElement;
}

describe.each(['interview', 'table'] as const)('asking an answered question again (%s)', (kind) => {
  it('asks first, and sends nothing until Ask again', () => {
    const onSend = vi.fn();
    render(room(kind, answered, onSend));
    type('  what DID you   believe?  ');
    expect(screen.getByText(/You asked this earlier/)).toBeInTheDocument();
    expect(onSend).not.toHaveBeenCalled();
    fireEvent.click(screen.getByRole('button', { name: askAgainCopy.ask }));
    expect(onSend).toHaveBeenCalledWith('what DID you   believe?');
    expect(screen.queryByText(/You asked this earlier/)).toBeNull();
  });

  it('moves focus to Ask again and closes on Escape with the text kept', async () => {
    const onSend = vi.fn();
    render(room(kind, answered, onSend));
    type(ask);
    expect(screen.getByRole('button', { name: askAgainCopy.ask })).toHaveFocus();
    fireEvent.keyDown(window, { key: 'Escape' });
    expect(screen.queryByText(/You asked this earlier/)).toBeNull();
    await waitFor(() => expect(screen.getByRole('textbox')).toHaveFocus());
    expect(screen.getByRole('textbox')).toHaveValue(ask);
    expect(onSend).not.toHaveBeenCalled();
  });

  it("Don't ask sends nothing and keeps the text", () => {
    const onSend = vi.fn();
    render(room(kind, answered, onSend));
    const box = type(ask);
    fireEvent.click(screen.getByRole('button', { name: askAgainCopy.decline }));
    expect(box.value).toBe(ask);
    expect(onSend).not.toHaveBeenCalled();
  });

  it.each([
    ['a limit-refused question', limited],
    ['a question only a safety turn answered', safety],
    ['a first-time question', [] as ConversationTurn[]],
  ])('does not ask for %s', (_name, turns) => {
    const onSend = vi.fn();
    render(room(kind, turns, onSend));
    type(ask);
    expect(screen.queryByText(/You asked this earlier/)).toBeNull();
    expect(onSend).toHaveBeenCalledWith(ask);
  });
});

describe('what counts as answered', () => {
  it('ignores a Table voice turn with no text', () => {
    expect(isAnsweredRepeat([{ speaker: 'participant', text: ask }, { speaker: 'fix', text: '' }], ask)).toBe(false);
  });

  it('does not treat a retry after a failure as a repeat', () => {
    expect(isAnsweredRepeat([...answered, { speaker: 'participant', text: ask }], ask)).toBe(false);
  });

  it('counts a question answered later in the same round', () => {
    const turns: ConversationTurn[] = [{ speaker: 'participant', text: ask }, { speaker: 'facilitator', text: 'Note.' }, { speaker: 'fix', text: 'An answer.' }];
    expect(isAnsweredRepeat(turns, ask)).toBe(true);
  });
});

describe('the words', () => {
  afterEach(() => vi.unstubAllEnvs());

  it('leave out the token sentence when Go Deeper is off', () => {
    render(<ChatInput onSend={vi.fn()} placeholder="" turns={answered} />);
    type(ask);
    expect(screen.getByText(askAgainCopy.bodyFree)).toBeInTheDocument();
  });

  it('mention tokens when Go Deeper is on', async () => {
    vi.resetModules();
    vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
    const { ChatInput: Input } = await import('../components/ChatInput');
    render(<Input onSend={vi.fn()} placeholder="" turns={answered} />);
    type(ask);
    expect(screen.getByText(askAgainCopy.body)).toBeInTheDocument();
  });
});

describe('the automatic resend after a code', () => {
  const CODE = '2345 6789 ABCD EFGH JKLM';
  const json = (status: number, body: unknown) => new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json' } });

  beforeEach(() => localStorage.clear());
  afterEach(() => {
    vi.unstubAllGlobals();
    vi.unstubAllEnvs();
  });

  it('sends the refused question again without asking', async () => {
    const sent: string[] = [];
    vi.stubGlobal('fetch', vi.fn(async (url: string, init?: RequestInit) => {
      if (url.endsWith('/api/session')) return json(200, { session_id: 's', session_code: 'c' });
      if (url.endsWith('/transcript')) return json(200, { transcript: [], closed: false, mode: 'interview', world_keys: null, round_open: false });
      if (url.endsWith('/api/deeper/balance')) return json(200, { remaining: 100 });
      const headers = init?.headers as Record<string, string>;
      sent.push(JSON.parse(String(init?.body)).text);
      if (!('X-Cic-Code' in headers)) return json(200, { facilitator: { kind: 'limit', text: 'Paused.' }, voice: null, limit_note: { key: 'spent', text: 'A line.' } });
      return json(200, { facilitator: null, voice: { speaker: 'fix', text: 'An answer.', citations: [] }, limit_note: null });
    }));
    vi.resetModules();
    vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
    const deeper = await import('../lib/deeper');
    const { useConversation } = await import('./useConversation');
    const { Conversation: Screen } = await import('../screens/Conversation');
    function Harness() {
      const c = useConversation();
      const { begin } = c;
      useEffect(() => {
        void begin('fix');
      }, [begin]);
      return c.sessionId ? <Screen {...roomProps} world={world('fix')} turns={c.turns} onSend={c.send} /> : null;
    }
    render(<Harness />);
    await screen.findByRole('textbox');
    type(ask);
    await waitFor(() => expect(sent).toEqual([ask]));
    await act(async () => {
      deeper.saveCode(CODE);
    });
    await waitFor(() => expect(sent).toEqual([ask, ask]));
    expect(screen.queryByText(/You asked this earlier/)).toBeNull();
  });
});
