/**
 * LexiconModal component - shows full lexicon entry details.
 */

import type { LexiconTerm } from '../types/conversation';

interface LexiconModalProps {
  term: LexiconTerm;
  onClose: () => void;
}

export function LexiconModal({ term, onClose }: LexiconModalProps) {
  // Parse the full content into sections
  const sections = parseContent(term.full_content);

  return (
    <div className="lexicon-modal-overlay" onClick={onClose}>
      <div className="lexicon-modal" onClick={(e) => e.stopPropagation()}>
        <button className="lexicon-modal__close" onClick={onClose}>
          &times;
        </button>

        <div className="lexicon-modal__header">
          <h2>{term.term}</h2>
          {term.aliases.length > 0 && (
            <p className="lexicon-modal__aliases">
              Also: {term.aliases.slice(0, 5).join(', ')}
            </p>
          )}
        </div>

        <div className="lexicon-modal__content">
          {sections.map((section, index) => (
            <div key={index} className="lexicon-modal__section">
              {section.title && (
                <h3 className="lexicon-modal__section-title">{section.title}</h3>
              )}
              <div className="lexicon-modal__section-content">
                {section.content.split('\n').map((line, i) => (
                  <p key={i}>{line || '\u00A0'}</p>
                ))}
              </div>
            </div>
          ))}
        </div>

        {term.related_terms.length > 0 && (
          <div className="lexicon-modal__related">
            <h4>Related Terms</h4>
            <div className="lexicon-modal__related-list">
              {term.related_terms.map((related, index) => (
                <span key={index} className="lexicon-modal__related-term">
                  {related}
                </span>
              ))}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

interface Section {
  title: string;
  content: string;
}

function parseContent(content: string): Section[] {
  const sections: Section[] = [];
  const lines = content.split('\n');

  let currentTitle = '';
  let currentContent: string[] = [];

  for (const line of lines) {
    if (line.startsWith('## ')) {
      // Save previous section
      if (currentContent.length > 0 || currentTitle) {
        sections.push({
          title: currentTitle,
          content: currentContent.join('\n').trim(),
        });
      }
      currentTitle = line.replace('## ', '').trim();
      currentContent = [];
    } else if (line.startsWith('---')) {
      // Skip separators
      continue;
    } else {
      currentContent.push(line);
    }
  }

  // Save last section
  if (currentContent.length > 0 || currentTitle) {
    sections.push({
      title: currentTitle,
      content: currentContent.join('\n').trim(),
    });
  }

  return sections.filter((s) => s.content.length > 0);
}
