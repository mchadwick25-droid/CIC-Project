# Recording settings

Every paid run passes these on the command, one story per command, and its printed settings are checked against this page before the run is called valid (Kit, Part 3, step 9). They change only with Mark's words in the Decision-Log.

## A person

Sally Ford, from 2026-11-28 (Decision-Log, "The people and stories voice: Sally Ford, speed 1.04"). Documented stories use the same voice id, model and voice settings. `eleven_multilingual_v2` reads no audio tags, so a person run sends no `--open-tag` or `--closing-tag`.

`node Build/tools/generate_tree_narration.mjs --people --only <slug> --person-voice-id kBag1HOZlaVBH7ICPE8x --model eleven_multilingual_v2 --output-format mp3_44100_64 --voice-settings '{"stability":0.95,"similarity_boost":0.68,"style":0,"use_speaker_boost":true,"speed":1.04}' --approved-run "<the run, with Mark's words>" --char-cap <cap>`

## A council or a tradition

`node Build/tools/generate_tree_narration.mjs --only <slug> --voice-id onwK4e9ZLuTAKqWW03F9 --model eleven_multilingual_v2 --output-format mp3_44100_64 --voice-settings '{"stability":0.95,"similarity_boost":0.68,"style":0,"use_speaker_boost":true}' --approved-run "<the run, with Mark's words>" --char-cap <cap>`

Each run is capped under 25,000 credits, and one story is recorded first for Mark's ear.

Sources: the Decision-Log, "The people and stories voice: Sally Ford, speed 1.04" (2026-11-28), batch 9's person runs (`Build/Ministry/Operations/Audits/2026-11-21_batch-9/recording/`), batch 7's council run (`Build/Ministry/Operations/Audits/2026-11-20_batch-7/recording/`), and the Decision-Log, "Recording settings for tradition briefs" (2026-11-25).
