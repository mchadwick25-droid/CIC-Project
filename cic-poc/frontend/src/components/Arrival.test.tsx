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

describe('Arrival order', () => {
  it('puts the disclosure before the folded "knows well" box, and keeps the living-tradition line outside it', () => {
    const { container } = render(<Arrival world={world({ livingTraditionFlag: true })} />);
    const disclosure = container.querySelector('.arrival__disclosure')!;
    const thinness = container.querySelector('details.arrival__thinness') as HTMLDetailsElement;
    expect(thinness).not.toBeNull();
    expect(thinness.open).toBe(false);
    expect(disclosure.compareDocumentPosition(thinness) & Node.DOCUMENT_POSITION_FOLLOWING).toBeTruthy();
    const living = container.querySelector('.arrival__living-tradition')!;
    expect(thinness.contains(living)).toBe(false);
  });
});
