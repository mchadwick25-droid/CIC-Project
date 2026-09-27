/**
 * The seat-identity guard's own
 * exhausted case writes a voice_turn with deliberately empty text -
 * pinned here so a future change can't silently reintroduce a blank
 * "turn--voice" bubble (portrait, name, nothing underneath) where the
 * spec says the voice's text should not be shown at all.
 */
import { fireEvent, render } from '@testing-library/react';
import { afterEach, describe, expect, it, vi } from 'vitest';
import { TableRoom } from './TableRoom';
import type { WorldEntry } from '../data/worlds';
import type { ConversationTurn } from '../hooks/useConversation';

vi.mock('../lib/flags', async (importOriginal) => ({
  ...(await importOriginal<typeof import('../lib/flags')>()),
  readAloudEnabled: true,
}));

class FakeUtterance {
  onend: (() => void) | null = null;
  onerror: (() => void) | null = null;
  voice: unknown = null;
  constructor(public text: string) {}
}

function stubVoices(voices: Array<{ name: string; lang: string }>) {
  vi.stubGlobal('speechSynthesis', {
    speak: vi.fn(),
    cancel: vi.fn(),
    getVoices: vi.fn(() => voices),
    addEventListener: vi.fn(),
    removeEventListener: vi.fn(),
  });
  vi.stubGlobal('SpeechSynthesisUtterance', FakeUtterance);
}

function world(overrides: Partial<WorldEntry> = {}): WorldEntry {
  return {
    worldKey: 'alx',
    censusId: null,
    displayName: 'Alexandrian Christianity',
    cardName: 'Alexandrian Christianity',
    representativeName: 'Theon',
    roleLabel: 'Teacher',
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
  afterEach(() => {
    vi.unstubAllGlobals();
  });

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

  it("gives two seated Representatives different read-aloud voices, not the same one", () => {
    stubVoices([
      { name: 'Alpha', lang: 'en-US' },
      { name: 'Beta', lang: 'en-US' },
    ]);
    const seatedWorlds = [world({ worldKey: 'alx' }), world({ worldKey: 'desert', representativeName: 'Papnoute' })];
    const turns: ConversationTurn[] = [{ speaker: 'alx', text: 'We watched them, not counted weeks.' }];
    const { getByRole } = render(<TableRoom {...baseProps} seatedWorlds={seatedWorlds} turns={turns} />);

    fireEvent.click(getByRole('button', { name: 'Read aloud' }));

    const speechSynthesis = window.speechSynthesis as unknown as { speak: ReturnType<typeof vi.fn> };
    const spokenVoice = (speechSynthesis.speak.mock.calls[0][0] as FakeUtterance).voice as { name: string };
    expect(spokenVoice.name).toBe('Alpha'); // 'alx' sorts before 'desert'
  });

  it('leaves voice unset for the Facilitator - there is no seat to assign one from', () => {
    stubVoices([
      { name: 'Alpha', lang: 'en-US' },
      { name: 'Beta', lang: 'en-US' },
    ]);
    const seatedWorlds = [world({ worldKey: 'alx' }), world({ worldKey: 'desert', representativeName: 'Papnoute' })];
    const turns: ConversationTurn[] = [{ speaker: 'facilitator', text: 'Welcome to the table.' }];
    const { getByRole } = render(<TableRoom {...baseProps} seatedWorlds={seatedWorlds} turns={turns} />);

    fireEvent.click(getByRole('button', { name: 'Read aloud' }));

    const speechSynthesis = window.speechSynthesis as unknown as { speak: ReturnType<typeof vi.fn> };
    expect((speechSynthesis.speak.mock.calls[0][0] as FakeUtterance).voice).toBeNull();
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
});
