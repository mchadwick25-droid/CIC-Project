import { cleanup, fireEvent, render } from '@testing-library/react';
import { afterEach, describe, expect, it } from 'vitest';
import type { SourceCard } from '../types/conversation';
import { QUOTE_LAYER_EDITION, QUOTE_LAYER_ORIGINAL, QUOTE_LAYER_RENDERING } from '../lib/markCopy';
import { StoryMark } from './StoryMark';

const quote: SourceCard = {
  record_id: 'fix.quote.a',
  record_type: 'quote',
  label: 'Enchiridion 112 - Augustine',
  sources: [{ source_id: 'fix.source.a', citation: 'Augustine, The Enchiridion, NPNF I, vol. III', author: null, work: null, locus: 'chapter 112', rights_status: null }],
  spoken_rendering: 'The pains may be eased.',
  speaker: 'Augustine',
  means: 'Augustine lets doubters suppose the pains are eased.',
  edition_words: 'But let them suppose that the pains of the damned are eased.',
  original: [{ label: 'Latin', file: 'cic/texts/enchiridion-lat.txt', lines: '10-12' }],
  confidence: { formation_confidence: 'Documented' },
};

afterEach(cleanup);

describe('StoryMark quote card', () => {
  it('hover carries the record meaning and the click page shows three labelled layers', () => {
    const { container, getByText } = render(<StoryMark sources={[quote]} quote />);
    fireEvent.mouseEnter(container.querySelector('.story-mark')!);
    expect(container.querySelector('.story-mark__means')?.textContent).toBe(quote.means);
    fireEvent.click(container.querySelector('.story-mark')!);
    expect(getByText(QUOTE_LAYER_RENDERING)).toBeTruthy();
    expect(getByText(QUOTE_LAYER_EDITION)).toBeTruthy();
    expect(getByText(QUOTE_LAYER_ORIGINAL)).toBeTruthy();
    expect(document.body.textContent).toContain('The pains may be eased.');
    expect(document.body.textContent).toContain(quote.edition_words!);
    expect(document.body.textContent).toContain('cic/texts/enchiridion-lat.txt');
    expect(document.body.textContent).toContain('Augustine, The Enchiridion, NPNF I, vol. III');
  });

  it('names each layer for assistive technology and marks a Latin-only edition as Latin', () => {
    const latin: SourceCard = { ...quote, edition_words: 'Deo gratias.', edition_language: 'Latin', original: [] };
    const { container } = render(<StoryMark sources={[latin]} quote />);
    fireEvent.click(container.querySelector('.story-mark')!);
    const edition = document.querySelector('.story-mark__edition blockquote')!;
    expect(edition.getAttribute('lang')).toBe('la');
    expect(document.getElementById(edition.getAttribute('aria-labelledby')!)?.textContent).toBe(QUOTE_LAYER_EDITION);
    expect(document.querySelector('.story-mark__original')).toBeNull();
  });

  it('a quote with no edition words or original shows only the layers it has', () => {
    const bare: SourceCard = { ...quote, edition_words: null, original: [] };
    const { container, queryByText } = render(<StoryMark sources={[bare]} quote />);
    fireEvent.click(container.querySelector('.story-mark')!);
    expect(queryByText(QUOTE_LAYER_RENDERING)).toBeTruthy();
    expect(queryByText(QUOTE_LAYER_EDITION)).toBeNull();
    expect(queryByText(QUOTE_LAYER_ORIGINAL)).toBeNull();
  });

  it('a story card keeps its label and sources and shows no quote layers', () => {
    const story: SourceCard = { ...quote, record_id: 'fix.story.a', record_type: 'story', spoken_rendering: undefined, edition_words: undefined, original: undefined, means: 'A short meaning.' };
    const { container, queryByText } = render(<StoryMark sources={[story]} />);
    fireEvent.click(container.querySelector('.story-mark')!);
    expect(queryByText(QUOTE_LAYER_RENDERING)).toBeNull();
    expect(document.body.textContent).toContain('Enchiridion 112 - Augustine');
  });
});
