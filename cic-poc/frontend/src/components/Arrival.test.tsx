import { fireEvent, render } from '@testing-library/react';
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
  it('carries the voice, its place and its living-tradition line, and no disclosure block', () => {
    const { container, getByText } = render(<Arrival world={world({ livingTraditionFlag: true })} />);
    expect(getByText('Theon')).toBeInTheDocument();
    expect(getByText('Nowhere')).toBeInTheDocument();
    expect(container.querySelector('.arrival__living-tradition')).not.toBeNull();
    expect(container.querySelector('.arrival__disclosure')).toBeNull();
    expect(container.querySelector('.arrival__thinness')).toBeNull();
  });

  it('leaves out the living-tradition line for a world that is not one', () => {
    const { container } = render(<Arrival world={world()} />);
    expect(container.querySelector('.arrival__living-tradition')).toBeNull();
  });
});

describe('Arrival doorway', () => {
  it('folds the doorway until Read more, without changing its words', () => {
    const doorwayDescription = 'In the 300s, thousands left the villages. They lived in the desert.';
    const { container, getByText } = render(<Arrival world={world({ doorwayDescription })} />);
    const horizon = container.querySelector('.arrival__horizon') as HTMLElement;
    expect(horizon.textContent).toBe(doorwayDescription);
    expect(horizon.classList.contains('arrival__horizon--open')).toBe(false);
    fireEvent.click(getByText('Read more'));
    expect(horizon.classList.contains('arrival__horizon--open')).toBe(true);
    expect(container.querySelector('.arrival__horizon-more')).toBeNull();
  });

  it('shows no Read more without a doorway', () => {
    const { container } = render(<Arrival world={world()} />);
    expect(container.querySelector('.arrival__horizon-more')).toBeNull();
  });
});

