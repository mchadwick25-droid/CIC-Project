import { fireEvent, render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { GlossMark } from './GlossMark';
import type { GlossUsed } from '../types/conversation';

const gloss: GlossUsed = {
  id: 'fix.term.catechumen',
  matched_name: 'catechumen',
  plain_meaning: 'A person being taught the faith before baptism.',
  quick_meaning: 'A learner before baptism.',
  translational_sense: null,
  false_friend: ['a church member'],
  sourced_by: [{ source_id: 'src.1', citation: 'Apostolic Tradition 17', author: null, work: null, locus: null, rights_status: null } as GlossUsed['sourced_by'][number]],
};

describe('GlossMark full entry', () => {
  it('lists the sources last, under a plain "Sources" heading', () => {
    render(<GlossMark label="catechumen" gloss={gloss} />);
    fireEvent.click(screen.getByRole('button', { name: 'catechumen' }));

    const labels = Array.from(document.querySelectorAll('.level3__section-label')).map((el) => el.textContent);
    expect(labels).toEqual(['What it means', 'Not to be confused with', 'Sources']);
    expect(screen.queryByText("What's said here, sourced from")).toBeNull();
  });
});
