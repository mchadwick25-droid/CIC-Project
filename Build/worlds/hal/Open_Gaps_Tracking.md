# Open Gaps — Hieronymian Ascetic-Literary Christianity ("The Bethlehem Circle")

Running, dated ledger for the `hal` world build, matching the discipline of
`Build/worlds/alx/Open_Gaps_Tracking.md`: dated entries, disclosed deferrals, honest status,
project-lead-anchored where confirmation is a project-lead act. This file is the durable
record; no real decision, review outcome, or open question lives only in a conversation
thread's own history.

**A note on how this file was produced (2026-09-20):** it was assembled by reading `hal`'s
own build files directly — `hal_Decision_Log.md`, the three `build/` files, the ~24
`Doc_0N_Review_RoundN.md` artifacts, the Representative construction and testing files,
the Pass-2 freeze declaration (in `Archive/Technology-Pass2-2026-08/`), the current
`records/hal/` and `records/worlds/hal.yaml`, and the two cross-world audit documents that
named this world by name. Every entry below traces to one of those files. Where the
underlying history genuinely could not be reconstructed from what's on disk, that is
stated plainly rather than filled in.

---

## World has been built THREE times, under three different architectures — read this first

Unlike a single-pass build, `hal`'s history on disk shows three distinct construction
efforts, each superseding parts of the last. Keeping them straight matters for trusting
any one status claim below:

1. **Generation 1 — L3B Construction Framework build (2026-07-12–13).** The classic
   Doc_01–Doc_09c sequence plus Representative Construction (Albina) and live adversarial
   testing, documented in `hal_Decision_Log.md` and the `hal_Doc_0N_Review_RoundN.md`
   files. Produced the prose documents still on disk (`hal_Doc_01…10`, `hal_World_Profile.md`,
   `hal_Ecology_Assessment.md`, the `Lexicon-Chunks/` and `Story-Chunks/` folders, the
   Permanent Prompt and World Capsule Core, the Phase 5 live-test transcripts). Explicitly
   never reached Frozen under this generation's own vocabulary — Article 31 and full
   Encounter Testing were outstanding at its own stopping point.
2. **Generation 2 — Pass-2 "WRS" record-store rebuild, FROZEN 2026-07-31.** A fleet-wide
   migration effort rebuilt `hal` as a validated record store (97 records) with its own
   gate suite, blind-graded battery, and triple-partner TRR. This generation reached an
   actual, project-lead-confirmed freeze — see OG-1 below. Its artifacts now live under
   `Archive/Technology-Pass2-2026-08/Pass2/` (archived, not deleted).
3. **Generation 3 — "New-architecture" record rebuild, 2026-08-21, superseding Generation 2
   in turn.** `Build/worlds/hal/build/BUILD-LOG.md` documents a **fresh** 139-record build on a
   new branch (`world/hal`), explicitly re-deriving from Generation 1's cleared prose docs
   rather than trusting Generation 2's frozen records, and explicitly **not carrying
   forward the Representative identity decision** ("`representative: null` in the
   registry; the prior framework's preliminary decision was *not* carried forward").
   `records/hal/` on the current main branch is this generation's direct descendant, since
   enriched further (now 173 records — see the per-type count in the Representative /
   registry section below) and repackaged repeatedly through September 2026
   (`packages/hal/2026-08-30…2026-09-20`).

**Net effect:** the world *was* frozen once (Generation 2, 2026-07-31), then rebuilt from
scratch under a new architecture that reset the Representative question to "null," then
had the Representative identity reconfirmed via the registry (see OG-2). Whether
Generation 2's freeze — including its Article 29 confirmation and Article 31 "deferred to
year two" disposition — still governs the current Generation-3-descended record set, or
whether that freeze lapsed when the architecture was rebuilt underneath it, **is not
stated anywhere on disk that this pass could find.** Flagged as OG-1.

---

## Build log — Generation 1 (L3B Construction Framework, 2026-07-12–13)

*(Source: `hal_Decision_Log.md`, cross-checked against the individual `Review_RoundN.md`
files. Format matches Alexandria's model: document · review outcome · rounds · artifacts ·
disposition.)*

- **Doc_01 — World Identification, Boundaries, Orientation:** **Approved to proceed**
  (2026-07-12). Review: Round 1 substantial (7 substantial/9 minor/1 cosmetic —
  `hal_Doc_01_Review_Round1.md`); Round 2 found the revision itself introduced 1 new
  substantial finding, most notably an erroneous claim that Ep. 108 places Arsenius
  physically at Nitria in 385–386, chronologically impossible (`hal_Doc_01_Review_Round2.md`);
  Round 3 confirmed genuine resolution, cosmetic-only residue (`hal_Doc_01_Review_Round3.md`).
  Two dedicated fact-verification passes were run outside the review rounds before
  accepting any "tooling artifact" flag. Scope settled: 382–420 CE, Bethlehem AND Rome
  (bipolar), strand-singular (reopenable only on evidence of a difference in kind, not
  degree).
- **Doc_02 — Source Ecology:** **Approved to proceed** (2026-07-12). Review: Round 1
  substantial (5 substantial — Paula/Fabiola confidence overclaims, an internal
  contradiction on Fabiola's hospital sourcing, an Ep. 108 Nitria/Bethlehem misattribution,
  an unverified Cain citation — `hal_Doc_02_Review_Round1.md`); Round 2 confirmed all fixed,
  cosmetic residue only (`hal_Doc_02_Review_Round2.md`).
- **Doc_03 — Lexicon Candidate List:** **Approved to proceed** (2026-07-12). 18 initial
  candidates. Review: Round 1 substantial (a self-contradicting tier for *Grammaticus*, a
  category-column error confusing evidentiary-thinness with Author Gravity risk, a
  dropped-term count error, a miscategorized pilgrimage entry — `hal_Doc_03_Review_Round1.md`);
  Round 2 cosmetic only (`hal_Doc_03_Review_Round2.md`).
- **Doc_03 Addendum (6 further terms, pre-Doc_06):** **Approved to proceed** (2026-07-12).
  **Significant finding:** review caught a fabricated primary-source quotation — an
  invented Latin gloss falsely attributed to Ep. 77.6 — confirmed fabricated and corrected
  against Perseus's critical Latin text across two rounds (`hal_Doc_03_Addendum_Review_Round1.md`,
  `_Round2.md`). Flagged as a standing caution: the fabricated reading appears to circulate
  in AI-generated search-summary content online.
- **Doc_04 — Gravity Discovery:** **Approved to proceed** (2026-07-12). Six candidates
  tested; G1 *Hebraica veritas*, G2 ascetic self-impoverishment, G3 patronage confirmed
  Primary; G4 letter-writing, G6 controversy Supporting; G5 (Marcella) Tensional. Directly
  resolved Doc_01's Open Issue #7 (Marcella's authority texture vs. Jerome's) as **not
  reopened** — same underlying currency, different position. Review: Round 1 substantial,
  its highest-severity finding being that the Open Issue #7 resolution bundled a valid
  argument with a non-sequitur and an unexamined reimport of prior reasoning
  (`hal_Doc_04_Review_Round1.md`); Round 2 independently re-traced the reasoning against
  Doc_01 §4 and Ep. 127's actual content and confirmed it genuinely closed, not escalated
  (`hal_Doc_04_Review_Round2.md`).
- **Doc_05 — Ecological Reconstruction:** **Approved to proceed** (2026-07-12). Review:
  Round 1 substantial (a required Step 5 element, Representative Theological Patterns, was
  effectively missing and added as new §9; a chronological ambiguity around Marcella; an
  unmarked Writing-From-Inside register break — `hal_Doc_05_Review_Round1.md`); Round 2
  documentation-hygiene only (`hal_Doc_05_Review_Round2.md`).
- **Doc_06 — Full Lexicon Development:** **Approved to proceed** (2026-07-12). Final term
  count 23 (15 Tier 1 with matching `Lexicon-Chunks/` files, 6 Tier 2, 2 Tier 3); 1 CT tag
  (Origenism); Pelagianism's non-CT-tagging explicitly deferred to Doc_08. Review: Round 1
  found 4 misdirected cross-references, a false Master Index reciprocity claim, an
  overstated verbatim claim, and Writing-From-Inside leakage in 3 sections propagated into
  their deployment chunks (`hal_Doc_06_Review_Round1.md`); Round 2 confirmed 3 of 4 fixes,
  found the fourth's own fix still inaccurate and corrected it directly (`hal_Doc_06_Review_Round2.md`).
- **Doc_07 — Integrated Ecology Analysis:** **Approved to proceed** (2026-07-12).
  **Significant finding:** Round 1's highest-severity finding was that §2 had reframed
  Doc_01/Doc_04's "same currency, different position" finding as a "non-overlapping
  domain" account — a real, subtle undermining of already-Approved reasoning
  (`hal_Doc_07_Review_Round1.md`). Round 2 traced the reworked section word-by-word against
  the original text and confirmed genuine, verified alignment — not escalated
  (`hal_Doc_07_Review_Round2.md`).
- **Doc_08 — Forces Document:** **Approved to proceed** (2026-07-12). 11 forces across the
  six-cell matrix; closed the Pelagianism CT-tagging handoff (decision: no CT tag).
  **Significant finding:** Round 1 found the 384–385 Rome crisis — this world's central
  transforming event — had no force entry at all and was mis-filed
  (`hal_Doc_08_Review_Round1.md`); Round 2 caught a further self-introduced Cell-placement
  conflict with Doc_04/Doc_06, resolved by deferring to the already-established
  classification (`hal_Doc_08_Review_Round2.md`); Round 3 was a light targeted verification
  of that fix (`hal_Doc_08_Review_Round3.md`).
- **Doc_09a — Story Inventory:** **Approved to proceed** (2026-07-12). 12 stories (6 Tier
  1, 0 Tier 2 — argued absence, 4 Tier 3, 2 Tier 4), no Tier 5, 6 named absences.
  **Significant finding:** Round 1 caught that the Origenist controversy/Rufinus rupture —
  called "this world's central internal fracture" at Doc_02 §2.1 — was missing from both
  the inventory and the Absent Stories list; added as S3a (`hal_Doc_09a_Review_Round1.md`);
  Round 2 cross-checked its confidence calibration against Doc_08's force entry 2B-1 and
  found an exact match (`hal_Doc_09a_Review_Round2.md`).
- **Doc_09b — World Profile (`hal_World_Profile.md`):** **Approved to proceed**
  (2026-07-12). Review Round 1 confirmed Section 10's hard verbatim requirement
  character-by-character against Doc_07 §8; found four moderate issues, including an
  **under-argued Living Tradition determination** (`hal_World_Profile_Review_Round1.md`);
  Round 2 confirmed the strengthened Section 9 argument, which actively rules out two
  named counter-candidates and lands on **NO living-tradition correspondence**
  (`hal_World_Profile_Review_Round2.md`). See OG-1 — this determination is now in tension
  with the current live registry.
- **Doc_09c — Validation Layer:** **Approved to proceed** (2026-07-12). 12 of 15 Part VI
  categories tested and Passed; Relational Safety, Adversarial Resistance, and Encounter
  Testing correctly deferred (no built Representative yet at drafting time). Review Round 1
  found self-certifying language overstating the document's own independence, plus a
  citation error (`hal_Doc_09c_Review_Round1.md`); Round 2 confirmed the deflation to
  compilation/citation register (`hal_Doc_09c_Review_Round2.md`). Explicit statement: this
  world **cannot** reach Frozen until Representative-dependent validation and External
  Scholarly Review close.
- **Representative Identity Decision (2026-07-12/13):** Four grounded options presented
  (Jerome; collective voice; Marcella; Paula) in `hal_Representative_Identity_Preliminary_Decision.md`,
  escalated to the project lead per protocol. **Mark selected a fifth option, superseding
  all four**: a period-typical, non-documented figure in the *vidua* (ascetic widow)
  status category — **name: Albina**, with one disclosed residual risk named and accepted
  at the time of the decision: "Albina" is also, in this world's own sources, the name of
  Marcella's mother (Ep. 127). Doc_10 was required to explicitly disambiguate.
- **Doc_10 — Representative Construction Package:** **Approved to proceed to live
  adversarial testing** (2026-07-13). `hal_Ecology_Assessment.md`,
  `hal_Representative_Construction_Notes_Albina.md`, the Permanent Prompt, World Capsule
  Core, and 12 Story-Chunks. **Significant finding:** Round 1 caught a meta-awareness leak
  in the Permanent Prompt — the highest-severity defect category under Total
  Embeddedness/No Meta-Awareness — plus a readability shortfall and a register slip
  (`hal_Doc_10_Review_Round1.md`); Round 2 independently re-verified with a word-count-based
  readability check rather than accepting the fix's own claim (`hal_Doc_10_Review_Round2.md`).
- **Live Adversarial Testing (RCF Part Eight, Phase Five, 2026-07-13):**
  `hal_Phase5_LiveTest_Transcript.md` (Round 1, 15 exchanges, 8 probe categories) scored
  `hal_Phase5_LiveTest_Scoring_Round1.md` — **provisional pass**, clean on 6/8 (Relational
  Safety untestable for lack of crisis-signal content); Confidence-Under-Thinness probes
  AMBIGUOUS. `hal_Phase5_LiveTest_Retest_Transcript_Round2.md` (7 further exchanges,
  escalated pressure) scored `hal_Phase5_LiveTest_Scoring_Round2.md` — **clean pass, 7/7**,
  the Round 1 ambiguity resolved. Explicit, disclosed scoping caveat: only the
  Representative's own words were testable — no Facilitator layer existed at this
  construction stage, so the full system-level relational-safety property remains
  untested and is **not** claimed as validated. This is where Generation 1 stopped.

**Two draft, never-finalized deliverables also on disk from this generation:**
`hal_Phase6_Facilitation_Brief_DRAFT.md` states its own status plainly in its header — "has
NOT itself cleared this project's own independent adversarial review process... should be
treated as a first-pass draft," produced by a separate integration pass, not the build
thread. `hal_Guided_Starters_V0_1_DRAFT.md` likewise states "DRAFT — awaiting Mark's
review. Not deployed." **Neither has a recorded review round or a recorded project-lead
disposition anywhere in this folder.** Stated plainly rather than invented: whether either
was ever finalized, superseded by Generation 2/3's own facilitation material, or simply
left as a draft, is not reconstructable from what's on disk.

---

## Build log — Generation 2 (Pass-2 WRS rebuild, FROZEN 2026-07-31)

Source: `Archive/Technology-Pass2-2026-08/Pass2/gates/S6.2_HAL_FREEZE_DECLARATION.md`, and
the corresponding entry in `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`
(2026-08-01 entry, "2 of the 3 remaining worlds (Hieronymian, PAHC) frozen and pushed").

**This is the one point in `hal`'s history where an actual, project-lead-anchored Freeze
was reached** — not merely "Approved to proceed."

- Froze a 97-record store (26 sources, 2 search records, world_core, 15 terms, 12 stories,
  9 figures, 10 gravities, 12 forces, 5 contested claims, voice_profile, 4 demonstrations),
  the first world authored end-to-end under the fleet's alias-safety gate (VG-1/VG-2),
  "opened and closed at zero."
- Freeze evidence: a two-trial blind-graded battery (Trial A 15/2/0, Trial B 13/1/1 with
  the one FAIL fixed and 6/6 reprobed), the fleet's first triple-partner TRR (24/24
  speaker-clean, 22/24 held-position with one flag declared — FLAG-032), parroting tested
  at 10 × 0.000.
- **Mark's two freeze-gate decisions, recorded in the System Hub Decision Log:**
  **Article 29 (living_traditions/universal-descent framing) — confirmed.** **Article 31
  (external scholarly review) — deferred to year two, aspirational by design** (this
  pattern was then saved to project memory so future freeze declarations treat provisional
  telos as by-design, not an open item to re-list each time).
- **Declared limits, carried forward honestly in the freeze declaration itself, not
  hidden:** FLAG-032 (table-register press class); FLAG-029 (upstream chunk wording); the
  Marcella-list apparatus check and the Palladius passage hunt (open verification items);
  Article 31 (as above); the relational-safety **system** caveat (Facilitator-layer
  end-to-end validation not claimable from this evidence); and — stated as **permanent, not
  a defect to fix** — the Author-Gravity extreme: "every account of the women's agency
  survives in Jerome's hand, and this freeze certifies the discipline that carries that
  honestly, not any escape from it."

This freeze's artifacts (the full `Pass2/` gate/battery/TRR/change-order set for `hal`) are
now under `Archive/Technology-Pass2-2026-08/`, not in `Build/worlds/hal/` itself — consistent
with the repo's own archival convention, but it means a reader working only from
`Build/worlds/hal/` would never see that this world was ever actually frozen. Noted for the
record; see OG-1 for why this freeze's current governing status is unclear.

---

## Build log — Generation 3 (new-architecture record rebuild, 2026-08-21, current basis)

Source: `Build/worlds/hal/build/BUILD-LOG.md`, `Build/worlds/hal/build/SOURCE-REQUEST-MANIFEST.md`,
`Build/worlds/hal/build/RECORD-SET-REVIEW-ROUND1.md`.

- Built the full voice-independent content canon fresh on branch `world/hal`: `world_core`,
  23 `source`, 10 `search_record`, 18 `term`, 11 `figure`, 6 `gravity`, 12 `force`, 7
  `contested_claim`, 16 `doctrinal_witness`, 19 `quote`, 12 `story`, 4 `honest_limit` = 139
  records. **Deliberately not built at this stage:** `voice_craft`, `demonstration`,
  compilation, admission — "the live-generation citation-and-grounding design is not yet
  proven end to end; building voice now risks a rebuild." **Representative identity
  explicitly reset:** `representative: null` in the draft registry entry; "the prior
  framework's preliminary decision was *not* carried forward." (Superseded — see OG-2.)
- Real findings made on this branch, beyond what Generation 1's cleared docs carried: the
  Marcella-correspondence letter list was edition-verified and found to have missed three
  letters (38, 59, 97); the 416 attack's fullest account was sharpened to note the
  women's own lost letter (Eustochium and the younger Paula's report to Innocent, attested
  only via Ep. 137 — the one attested act of the women's own authorship, itself lost);
  Jerome's own modest Hebrew self-assessment was located in-corpus (Ep. 108 §27); Sulpitius
  Severus's *Dialogi* I.8–9 was registered as a new admiring-witness source, closing an
  open flag from Generation 1's Doc_02; a new contested claim was added,
  `hal.contested.paula-jerome-relationship` (Jerome's partnership account vs. Palladius's
  "hindered by his jealousy" flatly disagree).
- **Independent adversarial review of the complete 139-record set** (fresh agent, no
  drafting context, 2026-08-21): `RECORD-SET-REVIEW-ROUND1.md`. Verdict: targeted fixes,
  no gravity/force/story/contested-claim classification required re-deriving. Two
  fabrication-adjacent substantial findings — a wrong date and a wrong "naming" claim for
  Rufinus's *Peri Archon* preface (repeated in two records), and two records that put a
  quotation-marked string in Jerome's mouth ("my own monastery has been destroyed") that
  does not appear verbatim in Epp. 138/139 — plus 7 minor and 5 cosmetic findings. **All
  eight findings were fixed directly on this branch following the review**, per the
  document's own disposition note.
- Source posture: `SOURCE-REQUEST-MANIFEST.md` states the vendored CCEL corpus already
  covers every load-bearing primary source this world's cleared docs cite. **Open, disclosed,
  non-blocking (P3) acquisition requests:** Egeria's *Itinerarium* (pilgrimage context
  only), Hilberg's CSEL Latin critical text of the letters (would allow offline
  Latin-wording verification; the English corpus already carries everything load-bearing),
  Prosper of Aquitaine's chronicle (bears only on day-level precision of Jerome's death
  date, which no record asserts as fact). **The constitutive absence, stated as data:** no
  text composed by Paula, Eustochium, Marcella, or Fabiola survives, anywhere — not a
  rights problem, a survival problem.
- **living_tradition_flag set provisionally TRUE**, explicitly "pending Mark's
  determination — flipping it is Mark's call." See OG-1: no record was found of that
  determination ever being made, and it stands in direct, unexplained tension with
  Generation 1's twice-reviewed World Profile finding of **NO** living-tradition
  correspondence.

**Current state of `records/hal/` (checked directly, 2026-09-20):** 173 records total —
6 gravity, 11 search_record, 11 figure, 16 doctrinal_witness, 28 source, 12 story, 7
contested_claim, 4 honest_limit, 32 quote, 23 term, 12 force, 1 voice_craft, 1 world_core,
9 demonstration — grown since the 2026-08-21 snapshot (quotes 19→32, sources 23→28, terms
18→23, contested claims 5→7) through later enrichment passes not separately logged in this
folder. `voice_craft` and `demonstration` — explicitly deferred at Generation 3's own
2026-08-21 entry — now exist (`records/hal/voice_craft/hal.voice.craft.md`,
`records/hal/demonstration/`), added in a later pass (git blame: commit `9876e314`, PR
#186 "census-content-enrichment").

---

## OG-1. Living Tradition Status — genuinely contradictory across generations, unresolved.

**The contradiction, stated plainly:**
- Generation 1's `hal_World_Profile.md` §9, reviewed and strengthened across two rounds
  (`hal_World_Profile_Review_Round1.md`, `_Round2.md`), reaches **NO living-tradition
  correspondence** — actively ruling out two named counter-candidates (a still-extant
  Jerome-patron religious order, founded too late to be a continuous descendant; Jerome's
  individual veneration as Doctor of the Church, a textual/reputational correspondence,
  not an institutional one for this world's own bounded community).
- Generation 2's freeze declaration (`Archive/.../S6.2_HAL_FREEZE_DECLARATION.md`) records
  **Mark confirming Article 29** for this world on 2026-07-31, with no further detail in
  that file about which direction (living-tradition-applicable, or not) was confirmed.
- Generation 3's `Build/worlds/hal/build/BUILD-LOG.md` (2026-08-21) sets
  `living_tradition_flag` to **provisionally TRUE**, explicitly "pending Mark's
  determination."
- The **current live registry**, `records/worlds/hal.yaml`, carries `living_tradition_flag:
  true` — unchanged across every package rebuild found in git history for that file back
  to the September 2026 registry split (`e82b0dd5` onward).

**What this pass could not determine:** whether Generation 2's Article 29 "confirmed"
disposition was itself a TRUE or a NO determination, whether it was ever reconciled with
Generation 1's opposite, reviewed finding, and whether the current `true` flag reflects an
actual project-lead decision made at some point between generations or is simply
Generation 3's untouched placeholder value, carried through every rebuild since because
nothing has ever revisited it. **No dated record of Mark actually choosing between these
two positions for `hal` specifically was found anywhere in this folder, the Pass-2
archive, or the System Hub Decision Log.** Given Article 29 is a freeze-eligibility gate
and this flag has real downstream disclosure consequences (whether Albina's voice may
speak of a living heir), this is escalated here as a genuine open item rather than
resolved either way.

## OG-2. Representative identity: reconfirmed as Albina, but `world_core`'s own text is now stale.

Mark's original identity decision (Generation 1, 2026-07-12/13) named **Albina**, *vidua*
of the Hieronymian household, with the Marcella's-mother naming-collision risk disclosed
and accepted at decision time. Generation 3's 2026-08-21 rebuild reset this to
`representative: null`, stating explicitly that the prior decision was not carried
forward. The current registry, `records/worlds/hal.yaml`, shows the decision **was in fact
reconfirmed**: `representative: {name: Albina, role_label: "Widow of the Household"}`,
consistent with a later ruling record embedded directly in `records/hal/voice_craft/hal.voice.craft.md`:
*"RULING RECORD (Mark, in session): Representative identity confirmed as Albina, Widow of
the Household (records/worlds.yaml's hal.representative entry, PR #13)... consistent with
the fleet's own established discipline (alx.voice.craft)."* That same voice_craft record
also carries the naming-collision caution forward faithfully, unprompted.

**The genuine, findable drift:** `records/hal/world_core/`'s own body text still reads,
uncorrected, *"World/Representative identity naming remains Mark's per-world touchpoint;
the registry entry holds representative: null accordingly"* — text written before the PR
#13 reconfirmation and never updated to match. A reader consulting `world_core` alone (as
opposed to the registry file or the voice_craft record) would be told something no longer
true. **Not escalated as a decision question — this is doc-hygiene drift, not an open
decision — but flagged so it doesn't go quiet**, per this project's own standing rule
against unlisted drift.

## OG-3. Portrait status — checked directly against the disclosed `witt` gap pattern: RESOLVED, no gap found.

`witt`'s own `Open_Gaps_Tracking.md` (OG-20) discloses that Nikolaus's portrait was
researched, generated, and Mark-approved, but the actual `Nikolaus_Portrait.png` file
never made it into the repository — a real, still-open gap there. Checked the equivalent
for `hal` directly: `Build/Ministry/Communication/Brand-Assets/Representative-Portraits/bethlehem/Albina_Portrait.png`
exists (1.1 MB, on disk), and the frontend is correctly wired to it —
`cic-poc/frontend/public/images/portraits/bethlehem.png` exists as a real file, and
`cic-poc/frontend/src/data/worlds.ts` maps `hal: { portraitImage: '/images/portraits/bethlehem.png', ... }`.
A separate copy also exists at `cic-website/assets/portraits/bethlehem.png` for the public
site. The System Hub Decision Log additionally notes Albina's is, as of that entry, the
**only** world with a standalone table-ready object asset already built (portraits/
world-media tiles otherwise "confirmed complete for what they cover"). **No gap here** —
stated as a genuine negative finding, not assumed.

## OG-4. Cross-world lexicon confidence-vocabulary / Author-Gravity finding — investigated, mostly corrected 2026-07-20, one narrow residual left open, and the whole finding is arguably moot under Generation 3's architecture.

**The original finding** (`Build/worlds/alx/Analysis/CROSS_WORLD_FINDING_Lexicon_Confidence_Gap.md`,
2026-07-19, logged at `Build/Ministry/Operations/Standing/CiC_System_Hub_Decision_Log.md`
2026-07-19 entry): Hieronymian-Ascetic-Literary's `Lexicon-Chunks/` carried Article 17
confidence-vocabulary language in only 6 of 15 chunks (40%) and Author-Gravity/mediation
language in only 1 of 15 (7%), against the L4 template's own Key Sources instruction. The
finding explicitly routed this to whoever owns `hal`'s own build thread, "not something to
import from Alexandria's conventions wholesale," and did not touch `hal`'s files.

**What actually happened next (2026-07-20 fix pass, logged in the same Decision Log, "Three
lexicon fixes closed"):** `hal`'s 15/15 chunks were audited directly and fixed. **Two
corrections to the original brief were made in the process:** the "entry 10/matrona" quote
cited actually belongs to entry 11, and — more importantly — **the stated 6/15 baseline was
itself found to be a naive word-scan overcounting casual prose, not real Article-17
non-compliance.** The real fix applied: restored the source's own "Author Gravity note:"
label wherever the source's own Doc_02 material actually supports one — **8 of 15
entries** — and *correctly declined to fabricate one for entries the source doesn't
support (e.g. *matrona*).* **One narrow, disclosed residual was left open, not resolved:**
`hal_lex01` (Hebraica veritas) was found to have a real cross-location prose divergence
between the `World-Builds` copy and the then-deployed runtime copy, traced to a specific
commit (`b7ad9a2`) — the same theological-clarity fix that had resolved an earlier
Permanent Prompt/Capsule Core drift, but this lexicon chunk's copy wasn't synced when that
fix landed. That entry states explicitly: **"left for Mark's decision — not assumed to
resolve the same way as the earlier prompt drift."**

**Checked directly against the files on disk today (2026-09-20):** re-ran the same kind of
count against the current 15 files in `Build/worlds/hal/Lexicon-Chunks/`. 8 of 15 carry explicit
"Author Gravity" / mediation-risk language (`hal_lex01, 03, 04, 07, 08, 09, 11, 13`) —
**matching exactly** the 2026-07-20 fix's stated result, confirming that fix genuinely
landed and has held. Confidence-vocabulary language (the five-level terms spelled out
literally) remains present in only a minority of files by a strict reading — but the
2026-07-20 entry's own finding that a literal word-scan is the wrong measure for this
world's chunks stands unrebutted; no later entry re-litigated it with a better method.

**Whether `hal_lex01`'s specific residual divergence was ever resolved could not be
determined.** The deployed-copy half of that comparison (`cic-poc/backend/data/hieronymian_world/`)
no longer exists in this repository — it was superseded by Generation 3's record-based
architecture (`records/hal/term/`), which carries confidence grading as structured,
schema-enforced YAML metadata (`confidence: {formation_confidence: ..., citation_specificity:
..., verification_state: ...}` on every record — verified directly against
`records/hal/term/hal.term.hebraica-veritas.md`) rather than as prose convention. **This
makes the original prose-lexicon gap largely moot at the architecture level going
forward** — the thing the finding was actually protecting against (an ungraded claim) is
now structurally harder to produce — but the specific `hal_lex01` residual, and the
`Lexicon-Chunks/` files themselves as historical build artifacts, were never explicitly
declared closed or superseded anywhere this pass could find. **Flagged open, not claimed
resolved, pending confirmation that the `Lexicon-Chunks/` artifacts are legacy-only.**

## OG-5. Article 31 (external scholarly review) — still outstanding, by design.

Generation 1's Doc_09c and the Facilitation Brief draft both state this world cannot reach
Frozen without it. Generation 2's freeze declaration records Mark's own decision to defer
it: **"Article 31 (external review) — deferred to year two, aspirational by design."**
Carried here as a standing, disclosed, project-lead-owned deferral — not a defect, and not
something this pass treats as needing action, but tracked per this project's own rule that
every disclosed deferral gets a durable, findable record rather than living only in an
archived file.

## OG-6. Diligence check for the Alexandria-OG-6-style "structural corpus gap" — run, closed clean.

`Build/worlds/hal/build/records/search_record/hal.search.unopened-volume-sweep.md` (2026-08-27) ran the same
class of check Alexandria's OG-6 finding named: every vendored volume whose principal
author this world names while never opening that author's own work. Twelve candidates
checked; three opened (Augustine's *City of God* XVIII.42–44 for the other side's case at
full strength; Origen's *Philocalia* as the control on whether Rufinus doctored *De
Principiis* in translation; the Syriac recension of Palladius's *Lausiac History*, which
turned out to sharpen — not just corroborate — the existing hostile-witness reading, and
surfaced a real, named absence: Paula is dropped from the Syriac's list of holy women
entirely). Nine declined with individual reasoning given for each (mostly: already-opened
volumes of the same author, on questions this world's own controversy doesn't ask). **No
structural gap found; disposition: closed, findings folded into the record set as
`hal.source.augustine-city-of-god`, `hal.source.origen-philocalia`, `hal.source.palladius-paradise-syriac`.**

## OG-7. Two draft deliverables with no recorded review or disposition.

`hal_Phase6_Facilitation_Brief_DRAFT.md` and `hal_Guided_Starters_V0_1_DRAFT.md` (see
Generation 1 build log above) both self-report as unreviewed drafts. No review-round
artifact, decision-log entry, or project-lead disposition for either was found anywhere in
this folder. Stated honestly rather than assumed: it's possible later generations'
facilitation material superseded these drafts outright (the current live app's Facilitator
layer is referenced elsewhere in this folder as already built at the architecture level),
but nothing on disk confirms that explicitly for `hal`. Left open rather than guessed at.

---

## What this pass did NOT find (stated so the absence itself isn't mistaken for nothing having been checked)

No standalone `hal`-specific portfolio audit postdating the 2026-07-19 cross-world finding
was found that re-checked `hal` specifically. No dated record of a project-lead
determination on OG-1 (living tradition) was found. No record of `hal_lex01`'s residual
divergence (OG-4) being finally closed was found. No review round or disposition for the
two draft deliverables (OG-7) was found. Each is logged above as open rather than silently
omitted.

---

**Reconciliation note, 2026-09-22 (live→main merge).** `live` had independently
created its own `Open_Gaps_Tracking.md` for this world on 2026-09-20 (same
day it authored this world's `facilitator_brief` record), unaware of this
file's own history above (`main` and `live` had diverged since 2026-09-20).
Its one entry — including its own RESOLVED update the same day, ruling
`living_tradition_flag: false` and closing the `census-living-flag/hal`
waiver, already reflected in `engine/m1/cross_world.py`'s merged
`ACCEPTED_OPEN` dict and this merge's own auto-resolved `records/worlds/
hal.yaml` — is appended below as OG-8, renumbered on merge.

## OG-8. **Living-tradition status: the source construction document's "confirmed NO" is contradicted by the current world registry — surfaced 2026-09-20 while authoring this world's `facilitator_brief` record, not yet resolved either way.** This world's own hand-authored, never-independently-reviewed Phase Six draft (`Build/worlds/hal/hal_Phase6_Facilitation_Brief_DRAFT.md`, Section B7) states: "Living-tradition status: confirmed NO, on a reasoned basis: two plausible counter-candidates (a modern Hieronymite religious order; Jerome's ongoing veneration as a Doctor of the Church and the Vulgate's later official status) were actively considered and rejected — the former is a 14th-century foundation with no institutional continuity to this specific household, the latter is textual/reputational correspondence, not institutional correspondence, and postdates this world's own bounded span." This is independently corroborated by `Archive/Ministry-Early-Days-2026-07/Scholarly-Review/CiC_WorldBrief_Hieronymian_V0_1_DRAFT.md` (archived on `main` since this entry was originally written, per Mark's 2026-09-21 Ministry-tree triage — same content, moved) ("No living tradition: two counter-candidates... were considered and rejected; the community's own institutional life does not survive its founders"). The current, live world registry, `records/worlds/hal.yaml` (verified verbatim this session), sets this world's `living_tradition_flag: true` — the same field this project's engine code (`engine/m1/cross_world.py`, `engine/m6/census_sync.py`) treats as the authoritative, machine-checked determination, cross-checked automatically against the public census's own `living` field. Nine of this fleet's ten current world registries carry `true` (alx, cappadocian, desert, gallic, hal, ijc, pahc, syr); only `don` (Donatism — whose own registry comment states its "institutional life does not survive its founders," the identical language used for hal in the Ministry document above) and the synthetic `fix` fixture carry `false`. This makes hal's own `true` flag either a deliberate correction of the Phase Six-era "confirmed NO" finding, or an unreviewed default that was never brought into line with hal's own specific determination — nothing in this repository currently documents which. The one real hal M1 record that speaks to this question directly, `records/hal/doctrinal_witness/hal.dw.one-church.md`, does not resolve it either way and says so in its own trailing note: "the living-tradition determination and its doorway chrome are Mark's touchpoint, outside this record." Its own `text` field ("Is there a church today you could visit that is ours? No... Many churches now claim parts of what we left — our Bible above all") is compatible with either a `true` or a `false` registry flag, depending on how diffusely "living tradition" is meant. Because this bears on how a facilitator introduces this world and manages a participant's prior associations (a fleet-adjacent, not purely per-world, question), it is recorded here as an open discrepancy rather than resolved either way: `hal.facilitator_brief.hieronymian-ascetic-literary.md`'s own `living_tradition_handling` field and one `cautions` entry were built to state only what `hal.dw.one-church` actually supports (no institutional continuity; a dispersed, diffuse legacy), and deliberately do not carry forward the Phase Six draft's flat "confirmed NO" framing as settled fact. Needs the project lead's own confirmation of which position is current — and, if `true` is correct, what specifically grounds it (Jerome's individual veneration? the Vulgate's later reception? something else?) — before either the Phase Six draft or the current registry flag is treated as authoritative on this point.

**RESOLVED 2026-09-20, ruling: false.** Mark confirmed `false`, matching the construction-stage documents' own reasoned "confirmed NO" finding over the registry's unreviewed `true` default. `records/worlds/hal.yaml`'s own `living_tradition_flag` is flipped to `false`, now matching `cic-website/data/world-census.json`'s own `living` field (which already read `false` — a genuine, independently hand-authored editorial call that turns out to have had this right all along; the registry was the stale side). The fleet-wide `ACCEPTED_OPEN` waiver `census-living-flag/hal` (finding F-06, `engine/m1/cross_world.py`) is closed and removed. `hal.facilitator_brief.hieronymian-ascetic-literary.md`'s own `living_tradition_handling` field and its `cautions` entry are updated to state this as settled rather than an open discrepancy. The Phase Six draft itself is left unedited, per this project's own "keep the live/canonical surfaces clean" discipline (a construction-phase draft is not corrected retroactively) — it should be read as confirmed correct on this point, not merely uncontradicted.

**Note for whoever next touches alx, pahc, or ijc:** those three worlds carry the identical `census-living-flag` discrepancy (registry `true`, census `false`), tracked under the same fleet finding F-06 — this hal ruling does not extend to them automatically, since each world's own construction-stage reasoning (if any exists) needs its own check before asking Mark to rule on it the same way.

## OG-9. **One fragment/verbless `modern_rendering` sentence, found by `engine/m1/sentence_completeness.py`'s report-only sweep — current as of `engine/m1/reports/sentence-completeness-report-2026-09-24.json`, not yet human-reviewed.** `hal.quote.hail-bethlehem`'s own flagged sentence: "Hail, Bethlehem, house of bread - where the Bread that came down from heaven was born." (`no_finite_verb`). Report-only check (not in `gates.GATES`); its own docstring requires a human read against the actual fragment rule before treating this as a defect — an apostrophe/address ("Hail, X") is a common, legitimate rhetorical fragment, not necessarily a violation. Logged as found and current, not adjudicated. See `Build/worlds/pahc/Open_Gaps_Tracking.md`'s own entry on this same `sentence_completeness.py` report-run, filed 2026-09-24, for the full fleet-wide context.

## OG-10. Decision 8B batch 3 — embedded old-translation quotations resolved in 5 host records, `engine.m1.embedded_quotations` count 5 → 0.

**Status: CLOSED for this batch's own 5 host records; hal carries no further `embedded_quotations` findings.**

P3 Decision-Log Entry 38 registered `engine/m1/embedded_quotations.py` as a standing report-only check and named Option B - extracting an embedded old-translation quotation that matters into its own `quote` record, with an Opus-authored `modern_rendering` - as a separate, batched workstream. Mark's ruling: **"c+b"**. This is the third batch of the fleet-wide pass (after syr + cappadocian, then desert), one world per batch: `hal.demo.believe`, `hal.demo.jesus`, `hal.demo.someone-like-me`, `hal.demo.suffering`, `hal.demo.woman-authority` - all 5 of hal's flagged hosts, 8 spans total, all already pointing at existing `quote` records via `sources[]`; no new quote record was needed.

**V1.8 §3 discipline applied (Mark's ruling "a", 2026-09-25, PR #615):** each host's own `exchange[].text` field was edited only in the specific sentence that held each flagged quote - nothing else in that field was touched. No `relations[]` link was needed (all 8 quote records were already declared in each host's own `sources[]`). Process-narration apparatus ("CORRECTED per independent Opus adversarial review...", "BAR SWEEP (2026-08-29...)", "LEXICON LABEL PASS (2026-08-30...)") was deleted, not reworded, from all 5 trailers.

**Span accounting, all 5 host records, every flagged span individually re-verified against its own cited quote record's `text` and `modern_rendering` fields:**
- **4 spans already matched their quote record's `modern_rendering` exactly** (accurate, deliberate quotations): `hal.demo.believe`'s Cicero-dream accusation (`hal.quote.dream-follower-of-cicero`); `hal.demo.jesus`'s "Hail, Bethlehem" line (`hal.quote.hail-bethlehem`); `hal.demo.someone-like-me`'s Portus-strangers line (`hal.quote.portus-strangers`); `hal.demo.suffering`'s "city taken" line (`hal.quote.city-taken`).
- **4 spans had drifted from both their quote record's `text` and `modern_rendering` fields** - presented in quotation marks as if verbatim, but matching neither: `hal.demo.jesus`'s "eyes of faith" material (`hal.quote.eyes-of-faith`) - the host's own trailer already documented this material as intended to be "correctly left unquoted," a design intent the actual quote-marked text contradicted; `hal.demo.someone-like-me`'s "detestable monks" line (`hal.quote.detestable-monks`) - reworded from "How long must we refrain from driving" to "How long before we drive"; `hal.demo.suffering`'s "house destroyed" line (`hal.quote.house-destroyed`) - reworded and reordered ("its earthly wealth has been" for "so far as its earthly wealth is concerned, it has been"; "Better to live on bread" for "To live on bread is better"); `hal.demo.woman-authority`'s "recourse to Marcella" line (`hal.quote.recourse-to-marcella`) - abbreviated, dropping the quote's own opening clause ("So after I left Rome") and reworded tail ("people went to her to settle it" for "She was the one who settled it").

All 8 spans were de-quoted and paraphrased in the Representative's own indirect voice within the single sentence each occupied - for the 4 accurate quotations, this is a pure extraction-discipline fix (still fully covered by the underlying quote record for anyone who wants the verbatim source); for the 4 drifted ones, de-quoting also resolves the fidelity defect directly, since the host no longer claims a verbatim quotation it did not carry.

**`sources[].locus` apparatus corrected to match:** every "verbatim quote used" locus for a quote this batch de-quoted was changed to "paraphrase source (...)", naming what it now grounds. One further stale locus was found and fixed in the same sweep, outside the 8 flagged spans proper: `hal.demo.suffering`'s own `hal.quote.innocent-ravages` source was already labeled "verbatim quote used" despite the host's `exchange` text never having quoted it directly (already a plain paraphrase before this batch touched the file) - corrected to "paraphrase source" alongside the others, since it sits in the same sources block this batch was already editing and makes exactly the same class of false claim this batch's own discipline exists to catch.

**Full-field sweep, per the managing thread's own instruction (learned from #612's own two extra review rounds):** every field of all 5 touched hosts was grepped for "verbatim", "exact", "word for word", and "quot" before this PR was opened, and every remaining match confirmed true - each either names a `hal.quote.*` record id (not a fidelity claim), or is a corrected `paraphrase source` locus, or is an unrelated use of "exactly"/"quote" as a plain word rather than a verbatim-fidelity claim.

## OG-11. **hal's first M3 sealed live-admission battery run against its current M2-compiled package, 2026-09-27 — 28/28 probes pass, part of closing the fleet-wide M2-migration/validation gap audit.** `Build/Ministry/Operations/Audits/CiC_M2_Migration_Validation_Gap_Audit_2026-09-27.md` (Finding 3) found that every deployed world except rzg had never had `engine.m3.live_admission_run` (the real-Bedrock-spend, 28-probe sealed admission battery) run against the package the 2026-09-26 fleet-wide M2 rebuild produced — hal's own prior M3 reports (`fleet-parity`/`remaining-four`, 2026-08-28) all predate that rebuild. `python3 -m engine.m2.cli staleness-check`, run fleet-wide immediately beforehand, confirmed hal's pin clean (`packages/hal/2026-09-26T20-12-57Z`, matching `records/worlds/hal.yaml`; `"stale": false, "diff": []`). Run in one batch invocation together with ijc, pahc, syr, and witt (`engine.m3.live_admission_run --worlds hal,ijc,pahc,syr,witt`, model `us.anthropic.claude-sonnet-4-5-20250929-v1:0`, region `us-east-1`, protocol `blind`); real cost for hal specifically $0.46871775 (batch total $2.4555968999999997 against the $3-per-invocation ceiling). **Result: 28/28 probes pass, no failing probe.** Full report: `engine/m3/reports/live-admission-report-batch2-2026-09-27.json`. Unlike rzg's own first run (`Build/worlds/rzg/Open_Gaps_Tracking.md` item 50, 27/28, one open finding not fixed there), this run surfaced no new defect for hal to carry forward — it closes hal's own share of the audit's named gap with a clean result. Investigation only: no `records/`, `packages/`, or registry file was touched to produce this entry, and no probe finding needed fixing.

**Package repinned** (`packages/hal/`, current pin, `records/worlds/hal.yaml`); `engine.m1.tests.test_embedded_quotations::test_fleet_survey_world_counts_match_the_og10_baseline`'s pinned baseline updated `"hal": 5` → `"hal": 0`; both staleness checks pass; `engine.m9.cli check` passes; `tools/check_paths.py --baseline` and `tools/check_live_commentary.py` show no new findings from any file this batch touched. A real trial build's gate battery (`python -m engine.m2.cli build hal`) shows every gate passing except `readability` (165 findings, unchanged from the pre-existing `m1:readability/hal` waiver, none in any file this batch touched) - no waiver needed tightening, since the count did not move; `reciprocity` and `voice-perspective` both pass clean.

## OG-12. **Record defects found while drafting and reviewing use notes (slice 6), 2026-10-04.** Not fixed; content for this world's build thread.
(1) `hal.quote.no-one-preferred-to-the-seventy` quotes Augustine's City of God XVIII.43, which the record dates about 426, after the window; it carries no use note and stays under hal's use-note waiver of one until this thread marks it analytic or replaces it. (2) `hal.dw.was-jesus-god` says "a dying woman greeted his birthplace by name"; Paula's "Hail Bethlehem" is from her arrival about 386 (Ep. 108 sec. 10), and her dying words (sec. 28) are psalm verses that do not name Bethlehem. (3) `hal.quote.let-her-be-brought-up-in-a-monastery`: locus Ep. 107 secs. 4-7; the quoted sentence is sec. 13 in the vendored text. (4) `hal.quote.those-of-my-own-order`: its modern lens note carries literal backslashes before its quote marks inside a folded block, while the body says there are none. (5) `hal.dw.empire` says the letter mocks clergy who "chase inheritances from wealthy widows" and rise "before dawn"; Ep. 22 sec. 28 has curled hair and rising "with the sun", and nothing on inheritances. (6) `hal.dw.church-failure`: the mockery of the dead Rufinus as "Grunnius" is found only in the commentary prefaces, and `hal.source.vulgate-prefaces` is not in its sources. (7) `hal.dw.inner-life`: the "love the knowledge of scripture" advice is Ep. 125, which has no source record and is not in its sources (the body says so). (8) `hal.quote.dream-follower-of-cicero` sits inside `hal.quote.a-follower-of-cicero-and-not-of-christ` (Ep. 22 sec. 30); one is graded Documented, the other Contested. (9) Same text twice: `hal.quote.city-taken` and `hal.quote.the-city-which-had-taken-the-whole-world` (Ep. 127 sec. 12); `hal.quote.innocent-ravages` and `hal.quote.they-have-left-untold-the-name` (Ep. 137). (10) `hal.quote.hindered-by-jerome`: verification_state reads verified-via-authority while the body says the text was checked word for word against the vendored Clarke file. (11) `hal.contested.ep46-authorship`: formation_confidence Widely Accepted beside evidentiary_weight contested, with no divergence note. (12) `hal.term.praeceptor`'s body says Bibliotheca, Scriptorium, Propositum and Exegesis have no standalone records; all four now do. That body and those of bibliotheca, scriptorium, propositum and exegesis-as-practiced-authority call the record a draft while its status is ready. (13) `hal.term.grammaticus` and `hal.term.praeceptor` cite only the De viris self-entry, which does not name Donatus; "my master Donatus" is Apology against Rufinus I.16 (`hal.source.jerome-apology-rufinus`). (14) `hal.contested.chronology` dates Marcella's household as a formation site "from the 340s" while its held_against argues against a "360s-370s placement", and it states the c. 347 birth year as received without naming the reconstruction. (15) `hal.term.origenism` says "the 390s"; `hal.gravity.controversy-pressure` gives 393-403. (16) `hal.gravity.epistolary-formation`'s plain-language description, written under the live-surface rule, says "long arguments over scripture" (the record says only scriptural argument, and its own example is the Marcella question-and-answer series) and "a household split between Rome and Bethlehem" (the record says community; in this world the household is Marcella's own circle). Both are acceptable readings, not errors; the tighter wording ("arguments over scripture", "the group split between Rome and Bethlehem") goes in at hal's next admission. Status: OPEN.

## OG-13. **Voice errors found in the pre-launch review (old-against-new grade and boundary battery), 2026-10-04.**

Errors in the voice's replies, each confirmed against the records by an independent Opus check; the records themselves are right. Content for this world's build thread: a use note's not_for, or an honest limit, that names the misreading is the usual remedy. The battery reports are on branch review/boundary-battery; the probe replies are in the 2026-10-04 admission transcripts.

(1) Probe f1-e: the Oea episode reversed - the reply says the town's Jews confirmed the Hebrew supported the new translation; `hal.story.oea-gourd` has them siding with the old reading and the bishop correcting it back. The same reply turns Augustine's "no one should be preferred to the Seventy" into "many preferred" Jerome's version.

Status: OPEN.

## OG-14. **Voice errors found in the staging reading of the voice hand-off, 2026-10-07.**

Errors in the voice's replies in the named, capped live test "voice hand-off staging reading, 7 October" (decision 57): four questions put to this world's Representative on main at ccc0ae4e, the merge of #811. Each item was traced against this world's records by an independent Opus check. The replies are in `engine/m4/reports/live-turn-report-hal-2026-10-07-voice-handoff-staging-reading.json` (#816). Not fixed; content for this world's build thread. Items are grouped by the reading's five defect classes: (A) altered words inside quote marks; (B) scripture or creed quoted or listed with no record behind it; (C) a demonstration record recited word for word; (D) doctrinal-witness text pasted near word for word, including a record's own scripted question; (E) a misstatement against a specific record. A class not listed did not occur in this world.

(1) (D) "Who is Jesus?" reproduces `hal.dw.jesus` near word for word, in full (about 170 of 173 words). "What did he do?" is mostly `hal.dw.record` word for word, reordered. "Why did your people believe this?" lifts whole sentences from `hal.dw.authority` and `hal.dw.believe`. No reply voices a record quote word for word.

(2) (E) "What does Hebraica veritas mean?": "a single changed word - 'gourd' instead of 'ivy'" reverses `hal.story.oea-gourd`, where the new translation put ivy where the old version had gourd. This is a second reversal of the same story; the first is item (1) of the pre-launch review entry of 2026-10-04.

(3) (E) The same reply: "But we held to it. For us, correcting a word against the Hebrew was as much a discipline as fasting" presents the principle as the community's view. The not_for of `hal.term.hebraica-veritas` bars treating it as this world's consensus rather than Jerome's own.

Status: OPEN.
