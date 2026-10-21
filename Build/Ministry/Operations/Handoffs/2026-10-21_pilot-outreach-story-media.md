# Handoff — Pilot outreach: story posts as audio and visual — 2026-10-21

From session: https://claude.ai/code/session_016TfsmpqN3i7uRXDPKQLpTz · World or workstream: public pilot outreach · Branch / PR: `claude/pensive-cori-culrhf`, no PR

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Outreach plan drafted as an Artifact: audience, funnel, channels, timeline, draft copy, launch checks. Read it at https://claude.ai/artifact/Drv9puyxWEfgiZAMauSPQa (Artifact `read`). | Pilot facts read from `engine/deeper/ops/go-deeper.yaml` (general audience: cap 100, public, one per address, ends 2026-12-31, Tally questionnaire) and `Build/Ministry/Operations/Audits/CiC_PrePilot_Systems_Review_2026-10-15.md` (spend ceiling and daily door). |
| Story library counted: 515 documented stories across 267 of 292 movements in `cic-website/data/world-census.json`; 62 atlas stories in `cic-website/atlas-v3.html` (46 Documented, 16 Widely Accepted). | Counted by script from the JSON in each file. Audio folders: `audio/stories` 62 files, `audio/docstories` 516 files (515 stories plus a manifest), `audio/worlds` 122 clips. |
| Shortlist of eight atlas stories chosen: Perpetua and Felicity, Cædmon's Hymn, Hildegard preaches, John of Montecorvino, Montesinos's Advent sermon, Walatta Petros, Benjamin Lay, Le Chambon-sur-Lignon. | Teaser, caveat and sources of each read in the atlas JSON. Audio file confirmed for each. |
| Readability of the eight scored. | `engine.m1.gates.grade_text`, plus a hand count. Both agreed. Seven of eight teasers score grade 18 to 27. Montesinos scores 11.5. Full texts score grade 12 to 20. |

## 2. Not done

- No story was rewritten. No audio, image, slide or video was made.
- The other 54 atlas stories and 515 census stories were not read, only counted.
- The shortlist is not approved by Mark.
- The Artifact's channel and copy sections predate the media question. They assume text posts.

## 3. Re-check before you trust it

- The story counts — rerun the count against the two files above. The built worlds' stories were not counted. The 122 clips in `audio/worlds` may not be 122 separate stories.
- "Only 32 of 515 census stories are checked against the primary text" — filter `documentedStories[].verification` in `world-census.json`. Those 32 all sit in eras 1 to 3.
- The eight records list most primary sources as "consulted via summary only." Only Perpetua (`cic/texts/perpetua-scillitan-martyrs-lat-grc_robinson1891.txt`) and Bede (`cic/texts/bede_ecclesiastical-history-english-people_giles1903.txt`) have vendored text. Check the rest of `cic/texts/` for the other six by author and work before assuming none exist.
- No audio clip was listened to. Whether the clips match their text was not checked.
- Whether a single story can be reached by its own link was not checked. The map deep-links by movement (`?world=`).
- Image rights were not researched. The Atlas Decision Log (around line 5803) records a recommendation to use public-domain period art and to keep AI generation away from depicting historical people. I did not find a ruling by Mark on it. Check the log before treating it as settled.

## 4. Waiting on Mark

- Approve the eight stories, or swap some. Shown in the Artifact, section "The first eight stories".
- Whether to hold back Nickel Mines (a shooting of schoolgirls, safety-adjacent). Shown in the same section.
- Which formats to build first. Options laid out in the chat of the session above: a single image card, a three-to-five slide carousel, a 30 to 60 second video with a slow pan over one or two images.
- Image policy: public-domain art only, with the source and the artwork's date shown on screen.
- Whether any paid audio or video generation is wanted, and under what cap (see 3.2 in CLAUDE.md).

## 5. Next step

Pick one story from the eight, preferably Cædmon or Perpetua because their primary text is vendored. Make one finished example in all three formats and show it as an Artifact for Mark to react to. Parts of the work:

1. Write one spoken script for the ear: about 80 to 110 words for the short cut, plain sentences, with what we know and what we do not said out loud.
2. Map the script to slides: image and hook, the scene, the evidence, the confidence tag and caveat, the invitation.
3. Find one or two public-domain images with their source lines.
4. Assemble a muted-friendly, captioned video with a slow pan using local tools, no model call.
5. Score the script with the project grader. Run an Opus review of the rewrite.

## 6. Spend

Allowance share used: not measured. Metered: none.
