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

export interface FacilitatorTurn {
  kind: 'door' | 'threshold' | 'safety' | 'bridge' | 'close';
  text: string;
}

export interface VoiceTurn {
  speaker: string; // the world_key, e.g. "alx"
  text: string;
  citations: Citation[];
  glosses: unknown[]; // declared by the event catalog, not populated by any code path yet
  figures_used: FigureUsed[];
  quote_offers: unknown[];
  attempts_meta: Record<string, unknown>;
}

export interface CreateSessionResponse {
  session_id: string;
  session_code: string; // shown once; required as `Authorization: Session <code>` on every later request
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
}

export interface ApiError {
  status: number;
  detail: string;
}
