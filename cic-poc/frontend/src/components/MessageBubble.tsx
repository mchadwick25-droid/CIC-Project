/**
 * MessageBubble component - displays a single message in the conversation.
 *
 * Facilitator: Minimal, neutral presence - they orchestrate, not participate
 * Representative (Mar Yausep): Prominent, distinctive - the voice of tradition
 * Participant: Clear but secondary - the one asking questions
 */

import type { Message, SpeakerName, LexiconTerm, Citation } from '../types/conversation';
import { HighlightedText, getTermMatches } from './LexiconHighlight';
import { CitationMarker } from './CitationMarker';

interface MessageBubbleProps {
  message: Message;
  termMap: Map<string, LexiconTerm>;
  onTermClick?: (term: LexiconTerm) => void;
  onCitationClick?: (citations: Citation[]) => void;
  worldColors?: Record<string, string>;  // Map of message name to world color
  /** Term keys allowed to render as interactive highlights in this message (first-occurrence-only filtering). Omit to highlight every match. */
  allowedTermKeys?: Set<string>;
}

// Representative display info by message name
const REPRESENTATIVE_INFO: Record<string, { name: string; title: string }> = {
  mar_yausep: {
    name: 'Mar Yausep',
    title: 'Teacher of the Syriac Tradition',
  },
  chloe: {
    name: 'Chloe',
    title: 'Household Leader',
  },
  papnoute: {
    name: 'Papnoute',
    title: 'Elder of the Desert',
  },
  albina: {
    name: 'Albina',
    title: 'Widow of the Household',
  },
};

function getSpeakerInfo(message: Message): {
  name: string;
  title: string;
  role: string;
  className: string;
} {
  if (message.role === 'user') {
    return {
      name: 'You',
      title: '',
      role: 'participant',
      className: 'message--participant',
    };
  }

  const speakerName = message.name as SpeakerName;

  switch (speakerName) {
    case 'facilitator':
      return {
        name: 'Facilitator',
        title: '',
        role: 'facilitator',
        className: 'message--facilitator',
      };
    case 'mar_yausep':
    case 'chloe':
    case 'papnoute':
    case 'albina':
      const info = REPRESENTATIVE_INFO[speakerName] || { name: 'Representative', title: '' };
      return {
        name: info.name,
        title: info.title,
        role: 'representative',
        className: 'message--representative',
      };
    default:
      return {
        name: 'Facilitator',
        title: '',
        role: 'facilitator',
        className: 'message--facilitator',
      };
  }
}

export function MessageBubble({ message, termMap, onTermClick, onCitationClick, worldColors, allowedTermKeys }: MessageBubbleProps) {
  const { name, title, role, className } = getSpeakerInfo(message);

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

  // Get world color for this representative (if available)
  const speakerKey = message.name?.toLowerCase().replace(' ', '_') || '';
  const worldColor = worldColors?.[speakerKey];

  return (
    <div className={`message ${className}`} data-role={role}>
      {/* Facilitator messages are minimal */}
      {role === 'facilitator' && (
        <div className="message-facilitator">
          <div className="message-facilitator__indicator" />
          <div className="message-facilitator__content">
            {message.content.split('\n').map((line, index) => (
              <p key={index}>{line || '\u00A0'}</p>
            ))}
          </div>
        </div>
      )}

      {/* Representative messages are prominent */}
      {role === 'representative' && (
        <div
          className="message-representative"
          style={worldColor ? { '--world-accent': worldColor } as React.CSSProperties : undefined}
        >
          <div className="message-representative__header">
            <span className="message-representative__name">{name}</span>
            <span className="message-representative__title">{title}</span>
          </div>
          <div className="message-representative__content">
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
        </div>
      )}

      {/* Participant messages */}
      {role === 'participant' && (
        <div className="message-participant">
          <div className="message-participant__content">
            {message.content.split('\n').map((line, index) => (
              <p key={index}>{line || '\u00A0'}</p>
            ))}
          </div>
        </div>
      )}
    </div>
  );
}
