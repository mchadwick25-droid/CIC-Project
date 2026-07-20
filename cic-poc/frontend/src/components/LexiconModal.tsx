/**
 * LexiconModal component - the Level-3 full lexicon entry (side panel on
 * desktop, bottom sheet on phone - see Level3Panel).
 */

import type { LexiconTerm } from '../types/conversation';
import { Level3Panel } from './Level3Panel';

interface LexiconModalProps {
  term: LexiconTerm;
  onClose: () => void;
}

export function LexiconModal({ term, onClose }: LexiconModalProps) {
  // Parse the full content into sections
  const sections = parseContent(term.full_content);

  return (
    <Level3Panel onClose={onClose}>
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
    </Level3Panel>
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
