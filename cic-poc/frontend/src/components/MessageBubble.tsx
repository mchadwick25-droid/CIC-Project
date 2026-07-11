/**
 * MessageBubble component - displays a single message in the conversation.
 *
 * Facilitator: Minimal, neutral presence - they orchestrate, not participate
 * Representative (Mar Yausep): Prominent, distinctive - the voice of tradition
 * Participant: Clear but secondary - the one asking questions
 */

import type { Message, SpeakerName, LexiconTerm } from '../types/conversation';
import { HighlightedText } from './LexiconHighlight';

interface MessageBubbleProps {
  message: Message;
  termMap: Map<string, LexiconTerm>;
  onTermClick?: (term: LexiconTerm) => void;
  worldColors?: Record<string, string>;  // Map of message name to world color
}

// Representative display info by message name
const REPRESENTATIVE_INFO: Record<string, { name: string; title: string }> = {
  mar_yausep: {
    name: 'Mar Yausep',
    title: 'Teacher of the Syriac Tradition',
  },
  amma: {
    name: 'Amma',
    title: 'Household Leader',
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
    case 'amma':
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

export function MessageBubble({ message, termMap, onTermClick, worldColors }: MessageBubbleProps) {
  const { name, title, role, className } = getSpeakerInfo(message);

  // Only highlight terms in representative messages
  const shouldHighlight = role === 'representative' && termMap.size > 0;

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
            {message.content.split('\n').map((line, index) => (
              <p key={index}>
                {shouldHighlight ? (
                  <HighlightedText
                    text={line || '\u00A0'}
                    termMap={termMap}
                    onDetailClick={onTermClick}
                  />
                ) : (
                  line || '\u00A0'
                )}
              </p>
            ))}
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
