import { cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, describe, expect, it } from 'vitest';
import { GlossMark } from './GlossMark';
import type { GlossUsed, SourceReference } from '../types/conversation';

afterEach(cleanup);

const source = (extra: Partial<SourceReference> = {}): SourceReference => ({
  source_id: 'src.1', citation: 'Apostolic Tradition 17', author: null, work: null, locus: null, rights_status: null, ...extra,
});

const gloss: GlossUsed = {
  id: 'fix.term.catechumen',
  matched_name: 'catechumen',
  plain_meaning: 'A person being taught the faith before baptism.',
  quick_meaning: 'A learner before baptism.',
  world_word: 'catechumen',
  translational_sense: 'A modern ear hears a church member; we mean a learner who is still being taught.',
  heard_today: null,
  meant_here: null,
  false_friend: ['a church member'],
  distortion_risk: 'high',
  confidence: { formation_confidence: 'Documented' },
  rests_on: [source()],
  sourced_by: [source()],
};

const labels = () => Array.from(document.querySelectorAll('.term-mark__layer-label')).map((el) => el.textContent);
const open = () => fireEvent.click(screen.getByRole('button', { name: 'catechumen' }));

describe('GlossMark term card', () => {
  it('hovers with the quick meaning, the confidence phrase and the risk flag', () => {
    render(<GlossMark label="catechumen" gloss={gloss} />);
    fireEvent.mouseEnter(screen.getByRole('button', { name: 'catechumen' }));
    expect(screen.getByText('A learner before baptism.')).toBeTruthy();
    expect(screen.getByText('Recorded directly in a source from the time.')).toBeTruthy();
    expect(screen.getByText('Very easily misheard today.')).toBeTruthy();
  });

  it('shows an unsplit term\'s whole translational block under "In this world" alone', () => {
    render(<GlossMark label="catechumen" gloss={gloss} />);
    open();
    expect(labels()).toEqual(['In plain English', 'In this world', 'Not to be confused with', 'What it rests on']);
    expect(screen.getByText(gloss.translational_sense!)).toBeTruthy();
  });

  it('shows a split term as "How we hear it today" beside "In this world"', () => {
    const split = { ...gloss, heard_today: 'A modern ear hears a church member.', meant_here: 'We mean a learner still being taught.' };
    render(<GlossMark label="catechumen" gloss={split} />);
    open();
    expect(labels()).toEqual(['In plain English', 'How we hear it today', 'In this world', 'Not to be confused with', 'What it rests on']);
    expect(screen.getByText(split.heard_today)).toBeTruthy();
    expect(screen.getByText(split.meant_here)).toBeTruthy();
    expect(screen.queryByText(gloss.translational_sense!)).toBeNull();
  });

  it('names the edition, locus and vendored span of a source that has them', () => {
    const rich = { ...gloss, rests_on: [source({ locus: 'De Unitate 17', edition: 'ANF vol. 5', translator: { name: 'R. E. Wallis', formation_confidence: 'Documented' }, edition_date: { year: 1885, formation_confidence: 'Documented' }, vendored: [{ file: 'cic/texts/cyprian.txt', lines: '10-20', label: 'English' }] })] };
    render(<GlossMark label="catechumen" gloss={rich} />);
    open();
    expect(screen.getByText('ANF vol. 5')).toBeTruthy();
    expect(screen.getByText('cic/texts/cyprian.txt')).toBeTruthy();
    expect(screen.queryByText(/unavailable/)).toBeNull();
  });

  it('says unavailable where a source names no edition and no vendored text, and invents neither', () => {
    render(<GlossMark label="catechumen" gloss={gloss} />);
    open();
    expect(screen.getByText('Translator or editor: unavailable')).toBeTruthy();
    expect(screen.getByText('Line span in the Library: unavailable')).toBeTruthy();
    expect(document.querySelector('.level3 a, [role="dialog"] a')).toBeNull();
  });

  it('renders a gloss logged before the card fields existed', () => {
    const old = { id: gloss.id, matched_name: 'catechumen', plain_meaning: gloss.plain_meaning, quick_meaning: gloss.quick_meaning, translational_sense: null, false_friend: [], sourced_by: [] } as unknown as GlossUsed;
    render(<GlossMark label="catechumen" gloss={old} />);
    open();
    expect(labels()).toEqual(['In plain English', 'What it rests on']);
    expect(screen.getByText('Sources: unavailable')).toBeTruthy();
  });

  it('says unavailable when the term has no source at all, and drops absent layers', () => {
    const bare = { ...gloss, rests_on: [], false_friend: [], translational_sense: null, plain_meaning: null, distortion_risk: null, confidence: null };
    render(<GlossMark label="catechumen" gloss={bare} />);
    open();
    expect(labels()).toEqual(['What it rests on']);
    expect(screen.getByText('Sources: unavailable')).toBeTruthy();
  });
});

describe('GlossMark edition facts', () => {
  const fact = (extra: object) => ({ formation_confidence: 'Documented', ...extra });

  it('prints the translator and edition year with how sure we are', () => {
    const g = { ...gloss, rests_on: [source({ translator: fact({ name: 'Rev. E. Wallis' }), edition_date: fact({ year: 1885, formation_confidence: 'Inferential-Thin' }) })] };
    render(<GlossMark label="catechumen" gloss={g} />);
    open();
    expect(screen.getByText('Translated or edited by Rev. E. Wallis (the edition prints it)')).toBeTruthy();
    expect(screen.getByText('Edition year 1885 (thinly supported)')).toBeTruthy();
  });

  it('says unavailable with what was checked where the row says unknown', () => {
    const g = { ...gloss, rests_on: [source({ translator: fact({ name: 'X' }), edition_date: { formation_confidence: 'unknown', checked: 'title pages and preface' } })] };
    render(<GlossMark label="catechumen" gloss={g} />);
    open();
    expect(screen.getByText('Edition year: unavailable (checked: title pages and preface)')).toBeTruthy();
  });

  it('says unavailable alone where the row holds nothing', () => {
    render(<GlossMark label="catechumen" gloss={gloss} />);
    open();
    expect(screen.getByText('Translator or editor: unavailable')).toBeTruthy();
    expect(screen.getByText('Edition year: unavailable')).toBeTruthy();
  });
});
