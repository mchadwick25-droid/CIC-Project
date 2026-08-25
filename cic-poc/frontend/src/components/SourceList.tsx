/**
 * A real, checkable primary-source reference list - author, work, locus -
 * shared by the citation marker and the name/figure bridge's Level 3, so
 * "look at the source document" reads the same way everywhere it appears.
 */
import type { SourceReference } from '../types/conversation';

interface SourceListProps {
  sources: SourceReference[];
  empty?: string;
}

export function SourceList({ sources, empty }: SourceListProps) {
  if (!sources.length) {
    return empty ? <p className="source-list__empty">{empty}</p> : null;
  }
  return (
    <ul className="source-list">
      {sources.map((s) => (
        <li key={s.source_id} className="source-list__item">
          <span className="source-list__work">{s.work ?? s.source_id}</span>
          {s.author && <span className="source-list__author"> — {s.author}</span>}
          {s.locus && <span className="source-list__locus">, {s.locus}</span>}
          {s.rights_status && <span className="source-list__rights"> ({s.rights_status})</span>}
        </li>
      ))}
    </ul>
  );
}
