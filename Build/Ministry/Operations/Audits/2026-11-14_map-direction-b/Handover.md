# Release 44 map build: handover (2026-11-14)

The first build worker (session_01JMNsSDk6Sa1zM9c44FsCS1) hands over here because its context passed Mark's limit ("keep the workers limited to their efficiancy"). Coordinator: session_01JMNsSChNTbJcEMJUSUv7LC. Brief: direction B, data release 44, as the coordinator gave it. The decision list is `Decisions_Converged.md` in this folder.

## Where things stand

- Branch `claude/cft-map-direction-b`, pushed with no pull request yet. Main (with release 43, era 4 on the tree) is merged in, and no conflict markers are left.
- Built in place in `cft-website/index.html`, with no overlay: A1 to A33, B1 to B5 and C1 to C6, with the defaults and rulings recorded in `Draft_Decision-Log_entry.md`.
- Census: `major` and `activeYear` on all 250 person entries. `tools/validate-census.mjs` requires them, and `engine/m6/census_atlas_sync.py` mirrors them. Church and Empire is on lane 3.4.
- `cic-website/assets/feedback.js`: the feedback bar now sits at the foot of each card.
- `Build/tools/generate_tree_pages.test.mjs`: five tests updated to the new rulings, plus one new test that the map's script parses.
- `Build/tools/tree_site_pages.json` and `cft-website/method.html`: the era 10 closing line in Mark's words.

## Local checks at the last commit

| Check | Result |
|---|---|
| Census validator, with `--base` against main | 0 errors |
| Atlas check | in sync |
| Tree-page tests | 35/35 |
| engine/m6 | 49 pass |
| Live-commentary (enforce) | pass |
| Spelling | pass |
| Overlaps at the A16 zooms (0.2 to 7) | 0 |
| Overlaps with a Who open, all 29 river-eras, desktop and phone | 0 |
| Map height | 12,744 |

Census test suite (the `node --test tools/tests/validate_census_*` line in ci.yml): 65/65. Spelling (enforce): pass.

## Reviews

All by fresh Opus agents at full effort.
- **Round 1** (code, text, AI tells): all fixed. Mark-approved wording went to Mark, and he took all the recommendations.
- **Round 2**: all fixed. Mark's eight wording picks were applied.
- **Round 3**: the text review (`Review_r3-text.md`) found 2 BLOCKING and 4 MINOR points. All six are applied as worded, and one targeted Opus check of only those strings follows, under Mark's standing cap ruling. Its result is `Review_r3-targeted.md`: all six pass.
- **Round 3 code review**: `Review_r3-code.md`. Three new BLOCKING points: see step 1 below.

## Waiting on Mark (through the coordinator)

1. **The majors and active-years table:** https://claude.ai/artifact/Vi1258rn3iDfoHpTXgdfZk
   - It covers 250 people. There are 36 proposals (23 major) under his pick "Worker proposes, you confirm (Recommended)", 8 flagged rows, and 72 proposed years.
   - The census on the branch carries these values pending his confirmation. Any change he makes goes into `cic-website/data/world-census.json`, then run `python3 -m engine.m6.cli atlas-sync`.
2. **P4 from round 3 text:** the river notes (RIVER_LORE) were researched against older member sets and read far over the bar. The reviewer recommends hiding all of them until one owner pass rewrites them. That is Mark's call.
3. **The preview, not yet built.** Mark must approve it before anything merges. It needs:
   - a private Artifact with screenshots at phone, tablet and desktop (`scripts/shots.js`);
   - the overlap numbers;
   - what changed from live;
   - what stays untested: real touch, a screen reader, an older phone, audio;
   - the P4 question.

## Steps left, in order

1. `Review_r3-code.md` (round 3 code, the last round; copied at handover, and the reviewer may have added to it in its own scratchpad) found 3 BLOCKING and 1 MINOR, all new: pressing a Who control moves focus off it; zooming while a Who name has focus drops focus to the body; on tablets with a larger browser text size the Key runs off screen; one unused line (`const years=` in render's river loop). Round 2's finding 2 and round 1's item 8 are still partly open. Under the brief these BLOCKING points, open after round 3, went to the coordinator for Mark; fix them under his ruling, then run one targeted check.
2. Build and publish the preview, then send the link to the coordinator.
3. Open one draft pull request, pushed once after the local checks pass, then mark it ready.
4. After Mark approves:
   - Write the Decision-Log entry from `Draft_Decision-Log_entry.md`, filling in Mark's table confirmation, the review counts and the date.
   - Add his picks: "Worker proposes, you confirm", "Best-known dated act", and the two "Take all" wording picks.
   - Record the era card as a coordinator call that Mark may overrule.
   - Write the Open-Gaps entry from `Draft_Open-Gaps_entry.md`, taking the next free number just before merging (main used 265 at handover), and mark Open-Gaps 217 as met.
   - Data release 44.
5. Merge on green, then check www.churchfamilytree.com.

## Records in this folder

- `scripts/`: the overlap counters and browser checks. They serve `.build/tree` on port 8765 after `node tools/build_tree_site.mjs`.
- `tables/`: the major and active-year tables as JSON, the 36 proposals, and Mark's era-note wording.
- `Review_*.md`: every review round.
