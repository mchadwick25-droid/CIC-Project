# Stage 4 report: answering from the sources, lpc proof run

Shadow run on `lpc`, 2026-11-01. In-plan helpers stood in for every model call; no metered spend; no cost figures recorded (Mark's ruling, relayed 2026-10-31). Code under test: `main` at `d6296887` (merge of #1415), which holds the bound-drafting grammar, the batched answer check, the one rewrite, and the instruction fixes of #1414 and #1415. Library's reviewed lpc `answers` sidecar (#1413) was in place. Nothing was tuned between the run and this report.

## What ran

All 106 questions of `S3-Test100/lpc_106_questions.yaml` (100 questions and the 6 fit traps), through: reader names a sub-question, category and kind; lens filter; offer (sub-question records first); draft with bindings; one batched read of each answer against its bound records; one rewrite from the survivors; the same read of the rewrite; compose; log. An answer abstains in the world's fallback sentence ("We do not have that here.", inserted by code) when too little survives, the rewrite is refused, or the rewrite fails its read.

The run before the proof run found 7 drafts written into the wrong question's slot by a helper, a fault of the test harness, not of the engine. The proof run was checked for the same fault by a separate read of all 106 question and draft pairs: no mismatch.

## Outcome

| | Count |
|---|---|
| Answers | 106 |
| Shipped | 92 (36 clean, 56 rewritten); mean 133 words |
| Abstained | 14 (13%): 6 too little survived, 8 failed the read of the rewrite, 0 refused |
| First read: bound sentences read | 516 |
| First read: unsupported | 71 (added detail 24, widened scope 21, other 11, unresolved referent 10, dropped scope 3, stronger force 2) |
| Placed quotes or stories dropped for fit | 39 |

For comparison, the first run of this pipeline abstained on 20 of 105 and the read struck 90 of 477 bound sentences.

## Against the Stage 4 change order's rows

| Row | Target | Result |
|---|---|---|
| lpc test set: cuts and orphan flags on the 28 sealed probes | Fewer than 45 cuts and 13 orphan flags, answer quality no worse | 23 unsupported sentences struck and 3 unresolved-referent flags on the 28 sealed probes (189 bound sentences read). Quality: see the reading below. |
| Fit to the question, placed quotes and stories | Reported, no target | 39 placements dropped across 106 answers; the reader's fit-trap findings are below. |
| Fabrication on retold stories | Zero added content; every event kept | The reader found no false or invented sentence in the 30 read. Story retellings were not tested separately here. |
| Recall and precision on unsupported sentences; constructed-defect catch rates; seed-control false alarms | At least 0.95, 0.85, 90% per class, 0 of 60 | Not measured in this run. Those rows belong to the held-out judge trial under `Stage1/runs/`; this run reports the pipeline's behaviour on the test set only. |

## Reading

One Opus reader, limited to the lpc shelf and records, read 30 answers drawn with a fresh written seed (20261110): 8 sealed probes, 2 fit traps (of q101 to q106), 20 others. It checked each claim itself and did not trust the pipeline's reads.

| Measure | All 30 | 8 sealed | 2 fit traps | 20 others |
|---|---|---|---|---|
| Tier 1 (false or invented) | 0 | 0 | 0 | 0 |
| Tier 2 (scope or ecology) | 5 | 2 | 0 | 3 |
| Tier 3 (craft) | 26 | 8 | 2 | 16 |
| Depth: rich / adequate / thin / flat | 4 / 12 / 9 / 5 | 1 / 5 / 2 / 0 | 0 / 0 / 1 / 1 | 3 / 7 / 6 / 4 |
| Addresses the question: yes / partly / no | 11 / 13 / 6 | 2 / 5 / 1 | 1 / 0 / 1 | 8 / 8 / 4 |
| Ecology slips | 4 | 1 | 0 | 3 |
| Abstentions | 5 | 0 | 1 | 4 |

All 5 abstentions in the sample were judged false silences by the reader (q043, q074, q081, q100, q102). The reader marked two answers serious (q006, q021).

### Tier 2 items (none is tier 1)

- q006 (serious): "Augustine said God's mercy is shown in easing the torments of the lost." In Enchiridion 112 the easing is a supposition Augustine allows his doubters, not his own teaching. The read let it through as supported.
- q021 (serious, ecology): "the evidence is unexcavated, not empty." This widens the world-core record's wording ("unexcavated", meaning the build has not read the site reports) into a claim about all remains; the shelf (Mesnage 1912) describes excavated basilicas at Carthage. The root cause is the record's wording.
- q072, q075 (ecology): the rule of the council of 256 (`lpc.term.bishop-of-bishops`) stands, undated, as the answer to the pope question, which the term's own `not_for` forbids. In q075 the rewrite dropped the frame sentence that kept it in its years.
- q080 (ecology): "between 258 and 391 we have no pastor's words of our own" drops the source's own hedge; Optatus of Milevis and the African councils are on the shelf.

### Fit traps

q103 handled rightly (the placed Possidius quote answers the question, thinly). q102 abstained: it avoided the turn-the-other-cheek quote, which does not answer self-defence, but Augustine's Letter 47.5 to Publicola on the shelf answers it directly.

### Abstentions (false silences)

Three are offer or record gaps. q100 (were the miracles true) and q102 need City of God XXII.8 and Letter 47.5, which have no records; both go to Library's gap log as record-stage items. q074 (Muslims) is answered by the world's 430 boundary but not offered it. q043 and q081 had records in the draft that the first read struck or the rewrite lost.

### Tier 3, most common

Retrieval misses of the exact line asked for (q042, q038, q099). Rewrites that dropped a framing sentence (q022, q075, q096). Process words spoken in the voice (q021, q080). A name repeated where a pronoun belongs (q006, q096). A claim guard not followed (q038, Paul as the speaker of the Sermon 78 quote).

## What the run shows

- Rigor holds: no false or invented sentence in the sample, and the abstention rate is 13% against 19% in the first run.
- Added detail is still the largest cause in the first read, 24 of 71 struck sentences (34%), down from 26 of 54 (48%) in the first redraft of the 106; widened scope is now close behind (21).
- Depth is the weaker axis: 14 of 30 answers thin or flat and 19 of 30 answer the question only partly or not at all. The voice has no unbound way to state a lack, so a question the ground does not cover gets a thin answer or a question back.
- Both serious findings are of the kind a reading finds and the read misses: a supposition given as teaching (q006), and a record wording that overstates (q021).

## Not changed by this report

Nothing in the engine, the abstain rule, or the records. The open items go where they belong: Library's gap log for the record gaps (Letter 47.5, City of God XXII.8, the `unexcavated` wording of the world-core record), and the coordination thread for any change order on abstention, depth, or the live path's `LIMIT_LINE`.

## Round 2: source fixes and a targeted redraft

Same method and limits as above (shadow, in-plan helpers, no metered spend, no cost figures). Four fixes went in at their source, each as one reviewed PR: the draft and rewrite instructions add no person, place, title or date the bound records lack (#1414); a kept placed passage reaches the rewrite as its marker alone, and a story's lead-in names its subject without telling its facts (#1415); the read, the draft directive and the rewrite instruction keep a record's hedge, concession and date (#1418); the long fallback sentence stands only when a bound or placed sentence follows it (#1421). Library meanwhile fixed the world-core wording and the answers sidecar (#1419, #1420, #1422, #1423).

Redraft sets, drawn after the fixes: the 18 first-run abstentions plus 12 shipped answers (30 answers, before #1415); then 17 answers (the 8 named defects, q029, and 8 shipped) on main at `7e40cdb7`; then q034, q072, q029 and q091 again on main at `de380da9`.

| Set | Shipped | Abstained | Tier 1 | Tier 2 |
|---|---|---|---|---|
| 30 (18 earlier abstentions, 12 shipped) | 25 | 5 | 0 | 1 |
| 17 (8 defects, q029, 8 shipped) | 16 | 1 | 0 | 5 answers, 1 serious |
| 4 (q034, q072, q029, q091) | 4 | 0 | 0 | 4 |

The 17 answers' first read struck 8 sentences (added detail 5, other 2, widened scope 1), against 71 of 516 in the proof run.

Outcome of the nine defects found in the proof run (after the 17-answer set, and the last four after the last set):

- Gone: q006 (a supposition no longer stated as teaching), q021 (matches the fixed world-core wording), q075 (rule dated, given to Cyprian, no pope judgement), q080 (hedge restored), q074 (the world's 430 boundary stated).
- Still present: q072 leads with the council-of-256 rule as "for us", the world's answer on the pope. Its dated form is correct; the "for us" widening and a wrong force ("a rule" for the presiding bishop's account of how the council proceeds) remain, and the read passed them.
- q034: the answer ships the world's own answer record for suicide. The voice wrote "we hold no words of Athanasius", but the net removed all three of its sentences (an absence stated wider than the record it cites; words attributed without a quote record), and the live answer-record fallback (`engine/m4/turn.py` `_answer_record_fallback`) then placed the first-offered doctrinal witness, which is on suicide. Wrong person, silently swapped in, though every word is the record's. The offer for q034 is at its cap and not on point: no record in lpc mentions Athanasius.
- q029 (Origen) and q091 (rabbis, Josephus): no longer an unrelated opposing view or off-topic, but neither answers its question. q029 gives Augustine on endless punishment and Cyprian on repentance without naming Origen; City of God XXI.17 (on the shelf, no record) answers both halves. q091 describes the thinness of the record rather than addressing rabbis or Josephus.

## Design limits and open items

- One rewrite from survivors cannot see that the survivors now answer wrongly: q075 in the proof run kept a rule once its framing sentence was struck. No step was added for it.
- The voice has no unbound way to state a lack, and the fallback sentence is code-inserted only. Questions the ground does not cover therefore get a thin answer, a question back, or an abstention; q029, q034, q091 and the earlier q100 and q102 are of this kind.
- The live path's answer-record fallback places the first-offered witness whether or not it fits the question. This is the live path, left for its own change order.
- Record gaps for Library's gap log: Letter 47.5 to Publicola (q102), City of God XXII.8 (q099, q100), City of God XXI.17 on Origen (q029), no record on Athanasius (q034), and sub-questions with no sidecar records (C11.S4, C11.S8).
- Not measured here: the judge trial's recall, precision and constructed-defect rows (they belong to the held-out trial under `Stage1/runs/`).
