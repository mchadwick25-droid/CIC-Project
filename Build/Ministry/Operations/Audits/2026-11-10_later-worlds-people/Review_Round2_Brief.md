# P2-G3b: review round 2 (targeted recheck, Opus)

Round 1's reviewers (brief: `../Review_Brief.md`, same rules) raised findings; revisers applied
them. `candidates.json` holds each revised row, the round-1 findings and the round-1 recount.
Recheck ONLY what changed, against the prior findings:

1. Each round-1 BLOCKING or SUBSTANTIAL finding: is it actually fixed in the revised row? Check the
   file where the fix needs evidence.
2. Every quote that is new or changed in the revised row (compare `revision_log`): verbatim in the
   file (grep it), and inside a passage the round-1 recount kept valid.
3. Each `clean` count matches the round-1 recount (refs kept plus refs added); and every counted
   tradition starts after the person's death (use the row's own dates; flag a death date that is
   unsourced only if a counted tradition starts within 50 years of the person's last known year).
4. Recommendation and `question` consistent with the rules in `../Revision_Brief.md`.

Do not re-review what round 1 approved and nobody changed. Do not raise "could be stronger".
Write `review.json` (same shape as round 1) in this folder, then a short summary.
Repository read only; no model or network calls.
