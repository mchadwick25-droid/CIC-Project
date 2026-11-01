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

// The three labelled layers of a quote card's click page.
export const QUOTE_LAYER_RENDERING = "In today's English";
export const QUOTE_LAYER_EDITION = 'In the edition';
export const QUOTE_LAYER_ORIGINAL = 'In the original';


// The labelled layers of a term card's click page.
export const TERM_LAYER_PLAIN = 'In plain English';
export const TERM_LAYER_WORLD = 'In this world';
export const TERM_LAYER_TODAY = 'How we hear it today';
export const TERM_LAYER_FRIENDS = 'Not to be confused with';
export const TERM_LAYER_RESTS_ON = 'What it rests on';
export const TERM_UNAVAILABLE = 'unavailable';

// The risk flag in plain words, by distortion_risk.
export const TERM_RISK_PHRASES: Record<string, string> = {
  low: 'Low risk of being misheard today.',
  medium: 'Often misheard today.',
  high: 'Very easily misheard today.',
};
