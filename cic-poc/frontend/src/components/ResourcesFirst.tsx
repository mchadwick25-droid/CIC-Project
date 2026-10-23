/**
 * A conversation reopened from the shelf that holds a Facilitator crisis turn shows that turn first, in the
 * Facilitator's own words as they were stored. The text is the server's, never composed here.
 */
import { accountsEnabled, resourcesFirst } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';
import type { ConversationTurn } from '../hooks/useConversation';

export function ResourcesFirst({ turns, sessionId }: { turns: ConversationTurn[]; sessionId: string | null }) {
  const text = accountsEnabled ? resourcesFirst(sessionId) : null;
  if (!text || !turns.some((t) => t.speaker === 'facilitator' && t.text === text)) return null;
  return (
    <section className="resources-first sans" aria-label={copy.resourcesFirst}>
      <p className="resources-first__lead">{copy.resourcesFirst}</p>
      {text.split('\n\n').filter(Boolean).map((paragraph, i) => <p key={i}>{paragraph}</p>)}
    </section>
  );
}
