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
and evidenced. No fix executed yet — reporting to Mark before any record
edit, documentation change, gate addition, or regeneration spend.**

### Follow-on scope, logged not dropped

The broader "future/outside-vantage" defect class Mark named in interview —
anachronistic terminology, forward-referencing statements before their own
horizon, comparisons framed for a modern reader rather than stated from
inside the world — is real and almost certainly present beyond these three
textual forms, but has no defined census method yet and was deliberately not
attempted this session (scope-bounding agreed with Mark in interview). Next
assignment candidate, not this one.
