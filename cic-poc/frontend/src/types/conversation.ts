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

export interface Message {
  role: 'user' | 'assistant';
  content: string;
  name?: string | null;
  citations?: Citation[] | null;
}

export interface StartSessionResponse {
  session_id: string;
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
}

export type ConversationPhase =
  | 'reception'
  | 'handoff'
  | 'active_encounter'
  | 'reroot'
  | 'closing';

export type SpeakerName = 'facilitator' | 'mar_yausep' | 'chloe' | 'papnoute' | 'albina' | null;

export interface ConversationState {
  sessionId: string | null;
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
}

export interface LexiconResponse {
  terms: LexiconTerm[];
}
