/**
 * The ✲ mark explainer
 * sentence is new prose in an otherwise verbatim-carried disclosure
 * block (see Arrival.tsx's own header comment) - this test pins that
 * it actually renders, since nothing else in the suite touches this
 * component.
 */
import { render } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { Arrival } from './Arrival';
import type { WorldEntry } from '../data/worlds';

function world(overrides: Partial<WorldEntry> = {}): WorldEntry {
  return {
    worldKey: 'fix',
    censusId: null,
    displayName: 'Fixture World',
    cardName: 'Fixture',
    representativeName: 'Theon',
    roleLabel: 'Teacher',
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

describe('Arrival', () => {
  it('explains the ✲ mark in the existing disclosure block', () => {
    const { getByText } = render(<Arrival world={world()} />);
    expect(getByText(/Look for the ✲ mark after a claim/)).toBeInTheDocument();
  });
});
