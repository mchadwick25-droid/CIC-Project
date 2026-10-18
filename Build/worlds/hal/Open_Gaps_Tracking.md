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

## OG-14. Spoken text opens on a question or carries a stage direction, 2026-10-06.

11 spoken field(s) across 11 record(s) in witness, term and story text have a first sentence that ends in a question mark, or carry "your second question", "start with the part", "you asked" or "as you asked". The voice answers in the kind the participant asked, so spoken text must start with the answer. Content for this world's record pass; the check is `spoken_scaffolding.scaffolding_hits`. Waived in `engine/m1/cross_world.py` as `spoken-scaffolding/hal` until the pass lands; the pass removes the waiver. First record: `hal.dw.apostolic`.

## OG-15. **Voice errors found in the staging reading of the voice hand-off, 2026-10-07.**

Errors in the voice's replies in the named, capped live test "voice hand-off staging reading, 7 October" (decision 57): four questions put to this world's Representative on main at ccc0ae4e, the merge of #811. Each item was traced against this world's records by an independent Opus check. The replies are in `engine/m4/reports/live-turn-report-hal-2026-10-07-voice-handoff-staging-reading.json` (#816). Not fixed; content for this world's build thread. Items are grouped by the reading's five defect classes: (A) altered words inside quote marks; (B) scripture or creed quoted or listed with no record behind it; (C) a demonstration record recited word for word; (D) doctrinal-witness text pasted near word for word, including a record's own scripted question; (E) a misstatement against a specific record. A class not listed did not occur in this world.

(1) (D) "Who is Jesus?" reproduces `hal.dw.jesus` near word for word, in full (about 170 of 173 words). "What did he do?" is mostly `hal.dw.record` word for word, reordered. "Why did your people believe this?" lifts whole sentences from `hal.dw.authority` and `hal.dw.believe`. No reply voices a record quote word for word.

(2) (E) "What does Hebraica veritas mean?": "a single changed word - 'gourd' instead of 'ivy'" reverses `hal.story.oea-gourd`, where the new translation put ivy where the old version had gourd. This is a second reversal of the same story; the first is item (1) of the pre-launch review entry of 2026-10-04.

(3) (E) The same reply: "But we held to it. For us, correcting a word against the Hebrew was as much a discipline as fasting" presents the principle as the community's view. The not_for of `hal.term.hebraica-veritas` bars treating it as this world's consensus rather than Jerome's own.

Status: OPEN.

## OG-16. **Identity-and-scaffolding pass on hal's spoken text, 2026-10-07: question-form openers and second-person directions removed from 13 witness records and 1 story record; the Jesus witness leads with who.**

**Records changed (spoken `text` field):** `hal.dw.apostolic`, `hal.dw.authority`, `hal.dw.doubt`, `hal.dw.empire`, `hal.dw.hell`, `hal.dw.jesus`, `hal.dw.marriage-ending`, `hal.dw.one-church`, `hal.dw.practices`, `hal.dw.record`, `hal.dw.sin-grace`, `hal.dw.suffering`, `hal.dw.was-jesus-god`, and `hal.story.attack-416`. Also `records/worlds/hal.yaml` (package pin). No other file in `records/hal/` was touched. Read and left unchanged: `hal.dw.believe`, `hal.dw.church-failure`, `hal.dw.inner-life` (their openers are statements; "What we would say to you is not an argument. It is this:" in `believe` was judged the world's own offer, not a restated question, and is listed here for the reviewer); the 23 term records (`plain_meaning`, `quick_meaning` carry no scaffolding); the other 11 story records (no question-form openers or directions; `hal.story.rome-crisis` keeps the crowd's own question, which is quoted source speech from `hal.quote.detestable-monks`).

**Identity witness.** `hal.dw.jesus` already led with who. Its first sentence, "To us Jesus is the Word of God made flesh - and made flesh in the very place where we chose to live and die", is now two: "To us Jesus is the Word of God made flesh. He was made flesh in the very place where we chose to live and die." The split adds the subject and verb "He was"; nothing else in the text moved. Every claim stays sourced as before (Ep. 108 sec. 10; Ep. 22 secs. 1, 25).

**What each opener now states (all content already in the old text; moved, not added):**
- `apostolic`: "Some of our practices went back to the apostles, and some were new." (a summary of the two halves the old text already gave: baptism, eucharist and scriptures traced to the apostles; the monastic way new within living memory). It replaces "Did our practices go back to the apostles?". "Did that argument work? Our own critics fought it" became "Our own critics fought that argument".
- `authority`: opener unchanged (a statement); "What about the council that supposedly voted Jesus into being God? We were born after Nicaea." became "We were born after Nicaea, the council that supposedly voted Jesus into being God."
- `doubt`: "Was there room for doubt? There was room for questions" became "There was room for questions"; "doubt" is first used later in "the darker kind of doubt".
- `empire`: "In our day, Christians were not hiding in the catacombs."; "We said the empire's embrace had corrupted the church. We said it loudly - about everyone but ourselves." (replacing "Did ... corrupt the church? We said yes, loudly"); "By our own evidence, an outsider would have found these strangest:" (replacing the question). The added "We said it" is a sentence split for the readability gate.
- `hell`: "We believed in real judgment and real punishment. We say so without softening." (dropped "Do you believe people like me are going to hell? Here is what we actually held"; "without softening" stays a description of the telling, as in the old text; "We say so" is added by the sentence split). The narrowness question became "We held one way without embarrassment - Christ. We would not have understood its narrowness as an objection." (the old text said "the question").
- `marriage-ending`: "Our answer was Fabiola rather than a ruling: divorced, she belonged here. We kept her story where everyone could see it." The clause "divorced, she belonged" was moved up from "So: divorced, she belonged." near the end, where "Remarried, it was named a fault, ..." now follows directly. The word "here" was added to "she belonged" (from the removed question's "belong here"). The opener names Fabiola's case, as the old text did, and does not state a rule for divorced people in general.
- `one-church`: "Our church was Catholic, and we used exactly that word for ourselves."; "No church you could visit today is ours. No single door today opens onto us."
- `practices`: "Born again is not our phrase, but we spoke of baptism as the washing that makes new." This moves the old "The words are different" up front and drops it from its old place; "born again" is the participant's term, repeated for an antecedent. "We did not tithe - a tenth would have sounded timid here." "No end-of-the-world scheme like the rapture is in our pages." (old: "anything like the rapture? No such scheme is in our pages").
- `record`: "First and above everything, we had the writings about Jesus." (the old text said "the writings" after the question). "We knew the resurrection really happened from the writings we trusted enough to spend a life correcting. We knew it from a hope strong enough that people gave away fortunes on it." (the added "We knew it" is a sentence split).
- `sin-grace`: opens "We held that everyone inherits Adam's fall, and everyone needs the washing of baptism." (moved from the third sentence); "Our last great argument came close to that ground" follows. "The bread and cup were the Lord's body and blood, received with fear and love - and that is nearly all our record says." "We did not speak of being saved by faith alone." Its `retrieve_when` is about infant versus adult baptism; the text says nothing about infants, which is a mismatch of the tags and the text, not touched here. Likewise `hal.dw.authority` has `retrieve_when` "participant asks who appointed or ordained the bishops", which its text (how disputed belief was settled; Nicaea) does not answer; its opener was not edited and the tag is not touched.
- `suffering`: opens "Our answers were the old ones: judgment on a proud city, reward stored up for the afflicted, the dead safe with Christ." (moved up from mid-paragraph); "We were not spared the question of where God was." (the old text said "the question"); the closing "If you ask where God was, we will give you our answers. Our sobs come with them." became "Those are the answers we give, and our sobs come with them."
- `was-jesus-god`: opens "Jesus is God the Son, of one being with the Father; and the Trinity - Father, Son, and Holy Spirit, one God - is simply the faith of the church, which we defended against every heresy we fought." then "We were born after the great council had settled that, and we never treated it as negotiable. To us it would be strange to hear it asked as an open question." (reordered; "that" and "it" now refer to Jesus being God). "That is near to the later language of punishment in our place without being identical to it" adds "of punishment in our place" to give "the later language" an antecedent after the question was removed. "Personal Lord and Savior was not our phrase."
- `attack-416` (story): "Who struck the blow, how many died, what was lost - the community itself chose not to say" became "The community itself chose not to say who struck the blow, how many died, or what was lost". Not a restated participant question; rewritten as a statement per the rule.

**Oblique judgment.** hal is not oblique by its sources. Its witnesses answer from Jerome's letters and prefaces and the Pelagian-era Dialogue, which state positions and deeds directly; where the sources are silent (the women's own words, eucharistic detail, a documented schedule) the records already say so in absent_detail and honest_limit records. No oblique shape was kept. If the Opus reviewer rules otherwise, that is an escalation, not decided here.

**Commentary removed from record bodies (not flagged by `tools/check_live_commentary.py`, removed under the live-surface rule):** the closing line "The text is written at the register bar: short sentences, everyday words; every claim, name, and reviewed constraint holds." (apostolic, authority, doubt, empire, jesus, one-church, practices, record, sin-grace, suffering); "The spoken field is written in plain modern English (mostly sentence-splitting ...)" (hell, marriage-ending, sin-grace, was-jesus-god); the label-pass notes ("epistula is labeled at the grief letter ...", "Hebraica veritas is labeled at the writings line ...", "The translation labor (Vulgata) is labeled at ... Claims are unchanged; the label is the only change.") in doubt, record and jesus; the cell-label headers ("F4-evidential answer-ground.", "F6-translational ... answer-ground", "Center-evidential answer-ground", "The Center cell's answer-ground.") from the first line of every edited witness body; in `one-church`, the attribution "the living-tradition determination and its doorway chrome are Mark's touchpoint, outside this record" was cut, and its scope clause kept in plain words: "Whether this world is a living tradition is not decided in this record." (OG-8 quotes both the old body note and the old `text` ("Is there a church today you could visit that is ours? No..."); the body now carries the clause above, and the text now reads "No church you could visit today is ours. No single door today opens onto us."; OG-8 itself is untouched and this entry is its cross-reference); in `hell`, "noted here for the later voice build"; in `attack-416`, "Re-derived from cleared Doc_09a S4, re-sourced on this branch to the full five-letter cluster." and the trailing "Serves F6-P.". **Kept:** the `hell` and `marriage-ending` body notes that a non-judgment line for the asker is a demonstration-stage requirement (`hell`) or deliverable (`marriage-ending`) in the world's own idiom, and that the witness supplies its substance (they describe the record, not a build step); `apostolic`, `practices`, `hal.dw.jesus` and others keep their source notes ("verified verbatim in the vendored text"), the `one-church` note on Dialogue I ch. VII and VIII, and the `was-jesus-god` note on near answers. The frontmatter `cell` tags (`F6-P` in `attack-416`) are schema fields and stay.

**Quotes.** No `quote` record was edited and no quotation inside a rewritten witness was altered or reordered; the edited sentences are paraphrase and the world's own voice, so no vendored-file re-verification was triggered. The quoted crowd murmur in `hal.story.rome-crisis` and the Cicero-dream verse were not touched.

**Known-wrong claims carried unchanged (OG-12):** `hal.dw.was-jesus-god` still says "a dying woman greeted his birthplace by name" (OG-12 item 2); `hal.dw.empire` still says the letter mocks clergy who "chase inheritances from wealthy widows" and "get up before dawn" (OG-12 item 5). Both are in sentences this pass left in place, and both go to the project lead; neither was fixed. Unedited witnesses with OG-12 items (`church-failure`, `inner-life`) were not touched. Separate observation: `records/worlds/hal.yaml` carries `living_tradition_flag: false`, while OG-8 states it was `true`; OG-8 is not updated here.

**Demonstration records (out of scope, left as they are):** every demonstration carries the participant question or questions it answers (`suffering` has two in one turn; `born-again` has two participant turns, the second with two questions). Two Representative replies also carry scaffolding of the kind removed from witnesses: `born-again` ("Would you like the honest version too - what happened after the turning?") and `hell` ("Here is what we held, without softening." and "Is one way too narrow?"). Out of scope; not edited.

**Gates (package `2026-10-07T01-25-20Z`, manifest `sha256:e8cab210e4d40ae3c0731bd23d6e068750124f940152ba734308b5d05b4d560b`; the earlier package of this pass was deleted):** `engine.m10.cli records hal` PASS; `engine.m10.cli regate hal --base origin/main` PASS (the first rebuild failed on FRE in `empire`, `hell` and `record`; fixed by splitting sentences, nothing widened); `engine.m2.cli determinism-check hal` PASS; `tools/check_live_commentary.py --base origin/main --enforce` exit 0; `engine.m10.cli deployed hal` PASS; embedded-quotation baseline test passes (hal 0, unchanged, so the baseline dict was not edited); `engine.m9.cli check` clean (every waiver live and current; no waiver count changed); `engine.m2.site_cli staleness-check` showed hal stale ("narrative") after the records edit, so the site JSON was recompiled in a second commit. `engine.m3.admission_conform` was not run (fails on any records change until the decision-58 gate change lands). No model call was made.

**Revision after review round 1 (2026-10-07):** `apostolic`, `marriage-ending`, `hell`, `practices` openers and the `one-church` and `hell` bodies were changed as described above; `was-jesus-god` "the answer" became "it". Package, pin and site JSON rebuilt.

**Merge with main and gate fix (2026-10-08):** main had taken OG-14 and OG-15 for the scaffolding-check and staging-reading entries, so this entry is OG-16. It resolves the hal scaffolding-check entry (Spoken text opens on a question or carries a stage direction, 2026-10-06). The `no-build-attribution` gate matched "not a ruling" in the `marriage-ending` opener written for review round 1; the opener now reads "Our answer was Fabiola rather than a ruling: divorced, she belonged here." Same claim, same order. The hal "spoken-scaffolding" waiver is removed from `engine/m1/cross_world.py`, because the scaffolding check finds nothing left for hal. Package `packages/hal/2026-10-08T05-12-13Z`, pinned in `records/worlds/hal.yaml` (manifest sha256:a41590ca7b9dd1ff2fc33b18bb9f08a4c6d2fa69807d7b9ff613264b60703610); site JSON recompiled.

**Status:** the records were cleared at round 2 (Opus, `Build/Ministry/Operations/Audits/hal_identity_scaffolding_review_round2_2026-10-08.md`).

## OG-17. **Voice errors found in the record pass staging reading, 9 October.**

Errors in the voice's replies in the named, capped live test "record pass staging reading, 9 October" (decision 56): six questions put to this world's Representative in one conversation on main at 691d2daa, after the identity-first, no-scaffolding record pass. Each item was traced against this world's records by an independent Opus check. The replies are in `engine/m4/reports/live-turn-report-hal-2026-10-09-record-pass-staging-reading.json`. Not fixed; content for this world's build thread. Items use the five defect classes of the voice-errors entry of 2026-10-07: (A) altered words inside quote marks or in a line given as a figure's own words; (B) scripture or creed quoted or listed with no record behind it; (C) a demonstration record recited word for word; (D) record text pasted near word for word, including a record's own scripted question; (E) a misstatement against a specific record; and three more: (F) a question opener or stage direction; (G) the voice outside its own years or outside the we-voice; (H) rhythm against decision 60 (quote or name pacing, a quote or story repeated rather than referred back to, a lexicon mark repeated). A class not listed did not occur in this world. In this run 16 sentence(s) the grounding net marked "withhold" still reached the reply text: `grounding_net.shown_text` takes the quotation marks off but keeps the sentence, and `sentence_enforce` is off. Decision 59(1) says such a sentence is withheld. This is a fleet-level engine finding, raised with the project lead, not a record defect of this world.

(1) (A) "Who is Jesus?": the voiced greeting ends "where the Bread that came down from heaven was first born". `hal.quote.hail-bethlehem` reads "was born", so 'first' is added, and the reply cites only `hal.dw.jesus`, not the quote record (decision 59 clause 2).

(2) (A) "Why did your people believe this?": the voiced quote reads "with much toil and effort I partially acquired a knowledge of Hebrew". `hal.quote.partially-acquired-hebrew` renders it "with much toil and effort partially acquired the Hebrew tongue".

(3) (D) "Who is Jesus?": outside one inserted attribution sentence and the voiced quote, the reply is `hal.dw.jesus` near word for word. "What did he do?" repeats most of `hal.dw.record` word for word ("copied, compared, corrected, and translated from the Hebrew we held truest"; "Our confidence stood on three things..."). This is the 7 October item (D) unchanged.

(4) (D) "Tell me about someone who lived this out": the reply closes with "Those are the answers we give, and our sobs come with them. We kept both on purpose.", pasted from the last lines of `hal.dw.suffering`, where 'those answers' refers to judgment, reward and the safety of the dead, none of which this reply names.

(5) (D) "What would you want me to understand that I haven't asked?": "Our own prior position-taking is part of why this force found this target" copies the analytic description of `hal.force.pelagian-attack` into the voice.

(6) (E) "What did he do?": "We were born more than three and a half centuries after the events" misstates `hal.dw.record`, which says "More than three and a half centuries stood between us and the events". Jerome (c. 331/347) and Paula (347) were born about three centuries after them (`hal.figure.jerome`, `hal.figure.paula`).

(7) (E) "What does Hebraica veritas mean?": "He claimed he learned it as an older man, with great toil and effort" reverses `hal.quote.partially-acquired-hebrew`, where Jerome says he began "as a young man".

(8) (E) "What does Hebraica veritas mean?": "His critics doubted that claim then" has no record behind it. `hal.contested.hebrew-fluency` names a modern scholar (Williams, 2006) as the doubter and cites a contemporary, Sulpitius Severus, only for Jerome's reputation.

(9) (E) "Why did your people believe this?": "Out of that crucible... came a sharper insistence: the Hebrew stands closest to what was given" ties the Origenist quarrel to the Hebrew principle. Neither the cited `hal.story.rufinus-rupture` nor `hal.term.hebraica-veritas` says this.

(10) (G) "What does Hebraica veritas mean?": "and scholars contest it still" speaks from the present, outside this world's years (382-420, `hal.core.hieronymian`).

(11) (H) "Tell me about someone who lived this out": two new figures, Marcella and Eustochium, appear in one round, one round after Rufinus and two after Augustine. A voiced quote comes one round after the previous one (decision 60 clauses 1 and 2).

(12) (H) "What would you want me to understand that I haven't asked?": the `hal.quote.house-destroyed` line voiced in the previous reply is voiced again in full, and the 416 fire is told again rather than referred back (decision 60 clause 1 and its 7 October referring-back refinement).

Status: OPEN.

## OG-18. Voice claim corrections after the record pass staging reading, 2026-10-09.

Closes the Jerome item of "Voice errors found in the record pass staging reading, 9 October": items (7) and (10), the Hebrew claims in the reply to "What does Hebraica veritas mean?". Review: `Build/Ministry/Operations/Audits/hal_voice_claim_corrections_review_2026-10-09.md` (Opus 5.5, one review).

**Changed.**
- `hal.quote.partially-acquired-hebrew` `use_note.means`: now says Jerome "began Hebrew as a young man, had only partially acquired it through long toil, and kept studying it lest he lose it". Before, it said only that he "had only partially acquired Hebrew through long toil", with nothing on when he began. The quote `text` is untouched and already says "beginning as a young man". Item (7), "learned it as an older man", has no record behind it that says so; the use note gave the voice no start date, so it now states Jerome's own account.
- `hal.core.hieronymian` `cautions`, caution 4: the phrase "contested in modern scholarship" is replaced by "an open question (hal.contested.hebrew-fluency). The Representative gives only his own words: he began as a young man and partly acquired it. Never state his fluency as settled. The modern dispute is for the Facilitator." The old phrase was outside-the-world scholarship in a record the Representative draws on, and it is the likely source of item (10), "scholars contest it still". The reply tagged this record for that sentence.
- The same `cautions` field was reworded in full, same eight points and no new claim, in shorter sentences. The regate gate treats any edit to a field as a new field, and the old field was at FK 14.1 and FRE 32.1, so it could not be edited alone.

**Not changed.**
- `hal.contested.hebrew-fluency` stays in its etic register with formation_confidence Contested. The Facilitator may say the contest directly. No other record states the contest to the Representative.
- `hal.term.grammaticus` carries "seriously contested" in `false_friend`, and `hal.figure.jerome` carries "per Williams" in its body. Both are for the builder and the Facilitator, not spoken text, and neither says "older man". Left as is.
- Item (8), "His critics doubted that claim then", is a separate item and is not closed here; `hal.contested.hebrew-fluency` names only Williams (2006) and, for reputation, Sulpitius Severus.
- Quote `text` and every `modern_rendering` are untouched. `hal.quote.partially-acquired-hebrew` `modern_rendering` ("I began as a young man and with much toil and effort partially acquired the Hebrew tongue...") agrees with the text; no change needed.
- Items (1) to (6), (8), (9), (11), (12) of the 9 October entry are not touched by this entry.

**Engine item for the fidelity slice.** The words "older man" come from no record, and the voice also altered the quoted line (item (2)). That is the voice's own error against a clear record. The sentence "scholars contest it still" was withheld by the grounding net but still reached the reply text (sentence_enforce is off); this is the fleet-level finding already raised in the 9 October entry.

**Gates.** `python -m engine.m10.cli records hal` and `python -m engine.m10.cli regate hal --base origin/main`: pass. `python -m engine.m2.cli determinism-check hal`: pass. `python -m engine.m2.cli staleness-check`: no world stale. `python -m engine.m9.cli check`: clean after the hal readability waiver in `engine/m9/enforce.py` went stale and was tightened from 161 to 159 (the `cautions` rewrite cleared two failures); `python -m pytest engine/m9/tests`: pass. `tools/check_paths.py` against its baseline and `tools/check_live_commentary.py --base origin/main --enforce`: pass. Package rebuilt after the last record edit: `records/worlds/hal.yaml` pins `packages/hal/2026-10-09T00-26-08Z`, `manifest_hash` `sha256:3523f325311735e6882f19ae7032858aa660edee89ef8d848ca5d86a19ec226a`.

Status: CLOSED for the Jerome item. The 9 October entry stays OPEN for its other items.

## OG-19. Record wording pass on hal's spoken fields and source citations, 2026-10-13.

Method: every spoken field audited against the record's cited source and the vendored text; fixes applied by record; two Opus reviews (`Build/Ministry/Operations/Audits/hal_record_audit_fixes_review_round1_2026-10-13.md`, `..._round2_2026-10-13.md`). All changed spoken fields score FK 10 or below and FRE 60 or above. Quote `text` is unchanged in every record. Build records (force, gravity, voice_craft, world_core, contested_claim) are not changed. Waivers: `m1:readability/hal` tightened from 159 to 102 (what remains is in `positions`, force, gravity, contested_claim, world_core and voice_craft fields, which this pass does not change); `m9:source-citation/hal` (28) deleted.

**Source records.** All 28 `hal.source.*` records gain a one-line `citation:`; the `m9:source-citation/hal` waiver is deleted.

**Changed, by record** (record | fields | category | source checked).

- hal.dw.apostolic | text | drift (minor), tell | Ep 22 secs 21, 36; Ep 127 sec 5; Against Jovinianus Bk I; Ep 48 intro (friends thought virginity was set above marriage). Claim that baptism, eucharist and scriptures were "traced to the apostles" cut entirely (audit proposed softening it to "we took them as the apostles' gift"; no cited passage supports even that, so the more conservative option was taken). "Went beyond scripture" replaced by the Ep 48 wording. Two stacked not-X-but-Y lines merged.
- hal.dw.authority | text | drift, tell | Apology (vi.xii) and Rufinus (vi.xi) checked for how the quarrel ended (nothing) and for Nicaea (no hit); Apology Bk II sec 5 line 146 "You confess a Trinity in one Godhead. The whole world now confesses this." Cut: "ended by exhaustion and death"; "council rejected a new teaching". "exactly" trimmed.
- hal.dw.believe | text | drift, tell | Ep 22 sec 30 (after the dream he read God's books with greater zeal); Ep 77 secs 3, 4, 6 (censure of the second marriage; "all Rome" belongs to the penance; sold property, founded hospital, carried the sick). Cut: "beginning of his life with God"; "all Rome knew it"; the quotable "not an argument" closer was replaced by a plain statement.
- hal.dw.church-failure | text, sources[] (added hal.source.vulgate-prefaces, hal.source.jerome-ep45) | drift, confidence, tell | Ep 22 sec 28; Apology Bk I line 54 ("if I am a little too sharp upon heretics"; "You should rejoice in my invectives"); Ep 45; Ep 135 intro ("pillaged and partially burned"); attack-letters-416 (attackers' number Inferential-Thin). "driven out of Rome by slander, as he told it" hedged; "mob" became "other Christians". Cut: "most of it"; "clay jars" closer.
- hal.dw.doubt | text | contradiction, drift | Ep 39 secs 5-6 (rebukes as well as pardons the grief); Ep 127 sec 7 (Marcella; "to learn the answers to those objections which might, as she saw, be made"). "Most learned woman in Rome" replaced by "Marcella, a widow in Rome". Letter now pardons the tears and also asks her to hold the grief in check.
- hal.dw.empire | text, sources[] (added hal.source.jerome-vita-malchi, hal.source.jerome-ep108) | drift | Ep 22 sec 28; Vita Malchi prologue sec 1 (vi.iii: church grew by persecution, then in wealth, decreased in virtue); Sulpitius Dial. I.8-9 (one traveler, six months); Ep 108 secs 3-4, 19, 27; Ep 127 sec 2. Cut: "bishops ate dinner with senators"; "crowded"; "grandparents"; "inheritances from widows"; "most eligible"; "senators' daughters".
- hal.dw.hell | text, sources[] locus (apology-rufinus) | confidence, drift, tell | Apology Bk I secs 25-27 (charge and answer); Bk II sec 12 (renunciation); Against the Pelagians (vi.ix) sec 28 ("mercy is sometimes blended with the threatenings of God"; penitence "a copy of the grace of baptism"; no sitting in judgment before the day). Rufinus's charge now stated as a charge. Cut: "one certainty was hope"; "no lists of the lost"; "pearl"; "map" closer.
- hal.dw.inner-life | text, sources[] locus (jerome-ep22 now includes sec 37) | drift, tell | Ep 22 secs 7, 37; Ep 125 sec 11 (verbatim: work for the hands; love the knowledge of scripture). Cut: "banquets and dancing girls" (now Ep 22 sec 7 wording); "we prayed through deaths we had begged God to prevent"; not-X-but-Y pivots and moral tag.
- hal.dw.jesus | text | tense, tell, drift | Ep 108 sec 10 (Paula: "I could behold with the eyes of faith the infant Lord"; "Hail Bethlehem, house of bread"). Past tense for community belief. Cut: "deepest devotion has the shape of that choice"; "doctor who receives the broken" (Apology Bk I sec 26 is about restoring the Church, not penitents). "within sight" became "near the cave"; Paula's sight now attributed to Jerome.
- hal.dw.marriage-ending | text, sources[] locus (jerome-ep77 now secs. 2-6, 11) | drift, contradiction (minor), locus | Ep 77 secs 2, 3, 4, 11 (funeral). Cut: "a senator's daughter"; "above almost everyone"; "did not defend herself / unforced" (now "She confessed her fault herself").
- hal.dw.practices | text, sources[] (added hal.source.jerome-ep22 sec 30, hal.source.jerome-ep77 sec 4, hal.source.jerome-against-pelagians) | contradiction, drift, locus | BORN AGAIN: the sources support the phrase as the world's own word for baptism. Against the Pelagians (vi.ix): "by being born again and incorporated into our Lord", John 3:3 quoted; also Ep 125 "born again in Christ", Ep 22 "I am born anew in Christ", Against Jovinianus "born again in baptism". The text now says "Born again was our word for baptism." The demo applier should match: the old line "Born again is not our phrase" is wrong and must not survive in the demo. Also: "tenth would sound timid", "giving was a direction", "urged to decide for more" cut ("We did not tithe" kept as an absence; no hit for tithe in the volume); Ezekiel preface (vii.iv line 63) checked; "translating" became "writing".
- hal.dw.record | text | drift, tell | Ep 108 secs 9-10; prefaces. "three and a half centuries" became "more than three centuries"; cut "No one among us had ever known an eyewitness"; "unbroken" dropped; "Nothing was received passively" cut; "We knew the resurrection" recast as "We held the resurrection to be true".
- hal.dw.sin-grace | text, sources[] (added hal.source.jerome-against-jovinianus, Book II) | drift, tell, locus | Against Jovinianus Bk II (vi.vi): "guilty of the body and blood of the Lord"; Against the Pelagians (vi.ix) for Adam and infant baptism. Cut: "received with fear and love"; "grace against the proud and works against the idle"; "We refused both easy halves."
- hal.dw.suffering | text | confidence, contradiction, drift | Ep 39 secs 5-6 ("killed with fasting" is the crowd's whisper; whispers to drive out, stone, or throw monks in the Tiber; rebukes the grief as well as pardons it); Ep 127 sec 13 ("she is said to have": hearsay, hence "or so Jerome was told"); Ep 135 intro ("pillaged and partially burned"); Ep 127 sec 14 (Marcella dies smiling); hal.story.rome-crisis not_for (no certain cause of Blaesilla's death). Cut: "never called the weeping faithlessness"; "grieving hardest"; "on purpose".
- hal.dw.was-jesus-god | text, sources[] locus (apology-rufinus) | locus, drift | Apology Bk II secs 3-5, 15 (Trinity exchange; homoousion), Bk I sec 26 (true physician); Ep 22 sec 25; Ep 108 sec 10; Ep 22 for "redeemed by the blood of Christ". Cut: "ransom", "debt of sin paid", "a penitent as her physician", "dying woman" (Paula greets Bethlehem alive; now "a widow"). Locus 'Book I' corrected.
- hal.story.attack-416 | text | tell (coined closer removed) + drift; readability | Ep. 137 (clemency; "untold the name and motive"), Ep. 138, Ep. 139, Ep. 136. Ends on the attested gap (only the pope's account).
- hal.story.ciceronian-dream | text | drift (invented "whole life" claim, imagery) + tell | Ep. 22 sec. 30; Rufinus Apology vi.xi (the jibe about Cicero).
- hal.story.day-at-monastery | text, tellable_as, sources[0].locus ("secs. 19-20" -> "secs. 14, 20") | drift (wool-work, distaff, bells, dictation, visitors, senators' daughters invented) + contradiction (discipline case, sick allowed meat); readability | Ep. 108 secs. 14, 20; Sulpitius Dialogues I.9. Text states no hours, so it stays consistent with the existing claim_guard.
- hal.story.desert-romances | text, tellable_as | drift + confidence (romance-genre and read-aloud claims removed, per lead decision); readability | Vita Malchi (npnf206 vi.iii: "history of chastity for the chaste"); Hilarion headnote (vi.ii).
- hal.story.journey-to-bethlehem | text, tellable_as, sources[0].locus ("secs. 7-14" -> "secs. 6-14") | drift + tell + locus; mismatch (tellable_as named Jerome); readability | Ep. 108 secs. 6, 7, 10, 14, 35.
- hal.story.marcella-death | text | drift (invented hope, shared grave, "thirty years", garbled thanksgiving) | Ep. 127 secs. 12-14. One audit clause ("since her poverty was her own choice") dropped on re-read as not in the letter.
- hal.story.marcella-standing | text, sources[0].locus ("secs. 2-8" -> "secs. 2-10") | confidence + drift + locus | Ep. 127 secs. 2, 7, 9-10.
- hal.story.oea-gourd | text, tellable_as | drift + tell (invented aphorism and closing verdict removed); readability | Augustine Ep. 71 sec. 5; Jerome reply = Letter LXXV sec. 22 (npnf101).
- hal.story.paula-epitaph | text, tellable_as | contradiction ("not one coin" reversed: she died in debt) + drift (age 32, stewards, "poor of the countryside"); readability | Ep. 108 secs. 1, 2, 5, 15, 26, 30, 31.
- hal.story.rome-crisis | text, tellable_as | tell (coined closer) + drift ("never saw Rome again" removed); readability | Ep. 39 secs. 1, 6; Ep. 45 secs. 2-3; Ep. 108 sec. 6.
- hal.story.rufinus-rupture | text, tellable_as | drift + tell + readability (FK 14.4 -> 6.8) | hal.figure.rufinus; Rufinus Apology; Jerome Apology (npnf203); Rufinus volume headnote.
- hal.story.translating-a-book | text, tellable_as | contradiction (Ep. 57 excepts scripture from sense-for-sense) + drift (twenty years, patron's purse, invented request wording); readability | Ep. 57 sec. 5; Vulgate OT dates (npnf206 vii.iii); Apology Against Rufinus (Baraninas, night, expense). Audit's invented request wording ("translate this book again, from the Hebrew") dropped as unsourced; "at great cost to the translator" kept.
- hal.limit.f5-enslaved | statement | drift (overstated silence) + contradiction ("held many people" vs "small" household) | Ep. 108 secs. 2, 10; Ep. 39 sec. 1.
- hal.limit.f5-women-own-words | statement | contradiction + confidence (Ep. 46 survives under their names, held to be his) | Ep. 46; Ep. 137; hal.contested.ep46-authorship.
- hal.limit.martyrdom | statement | contradiction (minor; "one attack" count) | Ep. 137; hal.story.marcella-death (Ep. 127 secs. 13-14).
- hal.demo.believe | exchange[1] (representative) | tell, drift | Ep. 22 sec. 30 (Judge, Cicero, treasure); Ep. 77 secs. 4, 6 (Fabiola). Removed invented opener and the unsourced "beginning of his life with God" reading; replaced with the sourced act (he gave himself to the Scriptures); shortened a repeated "not an argument" line.
- hal.demo.born-again | exchange[1] (representative) | contradiction, drift, tell | hal.dw.practices; Ep. 108 secs. 3, 6; Pelagians dialogue (vi.ix), Ep. 22, Against Jovinianus. Removed unsupported "close to how we would put it" and "Born again is not our phrase" (sources show the phrase was used for baptism). Now: "Born again was our word for baptism, the washing that makes a person new." Managers became relatives (Ep. 108 sec. 6); removed coined "two halves" line and the "honest version" hand-back.
- hal.demo.born-again | exchange[3] (representative) | contradiction, drift, tell | Ep. 22 sec. 30; hal.story.ciceronian-dream. "Our founder" became "Our teacher Jerome"; "way to the desert" became "way to Jerusalem", "could not give up his library"; removed invented closers ("put to work inside the new life", "Nobody among us stopped struggling").
- hal.demo.hell | exchange[1] (representative) | tense | hal.dw.hell. "we do not apologize" became "we never apologized".
- hal.demo.jesus | exchange[1] (representative) | tense | Ep. 108 sec. 10 (quote checked, accurate). Community devotion put in past tense; "He was" became "He is".
- hal.demo.marriage-ending | exchange[1] (representative) | drift | Ep. 77 sec. 2. "a senator's daughter" became "a woman of the old Fabian family".
- hal.demo.someone-like-me | exchange[1] (representative) | drift, tell | Ep. 39 (crowd's charge of death by fasting); Ep. 77 secs. 6, 10; Ep. 108 sec. 14. Death-by-fasting charge given to the crowd, "her teachers had praised" removed; "voices in the crowd"; Egypt/Parthia/Britain line attributed to Jerome without same-year claim; unattested "asked nothing of anyone's learning" replaced with a statement of what the records say; coined closer replaced.
- hal.demo.suffering | exchange[1] (representative) | tell | hal.dw.suffering; Ep. 127 sec. 12; Ep. 137; Ep. 139. Filler "we tell you honestly" removed.
- hal.demo.woman-authority | exchange[1] (representative) | confidence, drift, tell | Ep. 127 sec. 7 (single post-mortem source, Contested). Framed as "The one account we have says"; "house" removed; "citing" became "mindful of"; overclaims reworded.
- hal.demo.women-own-words | exchange[1] (representative) | drift, tell | Ep. 127 sec. 7; Ep. 108 sec. 26. "her house" removed; "you deserve it stated" replaced.
- hal.figure.augustine | bridge_line | readability, tell | Ep. 112; hal.source.jerome-augustine-letters
- hal.figure.blaesilla | bridge_line | drift, readability | Ep. 108 sec. 3; Ep. 39 ("eldest" removed; "severe fasting" reworded)
- hal.figure.damasus | bridge_line | drift, readability | Gospels preface (a.d. 383); figure body (protection ended with his death)
- hal.figure.eustochium | bridge_line | tell, readability | Ep. 22; Ep. 108
- hal.figure.fabiola | bridge_line | readability, tell | Ep. 77 secs. 4-6
- hal.figure.jerome | bridge_line | readability, tell | hal.gravity.patronage-authority ("never on a bishop's seat")
- hal.figure.marcella | bridge_line | confidence, readability | Ep. 127 sec. 7; figure body (attributed to Jerome; "the one" and flat founder claim removed)
- hal.figure.pammachius | bridge_line | readability | Ep. 66; Ep. 77 sec. 10
- hal.figure.paula-younger | bridge_line; names[0] (in-world name "Paula" became "Paula the younger", per lead decision) | drift, readability; contradiction (label collision with hal.figure.paula) | Ep. 107; Ep. 137
- hal.figure.paula | bridge_line | confidence, readability | Ep. 108 (attributed "By Jerome's account")
- hal.figure.rufinus | bridge_line | drift, readability | NPNF headnote v.vi.vii; Apology; hal.story.rufinus-rupture
- hal.term.bibliotheca | plain_meaning, quick_meaning, senses.personal, senses.translational | readability; tell; drift | Vulgate prefaces (npnf206 vii.iii/iv); divergence_note and use_note (no size claimed)
- hal.term.epistula | quick_meaning, senses.personal, senses.translational | readability; tell; drift | Ep 22, 45, 77, 108, 127 (npnf206); no "far from everyone I love" line, no source for "written to be copied and shared"
- hal.term.epitaphium | quick_meaning, senses.translational | readability; confidence; tell | Ep 108, Ep 127 (no source for "ancestor to all three")
- hal.term.exegesis-as-practiced-authority | plain_meaning, quick_meaning, senses.personal, senses.translational | confidence; tell; readability | Ep 127 sec. 7 (npnf206); divergence_note (single witness)
- hal.term.grammaticus | plain_meaning, quick_meaning, sources[] locus | readability; locus | Apology against Rufinus I ch. 16 (npnf203 div vi.xii), "my master Donatus". Added hal.source.jerome-apology-rufinus with locus "Book I, ch. 16 ('my master Donatus' on Virgil)"; hal.source.jerome-de-viris locus re-described as "ch. 135, Jerome's own entry listing his works (does not mention Donatus)"
- hal.term.hebraica-veritas | plain_meaning, quick_meaning | tense; readability; confidence | use_note not_for (Jerome's single voice)
- hal.term.matrona | senses.translational | drift; readability | Ep 108 secs 1, 3-4; Ep 127 secs 1-2 (no legal status stated)
- hal.term.monasterium | plain_meaning, quick_meaning, senses.personal | drift; readability; contradiction | Ep 108 sec. 10 (cave, Jerome prays there), sec. 20 (monastery for men; virgins in three companies meeting for psalm-singing and prayer), sec. 23. plain_meaning uses the audit's suggested wording (men's house, women's house in three companies, one project; Paula then Eustochium led the women; Jerome-as-men's-leader claim removed). quick_meaning shortened to "It had a men's house and a women's house, under one project" (drops "linked").
- hal.term.nosocomium | senses.personal, senses.translational | drift; tell | Ep 77 sec. 6; sec. 6 "first person to found a hospital"
- hal.term.patrocinium | senses.personal | drift; confidence; tell | Ep 45 secs 2-3 (Damasus; "worthy of the episcopate"); letter header Aug 385, Ostia
- hal.term.pelagianism | plain_meaning, quick_meaning, senses.personal, senses.translational | drift | Epp. 135-139; Ep 137 ("These ladies tell me"; ravages, murders, fires); Ep 138 (Jerome chose to leave); hal.source.attack-letters-416. Kept "words" (not "letter") per lead.
- hal.term.peregrinatio | quick_meaning, senses.personal, senses.translational | readability; drift; tell | Ep 108 secs 7-14 (sec. 10 "eyes of faith" at the manger; sec. 14 "accompanied by Eustochium and many")
- hal.term.praeceptor | plain_meaning, senses.personal, sources[] locus | readability; drift; tell; locus | Apology against Rufinus I ch. 16 (npnf203 div vi.xii). Added hal.source.jerome-apology-rufinus with locus "Book I, ch. 16 ('my master Donatus' on Virgil)"; de-viris locus re-described as for grammaticus
- hal.term.praefatio | quick_meaning, senses.personal, senses.translational | readability; confidence; tell | Vulgate prefaces (npnf206 vii.iii/iv); evidential sense and use_note (single-voice source)
- hal.term.propositum | quick_meaning, senses.personal | readability; confidence; tell | Ep 22; evidential sense (term not used in Ep 22); Dominant Modern Reconstruction
- hal.term.scriptorium | plain_meaning, senses.personal | readability; confidence | Ep 108 (no room named); Dominant Modern Reconstruction
- hal.term.vidua | plain_meaning | contradiction | Ep 77 secs 2-6 (Fabiola remarried, widowed again); Ep 127 sec. 2 (Marcella refused Cerealis); Ep 108 (Paula)
- hal.term.virginitas | plain_meaning, quick_meaning | readability | no source change
- hal.term.vulgata | senses.personal | drift | Vulgate prefaces (npnf206 vii.iii/iv); editor note, preface to Paula and Eustochium, c. 391
- hal.term.xenodochium | plain_meaning, senses.personal | readability; drift | Ep 77 sec. 10 (Portus); Ep 108 sec. 14 (guest house, cells, monastic buildings); Ep 84 (Hebrew teachers' cost was Jerome's own)
- hal.quote.a-follower-of-cicero-and-not-of-christ | modern_rendering | dropped words, dropped closing ellipsis, 27-word sentence | npnf206 Ep. 22 sec. 30, lines 6480-6484
- hal.quote.a-man-truly-catholic | modern_rendering | overstatement ("almost"), "at first" lost, misleading modern sense ("Catholic" rendered "orthodox" per lead decision) | npnf211 Sulpitius Dial. I.7, div ii.iv.i.vii
- hal.quote.detestable-monks | modern_rendering | "all along" for "often" | npnf206 Ep. 39 sec. 6
- hal.quote.dispute-to-learn | modern_rendering | words added from outside the excerpt ("about the scriptures" removed, "them" kept per lead decision), 30-word sentence, "acquiesce" | npnf206 Ep. 127 sec. 7 area (line 26165 is the sentence before the excerpt)
- hal.quote.ever-let-the-bridegroom-sport-with-you | modern_rendering | 40-word sentence, dropped closing ellipsis, ungrammatical phrase | npnf206 Ep. 22 (Bridegroom passage)
- hal.quote.eyes-of-faith | modern_rendering | padding and changed attribution ("protested in my hearing"), added words | npnf206 Ep. 108 sec. 10
- hal.quote.fabiola-hospital | modern_rendering | purpose clause turned into fact, misleading modern sense ("want" -> "poverty") | npnf206 Ep. 77 (Fabiola hospital passage)
- hal.quote.hindered-by-jerome | modern_rendering | readability fail (FRE 58.5 -> 77.6), added "instead" | palladius_lausiac-history_clarke1918.txt line 475
- hal.quote.innocent-ravages | modern_rendering | readability fail (FRE 53.1 -> 63.2), misleading modern sense ("deplored" -> "lamented"), causal "for" reversed | npnf206 Ep. 137 (div v.CXXXVII)
- hal.quote.they-have-left-untold-the-name | modern_rendering | readability fail (FRE 56.3 -> 63.2), "deplored" lost, causal "for" reversed; same text as innocent-ravages, same replacement | npnf206 Ep. 137 (div v.CXXXVII)
- hal.quote.no-one-preferred-to-the-seventy | modern_rendering | AI-tell framing pivot ("judge one thing:"), added emphasis, 36-word sentence | npnf102 City of God XVIII.43, line 36742
- hal.quote.oea-tumult | modern_rendering | 38-word sentence with dash insert | npnf101 Aug. Ep. 71 Chap. III sec. 5, line 32550
- hal.quote.paula-escaped-his-envy | modern_rendering | dropped "to such a degree that" | palladius_paradise-v1-syriac_budge1907.txt line 1233
- hal.quote.recourse-to-marcella | modern_rendering | asserted an outcome the source does not give | npnf206 (Marcella recourse passage)
- hal.quote.rome-resounded | modern_rendering | readability fail (FRE 55.2 -> 68.8) | npnf206 Ep. 45 sec. 3
- hal.quote.rufinus-writes-because-rome-is-where-the-news-is | modern_rendering | AI-tell framing pivot ("one thing:"), added causal link ("and so"), dropped "favourably" | npnf203 div vi.ix sec. 1
- hal.quote.she-put-on-sackcloth | modern_rendering | "yoke of restraint" for "yoke of servitude", added "instead", two 32-33-word sentences | npnf206 Ep. 77 sec. 4
- hal.quote.let-her-be-brought-up-in-a-monastery | sources[0].locus (secs. 4-7 -> sec. 13) | locus | npnf206 line 20723 (v.CVII-p74, "13.") and line 20730

**Changed after review round 1** (record | field | change).

- hal.story.journey-to-bethlehem | text | BLOCKING: removed unsourced spring clause; harbor at Portus
- hal.dw.practices | text | NB1: born-again now a thing that happens in baptism
- hal.dw.practices | sources[against-pelagians].locus | NB1: narrowed locus
- hal.demo.born-again | exchange[1] | NB1: matched dw.practices wording
- hal.demo.born-again | exchange[3] | NB2: cut coined closer
- hal.demo.someone-like-me | exchange[1] | NB3: ascetic life; crowd said fasting killed her
- hal.demo.someone-like-me | exchange[1] | NB3: cut redundant open-to-stranger sentence
- hal.dw.was-jesus-god | text | NB4: cut true-physician sentence
- hal.dw.was-jesus-god | sources[apology-rufinus].locus | NB4: dropped Book I sec. 26
- hal.dw.was-jesus-god | sources[jerome-ep22].locus | NB4: added sec. 39
- hal.dw.inner-life | text | NB5: cut Ep125 sentence
- hal.dw.empire | text | NB6: with the sun
- hal.dw.empire | text | NB6: one woman, not a class
- hal.demo.hell | exchange[1] | NB7: matched dw.hell (charge and answer)
- hal.demo.suffering | exchange[1] | NB7: pillaged and partly burned
- hal.demo.suffering | exchange[1] | NB7: Marcella thanks wording per Ep127 sec 13
- hal.demo.jesus | exchange[1] | NB7: cut unsourced doctor sentence
- hal.demo.marriage-ending | exchange[1] | NB7: matched dw.marriage-ending
- hal.story.rome-crisis | text | NB7: dropped eldest
- hal.story.oea-gourd | sources[augustine-letters].locus | NB8: proposed locus
- hal.story.oea-gourd | sources[jerome-augustine-letters].locus | NB8: reduced locus
- hal.figure.marcella | bridge_line | NB9: softened Roman clergy
- hal.term.monasterium | plain_meaning | NB10: reworded
- hal.term.monasterium | sources[jerome-ep108].locus | NB10: added sec. 10
- hal.story.desert-romances | text | NB11: cut repeated closer
- hal.term.grammaticus | sources[jerome-de-viris].locus | NB12: removed reviewer note
- hal.term.praeceptor | sources[jerome-de-viris].locus | NB12: removed reviewer note
- hal.quote.rufinus-writes-because-rome-is-where-the-news-is | modern_rendering | NB13: restored hedge

Round 2 (targeted recheck, Opus): passed, 0 blocking. Two non-blocking items, double spaces in three spoken fields (fixed) and two unlogged build-field alignments (logged in OG-20).

Status: CLOSED for the fields listed; the open items are in OG-20.

## OG-20. Items found in the hal record wording pass and not fixed, 2026-10-13.

Each item is outside the fields this pass may change (build records, `positions`, `use_note`, `informational`, source records, body paragraphs) or needs a source record or a decision. Entry numbers cited elsewhere are by subject and date.

- hal.dw.apostolic | sources[] | The friends' objection rests on Ep 48 (Pammachius and friends); no records/hal/source record exists for Ep 48 (nearest: jerome-ep45, jerome-ep46, jerome-ep57). Source record needed; not created.
- hal.dw.apostolic | positions[1], tensions, use_note | Repeat "went beyond scripture", which the Ep 48 intro does not support. Out of scope (not spoken). Owner to align.
- hal.dw.inner-life | sources[] | Ep 125 sec 11 carries "work for the hands" and "love the knowledge of scripture" (verified verbatim) but has no source record. Needs a new source record; not created.
- hal.dw.practices | sources[] | hal.source.jerome-ep107 (secs. 4-13) is still listed although the audit found the text does not use it. Left in place (removing a source is a judgment for the owner; conservative option). Also: "Against Jovinianus ... born again in baptism" and Ep 125 / Ep 22 "born anew" are corroboration only; the Against the Pelagians locus is given as a descriptive phrase because the audit gives no section number.
- hal.dw.practices | positions[0], use_note | Say "born again" was carried by other words. Contradicts the text now. Out of scope (positions not spoken); needs aligning. positions[1] "never a tithe system" is unsourced (no hit for tithe), same status.
- hal.dw.doubt | positions[1], use_note ("not condemnation") | Ep 39 rebukes the grief as well as pardoning it. Out of scope; owner to align.
- hal.dw.suffering | positions[1] ("never condemned as unbelief") | Contradicted by Ep 39. Out of scope.
- hal.dw.hell | positions[1] ("hope in every particular case") | No source. Out of scope.
- hal.dw.was-jesus-god | positions[1] ("redemption and healing") | Fine, but "ransom" is not attested in the sources. Out of scope.
- hal.dw.sin-grace | positions[3] ("against idleness") | Unsourced. Out of scope.
- hal.dw.one-church | text | Audit note only: the definition of "Catholic", "Latin monastery in a Greek-speaking province" and "ended within a generation" are world-level framing, not in the cited loci. Low risk; no change.
- hal.dw.one-church | sources[] jerome-apology-rufinus locus "the professions of catholic faith throughout" | Audit found no such professions in Book I; the audit proposed no fix for this record. Left; needs a locus check by the owner.
- hal.dw.church-failure | text "mocked a former friend after the man had died" | Rests on the Ezekiel Bk I preface (vii.iv, "the scorpion lies beneath the ground"); the editor identifies the Scorpion as Rufinus only at the Bk X preface. The identification is an inference. Kept per the audit, locus added; owner may wish to tag it.
- hal.dw.* positions | the 26 optional readability replacements in the audit | Not applied (outside scope: `text` only).
- hal.story.oea-gourd | sources[1].locus ("Ep. 112 (the reply)") | Not edited, per lead instruction to list the oea-gourd locus fix as unfixed. Audit's suggested locus: "Ep. 112 (= Augustine collection Ep. 75), sec. 22; text vendored at cic/texts/npnf101_augustine-confessions-letters.xml, Letter LXXV". Note the string sits in the story record's sources[]; it can be applied there on instruction. The source record hal.source.jerome-augustine-letters (edition field npnf206 v.CXII, a headnote only) also needs its owner to correct it.
- hal.story.day-at-monastery | absent_detail, claim_guards, modern_contrast, narrative_tier_justification, use_note | Build fields, out of scope. They say no hours are attested, but Ep. 108 sec. 20 names the hours (dawn, third, sixth, ninth, evening, midnight). They also list "wool-work", which Ep. 108 does not support. Owner to resolve. Story text states no hours meanwhile.
- hal.story.translating-a-book | use_note (and any other field repeating "sense-for-sense is Ep. 57's own stated theory") | Build field, out of scope; Ep. 57 sec. 5 excepts scripture.
- hal.story.desert-romances | modern_contrast, absent_detail, use_note (and formation_confidence Inferential-Thin) | Build fields, out of scope; they repeat the romance-genre claim, which the vendored edition cuts against (Hilarion headnote: "destitute of foundation"; Malchus: "history of chastity"). Governance question for the owner: can "consciously literary romances" stand?
- hal.limit.f5-material-remains | statement | No change; verified against Ep. 108 secs. 14, 30, 34. Flag: the negative claim ("no stone, coin, or record traced with certainty") cannot be checked from vendored texts or hal records, and the cited hal.search.bethlehem-archaeology record does not exist under records/hal. Burial "beneath the church" (sec. 30) could be added to the locus.
- Loci not checkable at passage level ("whole work", "whole letter", "passim"): desert-romances, rufinus-rupture, paula-epitaph, translating-a-book, rome-crisis Ep. 45, f5-enslaved ("household narratives"). Left as is.
- hal.figure.damasus | sources[0].locus | The locus "the Rome-period letters (the Damasus correspondence sits alongside them, Epp. 15-36 range)" is cited to hal.source.jerome-marcella-letters, which covers only letters to Marcella (Epp. 23-29, 32, 34, 37-38, 40-44, 59, 97) and does not carry the Damasus letters. The audit's proposed locus (Epp. 15, 16, 18-21, 35, 36; npnf206 div ids v.XV-v.XXI, v.XXXV-v.XXXVI) needs a new source record or a re-pointed existing one. Unfixed: needs a source record.
- hal.demo.someone-like-me | sources locus for hal.term.xenodochium ("the hospice open to any traveler") | the term record says "A hostel for travelers" (no "any"); audit marked this a label note only. Not changed.
- hal.demo.* and hal.figure.* body paragraphs | process commentary (e.g. "matching alx.demo...") | not spoken fields; body paragraphs not to be edited in this pass. CLAUDE.md treats commentary in records/ as corruption: needs separate cleanup.
- Source records outside this scope that the demos were adapted from; if not corrected, demos can drift back: hal.dw.marriage-ending text ("a senator's daughter", no source); hal.dw.suffering text ("died young of the very discipline her teachers had praised"; the fasting cause is the crowd's charge); hal.story.paula-epitaph ("stewards", Ep. 108 sec. 6 has relatives); hal.story.marcella-standing ("to her house they came", Ep. 127 sec. 7 has no house); hal.dw.believe text ("the beginning of his life with God", not in Ep. 22 sec. 30); hal.dw.practices ("Born again is not our phrase" contradicts the Pelagians dialogue, Ep. 22, Against Jovinianus; fixed in parallel).
- hal.demo.born-again exchange[1]: the sentence "Born again was our word for baptism" depends on the parallel dw.practices fix; the turn stays within Ep. 108 and the dw/source evidence (Pelagians dialogue vi.ix, Ep. 22, Against Jovinianus). It makes no claim either way about whether the participant's phrasing is "close to how we would put it".
- hal.demo.someone-like-me exchange[1]: the sentence "Our records describe these as open to the stranger and the sick poor, and they mention no test at the door" is the audit's wording (an absence statement from the term records); kept, flagged for review as it speaks about "records" from inside the voice.
- hal.term.monasterium | informational, use_note, and other records (hal.core and others) | "two linked houses" framing conflicts with Ep 108 sec. 20 (women in three companies); outside the allowed fields. Fleet-level; grep of records/hal for "three companies" finds nothing. Needs a lead/fleet decision.
- hal.term.monasterium | plain_meaning | audit gave no replacement; the audit's suggested wording was applied on the lead's instruction. It was not separately scored by the audit; scored in this pass (passes).
- hal.term.exegesis-as-practiced-authority | senses.informational | says clergy "came to her own house"; Ep 127 sec. 7 has no "own house" (only that many, "including sometimes priests", questioned her). Not in scope.
- hal.term.grammaticus | senses.evidential | says rhetoric is not attributed to Donatus; Fremantle's editor's introduction in npnf206 (div iv.III) says Jerome "studied rhetoric ... under Ælius Donatus". Not in scope; needs a decision on what "standard accounts" means.
- hal.term.patrocinium | senses.informational and hal.gravity.patronage-authority (line 51) | say Paula's fortune funded "his Hebrew teachers"; no cited source (Ep 84 gives it as Jerome's own expense). Not in scope (informational; build record).
- hal.dw.church-failure (line 37) and hal.term.pelagianism use_note.means | "mob" / "documented mob attack" not supported by the letters (attackers' number is Inferential-Thin per hal.source.attack-letters-416). Not in scope (build record; use_note).
- hal.term.pelagianism | senses.translational and source/quote records (hal.quote.innocent-ravages, source note) | describe a lost "letter" from the women; vendored Ep 137 never says a letter was written. "words" kept here; the carried-forward "letter" wording in those records is unchanged and needs review.
- hal.term.grammaticus and hal.term.praeceptor | sources[] hal.source.jerome-de-viris entry | kept with a corrected locus rather than dropped; confidence.divergence_note text on grammaticus ("not re-collated to a single locus") and praeceptor verification_state left as is.
- Pattern, not changed: other personal/informational senses that call the community "this world" were changed only where the sentence had another defect.
- hal.quote.rufinus-writes-because-rome-is-where-the-news-is | sources[0].source_id (hal.source.rufinus-apology) | The quote is from Rufinus's Apology to Anastasius (npnf203 div vi.ix, line 45886). The source record's edition names div vi.xi and its citation names "Apologia contra Hieronymum"; div vi.xi is the Apology addressed to Apronianus. Needs a source record: either widen hal.source.rufinus-apology to cover vi.ix, or add a separate source record for the Apology to Anastasius and repoint the quote. The quote's locus text is correct and was left as is.
- hal.source.sulpitius-dialogues | edition | Lists divs ii.iv.i.viii-ix, but a-man-truly-catholic is cited from I.7 (div ii.iv.i.vii, line 2834). Source record, out of scope.
- hal.quote.city-taken and hal.quote.the-city-which-had-taken-the-whole-world | text | Identical `text` (Ep. 127.12) with different renderings; flagged for dedup consideration.
- hal.quote.innocent-ravages and hal.quote.they-have-left-untold-the-name | text | Identical `text` (Ep. 137); both now carry the same rendering. Flagged for dedup consideration.
- hal.quote.hindered-by-jerome | verification_state | Still `verified-via-authority`, but direct verification is now possible (hand-verified at palladius_lausiac-history_clarke1918.txt line 475). The sweep tool reports a false FAIL because the footnote call "276" is glued to "Paula,"; this is a gap in the tool's apparatus stripping for this edition, not a record defect. Field left unchanged (not a spoken field).
- hal.quote.dispute-to-learn | text | The bare "them" is opaque out of context. If the referent matters, extend the `text` excerpt back to "a student of the scriptures"; the lead ruled to add nothing from outside the excerpt, so left as is.
- hal.quote.a-man-truly-catholic | modern_rendering | Audit option for Mark: lowercase emic "catholic" instead of "orthodox". Lead decided "orthodox"; applied.
- hal.source.* | missing records | No source record exists for Jerome's Ep. 48 (hal.dw.apostolic) or Ep. 125 (hal.dw.inner-life, and the Ep. 125 sentence removed from the text). A source record for each, with the vendored div ids, is needed before those claims can be cited.
- hal.dw.jesus | positions[1] | Still says "physician to the penitent"; this pass removed the claim from the spoken text because the cited passage does not support it as the community's own view.
- hal.dw.practices | positions[0], use_note | Still say "born again" was carried by other words; the spoken text now says the community spoke of being born again in baptism (Against the Pelagians III.15, III.19). Align in the build fields.
- hal.demo.* and hal.figure.* | body paragraphs | Carry build commentary (for example "matching alx.demo..."). Not spoken fields, so not changed here; CLAUDE.md treats commentary in `records/` as corruption.
- hal.figure.paula-younger | names[0] | "Paula the younger" is a convenience tag; the sources call her "little Paula" (Ep. 107) or "Paula" (Ep. 137).

Status: OPEN.

## OG-21. Corrections to OG-19 and OG-20 and further hal wording fixes after independent review, 2026-10-13.

Corrects OG-19 and OG-20 (their merged text is not edited) and records the fixes made after the independent review of the hal wording pass. Every touched field passes the readability limits. `m1:readability/hal` stays at 102: none of the fields below was in that count.

**Corrections to OG-19 and OG-20.**
- `hal.demo.born-again` exchange[1] and `hal.dw.practices` text: OG-19 and OG-20 quote the wording "Born again was our word for baptism". That is not the final text. After review round 1 both say "We spoke of being born again in baptism", and the `hal.source.jerome-against-pelagians` locus on `hal.dw.practices` is narrowed to Book III secs. 15 and 19 (the newly baptized "born again"; John 3:5).
- `hal.demo.someone-like-me` exchange[1]: OG-20 quotes "Our records describe these as open to the stranger and the sick poor, and they mention no test at the door". That sentence is not in the final text. The final text says "Nothing we kept speaks of a test at the door", and "taking up hard fasting" became "taking up the ascetic life" because only the crowd, not Ep. 39, says fasting killed her.
- OG-20 lists four records as not fixed that are fixed in OG-19: `hal.dw.marriage-ending` ("a senator's daughter"), `hal.dw.suffering` ("teachers had praised"), `hal.story.paula-epitaph` ("stewards") and `hal.story.marcella-standing` ("her house"). Those items are closed. `hal.dw.believe` ("the beginning of his life with God") is also fixed in OG-19.
- OG-20 states the `hal.dw.practices` and `hal.dw.jesus` open items twice (once from the change logs, once added). The open items are one each: `hal.dw.practices` positions[0] and `use_note` still say "born again" was carried by other words, and `hal.dw.jesus` positions[1] still says "physician to the penitent". Both are build fields outside this pass.
- Source entries added to `sources[]`, with the reason (each cited passage is in the vendored text and is used by the corrected spoken text, and no hal source record covered it): `hal.dw.church-failure` (`hal.source.vulgate-prefaces` for the Ezekiel preface, `hal.source.jerome-ep45`), `hal.dw.empire` (`hal.source.jerome-vita-malchi`, `hal.source.jerome-ep108`), `hal.dw.practices` (`hal.source.jerome-ep22` sec. 30, `hal.source.jerome-ep77` sec. 4, `hal.source.jerome-against-pelagians`), `hal.dw.sin-grace` (`hal.source.jerome-against-jovinianus`, Book II), `hal.dw.was-jesus-god` (`hal.source.jerome-ep108` sec. 10), and `hal.term.grammaticus` and `hal.term.praeceptor` (`hal.source.jerome-apology-rufinus`, Book I ch. 16, "my master Donatus", which `hal.source.jerome-de-viris` does not carry).

**Changed after the independent review** (record | field | change).
- hal.story.attack-416 | text | "wrote to the bishop of Rome and told him" became "told the bishop of Rome what had been done"; we-voice last line replaced with "the pope's account is all that survives"
- hal.story.paula-epitaph | text | staccato rejoined with semicolons and "and"; "led... learned... nursed" restored as one list
- hal.story.marcella-death | text | clauses rejoined (pointed to dress, but they did not believe her and beat her; took the two women...; thankful too); no claims added
- hal.story.day-at-monastery | text | clauses rejoined with "and", semicolons, colon; content unchanged
- hal.story.rome-crisis | text | clauses rejoined; crowd mutter restored as a semicolon list; slander and ship sentences joined
- hal.term.bibliotheca | plain_meaning | two sentences joined with "which his standing as a scholar rested on"
- hal.term.bibliotheca | quick_meaning | same rejoin
- hal.term.epitaphium | quick_meaning | "The letter for the dead, which mourned them and taught the living what a holy life looked like."
- hal.term.grammaticus | quick_meaning | "Latin school under Donatus, which was the base for all of Jerome's later work."
- hal.term.peregrinatio | quick_meaning | joined with semicolon: "Pilgrimage, or devout travel to the holy places; for us it ended in the choice to stay."
- hal.story.rufinus-rupture | tellable_as | "...over Origen. They had been friends for years, and it ended in angry, rival answers."
- hal.story.day-at-monastery | tellable_as | "a day at Bethlehem... It is a rebuilt picture, not a timetable." ("ordinary" dropped for FRE)
- hal.story.desert-romances | tellable_as | "They are not history" replaced by "They are the stories we told, and we make no claim that each event happened." ("desert" dropped from "hero-tales" for FRE)
- hal.limit.f5-women-own-words | statement | "held to be his work, not theirs" replaced by "He wrote the one letter sent in their names."
- hal.dw.church-failure | text | "He mocked a former friend after the man had died" became "He wrote a preface that seems to mock a former friend after the man had died"
- hal.demo.women-own-words | exchange[1] representative turn | "a report of a fire" became "a report of the attack"
- hal.quote.hindered-by-jerome | modern_rendering | Rewritten by Opus: the staccato version rejoined so every clause of `text` is rendered, nothing added (FK 8.1, FRE 69.8).

Status: CLOSED for the fields listed.

## OG-22. use_note.means checked against the corrected spoken fields, 2026-10-13.

Per Mark's ruling of 13 October, `use_note.means` is in scope where it contradicts the corrected spoken fields or the source, because `engine/m4/evidence.py` puts it into the evidence block the voice reads. All 99 hal records that carry a `means` were compared with their corrected fields, their cited source and their confidence level: 30 quotes (a 31st quote has none), 23 terms, 16 doctrinal witnesses, 12 stories, 4 honest limits, 6 gravities and 7 contested claims. Five were changed; the other 94 were left as they were. `not_for` and `years` are untouched. `means` is not readability-graded, so no waiver count moves.

**Changed** (record | field | before | after | why).
- hal.term.pelagianism | use_note.means | before: "The dispute over grace and human capacity, which reached this community as a documented mob attack in 416." | after: "The dispute over grace and human capacity, which reached this community as a documented attack in 416." | why: corrected spoken fields drop "mob" (plain_meaning, quick_meaning, personal)
- hal.limit.f5-women-own-words | use_note.means | before: "Nothing the four women wrote survives, though they demonstrably wrote, so what remains of them is what one man wrote about them." | after: "Nothing the four women wrote survives, though they demonstrably wrote, so what remains of them is what men wrote about them, above all one man." | why: corrected statement: "what men wrote about them, above all one man"
- hal.limit.f5-enslaved | use_note.means | before: "The sources are silent on the enslaved and dependent people in the great households, never naming or voicing a single one." | after: "The sources say almost nothing about the enslaved and dependent people in the great households, and name or voice none of them." | why: corrected statement: "our record says almost nothing ... mention them only in passing"
- hal.dw.church-failure | use_note.means | before: "This witness holds that the record openly names church failures, including clergy corruption seen from inside and Christian violence against Christians, both dealt and suffered." | after: "This witness holds that the record openly names church failures, including clergy corruption seen from inside and wounds Christians dealt one another, which the community both gave and took." | why: Corrected text says the community "used the church's power against Christians" and "dealt some and took some"; the only violence in it (burned out of buildings) was suffered, so "violence ... dealt" overreached.
- hal.story.desert-romances | use_note.means | before: "Jerome's hagiographic romances of Malchus and Hilarion, evidence of what this world imagined formation could look like and not of events." | after: "Jerome's lives of Malchus and Hilarion, which show what this community imagined a formed life could look like; whether each event happened is left open." | why: the story's corrected `tellable_as` and text make no claim that the events did or did not happen, and the vendored Malchus text calls the life a "history of chastity"; "romances" and "not of events" stated more than the record's Inferential-Thin confidence.

**Checked and left as they were, by request.** `hal.dw.church-failure`'s scorpion wording is not in its means (the change above concerns the violence wording only), and `hal.story.attack-416` (the means speaks of the women's lost report and does not say they wrote a letter), `hal.quote.detestable-monks` (the fasting claim stays with the crowd).

Status: CLOSED.

## OG-23. Atlas story pass: shorter story, nine card stories with tellings, highlights, 2026-10-17.

The project lead asked for each built tradition's Atlas story to run four to five minutes, with the other episodes moved into stories on the card. He approved the Bethlehem Circle story and card list, then the tellings, then a sample recording. `orientation.story` is now 9 units and 691 words, down from 11 units and about 1,150 words. `documented_stories` shows nine story records in date order. Each of those records gained a `telling`, which the card shows and plays. `orientation.highlights` adds 17 short notes; place notes cite Pleiades for modern locations (checked 2026-10-17). Episodes cut with no story record of their own stay in their records: Fabiola and the Portus hostel, Palladius's counter-account, the Hebrew-fluency question, and family resistance to Paula's leaving. Review: `Build/Ministry/Operations/Audits/hal_atlas_story_pass_review_round1_2026-10-17.md` (PASS). Package rebuilt and repinned: `packages/hal/2026-10-17T13-45-54Z`, `manifest_hash` `sha256:f9ca759df95602a5ce7717a7f084083bf83e8f560fd84dde8617866202a63641`. This pin supersedes the previous one. The story and the nine tellings were recorded in the existing voice.

**Open:**
- The package change makes the next promotion's admission stale. The project lead rules on that run.

## OG-24. Record disagreements found during the Atlas story pass, 2026-10-17.

The pass followed the more cautious record in each case and changed no record. Each needs a ruling on which wording is right:
- `hal.story.ciceronian-dream` gives `use_note.years` 384 to 384, while `hal.quote.a-follower-of-cicero-and-not-of-christ` locates the dream in the illness of 374. The card dates the dream about 374, told in a letter of 384.
- `hal.story.paula-epitaph` `use_note.not_for` asks for a closing acknowledgment that her own voice was not kept. Under the project lead's ruling on add-on endings, the telling opens with it instead; he approved that telling on 2026-10-17. The record's wording should follow.
- `hal.contested.paula-jerome-relationship` gives Paula nineteen years at Bethlehem, while `hal.figure.paula` gives 386 to 404. The story gives no count.
- `hal.quote.no-one-preferred-to-the-seventy` text has Augustine grant that the Jews call Jerome's work faithful, while its lens note says he "gives away every point". The story follows the quote text.
- `hal.figure.marcella` bridge_line calls the Aventine household a circle before Jerome came, while `hal.force.marcella-household` rates a multi-woman household as a modern reconstruction. The story and note follow the force record.

Status: OPEN for the project lead.

## OG-25. Other world_front sections keep AI tells and "this world" wording, 2026-10-17.

The Atlas story pass touched only the story, the card stories and the highlights. `voices` and their hedges, `floor_note`, `legacy`, `relations_summary`, `sourcing`, `read_first` and `narrative.who_speaks` still use "this world" wording and dash asides. The same holds for the Alexandria and Cappadocia records.

Status: OPEN for the project lead to schedule.

## OG-26. Atlas final-check fixes, 2026-10-17.

Three independent readers checked the live page (reviews `Build/Ministry/Operations/Audits/fleet_atlas_final_check_*_2026-10-17.md`). The project lead approved every blocking and should-fix finding, with three rulings: a tradition's own voice hedges emically ("we cannot be sure"), never with "scholars"; old-translation Wittenberg quotes are told as reported speech for now; House Churches keeps its "we" voice throughout.

Fixed: the tile now says no one held a bishop's office (not any church office), attributes Marcella's standing to Jerome, and no longer claims everything comes through Jerome's pen; tile rhythm, build wording and long highlight notes trimmed. No record changed.

Status: CLOSED for this review.

The same two claims in the census copy (`cic-website/data/world-census.json`, `index.html`, `atlas-v3.html` and the tradition page) were corrected in the recheck: Marcella's standing is now attributed to Jerome.

## OG-27. Unclear honest-limit endings, 2026-10-17.

Fleet sweep (project lead ruling, 2026-10-17): honest-limit sentences that put the object first and ended on a bare verb, so the ending did not say what is unknown. Each now puts the subject first and ends on what is not known. Wording and facts are the records' own; nothing was added.

- `records/hal/story/hal.story.day-at-monastery.md`: "Which psalms they sang, and how the two houses shared their worship, no one wrote down, or nothing that was written survived." -> "Either no one wrote down which psalms they sang and how the two houses shared their worship, or nothing that was written survived."

Status: CLOSED for this review.

## OG-28. The worst gloss cards rewritten, 2026-10-18.

Rewritten: `hal.term.grammaticus` (`senses.translational` and `false_friend[0]`), `hal.term.matrona` and `hal.term.monasterium` (`false_friend[0]`). On 17 October the project lead ruled that the readability gate grades the gloss card (`senses.translational` and each `false_friend` line), and that only cards scoring FK 18 or more are rewritten now (System Hub Decision Log, "2026-10-18 - The worst gloss cards rewritten"). Sonnet drafted; an independent Opus review checked each card against the record and, where it quotes one, the vendored text (`Build/Ministry/Operations/Audits/gloss_card_fk18_rewrites_review_2026-10-18.md`), and corrected 3 of this world's 4. Each card keeps every claim and quotation, adds nothing, and speaks from outside the world. Every rewritten card now scores FK 10 or below and FRE 60 or above; each scores below FK 8, which is reported, not failed. The `m1:readability/hal` waiver falls from 156 to 148. Cards below FK 18 stay as written. Package rebuilt and repinned. Status: CLOSED.
