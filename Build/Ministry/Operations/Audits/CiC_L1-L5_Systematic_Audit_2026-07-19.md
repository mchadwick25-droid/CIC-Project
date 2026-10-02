# CiC Systematic Audit — Build Process (L1–L4) and World Builds (Level 5)

**Date:** 2026-07-19 (later still) · **Run by:** System Hub, on Mark's instruction to "systematically go through all the functions, features and processes... start with the build process our core documents L1-L5"
**Method:** 10 independent read-only agent audits (5 covering L1-Foundation through L4-Templates + Project-Reference; 5 covering each live world's construction record under `World-Builds/`). No file in the audited structure was moved, renamed, or edited — this is a findings report only.
**Scope note:** L1–L4 are the non-world-specific methodology levels. "Level 5" has no literal folder — it is the per-world output in `World-Builds/`, produced *by* the L1–L4 methodology. Five worlds are live in the deployed app: House-Church (Chloe), Desert-Monasticism (Papnoute), Syriac Christianity (Mar Yausep), Bethlehem Circle / Hieronymian-Ascetic-Literary (Albina), Alexandria (Theon).

---

## Read this first: two items above everything else

### 1. Possible safety gap — House-Church, live with real participants

> **RESOLVED — see Decision Log 2026-07-21.** Confirmed by direct code read: the
> crisis-handoff mechanism exists at the Facilitator/platform level exactly as this
> finding speculated it might (`classify_relational_safety` in `cic-poc/backend/app/graph/
> nodes.py`, wired into both message endpoints, applies identically to all five worlds
> including House-Church/Chloe). The architecture is real. **What is still genuinely
> open, not resolved by this note:** live-model adversarial testing has never been run
> against it — see the new DO NOW item on the Task Board. Don't re-flag the mechanism's
> existence; do track the live-testing gap.

House-Church's own last recorded internal safety test (2026-07-09, `Phase5_BoundaryTesting_Independent_Verification_Round1.md`) scored **Relational Safety a FAIL against real-deployment readiness — blocking**: no crisis/distress handoff mechanism existed. The follow-on Facilitation Brief (still filenamed DRAFT) says, in its own words:

> "the actual safety-critical mechanism — recognizing a real crisis signal and executing a clean handoff to human help — remains explicitly Facilitator-governed... and still does not exist anywhere in this world's current artifacts... **this world should not be exposed to real participants until that mechanism exists and is tested.**"

Nothing in the House-Church folder postdates 2026-07-09. This audit cannot see past that per-world folder — it's possible a crisis-handoff mechanism was built at the Facilitator/platform level afterward and simply never got logged back into this world's own record. But if it wasn't, this is not a documentation gap. **Recommend confirming this directly before Prototype Testing 1 proceeds**, independent of every other finding below.

### 2. The canonical governance record is out of date, and the fix may already exist unmerged

`CiC_L2C_Phase_Status_V1.2.docx` — the document meant to be read every session — still tracks a **five-world registry** and shows 4 of 5 as "Not started." It does not mention House-Church, Syriac, Desert-Monasticism, or Bethlehem Circle under any name. `System Level Map`, `Clean File Structure`, and `System Operations` share the same stale picture.

The Change Orders Register explains why: **CO-023/CO-024 (2026-07-09) already declared a nine-world portfolio and formally deprecated "Early Communal"** — but that decision, plus a real batch of other governance work (Constitution 2.2→2.3, Facilitator-Governance V3.4→V3.6, Representative reconceived as the world's-own-voice), was made on separate branches (**`CiC-L1L3-Foundation`, `CiC-Fable-Experiment`**) and is explicitly marked in the Register as **"NOT YET PROPAGATED to the canonical project folder."** The Register then goes quiet for the ~10 days spanning the project's biggest recent progress — no change orders exist for the three additional worlds reaching deployment.

**`CiC-L1L3-Foundation` is a live git worktree right now** (flagged in this session's earlier worktree inventory, still `locked: initializing` on a cloud session). It is very likely already carrying some or all of the fix for a large share of what's stale below. **Recommend checking what's on that branch before manually re-editing any canonical L2 document** — the work may already be done, just not merged.

---

## Critical / High findings

| # | Finding | Where | Severity |
|---|---|---|---|
| 1 | ~~No crisis/distress handoff mechanism confirmed to exist for a live world (House-Church)~~ **RESOLVED 2026-07-21** — exists, platform-wide; live-testing tracked separately | L5 · House-Church | ~~Critical~~ Closed (see Decision Log 2026-07-21) |
| 2 | Canonical L2 status/registry documents describe a project that no longer exists; the fix may be sitting unmerged on `CiC-L1L3-Foundation` | L2A/L2C/L2D | **Critical — governance** |
| 3 | ~~Bethlehem Circle's *deployed* Permanent Prompt has drifted from the canonical, reviewed, adversarially-tested World-Builds copy~~ **RESOLVED 2026-07-21** — resynced, byte-identical | L5 · Bethlehem Circle | ~~High~~ Closed (see Decision Log 2026-07-21) |
| 4 | Constitution Article 35 cites a "Deployment Standards document" as existing and authoritative; the World Build Onboarding Framework states plainly it has never been produced | L1 / L2B | **High — dependency gap** |
| 5 | `CiC_Project_Status_July2026.docx` describes an early-July, pre-CO-013, single-world-paused state contradicted by other documents in the same folder | Project-Reference | **High — actively misleading if trusted** |

---

## Per-world lexicon confidence-vocabulary compliance (Article 17 / Author-Gravity)

A cross-world finding logged earlier today flagged Desert-Monasticism and Hieronymian as gaps. Each world audit independently re-opened and recounted every lexicon chunk rather than trusting the earlier tally — two of the five original numbers turned out to be wrong.

| World | Confidence-vocabulary compliance | Author-Gravity disclosure | Note |
|---|---|---|---|
| **Syriac** (Mar Yausep) | 9/9 (100%) | 9/9 (100%) | Clean first read — no gap |
| **Alexandria** (Theon) | 44/45 (97.8%) | — | Corrects the build's own "45/45" self-audit; `alexlex011_nous.md` discusses the dispute substantively but never applies the formal label |
| **Bethlehem Circle / Hieronymian** (Albina) | 6/15 (40%), confirmed | 1/15 (7%), confirmed | Underlying confidence ratings already exist in Doc_06 — fix is copying them into 9 chunks, not re-investigating |
| **House-Church** (Chloe) | 0/13 (0%) — **worse than logged (was not previously checked)** | ~9-10/13 substantively, via a different apparatus ("Distortion Risk" pairs) | Doc_06's own construction record applies Article 17 rigorously; it just never propagated into the runtime chunk text |
| **Desert-Monasticism** (Papnoute) | 0/9 (0%) — **worse than the logged 5/9 (56%); re-grep found the "5" were false-positive word matches, not real ratings** | 2/9 (22%), confirmed | Root cause diagnosed: Doc_06 gives every entry both "Key Texts" and "Key Sources: Doc_02 §X.X" fields; the chunk-extraction step kept the first and dropped the second, uniformly, across all 9 chunks. Grounding citations still exist upstream — mechanical fix. |

Story-repository chunks are healthier across the board: House-Church (spot-checked, compliant), Desert-Monasticism (8/8, 100%), Alexandria (compliant, spot-checked), Bethlehem Circle (compliant, spot-checked) all carry confidence vocabulary in front matter even where the *lexicon* layer doesn't — this looks like a lexicon-chunk-specific extraction problem, not a project-wide one.

---

## L1–L4 findings by level

### L1-Foundation
- **`CiC_L1_Vision_V2_0.docx` has no internal version marker anywhere** — the only L1/L2B document missing one. Worth confirming "V2.0" is actually current.
- **The newer governing vision doc (`Ministry/Communication/.../V1.1.docx`) has genuinely shifted the rigor-floor anchor**, not just reworded it: from "what the methodology requires of every world build" (L1 Vision/Constitution) to "what's been demonstrated in the two existing world builds" (v1.1) — a narrower, backward-looking standard. Worth a deliberate decision on which governs.

### L2A — System Architecture
- The "five-world registry" problem (see top of report) originates here and in L2D, then propagates into L2C.
- `Architecture Map V2.2` states no world has ever completed V7 Validation and that deployment outputs "do not yet exist for any world" — in tension with five worlds being live. Worth reconciling what bar each document is measuring against (built-and-deployed vs. formally-frozen-under-V7).
- `Clean File Structure V1.1`'s registered world-folder names don't match either the old or new real folder names, and states Alexandria's build artifacts live only in `Archive/` — contradicted by the fact that `World-Builds/Alexandria-Catechetical-School/` (116 files, current V7 build) exists and was actively in-progress as of today. Likely another instance of this document's general staleness rather than a real conflict — `Archive/Alexandria-Build-History/` is almost certainly the *prior* pre-rebuild version.

### L2B — System Entry
- **Confirmed gap, checked directly**: Constitution Article 35 treats the Deployment Standards document as existing; World Build Onboarding Framework states it has never been produced.
- **Checkpoint One timing conflict**: Critic Role Description v1.2 says Checkpoint One fires "after Steps 4 through 7" (before Doc_08 exists) but then asks the critic to review the Forces Document at that same checkpoint; World Build Onboarding Framework (same version number, v1.2) correctly says Checkpoint One is after Doc_07 *and* Doc_08. The Critic doc also has a garbled "Doc_01 through Doc_08 and Doc_07" phrase suggesting an incomplete edit.

### L2C — System Status
- `Phase Status V1.2` is the single most out-of-date document found in this audit (see top of report).
- Internal contradiction: Phase Status says the Prototype Alpha world ceiling is 3; System Operations says 2.
- Phase Status credits "Table Design V2.2" and "RCF V2.1" as current; System Level Map and the Corrections Tracker both agree the real current versions are V2.3 and V2.2 — Phase Status is the outlier.
- The Change Orders Register is the healthiest document found in the entire audit — current, self-critical, catches its own past mistakes — but has a ~10-day gap exactly where the project's most recent progress (three more worlds shipped) should be recorded.

### L2D — System Operations
- Explicitly dated 2026-07-02 — the oldest dated document in the entire audit, and the origin source for the stale five-world registry that Phase Status inherits by design.
- Cites Facilitator-Governance v3.2 — one version behind even the (also stale) canonical System Level Map's v3.3, three behind the real current v3.6.

### L3A — Shared Methodology
- Forces Framework (V1.1) says the Forces methodology integrates into an "eight-step construction sequence" — the actual sequence (per Construction Framework V7.3) is ten steps. The six integration points it names are still individually correct; only the "eight-step" framing sentence is wrong.
- Ecology lens naming has drifted: Construction Framework and Forces Framework both use "Human Ecology / Community Ecology / Boundary Ecology" — the Formation World Template (the document meant to be authoritative on this) uses different names entirely ("Formation Ecology," "Boundary Structures," a combined "Organizational & Ministry Ecology").

### L3B — World-Build Methodology
- **Doc_04's template location is explained, but the explanation itself is shaky.** The template says it's filed in L3B (not L4, unlike its siblings) per an editing-authority assignment to the coach role, and claims Doc_01–03 already have L4 templates and that a "Doc_02B Approved Source Database Template" is filed alongside it. Neither claim checks out: L4-Templates has no template for Doc_01, 02, or 03, and no file named anything like "Doc_02B" exists anywhere in L3B or L4.
- Blueprint and Construction Framework (both V7.3) describe the Formation World Template differently in otherwise-identical relationship-mapping blocks ("= WHAT" vs. "= Dimensions") — a small but real terminology mismatch between two same-version sibling documents.
- `Representative_Permanent_Prompt_Template.txt` is the only template file with no version number in its filename, and its internal header (2.1) is stale against its own changelog's latest entry (2.2).

### L3C — Representative Methodology
- Still cites the anti-fabrication rule as "Constitution Article 3; TC-001" — Facilitator-Governance V3.6 already corrected this same citation to "Article 28, Anti-Fabrication Prohibition." L3C wasn't updated to match.
- `desktop.ini` in this folder is confirmed harmless Windows Explorer metadata (pointing at template files that have since moved to L4) — safe cleanup candidate, not touched.

### L3D — Encounter Methodology
- **The three-Facilitator-Governance-versions question resolves cleanly**: V3.6 is current and actively cited elsewhere as governing; V3.7_PROPOSAL is a narrow, self-contained, not-yet-merged patch to Section 10 matching the decision log's description almost exactly; **V3.4 is a genuinely stale leftover, safe to archive** (nothing treats it as current).
- V3.7_PROPOSAL fixes a stale "six signals" count in Section 10 but doesn't fix the dependent "eleven signals" count in Section 14, which its own fix makes even further wrong — worth catching at merge time.
- `The Table Design Document V2.3` states "has not yet been deployed or tested" — its own companion document (`Table_Process_ThreeRepresentative`) documents real live testing, a dated 2026-07-13 incident fix, and an actual code reference (`MAX_MULTI_WORLD_TURNS` in `main.py`). Readiness status looks stale.
- **`CiC_L3D_Table_Process_TwoRepresentative` is referenced repeatedly by the Three-Representative document as an established governing sibling — confirmed via repo-wide search that no such file exists anywhere.** Real gap, not a missing-from-batch issue.

### L4-Templates
- Only **Doc_07 and Doc_08** of the ten construction steps have a dedicated L4 template. **Doc_10's Permanent Prompt has no template anywhere in L4**, despite being referenced as load-bearing by three other templates (Voice Configuration, Representative Construction Notes, World Capsule Core all calibrate against it).
- `World_Facilitation_Brief_Template.md` is the one template not updated for the CO-013 eleven-output architecture — still frames itself around "seven primary deployment outputs," and its own referenced output-number ("Output 6," per the Introduction Brief template) doesn't reconcile with that older framing.

### Project-Reference
- `CiC_Project_Status_July2026.docx` (see top of report) is substantially stale relative to its own folder.
- `CiC_Cleaning_Pattern_Log.md`, `CiC_Governance_Standing_Rules.md`, and `CiC_OneDocAtATime_Build_Protocol` (revised through 07-09) are current and mutually consistent — good evidence Level 2/3 cleaning is much further along than Project Status describes.

---

## Per-world (Level 5) build health

| World | Construction sequence | Process quality | Known open gates |
|---|---|---|---|
| **Syriac** (Mar Yausep) | Complete, 9/9 docs, deepest review history of any world | Caught and structurally corrected its own self-certification failure mid-build; live testing caught and fixed 3 real defects incl. a fabricated genealogy | Article 31 review never done; only 4/8 Part Eight categories live-tested (cross-project infra gap, not world-specific) |
| **Alexandria** (Theon) | Complete, 9/9 docs | Just-recovered 116 files show no corruption; unusually self-auditing (runs its own cross-world findings) | Newest, thinnest-tested world (1 boundary-testing round); Article 31 pending — both accurately disclosed |
| **Bethlehem Circle** (Albina) | Complete, 9/9 docs + Doc_10 | Caught its own fabricated quotation and a chronologically-impossible claim pre-ship | ~~Deployed Permanent Prompt has undocumented drift from the tested/reviewed version~~ **RESOLVED 2026-07-21 — see Decision Log.** World-Builds resynced to deployed (`5a63d80`), verified byte-identical; rename to "Bethlehem Circle" never reached any of the 77 internal files (still open) |
| **House-Church** (Chloe) | Complete, 9/9 docs, first world ever built | Exceptional — caught a false "verbatim" self-certification, a misattributed quote, and a logic error in Forces classification | **Own safety testing said not to ship without a crisis-handoff mechanism, dated 2026-07-09, status unconfirmed since** (see Critical findings); worst lexicon-chunk compliance (0/13) offset by a parallel Distortion-Risk apparatus; undisclosed "Amma"→"Chloe" Representative rename across dozens of review files |
| **Desert-Monasticism** (Papnoute) | Complete, 9/9 docs | Self-disclosed a recurring "illusory fix" pattern across 5 documents — caught every time by a subsequent independent round; genuine 3-cycle adversarial live-testing | Lexicon compliance worse than previously logged (0/9, not 5/9) but root cause now precisely diagnosed as a mechanical extraction bug, cheap to fix; explicitly Not Frozen, same two gates as Syriac |

**What's consistently healthy across all five:** every world's Doc_01–09 sequence is genuinely complete with real, substantive multi-round adversarial review — none of it reads as rubber-stamped. Every world honestly discloses its own open gates (Article 31, Encounter Testing) rather than hiding them. Every Representative that's had live adversarial testing has had real, fixable defects caught and closed by it, not a clean pass claimed on the first try.

---

## Recommended next steps (for Mark's decision, nothing actioned)

1. ~~Confirm the House-Church crisis-handoff mechanism status directly~~ **DONE — see the RESOLVED note under Finding 1 above and Decision Log 2026-07-21.** Live-testing follow-up now tracked separately on the Task Board.
2. **Check what's actually on `CiC-L1L3-Foundation` before hand-fixing any canonical L2 document** — a large share of the "stale registry" findings may already be resolved there, unmerged.
3. ~~Confirm and re-test the Bethlehem Circle Permanent Prompt drift~~ **DONE — see the RESOLVED note under the per-world table below and Decision Log 2026-07-21.** World-Builds resynced to match deployed (`5a63d80`), verified byte-identical.
4. Decide which "Governing Constraint on Revision" language governs (L1 Vision's methodology-required floor vs. the newer v1.1's demonstrated-so-far floor).
5. When capacity allows: the lexicon-chunk fixes for House-Church, Desert-Monasticism, and Bethlehem Circle are all mechanical (grounding data already exists upstream in each world's own Doc_02/Doc_06) — good candidates for a single focused pass across all three.
6. Archive `CiC_L3D_Facilitator_Governance_V3.4.docx` (confirmed superseded) and clean up `L3C-Representative-Methodology/desktop.ini` (harmless OS artifact) — trivial, low-risk, whenever convenient.

Nothing above has been changed. This is the findings record; every action item is a recommendation awaiting your call.
