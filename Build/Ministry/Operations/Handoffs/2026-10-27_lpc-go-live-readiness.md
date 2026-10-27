# Handoff — lpc: public face built, library-access gate blocks `built`, evidence reruns waiting — 2026-10-27

From session: https://claude.ai/code/session_01JMNsS9bcrM6mQTT5JwvP9o · World or workstream: `lpc` (Latin Pastoral-Congregational Christianity, c. 246–430; Representative Datus) · Branch / PR: `claude/lpc-next-session-2026-10-26`, restarted from `origin/main` after #1177 merged; PR not opened yet at the time of writing

This file says what the next session does. `2026-10-27_lpc-next-session.md` is the brief this session worked from.

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Registry card fields in `records/worlds/lpc.yaml`: doorway, `card_name` "The Ordinary Church", `app` (order 12, accent `#85914E`), thinness statement, `story_placement: false`, `card` with 15 topics and one alias | `Review-Artifacts/Public_Face_Review_2026-10-27.md` (round 1 Revise, 3 P1 and 9 P2, all applied) and round 2 Approved to proceed in `Review-Artifacts/Story_Tellings_And_Public_Face_Review_2026-10-27.md`; `python -m engine.m1.cross_world` 0 new defects; `python -m engine.m6.cli check` pass |
| Datus's portrait served: `cic-website/assets/portraits/datus.jpg` and 344×192 webp thumbnails in the site and the app | Opus review: identical to the approved asset; same shape as nikolaus and theophilus |
| `world_core.living_traditions` authored through s21 as a boundary statement | `deployed lpc` pass; Opus review; Decision Log, 2026-10-27 |
| Traditions page `cic-website/traditions/latin-pastoral-congregational-christianity.html`, chrome from the Wittenberg page, article generated in a scratch worktree | Opus round 2: no Wittenberg, Nikolaus or Luther text; tile equals `doorway_description`; first image is datus.jpg |
| Seven story `telling` fields, Opus-authored | Opus review round 1 (one P1, two P2, applied) and round 2 Approved to proceed; claims gate pass after four single-witness claims were registered |
| Seven figures' `dates.display` rewritten without record ids and build notes (the `ui-field-leak` finding that appeared once lpc was `built`) | `cross_world` 0 new defects; s24 run in a scratch worktree, only the `dates` blocks carried back |
| lpc moved to `built` on the project lead's ruling, then returned to `building` the same day because the fleet library-access gate (`engine.m9.cli check`) failed on it (OG-97, Decision Log change order) | the gate's output reproduced locally; `engine.m9.cli check` re-run after the revert |
| Rebuilt and re-pinned to `packages/lpc/2026-10-27T19-11-58Z` (hash `a2df2a13…`) | `determinism-check lpc` pass; see gate list below |
| One line added to `Source_Registry.md` for the Gregory of Nyssa Greek volume the Library thread vendored | `handoff lpc` step 2 finding cleared |

Gates run on the final head: `records`, `regate`, `claims`, `deployed` and `handoff` for lpc; `tools/check_live_commentary.py --base origin/main --enforce`; `tools/check_paths.py --baseline tools/check_paths_baseline.txt`; `cic/engine/texts_registry.py --check-readme`; the m1, m2, m4, m10 and api suites after restoring every pinned package. Results are in the PR.

## 2. Not done

- **Evidence reruns (admission, 28 sealed probes; full validation with a Deep Interview).** The project lead ruled again today that they wait for the engine fix to F4/F5. The pin changed, so earlier admission and validation runs do not count for it. No metered spend.
- **F4/F5 engine fault (OG-90, OG-95).** No fix on `main`, no open pull request; only the engine thread's brief (#1186) exists. A go-live blocker. Not fixed here.
- **`built`.** Blocked by the library-access gate (OG-97): about 480 findings in eight checks, mostly the 210 source records with no citation or kind and 47 retrieval guards. Needs a content batch or the project lead's named waivers.
- **`admitted`.** Waits for `built` and for admission to pass on the new pin.
- **Hidden `card.keywords`.** Left out on purpose: the project lead approves each one.
- **Sitemap entry for the traditions page.** Left out until the world is listed; the page offers Talk and Table.
- **Record-side defects found on the way (OG-94)** and the world front's "always inside a bond it would not break" line (wrong for grace). Logged, not fixed.

## 3. Re-check before you trust it

- **Cautions 13 to 17 are still untested live.** Their effect on Datus's voice is unproven.
- **`living_traditions` and the `horizon` paragraph now both say the world is still living.** The voice reads both. Which stays is the project lead's call (OG-92 addendum).
- **The accent colour and portrait.** The project lead said today he is not sure of the picture: it is a lot like the others, though it reflects this world. The approved image is in place unchanged.
- **The tellings are hand-added to the records.** A re-run of s24 does not carry them, and does not carry the `canon_cells` that s2y sets either; carry back only parsed content.
- **The pin changed after the tellings review.** The last rebuild followed the figure fixes only, but the package hash is new; run `deployed lpc` and `determinism-check lpc` again if anything merges that touches lpc's inputs. Restore every pinned package before the engine and api tests.
- **Check every changed `manifest.json` parses** after any merge that touches `packages/`.

## 4. Waiting on Mark

- **Governance V3.6 (OG-91).** Whether and where the two check-in cases enter the document. Draft shown as an Artifact on 2026-10-27; not asked again this session.
- **The `horizon` paragraph and `living_traditions` (OG-92).** Keep, move or remove the older paragraph.
- **The portrait.** Keep the approved image or choose another.
- **`card.keywords`** for lpc, one by one.
- **How to get lpc to `built`.** The project lead chose, on 2026-10-27, to clear the gate's findings in a content batch next session, with no waivers. Moving it also needs the `safety_adjacent` key across the other eleven worlds (eleven `registry-key-set` findings), lpc added to `test_observe_outside_help_guard_on_the_real_fleet` (it now carries the guard) and to the R41 probe set (`TEST_PROBES`, `CONTROL_PROBES`, control word `libelli`).
- **The live rerun** once the F4/F5 fix merges: a named test and a cap.
- **Promotion of `main` to `live`.** His alone, through `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md`.

## 5. Next step

First clear the library-access gate findings (OG-97) in a content batch, one subagent at a time, Opus review, then move lpc to `built`. Then check whether the engine thread's fix to F4/F5 has merged. If it has, ask the project lead for a named live test and cap, then run admission and full validation together on the new pin, followed by an Opus review of the transcripts. If it has not, wait.

## 6. Spend

Allowance share used: moderate to heavy (five Opus subagent runs, one at a time). Metered: none this session. The earlier live test "lpc full validation, 27 October" spent $2.21 of its $6 cap; no further spend is approved.
