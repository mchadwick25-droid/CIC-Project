# Handoff — conversation chooser, research and design — 2026-10-19

From session: https://claude.ai/code/session_01DieKxWNS33gUktGHTTiGeS · Workstream: Conversation-Chooser (landing page and table launch) · Branch / PR: PRs 982, 983 and 984, all merged into `main`; this file lands with PR 985

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Research plan, comparison grid (fifteen rows, each labelled opened, partly opened or indexed only) and a browser harness. | `Build/Ministry/Features/Conversation-Chooser/Research/`; private pages linked from the feature README. The harness ran against the live CiC pages and the Rijksmuseum. Seven systems stayed indexed only: the allowed-hosts change never reached the session. |
| Three design directions as a clickable prototype; Mark chose B, a hand of five dealt from a deck. | `Prototype/chooser-directions.template.html` with its README; private page `https://claude.ai/artifact/Npf19NpmiF9hKsPKcsj5ah`. Script parses; local Playwright runs found no page errors. |
| Converged design and later change orders, all in Mark's words. | `Decision-Log.md` in the feature folder, with the reasoning beside each. |
| Build plan for a later thread. | `Build-Plan.md`. Line numbers were read from `main` at `97f80128`. |
| Records: Features index row, Theme D entries in `Pilot_Feedback_Decisions.md`, an entry in `CiC_FrontEnd_Decision_Log.md`. | On `main` through PRs 982 to 984. `check_paths.py` 0 new unresolved; `check_live_commentary.py` exit 0. |

The converged design, in short: a collector's card per world (standard proportion, era bar, title strip, full-bleed portrait, name plate with the tagline; stat block, longer summary and record line on the back). A hand of five dealt from a deck; Shuffle; a search that brings matches into the hand; "See all" as a scroll of the whole deck under the hand; a tray that seats two or three for the table; a list fallback for phones and reduced motion. It replaces the chair strips and the table launch. The story teasers sit above the hand. Donatism stays live; the deck is eleven. The hand stays as it is, to be judged after the pilot on which control launches each room. Every path lands on the existing talk page, so the room's welcome, disclosure and safety handling are unchanged.

## 2. Not done

- Nothing is built. No live or canonical file was edited.
- The eleven taglines and the back summaries are drafts under their own review on the Gateway Cards page; Mark has signed off none.
- The claim-check fixes to the world records (the other thread's audit; Desert weakest) are not done. A card back ships only after its world's fixes.
- Google Arts and Culture, BibleProject, Material's site, Spotify, Netflix, Duolingo, Khan Academy and Europeana were not opened; the harness is ready when the hosts clear.
- The prototype uses the 192 px thumbnails and one crop point for all portraits.

## 3. Re-check before you trust it

- Build-plan line numbers — `main` moves; re-read before editing.
- "The other six chairs →" on the tradition pages — reported by a read-only agent; not found by a plain grep of the template or generator. Find where it is produced.
- That every live world's census `voices` strings open with a sentence giving the figure's relation to the world — checked for Donatism only. The "why it matched" line depends on it.
- The three era tones — proposals, unmeasured against the dark ground.
- That B scales to a hundred worlds — reasoned, not tested.
- The registry `card:` block and the census sync extension — designed, not written; `census_sync.py` line 47 is the hook.

## 4. Waiting on Mark

- Sign-off on the eleven taglines once their review clears. Nothing else waits on him.

## 5. Next step

A build thread opens `Build/Ministry/Features/Conversation-Chooser/Build-Plan.md`, re-checks section 3 above, and starts at step 1 (data). Schedule it early in a week after the Friday reset; it is a heavy step. If the allowed hosts have cleared, run `node Research/harness/open.mjs gac https://artsandculture.google.com/` first and amend the grid's row 1.

## 6. Spend

Allowance share used: one long session, one read-only subagent, no metered calls. Metered: none.
