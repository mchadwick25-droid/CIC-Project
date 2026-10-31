# Fit step: calibration on planted pairs, run 1

Decision-Log entry 31 (Stage 4 approved to proceed) and the Stage 4 change order set the bar: the fit step must drop at least 19 of 20 planted pairs before its verdicts count. The bar is the coordination thread's call, reviewed by AI, and follows the seeded-defect catch rate already ruled for the specialist.

## What was run

- `pairs.yaml`: 20 planted pairs (a question on-topic by words with an lpc quote or story record, where the record in its own context does not answer it) and 20 control pairs (a question the record answers). They use 16 quote records and all 7 story records; every story record is in at least one planted and one control pair, and 18 of 20 controls use a record that also appears in a planted pair, so a judge cannot learn that a record is a trap. None of the pairs is a question of the 106-question test set.
- Authored by an Opus agent from the records. A fresh Opus reviewer read every record and the source text around its locus and judged each pair. Planted: 15 passed, 5 needed a new question (p02, p05, p07, p10, p15). Controls: 16 passed, 4 needed wording that did not lead to the answer (p23, p25, p28, p37); the reviewer also suggested a safer wording for p29, which was taken. All replacements were adopted as the reviewer wrote them. The flaw in the five planted fixes was the same: the record half-answered the question, or the answer sat in the context window.
- The judge was four `judge-reader` helpers in this plan, ten prompts each, with no metered call. They saw only the exported prompt: the question, the record's meaning and not_for, the passage at the stated length, and the context window of the source text. They were not told which pairs were planted. The prompts come from `engine/m4/fit_step.py`; the replies are scored by `Sandbox/Answering-From-Sources/goldset/fit.py`.

## Result

| | Pairs | Right | Wrong |
|---|---|---|---|
| Planted (should be dropped) | 20 | 20 | 0 |
| Controls (should be kept) | 20 | 20 | 0 |

Planted: 20 of 20 off-point. Controls: 20 of 20 fits. No reply was unreadable. The bar (19 of 20) is met. Rows are in `runs/calibration-1/fit.jsonl` and the score in `runs/calibration-1/score.json`.

## What this does and does not show

- It shows the judge separates clear cases, including the four pairs the reviewer called hard because the context window holds a nearby answer (p08, p10, p15, p20): all four came back off-point with a reason that points at the record's own guard or at what the passage gives.
- It does not show how the judge treats a genuinely partial fit. The set has no pair labelled `partly`, and every pair was made clear enough for a fresh reviewer to agree on its label. A clean 40 of 40 on a clean set says the judge is not blind to the trap; it does not say how often it will be wrong on a real answer.
- The judge and the authoring and review agents are all from the same vendor, and the judge saw the same reviewed material the reviewer used. The real test is the 106-question run, where the fit step reads placed quotes and stories in real answers, and a person reads a sample.
- The judge helpers ran in this plan, not on a production model. No production fit judge exists; that stays a paid step deferred under Mark's standing rule.
