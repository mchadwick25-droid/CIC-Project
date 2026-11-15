# Handover: era 4 Who batch 9

Written by the first worker (session_01JMNsSDVZaALqFK9zbGRSGk) at a clean break after round 3's review landed, because its context passed the 400k rule (coordinator, 2026-11-15). Branch: `claude/cft-who-era4-batch9`. No PR is open yet.

## State

- Seven profiles in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era4/batch9/`: `john-of-damascus`, `theodore-the-studite`, `cyril-and-methodius`, `antony-and-theodosius-of-the-kyiv-caves`, `anskar`, `rimbert`, `clement-of-ohrid`. Stephen the Younger and Nikephoros I were split off to batch 10 (told to the coordinator).
- Majors (coordinator): John, Theodore, Cyril and Methodius, the Kyiv pair, Anskar. Briefs 405-406 words (2:30 cap); Rimbert 365, Clement 369.
- Rulings relayed by the coordinator (2026-11-15): Clement, Mark's pick "Keep as Who, dispute told (Recommended)", needs-ruling closed; the Kyiv pair on the map in era 5, tradition "Kievan Rus' Christianity, 1054-1240", active year 1062, files in this batch. Both are in the README and Open-Gaps 269.
- Rounds 1 and 2 done and applied (`R1_review.md`, `R1_changes.md`, `R2_review.md`, `R2_changes.md`). Round 3 review is `R3_review.md`; its fixes are NOT applied yet.
- **Round 3's result.** Part 1 (John, Theodore, Cyril and Methodius, Clement): no blocking point, 17 minor (R3-M1 to R3-M17). Part 2 (Kyiv pair, Anskar, Rimbert, README, Open-Gaps 269): 1 point marked blocking and 12 minor. Part 2's reviewer says no brief or card has a wrong fact, quote or date, or a contested point told as settled.
  - The one blocking point, Part 2 R3-B1, is procedural: Open-Gaps 269 cites the batch's Decision-Log entry, which is not written yet. That entry is a planned finish step (step 4 below), not a fault in reader-facing text. Whether writing it counts as the fix, or needs Mark's cap ruling, is the coordinator's call. The reviewer also notes that 269's "approved to proceed" holds only if no blocking point goes to Mark.
  - All other round 3 points are minor wording, line-range and record fixes, each with an exact replacement string in `R3_review.md`. Under Mark's standing ruling of 2026-11-14 they are applied as worded, then checked once by a fresh Opus agent looking only at those strings.
  - Two points reopen earlier "not taken" items, with versions that fit the length: Part 1 R3-M10 (explain "the Third Hour" in Clement's brief, paid for by cutting "and gave him houses at Devol") and Part 2 R3-M6 (Adam of Bremen's time in Anskar's brief, kept at 405 words).
  - Part 1 R3-M2 notes that the records half of R2-M2 was not applied: the Mansur contested claim in `records.json` still says "Fabricius agrees". R2_changes.md wrongly says it was applied.
- Open-Gaps 269 is written ("Era 4 Who batch 9", 2026-11-15). Recheck the number against origin/main just before merging; renumber if someone took 269.
- origin/main was merged into the branch once (no conflicts). Local checks passed before round 3: `check_live_commentary --base origin/main --enforce`, `check_spelling --base origin/main --enforce`, `check_paths --baseline tools/check_paths_baseline.txt` (0 new; main has the same 971 accepted), JSON parse, audio equals brief, quotation check.

## What is left

1. Apply round 3's findings (`R3_review.md`). If only minor points in reader-facing text: apply as worded under Mark's standing ruling of 2026-11-14, then one targeted check of only those strings by a fresh Opus agent (`R4_cap-check.md`; does not count toward the cap). If any blocking point is open after round 3: stop and report to the coordinator for Mark's cap ruling.
2. Write `R3_changes.md`. Rebuild the audio from each brief (`[calmly] ` at the start, `[warmly] ` at the start of the last paragraph). Keep a final newline on each JSON file.
3. `records.json` was built from per-person fragments in the first worker's scratchpad, which is gone; edit `records.json` directly from now on.
4. Decision-Log entry: "Who profiles, era 4 batch 9: seven profiles, five majors, ..." (2026-11-15), in the shape of the batch 8 and era 6 batch 2 entries, with Mark's Clement ruling quoted, the coordinator's Kyiv placing and majors, review counts per round, and "What is still open: Open-Gaps 269". Add the cap-ruling entry first if there is one. Point the README's Clement line to it.
5. Run the checks again, merge origin/main, check for conflict markers, take the next free Open-Gaps number, open one draft PR, push once, mark ready, merge on green, and send the coordinator words, spoken time and FK/Flesch per profile.

## How the work was checked (for scripts to rebuild)

- Scores: `from engine.m1.gates import grade_text`; words by `len(text.split())`; time about words / 2.7 seconds.
- Quotation check: for each card, take every `"..."` in the brief and card, normalize (NFC, join hyphen line-breaks, curly to straight quotes, collapse whitespace, lowercase, strip `[157 ]` page marks; for `.xml` files remove `<note>...</note>` and tags), and look for it in the card's own source files. Expected misses, both scan marks the README names: Robinson's "cloakf" (l.2652) and the running head inside Cross's "Who ... among you" (l.11855-11860).

## The review brief used in every round (abridged)

Fresh Opus agents that have not seen the drafting, full effort. Read CLAUDE.md and `Who_Profile_Pattern.md` first. For each changed sentence and card field: reopen the cited lines in context (who speaks, hedges, conditions, dates); every quotation verbatim; search all of `cic/texts` before accepting any absence; look for the held editor who disagrees before accepting a settled claim; names get "of <place>" at first mention; writing checks (AI tells, "not X but Y" / "X, not Y" / "X and never Y", colon-reveals, tails, unclear reference, sentences past about 25 words); lengths and `grade_text`; audio equals brief. Output blocking and minor points, each with the source line quoted and an exact replacement string.

## Lessons from this batch

- Round 1's own fix wording caused five of round 2's seven blocking points: a death turned into a fall, a plural "their" that moved a bishop into the Bollandists' century, a one-source claim put back on a card as settled, a "two princes" that named the wrong pair, and a reviewer's argument misstated. Read every fix as new text against its source.
- The river counts depend on the counting rule (census Who rows vs era 4 card traditions); say which rule, and give both.
- Lives with disputed dates: give every held placing, including the ones in other volumes of the same series (Patrologia Graeca 111 for Clement's Life).
- "Died" and "buried" are different dates; check which one a Life gives.
