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
