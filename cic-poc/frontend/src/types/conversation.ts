/**
 * Types matching engine/api's actual contract (engine/api/app.py,
 * engine/m4/projection.py). Replaces the old cic-poc backend's shape
 * (session_token/Bearer auth, streaming SSE, multi-world tables, lexicon/
 * guided-starter endpoints) - none of that exists in engine/api. See
 * PHASE-1-LAUNCH.md Stage 4: "dropping whatever the old system had that the
 * engine does not."
 */

// engine/m4/citation_cards.py's resolve_source_card - one real, checkable
// primary source (author, work, locus) behind a cited record. `rights_status`
// is read straight from the vendored text's own rights header (public-domain
// throughout the current corpus).
export interface SourceReference {
  source_id: string;
  author: string | null;
  work: string | null;
  locus: string | null;
  rights_status: string | null;
}

export interface SourceCard {
  record_id: string;
  record_type: string;
  label: string;
  sources: SourceReference[];
  // Quote records spoken in a build-authored modern rendering carry both
  // forms: what was said at the table and the original wording, shown on
  // the click page.
  spoken_rendering?: string | null;
  original_wording?: string | null;
  // engine/m4/citation_cards.py's own modern_term enrichment: present only
  // when record_type is "modern_term" - the plain-English sense of a
  // modern word the Facilitator bridged away from the voice, plus the
  // fleet record's own nuance on how the underlying idea relates to the
  // modern word.
  modern_sense?: string | null;
  distinguishing_claim?: string | null;
  // engine/m4/transparency_plan.py attaches the cited record's own
  // confidence envelope verbatim (same object TransparencyAnchor.confidence
  // carries) - optional here because a caller may omit it; a real API
  // response always includes the key (possibly null).
  confidence?: Record<string, unknown> | null;
}

export interface Citation {
  sentence: string;
  record_ids: string[];
  sources: SourceCard[];
}

// engine/m4/name_bridge.py's find_figures_used - one entry per figure
// record whose name (in-world or the scholarly form's short head) appears
// in this turn's text, first occurrence this session only. `names` carries
// both tags (in-world/scholarly) regardless of which one `matched_name`
// actually is, so the Level-3 panel can show "also called" either way.
// `sourced_by` (name_bridge.attach_cited_sources) is the real point: the
// primary sources behind whatever this sentence actually said about or by
// this figure, not just their own biographical dates.
export interface FigureUsed {
  id: string;
  matched_name: string;
  names: { name: string; tag: 'in-world' | 'scholarly' }[];
  bridge_line: string | null;
  dates: Record<string, string | null>;
  sourced_by: SourceReference[];
}

// engine/m4/term_glosses.py's find_glosses_used - one entry per term
// record the voice both cited AND actually said (its world_word's head
// form) in that same sentence. Anchored to citations rather than
// independent word-matching, so this can't fire on a term the voice
// didn't itself choose to cite - see that module's own docstring.
export interface GlossUsed {
  id: string;
  matched_name: string;
  plain_meaning: string | null;
  quick_meaning: string | null;
  translational_sense: string | null;
  false_friend: string[];
  sourced_by: SourceReference[];
}

export interface FacilitatorTurn {
  kind: 'door' | 'threshold' | 'safety' | 'bridge' | 'close';
  text: string;
  // engine/m4/facilitator_turns.py's bridge_turn: present only on a
  // 'bridge' turn - one SourceCard per modern term the Facilitator just
  // bridged away from the voice, so the hover card can show its
  // modern_sense.
  modern_terms?: SourceCard[];
}

// engine/m4/transparency_plan.py's build_transparency_plan - one complete,
// deterministic account of every record this turn cited and where each
// one's mark goes.
// `sentences` gives each of the engine's own sentences its span in the
// turn's `text`; each element sits in one of those sentences at
// [char_start, char_end), and its mark renders at char_end. Every
// record_id in `citations` appears in `references` exactly once, and is
// either an element's record or in `end_references`, never both.
export interface TransparencySentence {
  index: number;
  text_start: number | null;
  text_end: number | null;
}

export type TransparencyElementKind = 'quote' | 'story' | 'term' | 'figure';

export interface TransparencyElement {
  record_id: string;
  record_type: string | null;
  world_key: string;
  confidence: Record<string, unknown> | null;
  repeat: boolean;
  kind: TransparencyElementKind;
  sentence_index: number;
  char_start: number;
  char_end: number;
  surface: string;
}

// A turn stored before per-element placement carries sentence-run anchors
// and none of sentences/elements/end_references; VoiceTurnBody renders it
// with its legacy renderer.
export interface TransparencyAnchor {
  record_id: string;
  record_type: string;
  world_key: string;
  run_start_sentence: number;
  run_end_sentence: number;
  repeat: boolean;
  confidence: Record<string, unknown> | null;
}

export interface TransparencyPlan {
  world_key: string;
  sentences?: TransparencySentence[];
  elements?: TransparencyElement[];
  references: SourceCard[];
  end_references?: SourceCard[];
  anchors?: TransparencyAnchor[];
  unverified_claims: { count: number; sentence_indexes: number[] };
}

export interface VoiceTurn {
  speaker: string; // the world_key, e.g. "alx"
  text: string;
  citations: Citation[];
  glosses: GlossUsed[];
  figures_used: FigureUsed[];
  quote_offers: unknown[];
  attempts_meta: Record<string, unknown>;
  // Additive (Stage 3a/3b) - absent on a transcript entry replayed from
  // before this field existed, present on every turn since. Optional here
  // for that reason, not because a current turn might lack it.
  transparency?: TransparencyPlan;
}

export interface CreateSessionResponse {
  session_id: string;
  session_code: string; // shown once; required as `Authorization: Session <code>` on every later request
  // Stage 0c (Build-Plan.md): null for an interview session (no round cap
  // applies); the table session round cap for a table session.
  round_cap: number | null;
}

export interface MessageResponse {
  turn_no: number;
  routing_action: string | null;
  routing_reason: string;
  degraded: boolean;
  facilitator: FacilitatorTurn | null;
  voice: VoiceTurn | null;
}

export type TranscriptEntry =
  | { speaker: 'participant'; text: string }
  | ({ speaker: 'facilitator' } & FacilitatorTurn)
  | VoiceTurn; // speaker here is the world_key, not the literal string "voice"

export interface TranscriptResponse {
  session_id: string;
  world_key: string | null;
  turn_count: number;
  closed: boolean;
  transcript: TranscriptEntry[];
  // Table sessions (Artifact-7): mode "table" with the seated world_keys;
  // interview sessions carry mode "interview" (or null from older
  // sessions) and world_keys null.
  mode: string | null;
  world_keys: string[] | null;
  round_open: boolean;
  // Stage 0c (Build-Plan.md): same rule as CreateSessionResponse above.
  round_cap: number | null;
}

// POST /message on a table session, and every POST /continue: one
// table-round advance (Artifact-7 SS6) - at most one voice turn per
// response; round_open says whether to /continue for the next.
export interface TableMessageResponse {
  round_no: number;
  round_open: boolean;
  routing_action: string | null;
  routing_reason: string;
  degraded: boolean;
  facilitator: FacilitatorTurn[];
  turn_selected: { world_key: string; position: number } | null;
  voice: VoiceTurn | null;
  position: number | null;
  turn_no: number | null;
  session_closed: boolean;
}

export interface ApiError {
  status: number;
  detail: string;
}

// GET /api/worlds - engine.api.wiring.list_worlds's compiled/frame.json
// projection, per formation world. The doorway's real content source
// (Program-Spec SS165's "detailed world card": display name, period,
// place, thinness statement, starter questions), replacing the
// hand-copied-at-build-time data data/worlds.ts carried until now.
export interface WorldStarter {
  cell: string;
  text: string;
}

export interface WorldSummary {
  world_key: string;
  census_id: string | null;
  display_name: string | null;
  // Friendly participant-facing name; display_name is the scholarly one
  // (both registers are kept, for different contexts).
  card_name: string | null;
  representative: { name: string; role_label: string } | null;
  time_window: { start: number; end: number } | null;
  place: string | null;
  thinness_statement: string | null;
  // Registry-owned participant-facing doorway paragraph (plain English);
  // horizon is the model-facing self-description kept as the fallback.
  doorway_description?: string | null;
  horizon: string | null;
  living_tradition_flag: boolean;
  starters: WorldStarter[];
}

export interface WorldListResponse {
  worlds: WorldSummary[];
}
