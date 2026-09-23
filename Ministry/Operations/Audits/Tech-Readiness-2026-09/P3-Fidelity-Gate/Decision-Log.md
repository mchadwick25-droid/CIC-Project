# Decision Log — Tech-Readiness Package 3 (Fidelity Gate)

Append-only, per `CLAUDE.md`. One entry per ruling this package acted on
while building the verbatim quote gate (`engine/m1/quote_verbatim.py`).
Entries here record what was ruled and where it landed; the fuller
reasoning for each PR lives in that PR's own body.

---

**Entry 1 — 2026-09-22 (Ruling 1, normalization policy).** Mark ruled the
gate editorial-tolerant with a published, closed list: a quote passes only
when every difference between its `text` and the vendored source is one of
a named set of allowed classes (whitespace, case, punctuation, ellipsis,
bracket) — no fuzzy score, no threshold. Built on `p3-fidelity-gate`,
report-only, not registered in `gates.GATES`. PR #400.

**Entry 2 — 2026-09-22 (Ruling 2, verse_number / nested-mark).** A sixth
class, `verse_number` (an inline Arabic verse/section number at a sentence
boundary), ruled allowed. A seventh candidate — a nested quotation mark
rendered as a different mark — ruled NOT allowed; stays a failure, fixed in
the record. PR #401 (the class), PR #403 (hand-characterizing the remaining
73 failures into omission / edition-mismatch / nested-mark / other, no
record edits).

**Entry 3 — 2026-09-22 (Ruling 3, hyphenation and bracket-ellipsis).** Two
of the three patterns PR #403's triage flagged folded into the existing
whitespace/ellipsis classes rather than becoming new classes: source-side
line-wrap hyphenation ("eter-\nnity") and `[...]`/`[…]` as a single
bracket-wrapped ellipsis marker, not a bracketed insertion. The third
(stray backslash in a record's own `text` field — a YAML folded-scalar
authoring bug) held for the record-fix session. PR #405.

**Entry 4 — 2026-09-22 (R21/R24, record-fix policy).** A separate session
("Quote record repair after the verbatim gate") ran the record-fix pass
PR #405's triage list called for. Per that PR's own body: R21 defined
verbatim as every difference falling in the six allowed classes; R24 ruled
a quote that silently dropped words gets the words restored, or a true
ellipsis where the elision doesn't change meaning and the record is built
on the quoted formula as-is — every fix states which it did and why. 52 of
70 flagged records fixed across 11 worlds; 4 records escalated (genuine OCR
corruption or corrupted scans with no clean alternate edition, and one
paraphrase carried as verbatim in error) with `verification_state` lowered
rather than guessed at. Fleet 184/257 → 239/257 verified. PR #413.

**Entry 5 — 2026-09-23 (apparatus normalization).** Four closed, evidenced
source-edition apparatus forms (soft hyphen U+00AD, tilde-digit `~1~`,
pipe-page `|146`, bracketed locator `[964D]`/`[p. NNN]`/
`[Author. p. NNN, l. N.]`) folded into a new `apparatus` class, each traced
to its real break point in the vendored file before a pattern was written.
A bracket-locator pattern first written as 1-4 digits collided with
`desert.quote.the-noonday-demon`'s own `[1]`-`[6]` section numbering (real
quoted content, already tolerated via the existing `bracket` class) —
caught by the full fleet re-sweep, narrowed to 3-4 digits. A bare,
unwrapped footnote digit or symbol with no marker of its own (5 records)
was explicitly left unresolved rather than guessed at — see Rulings-
Pending.md. Fleet 239/257 → 246/257 verified. PR #422 (merged).

**Entry 6 — 2026-09-23 (R28, note-embedded quotation — superseded same
day, see Entry 7).** A first attempt at this problem (opened as PR #423,
never merged) had Mark rule: the gate keeps stripping `<note>` blocks by
default, but a quote record may opt in by naming the specific note `id` it
quotes from (`source_note_id`); the gate then verifies against that note's
own text instead of discarding it as editorial commentary. That PR's own
Rulings-Pending entry for R28 is struck through by Entry 7 below — the
mechanism it proposed was never merged, and no `source_note_id` field
exists on any record.

**Entry 7 — 2026-09-23 (R33, note-body fallback — gate-level, no per-record
field).** In the same session, reviewing #423's approach directly with
Mark, he ruled instead, in his own words: *"we should be setting principles
we will have a 100 worlds and cant tell the representitive what to say for
every quote."* A per-record field naming which note to check does not scale
to a hundred-world fleet the way a gate-level principle does. R33 replaces
R28's mechanism: the gate verifies against the running text first, exactly
as before; if that fails, it now tries every `<note>` body in the same
vendored source file in turn, same tolerances as everywhere else, and stops
at the first that verifies. `VerifyResult.verified_in` records which path
actually verified a quote (`"running_text"` or `"note"`, with `note_id` set
for the latter) so a note-verified record is always reported as what it is
in the fleet report's own `note_verified` list, never folded silently into
an ordinary running-text pass. `pahc.quote.two-female-slaves-who-were-
called-deaconesses` (Pliny's letter to Trajan, quoted in full inside a
translator's endnote in the vendored Eusebius volume, not in Eusebius's own
running text) is the one record this ruling actually restores —
`verification_state` back to `verified-direct`, no field added to the
record itself. Fleet 246/257 → 247/257 verified (1 of the 247 verified via
a note). PR opened same session; #423 closed with a comment pointing here,
its mechanism superseded.

R33 is a principle for this gate going forward, not a one-record fix: any
future quote embedded only in a source's own note verifies the same way,
automatically, with no record ever naming which note.

**Entry 8 — 2026-09-23 (R34 and R35, recorded for the program, not yet
acted on by code in this PR).** Two further rulings from the same session,
governing the rest of this gate's build-out (items 2-4 of the registration
brief), recorded here in Mark's own words so they aren't left only in a
conversation thread:

- **R34 (modern_rendering is translation, not summation):** *"the
  representitive translates it into modern english, this is translation,
  not summation."* The modern rendering must be a full translation of the
  original: every clause present, nothing added, nothing compressed. This
  governs item 4 (the rendering-fidelity grading gate) — not yet built;
  recorded here so the standard it will grade against is on record before
  that gate exists.
- **R35 (build quality, not fix on fix):** *"this is about the build
  quality, not fix on fix."* Both quote gates (verbatim, and rendering-
  fidelity once built) become birth conditions in the build process — run
  as each quote record is authored, not as a repair pass after the fact.
  No repair pass like PR #413's is meant to happen again for this gate.
  This governs item 3's registration work (`gates.GATES` and the build-
  process document) and is quoted there directly rather than paraphrased.

**Open, per Rulings-Pending.md:** the bare-digit/symbol apparatus question
(Entry 5) is with Mark, now scoped to item 2 of the registration brief
(edition-level apparatus); gate registration in `gates.GATES` waits for
that ruling, since registering now would go red on the six records it
affects.
