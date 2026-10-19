# Handoff — conversation chooser, research and design — 2026-10-19

From session: https://claude.ai/code/session_01DieKxWNS33gUktGHTTiGeS · Workstream: Conversation-Chooser (landing page and table launch) · Branch / PR: `claude/conversation-chooser-design`, PR link in the thread

## 1. Done, and how it was checked

| What was done | How it was checked |
|---|---|
| Research plan (deliverable 1): questions first, six criteria, fourteen systems, network routes. Mark accepted it and chose "Allow hosts, I open them". | `Build/Ministry/Features/Conversation-Chooser/Research/Research-Plan.md`; the private page `https://claude.ai/artifact/HzrgjJunooHwsMXaqWwVX2`; Mark's answer in the thread. |
| Comparison grid (deliverable 2): fifteen rows, each labelled opened, partly opened or indexed only; the six claims judged; gaps listed. | `Research/Comparison-Grid.md`; private page `https://claude.ai/artifact/PLbWFDty3LibDKNv6TQZ27`. Fetched sources are named in its section 5. The harness (`Research/harness/open.mjs`) ran against the live CiC pages and the Rijksmuseum; its JSON output is in the session scratchpad only. |
| Prototype (deliverable 3): three directions on the real eleven cards, era tints, seat tray, reduced-motion and phone fallbacks; direction B revised to deal from a deck with era chips, a search box, a written count and a Tree link. | `Prototype/chooser-directions.template.html` plus its README; private page `https://claude.ai/artifact/Npf19NpmiF9hKsPKcsj5ah`. The script parses (`node --check`), and a local Playwright run found no page errors; the deck search for "augustine" returned one match and the era II deal showed "5 of 6". |
| Convergence: Mark chose B, then "it replaces the chair strips and multi-voice table launch", then "Converged, write the build plan". | `Decision-Log.md` in the feature folder, quoting him. |
| Build plan (deliverable 4). | `Build-Plan.md`. Line numbers were read from `main` at `97f80128` this session. |
| Records: feature folder, Features index row, Theme D chooser entry in `Pilot_Feedback_Decisions.md`, an entry in `CiC_FrontEnd_Decision_Log.md`. | Files on the branch. |

## 2. Not done

- Seven systems stayed indexed only (Google Arts and Culture rendered only through Mark's two screenshots; BibleProject, Material's site, Spotify, Netflix, Duolingo, Khan Academy, Europeana not opened). Mark's Allowed-domains change had not reached this session. The host list he was given is in the thread; the harness is ready.
- The grid's Google Arts and Culture row does not say what a card opens, how it behaves on a phone or with the keyboard, or whether the hand holds more than five.
- Nothing is built. No live or canonical file was edited.
- The "What the record holds" lines in the prototype are first drafts derived from each world's thinness statement; they have had no readability score and no review.

## 3. Re-check before you trust it

- Build-plan line numbers (`index.html` 199 to 245 and 386 to 539; `table.html` 232 to 236, 241 to 289, 272, 305 to 418; `census_sync.py` 47) — `main` moves; re-read before editing.
- "The other six chairs →" footer string — reported by a read-only agent from `traditions/desert-monasticism.html`; a plain grep of `templates/tradition.html` and `generate_tradition_pages.py` did not find it. Find where it is produced.
- The claim that every live world's `voices` strings open with a sentence that explains the figure's relation to the world — checked for Donatism only (`Donatus succeeded Majorinus…`). Check all eleven before the "why it matched" line relies on it.
- The three era tones — proposals, unmeasured. Measure against `#17130F` and `#1E1913` as `World-Accent-Colours.md` does.
- The verdict that B scales to a hundred worlds — reasoned, not tested. No system in the grid was opened at that scale.

## 4. Waiting on Mark

- Merge of this PR (Ministry files only; see `git diff --stat`).
- Where the story teasers sit relative to the hand on the Theme D landing page — options not yet shown.
- The Donatism live-status decision, which decides whether its card ships.
- The eleven intro lines, under their own review on the Gateway Cards page.

## 5. Next step

A build thread opens `Build/Ministry/Features/Conversation-Chooser/Build-Plan.md`, re-checks section 3 above, and starts at step 1 (data). Before that, if the allowed hosts have cleared, run `node Research/harness/open.mjs gac https://artsandculture.google.com/` and amend the grid's row 1.

## 6. Spend

Allowance share used: one long research-and-design session with three artifacts and one read-only subagent. Metered: none.
