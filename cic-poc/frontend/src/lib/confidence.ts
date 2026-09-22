/**
 * Stage 6b (Ministry/Features/Conversation-Transparency-Engine/Decision-Log.md,
 * Entry 35 family): one plain phrase per `formation_confidence` value
 * (engine/m1/schemas.py's five-value enum), shown on a citation's Level 2
 * card. R16 (RULED c, Decision-Log.md Entry 29): confidence display reads
 * `confidence.formation_confidence` only, never a record's `status` -
 * `status` is Stage 6a's own eligibility gate for which records can carry
 * a confidence display at all (Decision-Log.md Entries 35-36), not the
 * value shown here.
 *
 * DRAFT COPY - not yet worded by Mark. Per his own Stage 6 instruction
 * ("phrases... worded by me"), this text is a proposal only, built so the
 * mechanism is testable end-to-end. Do not treat this wording as final
 * until Decision-Log.md records his own word on it.
 */
const CONFIDENCE_PHRASES: Record<string, string> = {
  Documented: 'Recorded directly in a source from the time.',
  'Widely Accepted': 'What historians broadly agree happened.',
  'Dominant Modern Reconstruction': 'The leading modern reading of the evidence.',
  Contested: 'Historians disagree about this.',
  'Inferential-Thin': 'Based on thin evidence, mostly inference.',
};

export function confidencePhrase(confidence: Record<string, unknown> | null | undefined): string | null {
  const level = confidence?.formation_confidence;
  if (typeof level !== 'string') return null;
  return CONFIDENCE_PHRASES[level] ?? null;
}
