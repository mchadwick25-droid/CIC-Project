/**
 * Participant-facing words for grounding marks that are placeholders
 * until the final wording is supplied. Each value is the wording the app
 * already showed in that place; none is new copy. `pendingMarkWording`
 * names every placeholder still waiting; an entry leaves the list when
 * its final wording replaces the value.
 */

// Title and accessible name of a quote mark's card. A quote used to share
// the story card, so this is the story card's wording.
export const QUOTE_CARD_PHRASE = 'Where this story comes from';

// Heading of the end-of-reply list of general references.
export const END_REFERENCES_HEADING = 'General references';

export const pendingMarkWording = ['QUOTE_CARD_PHRASE', 'END_REFERENCES_HEADING', 'Arrival disclosure line'] as const;
