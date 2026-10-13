import { render, screen } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import { SourceList } from './SourceList';

describe('SourceList', () => {
  it("shows a source's citation line in place of its work, author and rights", () => {
    render(
      <SourceList
        sources={[
          {
            source_id: 'w.source.s',
            citation: 'An Author, A Work, trans. A Translator (1898)',
            author: null,
            work: null,
            locus: 'Hymn I.1',
            rights_status: null,
          },
        ]}
      />,
    );
    expect(screen.getByRole('listitem').textContent).toBe('An Author, A Work, trans. A Translator (1898), Hymn I.1');
  });
});
