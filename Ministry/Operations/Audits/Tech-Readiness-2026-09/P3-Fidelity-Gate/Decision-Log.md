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

**Entry 9 — 2026-09-23 (item 2, edition-level apparatus).** Resolves
Rulings-Pending's Pending 1 (the bare-digit/symbol residue Entry 5 and #422
left open) for five of its six records. `cic/texts/REGISTRY.yaml` gains an
optional `apparatus` field per edition entry — a closed list of named,
evidenced marker patterns, applied by `engine/m1/quote_verbatim.py`
(`strip_edition_apparatus`) to every quote citing that edition and no
other. No field on any quote record, per R33. Populated for the three
editions the residue records cite:

- `palladius_lausiac-history_clarke1918.txt` — three patterns, each
  anchored to its own real surrounding words rather than a bare digit
  class, because this same edition also quotes real digit quantities as
  content elsewhere ("some 300 monks", "some 400 monks" - confirmed by
  reading the file, not assumed). Clears `desert.quote.good-good-i-dont-
  mind` ("163", "164") and `hal.quote.hindered-by-jerome` ("276").
- `ammianus-marcellinus_roman-history_yonge1862.txt` — one anchored
  pattern, same reasoning (this file spells its own real casualty count as
  words - "one hundred and thirty-seven dead bodies" - never as digits).
  Clears `ijc.quote.ammianus-sicininus-massacre`.
- `basil_ascetic-works-longer-shorter-rules_clarke1925.txt` — five
  patterns: one anchored digit, two bare footnote-glyph symbols (®, », safe
  as a general strip within this one file - never real prose content in
  any edition), one anchored stray Migne column-continuation letter, and
  one general per-edition pattern for this edition's own unbracketed
  column-locator convention (`\d{3,4}[A-Z]`, the same shape the fleet-wide
  `bracket-locator` class strips elsewhere, but printed here without
  brackets - confirmed recurring throughout the file, not a one-off
  guess). Clears `cappadocian.quote.basil-on-work-and-prayer` (all four
  non-digit patterns) in full; clears the digit marker in
  `cappadocian.quote.basil-on-common-life` but does NOT clear that record
  overall — see below.

Separately, this PR fixed a real, fleet-wide (not edition-specific) bug the
sixth residue record exposed: `_BRACKET_LOCATOR_RE` left a stray space
before trailing punctuation when a bracket locator sat between a word and a
comma/period with no space of its own (`cappadocian.quote.gregory-nyssa-on-
becoming-god`'s own npnf205 source: `"Him Who is [2002] , nor"` → `"is ,
nor"` instead of `"is, nor"`). Narrowed to that exact shape (a lookahead
confirms punctuation follows before the preceding space is folded in) -
not a blanket space-before-punctuation rule, which regressed three other
records (`desert.quote.antony-dying-daily`'s own intentional `"daily ."`,
among others) before being caught by the full fleet re-sweep and narrowed.
Clears `cappadocian.quote.gregory-nyssa-on-becoming-god`.

**Honest result vs. the expected count:** the registration brief expected
253/257 (all six residue records fixed). The real fleet run is **251/257**
(246 baseline → 251) - `cappadocian.quote.basil-on-common-life` clears its
own footnote-digit marker but remains unverified, because the same span
has separate, newly-discovered defects (a genuine OCR word misread, "Tor"
for "For", plus a stray inserted quote mark and two more bare footnote
glyphs) that no apparatus mechanism should paper over. Recorded as
Rulings-Pending's own Pending 2 rather than stretched to hit the expected
number.

**Entry 10 — 2026-09-23 (R33 review round 1, FAIL, and the fix).** The
reviewer thread reviewed Entry 9's own PR against R33 directly and failed
it: five of its entries — `endnote-num-after-from-work`,
`endnote-num-after-her-lover`, `endnote-num-after-paula-comma`,
`endnote-num-after-christian-church`, `endnote-num-after-in-common`, and
`stray-column-letter-after-work-with` — were each anchored to one quote's
own exact surrounding words (a pattern requiring the literal text "from
work" or "her lover" to appear), a per-quote instruction dressed as an
edition entry, exactly what R33 forbids: *"we should be setting principles
we will have a 100 worlds and cant tell the representitive what to say for
every quote."* What passed: the registry field and its schema comment, the
two Basil glyph strips (®, »), the unbracketed column locator, the
bracket-locator punctuation fix, the honest 251 count, and Pending 2
recorded rather than papered over.

Fixed same round:

- **Palladius** — the three anchored digit patterns replaced by one
  `kind: endnote-sequence` entry: walk the edition's own real numbered
  endnotes list (found via the file's own editorial marker, "[Footnotes
  renumbered and moved to the end]") and strip a bare digit only when it
  is genuinely the next number that list expects. Tested and correct
  against clean synthetic data — but real-world testing against the
  actual vendored file found its own sequence too interleaved with page
  numbers and bracketed chapter numbers to track safely end to end (the
  walk stalls well short of the 163rd entry). Rather than ship an unsafe
  mechanism to hit a number, the entry was dropped: `desert.quote.good-
  good-i-dont-mind` and `hal.quote.hindered-by-jerome` are
  `verified-via-authority` instead, each with a divergence_note naming
  the specific digits confirmed by direct inspection. The mechanism
  itself stays in the codebase (`strip_endnote_sequence`), tested, for a
  future cleaner-scanned edition.
- **Ammianus** — the one anchored pattern replaced by a general "digit
  glued after a sentence period" pattern, evidenced at 50+ real breaks
  throughout the file, not the one quote that first surfaced it.
- **Basil** — the anchored stray-letter pattern replaced by a general
  "lone column-continuation letter B-E" pattern, evidenced at 231 real
  breaks (excluding A and I, which are real English words that
  legitimately open a paragraph — 23 and 42 confirmed real cases
  respectively). The anchored digit entry (`in common 1 is more`) was
  dropped rather than generalized: Basil's own footnote numbering does
  not form one clean sequence the way Palladius's does, so no safe
  edition-wide rule was found — moot regardless, since **F3** resolves
  Pending 2 in the same round: `cappadocian.quote.basil-on-common-life`'s
  own compounding defects (the "Tor"/"For" OCR misread chief among them)
  are the same case as the already-ruled OCR-damaged don/ijc records, so
  the record is `verified-via-authority` with the corruption named in its
  own divergence_note — closed as resolved by that existing ruling, no
  new ruling needed.

Fleet: 246 baseline → **249/257**. Every remaining failure's own
`verification_state` is already below `verified-direct`
(`verified-via-authority` or `unverified`) — exactly the residue item 3's
own registration brief expects, once `#429` (merged) is rebased onto this
branch: `pahc.quote.two-female-slaves-who-were-called-deaconesses` will
drop out of this list too, leaving `desert.quote.good-good-i-dont-mind`,
`hal.quote.hindered-by-jerome`, `ijc.quote.ammianus-roman-luxury`,
`ijc.quote.compelled-to-come-in` (#426, in flight),
`cappadocian.quote.basil-on-common-life`, and the two `don.*` records.

**Resolved, per Rulings-Pending.md:** Pending 2 is closed by Entry 10's F3
above. Pending 1 stays closed (Entry 9). No entries remain open in
Rulings-Pending.md as of this entry. Gate registration in `gates.GATES`
(item 3) can proceed once `#429` lands on this branch and the rebased
fleet count is confirmed.
