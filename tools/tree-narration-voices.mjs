/**
 * Per-movement ElevenLabs voice overrides for Church Family Tree narration.
 *
 * Atlas narration only - this never touches live-conversation voice, which
 * stays free browser speechSynthesis per its own separate decision (kept
 * free for now, live with the rough edges).
 *
 * Every movement narrates with the single consistent narrator set by the
 * ELEVENLABS_VOICE_ID env var (e.g. "Josh"), UNLESS its id appears below
 * with a non-empty voice id - reserved for the movements that already have
 * a live built Representative, each getting their own distinct narrator
 * voice once Mark has auditioned and chosen one in ElevenLabs' own
 * dashboard. Leave a value '' to keep using the default narrator for that
 * movement in the meantime.
 */
// Movement id -> registry-verified Representative name, cross-checked
// against records/worlds/<code>.yaml and each world's own registry log
// (2026-09-27). Comment only, for readability; the empty string is what
// the script actually reads until a voice id is chosen.
export const voiceOverrides = {
  'post-apostolic-house-church': '', // Chloe (pahc)
  'alexandria-catechetical': '', // Theon (alx)
  'desert-monasticism': '', // Papnoute (desert)
  'syriac-edessa-nisibis': '', // Mar Yausep (syr)
  'cappadocian-nicene-pastoral-monastic-tradition': '', // Chilo (cappadocian)
  'hieronymian-ascetic-literary': '', // Albina (hal)
  'gallic-monastic-ascetic-christianity': '', // Renatus (gallic)
  donatism: '', // Fidelis (don)
  'lutheran-wittenberg-and-its-congregations': '', // Nikolaus (witt)
  'the-reformed-cities-zurich-and-geneva': '', // Theophilus (rzg)
  'imperial-juridical-christianity': '', // Marius (ijc)
};
