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

**Entry 11 — 2026-09-23 (item 3, PR #435 — a claimed `check_paths.py`
failure that does not reproduce).** The reviewer thread reported that PR
#435 (head `0e5a4119`) fails "Cited paths resolve; retired paths absent"
because `worlds/ijc/Open_Gaps_Tracking.md` line 157 cites
`packages/ijc/2026-09-23T04-41-35Z` — the package path item 3a's fleet
repin orphaned when `ijc` moved to `packages/ijc/2026-09-23T08-14-01Z` —
with a specific claimed output ("1 new unresolved path citation(s); 770
total; 769 accepted in baseline", exit 1), and asked for line 157 to be
re-pointed at `records/worlds/ijc.yaml` instead.

Per this project's own verify-before-acting discipline, that claim was
checked directly rather than acted on:

- Running the exact command specified
  (`python tools/check_paths.py --baseline tools/check_paths_baseline.txt`)
  on that exact commit, on a clean tree, twice, both times returned
  **"0 new unresolved path citation(s); 769 total; 769 accepted in
  baseline; 0 retired path(s) present"** — exit 0. The claimed output does
  not reproduce.
- Reading `tools/check_paths.py`'s own `resolves()` explains why: it
  checks `target.exists()` on the literal token — directory existence, not
  a specific file within it. `packages/ijc/2026-09-23T04-41-35Z` (the
  directory) still exists on disk; only its `manifest.json` was removed by
  the repin, per the "retire manifest.json only, keep the directory"
  convention used throughout this build. The citation resolves regardless
  of the stale manifest. `tools/retired_paths.txt` does not list this path
  either, so `retired_present()` does not flag it.
- The PR's own actual CI run for that check
  (`mchadwick25-droid/CIC-Project` run `35836710589`, job
  `107101801714`) shows `conclusion: failure` but a ~2-second duration and
  no downloadable logs (404) — every other job on the same run shows the
  identical zero-duration `skipped` pattern. This is the same signature
  previously diagnosed on PR #430 as a GitHub Actions account-payment
  failure (jobs never start; no logs), not a real script failure — so this
  run could not have produced the specific stdout quoted in the claim
  either.

**No code or content change made in response to this claim.** The
suggested edit (citing `records/worlds/ijc.yaml` instead of a timestamped
package path) may be reasonable future practice on its own terms, but
applying it now, as if confirming an unverified and seemingly incorrect
CI-failure claim, would be exactly the kind of unverified action this
project's fidelity discipline exists to prevent — and line 157 is a
historical narrative entry (it names the specific path #431's own re-pin
landed on at the time, the same way this log cites superseded PR numbers
and branch names elsewhere), not a live "current state" pointer that
`check_paths.py` was ever meant to hold current. Reported back to the
reviewer thread via PR #435 for reconciliation before any edit is made.

**Entry 12 — 2026-09-23 (reconciliation: Entry 11's claim reproduces on a
clean worktree — fix applied).** The reviewer thread's answer identified
the actual gap in Entry 11's own verification: `packages/*/*/**` is
gitignored except `manifest.json` (`.gitignore` lines 44-45), so this
session's own working tree still held `packages/ijc/2026-09-23T04-41-35Z/`
as untracked build output left over from item 3a's repin — the directory
that pin's own commit removed from git (`git ls-tree` on that commit shows
it empty) but which the "retire manifest.json only, keep the directory"
convention never deleted from disk. `resolves()` saw that untracked
directory and returned true. A clean checkout has no such directory,
because git does not track empty ones. Reproduced directly: `git worktree
add /tmp/clean ffb1d791` (no such directory present) then
`python tools/check_paths.py --baseline tools/check_paths_baseline.txt`
there returned exactly the claimed **"1 new unresolved path citation(s);
770 total; 769 accepted in baseline; 0 retired path(s) present"**, exit 1,
naming `worlds/ijc/Open_Gaps_Tracking.md: packages/ijc/2026-09-23T04-41-35Z`.
Entry 11 stands as written — a real verification step whose local
environment, not its method, produced the wrong answer — rather than
struck through.

Fix applied: entry 19 of `worlds/ijc/Open_Gaps_Tracking.md` now says the
current pin is recorded in `records/worlds/ijc.yaml` rather than citing
the timestamped package directory the #431 re-pin happened to land on;
the sentence's own meaning (that #431 re-pinned the package rather than
force-pushing #426's archived branch) is unchanged. Nothing else in that
file touched. No baseline or ignore-rule change, per instruction. Going
forward, `check_paths.py` runs against a clean `git worktree`, not the
working tree, before any push that repins a package — a working tree with
leftover untracked build output is not a substitute for what CI actually
sees.

**Entry 13 — 2026-09-23 (R40, desert half A — 23 of 46 missing quote
records authored).** Continues R40 world by world after alx (PR #442)
and ijc (PR #453): desert, split into two PRs by record range on the
reviewer's own suggestion to keep each PR reviewable, half A here and
half B in parallel on a separate branch/PR. desert had 46 of 60 quote
records missing `modern_rendering` (14 already had it); this PR authors
half A's 23.

Each rendering was written directly from the record's own `text` field
(never from memory of the source), reading `modern_lens_note` first so
flagged technical/theological vocabulary (apatheia, praktike, Essence,
Μονάς/῾Ενάς, diakrisis/discretion, compunction/penthos, and others) was
kept rather than softened away. Every rendering was checked against
`engine/m1/fk.py`'s `fk_grade()` locally before any live call, then run
through `engine/m1/rendering_fidelity.py`'s live Haiku 4.5 grader per
the birth-condition process, revised until the verdict read
"translation" on two consecutive runs of the same final text. **No
honest exceptions this pass** — all 23 cleared two consecutive
"translation" verdicts inside the normal revision process; five records
needed real revision (2-3 rounds) against grader findings of dropped or
added clauses, and one round on an already-revised record showed the
grader giving internally self-contradictory reasoning (calling a
rendering "mixed" while its own final sentence concluded the rendering
was faithful) before resolving to "translation" on the very next
consecutive run, so no exception was invoked.

One fidelity-mechanics catch along the way, worth recording: an early
draft of `desert.quote.god-is-not-a-body`'s rendering retyped its
source's polytonic Greek (Μονάς, ῾Ενάς) by hand and silently landed on
different Unicode codepoints for the accented alpha and the rough-
breathing mark than the source actually uses (monotonic vs. polytonic
forms, invisible to the eye, exactly the class of defect
`desert.quote.god-is-not-a-body`'s own record body already names for
its `text` field). Caught before commit by comparing codepoints
directly; the final rendering's Greek was extracted programmatically
from the record's own `text` field rather than retyped, to guarantee an
exact match.

`engine/m1/gates.py`'s `gate_readability` (FK ceiling 10): 0 findings
across the 23 (range 1.6-8.7). Full `run_all()` on desert: 0 findings
referencing any of the 23 (one pre-existing, unrelated `reciprocity`
finding on `desert.limit.communal-wrong-unrepaired` /
`desert.story.moses-leaking-jug` remains untouched by this work).
`pytest engine/m1/tests/`: 134 passed, no regressions. No field other
than `modern_rendering` touched on any record; no per-record notes
added, per R33.

Package re-pinned twice: once after authoring (records-commit
`02e0a1dc6431b5d123dbf8d64037776cadb98b4d`), then again after rebasing
onto current main immediately before push (records-commit
`697281f1197a0bd772e48e0183372c6076789b39`, the real post-rebase HEAD).
`staleness_sweep()`: clean across all 12 worlds after the final re-pin.
Old manifests retired (directories kept, per convention).

**Entry 14 — 2026-09-23 (R40, desert half B — 23 of 46 missing quote
records authored).** `alx` (PR #442) and `ijc` (PR #453) are done and
merged. `desert` has 46 of 60 quote records missing `modern_rendering`;
split into two PRs by record range, per the reviewer's own suggestion,
to keep each reviewable. This is half B, these 23 record IDs. Half A
(the other 23, PR #458) merged first, at `13796b85`; this entry's own
rebase and re-pin happen against that merged main, so desert carries
all 46 renderings (of 60 total quote records) once this entry's PR
merges too.

Each translation was written directly from the record's own `text`
field, reading its `modern_lens_note` first so vocabulary it flags as
significant (apatheia, nous, logismoi/"generic thoughts", acedia,
theoria, koinonia, etc.) was kept rather than softened away, then run
through `engine/m1/rendering_fidelity.py`'s live Haiku 4.5 grader per
the birth-condition process: revised until the verdict read
"translation" on two consecutive runs of the same final text.

**One honest exception:** `desert.quote.womens-house-across-the-river`.
After 6 genuine revision rounds, the rendering is defensible
clause-by-clause against its source `text`, but the live grader kept
flipping between "translation" and "summary" on materially unchanged
text, and by the final rounds its own reasoning was factually false
about the rendering it was grading — asserting an omission of "And when
any one of these went in to her rest" when the graded text literally
read "When one of these women went to her rest," and asserting a drop
of "the brethren received her on a raft" when the graded text read "the
brothers received her on a raft." Named here rather than presented as a
clean pass, per the alx/ijc precedent (2 such exceptions each).

**Gate results.** `gate_readability` (FK grade ceiling 10) on desert:
0 findings across all 23 of this PR's renderings — several first
drafts needed splitting into shorter sentences to clear it, each split
kept its own subject and verb per the process doc's fragment rule, and
several splits were themselves flagged by the fidelity grader as
content changes and had to be re-balanced (most visibly on
`desert.quote.the-kingdom-is-apatheia` and
`desert.quote.the-noonday-demon`). Full `run_all()` on desert, run
after the rebase onto half A's merged main (so all 46 newly-authored
renderings are present together): 1 finding, the same pre-existing
`reciprocity` gap between `desert.limit.communal-wrong-unrepaired` and
`desert.story.moses-leaking-jug` — neither record touched by either
half of this work. `desert` now has 60/60 quote records with
`modern_rendering`. `pytest engine/m1/tests/`: 134 passed, no
regressions.

**Package pin.** Rebuilt and re-pinned twice: once against
`fbc0fdd444bb2cba7e95ceb3bb9ed7332ac8981c` (this PR's own
modern_rendering commit, before half A had merged), then again after
rebasing onto main post-half-A-merge, against
`db19e5ac6147f549a271b1dcff78c36736beb66a` (the real post-rebase HEAD,
carrying both halves' 46 renderings) — the first pin would have shipped
a package missing half A's 23 renderings, so it is superseded rather
than reused. Final: old `packages/desert/2026-09-23T18-50-21Z`
(half A's own pin, `sha256:e597fe552b2b14604309f1ad010cd9c30625ae1272c171af4e32c32bd05440a4`)
→ new `packages/desert/2026-09-23T19-33-23Z`
(`sha256:a43b6eb055028868314ab3cdd5d7e5b64d23fb690f8042693e4e5a15b55b3977`).
`staleness_sweep()`: clean across all 12 worlds. Old manifests retired
(directories kept, per convention).
`check_paths.py --baseline tools/check_paths_baseline.txt` on a clean
`git worktree` of this branch's head: 0 new unresolved path
citation(s); 769 total; 769 accepted in baseline; 0 retired path(s)
present.

**Entry 15 — 2026-09-23 (R40, hal — 19 of 32 missing quote records
authored).** desert (PRs #458/#459) is done and merged, 60/60. Next in
the reviewer's stated order (hal, pahc, syr, fix): `hal` had 19 of 32
quote records missing `modern_rendering`. One PR, one world, per the
reviewer's revised sequencing note (author worlds one at a time, no
parallel subagents, to stay inside the account's remaining weekly
usage window).

Each rendering was written directly from the record's own `text`
field, split into short sentences where needed for readability, each
resulting sentence keeping its own subject and verb and one whole
thought of the original, per the process doc's fragment rule. Run
through `engine/m1/rendering_fidelity.py`'s live Haiku 4.5 grader:
4 of the 19 needed real revision against genuine findings on the
first pass (`helmeted-preface`, `i-gather-the-rose-from-the-thorns`,
`no-one-preferred-to-the-seventy`, `oea-tumult` — a dropped purpose
clause, an invented "only", an active-voice rewrite of a passive
attribution clause, and an invented "grew so great" respectively);
each was revised and reconfirmed individually. Two records
(`helmeted-preface`, `they-have-left-untold-the-name`) then showed the
grader flip verdicts on materially unchanged text across separate
full-world runs — the same inconsistency pattern already documented
for alx/ijc/desert — and each settled back to "translation" on
immediate re-runs of the identical text; no rewrite was needed for
either, and neither is an honest exception, since the text itself
never changed and the grader's own next call on it agreed. **No honest
exceptions this pass.** Two consecutive full-world runs (all 19
records, back to back) both came back 19/19 "translation".

**Gate results.** `gate_readability` (FK ceiling 10): 0 findings
across all 19 (range 4.2-9.6). Full `run_all()` (all M1 gates) on hal:
0 findings. `pytest engine/m1/tests/`: 134 passed, no regressions. No
field other than `modern_rendering` touched on any record; no
per-record notes added, per R33.

**Package pin.** Rebuilt and re-pinned once, against
`737c51a5f8b87d4f37e383487f269e0000190350` (this PR's own
modern_rendering commit; main had not moved since branching, so no
rebase was needed before this build). Old
`packages/hal/2026-09-23T08-13-52Z`
(`sha256:c2ccaf4ae9911d3d7999119d00853bcbe88d9919147141be2b5425000582c2e1`)
→ new `packages/hal/2026-09-23T20-32-17Z`
(`sha256:c98a2632cfadc230a540dfee33f56de83d679c7692d3f837f0f0b8674fa9783f`).
`staleness_sweep()`: clean across all 12 worlds. Old manifest retired
(directory kept, per convention).
`check_paths.py --baseline tools/check_paths_baseline.txt` on a clean
`git worktree` of this branch's head: 0 new unresolved path
citation(s); 769 total; 769 accepted in baseline; 0 retired path(s)
present.

**Entry 16 — 2026-09-23 (R40, pahc — 16 of 25 missing quote records
authored).** hal (PR #462) is done and merged. Next in the reviewer's
stated order (hal, pahc, syr, fix): `pahc` had 16 of 25 quote records
missing `modern_rendering`. One PR, one world, authored directly in
this session (no parallel background subagents), per the standing
budget-driven sequencing note.

Each rendering was written directly from the record's own `text`
field, split into short sentences where needed for readability, each
resulting sentence keeping its own subject and verb and one whole
thought of the original. Run through `engine/m1/rendering_fidelity.py`'s
live Haiku 4.5 grader: 2 of the 16 needed real revision against genuine
findings on the first pass. `moses-is-more-ancient` had dropped
"whatever" and "both" from its source clause on compression; revised to
keep both, then confirmed twice. `those-who-lived-reasonably-are-
christians` was flagged twice, consistently, for inventing the
connector phrases "this means"/"it means" to introduce its list of
names — a genuine finding, not grader noise (it repeated on unchanged
text), and this is the same construction `pahc.quote.justin-reasonable-
livers` also uses and which happened not to get flagged there; revised
to supply the list's own elided copula ("such people were") instead of
an interpretive connector, and confirmed twice. One record,
`put-away-doubting-from-you`, showed the grader flip to "summary" on
materially unchanged text on two separate occasions (out of 5 total
calls), each time citing a clause ("saying to yourself," the closing
"tender mercies" clause) that is plainly present in the graded
rendering — the same inconsistency pattern already documented for
alx/ijc/desert/hal; each time it returned to "translation" on immediate
re-runs of the identical text, so no rewrite was made and it is not an
honest exception. **No honest exceptions this pass.** A full-world run
of all 16 (after both real fixes) came back 16/16 "translation";
`put-away-doubting-from-you` was independently reconfirmed "translation"
3/3 on its own before that run.

**Gate results.** `gate_readability` (FK ceiling 10): 0 findings across
all 16 (range 4.5-9.5). Full `run_all()` (all M1 gates) on pahc: 2
findings, both the same pre-existing `reciprocity` gap between
`pahc.limit.enslaved-voices` / `pahc.limit.womens-own-words` and
`pahc.quote.two-female-slaves-who-were-called-deaconesses` (confirmed
present on main before this branch, untouched by this PR's 16 records).
`pytest engine/m1/tests/`: 134 passed, no regressions. No field other
than `modern_rendering` touched on any record; no per-record notes
added, per R33.

**Package pin.** Rebuilt and re-pinned once, against
`ed15e545d3f490eebef9693c19765a23965b93f5` (this PR's own
modern_rendering commit; main had not moved since branching, so no
rebase was needed before this build). Old
`packages/pahc/2026-09-23T08-14-12Z`
(`sha256:172013415ac56df97f88d122917329fc41c5b6d4a76909912f628eb7f0e1ff22`)
→ new `packages/pahc/2026-09-23T21-19-18Z`
(`sha256:fac1498358c0ef5d7577b6bb86263b1741a3d227b875f572b168109e53c2f8af`).
`staleness_sweep()`: clean across all 12 worlds. Old manifest retired
(directory kept, per convention).
`check_paths.py --baseline tools/check_paths_baseline.txt` on a clean
`git worktree` of this branch's head: 0 new unresolved path
citation(s); 769 total; 769 accepted in baseline; 0 retired path(s)
present.

**Entry 17 — 2026-09-23 (R40, syr — 16 of 34 missing quote records
authored).** pahc (PR #463) is done and merged. Next in the reviewer's
stated order (hal, pahc, syr, fix): `syr` had 16 of 34 quote records
missing `modern_rendering`. One PR, one world, authored directly in
this session (no parallel background subagents).

Each rendering was written directly from the record's own `text`
field, split into short sentences where needed for readability, each
resulting sentence keeping its own subject and verb and one whole
thought of the original — with one deliberate exception, below. Run
through `engine/m1/rendering_fidelity.py`'s live Haiku 4.5 grader: 3
of the 16 needed real revision. `palladius-hospitaller`'s "on your
behalf" had drifted to "on your own behalf," a genuine meaning shift
(self-interest implied by "own") caught and reverted. `sozomen-
melodies` had turned "not the precise copies by Harmonius" into
"not Harmonius's own songs," losing the "copies" distinction between
a precise copy and a looser one of the same melody; revised to "not
exact copies of Harmonius's versions." `nisibene-death-trembled` is
the one genuinely hard case in this project's R40 pass so far: its
source sentence ends "...and Satan because sinners rebelled against
him" — an elliptical construction missing Satan's own verb entirely
in the vendored translation. Six consecutive grading rounds, across
three different supplied verbs ("was terrified," "so did," "was
troubled"), were each rejected by the grader as inventing content not
present in the original — correctly, since no verb is actually there
to translate. The construction that finally cleared both gates
reproduces the source's own ellipsis verbatim ("...and Satan, because
sinners rebelled against him"), accepting the resulting fragment
rather than inventing a predicate the source never supplies. This is
recorded as a deliberate, narrow exception to the process doc's
no-fragment rule, not a precedent for splitting sentences carelessly:
the fragment already exists in the source's own English translation,
and preserving it was the only path that satisfied both fidelity and
readability. One record, `tatian-barbaric-writings`, flipped to
"summary" on materially unchanged text on two separate full-world
runs (out of 5 total calls), each time citing content that is plainly
present in the rendering, restructured into shorter sentences — the
same inconsistency pattern already documented for alx/ijc/desert/hal/
pahc; it returned to "translation" on immediate re-runs each time, so
no rewrite was made and it is not an honest exception. **No honest
exceptions this pass** (the nisibene fragment is a structural
accommodation, not an unresolved fidelity disagreement — it passed
the grader cleanly once rewritten). Two consecutive full-world runs
came back 16/16 "translation" (`tatian-barbaric-writings`
independently reconfirmed 3/3 "translation" on its own beforehand).

**Gate results.** `gate_readability` (FK ceiling 10): 0 findings
across all 16 (range 1.2-9.8). Full `run_all()` (all M1 gates) on
syr: 1 finding, the same pre-existing `voice-perspective` flag on
`syr.dw.death-judgment` (confirmed present on main before this
branch, untouched by this PR's 16 records). `pytest engine/m1/tests/`:
134 passed, no regressions. No field other than `modern_rendering`
touched on any record; no per-record notes added, per R33.

**Package pin.** Main moved during this PR (PR #449, an unrelated
table-parity fix, merged first) — rebased cleanly onto
`69391958` before building, then rebuilt and re-pinned once against
the real post-rebase HEAD `be18caf258364315ef4f98b54a949154165ee916`.
Old `packages/syr/2026-09-23T08-14-23Z`
(`sha256:97786ffefb3529c3a53913e7292c567a4ef46b019700654e944577802e7bfc71`)
→ new `packages/syr/2026-09-23T21-55-08Z`
(`sha256:047584444cedf6305fe3f191ad39d6dd99453d4fda08766c53e1fa46d6ebd902`).
`staleness_sweep()`: clean across all 12 worlds. Old manifest retired
(directory kept, per convention).
`check_paths.py --baseline tools/check_paths_baseline.txt` on a clean
`git worktree` of this branch's head: 0 new unresolved path
citation(s); 769 total; 769 accepted in baseline; 0 retired path(s)
present.

**Entry 18 — 2026-09-23 (R40, fix — 2 of 3 missing quote records
authored; R40 pass complete).** syr (PR #464) is done and merged.
Last world in the reviewer's stated order (hal, pahc, syr, fix): `fix`
(the sealed fixture world, `fixture-synthetic`, used to exercise the
engine's own defect-detection harness) had 2 of its 3 quote records
missing `modern_rendering`. One PR, its own pin, per the standing
process.

Both records were already short, plain modern English in their own
`text` field (`fix.quote.private-teaching`, license `do-not-voice`;
`fix.quote.witness-saying`, license `verbatim`), so each rendering is
a near-verbatim carry-over of the source rather than a restructuring —
nothing to split, nothing dense to simplify. Run through
`engine/m1/rendering_fidelity.py`'s live Haiku 4.5 grader: both read
"translation" cleanly on the first attempt and again on a second
consecutive run — no revision needed, no honest exceptions.

**Gate results.** `gate_readability` (FK ceiling 10): 0 findings
across both (2.3 and 6.1). Full `run_all()` (all M1 gates) on fix: 0
findings. `pytest engine/m1/tests/`: 134 passed, no regressions. No
field other than `modern_rendering` touched on either record; no
per-record notes added, per R33.

**Package pin.** Main had not moved since branching; rebuilt and
re-pinned once against this PR's own commit
`51c6f1e9fb05130e1942abd2b275c1ef82b3cc02`. Old
`packages/fix/2026-09-23T08-13-49Z`
(`sha256:ce011062ca438b5ddd51cef1d922124d1e67d78abd0ab80d00c0c6c3fb24840b`)
→ new `packages/fix/2026-09-23T22-10-53Z`
(`sha256:2c6f153eca0ad264fd186270769e987847a42226a653eecd0f79a17af7b76f53`).
`staleness_sweep()`: clean across all 12 worlds. Old manifest retired
(directory kept, per convention).
`check_paths.py --baseline tools/check_paths_baseline.txt` on a clean
`git worktree` of this branch's head: 0 new unresolved path
citation(s); 769 total; 769 accepted in baseline; 0 retired path(s)
present.

**This closes the R40 pass.** Combined with alx (PR #442), ijc (PR
#453), desert (PRs #458/#459), hal (PR #462), pahc (PR #463), and syr
(PR #464), every quote record across the fleet's 12 worlds now has a
`modern_rendering`. Next, per Mark's ruling (2026-09-23, 20:16Z): R43,
a fleet-wide `rendering_fidelity.py` sweep of the 45 pre-existing
renderings the grader had already marked summary or expansion before
this pass began, to produce a flagged-records-by-world list for the
reviewer to read before any re-authoring starts.

**Entry 19 — 2026-09-23 (one-record fix, syr — Mark's direct ruling on
the Nisibene ellipsis).** fix (PR #465) is done and merged; the R40
pass is closed fleet-wide. Before the R43 list, Mark ruled directly
(reviewer session, 22:27Z) on the judgment call Entry 17/PR #464
reported to him: `syr.quote.nisibene-death-trembled`'s rendering had
carried the source's own elliptical "and Satan because sinners
rebelled against him" over verbatim as a fragment, after six revision
rounds each rejected a supplied verb as invented. Mark's ruling: finish
the ellipsis into a whole sentence rather than keep the fragment,
supplying the verb the source's own parallel structure implies —
"Sin and Hell were terrified: Death trembled and the dead rebelled;
and Satan [did likewise] because sinners rebelled against him." This
supersedes PR #464's structural-accommodation approach for this one
record only; it is not a reversal of R34 generally, since Mark
explicitly modeled the completion himself rather than asking the
pipeline to keep guessing.

Rendering rewritten to: "Sin and Hell were terrified. Death trembled,
and the dead rebelled. And Satan did likewise, because sinners
rebelled against him." `gate_readability` (FK ceiling 10): clean (6.5).
Run through the live grader per Mark's own instruction to expect and
accept the rejection rather than loop: 2 consecutive runs, both
"expansion" (adding "did likewise" as content not in the source). This
is the exact strictness Mark's ruling anticipated and told this
pipeline not to argue with. **Documented honest exception, by Mark's
own direct instruction**, not a pipeline judgment call: the human
reading of the source's own parallel structure stands over the
grader's stricter-than-useful reading of ellipsis completion.

**Gate results.** Full `run_all()` (all M1 gates) on syr: 1 finding,
the same pre-existing `voice-perspective` flag on
`syr.dw.death-judgment`, untouched by this change. `pytest
engine/m1/tests/`: 134 passed, no regressions. Only this one record's
`modern_rendering` value changed; no other field touched.

**Package pin.** Main had not moved since branching; rebuilt and
re-pinned once against this PR's own commit
`d88d74c7915666823a9d080b4c01e66990da1b38`. Old
`packages/syr/2026-09-23T21-55-08Z`
(`sha256:047584444cedf6305fe3f191ad39d6dd99453d4fda08766c53e1fa46d6ebd902`)
→ new `packages/syr/2026-09-23T22-31-05Z`
(`sha256:412606009d30cb497180eaa881b1a02d3e5782ad44c1352f44f52cc5cd5a91b3`).
`staleness_sweep()`: clean across all 12 worlds. Old manifest retired
(directory kept, per convention).

**Entry 20 — 2026-09-23 (R43 Group A, world 1 of 4: cappadocian — 12
pre-existing renderings re-authored).** The R40 pass (Entries 13-18)
and the Nisibene fix (Entry 19) are merged. The reviewer's fleet-wide
`rendering_fidelity.py` sweep (reported on PR #465/#466) flagged 57
records that never went through the birth-condition grading process:
this is Group A, the four worlds whose renderings pre-date the gate
entirely (cappadocian 12, rzg 6, don 3, witt 3), ordered ahead of
Group B (today's R40 work re-read against fresh flags). This entry is
cappadocian, the first of the four.

For each of the 12 flagged records, read the grader's own reasoning
against the record's `text` field directly, rather than trusting or
dismissing the verdict on its label alone. All 12 were genuine: real
dropped clauses (`basil-canon-to-amphilochius`'s four distinct
penance-year restrictions collapsed together;
`basil-on-antiphonal-psalmody`'s two named effects of antiphonal
singing; `basil-on-the-doxology-challenge`'s full list of
qualifications on the doxology dispute; `gregory-nyssa-on-becoming-
god`'s concessive "although...still" clause connecting the two forms
of divine presence; `julian-galilaeans`'s causal "since" clause;
`macrina-refuses-remarriage`'s "compelled to consider another";
`ousia-and-hypostasis`'s description of how the word "strikes...the
ears"; `reading-scripture-hexaemeron`'s "open" firmament and its
distinct-qualities clause; `we-look-to-the-east`'s two separately-
stated unknowns conflated into one; `what-is-the-written-source`'s
"under the obligation to believe" and "principles of true religion")
or genuine invented framing (`basil-against-delaying-baptism`'s
over-explained "viaticum" and doubled invented "then" connectors).
None were dismissed as grader disagreement — no "human read stands"
exceptions this entry.

One structural pattern recurred and is worth naming for future
re-authoring passes: the grader consistently penalizes converting a
subordinate clause (a relative clause, a concessive "although...still",
a causal "since") into a separate paratactic sentence, even when no
content is lost — it reads the restructuring itself as dropping the
grammatical connection. `basil-on-work-and-prayer` needed two rounds
for exactly this reason: splitting "giving thanks to Him who gave both
X...and also Y" into "we give thanks to him. He gave us X...He also
gave us Y" was flagged as content loss on 5 consecutive calls despite
carrying every clause; keeping it as one relative-clause sentence
attached to "him" cleared on the first re-check. `gregory-nyssa-on-
becoming-god` needed the same fix for its "although...still" clause,
flagged 4 times before being restored to a genuine concessive
construction. Where FK forced a sentence break regardless (`julian-
galilaeans`), splitting the causal clause into a new sentence
introduced by "That is because" (rather than the drop-in connector
tried first) produced a passing, if inconsistent, verdict — 3 of 4
total calls read "translation" on the identical final text, matching
the established grader-noise pattern rather than a live disagreement.

**A real script bug, caught and fixed before commit.** The batch-
replacement script used to swap out these 12 pre-existing renderings
inherited a defect from how the file is split on the literal string
"---": when `modern_rendering` was the last field in a record's front
matter (true for all 12, since these were appended at the end by an
earlier, pre-R40 process), the script's own blank-line-skipping logic
also consumed the trailing empty split-artifact that normally
preserves the newline before the closing "---", gluing the last
rendering line directly onto it (`...pleasing him.---`). Caught by
inspecting the diff before committing, not by the grader or any gate
(the files remained parseable, since `content.split('---')` doesn't
care about line position). Fixed with a single targeted regex pass
restoring the missing newline in each of the 12 files, verified against
a clean `git diff` showing only `modern_rendering` values changed. No
gate currently checks front-matter line hygiene directly; noted here
rather than filed as a gap, since the fix is complete and the defect
never reached a commit.

**Gate results.** `gate_readability` (FK ceiling 10): 0 findings
across all 12 (range 2.7-9.5). Full `run_all()` (all M1 gates) on
cappadocian: 1 finding, the same pre-existing `voice-perspective` flag
on `cappadocian.dw.reading-scripture` (confirmed present on main
before this branch, untouched by these 12 records). `pytest
engine/m1/tests/`: 134 passed, no regressions. No field other than
`modern_rendering` touched on any of the 12 records; no per-record
notes added, per R33.

**Package pin.** Main had not moved since branching; rebuilt and
re-pinned once against this PR's own commit
`39db2f7adc8b3a5b7d4d2ae7b7f1313047d776b4`. Old
`packages/cappadocian/2026-09-23T08-13-26Z`
(`sha256:6cd515e5e88423f7c2fa60dec47ad3a927790821b6e8426cf9f09bb0c4e07ced`)
→ new `packages/cappadocian/2026-09-23T23-43-39Z`
(`sha256:941257d57d913b7715bfc8bd6fe8579a8e393cb160d1d9edde35fa0ec31ba7db`).
`staleness_sweep()`: clean across all 12 worlds. Old manifest retired
(directory kept, per convention).

**A second, separate staleness gate, discovered here for the first
time in this decision log.** CI's "Site staleness sweep" job failed on
the first push (head `e5bd8004`): `engine.m2.site_cli staleness-check`
reported `cappadocian` stale (`diff: ["narrative"]`). This checks a
different compiled artifact than the M2 package pin above -
`cic-website/data/worlds/<census_id>.json`, built by
`engine.m2.site_cli build <world> --records-commit <sha>
--compiler-version <version>` - and R40's world-by-world PRs never
tripped it because none of those touched a record that this compiled
JSON's "narrative" section draws from. R43's re-authoring apparently
does. Fixed by rebuilding that JSON against the real resolved HEAD;
`engine.m2.site_cli staleness-check` now reports `pass: true`
fleet-wide, and `pytest engine/m1/tests/ engine/m2/tests/` (191 tests)
passes. **Going forward, every remaining R43 world PR (rzg, don, witt,
then the Group B re-read pass) rebuilds both this site JSON and the M2
package pin as a standard part of its own re-pin step, not just the
world whose CI happens to catch it.**

**Round 1 FAIL, reviewer's human read (2026-09-24, head `f1c07aad`).**
The grader passed all 12 on the batch above, but a human re-read
against the process doc's own fragment rule (V1.6, Phase B) caught
three fragments the grader cannot see, since it grades meaning, not
grammar: `basil-canon-to-amphilochius`'s "In the third, to penance."
and "In the fourth, to standing..." dropped the implied "they may be
received" the source's own elliptical series carries across all three
year-clauses; `basil-on-the-doxology-challenge`'s "Or, if they are
wholly incurable, for the security of those who might fall in with
them." was split off from the purpose clause it modifies, leaving it
verbless; `what-is-the-written-source` paraphrased "Time will fail me
if I attempt to recount" as "I could spend the rest of the day
naming" where the original survives plainly in modern English and
should have been kept. All three re-authored (each fragment given its
own subject and verb, the paraphrase reverted to direct translation);
grader confirmed "translation" twice on all three; `gate_readability`
clean (6.4, 7.8, 9.7); full M1 `run_all()`: still only the same
pre-existing `voice-perspective` finding; `pytest engine/m1/tests/
engine/m2/tests/`: 191 passed. Re-pinned again against the real
resolved HEAD `c773bc43a044bc08a69bc04680c134efd70ec9ad` (both the M2
package, `packages/cappadocian/2026-09-24T00-06-02Z`
(`sha256:d553f510b634f92d38e7d1160c121805e19340dea0be50933da32fdb8ef1ec52`),
and the site-compiled JSON); both staleness checks clean.

**Entry 21 — 2026-09-24 (R43 Group A, world 2 of 4: rzg — 6
pre-existing renderings re-authored).** cappadocian (PR #467) is done
and merged, on its second round after the reviewer's own human read
caught 3 fragments the grader missed. This entry applies that lesson
from the first turn: every one of the 6 renderings below was re-read
by hand against the process doc's fragment rule before pushing, not
left to the grader alone.

Read each grader reasoning against the record's own `text` field
directly. All 6 were genuine: `christ-the-mirror-of-election` had
dropped the explicit rejection of those who seek election outside
Christ and lost the "mirror" metaphor to a paraphrase;
`mass-not-a-sacrifice` had dropped "certain and valid sacrifice for
the sins of all faithful" and "assurance of the salvation";
`seniors-selected-from-the-people` had dropped the term "seniors"
itself and "censures," and merged two distinct actions
(pronouncing censures, exercising discipline) into one vague
paraphrase; `signs-and-things-signified` had dropped the opening
"Wherefore" and inverted the original's negative "we do not disjoin"
into a positive restatement; `taught-better-from-scripture` had
dropped Zwingli's name, "Zurich," "articles and opinions," and
"called inspired by God"; `zwinglis-last-words` had dropped the "it
is true" concession and flattened the parallel kill-the-body/not-the-
soul contrast.

Two of the six needed a second revision round after the first fix
still read as summary: `christ-the-mirror-of-election` had swapped
"behold" for an added "reflected" (removed); `seniors-selected-from-
the-people` needed three attempts total — splitting into two
sentences first lost the "unite with the bishops in [doing both
things]" collaborative framing, then a single-sentence version with
simplified verbs ("give"/"keep" for "pronounce"/"exercise") was
flagged for the substituted vocabulary; the version that cleared kept
the literal verbs restored ("pronounce," "exercise") while splitting
into two sentences joined by "They," preserving both the exact
vocabulary and a natural sentence break. `zwinglis-last-words` showed
the established grader-noise pattern once more (a "summary" flag on
materially unchanged text that read "translation" 3/3 on immediate
re-runs) rather than a real defect.

**No honest exceptions, no "grader disagreement" entries this world.**
Two consecutive full-batch grader runs: 6/6 "translation" (with the
one independently-reconfirmed noise flake above).

**Gate results.** `gate_readability` (FK ceiling 10): 0 findings
across all 6 (range 1.0-9.3). Full `run_all()` (all M1 gates) on rzg:
0 findings. `pytest engine/m1/tests/ engine/m2/tests/`: 191 passed,
no regressions. No field other than `modern_rendering` touched on any
of the 6 records; no per-record notes added, per R33.

**Package pin and site JSON, both rebuilt from the start this time**
(per Entry 20's own discovery). Main had not moved since branching;
rebuilt and re-pinned once against this PR's own commit
`0880c259a01cb273aa56213b7f664edda4ffea34`. Old
`packages/rzg/2026-09-23T08-14-22Z`
(`sha256:57da83b635e38495dc8a1f636fa27ef27903d7d862172e032d9f2501986ee3de`)
→ new `packages/rzg/2026-09-24T00-32-15Z`
(`sha256:ebccc678a23583c6b8b34443e1a9d01d10cdcee8171e732851c9e281db554535`).
Site JSON (`cic-website/data/worlds/the-reformed-cities-zurich-and-
geneva.json`) rebuilt against the same commit. Both
`engine.m2.checks.staleness_sweep()` and `engine.m2.site_cli
staleness-check` report clean fleet-wide.

**Round 2 — register fix (2026-09-24), reviewer's own human read.**
The reviewer's verdict on the round above PASSed 5 of 6 records but
caught a register problem the grader itself did not: `signs-and-
things-signified`'s rendering had kept "Wherefore" and "disjoin"
verbatim from the source. Neither survives plainly in modern spoken
English — the rule that the original word stays where it survives
plainly cuts the other way for these two. Changed "Wherefore" →
"Therefore" and "disjoin" → "separate"; nothing else in the sentence
touched (the "as we ought" qualifier, the negative "we do not ...
the reality from the signs" structure, and the trailing genuine
ellipsis all carried over unchanged).

Five grading runs on the fixed text: 3 "translation," 2 "summary."
The two "summary" runs' own reasoning called "separate" a "synonym"
for "disjoin" in one clause and then, in the next, treated that same
substitution as a lost distinction — internally inconsistent, and the
same established grader-noise pattern documented elsewhere in this
log (unchanged text flipping verdict with reasoning not always
factually anchored to the text graded). Treated as noise, not a real
defect, per the standing protocol; not rewritten further.

`gate_readability`: clean. Full `run_all()` on rzg: 0 findings.
`pytest engine/m1/tests/ engine/m2/tests/`: 191 passed. Only this one
record's `modern_rendering` field changed from the round above.

Re-pinned against this fix's own commit `05d0c74ad5e0029ed3611617fd4ccf305f38a9d0`:
old `packages/rzg/2026-09-24T00-32-15Z`
(`sha256:ebccc678a23583c6b8b34443e1a9d01d10cdcee8171e732851c9e281db554535`)
→ new `packages/rzg/2026-09-24T01-14-01Z`
(`sha256:ec3bfe6c959c029e45c97015b8dd751f81535606fb44d98b833a71724e9ad775`).
Site JSON rebuilt against the same commit. Both staleness checks
clean fleet-wide.

**Entry 22 — 2026-09-24 (R43 Group A, world 3 of 4: don — 3
pre-existing renderings re-authored).** rzg (PR #468) is done and
merged, including its own round-2 register fix. All 3 of don's
findings were read by hand against the record's own `text` field
before re-authoring, and every rewrite was hand-checked against the
process doc's fragment rule before pushing.

All 3 were genuine. `emeritus-magno-argumento` had dropped the "great
argument" (magno argumento) concept entirely and lost the original's
causal `ut cum` structure (the small answer from the other side is
what triggers the rest going unanswered). `petilian-conscience-of-
the-giver` had dropped "him who gives in holiness" and flattened
"receives not faith, but guilt" into a single negation that lost the
original's explicit not-X-but-Y contrast. `the-shores-are-covered`
had dropped "shipwrecked members," "certain men," and "intensified in
death itself," and had condensed the Egyptian comparison so that the
specific image of shores covered with bodies was lost.

Two records needed more than one round. `emeritus-magno-argumento`'s
first fix added an unwarranted modal ("can hide") and was read by the
grader as adding a causal frame not in the Latin; removing the modal
and keeping the passive ("truth is hidden by...") cleared it, and a
lone "expansion" flag on an unchanged re-run afterward was the
established grader-noise pattern (4 "translation" out of 5 total
runs). `petilian-conscience-of-the-giver` needed three attempts: the
first dropped "conscience" as a term and blurred the not-faith-but-
guilt contrast; the second restored "conscience" but the added "so
that it may cleanse" was flagged as an invented causal claim not in
the Latin's plain infinitive; the third, closest to the original's
own clause order ("to cleanse that of the recipient"), cleared 3/3.
`the-shores-are-covered` needed a readability-driven revision after
the record's own first fix scored FK 12.7 (a long sentence built from
an inserted mid-clause, "the shores, ... are covered ..."); splitting
into shorter independent sentences brought it to FK 6.9, but that same
split had replaced the original's causal "since ... after their life
has been wrung ... they fail to find" with a bare "and," which the
grader caught reproducibly (4 of 5 runs) as a real dropped clause, not
noise; restoring "Since the avenging waters have wrung their life from
them" cleared 3/3 at FK 6.9.

**No honest exceptions, no "grader disagreement" entries this world.**
Every record read "translation" on at least two consecutive runs of
its final wording once genuine drops were fixed.

**Gate results.** `gate_readability` (FK ceiling 10): all 3 clean
(6.4, 7.8, 6.9). Full `run_all()` (all M1 gates) on don: only the
pre-existing `reciprocity` findings (52, confirmed unrelated and
present identically on unmodified main - none of the 52 name any of
the 3 records touched here, and none is this PR's to fix).
`pytest engine/m1/tests/ engine/m2/tests/`: 191 passed, no
regressions. No field other than `modern_rendering` touched on any of
the 3 records, per R33.

**Package pin and site JSON, both rebuilt from the start.** Main had
not moved since branching; rebuilt and re-pinned once against this
PR's own commit `5be7b57c31e3b226bfdd14da5008b16b9d0006c0`. Old
`packages/don/2026-09-23T08-13-44Z`
(`sha256:a69aab7d7b4a00fec1f9d7658e454e52609ecaabd40b4845c06c3dd97751f9f1`)
→ new `packages/don/2026-09-24T01-48-30Z`
(`sha256:8abee285d1ae498dc27d64686d40ec13cc38ce1d8d3b772a4135ded01dbbefde`).
Site JSON (`cic-website/data/worlds/donatism.json`) rebuilt against
the same commit. Both `engine.m2.checks.staleness_sweep()` and
`engine.m2.site_cli staleness-check` report clean fleet-wide.

`check_paths.py`, run on a clean `git worktree` of this branch's head:
0 new unresolved path citations; 769 total; 769 accepted in baseline;
0 retired paths present.

**Entry 23 — 2026-09-24 (R43 Group A, world 4 of 4: witt — 3
pre-existing renderings re-authored, completing Group A).** don (PR
#469) is done and merged. All 3 of witt's findings were read against
the record's own `text` field first, checked for genuine vs. noise by
re-grading the unmodified rendering 3x before touching anything (per
the lesson that a mid-range split like 2/3 "translation" still needs a
closer read, not an automatic pass): `article-ii-of-original-sin`
graded 0/3, `nothing-that-varies` graded 0/3, and `article-ix-of-
baptism` graded 2/3 but was still fixed rather than accepted, since the
one "mixed" run named a real, specific drop (the restrictive "being
offered to God through Baptism" clause) rather than reading as noise.

All 3 were genuine. `article-ii-of-original-sin` had replaced
"concupiscence" with an interpretive gloss ("desires turned the wrong
way") rather than a direct term-for-term translation, and had lost "to
obscure the glory of Christ's merit and benefits" as the Pelagians' own
stated motive, substituting a generic hypothetical ("a person could
obscure Christ's own merit") instead. `article-ix-of-baptism` had
dropped "being offered to God through Baptism" as the condition tied to
the children being baptized, and had added an invented "We do not
agree" with no source anchor. `nothing-that-varies` had split "against
Scripture or the Church Catholic" into two disconnected claims, dropped
"on our part," weakened "most diligent care" to "the greatest care,"
lost the purpose clause "in order that it might be understood," and
added an invented "in fact."

**No honest exceptions, no "grader disagreement" entries, no second
revision round needed.** All three cleared 3/3 "translation" on the
first rewrite.

**Gate results.** `gate_readability` (FK ceiling 10): all 3 clean (5.4,
5.5, 9.3). Full `run_all()` (all M1 gates) on witt: 0 findings.
`pytest engine/m1/tests/ engine/m2/tests/`: 191 passed, no
regressions. No field other than `modern_rendering` touched on any of
the 3 records, per R33.

**Package pin rebuilt from the start; no site JSON to rebuild.**
Rebuilt and re-pinned once against this PR's own commit
`9bd503f2bdb3e26872dd24303f90194eab50fb54`. Old
`packages/witt/2026-09-23T08-14-29Z`
(`sha256:ba693f3c0d7d16c35a30462adedbeba24494c1fb56a1dd9860c914233a98b088`)
→ new `packages/witt/2026-09-24T02-18-24Z`
(`sha256:f0ebc05d889ff9569e57e3d74e3f26b4fe30a8feb3dd46e9e16707258ba69f08`).
witt has no `world_front` record yet and is confirmed absent from
`engine.m2.site_cli staleness-check`'s own world list - not a gap
introduced by this fix, so there is no second artifact to rebuild here.
`engine.m2.checks.staleness_sweep()` reports clean fleet-wide;
`engine.m2.site_cli staleness-check` reports `pass: true` over its own
(witt-less) world list.

`check_paths.py`, run on a clean `git worktree` of this branch's head:
clean, matching the baseline exactly.

**This completes R43 Group A** (cappadocian, rzg, don, witt). R43
Group B (desert, hal, pahc, syr, alx re-read pass) starts next.

**Entry 24 — 2026-09-24 (R43 Group B, world 1 of 5: desert — 8 of 11
flagged findings re-authored, 3 grader disagreements).** witt (PR #470)
is done and merged, closing Group A at 24 records. This is the first
Group B world: unlike Group A, every flagged finding is re-graded 3x
unmodified before any change is made, to separate a genuine drop from
grader noise, and a record where the grader's own reading is wrong is
left unchanged and listed as a disagreement rather than rewritten to
satisfy it.

**3 of 11 are grader disagreement, human read stands, unchanged.**
`an-old-man-in-the-next-village` (3/3 translation on re-grade): the
grader's original flag wanted the "after he had seen this man" causal
link stated explicitly, but the rendering's own clause order (saw, then
imitated) already carries that sequence; nothing is dropped or added.
`monks-like-hyenas` (3/3 translation): the grader's flag claimed the
hyena-actions comparison was lost, but the rendering states it as its
own explicit sentence ("Their actions are like those of the hyena");
the flag does not match the actual text. `never-kneel-saturday-to-
sunday` (3/3 summary on re-grade, but the grader is wrong): re-reading
the source's own "nor...nor" structure directly shows that both
no-kneeling and no-fasting apply to BOTH periods (the weekly Saturday-
evening-to-Sunday-evening span and the Easter-to-Whitsuntide season),
exactly what the rendering already states; the grader misparses the
sentence as restricting fasting to only one period, which the Latin
does not support and standard patristic-liturgical practice (no
kneeling or fasting through the whole Paschal season) confirms.

**8 of 11 were genuine**, each requiring 2-3 revision rounds (re-graded
3-5x per round) before clearing on a translation majority: `eight-
principal-faults` had dropped the Greek/Latin technical terms
(gastrimargia, philargyria, acedia, cenodoxia) and split their glosses;
`equal-measure-of-strength` had dropped the causal "so that" framing
and "the labour of ascetic excellence" as the named domain;
`for-thirty-two-years-i-touched-no-fruit` had moved the purpose clause
("in order to get rid of it") out of its original position, changing
the emphasis; `grace-and-free-will-in-harmony` had dropped "the system
of" and the prescriptive "ought to have"; `so-perfectly-silent` had
dropped the "celebrate their rites" framing before naming the synaxis;
`they-have-taken-away-my-god` had dropped "Alas!" and compressed
"worship and address" into a single loosely-matched pair;
`the-deeds-of-christ-prove-him` had detached "which shew that Christ is
no longer a man but God" from the miracle list into a separate
sentence and dropped the "Or why...are you silent" rhetorical
structure - the record also carried an incidental defect independent
of the flagged issue (`paralytics` had been swapped for `lame`, a
different medical condition, though `paralytics` itself survives
plainly in modern English and needed no translation) - restoring the
relative-clause structure and the original term both were required
before it cleared 5/5. `twelve-psalms-by-an-angel` needed the most
rounds: an early revision introduced its own defect (an invented
"The elders once argued..." framing sentence not in the source, caught
5/5 as "expansion" once the surrounding content was restored) before a
version translating directly from the source's own opening clause,
with no invented frame, cleared on a 3/5 translation majority - the
residual 2/5 "summary" flags on that final version cite only minor
word-level compression ("quite easy" vs "easy," dropped "considering")
with no further clause actually missing, so majority-translation is
accepted rather than chased further, per the standing grader-noise
protocol.

**Gate results.** `gate_readability` (FK ceiling 10): all 8 re-authored
records clean, including two that needed a dedicated readability pass
after their first content-restoring rewrite scored above ceiling
(`twelve-psalms-by-an-angel` 22.6→9.6, `the-deeds-of-christ-prove-him`
12.4→9.0) - both re-cleared the fidelity gate again after the
readability-driven rewrite, since splitting a sentence for FK can
itself drop content if done carelessly, which happened once on each
before the version that held both gates at once. Full `run_all()` (all
M1 gates) on desert: only the pre-existing `reciprocity` finding (1,
confirmed identical on unmodified main, naming a record this PR does
not touch - not this PR's to fix). `pytest engine/m1/tests/
engine/m2/tests/`: 191 passed, no regressions. No field other than
`modern_rendering` touched on any of the 8 re-authored records, per
R33; the 3 disagreement records are untouched entirely.

**Package pin and site JSON, both rebuilt from the start.** Rebuilt and
re-pinned once against this PR's own commit
`edc5832ba1b749e07fa9c78577ddcadedb7ece8f`. Old
`packages/desert/2026-09-23T19-33-23Z`
(`sha256:a43b6eb055028868314ab3cdd5d7e5b64d23fb690f8042693e4e5a15b55b3977`)
→ new `packages/desert/2026-09-24T03-04-22Z`
(`sha256:f7c861054e70389fb7405bf1175a35ff4018785774c2366d6d8fc026c8273491`).
Site JSON (`cic-website/data/worlds/desert-monasticism.json`) rebuilt
against the same commit. Both `engine.m2.checks.staleness_sweep()` and
`engine.m2.site_cli staleness-check` report clean fleet-wide.

`check_paths.py`, run on a clean `git worktree` of this branch's head:
0 new unresolved path citations; 769 total; 769 accepted in baseline;
0 retired paths present.

**Entry 25 — 2026-09-24 (R43 Group B, world 2 of 5: hal — 7 of 8
flagged findings re-authored, 1 grader disagreement, 2 partial
disagreement notes).** desert (PR #471) is done and merged. Every
flagged finding re-graded 3x unmodified before any change, same
discipline as desert.

**1 of 8 is grader disagreement, human read stands, unchanged.**
`eyes-of-faith` (6/7 translation across all re-grades): the flag called
"She told me this herself, and I heard her say it" an invented framing
addition, but this is a fair two-clause rendering of the original's own
"she protested in my hearing" - the fact that she said it and that the
author heard it are both already stated in that one phrase; nothing is
added beyond restating it in two clauses instead of one.

**7 of 8 were genuine**, two of which carry their own partial
disagreement note alongside the fix. `a-follower-of-cicero-and-not-of-
christ` had dropped "judgment" from "judgment seat" and added an
unattested "beaten" gloss after "whipped" (the source says only
"scourged"). `detestable-monks` had merged the separate purpose clause
"that she might have grandchildren" into the marriage clause and
weakened "must we refrain from" (a strong negative obligation) into a
forward-looking question. `dispute-to-learn` had dropped "at once
acquiesce" and "on the contrary"; its "about the scriptures" phrase,
which the grader flagged 3/3 as an invented addition once the rest was
fixed, is left as written and disagreed with here - the record's own
body note independently verifies "them" = "the scriptures, from the
preceding sentence" in the source Jerome letter, so this is
disambiguated content already confirmed by this build, not invented.
`ever-let-the-bridegroom-sport-with-you` had lost the "ever...ever"
anaphora and flattened the "Do you pray? ... Do you read?" direct
question-and-answer form into conditional statements; the version that
cleared kept "delight" for "sport" (a defensible modernization of a
verb whose "play/frolic" sense is now unclear) and lowercase divine
pronouns (already this corpus's own house style), which a later re-run
flagged but which are not fidelity defects. `house-destroyed` had
dropped the "so far as...is concerned" scope qualifier; separately, in
4 of 6 re-grades after that fix, the grader claimed the trailing
"To live on bread is better than to lose the faith" clause was missing
- it was present verbatim throughout every version checked directly
against the file; noted here as a hallucination, not acted on.
`innocent-ravages` had dropped "have deplored to me" and the framing of
the women's silence as a deliberate act of "wonderful clemency and
generosity" rather than a bare fact. `recourse-to-marcella` had added
an invented "this is what happened" and flattened the conditional "in
case of a dispute arising" into a narrated "whenever people disagreed."

**Two records needed a readability-driven revision** after their first
content-restoring fix scored above the FK ceiling: `innocent-ravages`
(12.9→9.8) and `recourse-to-marcella` (10.3→6.7). Both re-cleared 3/3
translation after the split, with no new drop introduced this time.

**Gate results.** `gate_readability` (FK ceiling 10): all 7 re-authored
records clean. Full `run_all()` (all M1 gates) on hal: 0 findings.
`pytest engine/m1/tests/ engine/m2/tests/`: 191 passed, no
regressions. No field other than `modern_rendering` touched on any of
the 7 re-authored records, per R33; `eyes-of-faith` is untouched
entirely.

**Package pin and site JSON, both rebuilt from the start.** Rebuilt and
re-pinned once against this PR's own commit
`086ffdc35173ef82042c93b45bfbd8c6af73d916`. Old
`packages/hal/2026-09-23T20-32-17Z`
(`sha256:c98a2632cfadc230a540dfee33f56de83d679c7692d3f837f0f0b8674fa9783f`)
→ new `packages/hal/2026-09-24T03-27-07Z`
(`sha256:297a2b974640df9ae642ad49c364cb76791dcf7a8063433503c2191c66a96ec5`).
Site JSON (`cic-website/data/worlds/hieronymian-ascetic-literary.json`)
rebuilt against the same commit. Both
`engine.m2.checks.staleness_sweep()` and `engine.m2.site_cli
staleness-check` report clean fleet-wide.

`check_paths.py`, run on a clean `git worktree` of this branch's head:
0 new unresolved path citations; 769 total; 769 accepted in baseline;
0 retired paths present.

**Round 2 — fragment and register fix (2026-09-24), reviewer's own
human read.** PASS on 5 of 7 fixed records and on the one grader
disagreement; two records still needed a fix before merge.
`dispute-to-learn`'s "Not for argument's sake, but to learn the answers
to those objections which might, as she saw, be made to my statements"
stood as its own sentence with no subject or verb - the exact fragment
rule (process doc V1.6, Phase B) the grader does not catch. Joined to
the clause before it ("...she would dispute them, not for argument's
sake..."), and the earlier "Nor would she at once acquiesce in my
explanations" split into its own complete sentence to keep the result
under the readability ceiling (FK 11.3→8.1) without reopening a
fragment. `ever-let-the-bridegroom-sport-with-you`'s "Ever let" was not
everyday modern English (the same rule that turned rzg's "Wherefore"
into "Therefore"); changed to "Always let" in both halves of the
anaphora. "Delight" for "sport" and the lowercase divine pronouns were
confirmed correct as already written.

Both re-graded: `ever-let-the-bridegroom-sport-with-you` cleared 2/2
translation. `dispute-to-learn` continued to carry its own pre-existing,
already-documented disagreement ("about the scriptures," verified by
the record's own body note) across re-grades - expected, not a new
finding, and not grounds for a further round per the reviewer's own
"documented exception if the grader is stricter than the text."
`gate_readability` and full `run_all()`: clean on both. `pytest
engine/m1/tests/ engine/m2/tests/`: 191 passed.

Re-pinned against this fix's own commit
`f882c2f54f7323459f3b61021cdbd1cf4433df87`: old
`packages/hal/2026-09-24T03-27-07Z`
(`sha256:297a2b974640df9ae642ad49c364cb76791dcf7a8063433503c2191c66a96ec5`)
→ new `packages/hal/2026-09-24T03-53-40Z`
(`sha256:e4d70c99d7d1056660d420c442c535ffa08b3bbccf5532ed4bbeb29c25039829`).
Site JSON rebuilt against the same commit. Both staleness checks clean
fleet-wide.

**Entry 26 — 2026-09-24 (R43 Group B, world 3 of 5: pahc — all 6
flagged findings re-authored, no full grader disagreements).** hal (PR
#472) is done and merged. Every flagged finding re-graded 3x unmodified
before any change, same discipline as desert and hal.

**All 6 were genuine**, each needing 2-3 revision rounds.
`asia-rejected-new-prophecy`'s first attempted fix over-specified "the
followers of the New Prophecy" for the original's ambiguous "they" -
the record's own context (modern_lens_note, retrieve_when) makes that
referent likely, but unlike hal's `dispute-to-learn` there is no
explicit body-note verification of the antecedent within the text's
own reach, so this specification was removed as a genuine
over-correction rather than kept as a documented disagreement; the
remaining fix (restoring "for deliberation on this subject" and the
two distinct expulsion/debarment actions) cleared 3/3 translation after
a readability split (FK 11.2→9.0). `ignatius-truly-born` had replaced
"quickening" with an interpretive "giving him life" and lost "by
Christ Jesus" and "so raise up" from the resurrection parallel;
restoring "quickening" verbatim (a modern-survivable term, register-
appropriate to keep rather than translate) and the fuller parallel
cleared it. `melito-no-phantom` needed the most rounds: one revision
reintroduced dropped content but over-fixed readability (FK 19.2)
before a version balancing both gates was found (FK 9.97); it carries
a documented, previously-established tension - the same pattern don's
`the-shores-are-covered` showed in R43 Group A - where the grader
penalizes splitting a subordinate clause even when no content is lost,
and keeping the clause attached costs the readability ceiling. The
FK-compliant split is kept; the residual grader complaint (three
straight "summary" runs on the same single clause-attachment point) is
disclosed here rather than chased further. `polycrates-to-victor` had
dropped "scrupulously," the luminaries' resurrection clause, "in
accordance with the tradition of my relatives," and "the things which
are said to terrify us" - needing a further round after its own first
fix scored above the FK ceiling and a second round after that fix
dropped "Moreover I also" and "For in Asia." `two-female-slaves-who-
were-called-deaconesses` had compressed the necessity/purpose clause
and the tie between postponing inquiry and the preceding findings, and
needed one readability-driven revision (FK 11.97→9.4). `two-ways-one-
of-life-and-one-of-death` had lost the explicit parallel/reciprocal
phrasing of the golden rule's negative form ("all things whatsoever
thou wouldst... thou also to another do not do").

**Gate results.** `gate_readability` (FK ceiling 10): all 6 clean.
Full `run_all()` (all M1 gates) on pahc: only the pre-existing
`reciprocity` findings (2, confirmed identical on unmodified main,
naming a record - `two-female-slaves-who-were-called-deaconesses` - as
the reciprocal-relation target but not touching that record's own
content; not this PR's to fix). `pytest engine/m1/tests/
engine/m2/tests/`: 191 passed, no regressions. No field other than
`modern_rendering` touched on any of the 6 records, per R33.

**Package pin and site JSON, both rebuilt from the start.** Rebuilt and
re-pinned once against this PR's own commit
`882fb275e7905f4d68b21e8e2cd5c66bf2b003bd`. Old
`packages/pahc/2026-09-23T21-19-18Z`
(`sha256:fac1498358c0ef5d7577b6bb86263b1741a3d227b875f572b168109e53c2f8af`)
→ new `packages/pahc/2026-09-24T04-22-27Z`
(`sha256:7549fb4c6945e92baf28c76db6484bb4f50ae82eae2e993e25ae54f95ca59279`).
Site JSON (`cic-website/data/worlds/post-apostolic-house-church.json`)
rebuilt against the same commit. Both
`engine.m2.checks.staleness_sweep()` and `engine.m2.site_cli
staleness-check` report clean fleet-wide.

`check_paths.py`, run on a clean `git worktree` of this branch's head:
0 new unresolved path citations; 769 total; 769 accepted in baseline;
0 retired paths present.

**Round 2 — fragment and register fix (2026-09-24), reviewer's own
human read.** FAIL on 3 of the 6 records on grounds the grader cannot
see. `melito-no-phantom`: "Of his Deity, by his miracles during the
three years after his baptism." and "Of his humanity, during the
thirty similar years before his baptism." each stood as a fragment
with no subject or verb - fixed by supplying the verb the parallel
gives ("He showed his Deity...", "He showed his humanity..."), the
same fragment rule (V1.6, Phase B) that caught cappadocian and rzg's
own fragments earlier in R43. Also translated the archaic "by reason of
his low estate as regards the flesh" to "because of his lowly condition
in the flesh." The fix pushed FK to 10.36; a further trim ("during" ->
"in" twice, "concealed" -> "hid", "existing before" -> "from before")
brought it to 9.82 without reopening a fragment. The record's own
documented tension (the grader penalizing the subordinate-clause split
even with no content lost) persists after the fix (2/3 translation on
re-grade) - not a new finding, not chased further, per the reviewer's
own instruction that the fragment and register rules win over the
grader here.

`ignatius-truly-born`: "his Father quickening him" is archaic in the
bring-to-life sense (the same category as "wherefore" in rzg and "Ever
let" in hal); translated to "his Father bringing him back to life" -
a documented exception, since an earlier grading round's own
"interpretive" objection to exactly this phrasing is the grader being
stricter than the text, not a real defect; the human read stands. Also
modernized the archaic word order "will so raise up us who believe in
him by Christ Jesus" to "will raise us up too, we who believe in him,
by Christ Jesus." Cleared 2/2 translation.

`polycrates-to-victor`: "fallen in with the brethren" kept an archaic
idiom and an archaic word ("brethren") the same rendering already
translates elsewhere as "brothers" - changed to "met with the
brothers." Cleared 2/2 translation.

All three hand-checked for fragments before pushing. `gate_readability`
and full `run_all()`: clean on all three (only the pre-existing,
unrelated `reciprocity` findings remain fleet-wide). `pytest
engine/m1/tests/ engine/m2/tests/`: 191 passed.

Re-pinned against this fix's own commit
`5a15111272ad8571124041137c22bbeddac94c57`: old
`packages/pahc/2026-09-24T04-22-27Z`
(`sha256:7549fb4c6945e92baf28c76db6484bb4f50ae82eae2e993e25ae54f95ca59279`)
→ new `packages/pahc/2026-09-24T04-53-27Z`
(`sha256:6e0a30f0bf49d9413dd9442b8ef18d1855bb1e4a893fce5532de964d0b382269`).
Site JSON rebuilt against the same commit. Both staleness checks clean
fleet-wide.

**Entry 27 — 2026-09-24 (R43 Group B, world 4 of 5: syr — 5 of 6
flagged findings re-authored, 1 excluded).** pahc (PR #473) is done and
merged. `nisibene-death-trembled` is excluded from this pass entirely:
it was already fixed under Mark's own direct ruling (PR #466, "did
likewise" finishing the elliptical sentence), not a new finding for
this re-read to act on.

**All 5 remaining were genuine.** `blc-one-name` had added an
unattested "appointed" qualifier before "days of the readings" and
dropped the repeated preposition in "in every country and in every
region." `ephrem-only-begotten-dwelling` had expanded "a common manner
of birth" into an invented explanatory gloss ("He was born the way we
are all born") and dropped the "though only-begotten" paradox entirely.
`ephrem-resurrection-pledge` had added "the place of the dead," "knows
each one," and "us who die" - none in the source, and needed a
readability-driven revision after the first fix scored FK 15.5.
`tatian-barbaric-writings` had compressed "the declaration of the
government of the universe as centred in one Being" into a shorter
paraphrase ("one Being governs the universe"), losing the specific
locution; needed two readability rounds (FK 15.2, then 12.0, before a
version splitting the five-item causal list into short sentences
cleared at FK 6.7). One grading run on the final version showed a
verdict/reasoning mismatch worth recording as a distinct pattern: the
verdict enum read "summary" while the reasoning text itself said "no
content is omitted or added... a legitimate translation technique that
preserves all original content" - the label contradicted its own
stated reasoning, confirming grader noise rather than a real defect on
that run. `warned-before-baptism` had dropped two of the original's
three named groups the preachers are to warn (collapsing "those who
choose for themselves virginity and holiness" and "those wishing to
become holy" into "all who are choosing a holy single life") and the
"to warn them and say:" direct-speech attribution structure.

**Gate results.** `gate_readability` (FK ceiling 10): all 5 clean.
Full `run_all()` (all M1 gates) on syr: only one pre-existing,
unrelated `voice-perspective` finding naming a different record
(`syr.dw.death-judgment.text`) this PR does not touch. `pytest
engine/m1/tests/ engine/m2/tests/`: 191 passed, no regressions. No
field other than `modern_rendering` touched on any of the 5 records,
per R33.

**Package pin and site JSON, both rebuilt from the start.** Rebuilt and
re-pinned once against this PR's own commit
`e4c036e2e588b5276f2e55b4e8f848e61c351c0b`. Old
`packages/syr/2026-09-23T22-31-05Z`
(`sha256:412606009d30cb497180eaa881b1a02d3e5782ad44c1352f44f52cc5cd5a91b3`)
→ new `packages/syr/2026-09-24T05-14-56Z`
(`sha256:5d017b74530785cbd0c675c6ff7b722a175c52e38f3084ecb301c901c1bfab43`).
Site JSON (`cic-website/data/worlds/syriac-edessa-nisibis.json`)
rebuilt against the same commit. Both
`engine.m2.checks.staleness_sweep()` and `engine.m2.site_cli
staleness-check` report clean fleet-wide.

`check_paths.py`, run on a clean `git worktree` of this branch's head:
0 new unresolved path citations; 769 total; 769 accepted in baseline;
0 retired paths present.

**Round 2 — closing-sentence and register fix (2026-09-24), reviewer's
own human read.** PASS on 3 of 5 fixed records; FAIL round 1 on
`warned-before-baptism`'s closing sentence, with a carry-fix on
`tatian-barbaric-writings`. `warned-before-baptism`: the closing
sentence had drifted from the source on three points - "grows fierce"
changed the condition (the source is the battle going *against* him,
not merely intensifying), "to save it" invented a motive not stated in
the source, and "that is a disgrace" dropped the source's general
maxim form ("there is disgrace to him who turns back"). Rendered close
to the source: "when the battle goes against you, you may remember
your possessions and turn back to them, for there is disgrace for the
one who turns back from the fight." `tatian-barbaric-writings`: "They
showed real foreknowledge of future events" had added "real," not
present in the source's "the foreknowledge displayed of future
events" - removed.

Both re-graded 3/3 translation. `gate_readability` and full
`run_all()`: clean on both (only the pre-existing, unrelated
`voice-perspective` finding remains fleet-wide, naming a different
record this PR does not touch). `pytest engine/m1/tests/
engine/m2/tests/`: 191 passed.

Re-pinned against this fix's own commit
`84c2257afe7620909ae2bb9d33c78bc3087f2652`: old
`packages/syr/2026-09-24T05-14-56Z`
(`sha256:5d017b74530785cbd0c675c6ff7b722a175c52e38f3084ecb301c901c1bfab43`)
→ new `packages/syr/2026-09-24T05-26-17Z`
(`sha256:2434894870ed7ff0e29b872427fa86648a2b0883b694ac933b45e118151f06f0`).
Site JSON rebuilt against the same commit. Both staleness checks clean
fleet-wide.

**Entry 28 — 2026-09-24 (R43 Group B, world 5 of 5: alx — special
#442 re-verification, both flagged records).** syr (PR #474) is done
and merged; this closes R43 Group B. Unlike the other four Group B
worlds, alx's two flagged records were not a fresh sweep finding to
triage cold - they were named directly, with an instruction to re-read
each against the fresh grader reasoning and say whether the earlier
#442 human read still holds.

**It does not hold for either record.** `no-sun-no-moon-no-sky`: the
R40 rendering broke Origen's single continuous rhetorical question
into a declarative closing clause ("...would obtain life" as a
statement), dropping the "so that...obtained life" logical connector
the source uses to tie the tree's visibility and palpability to the
consequence of tasting it. Restored the question structure, splitting
the sentence at "planted a garden in Eden, toward the east?" / "Who
would think he placed in it a tree of life...so that..." so the causal
clause stays attached to its own question rather than being severed
into a bare declarative. 5/5 translation on re-grade, FK 8.57.

`the-grades-here-in-the-church`: the R40 rendering dropped "according
to my opinion" (paraphrased to "In my view") and lost the perfect
tense on "have lived" (rendered as present "live"). Restored both.
"Economy" (Greek *oikonomia*) is translated as "the divine plan" - the
term does not survive plainly in modern English and no other alx
record explains it, so R34's register rule (translate jargon the
grader's "interpretive" objection notwithstanding) governs. The
apostles'-footsteps clause and "according to the Gospel" are kept
close to the source's own wording. This record needed 6+ substantive
revisions, more than any other record in Group A or B, and the
residual grader complaint never stabilized: one revision was faulted
for adding an "economy, the divine plan" gloss not in the source; the
next, which dropped the gloss and translated the term directly, was
faulted for losing the term; tense and clause-order faults appeared
and disappeared the same way across attempts with no wording that
cleared all of them at once while holding FK under 10. This is the
same subordinate-clause-splitting tension already logged for desert's
`the-shores-are-covered` and pahc's `melito-no-phantom`: the source is
one ~60-word periodic sentence, and no split that fits the FK-10
ceiling escapes a strict grader reading the split itself as
"compression," independent of whether the content is actually still
there. It is: every clause the reasoning cites as dropped is present,
just distributed across two sentences instead of one. Kept the
FK-compliant, content-complete version and log the residual as an
accepted tension rather than a fixable defect - this is the
disposition Group B was explicitly opened to allow, used here because
careful re-reading shows the grader's remaining objection is about
sentence-boundary placement, not missing content.

Both hand-checked for fragments (mandatory since the grader grades
meaning, not grammar): clean.

**Gate results.** `gate_readability` (FK ceiling 10): both clean (8.57,
9.97). Full `run_all()` (all M1 gates), read directly from this
build's own `validation/gates-report.json` rather than a
partial-fleet script: `overall_pass: true`, no findings on either
record or fleet-wide. `pytest engine/m1/tests/ engine/m2/tests/`: 191
passed, no regressions. No field other than `modern_rendering` touched
on either record, per R33.

**Package pin and site JSON, both rebuilt from the start.** Rebuilt
and re-pinned against this PR's own commit
`3d75cbc10f619499536edbabb5a1982705b114de`. Old
`packages/alx/2026-09-23T17-10-40Z`
(`sha256:9d27e87d31c8df91e5a49a217dec80949974d5b8c06f02319538cb977c30beae`)
→ new `packages/alx/2026-09-24T05-58-09Z`
(`sha256:d3786be48aa2af2552519f4a1503500b28eb0e427ae3f65e3fcf8c796f50e6b5`).
Site JSON (`cic-website/data/worlds/alexandria-catechetical.json`)
rebuilt against the same commit. Both
`engine.m2.checks.staleness_sweep()` and `engine.m2.site_cli
staleness-check` report clean fleet-wide.

`check_paths.py`, run on a clean `git worktree` of this branch's head:
0 new unresolved path citations; 769 total; 769 accepted in baseline;
0 retired paths present.

**Round 2 — register and omission fix (2026-09-24), reviewer's own
human read.** PASS on `no-sun-no-moon-no-sky` (question structure held,
5/5 translation, FK 8.57). FAIL round 1 on
`the-grades-here-in-the-church`, three problems in the first two
sentences: (a) "Church has three ranks" dropped both the definite
article and "here" - the source's "the grades here in the Church" sets
the earthly ranks against "the angelic glory," and "here" carries that
contrast; (b) "three" is not in the source, which lists the ranks
without counting them; (c) "According to my opinion" is the source's
own wording carried forward unmodernized - the idiom is "In my
opinion," which an earlier revision already had before this fix
regressed it. The reviewer's own suggested wording restores all three
("In my opinion, the ranks here in the Church, bishops, presbyters,
and deacons, imitate the angelic glory and the divine plan. Scripture
says that plan awaits those who, following in the apostles' footsteps,
have lived in perfect righteousness according to the Gospel.") but
scores FK 11.7, over the readability ceiling as a two-sentence
rendering. Split the second sentence's embedded relative clause into
two independent sentences ("...those who follow in the apostles'
footsteps. They have lived in perfect righteousness according to the
Gospel.") to bring FK to 8.66 while keeping every element of the fix
intact: "here" restored, no count added, "In my opinion," "economy" as
"the divine plan," perfect tense on "have lived," "according to the
Gospel" kept close to the source.

Re-grading the three-sentence split shows a residual complaint (5/5
mixed) that separating "those who...have lived" loses the conditional
unity linking apostolic footsteps to the divine plan's promise - the
same subordinate-clause-splitting tension already logged earlier in
this entry and for desert's `the-shores-are-covered` and pahc's
`melito-no-phantom`. Every clause the automated grader cites as lost is
present in the rendering; flagged explicitly for the reviewer's own
human read (which already stands over the grader elsewhere in this
entry) rather than silently choosing between the reviewer's exact
wording and the FK gate, since the two cannot both be satisfied without
a split.

Re-pinned against this fix's own commit
`d808787dbd58bde53f8d8cf640cfb33de454cd54`: old
`packages/alx/2026-09-24T05-58-09Z`
(`sha256:d3786be48aa2af2552519f4a1503500b28eb0e427ae3f65e3fcf8c796f50e6b5`)
→ new `packages/alx/2026-09-24T06-31-34Z`
(`sha256:096977f80d5131fe112272a390b9dacf5a750a489697ecc534a5109440a5ad3f`).
Site JSON rebuilt against the same commit. Both staleness checks clean
fleet-wide. `check_paths.py` on a clean worktree of this commit: 0 new
unresolved path citations; 769 total; 769 accepted in baseline; 0
retired paths present. `pytest engine/m1/tests/ engine/m2/tests/`: 191
passed.

**This closes R43 Group B (desert, hal, pahc, syr, alx) and the whole
R43 fleet-wide rendering-fidelity re-authoring campaign**, once this
PR merges.

**Entry 29 — 2026-09-24 (sentence-completeness check on
`modern_rendering`, report-only).** Build thread C, item 1 of the
reviewer thread's brief. `rendering_fidelity.py`'s grader grades
meaning, not grammar, and passed every fragment the R43 human read
caught (Entries 20, 25, 26). `engine/m1/sentence_completeness.py`
checks grammar only: every sentence of every quote record's
`modern_rendering` must have a main clause with its own subject and
finite verb (process doc V1.6, Phase B, fragment rule). Report-only
per R39; not registered in `gates.GATES`; no record edited.

**Design.** Judged on the sentence's main clause (parse root), not on
whether any verb appears anywhere - Entry 25's "Not for argument's
sake, but to learn the answers to those objections which might ... be
made to my statements" has a verb only inside its relative clause.
Two categories: `no_finite_verb`, and `no_subject` (imperatives,
negative imperatives and subjunctives are whole and never flagged).
Parser: spaCy `en_core_web_lg` and `en_core_web_sm`, pinned in
`engine/m1/requirements-sentence-completeness.txt`, kept out of
`engine/m1/requirements.txt` because the m1 suite is hermetic in CI
(no network model fetch - `engine/m1/fk.py`). The tests use hand-built
parse trees; the real parsers are checked on every CLI run against
19 KNOWN_CASES (the real R43 fragments, their accepted fixes, and
whole-sentence shapes), and the run refuses to report on any miss.

**Precision, measured, not assumed.** Every flag hand-read against
the fragment rule, three configurations on the same 257 renderings /
1,149 sentences on main at `7d34e2c`:

| Configuration | Flags | Real fragments | Borderline | Misparse |
|---|---|---|---|---|
| `sm` alone | 62 | 18 | 1 | 43 |
| `lg` alone (with the readings below) | 48 | 20 | 2 | 26 |
| **both must agree (shipped)** | **30** | **18** | **1** | **11** |

The shipped rule flags a sentence only when no parser finds a whole
main clause under any reading: as written, without a dialogue label
("Question:", "Answer:"), and without an opening connective ("For",
"And", "But", ...). Cost of agreement: two real fragments `lg` alone
caught are dropped (`syr.quote.aphrahat-anti-jewish-frame` "A reply to
the Jews, who blaspheme ...", `witt.quote.congregation-of-saints` "As
Paul says: one faith, one baptism, ..."). Precision 18/30 (60%);
recall is not measurable without a hand-read of all 1,149 sentences.

**Fleet counts (shipped rule):** 30 sentences in 20 of 257 renderings;
`no_finite_verb` 25, `no_subject` 5. By world: alx 12 (4 renderings),
desert 10 (8), ijc 3 (3), cappadocian 2 (2), pahc 1, hal 1, don 1;
syr, gallic, rzg, witt 0. Full list:
`engine/m1/reports/sentence-completeness-report-2026-09-24.json`.

**The 18 real fragments**, by shape - several carry the source's own
verbless form, which the fragment rule as written still does not
accept (Mark's `nisibene-death-trembled` ruling, Entry 19, finished a
source ellipsis rather than keep it):
- a verbless inventory, 8 sentences: `alx.quote.couches-and-trenchers-and-bowls`
  ("Silver couches." "Pans and vinegar-dishes." ...);
- exclamation or acclamation: `desert.quote.they-have-taken-away-my-god`
  "Alas!", `ijc.quote.eutropius-right-of-refuge` "Yes!",
  `don.quote.deo-laudes` "Praise to God.", `hal.quote.hail-bethlehem`
  "Hail, Bethlehem, house of bread - ...";
- elliptical answer or report: `alx.quote.timothy-ordinary-questions`
  "Answer: No." (x2), `cappadocian.quote.basil-on-the-doxology-challenge`
  "At another, 'through the Son, in the Holy Spirit.'",
  `ijc.quote.he-held-aloof-for-a-short-time` "...had held back for a
  short time.";
- heading or bare phrase: `pahc.quote.first-concerning-the-cup` "Now
  about the Thanksgiving - the Eucharist.",
  `alx.quote.to-believe-or-disbelieve` "For example, to philosophize or
  not, to believe or to disbelieve."
Borderline (elliptical question, arguably whole idiom):
`desert.quote.antony-not-worsted` "But if you cannot, why trouble me
for nothing?".

**The 11 misparses** (parser error, sentence is whole): "Arsenius,
flee."; "First is gastrimargia, ..."; "From the fear of the Lord comes
healing compunction." and "From compunction of heart springs
renunciation ..." (inverted order); "Antony ... healed not by giving
commands ..."; both `twelve-psalms-by-an-angel` sentences; "At her
instigation, virgins and widows collected together ..."; "Now, faith
in Christ and the sign of the cross trample death down."; "Is
something that is not allowed ... allowed after the blood of many?";
"Her resolve held firmer than anyone would have expected ...".

**Not done here, on purpose:** no record edited (report-only, per the
brief); whether the 18 are re-authored, and whether a source's own
verbless form (inventory, acclamation) is ever an accepted exception,
is not this thread's call.

**Entry 30 — 2026-09-24 (process doc: rendering gates as authoring
birth conditions).** Build thread C, item 3 of the reviewer thread's
brief; PR #483. Docs only; no record, code or participant-facing text
touched. Numbered 30 after Entry 29 (PR #481); Entry 31 (PR #480)
landed on main first and left 30 free.

**Where it lands.** `reference/method/CiC_Record_Native_World_Build_Process_V1.5.md`,
Phase B, "The register bar is a birth condition". The doc is a live
surface under CLAUDE.md "Keep the live/canonical surfaces clean", so
each clause there is the rule only - no ruling numbers, dates,
attributions or log pointers (managing thread's condition, 2026-09-24);
the heading is left as it was. Provenance is here:
- **Fragment rule practice** (from the R43 human reads): the builder
  reads every sentence for its own subject and verb before the record
  leaves authoring, because neither the grader nor FK sees a fragment
  (Entries 20, 25, 26); a readability conflict is solved by splitting
  differently or trimming, never by reopening a fragment (Entry 26).
  The fragment rule names `engine/m1/sentence_completeness.py` (Entry
  29) as a report-only aid that supports the read and never replaces
  it, and says it still flags the source-spoken forms R44 accepts.
- **R44 (source-spoken forms)** - Mark's ruling, 2026-09-24 (~15:00Z),
  answering the question Entry 29 raised. Mark chose this option in a
  select box, so it is recorded as his ruling of that option: *"Interjections
  and answers stay; lists become one sentence; true ellipses get
  finished."* Meaning: an acclamation, interjection or elliptical answer
  the source itself speaks stays as the source speaks it; an inventory
  is rendered as one list sentence; a source sentence cut short
  mid-thought is finished with the verb its structure implies (as
  `syr.quote.nisibene-death-trembled`, Entry 19); a split made during
  rendering that leaves a clause without subject and verb is still a
  fragment. Relayed by the reviewer and managing threads; confirmed by
  Mark directly in thread C's session, 2026-09-24. Applied to Entry 29's
  18 real fragments: "Alas!", "Yes!", "Praise to God.", "Hail,
  Bethlehem, ..." and "Answer: No." (x2) stay; the 8-sentence
  `alx.quote.couches-and-trenchers-and-bowls` inventory becomes one list
  sentence; the rest are reread against the clause. Re-authoring the
  affected records is a separate dispatch, not this PR's.
- **Register rule**, new: everyday modern English; the original word
  stays only where it survives plainly (cappadocian's "Time will fail
  me", Entry 20); otherwise translate to the modern sense. Written as a
  principle, with "Wherefore"/"disjoin" (rzg, Entry 21), "Ever let"
  (hal, Entry 25) and "quickening" (pahc, Entry 26, the round-2 human
  read, which overrode round 1's decision to keep it) as worked cases,
  explicitly not a word list - the doc's register-bar section says no
  banned-word lists exist in this process.
- **Rendering-fidelity gate**, replacing the "not yet registered ...
  once it lands" placeholder: R34's standard (translation, not
  summation); the builder runs the grader at authoring, reads its
  reasoning against `text`, and revises to two consecutive
  "translation" verdicts (the reviewer's item-4 verdict, recorded in
  `rendering_fidelity.py`'s docstring); graders stay report-only and the
  fragment and register rules win where they disagree (Entry 26). A
  persistent grader objection after a full human read is recorded in
  the world's `Open_Gaps_Tracking.md` (CLAUDE.md's standing rule for
  review outcomes; the reviewer kept this line in round 1).
- **R45 (two graders at authoring)** - Mark's ruling, 2026-09-24
  (~15:50Z), chosen in a select box and recorded as his ruling of that
  option: *"Yes, two graders, either flag counts."* Meaning: Haiku 4.5
  and Sonnet 4.6 both run at authoring; a flag from either counts; the
  two-consecutive-runs bar applies to both; Sonnet 5 replaces 4.6 once
  the account can invoke it and the grader study is re-run. Evidence:
  Entry 31 / PR #480's memo (Sonnet 4.6 93% same-flag stability against
  Haiku's 70%; both together caught 46 of 52 fixed defects; under two
  cents per record). Relayed by the reviewer and managing threads;
  confirmed by Mark directly in thread C's session, 2026-09-24.

**Entry 31 — 2026-09-24 (model assignment: rendering-grader study;
voice study blocked at the AWS account).** Thread E, PR #480. Memo:
`Ministry/Operations/Audits/Tech-Readiness-2026-09/Model-Assignment/Model-Assignment-2026-09-24.md`.
Recommendations only; decisions are Mark's.

**Account gate on both target models.** Opus 5.5 and Sonnet 5 are
listed as Bedrock inference profiles in us-east-1 and us-west-2, but
every invocation returns `Error code: 403 - anthropic.claude-opus-5-5
is not available for this account` (the same error for
`claude-sonnet-5`), 2026-09-24. Mark saw the same error for both in
the Bedrock console at about 15:30Z and 15:35Z, as the reviewer thread
reports. What blocks them is the account gate, not the engine.
Invocable: Haiku 4.5, Sonnet 4.5, Sonnet 4.6, Opus 4.5, Opus 4.6
(`engine/provider/reports/model-availability-2026-09-24.json`).

**Study 1 (rendering grader), Sonnet 4.6 standing in for Sonnet 5.**
The R43 labeled set has 69 rows: 52 defects fixed on the grader's
finding, 5 kept as-is, and 12 defects the grader missed and the human
read caught, graded at their round-one commit. Each row was graded
3 times per model through `grade_rendering`, unchanged: 414 calls,
$1.77, 0 failures.
- Haiku 4.5 / Sonnet 4.6, flagged by majority:
  - on the 52, which Haiku selected: 45 / 34;
  - on the 12 misses: 3 / 6, but only 1 / 3 of those name the defect
    the human found;
  - false flags on the 5 kept: 1 / 2.
- Same flag on all 3 runs: 70% / 93%.
- p50 latency 2.2 s / 3.2 s. Sonnet 4.6 went over the 8 s production
  timeout on 2 of 207 calls.
- Cost per call $0.0022 / $0.0064.
- Neither grader caught any of the 4 fragments or 4 archaic-register
  defects. The grader prompt asks only about clause coverage, never
  about grammar or register.

**Study 2 (voice, Sonnet 4.5 vs Opus 5.5): held.** It is blocked by
the 403 above. No voice turn ran and there was no voice spend. The
plan (42 + 3 turns, $12 ceiling, an additive effort / max_tokens
passthrough on `run_turn`) is kept in the memo so it can run
unchanged, after the reviewer's go.

**Open, with Mark:**
1. Whether the authoring-time birth condition becomes two graders
   (Haiku plus a Sonnet-class model, a flag from either counts, human
   read kept). This replaces the single-Haiku "translation on two
   consecutive runs" rule (the reviewer's item-4 verdict, 2026-09-23,
   recorded in `engine/m1/rendering_fidelity.py`).
2. Whether to run the 12-record authoring test: re-author the 12
   round-one-rejected renderings with Sonnet 5 and with Opus 5.5 in
   Claude Code, then grade them blind. This would settle whether
   authoring moves to Opus, which would change a CLAUDE.md usage rule.
   Not started; if approved, it comes back to thread E as a dispatch.

**Entry 32 — 2026-09-24 (the authoring test: 12 renderings, two
authors, blind read).** Thread E, PR #493. Results only; the choice of
authoring model is Mark's.

**What ran.**
- Two fresh subagents re-wrote the 12 renderings that the round-two
  human read had rejected (Entry 31's labeled set).
- Both had one brief, holding each record's verbatim `text` at
  `c057a8c2` and no prior rendering or verdict.
- Their self-reported ids were `claude-sonnet-5` and `claude-opus-5-5`.
- The 24 renderings were blinded A/B per record, with the key sealed
  by SHA-256. The managing thread read them blind before the key was
  opened.
- Files: `Ministry/Operations/Audits/Tech-Readiness-2026-09/Model-Assignment/Authoring-Test-Blind-Read.md`.
  The memo addendum is in the same folder.

**Result.**

| | Opus 5.5 | Sonnet 5 |
|---|---|---|
| Passed the blind read | 12 of 12 | 3 of 12 |
| Preferred, of 10 non-tied records | 9 | 1 |

- Sonnet 5's failures were mostly sentences of about 45 to 90 words.
  The rest were three misleading word choices.
- The graders (Haiku 4.5 and Sonnet 4.6, 3 runs each) flagged 3 Opus
  renderings and 1 Sonnet rendering, the reverse of the human read.
  The graders are not asked about sentence length.

**Spend.** Bedrock $0.63, for the grader runs on the 24 renderings.
They ran under the reviewer thread's brief, before the managing
thread's rule of no new Bedrock spend without a go. The authoring
itself was on session credits.

**Open, with Mark:**
1. The authoring model and the CLAUDE.md usage rule.
2. Three rule questions raised by the reader:
   - voicing an editor's bracketed supplement ("[truly] died");
   - a small restructuring in the Polycrates rendering;
   - dropping a leading "Since" where the excerpt has no main clause.

**Entry 33 — 2026-09-24 (the authoring model: Mark's ruling, a change
order to the CLAUDE.md usage rule).** Closes item 1 of Entry 32's own
open list.

**Ruling: option A of three**, put to Mark directly.
- A — Opus authors every modern-English rendering the voice speaks (a
  quote's `modern_rendering`, and any re-rendering of it); Sonnet
  keeps every other drafting task, per the existing usage rule.
- B — Sonnet keeps authoring renderings, with a hard length check
  added to catch the failure mode directly.
- C — Sonnet drafts renderings and Opus fixes whatever a review round
  finds wrong with them.

**Mark chose A.** `CLAUDE.md`'s "Usage/credit discipline" section
gains one bullet, directly after the existing "Opus is for the final
adversarial-review gate only" line, as plain rule text: modern-English
renderings the voice speaks are authored by Opus; everything else
still drafts on Sonnet.

**Evidence.** The authoring test (Entry 32, this file):
`Ministry/Operations/Audits/Tech-Readiness-2026-09/Model-Assignment/Authoring-Test-Blind-Read.md`.
Opus 5.5 passed the blind read on 12 of 12 renderings; Sonnet 5 on 3
of 12. Sonnet 5's failures were mostly sentences of about 45 to 90
words, plus three misleading word choices.

**The test's limits.** 12 records, one authoring run per model per
record - not a large sample, and not repeated. The graders (Haiku 4.5,
Sonnet 4.6) missed most of what the human blind read caught, so the
result rests on the human read, not on an automated score.

**Scope.** This changes authoring of modern-English renderings only
(a quote's `modern_rendering` and any re-rendering of it). Every other
drafting task - records, intermediate review rounds, documentation,
build work - stays on Sonnet, per the existing rule.

**Entry 34 — 2026-09-24 (fleet-wide quote re-verification: results, one
real checker fix, five already-resolved).** A full re-run of the
quote-verbatim sweep (`engine.m1.quote_verbatim`, `verify_quote_record`)
across every `records/*/quote/*.md` in all 12 world directories - not
only the `fix` world-report's usual `REPORT_WORLDS` list, which omits
the `fix` fixture world (included here; its 3 quote records all pass):
260 checked, 254 verified, 6 failed - the same six the 2026-09-22 report
(`engine/m1/reports/quote-verbatim-report-2026-09-22.json`) already
named. Investigated each by hand against the vendored files directly,
per the brief's own rule: never invent or reconstruct a quote; a
record's `text` must match its source exactly, or stay flagged.

**What the investigation actually found, against the brief's own
assumption that all six needed fresh work:** five of the six had
already been fully investigated and correctly resolved by an earlier
thread on 2026-09-22, each with its own honest, dated divergence_note
already in the record, several explicitly "flagged for Mark... not
resolved further here." Re-verifying each by hand confirmed the earlier
work was right, not incomplete:
- `desert.quote.good-good-i-dont-mind` and `hal.quote.hindered-by-
  jerome` (Palladius, `palladius_lausiac-history_clarke1918.txt`): the
  record's own wording is correct; two bare endnote numbers ("163",
  "164") and a digit glued to a comma ("Paula,276") are footnote
  artifacts with no safe edition-wide rule (the endnote sequence
  desyncs against page/chapter numbers well before reaching these -
  confirmed by direct inspection, not assumed) - already
  `verified-via-authority`, already tested
  (`test_palladius_bare_digit_footnotes_are_verified_via_authority_not_gate`,
  `test_palladius_paula_comma_footnote_is_verified_via_authority_not_gate`).
- `ijc.quote.ammianus-roman-luxury` (`ammianus-marcellinus_roman-
  history_yonge1862.txt`): the record's English is correct; the
  vendored djvu OCR scan itself is corrupted at this exact passage
  ("vastuess" for "vastness", "east" for "cast", "sober-mirfded" for
  "sober-minded") - already disclosed and independently re-checked
  against the raw scan on 2026-09-22, already `verified-via-authority`.
- `don.quote.donatus-quid-est-imperatori` and `don.quote.emeritus-
  magno-argumento`: both Latin quotes are absent from the file
  originally cited (one carries only the English translation, the
  other only a different, unrelated locus) but present, OCR-corrupted,
  in a second vendored file each record's own `sources[]` already adds
  (Ziwsa's critical edition; the Migne PL11 scan) - already re-located,
  already given in corrected standard orthography rather than either
  the wrong file's content or the raw OCR string, already
  `verified-via-authority`, already flagged for Mark.

None of these five needed a text, locus, or verification_state change
today - doing so would either be a no-op or, worse, would mean
reconstructing wording to force a mechanical match, which is exactly
what "never invent" forbids. They are not new debt; they are the same
five items already sitting in each record's own divergence_note,
unchanged.

**The one genuine, actionable gap: `cappadocian.quote.basil-on-common-
life`.** Hand-confirmed against `basil_ascetic-works-longer-shorter-
rules_clarke1925.txt`: the record's own wording is correct, but the
passage carries three separate divergences from the raw scan, not the
one the brief assumed:
1. a bare footnote-reference digit with no wrapper ("common 1 is") -
   genuinely a checker-grammar gap, now fixed;
2. a stray extraction-artifact opening quotation mark before "To
   begin," with no closing mark anywhere in the passage - not fixed
   today, left as a known, already-disclosed item;
3. "Tor just as" for "For just as" - a genuine word-level OCR misread,
   not a marker.

Fixed only item 1, as a new per-edition apparatus entry in
`cic/texts/REGISTRY.yaml` (`bare-footnote-digit-common-is`), anchored
on both sides to the literal words "common" and "is" rather than to
the bare-digit shape - the module's own docstring already rules out a
FLEET-WIDE bare-digit class as unsafe (other editions quote real digit
quantities as content) and prescribes exactly this per-edition
apparatus mechanism as the correct resolution path; this entry follows
it. Checked the whole file first: the literal substring "common 1 is"
occurs exactly once, and a blanket "digit between two words" pattern
would hit 126 places - confirming the literal-word anchor, not a
general digit rule, is what makes this safe. `engine/m1/tests/
test_quote_verbatim.py` gained three tests: the entry strips exactly
the evidenced marker; it does not mask a different digit or a real
word at the same position; and the record's first sentence now
verifies in isolation. The existing
`test_bare_unwrapped_footnote_digit_is_not_silently_tolerated` still
passes unchanged - it tests the fleet-wide mechanism only, which this
change never touches.

**Item 2 (the stray quotation mark) is deliberately not fixed today.**
It is a real, single-occurrence, evidenced artifact, and could probably
take the same narrow-anchor treatment as item 1. It is left alone here
because item 3 already means this record cannot pass the mechanical
check regardless - fixing item 2 today would not change the fleet
sweep's result, so it stays out of scope rather than being done for its
own sake in the same pass as item 1.

**Fleet count, before and after, as asked:** 254/260 before this PR's
one apparatus entry; **254/260 after** - unchanged. This is the correct
result, not a failed fix: item 1's own fix is real and independently
verified (the record's first sentence, containing the digit, now
verifies against the real file in isolation - see the new tests), but
`cappadocian.quote.basil-on-common-life` was never going to flip to
fully verified from that fix alone, because of item 3 above (a genuine
word substitution, which this module's own ruling says must never be
maskable by any apparatus mechanism, on purpose). The brief's own
premise - "confirm... the only difference is the bare footnote digit"
- does not hold; reported here rather than silently fixed around.

**No record text, locus, or verification_state changed.** No package
rebuild or repin was needed - nothing in `records/` changed, only the
corpus-map apparatus definition and the engine's own test suite.
`python3 -m pytest engine/m1/tests -q` (156 tests, includes the 69-test
`test_quote_verbatim.py` file) and `python3 -m engine.m2.cli
staleness-check` both pass clean.

**Entry 35 — 2026-09-25 (three rendering fixes: a bracketed supplement,
a broken reason-to-conclusion tie, a truncated excerpt).** Applies
Mark's two rendering-bar rulings from the authoring-test follow-up: (1)
the voice never speaks a translator's own bracketed supplement, and the
bracket stays in the verbatim `text` field; (2) sentences may split
freely, but where the original ties a reason to a conclusion, the
rendering keeps the tie with a plain linking word. `modern_rendering`
was authored by Opus throughout (per the new CLAUDE.md usage rule,
Entry 33) - this session is Sonnet, so a fresh Opus subagent drafted
all three, reviewed here against both rulings, this project's own FK
target, and source fidelity before anything was applied.

**`pahc.quote.ignatius-truly-born` (Trallians 9).** The vendored
edition prints "[truly]" in brackets before "died" - the translator's
own supplied word; every other "truly" in the passage (born,
persecuted, crucified, raised) is unbracketed, original. The prior
rendering voiced all five as equally certain. Fixed: the rendering no
longer asserts the bracketed one; the other four - the actual
polemical point, a direct denial of a rival teaching that Christ's
body only seemed real - are unchanged. `text` field untouched (the
bracket was already correctly preserved there). FK grade 4.46, longest
sentence 17 words.

**`pahc.quote.polycrates-to-victor`.** The source's own grammar makes
his age (sixty-five), his travels ("in all parts of the world"), and
his reading ("through all Holy Scripture") the stated grounds for "am
not frightened" - a relative clause feeding one main verb, not four
separate facts. The prior rendering split them into disconnected
sentences with no linking word, losing that tie. Fixed with "So I am
not frightened..." Every other clause checked against rule 2
separately; no other real reason-to-conclusion tie in this passage was
broken. `text` field untouched. FK grade 5.99, longest sentence 21
words.

**`alx.quote.the-grades-here-in-the-church` (Stromateis VI.13).** The
`text` field stopped at "...according to the Gospel" - the end of a
"Since..." clause with no main clause of its own in the record: a
truncated excerpt, not a wording choice. Found the full sentence in the
vendored file (near line 47889) and extended `text` verbatim through
"...till they grow into 'a perfect man'" - the sentence the "Since"
clause was actually grounding, completing the thought that the
church's ranks mirror a progression, not only a static hierarchy.
Re-verified against the vendored file directly
(`engine.m1.quote_verbatim.verify_quote_record`): `True`, classes
`bracket` (the source's own "[as deacons]", not carried into the
rendering per rule 1), `whitespace`, `punctuation` (curly vs. straight
quotation marks). `locus` updated with a line reference.
`modern_rendering` rewritten to cover both sentences, and rendering "a
perfect man" (Clement's own allusion to Ephesians 4:13) as "full
maturity" rather than literally - the literal cognate would mislead a
modern reader into hearing a claim about becoming an adult male, which
is not what the phrase means. FK grade 7.33, longest sentence 21 words.

**Corrected the tie's own direction (same day, managing-thread
verdict on PR #531).** The first drafted rendering joined the two
sentences with "That is why" - a consequence reading, first sentence
causing the second. The source's own "For" makes the second sentence
EVIDENCE for the first sentence's claim, not something that follows
from it: the ranks mirror the angelic economy - *for* [proof:] those
taken up do in fact progress through it. "That is why" pointed the
tie backward. Corrected to "For those taken up in the clouds...",
keeping the author's own direction, per Mark's splitting rule (the tie
must be kept, in the direction the original actually argues, not just
any linking word). Re-verified: `True`, same classes. FK grade
unchanged at 7.33; longest sentence 21 words (was 23, since "For" is
shorter than "That is why").

**Checks.** `engine.m1.quote_verbatim.verify_quote_record` on all three:
verified `True`. `python -m engine.m1.gates` (via `gates.run_all`) on
`pahc` and `alx`: `alx` clean; `pahc`'s 2 `reciprocity` findings are the
same pre-existing, unrelated baseline count confirmed against this
branch's own unmodified base - not new. `python3 -m pytest
engine/m1/tests -q`: 156 passed. `python3 tools/check_paths.py
--baseline tools/check_paths_baseline.txt`: 0 new unresolved citations.
Packages for `pahc` and `alx` rebuilt and repinned on the corrected
content; determinism-check and staleness-check both pass.

All three FK grades sit below the CLAUDE.md target band's floor (8-10),
not above its ceiling (`engine/m1/gates.py`'s own enforced
`FK_CEILING = 10`) - reported as such rather than adjusted upward for
its own sake. This matches, not contradicts, this world's own prior
"BAR SWEEP" ruling on `pahc.quote.polycrates-to-victor` itself
(2026-08-29, Mark: "much better thats the bar" -
`Ministry/Technology/CiC_Register_Bar_2026-08-29.md`): short sentences
and everyday words were the explicitly approved style for these
renderings before this entry, not a defect this entry introduces.

**Entry 36 — 2026-09-25 (Entry 35's rendering fixes left pahc's site
JSON stale; rebuilt and re-pinned).** Entry 35's record edits (merged
as PR #531) changed `records/pahc/quote/pahc.quote.ignatius-truly-born.md`
and `records/pahc/quote/pahc.quote.polycrates-to-victor.md`, and the
same branch repinned the `pahc`/`alx` packages (`engine.m2.cli`) - but
never rebuilt `cic-website/data/worlds/post-apostolic-house-church.json`,
the separate world_front-compiled site JSON (`engine.m2.site_cli`).
`python -m engine.m2.site_cli staleness-check` on `origin/main` found
`pahc` stale (`diff: ["narrative"]`); `alx` was not stale (its own site
JSON has no world_front content touched by Entry 35's fix). This
surfaced as promotion PR #533's "Site staleness sweep" check failing.

**Fix.** `python -m engine.m2.site_cli build pahc --records-commit
a9f9f97f --compiler-version cic-m2-site-compiler-2` - `a9f9f97f` is the
commit that actually made the record content edit (matching this
project's own established re-pin convention of citing the content
commit, not a merge commit or the repin commit itself; confirmed
against the immediately preceding pahc re-pin, `aad6c76f2`, which cited
its own parent content commit `5a151112` the same way). Compiler
version held at `cic-m2-site-compiler-2`, unchanged. Verified the
rebuilt JSON actually carries the fix (Polycrates' added "So" appears;
Ignatius' legitimate "truly born" is retained while the bracketed
"[truly] died" supplement stays dropped from the rendering, matching
Entry 35's record). `engine.m2.site_cli staleness-check` and
`engine.m2.cli staleness-check` both pass clean across every world;
`engine/m2/tests/test_site_compiler.py` and
`test_site_staleness.py` (20 tests) pass.

**Why PR #531's own CI didn't catch this - correction.** It did catch
it: "Site staleness sweep (world_front-compiled JSON)" ran on the PR's
final head commit (`49ceae78`, ~1 minute after that commit was pushed)
and reported `conclusion: failure` - confirmed directly from GitHub's
check-run API, not inferred. The PR was merged anyway 23 minutes later,
with that check still red. So this was not a CI blind spot; it was a
failing, correctly-firing check that did not block the merge - a
branch-protection gap (this repo does not require "Site staleness
sweep" to pass before merging to `main`), which is a distinct and more
serious defect than a check that never ran. Fixing it means a repo
branch-protection setting change, a portfolio-level/infra decision this
entry does not make on its own - flagged to Mark rather than actioned
here.

**Entry 37 — 2026-09-25 (source-form fragment re-author across six
worlds).** Re-authors the `modern_rendering` values that Entry 29's
sentence-completeness check flagged as real fragments, under Mark's R44
ruling of 2026-09-24: "Interjections and answers stay; lists become one
sentence; true ellipses get finished." (now in the process doc, Phase B).
One PR per world; only `modern_rendering` changes, every protected field
byte-identical, confirmed by a front-matter diff. Every rendering authored
by Opus and graded with Haiku 4.5 and Sonnet 4.6, two runs each.

**Re-authored (7 records, 6 worlds):**
- alx `couches-and-trenchers-and-bowls` (list): whole short sentences, by
  Mark's direct ruling for this record on 2026-09-24 ("Option 1"), because
  the one-sentence list scores FK 41.7 and fails the live readability
  gate. The closing sentence keeps the source's reason tied to its verb
  ("They are to be given up because there is nothing at all in them worth
  our trouble"), per the independent fidelity review. The process doc's "one list sentence" does not yet say what
  happens when a list cannot pass the readability gate as one sentence;
  flagged to Mark as a methodology question, not changed here.
- alx `to-believe-or-disbelieve` (split fragment): re-split with an
  imperative for the source's "say" to keep FK under 10.
- cappadocian `basil-on-the-doxology-challenge` (split fragment):
  "at one point ... and at another ..." rejoined.
- ijc `he-held-aloof-for-a-short-time` (true ellipsis): finished with the
  implied subject, "He had held back ...".
- pahc `first-concerning-the-cup` (split heading): rejoined as one
  imperative sentence.
- syr `aphrahat-anti-jewish-frame` (verbless heading, caught only by the
  larger parser): finished, "This is a reply against the Jews ...", which
  also restores the source's "against" (the old rendering had "to").
- witt `congregation-of-saints` (verbless quotation, caught only by the
  larger parser): "As Paul says, there is one faith ...". Haiku's first
  objection also found real drift elsewhere in the rendering ("saints"
  and "etc." dropped, "instituted by men" weakened); fixed in the same
  field.

**Stays as the source speaks it:** desert "Alas!", ijc "Yes!", don
"Praise to God.", hal "Hail, Bethlehem, ...", alx "Answer: No." (x2),
and desert `antony-not-worsted` (the source's own elliptical question).
The 11 misparses need no change.

**Grader disagreements, recorded in each world's
`Open_Gaps_Tracking.md`:** syr (Haiku reads the finished heading as
expansion; Sonnet reads translation) and witt (Haiku reads summary and
names clauses the rendering carries; Sonnet reads translation). The
fragment rule wins on syr; the human read of every clause stands on witt.

**Counts (sentence-completeness check, fleet):** 30 flagged sentences
before, 18 after: the 11 misparses plus the 7 source-spoken forms kept.

**Entry 38 — 2026-09-25 (embedded-quotations check, `engine/m1/
embedded_quotations.py`, registered as a standing report-only check).**
OG-10 (`worlds/pahc/Open_Gaps_Tracking.md`) named three mechanism
options for the embedded old-translation quotation gap this module
finds and counts: (A) a schema extension, (B) extracting each embedded
quote that matters into its own `quote` record with an Opus rendering,
(C) registering the existing report-only module as a standing check.
Mark's ruling, relayed 2026-09-25: **"c+b"** - both C (this entry) and B
(a separate, batched workstream, not this thread's own work) adopted;
A (the schema extension) not taken up.

**Registered exactly as `engine/m1/sentence_completeness.py` already is
(Entry 29 above)**: report-only, not added to `gates.GATES` or
`gates.run_all`, never fails a build. `python -m engine.m1.
embedded_quotations` writes `engine/m1/reports/embedded-quotations-
report-<date>.json` and prints a per-world summary - the same shape
`sentence_completeness`'s own CLI already uses. No code changed by this
entry: the module has carried this exact report-only shape since it was
built (`worlds/pahc/Open_Gaps_Tracking.md` OG-10's own build history);
this entry is the formal registration, establishing it as a recognized
standing check for whoever runs a build to invoke and read, the same
governance step Entry 29 already gave `sentence_completeness`.

Option B (extracting the quotations this module finds into real `quote`
records, each with its own Opus-authored `modern_rendering`) is
explicitly not this entry's own work - a separate, batched workstream
covering the fleet's 198 flagged records, reported when it opens.

**Entry 39 — 2026-09-25 (R46: long-list exception to R44).** Answers the
methodology question Entry 37 flagged and left open: R44's "one list
sentence" rule doesn't say what happens when a list cannot pass the
readability gate as one sentence — the exact case `alx
couches-and-trenchers-and-bowls` hit (Entry 37: the one-sentence list
scores FK 41.7 and fails the live readability gate).
- **R46 (long-list exception to R44)** — Mark's ruling, 2026-09-25,
  Decision 5, option "a". Mark's approved wording: *"A list stays one
  sentence unless that sentence would pass about 25 words. Then it splits
  into a few list sentences grouped as the source groups them (e.g.
  tableware, furniture, bedding), keeping the source's order and every
  item. The source's own verdict closes it. There is no filler connective
  repeated sentence after sentence."* Landed in
  `reference/method/CiC_Record_Native_World_Build_Process_V1.5.md`, Phase
  B, next to the existing list-rule sentence — rule only, no ruling
  numbers, dates, attributions or log pointers in that live surface, per
  Entry 30's own convention for it. Mark's standing bar, restated
  alongside this ruling: scholarly rigor a professor of church history
  would be impressed by, not 100% perfection.
- Re-authoring `alx couches-and-trenchers-and-bowls` under R46 is a
  separate dispatch, not this entry's - it merged as PR #566, ahead of
  this rules PR, and carries no Decision-Log entry of its own.

**Entry 40 — 2026-09-25 (R47: ellipsis-finishing takes precedence over
the bracketed-supplement rule where the two collide).** Settles the
precedence between "true ellipses get finished" (2026-09-24, in the
process doc's Phase B) and "the voice never speaks a translator's own
bracketed supplement" (Entry 35, 2026-09-25): where finishing a true
ellipsis needs the exact word a vendored edition supplies in brackets,
using that word is not voicing the translator's own addition, because
the sentence's own structure requires it — the bracket marks where the
edition supplied a needed word, not an optional editorial one.
- **R47 (ellipsis-finishing vs. bracketed supplement)** — Mark's ruling,
  2026-09-25, Decision 6, option "a". Mark's approved wording: *"Where
  finishing a true ellipsis needs the very words an edition supplies,
  the rendering may use them. The words are there because the sentence
  needs them, not because a translator added them."* Landed in
  `reference/method/CiC_Record_Native_World_Build_Process_V1.5.md`,
  Phase B, next to the existing ellipsis-finishing sentence — rule
  only, no ruling numbers, dates, attributions or log pointers in that
  live surface, per Entry 30's own convention for it.
- **Worked case (not itself changed by this entry):** `syr.quote.aphrahat-anti-jewish-frame`'s
  current rendering, "This is a reply against the Jews, who blaspheme
  the people gathered from among the Gentiles," stands — its finished
  "This is" matches the edition's own supplement, per
  `worlds/syr/Open_Gaps_Tracking.md` #14. No record is touched by this
  entry; a separate change is coming for it.
