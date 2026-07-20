/**
 * MessageBubble component - displays a single turn in the conversation as
 * labeled flowing prose (Increment 1 §1.3: "we are not texting the
 * Representatives, we are talking with them" - the card/bubble grammar is
 * struck; three voices distinguished by label + type treatment alone).
 *
 * Facilitator: unlabeled, italic, graphite - they orchestrate, not participate
 * Representative: a gold-leaf small-caps "{name} · {world}" label, upright prose
 * Participant: a lapis "You" label, the question itself in italic
 */

import type { Message, SpeakerName, LexiconTerm, Citation } from '../types/conversation';
import { HighlightedText, getTermMatches } from './LexiconHighlight';
import { CitationMarker } from './CitationMarker';

interface MessageBubbleProps {
  message: Message;
  termMap: Map<string, LexiconTerm>;
  onTermClick?: (term: LexiconTerm) => void;
  onCitationClick?: (citations: Citation[]) => void;
  /** Map of message name (speaker key) to that world's display name, for the Representative label's "{name} · {world}" grammar. */
  worldNames?: Record<string, string>;
  /** Term keys allowed to render as interactive highlights in this message (first-occurrence-only filtering). Omit to highlight every match. */
  allowedTermKeys?: Set<string>;
}

// Representative display name by message name
const REPRESENTATIVE_NAMES: Record<string, string> = {
  mar_yausep: 'Mar Yausep',
  chloe: 'Chloe',
  papnoute: 'Papnoute',
  albina: 'Albina',
  theon: 'Theon',
};

function getSpeakerInfo(message: Message): {
  name: string;
  role: string;
  className: string;
} {
  if (message.role === 'user') {
    return {
      name: 'You',
      role: 'participant',
      className: 'message--participant',
    };
  }

  const speakerName = message.name as SpeakerName;

  switch (speakerName) {
    case 'facilitator':
      return {
        name: 'Facilitator',
        role: 'facilitator',
        className: 'message--facilitator',
      };
    case 'mar_yausep':
    case 'chloe':
    case 'papnoute':
    case 'albina':
    case 'theon':
      return {
        name: REPRESENTATIVE_NAMES[speakerName] || 'Representative',
        role: 'representative',
        className: 'message--representative',
      };
    default:
      return {
        name: 'Facilitator',
        role: 'facilitator',
        className: 'message--facilitator',
      };
  }
}

export function MessageBubble({ message, termMap, onTermClick, onCitationClick, worldNames, allowedTermKeys }: MessageBubbleProps) {
  const { name, role, className } = getSpeakerInfo(message);

  // Only highlight terms in representative messages
  const shouldHighlight = role === 'representative' && termMap.size > 0;

  const lines = message.content.split('\n');

  // Assign each allowed key to exactly one line - the first line it
  // actually appears in - as a plain, side-effect-free computation. Each
  // line then gets its OWN immutable Set, so HighlightedText never receives
  // a mutable object shared across calls (mutating a shared prop during
  // render is unsafe under React StrictMode's double-invocation: the second
  // invocation would see whatever the first already consumed).
  const perLineAllowedKeys: Set<string>[] = (() => {
    if (!shouldHighlight || !allowedTermKeys || allowedTermKeys.size === 0) {
      return lines.map(() => new Set<string>());
    }
    const remaining = new Set(allowedTermKeys);
    return lines.map((line) => {
      const forThisLine = new Set<string>();
      for (const key of getTermMatches(line, termMap)) {
        if (remaining.has(key)) {
          forThisLine.add(key);
          remaining.delete(key);
        }
      }
      return forThisLine;
    });
  })();

  // World name for this representative's "{name} \u00B7 {world}" label (if available)
  const speakerKey = message.name?.toLowerCase().replace(' ', '_') || '';
  const worldName = worldNames?.[speakerKey];

  return (
    <div className={`message ${className}`} data-role={role}>
      {/* Facilitator turns are unlabeled, italic graphite prose */}
      {role === 'facilitator' && (
        <div className="message-facilitator__content">
          {message.content.split('\n').map((line, index) => (
            <p key={index}>{line || '\u00A0'}</p>
          ))}
        </div>
      )}

      {/* Representative turns: a gold small-caps "{name} \u00B7 {world}" label above flowing prose */}
      {role === 'representative' && (
        <>
          <span className="turn-label turn-label--representative">
            {name}{worldName ? ` \u00B7 ${worldName}` : ''}
          </span>
          <div className="turn-prose">
            {lines.map((line, index) => {
              const isLastLine = index === lines.length - 1;
              return (
                <p key={index}>
                  {shouldHighlight ? (
                    <HighlightedText
                      text={line || '\u00A0'}
                      termMap={termMap}
                      onDetailClick={onTermClick}
                      allowedKeys={perLineAllowedKeys[index]}
                    />
                  ) : (
                    line || '\u00A0'
                  )}
                  {isLastLine && message.citations && message.citations.length > 0 && (
                    <CitationMarker citations={message.citations} onDetailClick={onCitationClick} />
                  )}
                </p>
              );
            })}
          </div>
        </>
      )}

      {/* Participant turns: a lapis "You" label, the question itself in italic */}
      {role === 'participant' && (
        <>
          <span className="turn-label turn-label--participant">You</span>
          <div className="message-participant__content">
            {message.content.split('\n').map((line, index) => (
              <p key={index}>{line || '\u00A0'}</p>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
