# Recording settings

Every paid run passes these on the command, one story per command, and its printed settings are checked against this page before the run is called valid (Kit, Part 4, step 9). They change only with Mark's words in the Decision-Log.

## A person

`node Build/tools/generate_tree_narration.mjs --people --only <slug> --person-voice-id onegjDE2z0mQtp1g0HK7 --model eleven_v4 --output-format mp3_44100_64 --voice-settings '{"stability":0.95,"similarity_boost":0.68,"style":0,"use_speaker_boost":true}' --approved-run "<the run, with Mark's words>" --char-cap <cap>`

## A council

`node Build/tools/generate_tree_narration.mjs --only <slug> --voice-id onwK4e9ZLuTAKqWW03F9 --model eleven_multilingual_v2 --approved-run "<the run, with Mark's words>" --char-cap <cap>`

A council run uses the tree's fixed format and delivery, which it prints: `mp3_44100_64`, `{"stability":0.95,"similarity_boost":0.68,"style":0,"use_speaker_boost":true}`.

Sources: batch 9's person runs (`Build/Ministry/Operations/Audits/2026-11-21_batch-9/recording/`) and batch 7's council run (`Build/Ministry/Operations/Audits/2026-11-20_batch-7/recording/`).
