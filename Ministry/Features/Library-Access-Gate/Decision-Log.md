# Library Access Gate — Decision Log

Append-only. Entries numbered; a merged entry's number never changes.

## 1. Workstream opened (2026-09-15)

Mark: "launch a design and build thread for this, using our sonnet,
opus, fable cycle. sonnet to manage, fable to research and design and
opus to critical/advisorial review. it should focus on design, not
evaluate the source content. it will be a massive library and we built
a library system that should be state of the art, but i want access
and worlds confined to only the source material that comes from their
tradition."

Scope: design and build the confinement mechanism (which world may
draw from which source material, enforced, at scale). Out of scope:
judging which works belong to which tradition (`cic/corpus-map/`'s
job, unchanged). Model routing per `README.md`. D0/D1 (Fable
immersion + divergent directions) kicked off same day.

## 2. D1/D2 complete (2026-09-15)

Fable's divergent directions (`Sandbox/D1-Directions.md`) and Opus's
adversarial review (`Sandbox/D2-Struggle.md`) are both filed. Opus's
review independently re-verified D1's claims against the real code,
corrected several, and surfaced nine open questions gating D3
convergence — walking them one at a time with Mark below.

## 3. Q1 (scope) converged: C — structure yes, judgment no (2026-09-15)

Mark's ruling: this workstream may specify new corpus-map structure
(new fields, a new role category, a `locus_ids` field) as a named
dependency, but never makes the classification judgment that fills
those fields in — that stays `cic/corpus-map/`'s own separate,
tracked work order. Keeps content evaluation out of scope per the
original charter while making the blocking-vs-reporting fork (Q3)
actually resolvable instead of structurally impossible.

## 4. Q2 (voicing) converged: mutual-awareness rule, not container role (2026-09-15)

Mark's ruling, refining beyond the three drafted options: voicing
permission turns on documented **historical mutual awareness between
the two traditions**, not on the citing work's role tag alone. If two
traditions were actually in dialogue or controversy with each other
(Donatists and Optatus's Catholics genuinely argued, on the record),
each side's Representative may voice that documented exchange, because
the fact of the argument is real history belonging to its own world's
record. If a source merely happens to preserve material from a
tradition that never knew of or engaged with it (one-way transmission,
e.g. Eusebius preserving Dionysius with no live argument), that
connection is not real history for the citing world and stays
unvoiced.

Structural consequence, confirmed in scope under Q1: this needs a
relationship classification between tradition **pairs**
(argument/mutual-awareness vs. one-way transmission vs. no
relationship), not just a role tag on the individual work — and it
lives in `cic/corpus-map/` itself, per Q1's "structure yes, judgment
no" split (this workstream can spec the pair-relationship field;
corpus-map's own thread rules on which pairs qualify).

## 5. Q3 (enforcement) converged: staged rollout by waiver (2026-09-15)

Mark's ruling: build the real gate now, in scope for this workstream.
New worlds must pass it clean before admission going forward. Existing
worlds with findings today (`don`'s 52, `syr`'s 1) are grandfathered
as tracked `ACCEPTED_OPEN` waivers with a deadline — the same
gap-tracking discipline CLAUDE.md already requires elsewhere in the
project. Makes the mechanism actually enforced for everything new
immediately, without stalling the whole workstream on an all-fleet
cleanup first.

## 6. Q4 (unvendored sources) converged: etic-only (2026-09-15)

Mark's ruling: a source record citing unvendored material (modern
scholarship, unvendored primaries, editorial apparatus) is only
permitted on an etic (analytical-layer) record — never on an emic
record, where it would ground the Representative's own in-character
voice in something unverifiable. Extends the emic/etic distinction
root `CLAUDE.md` already draws for hedge language to source records
generally: a Representative's own voice must stay grounded in
verified, vendored material; unverifiable scholarship belongs to the
analytical layer, not the tradition's own mouth. A schema/field change
(`register:` or equivalent) is a dependency, tracked under Q1's
structure-yes/judgment-no split.

## 7. Q5 (absence records) converged: dedicated kind + build-time-only read (2026-09-15)

Mark's ruling: a record documenting what an edition does *not* contain
(e.g. `gallic.source.augustine-letters-221-226-absence`) gets its own
explicit `kind: absence` schema tag. The compiler — never the runtime
Representative — gets a narrow, logged exception to read off-shelf
material specifically to verify such a claim before the record ships;
the Representative itself never receives or can voice that off-shelf
content. Mirrors the class of exception build-time quote verification
already has (`engine/m1/gates.py`), rather than inventing a new kind
of runtime access.

## 8. Q6 (corpus-map churn) converged: automate repin + split the file (2026-09-15)

Mark's ruling: CI automatically re-runs the staleness sweep on any
corpus-map edit and opens the repin PR(s) for every affected world —
no human has to notice or chase it. `records/worlds.yaml` splits into
one file per world (`records/worlds/<code>.yaml`) specifically to
retire the cross-branch merge-conflict risk already flagged as Gate A
finding B1 (`CiC_Repo_Structure_Tracking.md`), ahead of it getting
worse as the fleet scales from ~10 toward 100 worlds.

## 9. Q7 (pre-D3 measurements) converged: run both now (2026-09-15)

Mark's ruling: run both of Opus's flagged measurements before
finishing convergence — Direction E's complement sweep (file grain,
current nine worlds, evidence of live I5 leakage) and Direction B's
verbatim window-match against the 225 emic quotes (B's real
viability). Both cheap, both bear directly on the remaining
decisions. To be commissioned once the open-questions pass completes.

## 10. Q8 (the fixture) converged: in scope here (2026-09-15)

Mark's ruling: building the confinement fixture (`fix` gets a census
id, a bucket, a vendored fixture text, rewritten source records;
`corpus_map.validate()` tolerates a synthetic bucket) is in scope for
this workstream. It's test infrastructure the gate itself needs to be
testable at all — the same role `fix` already plays for M1/M2/M3 — not
a content-judgment call, so it fits inside Q1's "structure yes" scope
rather than needing its own work order.

## 11. Q9 (correct the record) converged: append a dated correction now (2026-09-15)

Mark's ruling: append a dated correction to
`Ministry/Operations/Standing/CiC_Repo_Structure_Tracking.md` itself,
in the same append-only style that doc already uses for every other
update — not a rewrite of its history. Opus's independent
re-confirmation clears CLAUDE.md's re-confirmation bar for a blocking
finding; done immediately after this entry.

## 12. All nine open questions converged (2026-09-15)

Q1–Q9 answered in full (entries 3–11 above). Next: correct
`CiC_Repo_Structure_Tracking.md` per Q9, commission the two Q7
measurements (E's complement sweep, B's verbatim window-match), then
write D3 (the converged design), incorporating every ruling above,
for Mark's freeze.
