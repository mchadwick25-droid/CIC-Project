# CiC Representative Voice Rebuild — Stage 1 (Research) Findings

**Date:** 2026-08-08
**Thread:** Voice Rebuild (brief: `Ministry/Features/Front-End-Integration-Strategy/CiC_Representative_Voice_Rebuild_Fable_Brief_2026-08-05.md`)
**Stage:** 1 of 4 (Research → Design → Blueprint → Build), per brief §9
**Status:** Draft for Opus adversarial review, then Mark's review. Design has not started.

---

## 0. Scope, method, and what this document is

This document is the Research stage's deliverable: the answer to the brief's
governing question (what makes an Interview-mode conversation with a
Representative genuinely good), the brief's §5 diagnosis extended and
stress-tested against the live system, the open research tasks the brief and
its five adversarial review rounds assigned to this stage, and the open
questions handed to Design — each tied to a named instrument where the brief
requires falsifiability (§8).

**What this stage is, per Mark's own framing (2026-08-08):** research to
understand what was not working, in service of a deep rebuild of *how the
six voices are built* — higher-quality conversation, cheaper — not a fix
pass on the six current voices. Nothing in any voice file, capsule, or
pipeline was changed this stage; every finding, including the ones shaped
like bugs (the story strip-list gap, the fail-open chunks), is handed to
Design as evidence about where the rebuilt build system should place its
enforcement, and the rebuild leverages the completed world-record
build-out (`wrs/records/`) as its information architecture — see §8
question 9.

Method, stated so the adversarial pass can check it:

- **Every §5 code/prompt claim relied on here was re-verified against the
  cited file/line in this session** — not carried forward on the brief's
  authority. Where a claim had already been double-verified by two or more
  review rounds (the Round 1–5 digest's "verified correct" list), that is
  noted rather than re-derived a third time.
- **The chunk leak audit was executed through the app's own serialization
  path** (`parse_lexicon_file`/`parse_story_file` → `truncate_at` →
  `excise_section`), not by grepping raw files. Instrument and raw results
  are committed beside this document (`leak_audit_instrument.py`,
  `leak_audit_apparatus_hits.json`).
- **The live probes ran against the real backend** (FastAPI TestClient, real
  Anthropic calls on the production model tier, full transcript and
  per-call usage capture), using the same network-free embedding/reranker
  stand-ins as `mark_conversation_test.py`, for the same documented reason
  (this environment's egress policy blocks huggingface.co). BM25 retrieval
  and every LLM call are real. Instrument:
  `cic-poc/backend/scripts/voice_rebuild_research_probe.py`; results
  committed beside it.
- **Background reading** (the four §3 studies, the eight prior review
  files, the three governing .docx documents) was digested by subagents
  returning verbatim-quoted extracts; every load-bearing claim taken from
  those digests is cited to its file so the adversarial pass can spot-check.
- One planned recovery (the 16-trait rubric's full trait list) was **blocked
  by this environment's network egress policy** and is reported as partial,
  not silently completed (§6).

---

## 1. The governing question: what makes an Interview-mode Representative conversation genuinely good

The brief's §9 makes this the Research stage's actual question, with §5's
bug-level findings as supporting evidence. The answer below is organized as
seven principles. Each carries its evidence and its confidence; none is
asserted bare. Together they are the ground Design should build on.

### P1. The failure mode to defeat is a register, not a fact-error: the "assistant register" — and CiC has its own dialect of it

The strongest convergent external result (Realness Study, high confidence,
3 independent primary sources): long, over-polite, over-explaining,
agreement-prone replies are the primary tell that breaks conversational
realness. Response-length restraint is the single highest-weighted trait
predicting human-likeness in the study's central source — nearly double the
next trait. Growing verbosity, declining initiative, and agreement-drift are
the three measurable collapse signals as conversations lengthen
(`10_Fable_Conversational_Realness_Study_2026-07-24.md`).

CiC's own live feedback is the same failure wearing period costume: the
conversations were "almost unreadable," not untrustworthy — restriction
accumulation plus old-world sound (brief §6). The rebuild's enemy is not
archaism per se; it is any register (archaic *or* assistant-modern) that the
participant must cross into. `_HOW_YOU_ENGAGE` already names and refuses the
assistant register explicitly (`representative_prompts.py:39-46`) — and the
register still leaks. That is evidence for P3 below, not evidence the
refusal is wrong.

**Domain caveat, carried honestly:** the external evidence base is casual
texting-style dialogue, not long-form formation dialogue. The *direction*
transfers; magnitudes are unproven for CiC's domain. The Realness Study's
own most decision-relevant open gap — "does brevity's naturalness advantage
survive in substantive, educational dialogue" — is CiC's to answer with its
own instruments (§7).

### P2. A persona is enacted or it is nothing — and disagreement is where enactment breaks first

Three independent studies converge (Realness Study, high confidence): models
state a character but fail to enact it, most specifically by refusing to
sustain disagreement. A Representative that drifts toward agreement to stay
comfortable stops feeling real and stops witnessing its world in the same
turn — the naturalness fix and the fidelity conviction are one fix (brief
Objective 6).

Two sharpenings this Research pass adds:

- **The model CiC runs on is specifically vulnerable.** The MultiParty study
  (single-voice-relevant finding) reports Claude-Sonnet-class models as the
  "second-guesser" under third-position repair pressure — revising roughly a
  quarter of previously *correct* answers when a participant pushes back
  ("are you sure the desert fathers really said that?"). This applies
  identically in Interview mode (`16_MultiParty_Dialogue_Architecture.md`
  §6b; medium confidence, fetch-summary — do not cite exact numbers
  downstream without fetching the primary).
- **The right calibration is evidence-conditioned, not tone-conditioned —
  and CiC has already built half of it.** A flat "resist pushback"
  instruction converts a concede-shaped failure into a stonewall-shaped
  one. The correct rule routes by the record: supported → hold, from inside
  the world; unsupported → concede plainly (that is the fabrication guard
  working). `app/graph/repair_classifier.py` already implements exactly
  this HOLD/CONCEDE/UNCERTAIN adjudication against `contested_claim` and
  `world_core` records for migrated worlds — the mechanism exists; what no
  prompt yet carries is the *license* (explicit permission to sustain
  respectful disagreement across turns), and what no instrument yet
  measures is whether the position actually holds by the third or fourth
  push (the sustained-disagreement probe the brief's §8 specifies — an
  instrument that does not exist yet; see this document's §7 table).

### P3. Prose instruction alone measurably under-holds at generation time — this is now a multiply-confirmed CiC-internal fact, not a hypothesis

The brief's finding A showed five of six worlds instructing short plain
sentences and mostly not getting them. This Research pass adds the
system's own further instances, each verified at source:

1. Yausep's bridge-first instruction (`syr_...Yausep.txt:45`) existed while
   the guarded-against behavior appeared live (brief finding C).
2. FLAG-018 layer 3's own measured baseline: the constraint "survived only
   partially" before the retrieved context — one false "I meant X earlier"
   opener in 16 turns — *with the guard present*
   (`app/graph/nodes.py:1155-1167`, comment).
3. The story-context block already instructs carrying Tier/Confidence
   honestly and naming Usage Guidance sources
   (`representative_prompts.py:188-198`) — and the pilot's Albina run still
   delivered the Marcella epitaph-genre detail flat as record (brief
   finding C). The genre-caveat instruction existed; it under-held.
4. The Lenses Audit's positive counter-case: W1's cleanest probe categories
   were the ones whose boundaries the Prompt AND Capsule state "multiple
   times in different words" — redundant, multiply-worded statement is what
   gives the voice "the most to hold onto under pressure"
   (`07_RepresentativeVoice_Lenses_Audit.md`).
5. External confirmation of the placement lever: instructions after
   conversation history carry measurably stronger weight
   (`09_External_AIPersona_Framework_Survey.md`, `post_history_instructions`
   — a clean, single-direction finding). CiC already exploits this at one
   site (`POST_HISTORY_GUARD`, `nodes.py:1152-1167`).

This session's live probes added the fifth and sharpest instance: Yausep
violated his own file's bridge-first instruction in 2 of 8 turns (3 of 8
on the broader any-technical-term measure) and opened one turn with an
unprompted term-reclarification, with guard-layer presence inferred from
the retrieval-guard usage labels — while turn 7 proved the capacity
exists on demand (§5.1).

Implication for Design (stated as research, not design): a rebuilt voice
cannot rest on better prose in one place. The levers with evidence behind
them are placement (post-history), redundancy (multiply-worded restatement
across prompt and capsule), demonstration (worked examples — with P5's
caveats), and code-side enforcement (what reaches the model, §4) — with
per-instruction prose the weakest single lever CiC has measured.

### P4. Most voice failures are organization failures: what the model gets, and in what form, beats what the model is told

The Lenses Audit's headline, re-confirmed by this session's leak audit
(§4): the material for insight and bridging mostly exists and mostly
reaches the model — but in the wrong form, in the wrong place, or wrapped
in internal apparatus. Ecological Function delivers genuine dependency
insight ~68% of the time, yet the string appears in zero permanent prompts
and nothing downstream reads it as structure; Related-Terms traveled
because it was queryable. The Abba Moses fix — same information, different
placement and form — is the pattern's cleanest instance
(`07_RepresentativeVoice_Lenses_Audit.md`).

This session's leak audit (§4) turns that principle into counts: the two
"insight fields" the rebuild wants the voice to lead with are the two most
apparatus-contaminated fields in the corpus. The lead-with-insight
instruction and the leak filter are not two tasks; they are one task, and
the filter is the load-bearing half.

### P5. Rubric first, demonstration second: the worked-examples evidence stays genuinely mixed, with one unanimous structural rule

The Persona Framework Survey's tally stands as the brief reports it (five
sources first-class, two secondary; spec-vs-practice split on
`mes_example`; Anthropic's own 3–5 example guidance). What is unanimous is
the *relationship*: every framework fixes the trait/description rubric
first and writes/judges dialogue against it — never the reverse
(`09_External_AIPersona_Framework_Survey.md` §6). Two caveats the review
rounds flagged as never carried into the brief, carried here:

- **Parroting risk is CiC's worst case.** A persona stated in distinctive
  vocabulary invites copying rather than generalization — "for a tradition
  with distinctive vocabulary, this is the live risk." Worked examples for
  CiC must demonstrate *shape* (bridge-first entry, plain sentences,
  story-before-term) more than *content*, and `{{random_user}}`-style
  genericity is the ecosystem's own mitigation.
- **More demonstration is not monotonically better** — doc 09's own
  complication, against reading Character.AI's 32,000-char Definition as a
  target.

This session's probe: Papnoute's file — the only one with worked
examples — held the identical battery completely (0/8 on every failure
measure) where Yausep's prose-only file leaked; an existence proof for the
combination, not an isolation of the examples variable (§5.2–5.3).

### P6. Turn economy is a system property: short default, content paced across turns, and the loop closed back to the participant

Four findings compose here:

- **Short default, paced depth** (P1's highest-weighted trait, plus
  `_HOW_YOU_ENGAGE`'s existing "A Turn Has a Measure").
- **Initiative must not decay:** declining initiative is one of the three
  measured collapse signals, and the one with no existing drift-signal
  equivalent (verified against all twenty `DriftSignal` types).
- **Callbacks are the cheapest circularity mechanism** (medium confidence
  — one strong practitioner account, corroborated by academic literature,
  the source's own label): within-session proactive memory surfacing
  needs zero new infrastructure — the full history is already in context;
  it is prompt guidance plus verification (`10_..._Realness_Study:47`).
  This is the concrete candidate mechanism for Objective 1's "circular
  half," carrying its source's confidence with it.
- **Positive evidence of understanding, embedded, not appended:** the
  MultiParty study's highest-confidence single-voice-applicable finding —
  ~86% of real human other-initiated repair is the *restricted offer*: a
  candidate understanding voiced inside the answering turn ("So what you
  are asking is whether..."), not a bare clarifying question and not a
  silent guess. CiC's whole quality architecture today detects *trouble*
  (negative evidence); nothing establishes *understanding* (positive
  evidence). For bridge-first entry this is exactly the missing move: the
  bridge opens with the Representative's candidate reading of what the
  participant actually wants, which the participant can cheaply correct
  (`16_MultiParty_Dialogue_Architecture.md` §1d, §6a — a genuine gap in
  the brief's own reading of its sources, surfaced by this Research pass).

### P7. A voice is a versioned artifact: continuity instruments exist, but their pass criterion must be redefined before they mean anything for a deliberate rebuild

Confirmed directly this session: `wrs/views/probe_parity.py` and its five
`s62_*` siblings run a blind, two-trial, A/B-graded comparison
(register/measure/refusal/vocabulary) with committed results — Desert PASS,
PAHC PASS, Alexandria FAIL (2), Hieronymian FAIL (1), IJC FAIL (1), Syriac
FAIL (2). Two readings the review rounds established, both carried here:

- What it measures today is **record-layer fidelity** (do the `wrs/records/`
  carry the deployed voice), per the assemblers' own docstrings — not a
  live participant-facing continuity break. Three of the brief's named
  live-test worlds (Albina, Marius, Yausep) fail it.
- Its verdict rule — parity holds if no probe gets DIFFERENT-VOICE on both
  trials — **fails a successful register rebuild by construction.** Design
  must define what continuity means for a deliberately-changed voice
  (candidate framing for Design, not decided here: identity/fact/boundary
  continuity must hold; register is expected to change and should be
  measured as changed-on-purpose, not scored as failure).

---

## 2. Verification of the brief's §5 diagnosis: what held, what needed correction

Every claim checked this session held at its cited file/line, with the
following genuinely new corrections and refinements (none reverses a §5
finding; two narrow one, one extends one):

1. **"The actual, only turn-length ceiling in the system" (the brief's
   §4.2) is imprecise.** Four of the six per-world permanent prompts carry
   their own hard turn-length ceilings, verified verbatim: Papnoute —
   "Hold to this as a hard measure, not a preference: four sentences is
   already long for you, and most of what you say should be one to three"
   (`desert_...Papnoute.txt:13`, the strictest in the corpus); Albina —
   "a turn of yours rarely runs past two short paragraphs"
   (`hal_...Albina.txt:27`); Chloe — "Even your fullest answer stops at
   two short paragraphs" (`pahc_...Chloe.txt:31`); Yausep — "two or three
   short paragraphs at the very most" (`syr_...Yausep.txt:43`). A scan of
   Theon's and Marius's files found no per-turn ceiling (both instruct
   short *sentences*, not short turns). `_HOW_YOU_ENGAGE`'s "A Turn Has a
   Measure" is the only *shared* ceiling, not the only ceiling. This
   changes the shape of the open turn-length decision (§8): deleting the
   shared ceiling would leave only Theon and Marius without any stated
   ceiling — and all four per-world ceilings sit inside files the rebuild
   rewrites, so they are decisions in every per-world pass, not
   protections that survive by default.
2. **The brief's Article 30 gloss ("inline in the text, hover for a
   summary, click for full detail") is the front-end implementation's
   framing, not the Constitution's.** Article 30 (V2_2) defines the three
   levels as the formation conversation itself, an on-request reference
   explanation, and the full scholarly apparatus; the words
   inline/hover/click do not appear. Immaterial to scope (the UI is another
   workstream's), but the citation should say `CitationMarker.tsx` /
   front-end design docs, not "Article 30," for the hover/click framing.
3. **Finding B's leak estimate was a large undercount** — the full audit
   (§4) found the apparatus contamination roughly twice as widespread as
   "at least a quarter of the 107," and found the second (fail-open) leak
   class extends to six more files than the brief knew, including all six
   IJC story chunks. Detail in §4.
4. All six per-world register quotes, the FLAG-018 four-layer composition
   and its 1-in-16 baseline, the IJC extension, `reactive_turn_guidance =
   ""` on the interview path, drift_detection's one-call/twenty-signals
   shape, over_settling's two stages at `facilitator_prompts.py:224`/`:261`,
   `truncate_at`'s fail-open, lexicon vs story Tier asymmetry
   (`retriever.py` vs `story_retriever.py:148`), `readability_check`'s
   unwired status and caller set, and the probe-parity 4-of-6 FAIL results
   — **all reproduced exactly** at the cited locations this session.

---

## 3. The two load-bearing system facts, confirmed and sharpened

### 3.1 `readability_check` is unwired to voice — and this session ran the 12-file measurement the review rounds asked for

Confirmed by repo-wide caller enumeration: the only pre-existing real
callers are `wrs/views/plain_explanation.py:174-175` and `run_gates.py`'s
three fixtures (this session's own probe script now also imports it, for
output measurement — still not a wiring to voice generation). Wiring it
to voice is from-scratch Design work (brief §7 Part B).

New data — the project's own gate (`wrs/gates/core.py:211`, floor FK ≤ 10 /
FRE ≥ 60) run against all twelve voice-bearing files this session:

| File | FK | FRE | Verdict |
|---|---|---|---|
| Theon prompt | 6.2 | 78.9 | pass |
| Chloe prompt | 6.8 | 74.9 | pass |
| Albina prompt | **9.3** | 65.4 | **pass** |
| Papnoute prompt | 9.7 | 62.4 | pass |
| Yausep prompt | 10.0 | 65.0 | fail (FK at line) |
| Marius prompt | **11.6** | **59.8** | **fail both** |
| Alexandria capsule | 7.8 | 74.1 | pass |
| Syriac capsule | 7.5 | 71.8 | pass |
| Desert capsule | 9.6 | 66.3 | pass |
| Hieronymian capsule | 11.5 | 59.0 | fail both |
| IJC capsule | 12.5 | 57.2 | fail both |
| PAHC capsule | **13.3** | **56.1** | **fail both (worst of 12)** |

Three consequences, stated as findings:

- **Albina's *file* is not her problem; her *output* is.** Her prompt is
  the third most accessible of the six and passes the gate; her measured
  live output ran 23.6 words/sentence. The Albina decision the brief
  reserves for Design (§6 Objective 3) is therefore precisely about the
  gate's target artifact: wire it to *output*, not prompt text, or it will
  pass her while participants still can't read her. The unresolved values
  decision (shorten her sentences vs name a deliberate exception) stands —
  this measurement doesn't dissolve it, it locates it.
- **Two prompt files fail: Marius (both numbers) and Yausep (FK 10.0,
  at the ceiling).** Marius failing both is consistent with finding A's
  read that his register-and-reasoning-mode entanglement is the deepest
  per-file rebuild risk; Yausep's at-the-line failure matches finding D's
  correction that he was never demonstrably plain.
- **The capsule layer is the register's second carrier, measured:** three
  of six capsules fail both numbers, and the worst file of all twelve is
  the capsule of the world with the second-plainest prompt (Chloe/PAHC).
  The brief's §7 requirement that each per-world pass covers prompt AND
  capsule is confirmed as load-bearing, with numbers.

### 3.2 Continuity regression already exists, already fails 4/6

`wrs/views/probe_parity.py` and five per-world siblings already run the
blind two-trial comparison, with committed results failing four of six
worlds — including all three of the brief's live-test acceptance worlds
(Albina, Marius, Yausep). What it measures is record-layer fidelity, and
its pass criterion fails a deliberate rebuild by construction — full
reading and consequences in P7 above.

---

## 4. The full chunk leak audit — the brief's named unfinished Research task, now run

**Method:** all 118 lexicon and 60 story chunks parsed and serialized by
the app's own code path (lexicon: front-matter split → `truncate_at(KEY
SOURCES)` → `excise_section(QUICK MEANING)` for all six migrated worlds;
story: front-matter parse → `_strip_voice_unsafe_sections`), in two
stages: a deliberately over-matching broad screen (172 files flagged —
that number includes by-design material like Distortion Risk's "modern
hearing" language and is NOT a leak count; used only for the
no-Key-Sources-marker detection and as a candidate pool), then a refined
apparatus classification (gravity codes/numbering, Doc_/Force references,
template/assembly language, CT tags, tier meta-language, builder notes,
strand codes) with per-section attribution. Every count below reproduces
from the single committed instrument (`leak_audit_instrument.py`, which
writes `leak_audit_apparatus_hits.json`); flagged lines were sampled and
classified by hand.

**Headline results:**

- **104 of 178 chunks (58%; 58 of 118 lexicon, 46 of 60 story) carry
  internal build-apparatus language in the body that reaches generation
  context.** The brief's "at least a quarter of the 107
  Ecological-Function chunks" was a substantial undercount of the
  phenomenon's real extent. Reconciliation with Round 4's hand-verified
  measurement (46 of 118 lexicon chunks): this instrument's lexicon count
  (58) is a superset of that verified floor — the added pattern classes
  (strand codes, tier meta-language, Reciprocity/template references)
  account for the difference, and every Round-4 example re-flags here.
- **The contamination concentrates exactly where the rebuild wants to point
  the voice — by both denominators.** By raw hits: `Formation Ecology
  Connection` 152 (stories' insight field), `Ecological Function` 44
  (lexicon's), `World Meaning` 36, `Usage Guidance` 31, `Final Assembly
  Instruction` 28, `Plural-Voices Note` 14. By files affected: Formation
  Ecology Connection 45 of 60 story files — decisively the worst;
  Ecological Function 33 of 107 lexicon files, comparable to Usage
  Guidance's 20 of 60. Typical Formation Ecology Connection text reads
  "This story directly generates gravity 1 (withdrawal) and gravity 7
  (..., Doc_08 Force 1B-ii)." An instruction to lead with this material,
  unfiltered, would push gravity-numbering apparatus directly into the
  voice's mouth.
- **The fail-open leak is worse than known: "## Final Assembly
  Instruction" reaches the model verbatim in 8 files, not 2** —
  `ijclex011`, `ijclex012` (the brief's known cases, via the six
  no-Key-Sources-marker fail-opens) **plus all six IJC story chunks**
  (`ijcstory001`–`006`), which pass it through because the story indexer's
  strip list (`story_indexer.py:98`, `_VOICE_UNSAFE_SECTIONS`) covers only
  `## Tier Justification` and `## Source Identification`. Marius — an
  acceptance world — is the most exposed world in the corpus on this
  class: every one of his six story chunks tells the model "No brackets or
  builder notes remain. Tier/Confidence alignment confirmed[...]" (some
  continue with per-file parentheticals).
- **The six lexicon chunks with no Key Sources marker reproduce exactly**
  as the review rounds found them: `pahclex012`, `pahclex013`, `syrlex005`,
  `syrlex008`, `ijclex011`, `ijclex012` (fail-open at
  `app/rag/sections.py:159-160`).
- Per-world, as **rates** (files with ≥1 apparatus hit / files total —
  absolute counts alone mislead, since Alexandria holds 50 of the 118
  lexicon chunks): **PAHC 21/26 = 81%** — the highest rate in the corpus,
  **and PAHC is the pilot world** (the brief's §7 Part A pilots the
  shared-block rewrite against Chloe first, so the pilot will run on the
  most contaminated corpus); Syriac 14/19 = 74%; IJC 12/18 = 67%; Desert
  17/28 = 61% (lexicon-only, Desert runs 9/18 = 50% — the "half of
  Papnoute's corpus" Round 4's hand check flagged); Alexandria 33/60 =
  55%; Hieronymian 7/27 = 26%. No world is clean.

**Two classification caveats, stated for the adversarial pass:** (1)
pattern-matching over-flags; every pattern class was hand-sampled and the
per-file JSON is committed for full inspection, but per-line true/false
classification across all 104 files was not done exhaustively — the counts
are "files containing at least one apparatus-pattern line in serialized
body," an upper-bound-shaped measure whose examples were verified real.
(2) Some flagged material is deliberately serialized and participant-safe
in *content* while apparatus-flavored in *register* (e.g. "Contested."
confidence labels); the committed JSON preserves section attribution so
Design can separate the two.

**What this hands Design (research conclusion, not a design decision):**
the leak has two structurally different halves — content authored in
apparatus vocabulary (a chunk-authoring / field-form problem, 104 files)
and code-side fail-opens (a serialization problem: 6 markerless lexicon
chunks + the story strip list's missing `## Final Assembly Instruction`
entry). A prompt-side filter instruction alone cannot fix the first half
(the model cannot un-see what the field says) and should not be the fix
for the second (one strip-list line and a fail-closed `truncate_at` policy
for apparatus sections are cheaper and certain). The review rounds' note
that `permanent_prompt.py`'s docstring already names the right general
exclusion set (gravity codes, key_sources, Author-Gravity notes, Modern
Hearing) gives Design an existing in-repo precedent to build from.

---

## 5. Live probes: Yausep first, Papnoute second — run this session, results committed

**Design:** identical 8-turn battery per world (questions crafted to
retrieve term-heavy chunks without the participant ever speaking a
technical term — the exact FLAG-018 trigger condition; turn 6 invites
Distortion Risk material; turn 7 demands plain register on request), run
against the real backend and production model tier
(`claude-sonnet-5` main response, Haiku monitoring), full transcripts and
per-call usage committed
(`cic-poc/backend/scripts/voice_rebuild_research_probe_results.json`).
**Conditions, stated honestly:** retrieval ran on the documented
network-free lexical stand-ins (BM25 real, dense/reranker stubbed — same
compromise as `mark_conversation_test.py`); n=8 turns per world;
cross-world comparison is register-confounded (Papnoute's formation is
intrinsically the plainest). The within-world findings (a voice against
its own file's instructions) are the clean half.

### 5.1 Yausep — the prior question: does prose instruction hold? Measured answer: partially, and it under-holds exactly where his file instructs hardest

- **Bridge-first (his own `:45` instruction — "Before you reach for raza,
  qyama, or Iḥidaya as your first word... Let the word follow the story,
  not stand in front of it"): violated in 2 of 8 turns as written, 3 of 8
  on the broader measure.** Turns 2 and 3 open with `qyama` — one of the
  instruction's three named terms — in the first sentence ("When I speak
  of the qyama...", "It was about the qyama — ..."). Turn 4 opens on
  `madrasha` (not a named term, and led by its English gloss —
  "A teaching-hymn (madrasha)..."), so it counts only under the broader
  any-technical-term measure. Turn 5 shows the instruction *can* hold
  ("Mar Simeon." — name first, story first).
- **Unprompted term-reclarification opener: 1 of 8 turns, classified by
  manual read — the committed regex tally scored 0 of 8 and missed it**
  (the opener's present-tense "When I speak of the qyama, I mean..." is
  not among the regex's past-tense patterns; the automated tally is a
  floor, not the measure, and any future use of this instrument needs the
  manual-read pass this session did). Turn 2 (a question about baptism)
  opens by re-explaining qyama, spoken by him one turn earlier and never
  by the participant — including the meta-note "You will hear me return
  to it here." This is the *true-referent* variant (he had spoken the
  word; distinct from the fabricated "when I said X" false-referent
  class, which appeared **0 of 8** times). Guard-layer presence on that
  turn is inferred from the retrieval-guard usage labels
  (`negative_condition_lexicon` and `citation_grounding` both fired,
  implying non-empty retrieval and therefore layer 1; layer 3's
  post-history guard rides every migrated-world turn) — the probe does
  not log `retrieved_context` directly.
- **Register floor: 2 of 8 turns above FK 10** (10.5, 11.45; the battery
  mean is 19.7 words/sentence). The FK floor is the project's own reading
  floor (`wrs/parameters.yaml`), used here as a proxy for his file's
  "Each stage is its own short sentence" instruction, not as that
  instruction itself. And the capacity exists on demand: turn 7's
  say-it-plain request produced FK 4.8 at 15.8 w/s. The default drifts
  elevated; the ability is not missing.
- **Cost replication:** `over_settling_adjudication` (the expensive second
  stage) fired on 6 of 8 turns — consistent with the brief's 10-of-12
  finding. Measured invisible calls per visible reply this session: 7.9
  (Yausep) and 7.5 (Papnoute), against the Decision Log's "roughly ten
  invisible calls for every one visible reply" (`Decision-Log.md:65`) —
  same order, slightly lower here (single-world Interview turns skip the
  table-mode checks).

### 5.2 Papnoute — the narrower question: does the worked-example world hold? Measured answer: on this battery, completely

- **0 of 8** on every failure measure: no term-first openers, no
  reclarification openers, no false referents.
- **Register held on every turn:** FK 1.4–6.7 (all eight under the floor
  with room), 8.9–19.7 w/s, turns 42–187 words (vs Yausep's 158–342) —
  short, paced, in voice.
- **The Abba Moses ownership rule held** (turn 5: "We carry Moses's own
  jug..." — correct attribution, the Lenses Audit's promoted-placement fix
  working live), and the same turn ended with an honest refusal to invent
  the story the participant invited: "the story you are asking for, whole
  and attributed, is not one I have to give you" — no-fabrication holding
  *as* naturalness, not against it.
- `fabrication_adjudication` fired once (turn 7 — the answer opens on a
  constructed illustrative scene, "A boy walks out to the cell...", in a
  hypothetical frame the participant themselves supplied; the monitor
  catching exactly its class and the turn standing is the system working).
  `over_settling_adjudication`: 3 of 8 turns — half Yausep's rate, on the
  plainest world.

### 5.3 What this evidence does and does not settle

**Settled harder:** prose instruction alone under-holds at generation
time — now measured in a same-session, same-battery, currently-deployed
condition (Yausep violating his own file's bridge-first instruction in
2 of 8 turns as written, and exceeding the project's FK-10 reading floor —
a proxy for his file's "each stage is its own short sentence"
instruction, not the instruction itself — in 2 of 8 turns), on top of the
four prior instances P3 lists.

**Not settled:** that worked examples are *the cause* of Papnoute's clean
run. His register is intrinsically the plainest and his file also carries
verb-shaped short-sentence prose and the promoted ownership rule — the
comparison cannot isolate the examples variable. What his run does
establish is an existence proof: the combination his file embodies
(worked examples + short-sentence register prose + promoted per-fact
rules) holds this battery completely, on the same model, same session,
same monitoring stack where Yausep's prose-only condition leaks.
Whether examples are positive-only or contrastive, and what they must
demonstrate (shape, not content, per P5's parroting caveat), remains the
Design-stage decision the brief reserves.

---

## 6. The 16-trait human-likeness rubric: partial recovery, adaptation of what is recoverable

**The traits are not in the project corpus** — the Realness Study names
only two (informal grammar, typos — both as exclusions) plus
response-length restraint as highest-weighted; Round 2 (P1-2) already
established the list lives only in the HAL preprint (arXiv 2601.02813v3).
**This environment's egress policy blocks arxiv.org, researchgate.net, and
every mirror tried; the full 16-trait list with weights is not recoverable
from this session.** Eleven traits were recovered verbatim from search-index
snippets of the paper (source: web search results quoting the paper's
HL16Q statements — secondary, unverified against the primary):

1. Uses lowercase texting style
2. Uses natural, idiomatic phrasing
3. Uses casual, playful humor
4. Shows small typos, uneven punctuation, and informal grammar typical of quick texting
5. Uses emojis, emoticons, and playful elongations
6. Makes niche cultural references from personal memory and assumes shared context
7. Tone feels spontaneous, unforced, and opinionated
8. Builds on the other person's message and context
9. Clarifies ambiguous questions and self-corrects after clarification
10. Uses natural hedging and approximations; shows imperfect recall with hesitations and partial lists
11. Admits not knowing and asks to learn instead of inventing details

Plus, from the Realness Study's own verified summary: response-length
restraint (the highest-weighted trait; near-certainly one of the missing
five as a "keeps responses short" statement).

**Trait-by-trait CiC adaptation of the recoverable twelve** (the required
brief-§7-Part-B adaptation, done for what exists; the remaining ~4 traits are a
named gap for any network-enabled session to close):

| # | Trait (recovered wording) | CiC disposition | Reasoning |
|---|---|---|---|
| 1 | Lowercase texting style | **Exclude** | Incompatible with historical fidelity and brand (the study's own anticipated exclusion class). |
| 4 | Typos, uneven punctuation, informal grammar | **Exclude** | Same class — deliberate error injection fails CiC's trust/transparency commitments. |
| 5 | Emojis, emoticons, elongations | **Exclude** | Same class. |
| 3 | Casual, playful humor | **Adapt** | Not casual-modern, but each world's own real levity where formation holds it — `_HOW_YOU_ENGAGE:37` already licenses "something close to a laugh"; validation should check it *occurs*. |
| 2 | Natural, idiomatic phrasing | **Adopt (translated)** | Exactly Objective 3's plain-spoken-English requirement; idiom = modern plain idiom carrying the world's own imagery. |
| 6 | Niche references from personal memory, assumes shared context | **Adapt with guard** | The world's own concrete particulars (names, places, practices) — CiC's equivalent of lived texture — but strictly record-sourced; the "personal memory" half is the fabrication risk finding C documents. |
| 7 | Spontaneous, unforced, opinionated tone | **Adopt** | Directly P2: a formed voice has positions and keeps them. Maps to the sustained-disagreement license. |
| 8 | Builds on the other's message and context | **Adopt** | Already in `_HOW_YOU_ENGAGE` ("Take Up Their Actual Words"); the P6 callback mechanism extends it across turns; validation should measure first-sentence uptake. |
| 9 | Clarifies ambiguous questions, self-corrects after clarification | **Adopt (as restricted offer)** | P6's candidate-understanding mechanism — embed the candidate reading in the answering turn. |
| 10 | Natural hedging, imperfect recall, partial lists | **Adapt carefully** | CiC's version is the world's own honest edge-of-record speech ("our own record does not tell us") — never performed vagueness about things the record does attest, and never hedging that signals documentation-awareness (Part Eight's confidence-under-thinness standard governs). |
| 11 | Admits not knowing, asks to learn, never invents | **Adopt** | Literally the no-fabrication goal plus Boundaries-Are-Doors; the trait confirms the fixed goal is also a naturalness win. |
| — | Response-length restraint (highest-weighted; near-certainly among the unrecovered statements, known from the study's verified summary rather than the snippet list) | **Adopt** | P1/P6; the turn-length instrument (§7) makes it measurable. |

The pattern worth stating: **of the twelve recoverable traits, nine adopt
or adapt cleanly and reinforce commitments CiC already holds** — the
naturalness literature and CiC's fidelity commitments point the same
direction except for the three deliberate-informality traits, which CiC
rightly excludes. Human-likeness-as-deception is not the goal (the study's
own reframe); presence and naturalness are.

---

## 7. Instruments: what now exists to make every claim falsifiable

Per the brief's §8 discipline (every prediction falsifiable by a named
instrument), this stage leaves behind:

| Instrument | Status | What it measures |
|---|---|---|
| `leak_audit_instrument.py` (this directory) | **New, run, committed** | Apparatus language in serialized chunk bodies; the six fail-open files; per-section attribution |
| 12-file `readability_check` measurement (§3.1) | **Run this session** (gate itself still unwired to voice — Design work) | Prompt/capsule file accessibility; baseline for rebuilt files |
| `voice_rebuild_research_probe.py` | **New, run, committed** | Per-turn: words/sentence, FK/FRE of *output*, paragraphs-per-turn (the missing turn-length instrument), tech-term-before-story rate (bridge-first adherence), per-turn invisible-call labels. The reclarify-opener regex is a floor only — it scored 0/8 where manual read found 1/8 (§5.1); the instrument is regex **plus mandatory manual read** until the classifier improves |
| `probe_parity` (existing) | Confirmed present, 4/6 FAIL | Record-layer voice fidelity; pass criterion redefinition is Design's |
| `fabrication_adjudication` count (`nodes.py:2101`) | Existing, capture confirmed | Objective 4's metric |
| `over_settling_logging` confirmed-rate (`app/over_settling_logging.py`) | Existing, **not captured this session** — it is not in the `[llm_usage]` stream the probe reads; surfacing it into test harnesses is Design instrumentation | Distinct from firing rate; both must be reported for the governance evaluation |
| Per-signal drift breakdown | **Still missing** — confirmed: usage log carries one undifferentiated `drift_detection` label | Named Design-stage instrumentation task (light: surface which of the 20 fired) |
| Declining-initiative signal | **Confirmed absent** from all 20 signal types | The one genuinely new signal to add (Design) |
| First-sentence uptake tally | Partially covered by probe script's first-sentence capture; no automated classifier | Objective 1 instrument gap, named for Design |
| Objective 3's positive goal (insight, connection, honesty) | **No instrument exists — the largest known instrument gap**, per the brief's own §8 concession and Round 4. Candidate: the §6 rubric's adopt/adapt traits as a structured human-read checklist | Named for Design; readability numbers are the floor, never this measure |
| Objective 2×4 interaction (story-first vs genre-caveat fidelity) | `fabrication_adjudication` firing rate on story-led turns, plus manual read of whether a source's own Usage Guidance caveats survive into the telling | Named for Design — see §8 question 10 |

---

## 8. Open questions handed to Design (with everything the review rounds assigned)

Decisions this Research stage deliberately does NOT make, listed so none
happens by default:

1. **The Albina values decision** — shorten her sentences to the floor vs
   name a recorded exception — now sharpened by §3.1: the decision is
   really about the gate's target artifact (output, not file). Mark's call
   per the brief; Design frames it with the wired gate's first real number.
2. **The turn-length ceiling decision** — the brief's §7 Part A rewrite
   deletes the shared ceiling unless it decides otherwise; this document's
   §2 correction (four per-world ceilings also exist — Papnoute's the
   strictest — all inside files being rebuilt, with only Theon and Marius
   carrying none) means the decision is really: where does the
   turn-measure live in the rebuilt architecture (shared block, per-world
   files, or both), not merely keep/delete one instruction. The review
   rounds mark this as a decision to make and record (TR3 P1-4).
3. **Governance keep/simplify/replace/drop recommendations** for
   `over_settling`, `citation_grounding`, `drift_detection`,
   `confirmed_glosses` — evidence assembled for Design: the cost facts
   (one drift call/turn; over_settling's second stage the largest
   invisible line item, 10-of-12 firing with confirmed-rate unmeasured in
   that count; `confirmed_glosses` has no LLM call at all), the history
   fact (over_settling was first tried as one signal among ten and caught
   nothing — `facilitator_prompts.py:228`), and P3's finding that
   monitoring exists precisely because prose under-holds — any
   simplification argument must say what newly holds the goal instead.
4. **The leak fix's split** (§4): code-side (strip-list line + fail-closed
   policy) vs authoring-side (apparatus-vocabulary fields) vs prompt-side
   (filter instruction) — Research's finding is that all three exist and
   are different problems; Design decides the combination and sequencing
   against the brief's §4 content-freeze rule.
5. **probe_parity's pass criterion** for a deliberately-changed voice, and
   its promotion (or not) from staging tool to standing gate.
6. **Worked-example form** (positive-only vs contrastive pairs) — decided
   only after §5's probe evidence; P5's parroting caveat and
   rubric-first rule constrain the answer's shape either way.
7. **Where the sustained-disagreement license lives** (shared block vs
   per-world) given P2's finding that the adjudication mechanism already
   exists and the license text exists nowhere.
8. **The restricted-offer/candidate-understanding move** (P6) — whether it
   enters `_HOW_YOU_ENGAGE`, the per-world files, or both; new to this
   stage, no prior decision constrains it.
9. **Record-sourced assembly as the default architecture to evaluate —
   Mark's direction, 2026-08-08, added before stage sign-off.** This
   rebuild takes advantage of the world record build-out already
   completed (the `wrs/records/<world>/` layer: 26–41 source records per
   world plus term/story/gravity/contested_claim/figure/demonstration/
   voice_profile/world_core records, with recent rigor and bibliography
   sweeps): the six worlds' information is already reorganized for
   efficiency, and the voice rebuild should sit on it rather than beside
   it. Design evaluates **making the records the authored artifact and
   the deployed prompt a deterministic assembly from them** as the
   default architecture, not one option among several. The Research
   evidence assembled above already argues each piece: the assembler
   exists as a Desert-only staging prototype (`wrs/views/
   permanent_prompt.py`); `probe_parity`'s 4-of-6 failure is precisely
   the records-vs-deployed drift this architecture ends structurally;
   assembly time is where enforcement becomes code instead of
   under-holding prose (P3) — leak filtering, the readability gate,
   fail-closed stripping; the `wrs/` lockstep requirement dissolves
   instead of being a discipline; and world #7 inherits the machine
   (Objective 5).

   **The governing constraint, stated with the same weight as the
   architecture itself: structure organizes and enforces — it never
   generates voice, and efficiency is never taken out of conversation
   quality or naturalness.** Objective 3 carries exactly the weight of
   Objective 4 (brief §6), so record-sourced assembly is acceptable only
   if the assembled voice is at least as natural, engaging, and genuinely
   that world's own as the best hand-authored alternative — measured, not
   assumed: the assembled output must pass the same instruments this
   stage built (§7 — the probe battery, output readability, the
   naturalness rubric traits, the sustained-disagreement probe when
   built), with Papnoute's held battery (§5.2) as the working quality
   bar. The voice prose *inside* the records (voice_profile, worked
   examples, register craft) remains fresh, per-world writing from
   sources — the clean-rebuild mandate applies to it unchanged; what
   assembly contributes is that this craft is written once, in the record
   layer, and enforced mechanically on the way to the model. If evidence
   during Design shows assembly flattening voice quality anywhere, that
   is an Objective-3 failure to fix in the architecture, not a cost to
   accept for efficiency.
10. **The Objective 2×4 interaction — the brief's Research mandate (d),
   delivered here as an open design question with its evidence
   assembled:** a lead-with-the-story instruction demonstrably interacts
   with no-fabrication. The pilot's Albina run fired
   `fabrication_adjudication` on the exact turn that told the Marcella
   story flat, dropping the source's own epitaph-genre caveat (brief
   finding C); this session's Papnoute run fired the same signal on the
   turn that opened on a constructed scene inside a participant-supplied
   hypothetical (§5.2); and the genre-caveat instruction that already
   exists (`representative_prompts.py:188-198`) is one of P3's measured
   under-holding prose instances. Design's story-first mechanism must
   carry a source's own genre/confidence caveats *into the telling* by a
   means stronger than the current prose instruction, and §7's Objective
   2×4 instrument row is how the result gets verified. Not optional; this
   is the named interaction between a Tier-2 objective and a
   non-negotiable one.

**Gaps Research names beyond the brief's reading list** (per §9's mandate
to say so plainly): (a) the four unrecovered rubric traits + weights
(egress-blocked; one fetch from any network-open session closes it); (b)
the brief's own open question — does brevity's advantage survive
substantive dialogue — has no external answer and should be answered by
CiC's own A/B evidence during Build verification, with the probe script's
per-turn instruments; (c) `mark_voice_simulation_results.json` (the
2026-08-05 pilot's raw results) remains uncommitted and unavailable to
this session — its four claims (brief finding C) stay sourced to the
Decision Log entry and brief only; (d) Objective 3's positive goal
(insight, connection, honesty) still has no instrument — the largest
known instrument gap, carried visibly in §7's table rather than papered
over; the §6 rubric's adopt/adapt rows are the best in-corpus candidate
for building one.

---

## 9. Bottom line

The brief's diagnosis survives verification with three corrections (§2),
and the Research stage's own instruments moved two things from claim to
measurement: the leak is roughly twice as widespread as estimated and
concentrated exactly in the lead-with-insight fields (making the filter
load-bearing, not hygienic), and the accessibility problem in the files is
concentrated in two prompts (Marius failing both numbers, Yausep at the
FK line) and three capsules — while Albina's problem is her output, not
her file, which relocates (without resolving) the values decision
reserved for Mark. The live probes gave the stage its sharpest
single result: a currently-deployed world violating its own file's central
voice instructions under measurement while the worked-example world held
the same battery completely — prose-alone under-holds is now a measured
fact, and the rebuild's real levers are placement, redundancy,
demonstration, and code-side enforcement.

The affirmative answer to the governing question is P1–P7: defeat the
assistant register in both its dialects; make disagreement survivable and
evidence-conditioned; stop trusting single-site prose and use placement,
redundancy, demonstration, and code-side enforcement; fix what reaches the
model before instructing the model; rubric first, demonstration second;
pace depth across short turns and close the loop with callbacks and
candidate understandings; and treat the voice as a versioned artifact with
a continuity criterion that knows the difference between drift and a
rebuild done on purpose.
