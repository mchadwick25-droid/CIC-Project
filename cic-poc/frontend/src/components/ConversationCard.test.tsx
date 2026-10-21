import { render } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { ConversationCard } from './ConversationCard';
import type { WorldEntry } from '../data/worlds';

const world: WorldEntry = {
  worldKey: 'desert',
  censusId: null,
  displayName: 'Desert Christianity',
  cardName: 'Desert',
  representativeName: 'Papnoute',
  place: 'Egypt',
  eraStart: 330,
  eraEnd: 400,
  thinnessStatement: '',
  doorwayDescription: null,
  livingTraditionFlag: false,
  starters: [],
  portraitImage: '/p.png',
  accentColor: '#000',
};

describe('ConversationCard', () => {
  it('shows the era band, the portrait and the name, with the era tint', () => {
    const { container } = render(<ConversationCard world={world} />);
    expect(container.querySelector('.conv-card__band')?.textContent).toBe('II. Imperial Church');
    expect(container.querySelector('.conv-card__name')?.textContent).toBe('Papnoute');
    expect(container.querySelector('img')?.getAttribute('src')).toBe('/p.png');
    expect(container.querySelector('img')?.getAttribute('alt')).toBe('');
    expect((container.firstChild as HTMLElement).style.getPropertyValue('--era')).toBe('#7E9B6E');
  });

  it('lifts only while its voice speaks', () => {
    const { container, rerender } = render(<ConversationCard world={world} />);
    expect(container.querySelector('.conv-card--speaking')).toBeNull();
    rerender(<ConversationCard world={world} speaking />);
    expect(container.querySelector('.conv-card--speaking')).not.toBeNull();
  });
});
