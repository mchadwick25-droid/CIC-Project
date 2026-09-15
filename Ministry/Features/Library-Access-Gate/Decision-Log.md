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

## 13. Q7 measurements complete (2026-09-15)

- **B (verbatim window-match, `Sandbox/Q7-measurement-B-verbatim-match.md`)**:
  221 real emic verbatim quotes, 98.2% match somewhere on their own
  world's shelf. Donatism is the sharp outlier — 60% of its 5 verbatim
  quotes land off-role or no-match, independently reproducing D2's
  separately-derived "61%" role-vocabulary finding by a completely
  different method (byte matching vs. pointer resolution) — a real
  cross-check that the Q2 role problem is genuine. Direction B's core
  byte-match bet holds up well; the same run also surfaces a handful
  of genuinely off-shelf citations and one bad OCR scan.
- **I5 (complement sweep, `Sandbox/Q7-measurement-I5-complement-sweep.md`)**:
  no live evidence I5 (cross-tradition leakage) is an active problem in
  the current 9-world fleet. The sharp verbatim check came back clean
  everywhere it touched; coverage is partial (621 of 4,524 sentences
  got the strong check). The ratio-based half of the same instrument
  turned out to be near-inert at whole-bucket-union file grain (~0.98
  against both a world's own shelf and its complement) — not usable as
  evidence on its own, a finding worth carrying into D3 if E's approach
  comes up again.

Next: write D3, the converged design, incorporating all nine rulings
and both measurements, for Mark's freeze.

## 14. D3 drafted and independently checked (2026-09-15)

Fable's D3 (`Sandbox/D3-Converged-Design.md`, "the Compiled Shelf,"
`engine/m9/`) synthesizes all nine rulings and both Q7 measurements
into one mechanism, not a menu. Opus's freeze check
(`Sandbox/D3-Freeze-Check.md`) independently re-verified D3's
load-bearing code/path claims and numbers against the real repo
(mostly correct; several count errors found and itemized as RF-1
through RF-16) and filed four rulings (R-1 through R-4) still needed
from Mark before build can start. Verdict: "ready to freeze with 16
required fixes and 4 rulings."

## 15. R-1/R-2/R-3 (voicing grain) converged: row-level tag required (2026-09-15)

Mark's ruling: a documented mutual-awareness pair between two
traditions makes voicing *possible in principle*, but each individual
work still needs its own explicit corpus-map tag confirming it was
actually part of the documented exchange — not just produced by an
aware party. Rejects D3's built default (whole-partner-work grain,
where any mutual-awareness pair silently voices everything either side
ever produced). Resolves both flagged cases: Cyprian stays
citable-not-voiceable for `don` (he wasn't party to the live Donatist
controversy itself, so gets no automatic tag); `alx`'s Dionysius-via-
Eusebius stays unvoiced unless corpus-map explicitly tags that
transmission as a real documented exchange, not mere chronological
adjacency. Closest to Mark's original Q2 wording ("the fact of the
argument is real history").

## 16. R-4 (waiver scope) converged: stage the closure (2026-09-15)

Mark's ruling: closed grandfathering stays the end state for every
check, but `voicing-pair` specifically — the one check directly
blocked on corpus-map's own CM-3 dependency — stays report-only for
new worlds until CM-3 actually lands, rather than making the tenth
world's admission hostage to a thread this workstream doesn't control.
Every other check enforces fully on new worlds from day one; only the
one check with a real external dependency gets a temporary,
auto-closing carve-out.

## 17. All four freeze-check rulings converged (2026-09-15)

R-1/R-2/R-3 and R-4 both ruled (entries 15, 16). Next: apply RF-1
through RF-16 to `D3-Converged-Design.md` incorporating these
rulings — a targeted revision, not a re-review, per this project's own
usage discipline — then bring the revised design back for Mark's
actual freeze word.

## 18. D3 revised: RF-1 through RF-16 applied, R-1–R-4 incorporated (2026-09-15)

All 16 required fixes and all four rulings are now in
`Sandbox/D3-Converged-Design.md`, applied directly (targeted revision,
Sonnet, per this project's own D3 pattern — fixes don't reopen
convergence). Headline changes: `voicing-pair` (§1.4) now requires a
row-level `documented_exchange` tag (new dependency **CM-8**, §3) on
top of the pair relationship, implementing R-1/R-2/R-3 — Cyprian stays
citable-not-voiceable for `don`, `alx`'s Dionysius-via-Eusebius stays
unvoiced absent a specific corpus-map tag. §4.2 gains R-4's staged
closure: every check stays fully un-waivable for new worlds except
`voicing-pair`, which is report-only for new worlds until corpus-map
lands its first real pair, closing automatically with no code change.
Numeric corrections: `emic-vendored-only` 152 → 166 (RF-2);
`voicing-pair`'s 296 restated as a file-grain floor, true range
296–407 (RF-3); `gallic`→npnf203 52 → 56 (RF-4); `locus-within-work`
(I2) restated as a shelf-grain claim, not row-grain (RF-5); increment
7/8's dependency statement corrected (RF-6); the unstated new-world
consequence (RF-7) is now stated, then resolved by R-4. RF-16 (the Q4
tightening) stays flagged for a one-line confirmation at freeze rather
than silently inherited. Ready for Mark's actual freeze word.
