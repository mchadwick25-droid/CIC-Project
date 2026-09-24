/**
 * The seat-identity guard's own
 * exhausted case writes a voice_turn with deliberately empty text -
 * pinned here so a future change can't silently reintroduce a blank
 * "turn--voice" bubble (portrait, name, nothing underneath) where the
 * spec says the voice's text should not be shown at all.
 */
import { render } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
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
});
