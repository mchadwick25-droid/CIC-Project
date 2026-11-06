# Stage 3 report: the quote door and the stories door, proof run on lpc

Shadow run on `lpc`, 2026-11-01. In-plan helpers stood in for every model call; no metered spend; no cost figures recorded (Mark's ruling, relayed 2026-10-31). Code under test: `main` at `f8d0487a` (merge of #1443), with the lpc package pinned at `2026-11-01T21-44-01Z`. That code carries quote card template B with the edition's translator and year (#1434), the lexicon card (#1432), the story card with its long telling, the seven tellings accepted in Decision-Log 60, and the Stage 4 pipeline (bound drafting, one batched read, one rewrite). Nothing was tuned between the run and this report.

## What ran

All 106 questions of `S3-Test100/lpc_106_questions.yaml` (100 questions and 6 fit traps; the 28 sealed probes are q001 to q028), through the same path as the Stage 4 proof run: reader names a sub-question; lens filter; offer; draft with bindings; one batched read; one rewrite from the survivors; the same read of the rewrite; compose; log. The story door ran on, in memory only, as in Stage 4; lpc's registered flag stays off.

One shortcut: the reader and safety classification of each question (212 small replies) was reused from the Stage 4 run, since it depends on the question alone. Every draft, read, rewrite and re-read is new. A separate read of all 106 question and draft pairs found no draft in the wrong question's slot.

## Outcome

| | Count |
|---|---|
| Answers | 106 |
| Shipped | 96 (47 clean, 49 rewritten); mean 128.5 words (136.8 on the sealed 28) |
| Abstained | 10 (9.4%): 4 too little survived, 5 failed the read of the rewrite, 1 rewrite refused |
| Bound sentences kept | 756; withheld by the net 21; withheld as unbound 28 |
| First read: sentences struck | 40 (added detail 22, unresolved referent 8, widened scope 4, dropped scope 2, other 4) |
| Placed quotes or stories dropped for fit | 40 (quotes 29, stories 11) |

For comparison, the Stage 4 proof run abstained on 14 of 106 (13%) and its first read struck 71 of 516 bound sentences.

## Against the Stage 3 change order's numbers

Quote door, on the 28 sealed probes (lpc today in brackets):

| Measure | Target | Proof run |
|---|---|---|
| Answers with a quote placed by code (today 4 of 28) | More than today | Engine placed a quote in 11 of 28 (51 of 106), as in Stage 4. After the fit step dropped 8 of those 11, 3 of 28 shipped (21 of 106). Placed by code: met. Shipped: 3 against 4, not met. |
| All cuts (today 45) | Fewer | 28: 5 by the net, 6 withheld as unbound, 17 struck by the read. A further 13 placements were dropped for fit. Not the same kind of count as the old gates', as in Stage 4. |
| Orphan flags (today 13) | Fewer | 3 unresolved-referent flags (8 across the 106). |
| Depth (replaces words per answer) | No more thin and flat together than 3 of 8 sealed | 2 of 8 (thin 2, flat 0). Met. Mean words are given only for reference: 136.8 sealed. |
| Readability (project target grade 10 or lower, reading ease 60 or higher; for story tellings the target is grade 8 and 7 is accepted) | At target | Sealed: mean grade 10.2, ease 59.7; 17 of 25 scored answers above the ceiling or under 60. All 106: 9.3 and 64.7; 43 of 96 scored answers. Not met on the sealed set. The voice's own sentences alone score 10.4 and 59.1 on the sealed set, so the placed quotes and tellings are not the cause. |

Stories door:

| Measure | Target | Proof run |
|---|---|---|
| 1. Stories marked inline | All of them | Every story in an answer is placed by marker (`[[story:id:length]]`) and nothing else tells one. The engine placed a story in 29 of 106 answers (6 of 28 sealed); 17 shipped (0 of 28 sealed), 12 short and 5 medium. The long telling is never placed; it is on the card. |
| 2. Told from a reviewed record only | 100% | 100% by construction: no sentence the voice wrote tells a story, and the 17 shipped are the record's own tellings. |
| 3. Story placements cut | Reported | 11 of the 29 dropped by the fit step. |
| 4. Faithfulness of a shortened or long telling | Every event kept, nothing added | One independent Opus reader read all 21 tellings (short, medium, long, 7 stories) against their cited sources. 19 faithful at Tier 1; 2 Tier 1 findings, both in `lpc.story.election-of-cyprian` (short: "surrounded his house", Pontius does not say whose house; long: "he held no office yet", Pontius has Cyprian already a presbyter). 0 Tier 2, 12 Tier 3. Not zero tolerance: OG-153. |

Three-level transparency:

- **Quote door cards.** 18 distinct quotes were placed in shipped answers. Every one carries the one-line meaning, the spoken rendering, the edition's words and a vendored line span. 4 carry a translator and edition year with their confidence (2 of the 4 with a year the row marks unknown, shown as "unavailable" with what was checked); 14 carry neither and show "unavailable". The cause is 15 cited source entries with no `shelf_row`, so there is no row to read (OG-152).
- **Story cards.** All 7 stories placed carry the meaning, narrative tier, heart and the long telling, and a vendored span.
- **Lexicon cards.** All 19 lpc terms render all five layers with the real data; 31 of the 50 sources carry a vendored line span; the other 19 say "Line span in the Library: unavailable" (render check of 2026-11-01).
- **Still-works check.** Lexicon highlight with hover and click-through and the citation marker with its links: `test_transparency_still_works.py` passes in CI on `main` with these cards in.

## Reading

One Opus reader, limited to the lpc shelf and records, read 30 answers drawn with a fresh written seed (20261111): 8 sealed probes, 2 fit traps, 20 others. It checked each claim itself and did not trust the pipeline's reads.

| Measure | All 30 | 8 sealed | 2 fit traps | 20 others |
|---|---|---|---|---|
| Tier 1 (false or invented) | 0 | 0 | 0 | 0 |
| Tier 2 (scope or ecology) | 1 | 0 | 1 | 0 |
| Tier 3 (craft) | 24 | 7 | 2 | 15 |
| Depth: rich / adequate / thin / flat | 8 / 7 / 12 / 3 | 2 / 4 / 2 / 0 | 0 / 0 / 1 / 1 | 6 / 3 / 9 / 2 |
| Addresses the question: yes / partly / no | 13 / 13 / 4 | 4 / 4 / 0 | 0 / 0 / 2 | 9 / 9 / 2 |
| Ecology slips | 0 | 0 | 0 | 0 |
| Abstentions | 2 | 0 | 1 | 1 |

For comparison, the Stage 4 reading of 30 answers: Tier 1 0, Tier 2 5, depth 4 / 12 / 9 / 5, addresses 11 / 13 / 6.

All placed quotes and stories that were read fit the question; none was off the point. The reader marked one answer serious (q101).

### The Tier 2 item and the fit traps

- q101 (a father beating a son out of love, serious): "What our record does hold is how a bishop met those under his care when they failed" implies the record has nothing on the question. `lpc.quote.love-and-do-what-thou-wilt` ("A father beats a boy… it is charity that beats") answers it. Retrieval missed it. Its guard (not a warrant for striking anyone today) could have been kept while answering the historical question.
- q102 (Augustine on self-defence) abstained, a false silence: Letter 47 to Publicola, s.5, on the shelf, answers it. The record gap is already logged (Stage 4 report; no record for Letter 47.5).
- Both fit traps were therefore handled wrongly; neither placed an off-point quote.

### Abstentions

q034 (Athanasius) is right: he is outside the world and off the shelf. q102 is the false silence above. q032 (Antony) and q099 (miracles) deflect without the stock phrase; q099 is a coverage gap (City of God XXII.8 and Possidius 29 have no lpc record).

### Tier 3, most common

Retrieval misses (q038 no "Love, and do what you will"; q090 only the pattern record; q028 left out the Gehenna passage). Questions not answered (q093 Eucharist, q032, q033, q087 never says plainly that it will not invent a childhood). Off-point filler (q064, q075). A build-process phrase spoken in the voice (q021, "has yet been read"). An opening non sequitur (q089).

## What the run shows

- Rigor holds again: no false or invented sentence in 30 answers read, and the abstention rate fell to 9.4% from 13%.
- Depth is about the same overall: rich answers doubled (4 to 8) and flat ones fell (5 to 3), but thin rose (9 to 12), so thin and flat together are 15 of 30 against 14. The questions answered fully or partly rose from 24 to 26 of 30, and Tier 2 fell from 5 to 1.
- Placed quotes now come with the edition's words, a translator and a year wherever the data links; the gap is 15 source entries with no `shelf_row` (OG-152).
- Quote shipping is the open number: the engine places more quotes than today but the fit step drops most of the sealed ones. Mark's 30-placement fit read is how that call is checked.
- Readability on the sealed set is a hair over the target and comes from the voice's own sentences (OG-154).

## Left for Mark's time

Put to Mark as an Artifact, not written into the repo: the 30 quote placements to read for fit (15 the fit step let through, 15 it dropped, seed 20261111) and the 21 tellings. Held for him: the 15% length tolerance and how the Numidicus telling closes.

## Not changed by this report

Nothing in the engine, the abstain rule, the cards or the records. Gaps go to `Open_Gaps_Tracking.md` (OG-152 to OG-154); the Election lines go to Library. No new gate or pass is added.
