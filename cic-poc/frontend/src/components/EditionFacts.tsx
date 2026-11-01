/**
 * Who translated or edited a vendored edition, and the year its own file
 * states, each with how sure we are. Where the corpus-map row says the fact is
 * unknown, the line says "unavailable" and what was checked. Where the row
 * holds nothing at all, the line says "unavailable" alone. Nothing is
 * supplied from anywhere else.
 */
import type { EditionFact, SourceReference } from '../types/conversation';
import { EDITION_FACT_SURENESS, TERM_UNAVAILABLE } from '../lib/markCopy';

function sureness(fact: EditionFact): string {
  return EDITION_FACT_SURENESS[fact.formation_confidence] ?? fact.formation_confidence;
}

function Line({ label, missing, value, fact }: { label: string; missing: string; value: string | number | undefined; fact: EditionFact | null | undefined }) {
  if (fact && value !== undefined && fact.formation_confidence !== 'unknown') {
    return (
      <span className="edition-facts__line">
        {label} {value} ({sureness(fact)})
      </span>
    );
  }
  return (
    <span className="edition-facts__line term-mark__unavailable">
      {missing}: {TERM_UNAVAILABLE}
      {fact?.checked ? ` (checked: ${fact.checked})` : ''}
    </span>
  );
}

export function EditionFacts({ source }: { source: SourceReference }) {
  return (
    <span className="edition-facts">
      <Line label="Translated or edited by" missing="Translator or editor" value={source.translator?.name} fact={source.translator} />
      <br />
      <Line label="Edition year" missing="Edition year" value={source.edition_date?.year} fact={source.edition_date} />
    </span>
  );
}
