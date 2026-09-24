/**
 * Participant-facing words for grounding marks that are Mark's to write
 * (Decision-Log.md Entry 69 §5). Each value below is the wording the app
 * already showed in that place before per-element placement; none is new
 * copy. `pendingMarkWording` lists the ones still waiting on his words -
 * an entry leaves the list only when his own wording replaces the value.
 */

// Title and accessible name of a quote mark's card. Before per-element
// placement a quote shared the story card, so this is the story card's
// own wording.
export const R31_QUOTE_CARD_PHRASE = 'Where this story comes from';

// Heading of the end-of-reply list of general references.
export const R31_END_REFERENCES_HEADING = 'General references';

export const pendingMarkWording = ['R31_QUOTE_CARD_PHRASE', 'R31_END_REFERENCES_HEADING', 'Arrival disclosure line'] as const;
