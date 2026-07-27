/**
 * LexiconModal component - the full lexicon entry (side panel on
 * desktop, bottom sheet on phone - see Level3Panel).
 *
 * S5.4 (Pass 1 §5.6): for migrated worlds (term carries a record_id),
 * the modal fetches the term's repository record and renders its real
 * faces - Level 2 (the on-request plain explanation) first, then the
 * Level 3 Observe → Reflect → Question scaffold with the full record
 * reachable beneath. Unmigrated worlds keep the legacy chunk-parsed
 * sections unchanged (compatibility rule: nothing breaks before its
 * world migrates).
 */

import { useEffect, useState } from 'react';
import type { LexiconTerm, RepositoryRecordEntry } from '../types/conversation';
import { Level3Panel, ORQScaffold } from './Level3Panel';

const API_BASE = '/api';

interface LexiconModalProps {
  term: LexiconTerm;
  onClose: () => void;
}

export function LexiconModal({ term, onClose }: LexiconModalProps) {
  const [record, setRecord] = useState<RepositoryRecordEntry | null>(null);
  const [recordFailed, setRecordFailed] = useState(false);

  const recordId = term.record_id;
  const worldId = term.world_id;

  useEffect(() => {
    let cancelled = false;
    setRecord(null);
    setRecordFailed(false);
    if (!recordId || !worldId) return;
    fetch(
      `${API_BASE}/repository/record/${encodeURIComponent(recordId)}?world_id=${encodeURIComponent(worldId)}`
    )
      .then((r) => (r.ok ? r.json() : Promise.reject(new Error(r.statusText))))
      .then((data: RepositoryRecordEntry) => {
        if (!cancelled) setRecord(data);
      })
      .catch(() => {
        if (!cancelled) setRecordFailed(true);
      });
    return () => {
      cancelled = true;
    };
  }, [recordId, worldId]);

  // Legacy face: the chunk-parsed sections (unmigrated worlds, or a
  // record fetch that failed - fail open to what already works).
  const showLegacy = !recordId || recordFailed;
  const sections = showLegacy ? parseContent(term.full_content) : [];

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

      {showLegacy ? (
        <div className="lexicon-modal__content">
          {sections.map((section, index) => (
            <div key={index} className="lexicon-modal__section">
              {section.title && (
                <h3 className="lexicon-modal__section-title">{section.title}</h3>
              )}
              <div className="lexicon-modal__section-content">
                {section.content.split('\n').map((line, i) => (
                  <p key={i}>{line || ' '}</p>
                ))}
              </div>
            </div>
          ))}
        </div>
      ) : record == null ? (
        <div className="lexicon-modal__content">
          <p className="lexicon-modal__loading">Opening the record&hellip;</p>
        </div>
      ) : (
        <div className="lexicon-modal__content">
          {record.level2 && (
            <div className="lexicon-modal__section lexicon-modal__level2">
              <h3 className="lexicon-modal__section-title">In plain terms</h3>
              {record.level2.sections.map((s, i) => (
                <div key={i} className="lexicon-modal__section-content">
                  <h4 className="lexicon-modal__level2-subtitle">{s.title}</h4>
                  <p>{s.text}</p>
                </div>
              ))}
            </div>
          )}
          <div className="lexicon-modal__section">
            <h3 className="lexicon-modal__section-title">The record itself</h3>
            <ORQScaffold face={record.level3} />
          </div>
        </div>
      )}

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
