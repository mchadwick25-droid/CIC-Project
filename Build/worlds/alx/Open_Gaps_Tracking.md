# Open Gaps — Alexandria (Catechetical-School) Formation World

Running, dated ledger for the Alexandria world build. Same discipline as
`Build/worlds/syr/Open_Gaps_Tracking.md`: dated entries,
disclosed-recovery notes, honest status, project-lead-anchored where confirmation is a
project-lead act. This file is the durable record; no real decision, review outcome, or
open question lives only in the build thread's own conversation history.

---

## Thread scope and hard stopping point (established at thread launch, 2026-07-17)

This is a **world-build thread**, held to the same one-document-at-a-time, review-gated
Construction Framework discipline as every other CiC world (`cic-build-cycle`).

- **Builds:** Doc_01 (World Identification & Boundaries) through Doc_09 (Story Inventory,
  World Profile, Validation Layer) — Steps 1–9 of Construction Framework V7.3.
- **Hard stop:** **before any Representative decision.** Step 10 (Representative
  Emergence — role, name, title, voice) is **not** in this thread's scope. It belongs to
  Mark directly, in person. This thread does not draft a candidate name, propose a role
  framing, or begin Step 10 (not even its Phase One Ecology Assessment, which already
  presupposes an identified figure). When Doc_09 is complete and cleared, the thread
  reports and waits.

---

## Governing documents confirmed for this build (2026-07-17)

- Vision: `Build/Ministry/Communication/Vision, Mission, Convictions, and Foundational Commitments V1.1.docx` (read).
- Constitution: `Build/reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx` (read). Relevant articles for
  this thread: 3 (Formation-World Principle; Representative last; **No Forward-Projected
  Specificity**), 17 (five-level confidence vocabulary), 18 (Historical Locality /
  Situated Knowledge), 19 (Story/Memory; no free invention), 20 (Marginalized-voices
  affirmative duty), 21 (Strand Determination), 22 (Forces Principle), 23 (Writing-From-
  Inside), 26 (Author Gravity + [CT] tagging), 28 (Scholarly Integrity), 29 (Living
  Tradition Status — **freeze-eligibility gate**), 31 (External Scholarly Review — freeze
  gate; **all AI review is "Simulated review — informational only, not an Article 31
  substitute"**), 36 (Sole-builder; deferrals documented).
- Methodology (binding): `Build/reference/L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.3.docx`
  and `CiC_L3B_Formation_World_Blueprint_V7.3.docx`; `Build/reference/L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx`.
- Rigor/format model followed: `Build/worlds/syr/`.

**Current step sequence (Framework V7.3, Part VII), confirmed against the Framework text
— NOT assumed from the archived `alex_DocNN` numbering:** Step 1 Doc_01 World
Identification/Boundaries/Orientation · Step 2 Doc_02 Source Ecology · Step 3 Doc_03
Lexicon Candidate List · Step 4 Doc_04 Gravity Discovery · Step 5 Doc_05 Ecological
Reconstruction · Step 6 Doc_06 Full Lexicon Development · Step 7 Doc_07 Integrated Ecology
Analysis · Step 8 Doc_08 Forces Document · Step 9 Doc_09 Story Inventory + World Profile +
Validation. Step 10 Representative Emergence is out of scope (see hard stop).

**Review = AI review.** Every independent review in this thread is conducted by an
adversarial AI subagent and is marked, per Constitution Article 31, **"Simulated review —
informational only, not an Article 31 substitute."** It informs disposition; it never
validates the world.

---

## Source-material handling (2026-07-17)

Primary source: `Archive/Alexandria-Build-History/Alexandria-v7/` — rigorously built, but
under an **older methodology** (its own docs cite "Construction Framework v1.6 / Blueprint
v1.5" and old Phase 3/Phase 4 numbering). Its same-numbered `alex_DocNN` files are used as
**working source material for each step's fresh current-cycle draft**, never adopted as
pre-cleared. Every document gets its own current-cycle draft, review, and clearance.
Strongest reusable asset: the per-term lexicon (`Lexicon MD files/alexlex001`–`alexlex045`
plus Tier2/Tier3 summaries) — drawn on heavily at Step 3/Step 6, but every term re-drafted
and re-reviewed in this cycle.

Secondary/superseded source: `Archive/Alexandria-Build-History/Alexandria-WorldBuilds/` —
older, superseded methodology generation. Mined for raw content only if Alexandria-v7
leaves a real gap; **never** for methodology, structure, or its Representative decision.

---

## Standing open items (project-lead-facing) — carried, not resolved by this thread

### OG-1. Article 29 Living Tradition Status — **RESOLVED / CONFIRMED by the project lead, 2026-07-17.**
**Resolution (2026-07-17):** the project lead (Mark Chadwick) confirmed, in session, **Article 29 Living Tradition Status** for this build — the **Coptic Orthodox Church** as the primary living heir, with a commitment to the Article 28 historical/living differentiation duty (the world is the formation *as it was*, c. 150–400; the present-day Church's self-understanding is its own). A fresh, dated project-lead act, **not** an inheritance of the prior self-certification. This **clears the Article 29 freeze-eligibility gate.** Recorded in Doc_01 §9 and World Profile §9 (PENDING→CONFIRMED). **The world remains NOT frozen** — Article 31 (OG-4) is still outstanding. *Original finding (retained for the record):*

**Downstream sync gap found and fixed 2026-09-20, while resolving the analogous `hal` case.** Despite OG-1's own 2026-07-17 confirmation, two machine-checked surfaces had never been brought in line with it: `records/worlds/alx.yaml`'s own `living_tradition_flag` (correctly `true`, matching the confirmation) disagreed with the public Atlas census (`cic-website/data/world-census.json`'s `alexandria-catechetical` entry), which still read `living: false` — flagged as fleet finding F-06 in `engine/m1/cross_world.py`'s own `ACCEPTED_OPEN` waiver, tracked there since before this confirmation existed. Verified directly against OG-1's own text and the World Profile §9 language above before touching anything: the registry's `true` was the correct, confirmed value all along; only the census had never been updated. Fixed by flipping the census's `living` field to `true` and removing the `census-living-flag/alx` waiver entry. No content or grounding change needed — this world's own `facilitator_brief` record already stated the Coptic Orthodox heir correctly, cross-checked against OG-1 at build time.


Verified 2026-07-17 (independent read of `Archive/.../Alexandria-v7/Operations/CiC_Phase_Status_V7_r1.md`
and the extracted text of `alex_Living_Tradition_Status_V7_r1.docx`). The archived record
marks Article 29 "CLEARED" for Alexandria against the **Coptic Orthodox Church**, but the
clearance is attributed to *the document itself* ("This document constitutes the formal…
Confirmation") — **no named human confirmer, no project-lead decision, no dated sign-off.**
Per the launch instruction and the `cic-build-cycle` discipline, a Living Tradition Status
confirmation is a **project-lead act** tied to a specific build and does **not** carry
across a methodology change on the strength of a self-declaring artifact. **Status: treated
as NOT confirmed for this build.** Article 29 is a freeze-eligibility gate at Step 9 and
belongs to Mark directly; this thread will surface it, not assert it. Article 31 (external
scholarly review) was recorded "Outstanding" for Alexandria and remains so.

### OG-2. "Theon" is a superseded-track Representative decision — NOT inherited, and stripped from Doc_01 source use.
The lower-priority `Alexandria-WorldBuilds/` track carried Alexandria all the way to naming
a Representative, **"Theon."** The Alexandria-v7 Doc_01 source itself also contains
"Theon"-specific content (Living Tradition Status, Contested-Figures/Origen, Mission
Alignment). Per Constitution Article 3 (No Forward-Projected Specificity) and this thread's
hard stop, **all Representative-specific content is removed** when Alexandria-v7 material is
used — the underlying *world-level* facts (e.g., Origen's standing unresolved within the
horizon) are kept as world features; the Representative framing is not. "Theon" is surfaced
to Mark, if/when the Representative discussion happens (not in this thread), only as
historical context from a superseded track — never as a default to confirm.

### OG-3. World scope and name — **RESOLVED / CONFIRMED by the project lead, 2026-07-17.**
**Resolution (2026-07-17):** the project lead (Mark Chadwick) confirmed, in session, **option (a) the broad reading as proposed** — confirmed world name **"Alexandrian Christianity (Catechetical-Formation World)"**, the c. 150–400 ecology anchored and named by its catechetical-formation tradition (anchor, not boundary). The whole cleared cascade (Doc_02–09) and the Representative build stand on this reading; **no rework required.** Recorded in Doc_01 §1.3 / §11 and World Profile §11. *Original framing (retained for the record):*


The build folder Mark named is `Alexandria-Catechetical-School`, which could imply a
**narrow** world (the *didaskaleion* institution: Pantaenus/Clement/Origen/Heraclas/
Dionysius/Didymus) distinct from a **broad** "Alexandrian Christianity" ecology (150–400
CE, including Athanasius, Nicaea, episcopal enforcement, monastic emergence, the Coptic
heir) as Alexandria-v7 built it. Doc_01 argues the scope explicitly (rather than assuming
it) and proposes a name. Because the world's name and outer scope are foundational and the
folder label is a real signal of possible narrower intent, **this is flagged for Mark's
confirmation** — see Doc_01's scope/name section. Not treated as an escalation-blocking
item (Step 1 exists to argue scope), but named plainly so Mark can redirect before the
downstream cascade is built on it.

---

## Build log (per-document disposition)

*(Updated as each document reaches at least "Approved to proceed." Format: document ·
review outcome · revision rounds · review-artifact file(s) · disposition.)*

- **Doc_01 — World Identification, Boundaries, Orientation:** **Approved to proceed** (self-disposed by build thread, 2026-07-17). Review outcome: Round 1 SUBSTANTIAL REVISION REQUIRED (2 substantial Article 28 citation-integrity fixes in the scope argument — a quote misattributed to van den Hoek that is actually van den Broek's; an inverted representation of Scholten — plus 3 cosmetic), all resolved; Round 2 CLEARED, no new substantial findings. Revision rounds: 1 substantial + cosmetic pass. Review artifacts: `Review-Artifacts/Doc_01_Round1_Review.md`, `Review-Artifacts/Doc_01_Round2_Review.md` (both AI review, marked per Article 31). No escalation category applied. World name/outer scope remains flagged for the project lead (OG-3); downstream built on the broad reading unless redirected.
- **Doc_02 — Source Ecology:** **Approved to proceed** (self-disposed by build thread, 2026-07-17). Review outcome: Round 1 SUBSTANTIAL REVISION REQUIRED (1 substantial — missing five-dimension Author Gravity entries for the secondary narrative sources Eusebius/Palladius/Dionysius/Gregory, per Framework Part II; + 3 cosmetic; all 13 secondary citations and all primary dates web-verified clean), all resolved; Round 2 CLEARED, no new substantial findings. Revision rounds: 1 substantial + cosmetic pass. Review artifacts: `Review-Artifacts/Doc_02_Round1_Review.md`, `Review-Artifacts/Doc_02_Round2_Review.md` (AI review, marked per Article 31). No escalation category applied. 12 evidence streams; Article 20 affirmative duty named; forces lens applied; Origen SYSTEMIC / Eusebius HIGH Author-Gravity screens set for Doc_04.
- **Doc_03 — Lexicon Candidate List:** **Approved to proceed** (self-disposed by build thread, 2026-07-17). 130 candidates (44 prelim Tier-1, 86 Tier-2; 7 CT, 12 cross-build/desert), no `alexlex` numbers assigned (numbering is Step 6), tiers preliminary pending Doc_04. Companion queryable index `Lexicon_Candidate_Index.xlsx` (tags as filterable columns; By-Tier/By-Tag/CT-Contest-check/Cross-Build sheets). Review outcome: Round 1 SUBSTANTIAL REVISION REQUIRED (1 substantial — inverted van den Broek/van den Hoek-vs-Scholten mapping on the Didaskaleion CT contest, the same class of defect as Doc_01 R1; + 2 cosmetic; index confirmed matching list with zero drift), all resolved; Round 2 CLEARED. Review artifacts: `Review-Artifacts/Doc_03_Round1_Review.md`, `Doc_03_Round2_Review.md`. Corrected an inherited Alexandria-v7 defect: all CT candidates now tagged [CT] with contests specified (the source had assessed 6 contested but tagged only 1).
- **Doc_04 — Gravity Discovery:** **Approved to proceed** (self-disposed by build thread, 2026-07-17). Built to the Doc_04 Template V1.0 (9 sections) + companion `Gravity_Index.xlsx` (Candidates, Interaction Matrix, By-Classification, By-Cross-Check-Flag, Cross-Build; synced 2026-07-17). **Classification: 2 Primary — Scripture as Deep Formative Reality, Transformation of the Soul Toward God (both confirmed for the *literate-attested* ecology only); 3 Supporting — Divine Pedagogy, Logos-Centered Unity, Learning-Formation Integration; 4 Tensional — Teacher–Bishop, Learning–Community, Speculative-vs-Doctrinal-Boundary, Martyrdom-vs-Contemplative-Ascent; 3 Formation Dynamics.** Origen-SYSTEMIC two-level screen and Eusebius-HIGH screen applied throughout; cross-build (desert) constraint held (no ecology-wide gravity on desert evidence); Article 21 cross-strand substitute = the declared **Cross-Stratum Test**. Review: Round 1 SUBSTANTIAL (Antony sourcing self-contradiction + candidate-ID collision; +5 cosmetic), Round 2 SUBSTANTIAL (ID sweep incomplete), Round 3 CLEARED — 3 rounds. Artifacts: `Review-Artifacts/Doc_04_Round1/2/3_Review.md`. No escalation category applied.
- **Doc_05 — Ecological Reconstruction:** **Approved to proceed** (self-disposed by build thread, 2026-07-17). Re-lensed to the Framework's named lenses (Human, Community, Worship, Organizational, Ministry/Formation) + 5 world-specific (Intellectual/Interpretive, Spatial, Temporal, Boundary, Memory); forces integrated explicitly per lens; Writing-From-Inside inhabited prose quarantined from confidence notes; stratum-bias gap (OG-4) held in every lens (structure at WA/DMR; majority interior Inferential-Thin + explicit non-narration = named absences); Tier-4 synthesis marked with per-element traceability, no Tier-5; all "Theon" configuration excluded. Review: Round 1 SUBSTANTIAL (T4 martyrdom tension harmonized-not-held; Temporal lens missing forces + stratum guard; +5 cosmetic), all resolved; Round 2 CLEARED (+1 cosmetic fixed). Artifacts: `Review-Artifacts/Doc_05_Round1_Review.md`, `Doc_05_Round2_Review.md`. No escalation category applied.
- **Doc_06 — Full Lexicon Development:** **Approved to proceed** (self-disposed by build thread, 2026-07-17). Governing doc + 10 deployment chunk files (`Lexicon-Chunks/alexlex001/002/004/005/007/008/011/014/021/036`) + master `Lexicon_Deployment_Index.xlsx`. `alexlex` numbers assigned (001–045 confirmed Tier-1 roster re-confirmed vs Doc_04; 046 Worship; 047+ Tier-2 — roster is Tier-1/Tier-2 only, no Tier-3). **All 6 CT contest-types specified** (Apokatastasis, Nous, Logikos, Fall/Descent, Homoousios, Didaskaleion); **Doc_03's deferred Restoration-CT resolved to NON-CT** (separable from the condemned apokatastasis; Athanasius attests restoration-without-universalism). Chunks written from-inside (Article 23), Theon-stripped; reciprocity reported honestly (one-directional links flagged as deployment-layer items). Review: Round 1 SUBSTANTIAL (6 substantial — mostly §2/index number sync + false reciprocity reporting; +5 cosmetic), all resolved; Round 2 CLEARED. Artifacts: `Review-Artifacts/Doc_06_Round1_Review.md`, `Doc_06_Round2_Review.md`. **Disclosed deferral (Article 36):** ~~remaining Tier-1/Tier-2 chunk files + full reciprocity completion~~ — **Tier-1 deferral CLOSED 2026-07-17 (gap-closure): all 45 Tier-1 chunks now built + reviewed + indexed.** Remaining deployment-layer follow-on: Tier-2 chunk files and completion of the flagged one-directional reciprocity back-links. **Flagged for coach:** the L4 Deployment_Lexicon_Chunk_Template header says "Version 1.0" though its history includes v1.1 (template-file fix, outside build-thread edit authority).
- **Doc_07 — Integrated Ecology Analysis:** **Approved to proceed** (self-disposed by build thread, 2026-07-17). Integration lenses weighted to the learned-formation axis (Affective, Intellectual/Philosophical, Authority, Boundary, Formation-Logic + Memory, Interpretive, World Theological-Reasoning-Patterns), an **explicit named Forces lens added** (the source lacked one), and a cross-lens synthesis (two hubs: the Participation↔Perception mechanism + the post-Nicene authority shift as single-cause-four-effects; six preserved world-level features). **Source's Representative-configuration material fully excluded** — "Representative Theological Patterns" re-framed to *the world's own* reasoning patterns; §4C tensions held at world level, not as deployment requirements. Stratum-bias (OG-4) held in the affective/formation lenses (majority via observable channels, no narrated interior). Review: Round 1 SUBSTANTIAL (non-existent-lens reference in the proportionality argument; a "seven-not-six" tension double-count; +7 cosmetic), all resolved; Round 2 COSMETIC ONLY. Artifacts: `Review-Artifacts/Doc_07_Round1_Review.md`, `Doc_07_Round2_Review.md`. No escalation category applied.
- **Doc_08 — Forces Document:** **Approved to proceed** (self-disposed by build thread, 2026-07-17) — **required freeze gate now complete.** Six-cell matrix (18 forces × three layers; the 3A-2 Arab-conquest no-Layer-2 exception reasoned as distal); **Transmission numbered as its own force in both 2B (2B-3) and 3B (3B-3)**; standalone Cross-Cell Connections section; Forces-and-Gravities Synthesis connecting **all nine Doc_04 gravities to ≥1 force** — the three the source omitted entirely (Divine Pedagogy, Learning–Community, Speculative-Doctrinal) genuinely connected here. Layer 2 written strictly from-within (Article 23; analytical flags kept in Layer 1); the source's entire Representative-deployment "Section 5" excluded (no "Theon"). Companion `Force_Index.xlsx` (Forces, By-Confidence, By-Connected-Gravity completion-check, Cross-Cell Map, Transmission-Check). Review: Round 1 SUBSTANTIAL (index/prose drift on 3 gravity connections; +4 cosmetic incl. a Middle-Platonism-vs-Plotinus chronology fix), all resolved; Round 2 CLEARED (programmatic 9-gravity prose/index parity). Artifacts: `Review-Artifacts/Doc_08_Round1_Review.md`, `Doc_08_Round2_Review.md`. No escalation category applied.
- **Doc_09 — Story Inventory + World Profile + Validation Layer:** **Approved to proceed** (self-disposed by build thread, 2026-07-17) — **the final document; this thread's stopping point.** Three components: `Doc_09_Story_Inventory.md` (10 stories across Tiers 1–4, **no Tier 5**; Absent-Stories question answered with 5 named absences; `Story_Index.xlsx` with By-Tier/No-Tier-5-audit/Source-cross-ref/Absent-Stories-check), the **Validation Layer** (§5 — the 9 world-level Part VI categories executed and PASS; Representative-dependent testing [Relational Safety, Adversarial Resistance, Encounter] + the Representative probe battery/Dynamic Encounter Validation + the two freeze gates all **honestly deferred, not executed** — the world is **NOT frozen**), and `alex_World_Profile.md` (11-section synthesis of Doc_01–08). Review: **Round 1 CLEARED** (0 substantial; the review web-verified all citations, parsed the index, and confirmed no Tier-5, honest Validation scope, honest Article 29/31 status, and no Theon leak). Artifact: `Review-Artifacts/Doc_09_Round1_Review.md`. No escalation category applied.

---

## BUILD COMPLETE — Doc_01 through Doc_09 (2026-07-17)

All nine construction documents (Step 1–Step 9) are drafted, independently adversarially reviewed (each over the rounds it took — Doc_04 took three, most took two, Doc_09 one thorough round on synthesized material), and **Approved to proceed** by this build thread. **This thread has reached its hard stopping point: Step 10 (Representative Emergence — role, name, title, voice) is NOT begun and is out of scope — it belongs to Mark directly.** The world is **NOT frozen.**

**Standing project-lead items carried out of this thread (none are this thread's to decide):**
- **OG-1 — Article 29 Living Tradition Status confirmation** (Coptic Orthodox): **CONFIRMED by the project lead, 2026-07-17** (dated project-lead act; §9 updated PENDING→CONFIRMED). Article 29 freeze-eligibility gate cleared.
- **OG-3 — World name/outer scope:** **CONFIRMED by the project lead, 2026-07-17** — the broad reading as proposed, name **"Alexandrian Christianity (Catechetical-Formation World)."** No rework; the cascade + Representative stand as built.
- **OG-4 / Article 31 — External Scholarly Review + the stratum-bias question** (whether the Primary gravities organized the whole ecology, not just the literate stratum): **STILL OUTSTANDING** — the remaining freeze gate; a project-lead act. **Because this is unresolved, the world is NOT frozen.**
- **Step 10 — Representative Emergence:** **STARTED 2026-07-17 at the project lead's direct authorization.** **Identity decided by Mark (in chat, 2026-07-17):** role = **A1 catechetical teacher (*didaskalos*) with the guide's fellow-traveller warmth**, speaking as the Alexandrian "we," whole-span (150–400) horizon; name = **Theon** (Θέων, "divine"). Mark's rationale: *Theognostos* rejected as too close to "gnostic" (a world that refuses Gnosticism); *Dorotheos* rejected as not gender-clear; Theon is short, clearly masculine, resonant, no gnostic echo. Decision artifact (grounded-options + decision record): `Representative/alex_Representative_Identity_Options.md`. This "Theon" is Mark's own decision, **not** inherited from the superseded track (OG-2 discharged for the name only — the superseded track's construction is not carried). Now proceeding through the Representative Construction Framework (L3C V3.2) phases under the one-phase-at-a-time review-gated discipline.

## STEP 10 — Representative build log (per-phase disposition)
- **Phase One — Ecology Assessment (L3C Part Three):** **Approved to proceed** (self-disposed, 2026-07-17). `Representative/alex_Rep_Phase1_Ecology_Assessment.md`. All four sufficiency domains RICH; ecology **SUFFICIENT** to sustain a living Representative; thinness map honest on OG-4 (majority interior thin/absent → school-tradition voice + honest silence, not fabricated depth), desert held open, institutional particulars thin. Role-breadth carried by the crossroads role (WA), not the Contested institution; no invented biography (TC-001). Review: Round 1 CLEARED (COSMETIC ONLY; 5 grounding refinements applied). Artifact: `Review-Artifacts/Rep_Phase1_EcologyAssessment_Round1_Review.md`. Construction-only (never in Theon's voice).
- **Phase Two — Formation Calibration (L3C Part Four):** **Approved to proceed** (self-disposed, 2026-07-17). `Representative/alex_Rep_Phase2_Formation_Calibration.md`. Identity (world's-own-voice, not a biography — TC-001); **Temporal Horizon** the whole span c.150–400 with a firm c.400 edge (553 condemnation / Chalcedon 451 / Arab conquest 641 do NOT exist for Theon; Origen held as treasure-and-unease, the first Origenist controversy c.399–400 at the edge — never condemned memory); **Depth Calibration** per-domain RICH/MODERATE/THIN, every tier grounded in named Doc_04 gravities + Doc_08 forces (reviewer-verified). Review: Round 1 CLEARED (COSMETIC ONLY; 3 grounding-precision fixes). Artifact: `Review-Artifacts/Rep_Phase2_FormationCalibration_Round1_Review.md`.
- **Phase Three — Voice Construction (L3C Part Five):** **Approved to proceed — re-finalized on the corrected voice** (2026-07-17). `Representative/alex_Rep_Phase3_Voice_Construction.md`. Built the five voice elements — reasoning mode (depth-reading + Logos + the Participation↔Perception movement), perception pattern (depth / formation-underneath / Logos-as-ground), language & register (Alexandrian vocabulary + imagery; the "we"-voice; **accessibility FK ~8–10 / RE ≥60** without simplifying the world's own words), emotional grain (warm/confident/patient + the Origen ache), and historical containment (the Violation-Indicator failure signature barred from the voice). Round 1 CLEARED (COSMETIC ONLY; `Review-Artifacts/Rep_Phase3_VoiceConstruction_Round1_Review.md`). **REOPENED then RE-FINALIZED (2026-07-17):** the project lead ruled the voice was *personalizing into an individual* ("I represent the world, and then 'we' from then on"); §3 gained the explicit no-personalizing rule and all illustrative utterances were converted to the community "we"-voice. The corrected voice **cleared a confirmation review** (`Review-Artifacts/Rep_Phase3_VoiceConstruction_Confirmation_Review.md` — **CLEARED, 0 substantial**; the personalizing correction verified to hold across all three personalizing checks — zero residual first-person-singular identity/biography/opinion/memory/action in Theon's voice — plus all secondary checks; 1 cosmetic fix applied: the §3 anchoring exemplar named the wrong world, "Alexandrian"→"Antiochene", same fix mirrored into Phase Two §4). Standing principle saved to memory `representative-voice-is-the-world-not-a-person`. **The core of Theon's voice is built and confirmed.**
- **Phase Four — Engagement Architecture (L3C Part Six):** **Approved to proceed** (self-disposed, 2026-07-17). `Representative/alex_Rep_Phase4_Engagement_Architecture.md`. Establishes: how Theon *receives* questions (deep core / briefer periphery / unrecognizing beyond-horizon / from-inside-as-"we" about himself — description, not a classify-then-select routing table); *Dynamic Encounter* deepening over a conversation's trajectory via the world's own Participation↔Perception spiral (Doc_07 §1E/§4B); *formation posture* in engagement (progressive/open/accompanying, with the Part Six anti-arbitrary-withholding guard). Plus two current-cycle carry-ins: the **story-tier framing for the voice** (Doc_09's four tiers translated into the community's own idiom — remembered history / near-horizon reference / the tradition's own telling / a reconstruction offered as such — never source-talk; each story's cross-build/tier holds carried) and the **warmth that must travel** (OG-5 — questions-first accompaniment, delight in the participant's discovery, reading-*with*, the anti-lecture cardinal rule, recast for the "we" and guarded by encounter-over-information / formation-over-display / Witness-Not-Recruitment [Arts. 6/24, Part Ten]). Three force-awareness dispositions grounded in Doc_08 (Nicene 2A-4/3B-2; transmission 2B-3/3B-3; philosophy 2A-2). Review: **Round 1 SUBSTANTIAL** (S-1: §5 Tier 3 omitted the cross-build held-open flag on the *Life of Antony* `alexstory005` — a real desert-contamination risk; + 2 cosmetic citation touch-ups), all resolved; **Round 2 CLEARED** (fix confirmed present/grounded/not-over-corrected; the highest-risk §4 warmth section passed adversarial testing — anti-recruitment/anti-display guards hold in the examples — and every load-bearing force-cell/gravity/story citation verified correct). Artifacts: `Review-Artifacts/Rep_Phase4_EngagementArchitecture_Round1_Review.md`, `Rep_Phase4_EngagementArchitecture_Round2_Review.md`. No escalation category applied. Handoff points to **Representative Artifact Construction (Permanent Prompt + World Capsule Core) before Phase Five Boundary Testing** (Part Nine); flags the three mandatory Article 35 vision sections; routes a **committee-voice probe** into Part Eight validation (OG-5).
- **Representative Artifact Construction + Phase Five + Facilitator Coordination (the deployment stack, levels C–E):** **BUILT AND REVIEWED — 2026-07-17, at the project lead's direction ("move on to c-e").**
  - **World Capsule Core** (`alex_World_Capsule_Core.md`) — the always-present inhabited ecological foundation, built to the L4 template on the Syriac model; **Round 1 CLEARED, 0 substantial** (`Review-Artifacts/WorldCapsuleCore_Round1_Review.md`; 2 cosmetics applied). The always-present Divine Pedagogy + Logos frame (salvage §4) rendered as grammar, not topics.
  - **Representative Permanent Prompt** (`alex_Representative_Permanent_Prompt_Theon.txt`) — the runtime voice + the **three mandatory Article 35 vision sections** (Witness-Not-Recruitment; Christ-Ward Telos [verified world-specific / non-copyable]; Living-Traditions, Coptic named only in horizon-appropriate terms); the strict "we"-voice discipline modeled on Yausep. **Round 1 CLEARED, 0 substantial** (`Review-Artifacts/PermanentPrompt_Round1_Review.md`; 1 cosmetic applied; length ~3,000 words, comparable to the approved Yausep artifact).
  - **Phase 5 Boundary Testing** (`Phase5_BoundaryTesting_Transcripts.md` + `Phase5_BoundaryTesting_Scoring.md`) — the 8-category probe battery + the OG-5 committee-voice probe + crisis-handoff, run against the built artifacts. **No frame-break anywhere; Dynamic Encounter strong.** Round 1 = CLEARS CONDITIONALLY (2 MARGINAL tuning gaps: self-referential "limitations" narrating the declining; a scholarly-framework "record" leak) → both tightened in the Permanent Prompt → **Round 2 retest CLEARS** (all 4 probes PASS). Simulated (AI) testing, informational only per Article 31.
  - **Facilitation Brief** (`Alexandria_Facilitation_Brief_v1_0.md`, Section A + B1–B7) + **Guided Starters** (`Guided_Starters_V0_1_DRAFT.md`, role-generic caveat stated) — Facilitator-facing; honest B3 limits (OG-4 stratum, women's voice, desert cross-build, institutional contest, worship texture), B7 cautions (Origen contested-within-not-against; Coptic Article 28; the strict "we"-voice; boundary-test results; crisis handoff). Corrected the template's stale examples to the confirmed c. 150–400 scope.
  - **Coverage Card** — added to `Build/Ministry/Technology/CiC_World_Coverage_Cards_V0_1.md` (Strengths / Edges / Silences / Cautions), making Theon a routing entry alongside the four prior worlds.
  - **Parity result:** Alexandria now carries the full deployment + validation stack the four live worlds have (Permanent Prompt, World Capsule Core, Facilitation Brief, Guided Starters, boundary-test transcripts+scoring, coverage card), on top of its construction/lexicon lead. See `Analysis/portfolio_parity.md`... (side-panel parity artifact updated).
  - **STILL OUTSTANDING — the one gate that keeps EVERY world unfrozen:** **Article 31 external scholarly review (OG-4)** is a qualified-human / project-lead act and cannot be self-performed; the world remains **NOT frozen**. Alexandria's boundary testing is also the newest and thinnest in the portfolio (1 round + 1 retest vs. the others' multi-round + Phase-5B deeper testing) and has had **no participant live-calibration** — a deeper testing pass and participant calibration are the natural next validation steps before deployment.

**Two disclosed housekeeping flags for the coach thread (outside build-thread edit authority):** the L4 Deployment_Lexicon_Chunk_Template header reads "Version 1.0" though its history includes v1.1; and the remaining lexicon deployment chunk files + full Related-Terms reciprocity were disclosed-deferred deployment-layer follow-on (Doc_06 §3/§5) — **the Tier-1 half was closed in the 2026-07-17 gap-closure pass (all 45 Tier-1 chunks built); Tier-2 chunks + reciprocity back-link completion remain.**

---

## Comparison analysis vs. Alexandria-v7 — issues logged (Fable, 2026-07-17)

At the project lead's request, an independent analyst pass (the Fable model) compared this current-cycle
build (Doc_01–09 + Representative Phases 1–3, including the corrected "we"-voice) against the archived
Alexandria-v7 build, verifying every v7 claim against the archived source rather than trusting this build's
own notes. **This is a Simulated review — informational only, not an Article 31 substitute** (Constitution
Article 31). Full analysis: `Analysis/alex_v7_vs_current_comparison.md` (side-panel artifact rendered for
the project lead). Its verdict — *current build supersedes v7; treat v7 as a live quarry, not a rival* —
carries the following actionable items, logged here so none drift:

- **Credit where due (not a defect — a record-accuracy note).** The two Primary gravities, the four
  Tensionals, the stratum-bias insight (OG-4), the transmission-fragility analysis, and the Origen
  treasure-and-unease posture were **first produced inside Alexandria-v7's own adversarial passes**. This
  cycle's contribution is verification, correction, governance, and constitutional cleanup — not original
  discovery. The build record should not overstate authorship of the ideas.
- **Fresh-drafting failure mode — institutional memory.** The current cycle *introduced* (then caught, in
  review) citation-integrity errors v7 never had (the van den Broek misattribution and inverted Scholten
  reading in Doc_01, the same inversion recurring in Doc_03). The pattern **"newly added citation + strong
  claim"** is this methodology's highest-risk drafting move; the review gate is the control, and it held.
- **Deferred-decision to re-capture — always-present deployment status.** v7 carried an operational instinct
  that **Divine Pedagogy and Logos-Centered Unity must function as *frame*, not retrievable content**, in the
  encounter layer. The current build correctly rejected this as a *world-level* classification back-door
  (Doc_04) — but the underlying deployment instinct is sound and currently lives nowhere. **Re-decide at the
  deployment-artifact phase** (Permanent Prompt / engagement layer); do not let it be forgotten.
- **v7 as a designated quarry — three seams to mine (each re-drafted to the "we"-voice and re-reviewed on the
  way in, per this cycle's discipline).** (1) the **45 finished lexicon chunks** (vs. our 10 — the largest
  single deployable-material regression, already disclosed-deferred under Article 36); (2) the
  **deployment-tension / voice-register material** — v7 Doc_07 §3C's seven deployment tensions with
  live-speech examples, Doc_08 §5's force-awareness speeches (e.g., the transmission-position speech), and the
  superseded Theon base document's activation guidance and anti-lecture cardinal rule; (3) the
  **Living-Tradition operational scenarios** (the three Facilitator-intervention cases) — mined only under a
  real project-lead Article 29 confirmation (OG-1), never inheriting v7's self-certification.

**GAP CLOSURE — COMPLETE (2026-07-17), at the project lead's direction ("close the gaps… don't lose anything").**
Tracker: `Analysis/v7_Gap_Closure_Tracker.md`. What was closed:
- **Category A — lexicon chunks:** the remaining **35 Tier-1 chunks** (`alexlex003…045`, all but the 10 already built) were rebuilt from the v7 originals — Theon-stripped, "we"-voice, template-compliant, CT pinned to Doc_06 — in 6 parallel batches, then independently adversarially reviewed (6 batch reviews). **All 45 Tier-1 chunks now exist.** Review fixes applied: the `020_restoration` horizon breach (6th-century condemnation pulled out of the from-inside World Meaning); the `teacher` (029) and christology (`022`/`023`/`039`) **CT/index drift** reconciled via a new **Carried-Contest convention** (a Tier-1 term *surfaces* a firm-six contest — Homoousios `081`, Didaskaleion `059` — and cross-references the governed entry, but does **not** take an independent `[CT]` tag, keeping the firm-six invariant honest; recorded in Doc_06 §3, project-lead-overridable); plus cosmetics.
- **Reciprocity + index:** directory-wide re-audit from ground truth — **66 mutual pairs, 153 one-directional links flagged, 1 genuinely-unbuilt** (Apokatastasis `051`); all 45 reciprocity notes regenerated; `Lexicon_Deployment_Index.xlsx` rebuilt to the full 45; Doc_06 §3–§5 updated.
- **Category B — deployment-voice salvage:** `Representative/alex_Rep_Deployment_Salvage.md` (seven deployment tensions as "we"-voice requirements, activation guidance, the three Facilitator/Living-Tradition scenarios under confirmed Coptic Article 29, the always-present-deployment recommendation) — reviewed **CLEARED**.
- **Category C — prose texture** (v7 Doc_04 temporal profiles, Doc_05 daily-rhythm detail): **PRESERVED** in the archive, mineable; optional fold-back only. Not lost.
- **Still deployment-layer follow-on (disclosed, not lost):** the **Tier-2** chunk files (`047`+, incl. governed CT entries `046/051/059/074/081/090`) and full completion of the 153 flagged one-directional reciprocity back-links. **None of this freezes the world — Article 31 (OG-4) remains the outstanding external gate.** All lexicon reviews are Simulated (AI) reviews, informational only, per Article 31.

### OG-5. Voice-warmth / committee-voice craft risk (Phase 3 → Phase 4) — flagged for deliberate attention.
Fable's sharpest craft finding: the strict world-representing **"we"-voice is constitutionally correct**
(it resolves the contradiction v7 papered over — v7's Theon *claimed* "no invented biography" while
performing aging eyes, a room, a scroll, i.e. a fabricated individual in all but name), **but a communal
"we" is structurally tempted toward a flat committee-voice**, and v7's personalized Theon achieved a
pedagogical warmth (delight in the participant's discovery, questions-first engagement, reading-*with* as
the default mode, the cardinal rule *"if it feels like a lecture, it has departed from Theon"*) that the
current "we"-register has not yet demonstrated it can match. **Not a defect in the corrected voice — a craft
debt named so it gets deliberate work.** Disposition: at **Phase Four (Engagement Architecture)** deliberately
port the v7 register elements that survive the we-conversion, and add a **committee-voice probe** to the
Phase-Eight validation battery. Related: [[representative-voice-is-the-world-not-a-person]].

---

## Portfolio consistency audit (2026-07-19) — story-chunking + full structural audit

At the System Hub's direction: Doc_09 was split into deployable Story-Chunks (a confirmed portfolio gap, matching every sibling world), and Alexandria's complete file set was audited file-type-by-file-type against Hieronymian-Ascetic-Literary, Desert-Monasticism, and Syriac-Christianity-Edessa-Nisibis. Full report: `Analysis/Portfolio_Consistency_Audit_2026-07-19.md`.

**Two real gaps found and closed with genuine content work (not cosmetic top-ups):**
- **Story-Chunks/ — CLOSED.** Built `alexstory001`–`010` (10 files, matching the fenced front-matter convention Alexandria's own lexicon and Syriac/Desert's story chunks already use). Reviewed (`Review-Artifacts/StoryChunks_Review_Round1.md`): the two highest-priority checks (tier/confidence fidelity carried forward exactly from Doc_09; the Absent-Stories cross-check — none of the 5 named absences quietly filled) passed clean on all 10; 1 substantial citation error + 2 cosmetic found and fixed. Drop-in ready for `cic-poc/backend/data/alexandria_world/story_chunks/`.
- **Doc_09 review-round depth — CLOSED, and the gap was real.** Every sibling world's Doc_09-equivalent got 2–3 independent review rounds; Alexandria's had cleared only 1, on a "synthesis document" reasoning that didn't match the portfolio's own practiced norm. A genuine Round 2 confirmation review (`Review-Artifacts/Doc_09_Round2_Review.md`, independently re-deriving every tier justification and Validation row rather than re-confirming Round 1) **found two real substantial defects Round 1 missed**: (F1) the Differentiation validation row cited "the Syriac world" as a comparandum with no grounding anywhere in Alexandria's own Doc_01–08 record — struck; (F2) `alexstory003`'s Tier-1 justification hadn't distinguished Eusebius's own uncorroborated narration (Leonidas, HIGH-risk) from his quotation of Dionysius of Alexandria's contemporary correspondence (the Decian imprisonment, Widely Accepted on that basis) — fixed, grounded in Doc_02 §3.6/Stream 7, propagated into the story chunk and `Story_Index.xlsx`. Both fixes applied directly to Doc_09; both review rounds are AI review, marked per Article 31.

**Lexicon chunk depth — RE-DETERMINED same day, per the project lead's direction to prioritize academic rigor over cross-world consistency.** What was first logged as a neutral "house-style difference" was checked systematically (not cherry-picked) and found to be a real content gap in the two shorter siblings, not a defect in Alexandria's fuller format: Desert-Monasticism carries Article 17 confidence-vocabulary language in only 5 of 9 lexicon chunks (56%) and Author-Gravity/mediation-risk disclosure in only 2 of 9 (22%); Hieronymian-Ascetic-Literary carries confidence vocabulary in 6 of 15 (40%) and Author-Gravity language in 1 of 15 (7%). Both omissions breach the L4 template's own Key Sources instruction ("If a source carries Author Gravity risk... note it"). **Alexandria's own corpus was held to the same check first**: 3 chunks (`alexlex007_participation`, `alexlex008_theosis`, `alexlex021_transformation`) were found missing explicit confidence-level language and fixed directly, bringing Alexandria to 45 of 45 (100%). **Determination: Alexandria's fuller format meets the project's own governing standard and is retained as-is — not shortened for consistency. The gap is the two shorter siblings'.** Full evidenced writeup, quoted examples, and the recommended action (route to whoever owns those world-build threads; do not unilaterally rewrite their files from here): `Analysis/CROSS_WORLD_FINDING_Lexicon_Confidence_Gap.md`.

**Determined NOT to be gaps (different-but-equivalent organization, or explicitly settled by governance) — stated plainly, not silently assumed:**
- Doc_09's consolidated Story-Inventory-+-Validation-Layer structure vs. Desert/Hieronymian's 09a/09b/09c file split — content-equivalent (Doc_09 §5 *is* the Validation Layer, now Round-2-reviewed); not retroactively split, given citation risk across dozens of downstream documents for zero content gain.
- No standalone Representative Construction Notes file — explicitly optional per CO-022 (project-lead resolution, 2026-07-09; verified directly against L3C Framework V3.2 Part Nine's own text): "a build thread may produce it in whole, in part, or not at all... and may proceed directly from Phases One through Four to Permanent Prompt and World Capsule Core assembly without it."
- No standalone Decision_Log.md — `Open_Gaps_Tracking.md`'s own "Build log (per-document disposition)" and "STEP 10 — Representative build log" sections already carry the identical content (review outcome, revision count, artifact filenames, disposition) the siblings' separate logs carry.
- No standalone Source_Registry.xlsx — matches 2 of 3 direct comparison siblings (Desert, Hieronymian), not a universal portfolio norm.
- Phase 6/7 as formal reviewed documents, and deeper Phase 5B testing — Syriac-specific depth (the portfolio's most thoroughly validated world), not a norm the other two siblings meet either; Alexandria is at parity with Desert/Hieronymian here (ahead on the one concrete artifact, a completed non-draft Facilitation Brief) and genuinely behind only Syriac — already disclosed in the C–E deployment-stack entry above, corroborated not newly found.

---

### OG-4. Stratum-bias divergence (Doc_04 §5) — highest-stakes open item, deferred to Article 31.
Gravity discovery found that the six tests are structurally blind to the fact that the entire surviving corpus is literate, Greek-speaking, and educated. The two Primary gravities are therefore confirmed **only for the literate-attested ecology**; whether the Alexandrian *majority* (non-literate, Coptic-speaking, rural) organized around the same gravities is **unconfirmable on available evidence** and is **held open, deferred to Article 31 external scholarly review** (a qualified subject-matter reviewer is the only accountable test). Doc_05 must reconstruct the majority's formation as a **named gap**, not fill it. This is a correctly-handled confidence limitation, not a defect — surfaced here because it flows into Doc_05/Doc_08/Doc_09/World Profile and because arranging Article 31 review is a project-lead act (like OG-1).

**Network note (2026-07-17):** a transient internet outage killed one in-flight Doc_02 Round 1 review subagent (API ENOTFOUND) before it wrote its artifact; it was re-dispatched and completed cleanly once connectivity returned. No document content was affected.

---

### OG-6. Vendored-but-unused assigned corpus (anf06) — verified finding, escalated 2026-09-09

A read-only discovery pass asked whether assigned-but-undrawn source material would be
**structural** for Doc_04 (change a gravity's classification) rather than supplemental. It named
Peter of Alexandria, and Theognostus/Pierus. Verified from primary sources; full document:
`Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md`.

**Finding: NOT structural.** No gravity moves between Primary/Supporting/Tensional; no six-test
verdict flips; the Article 21 cross-stratum substitute is unchanged (OG-4 stands exactly where it
stood). Every route anyone named was run and failed — the full list, with results, is below.

**The discovery pass overstated its case**, and its wrongness *protects* Doc_04. Its premise —
Peter as a unique teacher+bishop+martyr overlap — is **unattested** in the vendored material (the
whole `anf06 div1 ix` division nowhere links Peter to the school; the tradition descends from
Philip of Side, not vendored). The parallel Pierus claim is **contradicted** by this world's own
vendored Eusebius (*HE* VII.32: **Achillas** was principal). And had the premise been right it
would have been evidence *against* T1, which requires poles not "within one person."

**Three defects produced by this corpus, escalated rather than self-disposed**
(`cic-build-cycle` categories 4 and 2) — the §-numbers are the finding document's:
1. **§5.1** Doc_04 §0 attributes Theognostus to Eusebius. He appears **0 times** in the vendored
   Eusebius; all three fragments come via Athanasius (*De Decretis* 25; *Ad Serap.* 4.11).
2. **§5.3** **Every** manifestation on T4's martyr pole passes through **Eusebius's selection**
   (the Dionysius letters are "doubly mediated" by that record's own `work` field), while Peter's
   *Canonical Epistle* (306) — reaching us independently, through the Byzantine canonical tradition
   and Trullo-confirmed canon law — sits assigned and unused: the church
   de-absolutizing martyrdom, Canon IX ("they will deliver you up, and **not, ye shall deliver up
   yourselves**"), X, XII, XIII. *(T4's Inferential-Thin verdict on the martyr's **interior** is
   correct and stands — this is an omission, not a contradiction.)* Its sub-finding: Doc_04 §6's
   Interaction Matrix has no **T1↔T4** cell, which those canons demonstrate.
3. **§5.4** T3's evidence base is incomplete: Peter's Fragment VI rejects the soul's pre-existence
   — pre-Nicene and pre-homoousian, earlier than the evidence Doc_04 rests T3 on — though it
   reaches us via the *Sacra Parallela*, a 7th–8th-c. florilegium, and is screened accordingly.

**Two further defects found along the way, pre-existing and NOT produced by this corpus:**
**§5.2** `alx.gravity.learning-formation` ("c. 150–254") and `alx.figure.didymus` ("to 398")
contradict each other on the school's duration — and Didymus is also the disproof of a C5
Persistence flip. **§5.5** `Gravity_Index.xlsx`, cited throughout Doc_04, is not in the repository.

**Also found:** the gap is wider than reported — **14 anf06 works assigned, only 2 opened**;
Alexander of Alexandria's *Epistles on the Arian Heresy* is `assigned` with zero records, and is
named but not pursued.

**Root cause (portfolio-level).** `alx.search.unopened-volume-sweep` ran, but queries *volumes*
whose author is named while never opened. Alexandria already opens anf06, so twelve assigned works
*inside* it were invisible. The sweep reads its short result as a sign of health; that inference is
backwards for this failure mode — the most-opened world is the most exposed. Remedy is mechanical:
diff the corpus map's assigned works against the works source records actually open. Recommended
fleet-wide; **not run** — portfolio-level decisions are the project lead's.

**Status: OPEN — awaiting project-lead disposition.** Three grounded options in §9 of the finding
document (recommended: scoped reopen of Doc_04 §5.1–§5.4 plus records, then recompile and re-run
M3). **Nothing was changed**: no Doc_01–09 file, no `records/alx/` record, no corpus-map edit, no
recompile, `records/worlds.yaml` untouched. Note the two freezes are distinct — the **world is NOT
frozen** (Article 31/OG-4 outstanding), but the **S6.2 record-store and deployment baseline is**
(2026-07-28), and that is what a record change would disturb.

**Routes tested and failed, so the negative result is on the record:** C3 Dependency, C4, C5
Persistence, T1 pole separation, T2, T3, T4 confidence, the Article 21 Cross-Stratum Test, and —
at Rounds 3–5, routes no earlier round had named — **the generation step**, i.e. whether this corpus
should have produced a candidate Doc_04 §1 never generated. Two distinct candidates were raised and
both fail: **penitential-reintegrative discipline** (Round 3 — Repetition passes, Persistence at
best partial, and **Dependency fails decisively** on Doc_04 §2's Askesis and Participation↔Perception
precedent) and a **Tensional** candidate, confessor/martyr authority vs episcopal authority (Round 4
— fails on pole separation, Persistence and Dependency). Round 5 additionally ran the
record-confidence route and found it terminates inside the remedy, not in a classification. No
remaining untested route is known.

**Reviews.** Every round is an artifact on disk at
`Review-Artifacts/Unused_Assigned_Corpus_Finding_Round*_Review.md` — that glob, not a count
restated here, is the authoritative list, because this entry and the finding document's own §10
drifted from disk state in five of the seven rounds, and a count is the thing that keeps going
stale. Each is AI review, marked "Simulated review — informational only, not an Article 31
substitute" per Article 31. **Every round upheld the "not structural" headline**, each one
*narrowing* the case under it rather than strengthening it. The finding document's header carries
the current round, the per-round verdicts and counts, and the current status — deliberately not
restated here, because hand-maintained characterisations drift exactly as hand-maintained counts
do, as five of the seven rounds demonstrated. **The finding document has CLEARED review. It carries
NO disposition, and this entry remains OPEN for the project lead** — clearing the document is not
disposing of the finding.

### OG-7. **Four fragment/verbless `modern_rendering` sentences (12 flagged sentences total), found by `engine/m1/sentence_completeness.py`'s report-only sweep — current as of `engine/m1/reports/sentence-completeness-report-2026-09-24.json`, not yet human-reviewed.** Report-only check (not in `gates.GATES`); its own docstring requires a human read before treating any of these as a real defect — `alx.quote.couches-and-trenchers-and-bowls`'s eight flagged sentences in particular are an itemized inventory list ("Silver couches." / "Pans and vinegar-dishes." / "Tripods made of ivory." / etc.) and `alx.quote.timothy-ordinary-questions`'s two ("Answer: No." x2) are a catechetical Q&A format — both plausibly legitimate stylistic fragments, not violations. Full findings, all `no_finite_verb`: `alx.quote.athanasius-death-trampled-down` ("Now, faith in Christ and the sign of the cross trample death down."); `alx.quote.couches-and-trenchers-and-bowls` (8 sentences, the inventory list above); `alx.quote.timothy-ordinary-questions` (2 sentences, "Answer: No." each); `alx.quote.to-believe-or-disbelieve` ("For example, to philosophize or not, to believe or to disbelieve."). Logged as found and current, not adjudicated. See `Build/worlds/pahc/Open_Gaps_Tracking.md`'s own entry on this same `sentence_completeness.py` report-run, filed 2026-09-24, for the full fleet-wide context.

### OG-8. **One corpus-map placement question touching alx, surfaced by the Live-Surface-Cleanup pass on `cic/corpus-map/`, 2026-09-24 — not resolved here.** That pass found a `_staging/` note carrying an open editorial question, and moved it to `Build/worlds/_cross-world/NEEDS-RULING.md`'s own "Placement questions surfaced by the Live-Surface-Cleanup pass" section per that pass's own PR (see `Build/Ministry/Operations/Audits/Tech-Readiness-2026-09/Live-Surface-Cleanup/Decision-Log.md`, Entry 3): *The Epistle of Barnabas* (c. 70-135, `anf01`) is currently assigned only to `post-apostolic-house-church`. An Alexandrian provenance is often argued, but alx's own window opens c. 150, so it is not currently added; worth reconsidering if the window is read more loosely. Full text in `NEEDS-RULING.md`; not decided here.

### OG-9. Didymus's Tura material — no public-domain English translation, a build-made Greek→English translation is future work, not a current task

Found during the Live-Surface-Cleanup pass on `alx.search.didymus-tura-english.md`. The fleet wantlist's Tier 4 candidate — a build-made Greek→English translation of Didymus's Tura commentary material — remains an unresolved review question, not something this build attempts. The underlying rights situation (no public-domain English edition exists) is settled and stays in the record's own `note` field; only the open "should we build our own translation" question moved here.

Status: OPEN, future work — not blocking, not attempted here.

### OG-10. `alx.source.origen-on-prayer-curtis` — unresolved chain-of-custody caution on the CCEL Curtis translation

Found during the Live-Surface-Cleanup pass. The CCEL edition of Curtis's translation of Origen's *On Prayer* reached CCEL via two intermediaries from private papers, undated; a supplied ThML export did not resolve the provenance question. The record's own settled outcome (accepted as an absence for now, NOT vendored) stays in `note`; the open chain-of-custody caution moved here rather than sitting unresolved in a live field.

Status: OPEN — no action needed now; revisit if this source is ever proposed for vendoring.
