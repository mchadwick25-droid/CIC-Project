/**
 * TypeScript interfaces for the conversation system.
 */

export interface RegistryEntry {
  id: string;
  [field: string]: string;
}

export interface Citation {
  type?: 'lexicon' | 'story';
  term: string;
  key_sources: string;
  source_file?: string;
  registry?: RegistryEntry[];
}

// A confirmed inline gloss actually used in one representative turn - see
// cic-poc/backend/app/prompts/confirmed_glosses.py, the source of truth
// for both `rendered` (the exact substring to find in the message text)
// and the category/original/gloss breakdown behind it.
export interface GlossUsed {
  category: 'A' | 'B';
  original: string;
  gloss: string;
  rendered: string;
  inline?: boolean;
}

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  name?: string | null;
  citations?: Citation[] | null;
  glosses_used?: GlossUsed[] | null;
}

export interface StartSessionResponse {
  session_id: string;
  session_token: string;  // required as X-Session-Token on every later request to this session
  world_id: string;
  world_ids?: string[];  // For multi-world tables
  messages: Message[];
}

export interface SendMessageRequest {
  message: string;
  close_requested?: boolean;
}

export interface SendMessageResponse {
  messages: Message[];
  phase: ConversationPhase;
  turn_count: number;
}

export interface SessionResponse {
  session_id: string;
  messages: Message[];
  phase: ConversationPhase;
  turn_count: number;
  world_id?: string | null;
  world_ids?: string[];
}

export type ConversationPhase =
  | 'reception'
  | 'handoff'
  | 'active_encounter'
  | 'reroot'
  | 'closing';

export type SpeakerName = 'facilitator' | 'mar_yausep' | 'chloe' | 'papnoute' | 'albina' | 'theon' | 'marius' | null;

export interface ConversationState {
  sessionId: string | null;
  sessionToken: string | null;
  worldId: string | null;
  worldIds: string[];  // For multi-world tables
  messages: Message[];
  phase: ConversationPhase;
  turnCount: number;
  isLoading: boolean;
  error: string | null;
}

// World types
export interface Representative {
  id: string;
  name: string;
  title: string;
  description: string;
}

export interface World {
  id: string;
  name: string;
  subtitle?: string | null;
  period: string;
  region: string;
  description: string;
  representative: Representative;
  color: string;
}

export interface WorldsResponse {
  worlds: World[];
}

// Lexicon types
export interface LexiconTerm {
  term: string;
  aliases: string[];
  quick_meaning: string;
  full_content: string;
  related_terms: string[];
  // S5.4 (additive): the repository record behind this term, present for
  // migrated worlds only - lets the modal fetch Level 2/3 faces.
  record_id?: string | null;
  world_id?: string | null;
}

export interface LexiconResponse {
  terms: LexiconTerm[];
}

// Wave 3 ending-screen rebuild: further-reading packs served from
// backend/data/further_encounter_resources/{world_id}.json - the same
// files the Facilitator's own sensed-closing resources offer reads.
export interface FurtherReadingResource {
  resource_id: string;
  title: string;
  author?: string;
  publisher?: string;
  year?: string;
  type?: string;
  locator?: string;
  note?: string;
  topic_tags?: string[];
}

export interface ResourcePack {
  world_id: string;
  world_offer_label: string;
  resources: FurtherReadingResource[];
}

export interface ResourcesResponse {
  packs: ResourcePack[];
}

// S5.4 - repository faces (Pass 1 §5.6).

// Level 2: the on-request plain explanation, machine-checked at the
// reading floor at render time.
export interface PlainExplanationSection {
  title: string;
  text: string;
}

export interface PlainExplanation {
  record_id: string;
  term: string;
  sections: PlainExplanationSection[];
  readability: {
    fk_grade: number;
    fre: number;
    violations: string[];
    ok: boolean;
  };
}

// Level 3: the Observe -> Reflect -> Question scaffold over the full
// record (a starting shape being tested - the payload says so itself).
export interface Level3Face {
  record_id: string;
  record_type: string;
  title: string;
  scaffold_note: string;
  observe: string[];
  reflect: string[];
  question: string[];
  full_record: Record<string, unknown>;
  conversation_audit_backbone: string;
}

export interface RepositoryRecordEntry {
  id: string;
  record_type: string;
  title: string;
  rights: { gated_fields: string[]; basis: string | null };
  level2?: PlainExplanation;
  level3: Level3Face;
}

// Guided Starters - "Don't know what to ask?" content, one file per seated
// world (see cic-poc/backend/scripts/build_guided_starters_json.py and
// World-Builds/<world>/*Guided_Starters_V0_1_DRAFT.md, the grounded source).
// Four depth tiers per world; the first three are walk-style entries, the
// last (honest_limits) is question/answer pairs with no follow-ups.
export interface GuidedStarterEntry {
  topic: string;
  why: string;
  citations: string[];
  opening_question: string;
  follow_ups: string[];
}

export interface GuidedStarterLimitEntry {
  question: string;
  answer: string;
  citations: string[];
}

export type GuidedStarterTierId =
  | 'first_visit'
  | 'going_deeper'
  | 'for_the_wrestling'
  | 'honest_limits';

export interface GuidedStarterTier {
  tier_id: GuidedStarterTierId;
  tier_title: string;
  entries: GuidedStarterEntry[] | GuidedStarterLimitEntry[];
}

export interface GuidedStarterWorld {
  world_id: string;
  source_file: string;
  title: string;
  status: string;
  world: string;
  purpose: string;
  grounding: string;
  tiers: GuidedStarterTier[];
}

export interface GuidedStartersData {
  $schema_version: string;
  name: string;
  worlds: GuidedStarterWorld[];
}
