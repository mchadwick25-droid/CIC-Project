/**
 * A bridge facilitator turn's own modern-term card (OG-13,
 * Build/worlds/pahc/Open_Gaps_Tracking.md) - pinned here the same way
 * TableRoom.test.tsx pins its own table-route rendering, so the interview
 * route's own facilitator-turn branch is covered too.
 */
import { fireEvent, render } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
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
