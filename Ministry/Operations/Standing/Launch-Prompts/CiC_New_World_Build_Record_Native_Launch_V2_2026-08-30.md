# Launch prompt — Record-Native World Build (V2, 2026-08-30)

**V2 change (Mark's rulings, 2026-08-30, industrializing the pipeline
after the pilot launch):** "not full automation, but as much as
possible. i don't want to be just pushing a button or saying i approve
when no real decision is being made." Five structural changes from V1:
(1) the build runs autonomously under CO-022's self-disposition
discipline between gates, and every gate that remains is a REAL
decision — what Mark actually decides is written into each gate below,
and a gate with nothing real to decide does not exist; (2) a new Source
Acquisition gate: the pipeline identifies the open-source editions, and
Mark manually downloads them into the vendored library — edition and
rights choices are his; (3) the launch-phase birth conditions (register
bar V1.1, transparency ground V1.2) are in force from the first record;
(4) the prompt is GENERAL: it launches any world, listed in the Step-0
portfolio or not — an unlisted world opens with the G0 scope gate below
(same-day ruling; the roadmap ahead runs through Galatia, then
pre-Reformation and Reformation worlds, none of which the original
portfolio scoped); (5) stewardship never outranks quality (Mark: "while
good stewardship is important it shouldn't compromise the quality") —
see the cost section. V1's model-routing policy (Mark, 2026-08-01) and
lean-validation default carry forward.

Paste this into a fresh thread when a world build is authorized. Fill in
the one blank. The thread runs the build with agents and quality loops
and stops only at the gates and escalations below.

> **WORLD TO BUILD:** ______________________
>
> If the named world is IN the Step-0 portfolio
> (`CiC_Step0_Conclusion_FINAL_v2.docx`), build on its conclusions and
> skip G0. If it is NOT (Galatia; any pre-Reformation or Reformation
> world), the build OPENS at G0 — no Doc work before it clears.
> ALWAYS check first for a prior partial build of the named world
> (unmerged branches, `Archive/`, `World-Builds/`) — recover and audit
> under the process document rather than rebuilding from scratch
> (precedent: Cappadocian on `origin/CiC-Fable-Cappadocian`).

## What this thread does

Build the named world end-to-end — Step-0 confirmation through a
drafted freeze declaration — **born record-native and born at the bar**,
under `Ministry/Technology/CiC_Record_Native_World_Build_Process_V1_2.md`.

Read IN FULL, in this order, before any work:

1. The Build Process V1.2 (sequences everything; Phase B's two birth
   conditions — the register bar and transparency ground — govern every
   spoken field from the first record).
2. `Ministry/Technology/CiC_Register_Bar_2026-08-29.md` — the ONE
   approved sample. Every spoken field is drafted with it open. It is
   the standard; no banned-word lists exist or accumulate anywhere.
3. `Ministry/Technology/CiC_World_Build_Completion_Standard_V1.2.md`.
4. The Construction Framework V7.4, the RCF V3.2, and
   `Ministry/Technology/Pass2/SESSION_CONTRACT.md` — the process
   document tells you where each governs.
5. The cic-build-cycle discipline (CO-022): one document at a time,
   review files as artifacts, self-disposition for procedural work, the
   four standing escalation categories, Frozen never self-assigned,
   nothing attributed to the project lead without a verifiable record.

## The gates — every one a real decision

Everything between gates is the build thread's to decide, do, and
record under CO-022. Everything below stops the build until Mark's own
decision, and each names what he is actually deciding — never a bare
"approve":

**G0 — Portfolio admission (unlisted worlds only), before any Doc
work.** A world outside the Step-0 portfolio is a portfolio-level
decision by definition (CO-022 category 2). Prepare a Step-0-grade
scope brief and STOP: proposed time window and boundaries; era
placement and what it implies for the Atlas/census (a new era is its
own flagged decision); a source-landscape preview (what kinds of
sources exist, the rights outlook — post-1500 worlds mean many modern
translations are UNDER COPYRIGHT, so name the public-domain path
honestly or the licensing question plainly); living-tradition proximity
(the Article 29 outlook — Reformation worlds have direct denominational
descendants, which sharpens the bounded-reconstruction discipline);
known sensitivities (e.g., inter-tradition polemic in the sources,
carried per the project's own named-plainly-not-reenacted precedent);
and — for apostolic-era worlds like Galatia — the methodology question
stated as a question: how canonical Scripture itself functions as a
world-source is NOT settled precedent from the pilot fleet, and Mark
rules on the approach before it is used. What Mark decides: whether
this world enters the portfolio at all, its era and window, and the
named new-territory approaches. His ruling is recorded as a decision
artifact the whole build cites.

**G1 — Scope & Sources, after Doc_02 clears review.** Present the world
scope AND the **Source Acquisition Manifest** (format below). What Mark
decides: whether this world's window and boundaries are right, and
WHICH editions enter the library — rights, translation, and scope
choices per source, with the manifest's own recommendations to accept
or override. He then manually downloads the chosen open-source texts
into `cic/texts/` under the manifest's stated filenames. The build
VERIFIES every listed file is present and matches its stated
size/identity before Phase A continues past Doc_02 — a missing or
substituted file is a halt, never a workaround.

**G2 — Representative identity, after Doc_09.** The grounded-options
artifact: named ROLE + NAME alternatives, an explicit trade-off each,
one recommendation each (Alexandria/Hieronymian precedent files are the
shape). What Mark decides: who speaks for this world. He has overridden
the recommendation on multiple worlds — present real options, record
his actual words, proceed only on his choice.

**G3 — The bar read, at the end of Phase B.** The bar screen artifact
(quote-stripped grade, longest sentence, fragment ratio — visibility
only, nothing gates on a number) plus a curated sample of spoken fields
across record types, read against the approved sample. What Mark
decides: whether this world's voice is actually AT the bar — the read
that set the pilot's quality. A sentence he has to re-read, or has to
ask the meaning of, fails; that question IS the finding, and the fix
lands in records.

**G4 — Article 29 determination**, listed in the freeze declaration for
explicit confirmation (carry `provisional` until then). What Mark
decides: the living-tradition determination itself.

**G5 — Admission & freeze.** Draft the declaration, post the
world-boundary completion summary, run the lean validation battery
(below), then stop. What Mark decides: admission — on the battery
evidence PLUS his own live conversation with the world, never on a
score. Only Mark assigns Frozen.

Standing escalations apply at any point regardless of gate position:
identity/name/title changes, portfolio-level decisions, governance or
methodology changes, and unresolved tensions the pipeline cannot close
(CO-022's four categories). Article 31 is NOT a stop (provisional by
design, year two — standing ruling).

## The Source Acquisition Manifest (G1's artifact)

One row per source the world will cite, produced during Doc_02 and
frozen at G1. Columns:

| Column | Content |
|---|---|
| source_id | the row's future record id |
| work / edition | title, translator/editor, year — the exact edition proposed |
| rights_status | public-domain / licensed / excluded, with the basis |
| where | the open-source location (CCEL, archive.org, etc.) — a real, checked URL |
| destination | exact filename under `cic/texts/` per the library's naming convention (`<slug>_<work>_<edition><year>.<ext>`) |
| why this edition | one honest sentence: rights + quality rationale |
| alternatives | the editions considered and passed over, with the reason |
| scope note | what within the file is IN scope (recensions, appendices, spuria excluded — carried verbatim into the source row's license notes) |

The manifest is a decision instrument, not a download list: every row
Mark accepts is an edition ruling that the source records then carry
for the life of the world.

## Birth conditions (Phase B, non-negotiable, from the first record)

- Every spoken field drafted with the approved sample open — plain
  modern English, simple sentences, a scholar's term only after its
  plain meaning, as a label. The world's own words ARE authored into
  the spoken prose where their territory is discussed (the lexicon
  label form: "give thanks over the cup — the eucharistia"), so the
  transparency scan can light them.
- Quote records author `modern_rendering` at birth; the original stays
  as `text` for the click-through page.
- Every substantive cell offers a genuinely-belonging story and term at
  birth or records its honest empty; forced fill fails the read.
- No spoken field hard-binds a first-mention introduction formula
  ("One of us, N,") to its answer — the plain name speaks; introducing
  figures is the system's job.
- Figure records author at least one name whose comma head is the name
  the voice actually says.
- Gates green from the first record (Hieronymian's born-at-zero
  standard); a new record set opens at alias_safety zero or the step
  isn't done.

## Model routing (pinned — Mark's policy, 2026-08-01, names refreshed)

Orchestration, ledger discipline, mechanical record conversion,
templated docs, wiring, and validation execution run on the
**Sonnet-class** thread (current generation at launch time). Reviews
and blind grading run as **Opus-class** subagents (cross-model
independence both directions). The key components run as **Fable
subagents**: lexicon discovery/development (Doc_03 + Doc_06), story
inventory + quote discovery and vetting (Doc_09) — discovery misses are
invisible to every gate — plus gravity discovery (Doc_04), forces
synthesis (Doc_08), voice construction (Doc_10 + B-7), and battery-fail
diagnosis. Fable briefs are POINTERS, NOT SUMMARIES: file paths + the
specific question; the subagent reads the sources itself. Handoffs
happen at document boundaries through the repo's own artifacts (docs,
review files, records, manifests) — the repository is the context bus;
no phase re-narrates state to the next.

## Cost (one real approval, not a drip of empty ones)

**Governing rule (Mark, 2026-08-30): stewardship never outranks
quality.** The envelope is a planning instrument, not a quality
ceiling. If staying inside a number would mean shipping under-bar work,
the build HALTS and states the choice in dollars — it never quietly
thins the work to fit. Doing the job right inside the current scope —
an extra review round, a battery-fail loop run to clean, a re-probe —
is always in-policy without a fresh approval; it is simply reported in
the real costs. The halt-and-ask is for genuinely expanded scope, never
for quality.

At launch, before any billed work: estimate the world's build envelope
from the current rate card (generation lanes + review rounds + lean
validation), state it in dollars with the lanes itemized, and get
Mark's one approval of the envelope. Within it, the build runs without
per-call asks; projected overrun or an exhausted allocation is a HALT
at the last green checkpoint, stated plainly with the revised estimate
— never silent continuation, never a mid-build unbudgeted lane.

Lean validation stays the default (Mark's cost policy, 2026-08-01):
free floor (gates/schema/parities/coverage) + ~10–14 single-trial
targeted probes blind-graded (content classes PLUS parroting, pushback,
over-settling, re-gloss) + ONE extended live Deep Interview (6–8
rounds) against the real deployed runtime. The full V7.4 two-trial
battery and the TRR run on Mark's word only — and if the build judges
lean insufficient for THIS world's specific risks, it says so at G5
with the reason and the price, so the choice reaches Mark as a quality
decision, not a budget one. The freeze declaration names what lean
gives up — never silently. Checkpoint probe state so interruptions
resume rather than restart.

## When done

World-boundary completion summary to Mark: what froze, what is listed
for G4/G5, gloss/lexicon items pending his one-at-a-time confirmations,
watch items, and real costs per the standing real-not-estimated
discipline. Then hand a summary to the System Hub thread to sync the
Standing files — do not edit the Dashboard, Task Board, or Gantt
yourself.
