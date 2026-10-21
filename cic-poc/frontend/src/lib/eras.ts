export interface Era {
  no: string;
  name: string;
  start: number;
  tint: string;
}

const GOLD = '#D9B35C';

// Dates and tints follow cic-website/data/world-census.json (eras); the band
// names drop the census's leading "The" and trailing "Era".
const ERAS: Era[] = [
  { no: 'I', name: 'Early Church', start: 70, tint: '#C9973A' },
  { no: 'II', name: 'Imperial Church', start: 312, tint: '#7E9B6E' },
  { no: 'III', name: 'Age of Monks and Empires', start: 451, tint: GOLD },
  { no: 'IV', name: 'Early Medieval', start: 622, tint: GOLD },
  { no: 'V', name: 'High Medieval', start: 1054, tint: GOLD },
  { no: 'VI', name: 'Late Medieval', start: 1300, tint: GOLD },
  { no: 'VII', name: 'Reformation', start: 1517, tint: '#6C8DB5' },
  { no: 'VIII', name: 'Enlightenment & Awakening', start: 1650, tint: GOLD },
  { no: 'IX', name: 'Missionary', start: 1815, tint: GOLD },
  { no: 'X', name: 'Global Church', start: 1906, tint: GOLD },
];

/** The era a world's time window opens in. */
export function eraFor(year: number): Era {
  let found = ERAS[0];
  for (const era of ERAS) if (year >= era.start) found = era;
  return found;
}
