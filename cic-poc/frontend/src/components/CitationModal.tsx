/**
 * CitationModal component - full sourcing detail for a message's citations.
 *
 * Level 3 of the same transparency mechanic LexiconModal provides for
 * lexicon terms - deliberately mirrors its layout (and shares its
 * Level3Panel container) so a participant learns one interaction pattern
 * once and it applies everywhere sourcing shows up.
 */

import type { Citation, RegistryEntry } from '../types/conversation';
import { Level3Panel } from './Level3Panel';

interface CitationModalProps {
  citations: Citation[];
  onClose: () => void;
}

function registryTag(entry: RegistryEntry): string {
  const confidence = entry.confidence || entry.confidence_level || entry.citation_reliability;
  const boundary = entry.boundary_status;
  return [confidence, boundary].filter(Boolean).join(', ');
}

export function CitationModal({ citations, onClose }: CitationModalProps) {
  return (
    <Level3Panel onClose={onClose}>
      <div className="lexicon-modal__header">
        <h2>Sources for This Turn</h2>
        <p className="lexicon-modal__aliases">
          {citations.length} {citations.length === 1 ? 'source' : 'sources'} grounded this response
        </p>
      </div>

      <div className="lexicon-modal__content">
        {citations.map((citation, index) => (
          <div key={index} className="lexicon-modal__section citation-modal__entry">
            <h3 className="lexicon-modal__section-title">
              <span className={`citation-tooltip__kind citation-tooltip__kind--${citation.type || 'lexicon'}`}>
                {citation.type === 'story' ? 'Story' : 'Term'}
              </span>{' '}
              {citation.term}
            </h3>
            <div className="lexicon-modal__section-content">
              <p>{citation.key_sources}</p>
              {citation.registry && citation.registry.length > 0 && (
                <p className="citation-modal__registry">
                  {citation.registry.map((entry) => registryTag(entry)).filter(Boolean).join(' · ')}
                </p>
              )}
            </div>
          </div>
        ))}
      </div>
    </Level3Panel>
  );
}
