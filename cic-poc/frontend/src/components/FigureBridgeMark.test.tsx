import { describe, expect, it } from 'vitest';
import { formatDates } from './FigureBridgeMark';

describe('formatDates', () => {
  it('labels born, died and floruit for the participant', () => {
    expect(formatDates({ born: 'c. 296', died: '373', floruit: 'bishop 328-373' })).toBe('Born: c. 296 · Died: 373 · Active: bishop 328-373');
  });

  it('shows display and note sentences without the key', () => {
    expect(formatDates({ display: 'traditionally dated c. 96', note: 'later additions' })).toBe('traditionally dated c. 96 · later additions');
  });

  it('drops empty values and unknown keys', () => {
    expect(formatDates({ born: null, died: '222', internal: 'x' })).toBe('Died: 222');
    expect(formatDates({})).toBeNull();
  });
});
