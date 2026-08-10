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
  // Two-tier (2026-08-10) - drawn-on first, consulted after, each saying
  // only what is true of it. See the Citation type for why the wording
  // difference is load-bearing rather than decorative.
  const isDrawnOn = (c: Citation) => c.grounded !== false;
  const drawnOn = citations.filter(isDrawnOn);
  const consulted = citations.filter((c) => !isDrawnOn(c));
  const ordered = [...drawnOn, ...consulted];

  return (
    <Level3Panel onClose={onClose}>
      <div className="lexicon-modal__header">
        <h2>Sources for This Turn</h2>
        <p className="lexicon-modal__aliases">
          {drawnOn.length} {drawnOn.length === 1 ? 'source' : 'sources'} drawn on in this response
          {consulted.length > 0 && (
            <>; {consulted.length} more consulted but not specifically drawn on</>
          )}
        </p>
      </div>

      <div className="lexicon-modal__content">
        {ordered.map((citation, index) => (
          <div
            key={index}
            className={`lexicon-modal__section citation-modal__entry${
              isDrawnOn(citation) ? '' : ' citation-modal__entry--consulted'
            }`}
          >
            <h3 className="lexicon-modal__section-title">
              <span className={`citation-tooltip__kind citation-tooltip__kind--${citation.type || 'lexicon'}`}>
                {citation.type === 'story' ? 'Story' : 'Term'}
              </span>{' '}
              {citation.term}
              {!isDrawnOn(citation) && (
                <span className="citation-modal__tier"> — consulted for this turn</span>
              )}
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
