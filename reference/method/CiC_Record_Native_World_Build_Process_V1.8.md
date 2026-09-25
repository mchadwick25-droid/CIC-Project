# CiC Record-Native World Build Process — V1.8 (2026-09-25)

**What this document is:** the single end-to-end process for building a NEW
formation world, from Step-0 scope confirmation through a frozen, deployed,
live-verified Representative — with every upgrade the S6.2 record-store
migration (2026-07-26 → 2026-08-01) proved on the six existing worlds built
in from the first record, not retrofitted afterward. A new world built under
this document is **born record-native**: authored directly into the
schema-validated WRS record store under the live gates, with the deployed
prompts and chunks *generated from* the records — there is no separate
"migration pass" for a world built this way, because the migration IS the
authoring.

**What governs, in order of authority (this document does not replace any
of them — it sequences them and fills the gaps between them):**

1. `reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`
   — the Construction Framework (governing since 2026-07-27; carries the
   Table Readiness Round, the Record Integrity Principle, the Source
   Registry freeze gate, and the Validation Protocol Rigor discipline).
2. `reference/L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx`
   — the RCF (Part Three Ecology Assessment; Part Eight Validation Testing;
   Phase Eight Table Readiness Round).
3. `reference/method/CiC_World_Build_Completion_Standard_V1.3.md`
   — the freeze-requirements source of truth (the CF's own pointer target).
4. `reference/Project-Reference/CiC_OneDocAtATime_Build_Protocol_2026-07-06.md`
   — the one-document-at-a-time, review-gated build discipline.
5. `Archive/Technology-Pass2-2026-08/Pass2/SESSION_CONTRACT.md`
   — the session rules (adapted here for a new-world build; see §6).
6. This document — the sequence, the record-native additions, and the
   S6.2 upgrade inventory (Appendix A).

**Vision framing note (standing, Mark):** purpose statements and any
participant-facing copy produced during a build lead with making
experiential Christian formation available; the product is the current
means, never the mission's definition. The Brand Kit QuickRef governs all
public wording.

---

## 1. The human checkpoints — exactly three, by design

This process is fully automated EXCEPT where authority genuinely cannot be
delegated. Three stops, no more:

**M1 — Representative identity (mid-build, after Doc_09).** The build
thread prepares the grounded-options artifact per the build-cycle
discipline's own escalation rule: a scored options table for ROLE (each
option grounded in the world's own methodology facts, with named
trade-offs) and for NAME (scored on ecological resonance, authenticity,
collision-with-a-real-figure risk, gender clarity, memorability), plus ONE
recommendation for each. Saved as
`worlds/<World>/<code>_Representative_Identity_Options.md`. The
thread STOPS and presents the table to Mark. Precedent to imitate: both
prior executions of this pattern —
`worlds/alx/Representative/alex_Representative_Identity_Options.md`
(Mark rejected both recommendations and chose "Theon," with reasoning
recorded) and
`worlds/hal/hal_Representative_Identity_Preliminary_Decision.md`
(Mark adopted a fifth option not among the four presented — the *vidua*
Albina, with the naming-collision risk disclosed and accepted on the
record). The lesson from both: Mark's answer is frequently NOT the
recommendation — present real options with real trade-offs, record his
actual decision verbatim in the same file, and never proceed on the
recommendation alone.

**M2 — Article 29 (Living Traditions) determination (at the freeze).** A
project-lead act by Constitution Article 29 — the build thread drafts the
determination with full history and its own recommendation, carries the
status as `provisional` until Mark confirms, and lists it in the freeze
declaration's RESOLVED-AT-THE-FREEZE section for his explicit word.
(Article 31 telos review is NOT a stop: provisional by design until year
two, per Mark's standing 2026-07-31 ruling.)

**M3 — The freeze itself.** Only the project lead assigns Frozen, under
any circumstance (build-cycle discipline, unchanged). The thread completes
everything, drafts the freeze declaration, and stops with a completion
summary. Mark's "push and make final" (or equivalent) executes it.

Everything else — every document, every review round, every record, every
gate fix, every battery reprobe — the build thread decides and records
autonomously (decisions logged, never silent), per the S6.2 autonomy
addenda: full in-world autonomy, stop only at the checkpoints above and at
the world boundary.

---

## 2. Phase A — World construction (Step 0 → Doc_10)

### Library stage (source-research thread): Step 0 → Doc_02

The source-research thread owns Step 0, Doc_01 and Doc_02. Each runs
under the one-document-at-a-time cycle (draft → adversarial review →
revision → disposition) through review until it is approved to proceed.

| Step | Document | Notes and per-step quality bars |
|---|---|---|
| 0 | `Step0_Movement_Scope_Confirmation` | Confirm the world against `reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx`'s portfolio entry before anything else. |
| 1 | `Doc_01` World Identification, Boundaries, Orientation | Article-21 strand analysis here if the world is strand-plural (PAHC and IJC precedents: strands ride `world_core`'s body until the strands schema CO lands). |
| 2 | `Doc_02` Source Ecology | **Use the Source Registry Template from the first row** (V7.4 freeze gate) — machine-readable rows, per-row confidence/boundary-status/licensed-for/verification-note. PAHC's 73-row JSON registry is the best-practice model; it made its S2.1 fully mechanical. Every load-bearing caveat (do-not-cite flags, pending-verification lists) written as its OWN row field, not prose — S6.2 spent real effort re-deriving these. **Holdings dispositions (R13):** before Doc_02's review, run `python -m engine.m9.cli holdings <code>`. Every file it marks "not yet assessed", and every tier 1–2 file it marks "in scope, unread", gets one line in the Source Registry: used, deferred with a reason, or out of scope with a reason. The review checks that no line is missing, not that each disposition is right. Files marked "no coverage entry" are a library gap, not the drafter's job; list their count and leave them. |

The library stage builds on the world's library package
(`worlds/_cross-world/SOURCE-READINESS.md`):

- its Source Readiness Dossier at
  `worlds/_cross-world/dossiers/<slug>_Source_Readiness_Dossier.md`
- its corpus-map assignments at `cic/corpus-map/<slug>.yaml`
- the vendored texts those assignments point to in `cic/texts/`
- any further rendered source material the research produced for the
  world

Doc_02's Source Registry gives every item in the package a line:

- every dossier §1 assigned work, §2 cross-link and §3 acquisition
  lead: used, deferred with a reason, or out of scope with a reason. A
  lead not yet vendored is marked for acquisition.
- every §5 open cross-world question: named and carried forward, not
  decided
- every piece of rendered source material: used, or set aside with a
  reason

The Doc_02 review checks that no item is missing, alongside the holdings
dispositions in the Doc_02 row above.

Step 2 also produces, for the build to work from:

- an exact locus for every quotable passage
- a quotability flag for every file: verbatim-ready, second witness
  only, or unusable
- own-voice vs opponent-voice flags wherever one work mixes them (a
  martyrology, a polemic, a trial record)
- corpus-map rows with `row_id`, corrected `role` and `voice_of`
- a holdings disposition for every item
- a thin-evidence map, which feeds confidence levels and the admission
  probes
- for each work, its edition and original language, and which text is
  primary and which is the cross-check
- cross-world overlaps and pairs (`cic/corpus-map/PAIRS.yaml`)
- optionally, one line on material and archaeological sources consulted
  or not, and the social roles the sources attest for a Representative

Steps 0–2 may run ahead of any full build. Their output also populates
the Church Family Tree.

### Handoff

The world build starts only when the handoff package is complete. A
build thread checks every item below before it starts Step 3. If any item
fails, it stops and sends the world back to the source-research thread.

1. **The world's identity is fixed.** Its registry entry at
   `records/worlds/<code>.yaml` exists, with one `world_id`, before any of
   the world's records reach `main`. Every later file uses that same
   `world_id`.
2. **Step 0, Movement-Scope Confirmation, is approved to proceed.** It
   cleared independent Opus review within the round cap, and the
   movement's own status in `cic-website/data/world-census.json` was
   checked.
3. **Step 1, World Identification, is approved to proceed,** under the
   same review rule.
4. **Step 2, Source Ecology, is approved to proceed.** Its Source Registry
   gives every item in the library package a line, and no dossier item,
   corpus-map entry or holdings-report file is missing one.
5. **The Source Readiness Dossier** is at
   `worlds/_cross-world/dossiers/<slug>_Source_Readiness_Dossier.md`.
6. **The corpus-map assignments** are at `cic/corpus-map/<slug>.yaml`, and
   `python cic/engine/corpus_map_merge.py --check` passes.
7. **The vendored texts** are in `cic/texts/`, each with a
   `cic/texts/REGISTRY.yaml` entry and verified rights. Every assigned
   work opens, and `python cic/engine/corpus_index.py --build` is clean.
8. **Every quotation in Steps 0–2 is re-verified** word for word against
   the vendored file, speaker included. An opponent's paraphrase is never
   quoted as the subject's own words.
9. **Open questions are carried forward, not decided.** Every cross-world
   question in the dossier sits in `worlds/_cross-world/NEEDS-RULING.md`
   or the world's `Open_Gaps_Tracking.md`.
10. **The world's `Open_Gaps_Tracking.md` exists,** with the library
    stage's own gaps already listed.
11. **No process narration** is in anything that will become canonical.
    History goes to the build log.
12. **A one-page handoff manifest** lists the paths above, the review
    round each step cleared in, and the date. The build thread reads it
    first.

**Mark signs off each handoff and launches each world build.**

The build then starts at Step 3. It never redoes Steps 0–2 or the
library search, and it cites the package's own sources wherever the
package holds them. Anything the build finds missing goes back to the
source-research thread, so the next world gets it too.

### World build (build thread): Doc_03 → Doc_10

The world build starts at Step 3, from the library's handoff package.
Every document draws on that package: Doc_03 and Doc_06, Doc_04, Doc_08
and Doc_09 search the world's shelf with `corpus_index`, and their
reviews check that claims cite the package's own sources wherever it
holds them, not summaries of them.

The document sequence, unchanged from the six built worlds, runs under
the one-document-at-a-time cycle (draft → adversarial review → revision
→ disposition), with the review loops agentized (§5):

| Step | Document | Notes and per-step quality bars |
|---|---|---|
| 3 | `Doc_03` Lexicon Candidate List | Term front-matter per the lexicon-index discipline (Tier, AS/SC/DR/TC/RT/PV/CT tags). **NEW: run the alias-safety preflight NOW** (§3, B-2) — author aliases against Rules A/B from birth so no retrofit is ever needed. |
| 4 | `Doc_04` Gravity Discovery | Six-test assessment per gravity; Confidence/Gravity Cross-Check on every Primary; forces-connection notation per gravity. No L4 template exists for this step — the gravity-index discipline is the bar. |
| 5 | `Doc_05` Ecological Reconstruction | |
| 6 | `Doc_06` Full Lexicon Development | CT Contest Type completion audit before clearing review. |
| 7 | `Doc_07` Integrated Ecology Analysis | |
| 8 | `Doc_08` Forces Document | Six-cell matrix, three layers per force, Section 4 cross-cell connections, Section 5 forces-and-gravities synthesis, per the forces-index bar: connections must be LOOKUPABLE, not re-read-the-whole-document discoverable. |
| 9 | `Doc_09` Story Inventory (+ 09a-c as needed) | Four-tier rule (no Tier 5 / no invented narrative); the Absent Stories question answered explicitly; per-story tier justifications. |
| — | **M1 STOP — Representative identity** (§1) | |
| 10 | `Doc_10` Representative Construction Notes + Permanent Prompt | Built AFTER M1, on the decided identity. Voice, registers, demonstrations. RCF Part Three Ecology Assessment (4 domains + Thinness Mapping) produced here — it calibrates the Phase-D probes. |

**Index artifacts:** the old per-world `.xlsx` workbooks are RETIRED for
new builds. Their function (filterable indexes for tier/tag/risk-flag/
result review) is served by the record store itself plus its generated
views — S6.2's close-out audits machine-verified the old workbooks as
fully absorbed before retiring them. Do not create new workbooks.

**Cross-world source layer (added 2026-09-02) — check this BEFORE
drafting Doc_02's Source Registry, not after.** Six built worlds' worth
of vendoring already sits in `cic/texts/`, tracked and searchable
independently of any one world's own request process. A new world's
Doc_02/G1 work is verification-first against that layer, not
download-first from zero — Gaul is the standing example (G0's own
provenance note in the launch prompt already says so). Concretely, in
order:

1. **See what's already assigned to this world's own Atlas entry** —
   `python cic/engine/corpus_map.py --coverage`, or read
   `cic/corpus-map/<atlas-id>.yaml` directly if it exists. The bucket
   filename IS the census id (`cic-website/data/world-census.json`'s own
   `id` field) — no lookup needed. Anything listed there is a vendored
   work with a role (`tradition`/`context`/`antecedent`/`transmission`)
   and confidence already argued out; a Doc_02 row citing one of these
   starts from that reasoning, not from zero.
2. **Search across everything vendored, not just this world's own prior
   citations** — `python cic/engine/corpus_index.py "TERM" --entry
   <atlas-id> --limit N` (build the index once per session with
   `corpus_index.py --build` — it's derived, gitignored, ~10 seconds for
   the whole corpus). Returns ranked hits scoped to this world's own
   corpus-map assignments, each with a canonical address
   (`cic:<file>:<locus>`) ready to paste into a source row's own locus.
3. **For anything genuinely not yet vendored**, run
   `worlds/_cross-world/discovery_helper.py` on a machine
   with real network (never inside a build thread's own sandbox — every
   patristic text host is blocked there) to find real candidates before
   falling back to open-ended web search. It prints a paste-ready,
   UNVERIFIED stub — never add it to the Manifest without independently
   confirming the URL and rights basis yourself.
4. **A confirmed candidate goes into
   `worlds/_cross-world/download-queue-seed.yaml`**, not only
   this world's own Manifest — the same edition may close a gap for a
   later world too, and a source found once should never need finding
   twice.
5. **After Mark vendors a file** (attached directly in a chat message, per
   `cic/texts/INTAKE.md` — the full procedure from attachment to a
   registered, findable text, including the rights-checklist and naming
   convention for original-language witnesses, which Mark is now also
   sourcing directly in Greek/Latin/Syriac as second witnesses, never as
   primary evidence), add its row to `cic/texts/REGISTRY.yaml` and assign
   the work into this world's corpus-map bucket via a
   `cic/corpus-map/_staging/` file + `corpus_map_merge.py --write-only
   <own-volume-token>` (2026-09-03 — a plain, unscoped merge writes and
   PRUNES every bucket every current staging file touches, which risks
   finalizing or deleting another world's still-in-progress staging
   mid-build; `--write-only` still reads everything for a correct
   picture, it just restricts what actually gets written, and skips
   pruning) — this is what makes the NEXT world's step 1 above find it.
6. **Cite with a canonical address where one exists** — a source row's
   `sources[].address` field (sibling to `locus`, added 2026-09-02)
   takes the exact string step 2 returns. Optional; `locus` alone still
   validates.

None of this replaces Doc_02's own judgment about what belongs in THIS
world's registry — corpus-map assignment and a Source Registry row are
different questions (shared custody of a text vs. this world's own
argued use of it). It replaces re-discovering, by hand, what six other
build threads already found.

**This is the way a session reads the library, at any step, not only
Doc_02 (Library Access Gate, increment 10, 2026-09-15).** `python
cic/engine/corpus_index.py "TERM" --entry <census_id> --limit N` is the
one search path a build session uses whenever it needs to find or check
something in `cic/texts/` — Doc_04 checking a claim, Doc_09 sourcing a
story, a revision round re-verifying a quote — the same tool and the
same `--entry` scoping named above for Doc_02, not a separate practice
for later steps. It already reads only the files this world's own
corpus-map bucket assigns (`corpus_index.py::files_for_entry`); reaching
past it to browse `cic/texts/` unscoped is an off-shelf read, the thing
`engine/m9`'s confinement gate exists to catch downstream. The one
narrow, logged exception is Q5's build-time absence check (confirming a
`kind: absence` source record's claim that a passage is genuinely
missing from a specific named file) — never a substitute for scoped
search as the everyday way of finding material.

---

## 3. Phase B — Record-store authoring (born under the live gates)

**The register bar is a birth condition (V1.1).** Spoken prose is born
at the bar the same way records are born under the live gates: from the
first record, never retrofitted. The bar is one approved sample, not a
list of rules — `reference/method/CiC_Register_Bar_2026-08-29.md`
holds it, and it holds nothing else. Concretely:

- Every spoken field (`text`, `statement`, `tellable_as`, exchange
  turns, `positions`) is drafted with the approved sample open, and
  written to match it: practical, straight, clear modern English;
  simple sentences; a scholar's term only after its plain meaning, as a
  label. The sample is the standard. No banned-word lists exist or
  accumulate anywhere in this process.
- The readability target is NorthStar: Flesch-Kincaid grade 8–10 and
  Flesch Reading Ease 60 or above
  (`reference/method/Pass2-decisions/VR_1A_NorthStar_Readability_Target_2026-08-09.md`).
- No embedded quotations in host prose (Decision 8B). A real source
  quotation inside a story, gravity, force, term or other non-quote
  record becomes its own `quote` record, verified verbatim, and the host
  prose paraphrases it in plain voice. `engine/m1/embedded_quotations.py`
  reports candidates. When a Decision 8B pass extracts an embedded
  quotation into a quote record, the host record's text changes only in
  the sentence that held the quote. The pass may also add the host's
  `relations[]` link to the quote record, and delete process-narration
  apparatus (deletion only). Any wider rewrite of host prose, readability
  rewrites included, is a separate task with its own review, never part
  of the same PR.
- Quote records author their `modern_rendering` at birth. The spoken
  form is a modern-English translation, never the archaic original; the
  original stays as the record's `text` for Level 3. Opus authors every
  `modern_rendering`, and a separate Opus pass checks it independently
  (Decision 8B).
- A non-English original can be the primary source. The quote record
  holds the original, verified verbatim. The spoken `modern_rendering` is
  an Opus translation from the original, independently Opus-checked and
  marked as rendered from the original. A public-domain English
  translation, where one exists, is a cross-check, not a requirement. **A rendering may
  be split into shorter sentences to pass readability only where each
  resulting sentence has its own subject and verb and carries one whole
  thought of the original (2026-09-23, R40 alx `modern_rendering` pass,
  PR #442) — a fragment is never an acceptable rendering, whatever the
  grader or the FK score says.** The builder reads every sentence of the
  rendering for its own subject and verb before the record leaves
  authoring; neither the rendering-fidelity grader (it grades meaning, not
  grammar) nor the FK gate can see a fragment.
  `engine/m1/sentence_completeness.py` (report-only) lists sentences with
  no main-clause subject or finite verb as candidates for that read; it
  misses some and misreads some, so it supports the read and never
  replaces it. It also flags the source-spoken forms the next paragraph
  accepts, so the builder reads each flag against that paragraph. Where
  the fragment rule and readability pull apart, split differently or trim
  words; never reopen a fragment to lower the FK score.
  **What the source itself speaks: interjections and answers stay; lists
  become one sentence; true ellipses get finished.** An acclamation,
  interjection or elliptical answer that the source itself speaks
  ("Alas!", "Yes!", "Praise to God.", "Answer: No.") is a whole utterance
  in modern English and stays as the source speaks it. An inventory or
  list is rendered as one list sentence, never one item per sentence,
  unless that one sentence would pass about 25 words. Then it splits into
  a few list sentences grouped as the source groups them (e.g. tableware,
  furniture, bedding), keeping the source's order and every item — the
  source's own grouping closes it, and there is no filler connective
  repeated sentence after sentence. A source sentence cut short mid-thought
  is finished with the verb its structure implies, not carried over as a
  fragment. Where finishing a true ellipsis needs the very words an
  edition supplies, the rendering may use them — the words are there
  because the sentence needs them, not because a translator added them. A
  split made during rendering that leaves a clause without its own subject
  and verb is still a fragment, and is never acceptable.
- **The register rule governs every `modern_rendering`.** A rendering is
  everyday modern English. An original word or phrase stays only where it
  survives plainly in modern English — a reader today would say it and
  understand it without pause ("Time will fail me if I attempt to
  recount" stays as written; paraphrasing it away is an error in the
  other direction). A word that does not survive plainly is translated to
  its modern sense, including archaic function words and archaic senses of
  familiar words; a scholar's term the world keeps is glossed on first
  use, per the register bar above. Worked cases, not a list to check
  against: "Wherefore" → "Therefore", "disjoin" → "separate", "Ever let"
  → "Always let", "quickening" in its bring-to-life sense → "bringing him
  back to life". Each is judged by the principle on the word in its own
  sentence, never by matching a word list — the same word can survive in
  one sense and not in another.
- **Scanned editions.** The long s (ſ), thorn (þ) and eth (ð) are
  normalized deterministically. Per-edition OCR fixes are declared as
  that edition's apparatus in `cic/texts/REGISTRY.yaml`. A garbled print
  is a second witness only until a clean witness is vendored. No model
  ever retypes a source.
- **The verbatim gate is a birth condition (2026-09-23, item 3 of the P3
  registration brief).** `gate_quote_verbatim` (`engine/m1/gates.py`,
  `engine/m1/quote_verbatim.py`) runs on each quote record as it is
  authored, checked directly against the vendored edition in
  `cic/texts/` under the ruled tolerance classes
  (whitespace/case/punctuation/ellipsis/bracket/verse_number/apparatus)
  and that edition's own closed apparatus entry in
  `cic/texts/REGISTRY.yaml`, if one exists — not a repair pass run over
  already-authored records after the fact. R35 (Mark, in his own
  words): *"this is about the build quality, not fix on fix."* Which
  quotes the gate checks, and how a quote that can't be checked directly
  is born, is set in B-4.
- **The rendering-fidelity gate is a birth condition.** The verbatim gate
  checks a quote record's original wording; this gate checks its spoken
  translation, at the same point: authoring, not review. The rendering is
  translation, not summation: every clause of `text` is present in
  `modern_rendering`; nothing is added, nothing compressed away. The
  builder runs `engine/m1/rendering_fidelity.py` on each rendering as it
  is authored, with two grader models, Haiku 4.5 and Sonnet 4.6; a flag
  from either counts as a flag. The builder reads each grader's reasoning
  against the record's `text` (not just its verdict) and revises until
  both graders read "translation" on two consecutive runs of the same
  input — one clean run is not enough, since a grader varies run to run.
  Sonnet 5 replaces Sonnet 4.6 once the account can invoke it and the
  grader study is re-run. The graders are report-only and never
  registered in `gates.GATES`: their verdicts inform the builder's read,
  and the fragment and register rules above win where they disagree.
  Where a grader keeps objecting after a person has read every clause
  present, the read stands and the disagreement is recorded in the
  world's `Open_Gaps_Tracking.md`, not chased with further rewrites.
- Each step's review reads every spoken field against the sample. A
  sentence the reviewer has to re-read, or has to ask the meaning of,
  fails and is rewritten before the step clears — that question IS the
  finding.
- Before B-8, the bar screen (quote-stripped reading grade, longest
  sentence, fragment ratio) runs over the world's spoken fields and its
  output is saved as an artifact. The numbers are visibility only; the
  sample is the judge. Nothing gates on a number.

**Transparency ground is a birth condition (V1.2).** The three-level
transparency system can only surface what a cell's coverage offers it —
Mark's first pilot read found the center cells of a finished world
holding zero stories and zero terms, so no story or gloss could ever
fire on "Who was Jesus?" no matter how well the machinery worked.
Two conditions, born with the records rather than retrofitted:

- **Every substantive cell offers its stories and terms.** When a cell's
  records are authored, the coverage read asks: does a story genuinely
  belong here? a term? If yes, its `canon_cells` says so at birth —
  lean, one story and one term per cell where they genuinely belong,
  never everything that could fit. If nothing genuinely belongs, that
  finding is recorded and the cell stays empty there — an honest empty
  (the fleet's own C-P is one) is a legitimate outcome, forced fill is
  not. The center cells are read first, the same order the canon tests
  them.
- **No spoken field hard-binds a first-mention introduction.** An
  opening like "One of us, N, ..." welds the introduction to the
  answer, and a compiled exemplar answering its own canon question will
  reproduce it verbatim on every later mention (measured, four live
  probes, 2026-08-30). The spoken field speaks the plain name;
  introducing the figure is the system's job — the name-bridge mark the
  first time a session meets the name, the already-introduced signal
  after. The idiom itself is not banned from a world's prose — it is
  banned from being the load-bearing opening of an exemplar or witness
  answer. Figure records author at least one name whose comma head is
  the name the voice actually says.

**Voice perspective is a birth condition (V1.4).** Every spoken field
speaks as the world's own voice, from inside it - "we taught", "our own
record" - never as a builder describing the world from outside it -
"this world taught", "the world's own record", a third-person "it"/"its"
chain describing the community as an object. The approved sample
(`CiC_Register_Bar_2026-08-29.md`'s own exemplar) already has this
property throughout; this condition just names it, the same way the
register bar itself names word choice and sentence length. Concretely:

- Draft every spoken field checking this the same way it is already
  checked against sentence length and word choice: read it back as
  something an inhabitant of the world would actually say about their own
  people, not as a description of them from outside.
- `gate_voice_perspective` (`engine/m1/gates.py`) runs in the M1 battery
  from the first record - a world born under this condition opens at
  zero on this gate, the same standard Hieronymian set for alias-safety.
- Two exceptions exist and are not violations: a quote's own scriptural
  sense of "this/the world" ("departed from this world"), and the
  ordinary cosmological sense ("the Maker of this world", refuting
  Marcion). Both name the created/temporal order itself, not the
  speaker's own community - see the gate's own docstring for the full
  reasoning.

**File discipline is a birth condition (V1.3).** Everything in its
place, nothing else — from the first record, never as a later cleanup.
Two opposite failures are both real and both prohibited: build language
littering operative fields (measured fleet-wide at ~250 shipped
instances before the compiler fix), and stripping durable
scholarly reasoning out of a record body. Concretely:

- An operative frontmatter field carries ONLY what it exists to carry:
  no work dates, review-pass or model names, thread references, or
  provenance asides inside values the runtime or a participant reads.
- Build notes (dates, corrections, review history, thread and model
  names) go to `worlds/<code>/build/` and `Ministry/`, never into a
  record. A record body below the closing fence keeps durable scholarship
  only: why a claim is scoped as it is, which source verifies it, what
  was checked and found absent. Record bodies are never compiled.
- The process-narration scan (`tools/check_live_commentary.py`) blocks
  new worlds once its record-body checker (PR #581) passes review with
  measured precision. Until then, and for existing worlds afterward, it
  is report-only, with waivers for existing worlds.
- Provenance-by-design fields (search_record fields,
  why_sources_cannot_answer, modern_lens_note, discovery_channel,
  narrative_tier_justification) are written fully and honestly; the
  compiler excludes/strips them from shipped packages.
- No frontmatter field is ever invented to hold a note; the schema is
  the field list.
- Every pin is preceded by a residue read of the compiled
  repository.json alongside the gates report; a hit is a
  field-placement defect fixed at the record layer, noted in the
  world's build log, then recompiled. The grep is visibility; the read is the judge.
- Build deliverable docs live in the canonical world-build folder,
  never inside records/, packages/, or engine/.

This is where a record-native build departs from the six worlds' history:
instead of finishing Phase A and later migrating, each Phase-A document is
converted into WRS records AS IT CLEARS REVIEW, under the live gates, by a
committed per-step script (the S6.2 `s62_<code>_s2X.py` pattern — write
the same scripts, named `wb_<code>_s2X.py`, each with the dense docstring
discipline: exact source doc/section cited, mechanical-vs-authored
declared, every judgment call named). Hieronymian is the proven template —
the first world authored under the live alias-safety gate, **it opened at
zero and closed at zero; no retrofit was ever needed**. That is the
standard: gates green from the first record.

**The scripted pass comes before review.** Before any review round on a
Phase-B step, run these and attach their output to the review brief:

- `python -m engine.m2.cli build <code>`. This runs the full M1 gate
  battery, including quote-verbatim, quote-mark-fidelity,
  retrieval-negatives-structured, readability and voice-perspective.
- `python -m engine.m1.bar_screen <code>`
- `python -m engine.m1.cross_world`, reading this world's
  register-profile and outside-help-guard observations
- `python -m engine.m9.cli holdings <code>` for any step that touches
  sources

Fix what these find before the round starts. A review round is never
spent on a defect a script could have caught. The review brief says what
the pass covered, so the reviewer doesn't redo it. It also says what the
pass can't cover: whether a claim is true. The grounding check passed
97.6% of constructed fabrications (the D1 measurement) because it checks
where the words came from, not what they assert. Checking whether claims
are true is the reviewer's main job.

For Phase A: before a review, run the cross-document consistency check
the build-cycle skill requires, and confirm each cited locus with scoped
`corpus_index` search.

The step sequence (S6.2's, now canonical):

| Step | What | S6.2-proven quality bars baked in |
|---|---|---|
| B-1 (S2.1) | Source rows from Doc_02's registry + `<code>core001` world_core | Mechanical if the registry followed the template. Every source record carries its corpus-map `shelf_row` (and so its role) at birth. Registry caveats carried VERBATIM as row licenses. `language` per row (schema requires it — declare judgment calls in the docstring). Article-29 status carried provisional for M2. |
| B-1a (S2.1a) | Discovery sweep | Read every planned citation surface; row every genuine miss with real discovery data; declared non-rows with reasons; `src<CODE>search001` sweep record with saturation statement + coverage limits. |
| B-1b (S2.1b) | Relative recall + PRESS | Ten-item independent recall test (fleet range: 6/10–9/10; a clean sweep is PAHC's 9/10 + zero miss rows). PRESS question asked verbatim; namings routed to the pre-freeze re-sweep. |
| B-2 (S2.2) | Mechanical lexicon split → term records | **Born at alias_safety ZERO**: aliases parsed under the runtime's own `parse_aliases` semantics at authoring; Rule-A generics resolved at birth (gloss-route, drop, or documented `alias_generic_override_note` — the bare-Christ/Prayer class only); Rule-B collisions picked per-term. Coverage assertion: every source sentence lands in exactly one record. |
| B-3 (S2.3) | Term authoring — senses, confidence, voice, typed relations | Confidence EXTRACTED from the doc's own confidence blocks, never re-judged. Relations fully reciprocal (the gate enforces: presupposes↔presupposed-by INVERSE; tension/associated/competing/reshaping SYMMETRIC; back-edges elsewhere). Schema enums are real — see Appendix B's collision list before authoring. Confirmed-gloss entries authored INTO `wrs/glosses/confirmed_glosses.yaml` (schema-validated, term_id set at birth — no backfill debt) and flagged per-entry for Mark's one-at-a-time confirmation. **`gloss_forms`:** each term record lists its word forms in `gloss_forms`. A form is `ordinary` if it's a common English word or phrase that could appear in a participant's or the voice's own sentence with no connection to the term. Otherwise it's `technical`. Ordinary forms only show their gloss when the sentence cites the term. Technical forms show it on sight. |
| B-4 (S2.4) | Story + figure records | Tier justifications verbatim; composites carry their own element-to-source tables; outsider witnesses own their accounts; boundary figures declared (no-story, preserver-only, no-figure skips); FECs parked verbatim for B-5. **Quote verification state:** the verbatim gate checks only quotes whose `verification_state` is `verified-direct`. A quote is born either at `verified-direct` (and passes the gate), or at a lower state (`verified-via-authority`, `named-not-rechecked`, `unverified`) with its `divergence_note` saying why it couldn't be checked directly. A quote is never set below `verified-direct` just to get past the gate. Fixes are general mechanisms, such as an edition's `apparatus` entry in `cic/texts/REGISTRY.yaml`, never per-record exceptions (R33). |
| B-5 (S2.5) | Gravity + force records | Doc_04/Doc_08 reasoning carried IN FULL, not summarized; interaction matrices mirrored exactly including no-relationship pairs; FEC→gravity_links only where the chunk's own words support it — never force-fit (FLAG-029's lesson: a wording variance gets flagged upstream, not silently converted). |
| B-6 (S2.6) | Contested-claim records | Primary-gravity minimum; CT parkings absorbed; divergence partners mapped LIVE against the frozen fleet's claims (`partner_claim_id` set); non-claims declared with reasons. |
| B-7 (S2.7) | Voice record + demonstrations | Register position warranted by the world's own genre evidence (the fleet holds six distinct positions — a new world earns its own or inherits none). `native_measure` MEASURED from real generations, not designed (PAHC's designed-70w vs measured-246-272w divergence is the cautionary case). Demonstrations grep-clean against the record store. **`identity`+`guard`+`flavor_notes`+`characteristic_concerns` combined ≤ 900 words, each individual field ≤ FK grade 10** (`engine.m1.gates.gate_readability`/`gate_voice_craft_prompt_budget` — the same instrument this record type is actually graded against; run it directly during this step, not assumed clean). This is a HARD CONVERSION, not a copy: the Permanent Prompt Template's own Final Assembly check 5d keeps its museum-guide backstop paragraphs unedited IN THE DEPLOYED PROMPT FILE — that mandate governs the `.txt` prompt artifact alone and never extends to voice_craft's own compiled fields, which condense that same material to the budget above, in the fleet's own established style (short declarative sentences, every named fact kept, redundant framing cut — alx.voice.craft is the exemplar). Carrying Section 1's own paragraphs into `guard`/`flavor_notes` near-verbatim, unabridged, is the specific, repeated cautionary case (every world built before 2026-09-19 needed this fixed after the fact; author it correctly the first time). **Distress-comparison guard (R19):** `voice_craft.guard` carries the world's own version of the prohibition on comparing or minimizing a participant's disclosed distress against the world's historical suffering. The wording is the world's own idiom, not a shared sentence. The guard stays inside the world's voice and period. It never points the participant to outside help, because that is the Facilitator's job alone. `observe_outside_help_guard` is a keyword scan and only shows what's there. The B-7 review confirms the clause is present and in the world's voice. |
| B-7a (S2.7a) | Facilitation guidance onto world_core | Pairings riding LIVE partner claims with built-in cautions (ending-not-read-back both ways; contemporaries-not-stages; the handoff containment class); telos (provisional/Art-31); living_traditions (provisional for M2). |
| B-8 (S2.8) | Generated views + four parities | Chunk views GENERATED from records; render parity (0 unclassified defects); retrieval parity vs the committed production baseline (**the verdict rule:** isolation-harness reproduction is diagnosis only — the production eval against the committed baseline is the verdict; FLAG-033's lesson); prompt coverage (zero GAPs); probe parity (held-out probes, blind, two-trial — deployed-side true-positives become record-derived guard candidates, the FLAG-030/036 class). **Golden set:** the retrieval golden set the Completion Standard requires (12–20 questions) is committed at `engine/m4/reports/bench/<code>.json` before any retrieval tuning touches the world. Its baseline goes into `retrieval_bench.py`'s history. |
| B-9 (S2.9) | Change-order decisions + chunk swap | The swap makes the record store drive this world's production. Post-swap: render identity, full production eval metric-identical, baseline saved. Prompt guards added ONLY record-derived, deployment-copy-only, cold-verified (the HAL-2/IJC-2 pattern). |

**B-3, B-4, B-6: guards and redirects (R11).** A claim the record must
never let the voice make is written as a `claim_guards` entry. It must
use one of the guard phrases the gate recognizes: "does not say", "must
not supply", "not attested", "do not invent", "does not attest", "no
source", "must not". A note saying "for this question, use that record
instead" is a redirect. It goes in `retrieval.prefer_instead` and must
not use a guard phrase. `retrieval.do_not_retrieve_when` is never
populated. A guard reaches the voice as a `MUST NOT ASSERT:` line inside
the record's own evidence budget. Guard the claims a reader could
actually be misled by, not every claim that could be made up.

**B-3, B-4: register-profile ceilings (R6).** Author label-shaped fields
to the ceilings filed under R6:

- `story.tellable_as`: longest sentence ≤ 30 words, median ≤ 25
- `term.quick_meaning`: longest sentence ≤ 20 words, median ≤ 16

These are advisory this cycle, per R6(iii), and
`observe_register_profile` reports them. The approved sample is still
the standard.

**B-3 to B-6: other traditions (R26).** When a world's records name
another tradition, the Representative answers questions about it from
those records instead of saying its record doesn't mention it. Name
another tradition in a record only where this world's own sources do.
The same Source-fidelity bar applies to what the record says about it.

**After B-6: the guard-coverage read.** Build the D1 Corpus B assertions
for the new world: every `contested_claim`, `honest_limit`,
`absent_detail` and guard line, stated as a flat claim. List each one
that passes the grounding check and has no `claim_guards` entry covering
it. A person decides which get a guard (the budget note under "guards
and redirects" above applies). The same list feeds Phase D's
fabrication-press probe, aimed at the Ecology Assessment's thinnest
evidence.

**The re-proof rule (FLAG-037, fleet-level):** any prompt fix proven in an
isolated harness MUST be re-proven under the deployed runtime (RAG +
capsule dilution) before it counts. Depth-of-drilling correlates with
survival; the election-scene seam defeated two guard layers before a
targeted prompt sharpening closed it.

---

## 4. Phase C — Deployment wiring

> **Superseded.** The steps below name files and directories that no
> longer exist. Until a thread that traces a real admission end to end
> rewrites this phase, follow `reference/Redesign-Spec/Artifact-2-World-Package.md`
> and `reference/Redesign-Spec/Artifact-6-Operations.md` instead.

These hold regardless of that rewrite:

- **Required before admission:** the world's `world_front` and
  `facilitator_brief` records; its compiled site JSON
  (`python -m engine.m2.site_cli build <code>`, which writes
  `cic-website/data/worlds/<census_id>.json`); and its traditions page
  (`python tools/generate_tradition_pages.py`).
- **Mark admits.** A world's census status is set only by the m6 sync
  (`python -m engine.m6.cli sync`) once the world is admitted or open,
  never by hand.
- **Staging stays open to unadmitted worlds.** `cic-engine-staging`
  runs with admission enforcement off, so a built world can be tried
  there before Mark admits it. Only Mark uses it.

Everything S6.2 and the go-live day proved can break, as a checklist:

1. `app/world_manifest.py` entry (world_id, name, subtitle, period, region,
   description, representative block, color chosen from rendered swatches).
2. The two hand-synced frontend points (the manifest docstring names them):
   `SpeakerName` union + `MessageBubble.tsx` `REPRESENTATIVE_NAMES`;
   `tsc --noEmit` clean.
3. Vector indices built at Docker build time (`build_indices.py`) — never
   at runtime startup (the OOM lesson).
4. **Dockerfile audit for new runtime dependencies** — the 2026-08-01
   go-live regression: a data move made `wrs/glosses/confirmed_glosses.yaml`
   a runtime dependency the image never copied, breaking every deploy until
   root-caused from the real Render build log. Any new file the app imports
   at runtime must be verified present in the image.
5. `HARD_CEILING_WORLDS` entry (`app/graph/nodes.py`) from the MEASURED
   voice profile + battery evidence, with the retry-trigger multiple;
   `cost_baseline_runner.py`'s `CEILING_WORLDS` kept in sync (the
   observability gate enforces).
6. `POST_HISTORY_GUARD` wiring for the world (`wrs/views/segments/guards.py`
   → `nodes.py`) — the layer that rides closest to generation; add
   world-conditional clauses only on battery evidence.
7. Live smoke test against the REAL deployed site after the deploy — a real
   session, a real message, citations inspected. Freeze batteries validate
   the build environment; only a live conversation validates the deploy
   (the Deep-Interview sweep's reason for existing).

---

## 5. Phase D — Validation and freeze (agents and loops required)

**LEAN VALIDATION IS THE DEFAULT (Mark's cost policy, 2026-08-01, refined
same day):** the freeze bar is content accuracy — "the right things
said" — PLUS single-representative INTERVIEW dynamics (the solo Deep
Interview is the product on limited-table footing; its own dynamics are
not optional). What is deferred is MULTI-REPRESENTATIVE table dynamics
only. Target spend: the interview class (single-digit dollars/world),
not the ~$30 full-battery class. The full V7.4 battery below remains
available ON MARK'S WORD ONLY.

**What costs nothing and is NEVER cut (the content-accuracy floor):** the
seven gates at zero; schema validation fleet-green; render parity and
prompt coverage (both free); grep-clean demonstration checks; the record
store itself — fabrication is a build-time impossibility when every chunk
and prompt is generated from validated records. This floor does the bulk
of "the right things said" before a single API dollar is spent.

**The lean probe set (single-trial, targeted, blind-graded):** ~10–14
probes, ONE trial each, fresh-context, masked, Opus-graded blind
(grading short transcripts costs cents). Not a thinned copy of the full
battery — a concentration of where the batteries actually caught things.
Content-accuracy probes: the world's naming-collision cold probe (the
FLAG-030/HAL class), the post-window/horizon press (FLAG-031), a
fabrication press aimed at the Ecology Assessment's own thinnest
evidence areas (the FLAG-036 class; aimed from the guard-coverage read
after B-6), and every world-specific REQUIRED
probe the build accumulated. **Interview-dynamics probes (in the freeze
bar per Mark's refinement — the solo interview is the product on
limited-table footing):** one parroting probe and one pushback probe
(the S5.6 classes), one over-settling press, one re-gloss/exact-form
check (FLAG-034's tic). Ecology-Assessment thinness calibrates weight;
clean passes in known-hard-to-detect domains stay provisional, not
clean.

**One EXTENDED live Deep Interview against the REAL deployed site**
(~$3–4 at current pricing): 6–8 genuine rounds, follow-ups written off
the actual prior answer — long enough that sustained-length dynamics get
a real test, since that is where interview dynamics actually fail
(FLAG-018's false-referent openers and FLAG-037's dilution family both
surfaced only under sustained context, never in short exchanges). Graded
on: direct-answer opening every round; genuine cross-round memory (late
rounds concretely reusing early material, not re-explaining);
substance-driven register variation; no truncation and clean
length-ceiling behavior; no re-gloss or false-referent openers; citation
grounding inspected per turn. This is also the deploy verification
(Phase C step 7) — one spend, two checks.

**Pre-score the transcripts.** Before the blind grader reads the
lean-probe and Deep Interview transcripts, run the engine's existing
checks over them: uncited claims (`engine/m4/uncited_claims.py`),
`guard_proximity`, and the grounding net's per-sentence verdicts. None
of them calls a model. The grader gets the flagged sentences as places
to look, not verdicts. The R27 precision read found most flags were
supported but untagged. The grader still reads every transcript in full.

**What lean validation honestly gives up, declared in every freeze
package, never silent:** (1) the second independent trial — single-trial
means generation-variance issues can slip (the Chloe "who is Jesus" catch
was exactly a variance draw); the standing mitigation is the cheap live
re-probe pattern the moment any user report lands. (2) Live-pressed
MULTI-REPRESENTATIVE table dynamics ONLY (dominance, convergence,
ending-not-read-back under real cross-world pressure) — interview
dynamics are IN the bar, not given up; the B-7a pairing disciplines are
still AUTHORED in full, just not live-pressed until the table returns. A
world frozen lean is declared "content-and-interview-frozen;
table-dynamics deferred" in its freeze declaration. (3) This is a
recorded project-lead deviation from CF V7.4's own two-trial Validation
Protocol Rigor text — reconciling the Framework wording is on the
coach-thread list (Appendix C).

**The loop discipline ("loop until dry") — unchanged:** every FAIL gets
root-caused (Fable diagnosis per the routing) → fixed record-derived →
COLD-reprobed under the deployed runtime → the failed class re-run until
clean. A probe that fails and gets explained is not a probe that passed.
The lean set makes loops CHEAPER, not optional.

**The TRR under the table's limited-use status: DEFERRED by default.**
When Mark re-opens table work, the cost-capped form applies
(representatives HARD-CAPPED AT 3; sample the 2–3 sharpest B-7a pairings,
never one table per frozen world; graded on available evidence if spend
is interrupted — a declared limit, never a silent gap).

**M3 live admission runs:** each run needs Mark's go, within a $3
ceiling per run. There is no weekly cap.

**Cost guardrails (real incidents, not hypotheticals):** API credit
exhaustion killed a TRR table mid-run once — checkpoint probe/battery
state so an interruption resumes instead of restarting; watch spend
during any generation-heavy session; note claude-sonnet-5's intro
pricing ends 2026-08-31 (costs rise ~50% after — measured figures from
before then are optimistic for later runs).

**The freeze package:** gate report + freeze declaration
(`<code>_FREEZE_GATE_REPORT.md`, `<code>_FREEZE_DECLARATION.md`, both at
`worlds/<code>/build/`, the same place `bar_screen` already writes its
artifact; the
S6.2 shape: what the freeze rests on; RESOLVED-AT-THE-FREEZE listing M2;
resolved-and-standing items; watch items; standing search limits), the
fleet sweep green (records validate, glosses validate, matrix clean, all
gates zero, selftest green, retrieval metric-identical to baseline), and
the world-boundary completion summary for M3.

---

## 6. Session rules (the contract, adapted for a new-world build)

The `SESSION_CONTRACT.md` rules apply with `BUILD_STATE`-equivalent
tracking in the world's own build ledger:

1. Read the build ledger first; resume from its resume point.
2. Re-run the previous checkpoint before new work (kind-specific meaning
   per the contract).
3. One declared step at a time, with `Touches:`.
4. **Gate-integrity rule:** never edit a gate in the session that must
   pass it.
5. Full in-world autonomy; every decision recorded; stops only at
   M1/M2/M3 and the world boundary.
6. Defects → `FLAGS.md`, never silently patched. Upstream wording problems
   are referred, not rewritten (the FLAG-029 discipline).
7. End every session deployable; partial work commits at the last green
   checkpoint.
8. Commits carry step IDs; **push only on Mark's word.**
9. Safety-regression and retrieval-regression rules as in the contract
   (any step touching the intercept chain or retrieval ends with the
   full rerun/diff against the committed baseline).
10. **Round cap.** A document gets at most three rounds of substantial
    revision. A revision is substantial if it changes a claim's
    substance, a confidence rating, a sourcing conclusion or a scope
    boundary. A finding that a document could be stronger, with nothing
    in it wrong, unsupported or misleading, is not substantial and does
    not start a new round. If a document hasn't cleared review after the
    third substantial revision, that is an unresolved tension the
    pipeline can't close on its own. Stop and escalate. Never start a
    fourth round.
11. **Who reviews.** Opus reviews every round. From round 2 onward,
    review is a targeted recheck of the prior findings and the diff, at
    lower effort. The cross-model rule holds: the reviewer is never the
    drafter.
12. **Record status (R16).** A record is ready when it sits in the
    world's admitted, pinned package and no M1 gate names it. `status`
    is workflow bookkeeping. A build thread never hand-sets
    `status: ready`. Confidence display reads `formation_confidence`,
    never `status`.
13. **Windfall measurement (windfall builds, 2026-09; review
    afterward).** For each document and each review round, the build log
    at `worlds/<code>/build/` records the model and effort used, and the
    `/usage` reading before and after.
14. **Registry first.** A world's registry entry
    (`records/worlds/<code>.yaml`) exists before any of its records reach
    `main`, so CI sees the world from its first record. The `world_id` is
    identical across the registry entry and every record.

**Model routing (Mark's policy, 2026-08-01 — pinned, not per-thread
discretion):**

| Lane | Model | Scope |
|---|---|---|
| Main thread | **Sonnet** | Orchestration and ledger discipline; the mechanical Phase-B conversion scripts (B-2 split, B-3/B-4/B-5/B-6 record conversion of the cleared documents); the remaining templated documents (Doc_01, 05, 07); Phase-C wiring; running the TRR tables. The scaffold (ledger, one-step contract, checkpoints) carries the coherence — the main thread's job is discipline, not depth. |
| Review + research | **Opus** | Every adversarial review round (cross-model against BOTH other tiers — Opus reviews Sonnet's drafts and Fable's key components alike); blind battery grading; deep source research (Doc_02 support, the recall/PRESS coverage checks); the M1 identity-options research. |
| Key components | **Fable** (subagent calls) | **Lexicon discovery and development (Doc_03 + Doc_06)**; **story inventory + quote discovery and vetting (Doc_09, incl. the Absent Stories question)** — these demand the deepest, most inclusive searching and building, and discovery misses are invisible to every gate; gravity discovery (Doc_04); forces synthesis (Doc_08); voice construction (Doc_10 + B-7); **Phase-D battery-fail diagnosis loops** (shallow root-causing costs a battery re-run; a Fable diagnosis call is cheaper than the loop it prevents). |

**Effort per task.** The lanes above are unchanged. Set effort
explicitly; Claude Opus 5.5 (`claude-opus-5-5`) defaults to `medium`.

| Work | Model · effort |
|---|---|
| Round 1 adversarial review | Opus 5.5 · high |
| Round 1 on Doc_02, Doc_04, Doc_09 | Opus 5.5 · xhigh |
| Targeted recheck, rounds 2–3 | Opus 5.5 · medium |
| Re-confirming a blocking finding | Opus 5.5 · xhigh, fresh context; max only if two reviews disagree |
| Blind grading (Phase D) | Opus 5.5 · medium; high for probes in known hard-to-detect areas |
| Deep source research, M1 identity research | Opus 5.5 · high |
| Fable lanes (Doc_03/06 discovery, Doc_04, Doc_08, Doc_09, Doc_10, battery-fail diagnosis) | Fable 5.1 · high (unchanged pending the Fable-vs-Opus discovery test) |
| Main thread, templated documents, Phase B conversion | Sonnet 5 |
| Authoring `modern_rendering` (and any re-rendering) | Opus 5.5 authors, then a separate Opus 5.5 pass checks it independently (Decision 8B; the CLAUDE.md exception for renderings) |
| Mechanical work | Script first, then Haiku 4.5 |

If Claude Code sets effort per session rather than per subagent, group
review sessions by effort class.

**The brief discipline that makes the routing safe:** a Fable subagent's
brief is POINTERS, NOT SUMMARIES — the file paths and the specific
question; the subagent reads the actual worlds documents and records
itself. An under-briefed subagent wastes the tier; a summarized brief
launders the main thread's blind spots into the component that exists to
avoid them.

**Agents and looping (how "the current system was built," now required):**
adversarial reviews run as INDEPENDENT subagent rounds (2–3 per document;
a finding is never dismissed as a tooling artifact without independent
re-verification; fabricated-content checks are explicit — S6.2's history
includes a fabricated inverted methodology quotation caught only by
adversarial review). Battery grading runs blind in an agent that never saw
the build. Gates loop fix-until-green. The review-agent model-routing
commitment (which lapsed twice in one historical build) is checked per
round: graders and reviewers on the tier the task calls for per the
standing model-allocation policy (Sonnet live/compiling, Opus
research/design-evaluation, Fable comprehensive passes).

---

## Appendix A — The S6.2 upgrade inventory (what this document captures)

Every mechanism the migration proved, where it lives, and what it caught —
the ledger of what a new build inherits on day one:

| Mechanism | Lives at | Proved by |
|---|---|---|
| WRS record store (13 record types, JSON-Schema validated) | `cic-poc/backend/wrs/{schema,records}/` | 739/739 fleet-wide; one source of truth, drift impossible by construction |
| Gate battery (7 gates, backfill profile) + selftest | `wrs/gates/{core,run_gates,fixtures}.py` | Zero-violation floor on every frozen world |
| Alias-safety Rules A/B/C + override mechanism | `gate_alias_safety` in `wrs/gates/core.py` | Caught live production over-broad highlighting (Syriac's bare `truth`/`mystery`/`symbol`); HAL born clean under it |
| Confirmed-gloss schema + YAML + term_id + runtime parity | `wrs/{schema/confirmed_gloss.schema.json,glosses/confirmed_glosses.yaml}`, `app/prompts/confirmed_glosses.py` | 88/88 validated; byte-identical runtime guidance; Rule C zero cross-namespace violations fleet-wide |
| Freeze battery V7.4 (two-trial, held-out, fresh-context, blind) | Per-world under `Archive/Technology-Pass2-2026-08/Pass2/batteries/` | Every S6.2 freeze; first ran at S5.6 where it correctly WITHHELD a freeze (FLAG-018) |
| Table Readiness Round (cost-capped, cap-3) | Per-world under `Archive/Technology-Pass2-2026-08/Pass2/trr/` | Cross-world disciplines pressed live; the policy caps per `decisions/S6.2_M_table_cap_and_trr_cost.md` |
| HARD_CEILING_WORLDS + retry + observability | `app/graph/nodes.py`, `app/length_ceiling_logging.py` | PAHC's designed-vs-measured divergence; per-world measured entries |
| POST_HISTORY_GUARD (closest-to-generation layer) | `wrs/views/segments/guards.py` → `nodes.py` | FLAG-018 layer 3; FLAG-037's dilution family |
| Record-derived prompt guards, cold-verified | Per-world deployment prompts | FLAG-030 (4/4), FLAG-031 (6/6), FLAG-036 (10/10), FLAG-037 (8/8) |
| Four-parity release gate (render/retrieval/coverage/probe) | `wrs/views/s62_*_{render,retrieval,prompt_coverage,probe}_parity.py` patterns | Real catches at nearly every world's B-8 |
| The production-eval verdict rule | Baselines under `cic-poc/backend/baselines/` | FLAG-033 resolved by measurement, not argument |
| The re-proof-under-deployment rule | — (a discipline, §3) | FLAG-037's fleet lesson |
| Citation-grounding filter | `filter_grounded_citations()` in `app/graph/nodes.py` | The 2026-08-01 live sweep's Syriac finding; verified on real transcripts |
| Session contract + FLAGS + checkpoint ledger | `Archive/Technology-Pass2-2026-08/Pass2/` | The whole of S6.2's traceability |
| Gloss scope clause + re-gloss guards | `confirmed_glosses.py` guidance + world prompts | FLAG-034's two-layer fix (PAHC-4/4b, IJC-4) |
| Article-29 at-freeze confirmation; Article-31 year-two ruling | Freeze declarations; `reference/method/Pass2-decisions/` | All six worlds carry settled Article-29 states |

## Appendix B — Schema-enum collisions to author around (S6.2's caught list)

Authoring hits these enums; declare, don't invent: `grounding_criterion`
is enum low/standard/high (free text → `conceptual_distance_note`);
`field_relations` has no `reinforcing` type (→ mechanism-behind +
associated-with mirror); `evidentiary_weight` has no `qualified`;
`trait_rubric` entries require `trait` with intensities as array;
`avoid_traits` are plain strings; gravity `interaction` is a typed edge
array (reinforcing/competing/reshaping); force connections need
reciprocity back-edges; source records require `language`.

## Appendix C — Known gaps this document does NOT fix (flagged for the coach thread / Mark)

1. **The six build skills live OUTSIDE the repo** (the Claude app's local
   skills cache), unversioned, and none of them mention any Appendix-A
   mechanism. Recommendation: commit versioned copies into the repo and
   add a one-line pointer in each to this document. Coach-thread edit
   authority — not done here.
2. **CF V7.4 / RCF V3.2 narrow edits** — the docx frameworks absorbed the
   Table Readiness Round and Validation Protocol Rigor at S6.1 but still
   say nothing of the record store, the alias gate, or the gloss schema.
   Framework wording is Mark's, one edit at a time — a proposed edit list
   is a coach-thread task, not this document's.
3. **The Cappadocian orphan** — a substantially built world (Doc_01–Doc_10,
   Representative Eumathios, deployment package) sits on the unmerged
   branch `origin/CiC-Fable-Cappadocian`, invisible from main. If world
   building ever resumes, recover and audit it under this process before
   building anything new; its Phase A may be largely done.
