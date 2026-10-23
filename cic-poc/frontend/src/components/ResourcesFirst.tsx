/**
 * A conversation reopened from the shelf that holds a Facilitator safety turn shows that turn first, in the
 * Facilitator's own words as they were stored, every time. The text is the server's, never composed here.
 */
import { useState } from 'react';
import { accountsEnabled, resourcesFirst } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';
import type { ConversationTurn } from '../hooks/useConversation';

export function ResourcesFirst({ turns }: { turns: ConversationTurn[] }) {
  const [shown] = useState(() => accountsEnabled && resourcesFirst());
  if (!shown) return null;
  const safety = [...turns].reverse().find((t) => t.speaker === 'facilitator' && t.kind === 'safety');
  if (!safety) return null;
  return (
    <section className="resources-first sans" aria-label={copy.resourcesFirst}>
      <p className="resources-first__lead">{copy.resourcesFirst}</p>
      {safety.text.split('\n\n').filter(Boolean).map((paragraph, i) => <p key={i}>{paragraph}</p>)}
    </section>
  );
}
