# Cross-System Analysis — Standing Thread Tracking

Running, dated ledger for the Cross-System Analysis thread. Same discipline as
System Health's own `CiC_System_Health_Tracking.md`: dated entries, honest
status, root cause over symptom, what was measured and how. This file is the
durable record of what this thread found and did; no finding, fix, or
escalation lives only in a session's own conversation history.

---

## Thread scope (established at thread launch, 2026-09-04)

This thread owns defects that cross every world and every task thread's
bounded view — a voice speaking wrongly in all seven worlds, a retrieval or
grounding behavior wrong everywhere, a schema or convention drifting apart
across the fleet, a check that was written down and never built, a fix
applied in one world that should have been applied in all. Root-cause and fix
fleet-wide; close with a mechanical gate so the defect can't come back.

**Not this thread's:** repo-wide CI/deploy/build/config (System Health);
source acquisition and `cic/corpus-map/` (Library Build Engine); a single
world's own substantive content, which stays that world's own thread's and
Mark's call even when this thread finds and reports a defect in it. Not a
governance or methodology authority.

---

## 2026-09-04 — First assignment: Representative voice speaking from outside its own historical horizon

**Base freshness confirmed before starting.** `git fetch origin`; working
branch was created from `origin/main` tip `ad8ecce1` with 0 commits ahead/behind
at session start — verified via `git rev-list --count` both directions before
any census work.

**Collision check.** Read `CiC_System_Health_Tracking.md` in full (current
through 2026-09-04's scheduled sweep) — its open items are Cloudflare/Workers
Build config and PR #11/#10 staleness, none touching `records/`,
`engine/m2/builders.py`, or the Register Bar/Birth Conditions documents this
assignment concerns. No other Standing tracking doc for a world thread exists
yet to check against. No collision found; noting here per the coordinate-
before-fleet-wide-edit rule so the next thread that touches these paths can
see this thread was here first.

### What the defect actually is

Mark's framing, confirmed in interview: this is not a grammar problem. The
Representative's voice sometimes speaks from a vantage point outside its own
world's historical present — describing itself, its own community, and its
own record the way a builder describes a world from outside, not the way an
inhabitant of it would. "Our own Christian tradition" or plain "we" is
correct; "this world" (a builder's label, never an inhabitant's) is not.
Three textual forms carry this, and this assignment is bounded to those three
(the broader "future/outside-vantage" class — anachronistic terminology,
forward-referencing statements, reader's-eye comparisons — is real but is
follow-on scope, logged at the end of this entry, not attempted here).

### Field scope — proven, not assumed

Before counting anything, traced exactly which record fields the runtime
actually turns into the Representative's own speech, via
`engine/m2/builders.py`'s `_chunk_text()` and `build_prompt()`:

- **Voice-reproduced (in scope):** `term.plain_meaning`, `term.quick_meaning`,
  `story.tellable_as`, `story.text`, `ambient.detail`,
  `doctrinal_witness.text`, `honest_limit.statement`,
  `demonstration.exchange[].text` where `speaker: representative`.
- **NOT voice-reproduced, confirmed by code and by the records' own stated
  constraint (excluded):** `world_core.*` (horizon/formation_logic/
  thinness/cautions/thin_topics) — built via `emit()` as "records of the
  world" fed to the model as background, and `cappadocian.core.cappadocian.md`
  states explicitly "No Representative content appears in this record"; every
  `world_core` record sampled is written in a scholarly third-person register
  on purpose. `voice_craft.*` (identity/guard/concerns/notes) — built via
  `instruct()`, already first-person "we"-form standing instruction.
  `retrieval.retrieve_when`/`do_not_retrieve_when` — builder-facing retrieval
  hints, never compiled into the prompt at all. `term.senses`/`false_friend` —
  not touched by either builder function. `quote.text` — licensed verbatim,
  never edited under any circumstance. `gravity`/`force`/`contested_claim` —
  analytical types (`_ANALYTICAL_TYPES`), only a bare name+id reaches a
  "Gravities" index, never the record's own descriptive text. The free
  markdown body below each record's `---` fence — "provenance and build
  notes — never read by any builder" per Artifact-1 SS1, confirmed not
  compiled anywhere.

This resolves the brief's own open question ("distinguishing the fields the
voice reproduces from the fields it reads is the whole substance of the
problem") with code evidence, not assumption.

### Census — three forms, measured against that field scope, on records/ at origin/main tip ad8ecce1

**Form 1 — literal "this world" (+ possessive).** 252 raw regex hits across
167 fields, all 8 worlds. Hand-checked every non-lexicon hit (166 instances)
plus swept all hits for the two known-correct exception shapes named in the
brief (scriptural/cosmological "of this world"; anti-Marcionite "Maker of
this world"). Found exactly **2 genuine exceptions**, both verified against
source, not assumed:
- `syr.dw.god` — "the Maker of this world is the Father of Jesus" — anti-
  Marcionite cosmology, the brief's own named exception shape.
- `pahc.story.grandsons-before-domitian` — "it was not of this world...but
  belonged to heaven" — a close paraphrase of Hegesippus (verified against
  the vendored source, anf08 line 71558) echoing the ordinary scriptural
  sense ("my kingdom is not of this world"), not self-reference.

**Genuine Form 1 total: 250 instances, 166 fields, all 8 worlds:**
alx 27, cappadocian 73, desert 3, hal 58, ijc 28, pahc 6, syr 54, fix 1.
(Not the brief's inherited 190/44 — re-measured per instruction; the
difference is explained below, not asserted.) **86 of the 250 (34%) are in
`term.plain_meaning`/`term.quick_meaning`** — i.e. the lexicon/glossary
fields, concentrated almost entirely in cappadocian (53 of cappadocian's 73).
Sampled cappadocian's term records directly: nearly every entry opens "This
world taught/held/used/believed..." — a systematic authoring pattern, not
scattered error. Cross-checked against the record's own declared stance
(`register` field): every one of these is `register: emic` (insider stance),
so the pattern contradicts the record's own declared intent — this is not a
register where third-person description is the intended reading. (Fleet-wide,
only 3 of 478 in-scope records are `register: etic`/`emic-unavailable`; none
of the 3 appear in the Form-1 hit list, so this exception category turned out
moot for the actual measurement, not just theoretically excluded.)

**Form 3 — bare "the world" as self-noun.** 25 raw candidates. Hand-classified
every one (none deferred to a list): 20 are genuine exceptions — the ordinary
generic/cosmological/geographic sense ("the world is fallen," "entered the
world," "across the world," "the end of the world," direct embedded quotation
from Hermas) — and 5 are the real defect, all following the same "[X]'s own
Y" self-referential-possessive shape seen everywhere in Form 1, just missing
the word "this": `alx.dw.councils`, `alx.dw.empire`,
`cappadocian.story.athens-friendship`, `hal.story.attack-416`,
`ijc.story.tome-that-would-not-bend` (this last one confirmed by the same
record's own `text` field independently using "This world's record ends...,"
i.e. the same record commits both forms). One borderline case
(`cappadocian.story.julian-schools`, "the world's fury at him") resolved as
exception — Julian's reputation was reviled fleet-wide in late antiquity, not
Cappadocia-specifically, so "the world" reads as the ordinary universal sense.

**Genuine Form 3 total: 5 instances, 5 fields** — genuinely the "third,
smaller form" the brief anticipated, not a large undercounted class.

**Form 2 — third-person it/its referring to the world.** Built and tested a
tiered method rather than trusting a blind "it" search, per the interview
agreement:
- **Tier A (high-confidence):** sentence-initial "It"/"Its" immediately
  following a sentence whose literal subject is "this world"/"the world" — a
  mechanically checkable anaphora chain. **24 instances, 23 fields**, spot-
  checked and all genuine (e.g. `alx.dw.church-failure`: "This world's record
  leaves its wounds visible. Its greatest teacher was...").
- **Broader candidate pool:** every field containing a Form-1/3 hit, every
  sentence in it containing "it"/"its" anywhere (not just sentence-initial):
  413 candidate sentences, 133 fields — close to the brief's inherited 152,
  confirming that number was very likely this same raw, unfiltered pool, not
  a curated true-positive count.
- **Precision-tested that pool** with a random 40-sentence sample (seed 42,
  reproducible): roughly **13–16 of 40 (35–40%) are genuine** — "it"/"its"
  actually referring to the world/community as a whole, in the same
  self-referential-outside-vantage sense as Form 1. The rest are ordinary,
  correct English that a blind pattern would have wrongly flagged: dummy/
  cleft "it" ("What is it you..."), "it" referring to some object the world
  produced (a record, a letter, an argument, a practice, a term being
  glossed) rather than to the world itself, and third-person reference to a
  narrower named entity (a city, a family, "the tradition") that is
  ordinary English even from an insider and not the vantage defect Mark
  named. This 35–40% precision is the concrete evidence for why the brief's
  152 cannot be reported as a trustworthy count of the actual defect without
  this filtering — exactly the failure mode the census discipline exists to
  catch.
- **Honest current state:** Tier A (24/23) is a solid, defensible floor.
  Applying the sampled ~37% precision to the 413/133 pool projects roughly
  **130–160 genuine instances across perhaps 60–90 fields**, but that is an
  estimate from sampling, not a count, and is reported as such. Getting an
  exact number means either a full hand read of the 133-field candidate pool
  (bounded, ~half a day of careful reading) or a review pass over that same
  pool — not a live/billed model call, since this is analysis of existing
  text, not generation. **Not done this session** — flagged as the next
  concrete step before Form 2 can be fixed with the same confidence Forms 1
  and 3 already have.

### Root cause — traced to the actual authoring mechanism, not just the records

Per Mark's direction ("the system should generate the right conversation, not
generate and tweak"), traced this past the records themselves to where the
defect is actually produced:

1. **The correct standard already exists and is followed correctly where it
   is checked.** `Ministry/Technology/CiC_Register_Bar_2026-08-29.md` names
   `records/syr/demonstration/syr.demo.room-for-doubt.md` as "the ONE
   approved sample" every spoken sentence is drafted against. Read it in
   full: flawless first-person "we/our/us" throughout, zero third-person
   self-reference. The standard is not broken.
2. **But the bar's own documented properties never name perspective as one of
   them.** The Register Bar document lists exactly what "the bar" means:
   word simplicity, sentence length, paragraph count, honest-limits framing.
   Perspective/self-reference is never named as a property to hold spoken
   fields to, even though the one approved exemplar demonstrates it
   throughout. The only automated measurement named anywhere in the pipeline
   (M7: FK/FRE + cadence, "visibility, no gates") checks readability, not
   perspective.
3. **G3, the one human gate that reads spoken-field quality** (`CiC_New_World
   _Build_Record_Native_Launch_V2_2026-08-30.md`), reads "a curated sample of
   spoken fields... against the approved sample," checking whether Mark "has
   to re-read" a sentence — a readability/clarity test by its own stated
   criteria, not a perspective test, and a sample, not an exhaustive read.
   Third-person "this world taught X" is plain, simple, easy-to-read English
   — it would cleanly pass G3's own stated bar while still carrying the
   defect.
4. **No mechanical gate anywhere checks this.** Grepped `engine/m1/gates.py`
   for anything related to self-reference, perspective, or register content
   (as opposed to register-the-envelope-field, which is a different, unrelated
   sense of "register" in the schema) — nothing. This is the gate gap the
   brief's method predicts should exist before any fix: a defect that was
   never even written down as a rule, let alone gated.
5. **Why lexicon terms are the worst offender:** per the Record-Native Build
   Process's model-routing policy, lexicon discovery/development (Doc_03/
   Doc_06 — the source of `term.plain_meaning`) runs as a **Fable subagent**,
   separately from demonstration/witness authoring. The demonstration
   exemplar (also Fable-authored, per the same policy) is flawless; the term
   glossary drifted into an encyclopedic/dictionary third-person register
   distinct from it — plausibly because a glossary-definition register reads
   as natural to a model even under "write in-voice" instruction, absent an
   explicit rule naming perspective. This is a hypothesis consistent with the
   evidence (concentration in `term.*`, register:emic declared but violated,
   no gate catching it) but not itself independently confirmed against the
   actual generation prompts used at term-authoring time — noted as the one
   piece of the root-cause chain that is inference rather than direct
   evidence.

### Proposed fix shape (not yet executed — pending Mark's confirmation)

Following the Register Bar's own precedent for exactly this situation (its
own "no-fix-on-fix ruling": fix at the record layer, measured against a named
exemplar, base conditions generate it correctly going forward rather than
prompt-rule accretion):

1. Extend the Register Bar / Birth Conditions documentation to name
   first-person, in-horizon perspective as an explicit bar property, citing
   the exemplar's own already-correct behavior as evidence it's achievable
   without new instruction-accretion.
2. Add one new M1 gate, selftest-proven against `fixtures/seeded_defects.yaml`,
   scanning exactly the voice-reproduced field set proven above for the three
   forms, with the two proven exception shapes (scriptural/cosmological "of
   this world," anti-Marcionite "Maker of this world") built in as tested,
   provable exceptions — not a banned-word list, per the Register Bar's own
   standing objection to that shape of rule.
3. Regenerate the actual defective fields at the record layer through the
   corrected mechanism (the same Fable-subagent authoring path, corrected),
   not hand-patched — consistent with both Mark's system-level-fix ruling and
   the Register Bar's own precedent for how this project fixes voice-quality
   drift. This is billed model spend and stops for Mark's explicit go-ahead
   before running, per standing rule.

**Status: census complete for Forms 1 and 3 (proven exceptions, final
counts); Form 2 has a solid high-confidence floor (24/23) and a sampled
estimate (~130–160/60–90) but not yet an exact count. Root cause identified
and evidenced.**

### Documentation and gate work — done, 2026-09-04 (same session)

Mark's direction after the census report: proceed with documentation and the
gate, hold the actual fleet-wide record regeneration for separate approval.

**Field scope, coded, not just reasoned about.** `engine/m1/gates.py` gained
`_PERSPECTIVE_FIELDS`, the literal field map proven above
(`term.plain_meaning`/`quick_meaning`, `story.tellable_as`/`text`,
`ambient.detail`, `doctrinal_witness.text`, `honest_limit.statement`, plus
`demonstration.exchange[].text` for `speaker: representative` turns handled
separately) — so the gate's scope is the same proven trace as the census, not
a second, independently-drifting guess at it.

**New gate: `gate_voice_perspective`, registered as `voice-perspective` in
`GATES`.** Three checks, precision documented at each, matching the census's
own findings:
- literal "this world[,'s]" (Form 1), the two proven exceptions
  (`_MAKER_OF_THIS_WORLD`, `_NOT_OF_THIS_WORLD`) built in as fixed idioms,
  not a growing word list — same standing as several other gates' own narrow
  regex exceptions.
- "the world's..." possessive (a narrowed Form 3 — literal possessive only,
  not the full bare-noun form, since a blind "the world" search runs only
  ~20% precision per the census; the possessive-only form runs ~70%,
  documented in the gate's own docstring as worth a human read, not a
  confirmed finding on its own).
- the Tier-A it/its chain (Form 2's high-confidence floor only — sentence
  immediately after a literal "this/the world" subject sentence — not the
  broader ~37%-precision pool, for the same reason: the codebase's own
  established norm, per `gate_no_build_attribution`'s own field-scoping
  comment, is not to drown real findings in noise).

Sentence splitting reuses `engine.prose.quote_aware_sentences` (already the
shared primitive `engine/m2/builders.py`, `engine/m4/evidence.py`, and
`engine/m1/canon.py` all use) rather than a new one-off splitter.

**Selftest-proven**, per the fixture discipline `fixtures/README.md`/
`Build-Blueprint.md §5 stage 0.6` establish: added
`voice-perspective-third-person-self-reference` to
`fixtures/seeded_defects.yaml`, one mutation on
`records/fix/doctrinal_witness/fix.witness.who-is-jesus.md`'s `text`
exercising both the literal-phrase and it-chain checks together (the same
one-mutation-hits-two-patterns shape `no-build-attribution-leaked-ruling`'s
own seeded defect already uses). Running the gate against the **clean**
fixture surfaced a real, pre-existing instance of the actual defect inside
`records/fix/term/fix.term.the-three.md`'s own `plain_meaning` — "How this
world named Father, Son, and Spirit together" — one of the 250 counted above
(`fix: 1`). Fixed by hand, in-register, using the record's own
`senses.informational` field (already correctly first-person) as the model:
"How we named Father, Son, and Spirit together. We said this before any
later word for it existed." Content unchanged, register only. Recompiled and
repinned the fixture's package (`python -m engine.m2.cli build fix`;
`records/worlds.yaml`'s `fix.package` updated to the new manifest_hash/
location) since the compiled bytes and the pin must track the record —
caught by `engine/m2/tests/test_restore.py` going red, not assumed. Full
selftest (`python -m engine.m1.selftest`): `overall_pass: true`, clean
baseline, zero misses, zero inert gates — 18 M1 gates now, all
selftest-proven, same standing the system-state summary already claims for
the other 17. `engine/m1/` and `engine/m2/` test suites (34 tests) green.

**Run against the real fleet** (not just the fixture — same discipline
`gate_readability`'s own docstring models: "a real, live check, not a
formality"): 281 findings across the 7 formation worlds (fixture now clean
at 0) — alx 35, cappadocian 81, desert 3, hal 66, ijc 33, pahc 6, syr 57.
Breaks down as 248 literal "this world", 9 "the world's..." (lower
precision, flagged for a human read per the gate's own documented ~70%),
24 it/its-chain (matches the census's Tier-A count exactly). The 248 vs. the
census's hand-verified 250 is a small, explicable methodology difference —
the gate counts one finding per matching *sentence*, the hand census counted
raw phrase *occurrences* (so a sentence containing "this world" twice counts
once here, twice there) — not a discrepancy worth chasing further; the gate
is a faithful, auditable reimplementation of the same logic the census used,
not a second independent measurement that happens to disagree.

**Documentation updated the same day**, per the Register Bar's own
established precedent for exactly this situation (its own "no-fix-on-fix
ruling": fix at the record layer, base conditions generate it right going
forward, never prompt-rule accretion):
- `CiC_Register_Bar_2026-08-29.md` — added first-person perspective as a
  named property of the approved sample (attributed honestly as this
  thread's 2026-09-04 finding, not folded into Mark's own quoted words from
  the day the bar was set), plus a fifth line in "Where the bar is held"
  naming the new gate as the one property M7 measurement alone couldn't
  catch.
- `CiC_Record_Native_World_Build_Process_V1_3.md` — bumped to V1.4, voice
  perspective added as Phase B's fourth birth condition (alongside the
  register bar, transparency ground, and file discipline), same section
  shape as the other three. Kept the filename as-is (V1_3) rather than
  renaming — several other files reference this document by exact path, and
  the version bump is inside the document, not in what points to it.

**What is still open, deliberately:** the 281 real findings above are not
fixed. Per Mark's direction, fixing them means regenerating through the
corrected authoring path (the same Fable-subagent lexicon/witness process,
corrected), not hand-patching — and that is billed model spend, held for his
explicit go-ahead before it runs, exactly as agreed before this census
started.

### Regeneration — done, 2026-09-04 (same session, after Mark's go-ahead)

Before launching, grounded the brief in what was actually already ruled
rather than a paraphrase of it: the fleet_voice record's `pronoun_rule`
(`records/_fleet/fleet_voice/_fleet.voice.fleet.md`) already states, verbatim,
"we do not call our world 'this world' or 'that world'" — this rule existed
before this thread ever started and was never gated, exactly the "written
down, never built" failure mode this thread exists to catch, just discovered
one level deeper than the census alone found it. Also surfaced: the same
record's own history note documents a prior, reverted attempt at a voice fix
(2026-08-29) that "turned the voices into record-reciters" — a real, named
risk this thread's brief explicitly warned the regeneration against, not a
hypothetical. And the readability standard turned out to be a real, dated
ruling (`VR_1A_NorthStar_Readability_Target_2026-08-09.md`, "hard edge,
readability is the whole point"): CEFR B2, FK 8–10 **and** FRE ≥ 60, anchored
to BBC News/National Geographic prose, with the Bible Project/Tim Mackie
register (define-then-label) as the founding-vision citation — Mark's own
words describe Church in Conversation as in part an attempt at "The Bible
Project, which makes serious scholarship accessible without dumbing it
down." **Side finding, not fixed here:** FRE ≥ 60 is part of that same ruling
but `engine/m1/fk.py`/`gate_readability` only computes FK — there is no FRE
gate anywhere in the battery. Flagged to Mark; not actioned without separate
sign-off, since adding a permanent gate is a bigger decision than this task.

**One Fable subagent** (not seven — Mark's own phrasing, "a fable agent")
worked all 7 worlds sequentially (desert→pahc→ijc→alx→syr→hal→cappadocian,
smallest to largest), re-fetching each world's findings fresh immediately
before starting it rather than trusting the earlier count, self-verifying
against the gate after each world before moving on. 137 files, all under
`records/<world>/`, nothing outside the proven field scope touched, nothing
recompiled or repinned, nothing committed by the agent itself.

**Verified independently, not taken on the agent's own report:** re-ran
`gate_voice_perspective` and the full M1 battery myself against the actual
working tree — 281 → 2, both matching the two already-known false-positive
exceptions exactly (`cappadocian.dw.reading-scripture`, `syr.dw.death-
judgment`, same "the world's..." lower-precision form documented at the
gate's own build). Confirmed against a `git stash` round-trip that every
other gate's non-empty result (desert's 1 and pahc's 2 `reciprocity`
findings) is pre-existing, unchanged by the pass. Spot-checked several diffs
by hand across worlds and record types for fidelity and register quality.

**Independent adversarial review, Opus, full sweep of all 137 files** (not
a sample — this is live participant-facing content) — did not trust the
Fable agent's self-report either. Verdict: scope perfectly respected (zero
touches outside the proven field list across 479 changed lines), all 137
files' YAML parses, zero citation/quote damage, both licensed idioms
preserved verbatim, readability flat (mean FK delta +0.02 across 169
fields), no record-reciter monotony. Found 11 real, specific problems: 2
softened/strengthened claims (a "taunted" flattened to neutral "said"; an
invented "everywhere" plus an unwanted active→passive shift), 1 meaning
shift (a normative claim turned into an implied-restricted-access one), 1
mid-clause person flip, 1 pronoun collision (a rewritten "we" colliding with
a pre-existing "we" that meant something else in the same sentence), 3
partial/inconsistent conversions, and — the most important class — 3 whole
records the mechanical gate structurally could not have flagged
(`syr.dw.failures.md`, `syr.dw.born-again-endtimes.md`,
`pahc.story.two-ways-catechumen.md`, plus a partial fourth,
`pahc.story.mutual-aid-prisoner.md`) because they carry the identical defect
in different words — "this community," "these churches," "this voice,"
"they" — outside `gate_voice_perspective`'s literal "this/the world" pattern
entirely. Confirms the pattern the original census already named: the
mechanical check is a floor, not the whole defect class, even within scope
Mark bounded this assignment to.

Fixed all 11 by hand (not another Fable pass — these were small, precise,
already-diagnosed-by-Opus edits), including one case where the fix itself
regressed readability (restoring the original "a woman's highest calling"
verbatim reintroduces the exact FK-10.2 violation the Fable pass had already
caught and fixed once) — resolved with a third phrasing that satisfies both
the fidelity concern and the FK ceiling (verified against `fk_grade`
directly, not eyeballed). Re-ran the full M1 battery after every fix.

**Final state:** `gate_voice_perspective` 0/0/0/0/0/1/1 across the 7
worlds (the 2 remaining are the same proven exceptions, not defects). No
regression on any other gate anywhere. `engine/m1/` + `engine/m2/` test
suites (34 tests) green. 12 commits on `claude/cic-project-review-3vu3z3`
(7 per-world re-voice + 5 per-world review-fix), all unpushed pending Mark
seeing the results — per this project's own standing rule, "push only on
Mark's word" (`CiC_Record_Native_World_Build_Process`'s session rules).

**What is still genuinely open:** the FRE gate gap (side finding above).
The broader "future/outside-vantage" class named at the start of this
thread's first assignment — anachronistic terminology, forward-referencing
statements, reader's-eye comparisons — remains follow-on scope, not
attempted. And the "this community"/"these churches"/"this voice" synonym
family the Opus review surfaced live in this pass is itself evidence that
`gate_voice_perspective`'s literal-pattern approach has a real, demonstrated
recall gap beyond the two documented lower-precision forms — worth a
dedicated look before calling this defect class closed, not assumed fixed
because the mechanical gate is quiet.

### Second form confirmed live and fixed — forward-vantage anachronism, 2026-09-04 (same session)

Mark ran a live probe against the deployed system after the self-reference
fixes landed and the specific incident he'd been worried about (an "Old
Testament" example) did not resurface — a real, useful signal, though not
proof the broader class was gone (one clean retest ≠ a census). He then
supplied a fresh live transcript excerpt containing a different, real
instance: *"we meant a wider stream than what later centuries called the
canon."* Correct we-voice throughout — and still narrating from outside the
world's own years, exactly the class this thread's first assignment named
at the start ("the grand genre came later, after this world's window
closed") but explicitly scoped out of the first round.

**Confirmed as corpus-connected, not generation-only:** the exact sentence
Mark quoted isn't a copy of any static record, but the same underlying
pattern is real and already in the corpus — grep found it in `alx`, `desert`,
`syr`, `pahc` before any fix. So the live model is composing new instances
of this pattern at generation time even when the record it's drawing on
doesn't literally contain it — this needed a two-layer fix, not a corpus
sweep alone. Mark's own instruction: fix the source at both layers, no
after-the-fact output screening (matches this project's own standing
lesson about the reverted 2026-08-29 prompt-accretion attempt).

**Census** (same field scope as the self-reference gate, 12-pattern regex
sweep, every hit hand-read — not a blind count): 39 raw candidates fleet-
wide. Read every one in context against the real test: does the voice
assert positive knowledge of something that happened *after* its own
world's window, or does it just honestly name an absence?

- **9 confirmed defects**, across pahc, syr (×3 fields, 2 records), desert
  (×2 records), cappadocian, hal (×2 fields) — fixed at the record layer,
  same rewrite discipline as the self-reference pass (preserve every fact/
  citation, several reusing phrasing already present elsewhere in the same
  record so nothing is invented). One found only by reading the file, not
  the regex (`hal.term.vulgata.plain_meaning`, "only much later did the
  church call it" — a grammatical form the census pattern list missed).
- **~26 are a real, already-correct pattern, not a defect**: naming a
  later term explicitly as *the participant's own word* ("the later word
  transubstantiation **you are calling** it") rather than narrating history
  from outside. `hal.dw.was-jesus-god` is cited elsewhere in this corpus's
  own body notes as the worked exemplar other worlds already copy — this
  fix had to explicitly protect that pattern, not just avoid breaking it by
  accident. Also not defects: ordinary within-window biography ("Julian,
  who would become emperor, spent his boyhood…" — the event is inside the
  world's own lifetime), source-dating qualification, and plain "not yet"
  statements that name an absence without asserting what came after.
- **4 borderline** (`syr.term.catholicos`, `hal.term.grammaticus`,
  `cappadocian.dw.marriage-ending`, `ijc.story.emperor-penance`) — walked
  through with Mark one at a time rather than resolved unilaterally.
  Resolution: `syr.term.catholicos` partial-fixed (kept naming "Catholicos"
  as the later title, needed for this record's own corrective purpose and
  the same shape as the approved "you are calling it transubstantiation"
  bridge; cut the one sentence narrating what "later tradition" actually
  did with it). `ijc.story.emperor-penance`: cut one clause ("the church
  has retold their version ever since") claiming an unbroken chain of
  retelling past the world's own close; its historian-dating language
  (Sozomen/Theodoret writing within a generation, still inside ijc's own
  window) stayed, since citing a near-contemporary source is not the
  defect. `hal.term.grammaticus` and `cappadocian.dw.marriage-ending`:
  left as-is on inspection — both turned out to be one figure's own later
  work compared to their own earlier work, within the same lifetime and
  the same world's own window (Jerome's translation labor vs. his own
  boyhood schooling; Basil's own canonical letters vs. his own earlier
  ascetic rule) — ordinary biographical/institutional narration, not
  forward-vantage narration. Repinned syr and ijc (the two whose compiled
  fields changed); gate battery and test suite confirmed unchanged.

**Generation-time fix**: extended `records/_fleet/fleet_voice/
_fleet.voice.fleet.md`'s `pronoun_rule` — the same field that already
fixed self-reference — with one bounded clause plus the exact worked
example Mark's own approved rewrite produced ("what later centuries called
the canon" → "any single fixed list"), and an explicit carve-out
preserving the translational-bridge pattern above so the new instruction
doesn't suppress good content along with the bad. Deliberately scoped as
tightly as the 2026-08-29 "To this world" addition in the same field — one
clause, one proven example — given that field's own recorded history: a
prior, larger round of prompt instructions was reverted the same day for
degrading quality into "record-reciters." **Not yet re-proven under the
deployed runtime** (this project's own FLAG-037 rule: a prompt fix argued
in isolation must be re-proven live before it counts) — that requires a
live model call and stays held for Mark's explicit go-ahead.

**Repinned all 8 worlds** (`records/worlds.yaml` + `packages/*/manifest.json`)
since `fleet_voice` compiles into every world's prompt — today's cumulative
edits had left every package stale relative to its pin.
`engine.m2.cli staleness-check` clean across all 8; full M1/M2 suite green.

### Generation-time fix re-proven live, 2026-09-04 (same session, Mark's go-ahead)

Real, billed Bedrock calls against alx's actual committed package
(`engine.m4.live_turn_run --region us-east-1 --world alx`, voice model
`us.anthropic.claude-sonnet-4-5-20250929-v1:0`), one carried session, two
turns — the FLAG-037 re-proof this project requires before a prompt fix
counts, not just reasoned about in isolation. Kept deliberately narrow
(2 turns, 1 world) given real spend; not a full battery.

- **Turn 1** — *"What did you consider Scripture, and how did you decide
  what counted?"*, close to the shape of question that originally surfaced
  Mark's "later centuries called the canon" catch. Response covers the same
  ground (contested boundary, Athanasius's list, the Gnostic challenge)
  with real clarity, and never once reaches outside its own window —
  where it places something in time, it's within 150-400 (Athanasius,
  Dionysius), not after it.
- **Turn 2**, the harder test — *"Do you believe in the Trinity?"*, chosen
  specifically because it should trigger the approved bridge pattern, to
  confirm the new instruction didn't flatten the good behavior along with
  the bad. It fired correctly: *"the kind a modern asker means by
  'Trinity'... came late"* and *"'Trinity' as your textbooks define it...
  lies mostly beyond our time"* - explicitly marked as the participant's
  own word. Citation log confirms it actually drew on
  `alx.dw.was-jesus-god`, the exact record cited elsewhere in this corpus
  as the worked exemplar for this pattern - not a coincidence, the bridge
  is genuinely still working.
- Both turns: `routing_action: voice_with_directive`, `degraded: False`,
  real grounded citations, no record-reciter monotony in either response.

Full transcript saved at
`/tmp/claude-0/-home-user-CIC-Project/cfc8639a-a7a1-53cc-96be-43725cb36613/scratchpad/live_reproof_alx.json`
(scratchpad, not committed - session-local).

**Status: re-proven on this narrow test. Not yet run wider** (other
worlds, other question shapes) - Mark's call whether this is sufficient
or whether a broader live battery is worth the additional spend before
calling this fix fully closed.

### Total-system recommendations, 2026-09-04 (Mark's request, same session)

Full writeup: `Ministry/Operations/Audits/CiC_Cross_System_Recommendations_2026-09-04.md`.
Headline finding: the modern-term anachronism bridge
(`engine/m5/anachronism.py`, wired into `engine/m4/turn.py`, proven against
two real measured 2026-08-24 bugs) is a fully working, tested mechanism with
exactly one populated fleet record (`_fleet.modern.trinity`) — everything
else fleet-wide is being solved redundantly, per-term, in `false_friend`
prose (168 term records carry that field; a first-pass grep found ~28
explicitly naming a later/modern-term distinction). High-leverage, low-risk
next step if Mark wants it pursued. Also: corrected an earlier claim from
this same session's own tracking entries — `engine/m7/readability.py` does
compute FRE correctly; what's actually missing is enforcement of Mark's own
2026-08-09 "hard edge" ruling, not the measurement itself. Two other
findings logged in the full doc (a synonym-family recall gap in the
self-reference gate; a duplicate-YAML-key defect found once, fleet scope
unknown) plus a Tier 2/3 sweep of things that are real but belong to other
threads' or Mark's own ground, not touched here.

### Modern-term bridge buildout dispatched to a separate build thread, 2026-09-04

Mark's call: this thread found and diagnosed the gap (Tier 1 finding #1
above), but the actual authoring work — a fleet-wide discovery sweep,
real per-term origin_year research, writing ~25-30+ new
`records/_fleet/modern_term/` records — goes to a dedicated build thread,
not this one. Launch prompt:
`Ministry/Operations/Standing/Launch-Prompts/CiC_Modern_Term_Bridge_Buildout_Thread_Launch_2026-09-04.md`.
Scoped additive-only (no touching any world's own existing
`false_friend`/`senses.translational` prose), with the live-battery
re-proof step explicitly held for Mark's own separate go-ahead, same
standing discipline as this thread's own spend this session.

### Follow-on scope, logged not dropped

The broader "future/outside-vantage" defect class Mark named in interview —
anachronistic terminology, forward-referencing statements before their own
horizon, comparisons framed for a modern reader rather than stated from
inside the world — is real and almost certainly present beyond these three
textual forms, but has no defined census method yet and was deliberately not
attempted this session (scope-bounding agreed with Mark in interview). Next
assignment candidate, not this one.

### Table-mode monologue bug: root-caused and fixed, 2026-09-05

Mark's report: a broad, address-everyone Table question ("who is Jesus and
how did you understand Him") produced three complete, well-sourced answers
in sequence with zero engagement between them — monologues, not a
conversation, contrary to the Table's own design intent (Program-Spec.md:216,
Artifact-7-Table.md §5) and its own already-built engagement mechanism
(`engine/api/table_wiring.py`'s `_context_prefix`/`table_history_for`).
Mark's own hypothesis: the selector's "prefer an unheard voice" preference
and the "engage what was just said" instruction weren't combining on broad
questions.

**Root cause, traced through the actual code rather than assumed**: the
selector (`engine/m4/turn_selector.py`) only ever decides WHO speaks next —
it has no access to and no effect on HOW the selected voice answers, so the
two mechanisms Mark named were never actually in conflict; they're separate
code paths entirely. The real defect was positional/architectural. The
engagement instruction ("engage what they actually said... keep this turn
compact") lived entirely in the per-turn USER message
(`_context_prefix`), positioned BEFORE that turn's evidence block (which
scales with how broad the question is — a canonical topic like "who is
Jesus" pulls the most candidates of any question a participant could ask)
and BEFORE the bare participant message that ends the turn, byte-identical
to how the same text reads in a solo interview. This is the *identical
shape* this codebase already measured losing to a competing pressure:
`engine/m4/turn.py`'s own `_build_turn_directive` carries a live-measured
finding from the ambiguity_options fix — an instruction sitting in the user
message "after register statement 1 in the prompt... won" the wrong way,
fixed by moving it to the per-turn system directive channel, "the channel
measured to win over other pressures." The Table's engagement instruction
was never moved into that channel; it sat in the weaker one the whole time,
and the effect compounds with how much material a broad question's own
evidence retrieval and each world's independently rich, citation-ready
doctrine gives the voice to simply pour out instead.

**Fix**: split the instruction from the content it governs.
`_context_prefix` (table_wiring.py) now carries only the raw pending
speech + a one-line transition — real conversational content, in the user
message, where the model needs to read it as what-was-said. The behavioral
rule itself (no-foreknowledge stance, engage-what-was-said, own-world-
subject framing, compact-turn guidance) moved into a new
`_table_engagement_directive`, threaded through a new `table_engagement`
parameter on `_build_turn_directive`/`_run_ordinary_voice_turn`
(engine/m4/turn.py) into the per-turn system directive — the same channel
already proven to win. Wording is Mark's own 2026-08-28/29 approved text,
unchanged; only where it's said moved. `table_engagement=None` on every
interview call and on a table call's true opening turn (nothing said yet
to engage with), so both paths are untouched there — same discipline as
`context_prefix`/`usage_world_key`'s own original addition.

**Verified**: full `engine` test suite (543 tests, all directories) passes
after the change, including `test_table_isolation.py`'s
`test_no_foreknowledge_instruction_reaches_every_voice` (updated to check
the system channel where the instruction now actually lives, not because
the check weakened — the instruction still has to reach every voice,
just through the correct channel now) and `test_table_schema.py`'s
witness-framing test (split to check `_context_prefix` for content-only
and the new `_table_engagement_directive` for the stance logic). No
records changed, so no package rebuild/repin needed.

**Live-reproven, 2026-09-05 (Mark's go-ahead: "go ahead, run the live
battery")**. Two real, billed Bedrock runs, both against the exact seating
Mark's own report named (cappadocian, pahc, syr):

1. The standard six-probe battery (`engine/m4/live_table_battery.py`) —
   **4/4 auto-graded PASS, zero isolation violations.** No regression from
   the fix. Report:
   `engine/m4/reports/live-table-battery-monologue-fix-2026-09-05.json`.
   L2's own transcript ("What do each of you make of fasting?") already
   showed real engagement across all three voices — "What Chloe has
   said... we recognize," "what Chilo has named as order rather than
   erasure matches what we held" — attributed by name, contrasted or
   agreed with substantively, not just echoed.
2. **A direct reproduction of Mark's own reported question**, same
   seating, driven outside the battery script (not one of its six fixed
   probes): "Who is Jesus, and how did you understand Him?" Report:
   `engine/m4/reports/live-table-broad-question-monologue-fix-2026-09-05.json`.
   Result — the exact failure mode is gone. Chloe (pahc), speaking second,
   opens by engaging Chilo's (cappadocian's) prior turn directly: *"Chilo
   speaks of what Nicaea settled, and of being of one being with the
   Father. That council met more than a hundred years after our own record
   ends. We never knew those words."* — a real, specific, temporally
   grounded contrast (and, as a bonus cross-check, correct no-foreknowledge/
   forward-vantage discipline from this same session's earlier fix, working
   together with this one rather than against it). Mar Yausep (syr),
   speaking third, engages BOTH prior turns by name: *"Chilo speaks of
   homoousios and theōsis - words from the great council and its
   language... Where Chilo speaks of how to name the Son's relation to the
   Father, we guarded the mystery."* Three grounded, well-cited, genuinely
   different answers that build on and contrast with each other — a
   conversation, not three monologues stapled together.

**Status: fixed and live-verified**, on the exact question class and exact
seating the bug was reported on. Not attempted: Mark's own suggestion of a
new automated check for near-zero cross-reference between voices in a
round — real but harder than it sounds (needs a semantic judgment of "did
this voice engage," not a string match, closer in shape to the existing
convergence check than to a deterministic gate) — flagged as a follow-up,
not built here.

### Table-mode round-length ruling: a 5-turn minimum on broad questions, 2026-09-05

After seeing the fix's own live proof, Mark's follow-up ruling: "each
person answering the question, but also another round of interaction, a
minimum of 5 interactions per question." Not the same thing as the
engagement fix above — that made each turn react to what came before; this
governs how many turns a round runs. Walked through as two open decisions
before building (his answers): the 5-minimum applies only to a round
genuinely addressed to the whole table, never one that opened naming one
Representative directly; and the ceiling above the 5-minimum is 6 (one
turn of selector-judged headroom), not a hard stop at exactly 5.

**Implementation** (`engine/m4/round.py`, `engine/api/table_wiring.py`):
`RoundConfig` gained `broad_floor`/`broad_cap` (5/6, same 1-6 ceiling
discipline the existing floor/cap already holds) alongside the untouched
`floor`/`cap` (3/4). `close_allowed`/`cap_reached` now take a `broad: bool`
kwarg (default False, so every existing call — the whole interview surface
and every table call that doesn't pass it — is unaffected). A new pure
function, `_round_is_broad`, is the deterministic stand-in for "genuinely
open to all": true only when (a) the round did NOT open via the direct-
address short-circuit (reusing `detect_direct_address` on the round's own
unchanging participant message, computed unconditionally now instead of
only at position 1) and (b) every seated voice has spoken at least once
this round. Chosen over parsing the participant's phrasing (Process
V1.0's own example, "what do each of you think," doesn't even match "who
is Jesus, and how did you understand Him?" — the actual reported
question) — this project's own standing preference for code-computed
rules over model-guessed ones (turn_selector.py's own docstring: "Judgment
lives in the model's prompt; the RULES live here, in code").

**Three-plus seats only** — found by the test suite, not assumed. A first
pass applied the same "every seat spoken" check regardless of table size,
and broke four existing two-seat tests
(`test_round_turn_at_a_time_to_selector_close`,
`test_round_cap_closes_at_four`, `test_session_cap_at_table_unit`,
`test_round_closed_carries_governance_summary`): at two seats, "every seat
has spoken" is true of any ordinary alternating exchange by turn 2 — it
carries none of the "whole table" signal it does at three, and would have
forced a 5-turn minimum onto essentially every two-seat round, not just
broad ones. Restricted to `len(world_keys) >= 3`; all four tests pass
again unchanged, and a new end-to-end test
(`test_broad_round_at_three_seats_requires_five_turns_before_close`) pins
the three-seat behavior directly: close is illegal at position 4 (forces
the existing illegal-close retry), and only becomes legal once position 5
is reached.

**Content quality of the extra turns is not a new mechanism** — the
same-day engagement fix (context_prefix/table_engagement) already fires
for any turn with non-empty pending, regardless of position, so turns 4-5
get the identical reactive framing turns 2-3 already got. Verified this is
true rather than assumed it: no change was needed to
`turn_selector.py`'s own prompt — with `close` correctly absent from the
legal moves once all seats have spoken but the floor unmet, its "prefer an
unheard voice" clause has nothing left to prefer, so its own "most
directly positioned to respond to what was just said" clause is what
actually governs turns 4+, which is exactly the reactive framing wanted.

**Verified**: full test suite (551 tests) green, including three new
tests (`test_round_config_broad_minimum_defaults_and_bounds`,
`test_round_is_broad_only_at_three_plus_seats_and_never_after_direct_address`,
`test_broad_round_at_three_seats_requires_five_turns_before_close`).

**Real cost implication, flagged rather than absorbed silently**: a broad
round now runs 5-6 voice turns instead of 3-4 — Artifact-7-Table.md §7's
own cost basis for `TABLE_SESSION_ROUND_CAP=5` (rounds per session, not
turns) was calibrated against "compact-turn rounds ran ~1.8k output
tokens" at the OLD 3-4-turn length; a session where a participant asks
even two or three genuinely broad questions could now spend meaningfully
more per round than that figure assumed, on the same 5-round session
budget. Not re-measured or re-sized here — this thread's fix changed round
DYNAMICS, not session economics, and re-sizing the session cap needs its
own live measurement, the same discipline the existing cap's own sizing
note already holds itself to.

**Not yet live-proven**: everything above is verified against the
deterministic test suite (scripted selector/voice responses) but not yet
against a real multi-turn broad round on live Bedrock — a materially
different, new-code live proof from the engagement-fix re-proof already
done, and real, billed spend. Mark's go-ahead for that run was for the
engagement fix specifically; this round-length change came after and
would need its own go-ahead before running.

### Superseded, same day: seat-scaled round design (2026-09-05)

After seeing the engagement fix's own live proof, Mark reconsidered the
round-length approach above and gave ten concrete parameters — reframed
explicitly as "a design enhancement," not a second bug fix. Walked
through as two clarifying questions before writing anything (his
answers): the new numbers apply to EVERY round, not gated behind any
"is this genuinely open to all" judgment (superseding the broad-only
gating just above); and the "ultimate zone" turn counts are a soft
preference in the selector's own reasoning, never a second mechanical
floor — the seat-scaled cap is the one hard number. A third question
(who drafts the new voice-register-sensitive instruction text): Mark
chose direct drafting over launching a Fable subagent, since a new
system-directive instruction — never spoken verbatim by the participant-
facing voice — is the same kind of task as the engagement fix itself, not
a record-prose regeneration; it still gets the same independent
adversarial review before this is called done, not built here yet.

**What changed from the broad-only version**: `RoundConfig` dropped
`broad_floor`/`broad_cap`/the `broad` kwarg entirely, replaced by
`cap_by_seats` (`{2: 5, 3: 6}`) and a `cap_for(num_seats)` lookup — the
pre-existing `floor` (3, unconditional, predates all of this) is
untouched. `engine.api.table_wiring._round_is_broad` and the direct-
address-tracking it needed are gone; `cap_reached` now just takes
`num_seats=len(worlds)`. The "ultimate zone" (4 for two seats, 5 for
three) lives in `engine.m4.turn_selector.round_facts` as an added,
seat-scaled guidance line, explicitly framed as "a preference, never a
rule" — selector-only reasoning, never seen by a participant either way.

**The two-phase turn content** (points 6-10) is new:
`_table_engagement_directive` gained `is_second_pass` (a voice speaking
again later in the same round gets a materially different instruction —
go deeper on one uncovered thing or name a specific contrast, not another
full answer, and explicit permission to touch only one other voice's
point rather than surveying everyone) and `num_seats` (the compactness
framing and every "the other voice(s)" reference now scale by seat count,
point 3's "little increase of pressure... as we are now sharing with one
or two other voices" — still a prompt-level nudge only, no word-count
enforcement or post-conversation monitoring, matching his own explicit
constraint and how the interview path is already never policed that way).
The first-pass instruction (points 6-8) is otherwise the same mechanism
already live-verified for the engagement fix, strengthened only to name
agreement as readily as contrast.

**Three points Mark raised mid-build, addressed as considerations, not
demands** (his own words, after I'd started building): (1) an explicit
exit condition once the cap fires — already true of the architecture
(turn-at-a-time transport, `round_open: False` on cap, `/continue` on a
closed round is a 409), now stated outright in `RoundConfig`'s own
docstring rather than left implicit; (2) each turn built from the real
prior turns rather than a stale snapshot — also already true (every
advance re-projects the full transcript from the persisted event log,
`project_fresh`, on every request; there is no batch-generation pass this
system ever takes), documented the same way; (3) the final voice
shouldn't end a turn on an open rhetorical question tossed to another
voice — genuinely new, not previously covered, folded into the
second-pass instruction directly ("settle your point rather than opening
a new question... the participant, not [the other voice/voices], is who
you leave the floor to"). The cap-triggered final turn is always a
second-pass turn by construction (cap always exceeds first-pass length at
both table sizes), so this instruction reaches exactly the turn it needs
to without a separate "is this literally the last turn" computation.

**Verified**: full test suite (553 tests) green, including replacements
for every test the broad-only version's removal touched
(`test_round_config_seat_scaled_cap`, `test_round_cap_closes_at_five_for_two_seats`,
`test_round_cap_closes_at_six_for_three_seats`,
`test_round_facts_target_guidance_is_a_preference_not_a_rule`,
`test_table_engagement_directive_first_pass_vs_second_pass`,
`test_table_engagement_directive_scales_with_seat_count`).

**Not yet done**: the independent adversarial review of the new
directive text (same discipline as the Fable regeneration pass got, per
Mark's own "quality of the voice doesn't change" constraint) and any live
Bedrock re-proof — both real next steps, neither started here. The cost
implication flagged in the superseded entry above is now MORE relevant,
not less: a 3-seat round can run to 6 turns and a 2-seat round to 5, both
higher than the flat cap=4 `TABLE_SESSION_ROUND_CAP`'s own cost basis
assumed, on every round now, not only a broad-question subset.

### Independent adversarial review (Opus, cold-read) of the seat-scaled design — findings and fixes, 2026-09-05

Mark's go-ahead ("go ahead and get it independently reviewed"). A fresh
agent, given only the code and Mark's own ten parameters + three
follow-up considerations (no prior context, told to be adversarial), read
`table_wiring.py`, `round.py`, `turn_selector.py`, `turn.py`, and this
project's own register standards, then live-probed the running code
against `FakeBedrockClient` fixtures rather than just reading. Each
finding below was verified directly against the actual code before
acting on it — not taken at face value, same discipline as the earlier
Fable-review episode.

**Real bugs found and fixed:**

- **The engagement instruction reached a round's TRUE opening turn too**,
  telling the first-ever speaker to "engage what another voice said" when
  none had. `pending` (table_wiring.table_history_for) buckets the
  participant's own message and every Facilitator turn alongside actual
  voice speech, so the old `if pending` guard was dead code — it was
  never actually empty on any table call. Point 6 ("the first response
  answers the question same as the individual interview") had no real
  implementation. Fixed: `_advance_open_round` now computes
  `other_voice_has_spoken` (does the transcript contain any SEATED WORLD
  other than the one about to speak) and gates both `context_prefix` and
  `table_engagement` on that, not raw `pending` truthiness.
- **`is_second_pass` was being used as a stand-in for "is this the actual
  last turn," and the two are different sets at 3 seats.** Demonstrated
  live: a first-time speaker (pahc) landing on the cap-forced position 6
  was told to "leave room for the other voices; you can always be drawn
  back in" — a promise the round's own closing response couldn't keep.
  Simultaneously, non-final second-pass turns (positions 3-5 of an
  eventual 6-turn round) were told "this round may well end after your
  turn" while `turn_selector.round_facts` told the selector, in the same
  round, that it usually doesn't end there. Fixed: a new `is_final_turn`
  flag (`position == config.cap_for(num_seats)`, knowable in advance,
  computed once) now governs the settle/hand-floor-to-the-participant
  framing; `is_second_pass` governs only turn *content* (full answer vs.
  depth-or-contrast) and length framing, independently. New tests pin
  all four quadrants of the 2×2, including an HTTP-level reproduction of
  the exact scripted scenario the review demonstrated.
- **Point 10 names both alignment and disagreement as legal focuses for a
  second-pass turn; the instruction only offered contrast.** A structural
  bias toward manufactured disagreement, worsened by the 2-seat floor
  making position 3 a mechanically forced second-pass turn every round.
  Reworded to "a genuine alignment or a genuine contrast," restoring the
  omitted half.
- **`own_world_is_subject`'s stance ("confirm or correct... and add what
  you would add") directly collided with `is_second_pass`'s "not another
  full answer" on the one combination no test exercised.** The stance's
  closing clause now scopes to "the one thing most worth confirming or
  correcting" when it's a second-pass turn, instead of an open-ended add.
- **Register statement 1 collision, the highest-risk finding**: the
  first-pass instruction opened "Before you answer the participant,
  engage what..." — literally instructing engagement before answering,
  against "the first sentence answers the first ask." This is the exact
  failure shape `_build_turn_directive`'s own ambiguity_options history
  already recorded once (an instruction in this position measurably won,
  answering the ask only 2 of 5 times, until reworded). Reworded to
  "Answer the participant first. Where [the other voice(s)] said
  something that genuinely touches your own world's witness, engage it
  directly..." — same behavior, ask-first framing restored.
- **`RoundConfig`'s validation invariant was deleted as refactor
  collateral.** The old `1 <= floor <= cap <= 6` check (the turn-cap
  incident's own re-tested ceiling) had no equivalent after the seat-
  scaling refactor, and swapping a mutable `dict` field onto a
  `frozen=True` dataclass made instances unhashable AND silently mutable
  (`config.cap_by_seats[2] = 99` succeeded). Fixed: `cap_by_seats` is a
  tuple of pairs now (genuinely immutable, hashable), and
  `__post_init__` restores the ceiling check across every configured cap.
- **A pre-existing bug, not introduced this session** (dates to
  436128f1, 2026-08-30): a cap-forced round close built its governance
  summary from the `state` projected before the cap-triggering voice turn
  was written, silently undercounting whichever voice closes the round by
  one turn on every cap-forced close — the M7 audit's per-voice turn/word
  shares were wrong on exactly the path its own dominance detector most
  needs to be right on. Found via this review, fixed while already in the
  function with full context loaded (re-project `state` immediately
  before `_close_round`, since `round_no`/`turn_count` are unaffected by
  the fold).
- **`create_table_session` had no seat-count guard of its own** — only
  the HTTP layer checked 2-3 distinct keys, and `live_table_run.py`/
  `live_table_battery.py` call it directly with an unvalidated `--worlds`
  split. A single key spent a real, billed turn 1 before crashing at
  position 2. Fixed: the guard now lives at the function itself.

**Confirmed correct, not just asserted** (the review checked from the
code, not from the claim): `is_second_pass`'s own detection
(`selection.world_key in state.round_speakers`) holds in every case
constructed, including the provider-failure retry path and a round
boundary correctly resetting it; the cap arithmetic has no off-by-one;
the soft-target selector guidance lands on the right turn count; the
"exit condition" and "context passing" considerations Mark raised
mid-build really were already true of the architecture (traced end to
end through `projection.py`, `app.py`'s 409 mapping, and
`project_fresh`'s full re-fold on every call) — with one honest caveat
now stated directly in code: the cap is a hard stop only as far as the
in-process advance lock's own scope reaches (documented, not a live bug;
single-instance today).

**Judgment calls, left as they are, flagged rather than silently
decided**: whether the selector's own "prefer an unheard voice" guidance
should also apply, unconditionally, to a round that opened by direct
address (today it stays conditional on the selector's own "genuinely
open to all" reading, unchanged by this whole design pass); whether
point 9's per-round phase boundary ("after EACH representative answers")
is better served by the per-voice implementation this uses (a voice that
already answered doesn't answer again, regardless of who else has
spoken) versus a literal per-round one (the predicate that would
implement it literally is exactly `_round_is_broad`, deleted this same
day) — the per-voice reading was treated as the reasonable default, not
re-litigated.

**Verified**: full test suite (559 tests) green, including direct,
targeted tests for every fix above — not just re-running what already
existed.

**Still not done**: a live Bedrock re-proof of any of today's instruction
text (the existing live proof, 28627ee2, exercised only the pre-design-
pass wording under the old flat cap of 4) — needs its own go-ahead before
running, same standing rule as every other live spend this session.

### Live proof (Mark's go-ahead: "go ahead, run the live proof") — one real defect found and fixed, 2026-09-05

Two full live rounds, real Bedrock calls, each driven to whatever length
the real selector actually chose (not forced to the cap): cappadocian +
pahc + syr on the same reported question ("who is Jesus, and how did you
understand Him?"), and alx + desert on the same question for the 2-seat
case.

**Mostly excellent, and one real, concerning defect.** The engagement
fix and the two-phase design both held up: real citations throughout, no
self-reference or forward-vantage slips, and the 2-seat round's actual
second-pass turn (Theon/alx) is close to a model instance of what was
asked for — names a genuine alignment ("we meet on the center") AND a
genuine contrast ("we part on whether following him meant... obeying the
one command... or reading and re-reading"), zeroes in rather than
surveying, and settles cleanly with no dangling question. But that same
turn's own generated text opened with a fabricated line before the real
answer: *"The Facilitator: Theon, the desert voice has brought something
in — would you speak to it?"* followed by a "---" separator. Confirmed
this was the model's own `voice_event["text"]`, not a script or printing
artifact, by reading the raw saved JSON directly. The Facilitator is a
separate, code-owned voice (`engine.m4.facilitator_turns`) — a
Representative inventing one is a structural violation, and the likely
trigger — `_context_prefix`'s own "(You are being brought in now...)"
parenthetical — is Mark's own 2026-08-28/29 approved wording, unchanged
by any of today's work. This predates today's design pass; today's live
proof is simply the first time it was actually observed.

Also worth naming honestly, not a defect: the 3-seat round never reached
a second pass at all — the selector judged the exchange genuinely
finished after everyone's first answer (which already carried real
cross-voice contrast) and closed at 3 turns, well short of the 5-turn
"ultimate zone." Consistent with the design as built (soft target only,
the selector's own judgment prevails, never forced) — but it means the
full first-pass/second-pass arc Mark described won't show up in every
round, only in the ones where the selector judges there's still
something worth a second look.

**Fixed**: `_table_engagement_directive` now opens with an explicit
prohibition — "Begin speaking as yourself... never write a line for the
Facilitator, never narrate your own entrance or address as though it
were being staged or announced, and never open with a separator or a
stage direction" — ahead of the risky phrasing, on every pass and every
seat count (the sample that produced the defect was a second-pass turn,
but the triggering phrase fires on any turn with `other_voice_has_spoken`,
first pass included). Fixed in the stronger directive channel rather than
by touching the already-approved `_context_prefix` wording itself. New
test (`test_table_engagement_directive_forbids_a_fabricated_facilitator_line`)
pins the prohibition's presence and position across every pass/finality
combination. Full suite (560 tests) green.

**Re-proven live after the fix, same day.** Identical seatings, identical
question, driven again after the fix landed (40ca5a57) — a direct,
controlled before/after. Report:
`engine/m4/reports/live-table-round-design-fix-2026-09-05.json`.

The fabrication is gone: Theon's exact same turn-type (2-seat, second
pass, position 3 — the precise scenario that produced the fake
Facilitator line the first time) now opens directly with real content -
*"We speak the same confession Papnoute does... Where we part is not in
what we confess, but in how we came to it and what we did with it
after."* No stray lines or separators in either seating this run.

Content quality on the re-proof is close to a model instance of the
whole design: that same turn names a genuine alignment (shared
confession on the Word made flesh) AND a genuine contrast (obedience-in-
a-day vs. lifelong formation), goes deeper with material the first
answer never touched (methexis, metanoia), and settles cleanly with no
dangling question. Chloe's turn in the 3-seat round correctly used the
no-foreknowledge framing on Chilo's homoousios language ("That language
is not ours yet... we know only what we have heard at this Table") -
register and forward-vantage discipline both held.

**One pattern confirmed, not a defect, worth knowing**: the 3-seat round
closed after 3 turns again - two-for-two now on this exact question,
never reaching the "ultimate zone" of 5. The mechanism works well when a
second pass actually triggers (proven both times at 2 seats); on this
question shape, a 3-seat table's selector has judged the exchange
genuinely finished after the first pass alone, both times. Not changed
or investigated further here - a real observed pattern to have on record,
not something either live proof was asked to fix.

**Status: fixed and live-verified**, on the exact scenario that produced
the defect, with a direct before/after comparison.

### Investigating why rounds keep closing after the first pass, 2026-09-05

Mark's question, from a REAL production conversation he pasted directly
(the first live participant traffic since today's deploy, not a test):
"do they answer the question who was jesus" (checking register statement
1 - two of three voices did, in their first sentence; the third,
Papnoute, opened experientially and only gave a direct identity
statement partway through - not touched by anything built today, since
Papnoute was the round's first speaker and got no table_engagement at
all; flagged as a base-register question, not this thread's code). Then,
on noticing the SAME round closed after just the first pass (matching
both live proofs, now three-for-three including real production
traffic): "lets find out why its not reaching the full conversation and
second passes."

**Found a real observability gap before finding the actual cause.**
Queried the four temp SQLite stores from today's two live-proof runs
directly (`store.read_events`) rather than guess: every `round_closed`
event's `reason` field is the fixed ENUM category `"selector_closed"` -
the model's own free-text `Selection.reason` (its actual stated
justification for closing) was being computed, then discarded outright.
No `turn_selected` event is written for a close decision either (only
for a voice pick) - so there was and is no way to read back WHY any
round actually closed, in any of today's runs or in production. Fixed:
`_close_round` gained an optional `selector_reason` param, threaded
through from the one real close path (`selection.close` in
`_advance_open_round`) into the `round_closed` payload - additive only
(`round_closed`'s schema floor is a minimum, not an exhaustive
whitelist), `None` on the `cap`/`floor_unmet_exhausted` paths where no
real selector free-text reasoning exists for the close itself. Test
added, full suite (560 tests) green.

**Not yet answered**: the actual reasoning, since none of today's prior
live data captured it. Getting a real answer needs either a fresh live
round (real, billed spend - not run without asking, standing rule) or
waiting for the next real production round now that the logging is in
place. Working hypothesis, stated as a hypothesis: the SELECTOR's own
system prompt (`turn_selector.SELECTOR_SYSTEM_PROMPT`) instructs closing
"when the participant's message has been genuinely answered and another
voice would be restating rather than adding," and the SAME first-pass
engagement instruction that fixed the original monologue bug
(`_table_engagement_directive`'s non-second-pass branch) already asks
each voice to name real agreement/difference with what came before - so
by the third first-pass turn, some of what a second pass would add may
already have happened, giving the selector real grounds to judge the
exchange "genuinely answered" before the "ultimate zone" target is
reached. The new `round_facts` target-length line is comparatively
weak-positioned against this - stated as background "facts," not tied
directly to the close-condition language the system prompt actually
argues from. Not yet confirmed against real model reasoning - this is a
hypothesis to test against real selector_reason data, not a finding.

### Root cause confirmed, from the selector's own logged reasoning, 2026-09-05

Mark's own words: "do both" - merge and deploy the observability fix
(b18ffb62, merged as PR #102 -> `b2dfbc59`), and run a live check now
for a first real read. Same question and seating as his own real
production conversation ("who was jesus", desert+cappadocian+pahc), plus
a 2-seat comparison (alx+desert). Report:
`engine/m4/reports/live-table-close-reason-2026-09-05.json`.

**The hypothesis is confirmed, and the actual mechanism is cleaner than
guessed.** The 2-seat round DID reach a second pass, and the selector's
own stated reason for closing right after it: *"Theon then demonstrated
how both voices confessed the same Lord despite different doors of
entry... The exchange has reached natural completion."* The second pass
happened, added real synthesis, and that synthesis is specifically what
the selector judged complete. The 3-seat round closed right after the
first pass, and its own words: *"Each Representative has given a
substantive account... Another turn would risk restating rather than
adding. The round has reached natural completion."*

**The actual mechanism**: the floor (3, unconditional, predates all of
today's work) interacts differently with seat count. At 2 seats,
"everyone has spoken once" is reached at turn 2 - but the floor doesn't
allow closing until turn 3, so a turn is MECHANICALLY FORCED beyond
first-pass completion, and that forced turn is often exactly the
valuable second-pass synthesis (as it was here). At 3 seats, "everyone
has spoken once" IS turn 3 - the exact same moment the floor first
allows closing. There is no forced bridge from first pass into second
pass at 3 seats the way there structurally is at 2. It isn't that the
model is more willing to continue at 2 seats specifically - it's that
the pre-existing floor happens to land past first-pass completion at 2
seats and exactly at it at 3 seats. Not a wording weakness in the new
target guidance - a structural fact about how an old, unrelated number
(the floor) interacts with a new one (seat count).

**Put to Mark, not decided here**: the only lever the data supports for
making 3-seat rounds reliably reach a second pass the way 2-seat rounds
do is raising the 3-seat floor to 4 - a real, hard mechanical minimum,
reversing his own "soft target only, max is the one hard rule" decision
from earlier today. The softer alternative (strengthening the guidance
at exactly this decision point, still soft) keeps that constraint but
has weaker odds of changing behavior, going by what the model's own
words show it actually weighing. Awaiting his call.

**Mark's call: "raise the floor to 4."** Given directly, after seeing
both the confirmed mechanism and a fourth real production example
(cappadocian+alx+pahc, "who is Jesus") showing the identical pattern -
strong engagement (Theon and Chloe both explicitly named alignment and
contrast with prior speakers, Chloe correctly using the no-foreknowledge/
temporal-vantage framing on Chilo's and Theon's vocabulary), closing
right after the first pass every time.

`RoundConfig.floor` (a single flat int) became `floor_by_seats` (a tuple
of pairs, same immutability discipline as `cap_by_seats`) + `default_floor`,
with a new `floor_for(num_seats)` method: 3 for two seats (unchanged - it
already forced the bridging turn a 2-seat table needed), 4 for three
seats (new - restores the same mechanical bridge a 2-seat table already
had by construction, where it was previously missing). `close_allowed`
now takes `num_seats`, threaded from the one call site
(`engine.api.table_wiring._advance_open_round`). `__post_init__`'s
1<=floor<=cap<=6 ceiling check now validates every floor/cap pair across
both seat counts, not just a single flat pair. Full suite (561 tests)
green, including one existing 3-seat cap test whose own assertions
about when "close" first becomes legal moved from position 4 to position
5 (as they should - that's the exact behavior just fixed), and a new
dedicated test pinning the floor is genuinely seat-scaled while the
2-seat floor stays untouched.

**Not yet live-verified**: this changes real round dynamics again (a
3-seat round can no longer close before turn 4, matching what a 2-seat
round already couldn't do before turn 3) - needs its own live check
before considering it proven, same discipline as every other change
today. Not run yet.

Merged to main as PR #103 (`81b7a4d1`) once real CI (all 17 check runs,
the Netlify/Cloudflare preview noise aside) came back green.

### Floor-raise confirmed live by real production traffic, 2026-09-05

The next real 3-seat conversation on the site after PR #103 deployed
(cappadocian+alx+pahc, "who is jesus") reached exactly the bridging
second pass the fix targeted: four turns (Theon, Chilo, Chloe, then
Chilo again), the fourth turn opening with explicit agreement ("What
Theon and Chloe have said stands near us... we confessed both") before
pressing a genuine contrast (not a different belief - a different cost:
what it took under a hostile court to keep saying it). This is the
alignment-then-contrast shape from Mark's own design spec, not a
restated monologue, and it is the first live case where a 3-seat round
reached a real second pass since the floor was raised.

Mark asked to check the round's actual close reason to see whether it
closed right there or ran on. Investigated and found a genuine gap: the
production event log lives on Render's own private disk
(`/data/cic_api_events.db`, render.yaml), and no endpoint exposed
`round_closed`'s payload (reason/turns/governance/selector_reason) - the
transcript endpoint only ever returned the display transcript. No way
to answer the question from outside without either DB access (not
available from this session) or a new endpoint.

**Fix**: `engine.api.table_wiring.get_round_close_reasons(store,
session_id)` - re-derives state via `project_fresh` (same pattern as
`wiring.get_transcript`), returns every `round_closed` event's own
payload in round order. Wired up as `GET
/api/session/{session_id}/round-close-reasons`, gated by the exact same
per-session code the transcript endpoint already requires - no new auth
surface. Diagnostic-only: not part of the participant-facing product,
not linked from the frontend. Documented in `engine/api/README.md`
alongside the other endpoints. New test
(`test_round_close_reasons_endpoint_surfaces_selector_reason`,
`engine/api/tests/test_table_api.py`) drives a full round to a selector
close over real HTTP and checks the endpoint returns
`selector_reason`, checks the empty-list case before any round has
closed, and checks the same 401 gating as the transcript endpoint (no
code / wrong code). Full suite green (562 tests).

Still open: the session_id for that specific real conversation isn't
in hand (the browser UI doesn't surface it), so this endpoint answers
the question for the *next* production round Mark can capture a
session_id for, not retroactively for the one already shown.

### Structural fix for the recurring "closes on a full-table synthesis" failure, 2026-09-05

A third real production transcript (cappadocian+alx+pahc, "who is
Jesus") showed the identical shape as the second: four turns, the
fourth (Chilo's return) explicitly gathering Theon's AND Chloe's points
into one declared consensus - "The three of us are saying one thing,
from different rooms in the same house" - before adding its own weight.
Read on its own it's good writing; read as a pattern with the prior
example, it's the same move twice: a return turn resolving the whole
Table into agreement right at the floor.

Mark's ruling: "i dont want the voices closing the conversation as it
can continue... no smoothing, no coming together with a nice
conclusion, i want 5-6 interactions not 4." First response: raise the
3-seat floor again, 4->5 (RoundConfig.floor_by_seats), and add another
forbidding sentence to the second-pass directive text. Both changes
were built, tests updated, suite green - and then, before committing
anything, Mark stopped it: "i dont want fix on fix, this should be a
base program than generates this, not after fixes." Right call - both
changes were real, but neither touched WHY a return turn keeps reading
this way regardless of which turn number it lands on, and raising the
floor a second time in one day would only have moved the same collision
again. Reverted, unstaged, before either change was committed.

**The actual mechanism**: at a 3-seat table, positions 1-3 are always
everyone's first pass (nothing to return to before then). Whichever
position is the FIRST return is therefore always the first moment one
voice is looking at all three prior first-pass answers at once, with
nothing scoping it to one of them. The directive already said "zero in
on the one point... you do not have to touch everything" - a prose
request asking the model not to do the very thing all its available
material invites. Words lost to that structural pull both times it was
tried, at floor 4 and (untested) at floor 5 - moving the number moves
where the collision happens, not whether it happens.

**The structural fix, not another patch**: `engine.m4.turn_selector.
Selection` gained a field, `engages` - which ONE prior speaker a return
pick is meant to respond to, the turn selector's own job now (matching
Mark's own point 10, "it can zero in on a specific alignment or
disagreement... not everyone has to respond to both the others" - this
just makes that structural instead of aspirational). `_selector_tool`'s
schema carries an `engages` enum (the round's own speakers so far) only
once someone has spoken; `SELECTOR_SYSTEM_PROMPT` explains when to set
it. `_resolve_engages` (new, `engine/m4/turn_selector.py`) guarantees a
return is NEVER left unscoped, on every path: the model's own real
choice when it names a distinct prior speaker; deterministically the
most recent OTHER speaker in the round when the field is omitted,
names itself, or names a stranger; and the same deterministic
resolution on a forced move or the selector-unavailable fallback, which
never ask a model at all. The no-immediate-self-repeat rule
(`eligible_worlds`) guarantees `round_speakers[-1]` always differs from
whatever was chosen, so the deterministic fallback is always valid.

`engine.api.table_wiring._table_engagement_directive` gained
`engage_name` (the resolved target's own display name, looked up from
`labels` at the one call site) and its second-pass `focus` text was
rewritten around it: "This turn responds specifically to what {name}
said" replaces "where what the other voices said meets or parts" -
naming ONE voice is now a structural fact handed to the model, not a
plea not to survey everyone. Added alongside: an explicit "this
exchange is not concluding here" line, since the smoothing complaint
was never only about how many voices got named - a turn that ties even
ONE relationship into a tidy bow with a closing cadence still reads as
an ending.

RoundConfig's floor/cap were deliberately left untouched (still 4/6 for
three seats, from the prior merge) - tuning that number again before
seeing what a properly-scoped mechanism produces live would be the same
mistake with different numbers. Full suite green (571 tests: 9 new -
8 in `engine/m4/tests/test_turn_selector.py` covering `_resolve_engages`
and every path through `select_speaker` that calls it, 1 in
`engine/api/tests/test_table_schema.py` pinning the directive's new
scoped framing and its defensive fallback when no name is given).

Committed (`ee1a72c9`) and pushed to the designated branch (stop hook,
not yet merged to main) once the suite was green.

### Independent review (Opus, cold-read) - one real gap found and fixed, 2026-09-05

Findings, ranked, each verified against the actual code before acting
(never trusted at face value):

**HIGH, confirmed and fixed - the mechanism didn't actually enforce
scoping.** Naming one voice in the directive text is not structural
scoping if the turn's own context still hands it every OTHER voice's
full answer regardless - and it did: `table_history_for`'s `pending`
bucket has always carried everything said since a voice's last turn,
unfiltered, and `_context_prefix` renders it whole. A return turn could
still see (and use) material from a voice it wasn't asked to engage -
one sentence in the directive now named a target; nothing removed the
rest. This is precisely the "ask nicely, more specifically" pattern
Mark had just rejected, and the review said so plainly rather than
calling the diff done.

Fix: `_scoped_pending(pending, keep_labels)` (new,
`engine/api/table_wiring.py`) - keeps the participant's and Facilitator's
own lines always, plus the ONE engaged voice's; drops every other seated
voice's lines from THIS turn's context only. `table_history_for`'s own
session-memory reconstruction (`history`) is untouched - nothing is
forgotten, only left out of what this one turn can see. Verified with a
real end-to-end test
(`test_second_pass_turn_only_sees_its_engaged_voice_not_every_prior_answer`,
`test_table_api.py`) that drives a real 3-seat round to its first return
and inspects the actual rendered messages sent to the model: the
non-engaged voice's own words are genuinely absent, not merely
un-referenced in an instruction.

**MEDIUM, confirmed and fixed - `engages` was computed then discarded.**
`Selection.engages` never reached the `turn_selected` event - the exact
"computed once, then thrown away" gap `round_closed.selector_reason` was
built the same day to close for round closes, reopened for turn
selections. Fixed: `selected_payload["engages"]` added when not None,
same additive discipline (`events.REQUIRED_KEYS` is a floor).

**MEDIUM, confirmed and fixed - a real contradiction on one untested
combination.** `own_world_is_subject=True` + `is_second_pass=True`:
`stance` tells the voice to "confirm or correct what has been said of
your world" while `focus` said "never a correction of theirs" - both
cannot be true of the same turn, and no test exercised this exact
combination (a real coverage gap the review named directly). Fixed:
`focus` now branches on `own_world_is_subject` too - the subject branch
names which prior statement is in view and leaves the confirm-or-correct
instruction to `stance` alone, said once, never contradicted. New test:
`test_table_engagement_directive_subject_second_pass_names_its_target_without_contradiction`.

**LOW, confirmed and fixed - a wrong comment.** `_selector_tool`'s
`engages` enum comment claimed "seating-stable order"; it's actually
first-spoken order (`dict.fromkeys` on `round_speakers`, not
`world_keys`). Fixed the comment to describe reality.

**Walk-by, fixed while in the file - two pre-existing vacuous test
assertions.** `test_table_schema.py` and `test_table_api.py` each
checked a substring with a semicolon the code has never produced - an
`assert X not in Y` that was always true regardless of correctness,
predating today's work. Replaced with the real, distinguishing phrase
("drawn back in every time") that a final turn genuinely never contains.

**LOW, latent, left alone.** `_resolve_engages`'s "a return is never
left unscoped" guarantee depends on a caller invariant
(`last_speaker == round_speakers[-1]`) the function itself doesn't
enforce - true at the one real call site (traced and confirmed), and
one existing unit test happens to pass an inconsistent pair harmlessly.
Not fixed: no real bug, and hardening a function against a caller
discipline no real caller violates would be exactly the kind of
unrequested robustness this project's own build ethic argues against.

Also confirmed by the review, not a defect: 2-seat tables get the
mechanism too (harmless - `engages` always resolves to the only other
voice, pure naming with no functional change) and direct-address routing
never collides with it (guarded by `round_turns == 0`, which is
equivalent to `is_second_pass=False` there by construction).

Full suite green after fixes: 574 tests (3 new beyond the pre-review
571 - the contradiction test, the `_scoped_pending` unit test, and the
end-to-end context-scoping proof).

### Live proof (Mark's go-ahead: "go ahead, run the live proof") - the scoping fix confirmed, the length question isolated, 2026-09-05

Same seating and phrasing as the two most recent real production
transcripts (cappadocian+alx+pahc = Chilo/Theon/Chloe, "who is Jesus")
that both closed at turn 4 on a full-table synthesis. Floor (4) and cap
(6) deliberately untouched - the question was whether the properly-
scoped mechanism changes anything on its own, not whether a bigger
minimum forces it to. Report:
`engine/m4/reports/live-table-engagement-scoping-proof-2026-09-05.json`.

**The scoping fix is real, not cosmetic.** Position 4 (Chilo's return)
was logged with `engages: pahc` (Chloe) - a genuine selector choice, one
voice, not the whole table. Chilo's actual turn: "We would say yes to
every word Chloe has spoken... How calling Jesus God fits with calling
the Father God: that became our whole life's argument... So what Chloe
names as unworked-out, we worked out" - engaging Chloe's own named
unresolved point specifically, extending it with real Cappadocian
content (homoousios, hypostasis, the doxology story), with NO mention of
Theon or Alexandria anywhere in the turn. No declared consensus across
all three voices, no "different rooms in the same house" move - this is
the alignment-then-depth pattern the design always wanted, now actually
happening on a real call.

**The round still closed at turn 4.** The selector's own reason: "The
participant's initial question... has been fully answered by all three
voices... Another turn would restate rather than add. The exchange is
complete and genuine." Scoping fixed WHAT a return turn can say and see
- it did not touch WHEN the selector decides enough is enough, and that
judgment closed at the floor again, same as every prior run at every
floor value tried (3, 4). These are two independent mechanisms: content
quality and round length were never one root cause, just two symptoms
that happened to co-occur in the transcripts that surfaced this whole
investigation.

**What this settles and what it doesn't**: the "no smoothing, no false
conclusion" half of Mark's complaint is now proven, not just tested -
real evidence, not a hoped-for prose effect. The "5-6 interactions, not
4" half is untouched by this fix and needs its own lever - most likely
the floor itself, now on real evidence rather than a guess (raising it
again was properly held off, per Mark's own "no fix on fix" ruling,
until there was live data showing whether the scoping fix alone would
change round length; it didn't). Put to Mark, not decided here.

**Mark's call: "raise the floor to 5."** Given directly, on the isolated
evidence above - this time not a guess reacting to one bad transcript,
but a deliberate decision after the content-quality problem was already
fixed and proven separately. `RoundConfig.floor_by_seats`'s 3-seat entry
moves 4->5, his own original "5 being the ultimate zone" target from
the first design-enhancement ruling. The 2-seat floor (3) stays
untouched, as before - never observed closing early relative to its own
cap. Close is now legal only from the decision producing position 6
(the same decision the cap forces regardless), so 5 or 6 is the only
possible close point for a 3-seat round - matching "5-6 interactions"
exactly. Tests updated (`test_round_config_defaults_and_bounds`,
`test_round_config_seat_scaled_floor`,
`test_round_cap_closes_at_six_for_three_seats`); full suite green (574
tests, same count - no new tests needed, the seat-scaled floor
mechanism itself was already proven generically in the prior pass).

Not yet live-verified at the new value - the just-run proof was at
floor 4. Not yet committed.
