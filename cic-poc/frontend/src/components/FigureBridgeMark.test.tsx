import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { FigureBridgeMark, formatDates } from './FigureBridgeMark';
import type { FigureUsed } from '../types/conversation';

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

describe('FigureBridgeMark full entry', () => {
  it('lists the sources last, under a plain "Sources" heading', () => {
    const figure: FigureUsed = {
      id: 'fix.figure.example',
      matched_name: 'Cyprian',
      names: [{ name: 'Cyprian', tag: 'scholarly' }],
      bridge_line: 'Example bridge line.',
      dates: { died: '258' },
      sourced_by: [{ source_id: 'src.1', citation: 'Example citation', author: null, work: null, locus: null, rights_status: null } as FigureUsed['sourced_by'][number]],
    };
    render(<FigureBridgeMark label="Cyprian" figure={figure} />);
    fireEvent.click(screen.getByRole('button', { name: 'Cyprian' }));

    const labels = Array.from(document.querySelectorAll('.level3__section-label')).map((el) => el.textContent);
    expect(labels).toEqual(['Who this is', 'Sources']);
    expect(screen.queryByText("What's said here, sourced from")).toBeNull();
  });
});
