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
export const voiceOverrides = {
  'post-apostolic-house-church': '',
  'alexandria-catechetical': '',
  'desert-monasticism': '',
  'syriac-edessa-nisibis': '',
  'cappadocian-nicene-pastoral-monastic-tradition': '',
  'hieronymian-ascetic-literary': '',
  'gallic-monastic-ascetic-christianity': '',
  donatism: '',
  'lutheran-wittenberg-and-its-congregations': '',
  'the-reformed-cities-zurich-and-geneva': '',
  'imperial-juridical-christianity': '',
};
