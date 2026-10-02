# Build-Process Sequencing: Is CiC Constructing World → Representative → Facilitator/Table in the Right Order?

**Method.** CiC's real build order was read first, from the governing documents themselves, not from summaries: `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4_DRAFT.docx` and `..._V7.3.docx` (both extracted and read in full — Parts I–VII and the complete Step 0–10 sequence), `L3C-Representative-Methodology/CiC_L3C_Representative_Construction_Framework_V3.2.docx` (all ten Parts, including Part Nine's seven-phase Construction Process Summary), `L3D-Encounter-Methodology/CiC_L3D_The_Table_Design_Document_V2.3.docx`, `CiC_L3D_Facilitator_Governance_V3.6.docx` and `..._V3.7_PROPOSAL.docx`, `CiC_L3D_Table_Process_ThreeRepresentative_V1.0.md`, `L3A-Shared-Methodology/CiC_L3A_Phase_Structure_V1.1.docx`, `L1-Foundation/CiC_L1_Constitution_V2_2.docx` (Article 3), `L2C-System-Status/CiC_L2C_Change_Orders_Register_V1_18.docx` (all 24 Change Orders), `L2C-System-Status/CiC_Pipeline_Decision_Log.md`, `L3B-World-Build-Methodology/CiC_L3B_Prototype_Testing_Charter_V1.0.docx`, `L4-Templates/World_Facilitation_Brief_Template.md`, plus research docs 03, 04, 05, 06, 16 and the Fable brief in full.

Chronology was established from git history (`git log --diff-filter=A`, `--name-status`, and commit bodies), not from document version numbers, because the version numbers do not carry dates. Per-world evidence was read directly: `World-Builds/01-Post-Apostolic-House-Church/CiC_W1_Phase5_BoundaryTesting_Independent_Verification_Round1.md`, `CiC_W1_Validation_Testing.md`, all five surviving Phase Six Facilitation Briefs, `World-Builds/Imperial-Juridical-Christianity/Step10_Phase5_Boundary_Testing_Record.md`, and `Cross_World_Roundtable_Validation.md` via `git show CiC-Fable-Experiment:`. All six deployed Permanent Prompts under `cic-poc/backend/data/` were grepped directly.

External research ran as four parallel passes. Every claim rated **High** was verified against a primary source I or the dispatched pass actually loaded. I personally re-verified the five most load-bearing external citations (arXiv 2603.24284, 2503.13657, 2602.01011, the Anthropic multi-agent post, the Roth table of contents, the NPS competency order). Fifteen items I could not verify are listed at the end under **Do not cite**.

---

## Summary — the direct answer first

**Mark's question was: is CiC building world → representative → facilitator/table in the right order? The honest answer is yes, and the premise of the question is factually wrong in a way that matters.**

CiC did not build the Facilitator/Table layer last. It built it *first* — and then never made it a gate. Those are two different problems, and only the second one is real.

The order itself is more strongly supported than I expected going in. Every field with real published methodology on this — living-history interpretation, Stanislavski-tradition actor training, worldbuilding craft, multi-agent system design — either endorses context-before-persona or is silent. Nobody recommends the reverse. **Do not reorder the Construction Framework's steps.** The five most important findings:

**1. The chronology contradicts the "built late" hypothesis outright.** Facilitator Governance v3.0–v3.2 and Table Design v2.1 existed before the git repo was initialized (2026-07-01); V3.3 and V2.2/V2.3 were produced 2026-07-02. The six current world builds ran 2026-07-07 to 07-22. Earlier still, the pre-V7 Alexandria/Theon prototype ran a complete five-layer vertical slice on one world — `World Activation.md`, `Lexicon Activation.md`, `Representative Activation.md`, `Facilitator Governance Activation.md`, `Assembly The Table.md` (all under `Archive/Alexandria-Build-History/`) — and CO-008 states in its own Rationale that the governing documents "emerged from what those tests revealed." CiC's own history contains the thin-slice-first pattern this research would otherwise have recommended. Confidence: High.

**2. CiC's own governing documents already specify parallel construction and an early two-world gate — and the specification is better than the execution.** CO-005 states the Table/Facilitation track "runs in parallel with the World Build track and is world-neutral." `CiC_L3A_Phase_Structure_V1.1` Phase 0 says: "Phase 1A/1B/1C world builds run simultaneously with table architecture documents. Neither waits for the other," and sets the Gate to Prototype Alpha as "Two-world table proven end-to-end." That gate was in fact satisfied on 2026-07-10 — the day the runtime landed, with exactly two worlds built — and it immediately paid off (finding 4). Nothing needs to be reordered. Confidence: High.

**3. The real defect is that the table is a destination and a specification but never a gate.** Facilitator Governance V3.6 §15 states it plainly, in its own voice: **"The governance specified in this document is specified with more precision than it has been validated."** The Construction Framework's Freeze Criteria include "encounter testing is successful" — but Step 10 says the Representative is built from the *already-frozen* world, so the gate is unsatisfiable at the point it is stated, and World #1's own Step-9 validation document deferred four of Part VI's fifteen categories for exactly this reason. Meanwhile the three governing documents barely share vocabulary: Construction Framework V7.4 (720 paragraphs) contains the word "table" **zero times** and "multi-world"/"multi-representative" **zero times**; Table Design V2.3 references **zero** Doc_0N documents and **zero** numbered Steps; Facilitator Governance V3.6 references world-build artifacts **four times total** and mentions "forces" or "gravity" **zero times**. This is the brief's §5d finding ("relational insight that never reaches the Facilitator") stated at the level of build sequence rather than data schema. **Verdict: REAL GAP.** Confidence: High.

**4. Table testing demonstrably catches classes of defect that no solo build can, and CiC has four documented instances.** (a) 2026-07-10, commit `bb0698c`, the first day two worlds sat at a table: "Representatives were adopting each other's terminology when responding to the public transcript" — real cross-world contamination, hours after the capability existed, in two worlds that had both already cleared their own builds. (b) The four-voice roundtable found anachronistic vocabulary under multi-voice pressure, its own record noting it "was not previously tested by any single-world probe (all of which test a voice in isolation)," plus closing-speaker synthesis bias. (c) The three-Representative turn-cap incident, whose root cause was an extended-thinking token-budget interaction invisible at any single-world scale. (d) The sharpest one: a Construction Framework Part Five requirement that had "always" applied — anchoring a reference to another Representative's world by name — reached **zero of five** deployed Permanent Prompts until a multi-voice test was finally run on the last world built, 2026-07-20. Confidence: High.

**5. But the layer that carries table work per-world is the least-finished thing in the entire pipeline, and that is a sequencing consequence.** RCF V3.2's Phase Six (Facilitator Coordination) and Phase Seven (Encounter Ecology Mapping) are the last two phases of the last step. Phase Six exists for 5 of 6 worlds and is **fully review-cleared for 2 of 6**. Phase Seven exists for **1 of 6**, written retrospectively. And Phase Seven's own text opens with the words **"Before Representative construction begins"** while being numbered *seventh* — a literal, unreconciled ordering contradiction inside the governing document. Confidence: High.

---

## 0. CiC's actual build order, verified precisely

### 0a. The stated sequence is real and matches the brief's description

Construction Framework V7.4 DRAFT, Part VII, step headers verified verbatim: Step 0 — Movement-Scope Eligibility and Seed Identification; Step 1 — World Identification, Boundaries, and Orientation; Step 2 — Source Ecology and Source Registry; Step 3 — Lexicon Candidate List; Step 4 — Gravity Discovery; Step 5 — Ecological Reconstruction; Step 6 — Full Lexicon Development; Step 7 — Integrated Ecology Analysis; Step 8 — Forces Document; Step 9 — Story Inventory, World Profile, and Validation; Step 10 — Representative Emergence.

Two deviations from a naive reading, both real:

- **Forces run twice, deliberately.** Step 1's output includes "preliminary forces identification"; the framework adds "This is not the complete forces analysis. It is the orientation that governs Step 2 scope," with Doc_08 compiled at Step 8 and "Forces Framework integration: Steps 7 and 8." This is CO-004, filed because "Single-pass forces analysis at Step 7 missed forces-last cost." **Worth flagging: CO-004's own text says the split is "Step 3 preliminary identification + Step 7 full synthesis." The framework implements Step 1 + Steps 7–8.** An ADOPTED sequencing change order's own step numbers no longer match the framework it governs — small, but it is drift in exactly the governance area this document is auditing. Confidence: High.
- **Step 10 is a hard, one-directional firewall, by explicit design.** Verbatim: "The Representative emerges last, built only from the completed and frozen world's ecology — never from invented biography (Constitution Article 28...). **It influences nothing above it.**" This is CO-003, filed because "The Representative was being introduced during the build (TC-001 violation)." Confidence: High.

Step 10 then expands into RCF V3.2 Part Nine's seven phases: Ecology Assessment → Formation Calibration → Voice Construction → Engagement Architecture → *Representative Artifact Construction* → Boundary Testing → **Facilitator Coordination** → **Encounter Ecology Mapping**.

**So the full stated pipeline is 10 world steps, then 7 Representative phases, with the Facilitator/table layer occupying the final two phases of the final step.** That is where the "built last" impression comes from, and at the per-world level it is accurate.

### 0b. The Construction Framework already denies that it is a waterfall

Part VII, identical in V7.3 and V7.4: **"The workflow is not strictly linear. Later discoveries may require revisiting earlier steps."** Part VI, Revision Testing: "If significant failures are discovered: Return to earlier construction stages. **Revision is expected.**"

This matters for the recommendations. CiC does not need to be told that iteration is legitimate — its own governing document says so twice. What it lacks is any *mechanism* that makes a later-layer discovery reach back. Confidence: High.

### 0c. The real chronology of the Facilitator/Table layer

| Date | Event | Evidence |
|---|---|---|
| Pre-V7 (undated) | Alexandria/Theon prototype: a full five-layer vertical slice on one world — World, Lexicon, Representative, Facilitator Governance, and "Assembly The Table" activation documents | `Archive/Alexandria-Build-History/Alexandria-WorldBuilds/`, confirmed on `main` via `git ls-tree` |
| June 2026 | CO-001–CO-011 registered from "the L2A full review session June 2026" — including CO-003 (Representative firewall), CO-004 (forces split), CO-005 (three parallel tracks), CO-007, CO-008 | Change Orders Register V1.0 version history |
| ≤2026-07-01 | Facilitator Governance v3.0, v3.1, v3.2; Table Design v2.1; Pre-Encounter Experience Design v1.0 all present at repo initialization | `git log --diff-filter=A` |
| 2026-07-02 | "L3D production": Facilitator Governance V3.3 ("closes BLOCKING Phase 1 gap"), Table Design V2.2 → V2.3, Pre-Encounter V1.1 | commit subjects |
| 2026-07-03 | Facilitator Governance V3.4 (CO-014) | commit |
| **2026-07-07/08** | **First two worlds of the current six built** (PAHC, Syriac) | research doc 06 §1 |
| **2026-07-10** | **Runtime lands: "Add CiC POC: React frontend + LangGraph backend with multi-world table support"; then "Implement public transcript for genuine multi-representative encounter at The Table"; then, the same day, "Fix: strengthen vocabulary isolation between representatives at multi-world table"** | commits `09a59c4`, `1300daf`, `bb0698c` |
| 2026-07-11 → 07-13 | Desert, then Hieronymian built; three-Representative live testing; turn-cap incident diagnosed and Table Process ThreeRepresentative V1.0 written | commits; `CiC_L3D_Table_Process_ThreeRepresentative_V1.0.md` §6 |
| 2026-07-17 | Alexandria built; Facilitator Governance V3.7 PROPOSAL; multi-world Acute-Distress test VERIFIED PASS | commits; Decision Log |
| 2026-07-19 → 07-22 | Imperial-Juridical built; 07-20 its multi-voice test finds the anchoring gap; commit `aab5205` propagates the fix to all five other live Representatives | `Step10_Phase5_Boundary_Testing_Record.md`; commit body |

**Answer to the chronology question as posed:** the Facilitator/Table mechanisms were built **once, early, before multiple worlds existed to test them against** — *and then* iteratively refined many times as worlds were added (V3.3 → V3.4 → V3.6 → V3.7 proposal; Table Design V2.2 → V2.3; plus Table Process V1.0). Both halves of the answer are true. What never happened is the third possibility: they were never built *after* several worlds existed and needed a shared table. The specification always ran ahead of the worlds. Confidence: High.

---

## 1. Living-history and first-person historical interpretation

This is the closest real professional analogue to CiC, and it is the area where CiC comes out best.

### 1a. The field's standard text orders it exactly as CiC does

Stacy F. Roth, *Past into Present: Effective Techniques for First-Person Historical Interpretation* (University of North Carolina Press, 1998, 254 pp.) is the work ALHFAM's own First Person Interpreters group names as its primary resource. Its structure, verified from two independent renderings of the table of contents plus the Internet Archive bibliographic record:

- **Part II — Foundations for Historical Roleplaying**: Ch. 4 "Before Interpretation Starts: Planning, Research, and Development" (p. 41) → Ch. 5 "Is First-Person Interpretation Theater?" (p. 50) → Ch. 6 "Developing a Character" (p. 57)
- **Part III — Interaction across the Centuries**: Ch. 7–11, pp. 67–118 (communication challenges, the role of the visitor, breaking the ice, the art of conversation, body language)
- **Part IV — Roleplay and Relevance**: audience-specific adaptation, ending with Ch. 15 "Interpreting Special Situations: Conflict, Controversy, and Heightened Emotion" (p. 161)
- Appendix 2: "The Ultimate Character Development List" (p. 186)

Research precedes persona precedes interaction, and the hardest visitor situations come last. **This is the single cleanest external validation of CiC's order that exists.** Sources: https://books.google.com/books/about/Past_Into_Present.html?id=H4AzhOgFJHUC and https://archive.org/details/pastintopresente0000roth. Confidence: **High for the sequence, as a verified table of contents. I did not read the book — no argument, quote, or page-level claim should be attributed to Roth.**

Institutional practice corroborates. Conner Prairie's own podcast transcript has its President & CEO Norman Burns describing the method as: research the era, then create a composite character (https://assets.speakcdn.com/assets/3053/ep1transcript.pdf, **High** — official transcript, extracted in full). Old Sturbridge Village's NEH application specifies its per-space Interpretive Guides to run *internally* in the order theme/scenario → engagement tactics → frequently asked questions (https://www.neh.gov/sites/default/files/inline-files/FOIA%2020-132%20Old%20Sturbridge%20Village%202020.pdf, **High** — FOIA-released, on neh.gov). Ashlee Beattie's EXARC account describes her own preparation as research on a class of people, then fictionalization into an individual (https://exarc.net/issue-2014-2/int/interpreting-interpreter-live-historical-interpretation-theatre-national-museums-and-historic-sites, **High**).

**Verdict: ALREADY DOES THIS.**

### 1b. But the field's credentialed curricula put audience-handling *early*, and CiC has no equivalent

The National Park Service Interpretive Development Program is the only interpretation curriculum with a published, externally validated competency order. Its thirteen competencies, in printed order, begin: **(1) Knowledge of the Resource, (2) Knowledge of the Audience, (3) Knowledge of Appropriate Technique, (4) Informal Visitor Contacts, (5) The Interpretive Talk** — then conducted activities, demonstrations, writing, curriculum programs, planning, coaching, media, research. The thirteen were identified in 1995 by more than 300 NPS field interpreters and all thirteen were validated by the Office of Personnel Management in a 2003 scientific survey. Module numbering matches: 102 Informal Visitor Contacts is entry-level and precedes 103 The Interpretive Talk. Source: https://npshistory.com/publications/interpretation/interp-dev-pgm.pdf. Confidence: **High** (I confirmed the competency names, the order, the 1995/300+ provenance and the 2003 OPM validation independently; note the nps.gov/idp web tree is retired and 404s, so cite npshistory.com).

Two things follow, and they cut in opposite directions.

First, **audience knowledge and *unstructured* visitor contact are competencies #2 and #4 — both ahead of any prepared program.** The analogue in CiC is not the Representative's voice; it is the Facilitator's job of meeting a modern participant. In CiC's build sequence that work is Phase Six of Step 10 — dead last. That is a real inversion against the one validated order the field has.

Second, an honest limit: **NPS IDP contains no first-person, costumed, or character competency at all**, so it is not a sequence for CiC's whole problem. Nor is NAI's Certified Interpretive Guide: 32 hours over four days, published as a topic list rather than an ordered curriculum, with no character/first-person component, and the only ordering it commits to is that the graded ten-minute talk falls on the final day (https://coloradoopenspace.org/wp-content/uploads/2018/10/BP-2018-CIG-FLYER-Host-Organization.pdf; corroborated at https://eepro.naaee.org/learning/certified-interpretive-guide-training-course-national-association-interpretation — I independently confirmed the 32-hour/4-day figure and the absence of a published sequence). **There is no "Certified Interpretive Performer" program; NAI's six certifications are CIG, CIH, CHI, CIM, CIP, CIT.**

### 1c. There is no field-wide standard sequence, and the field says so

ALHFAM's First Person Interpreters page states an objective of promoting "high standards of quality" but **names no standards document** — its entire recommended-resources list is Roth's book plus three ALHFAM *Proceedings* items (https://alhfam.org/FPI-pig; I fetched this and confirmed directly). ALHFAM's Resource Guidelines & Policies page publishes only social-media, publication, branding, photo-release and advertising policies — nothing on interpretation methodology or interpreter training (https://alhfam.org/resource-guidelines-policies). Old Sturbridge Village's own NEH application states that its 12-month staff training calendar beginning January 2021 was the first of its kind in decades.

**This is a useful finding for CiC's self-understanding: the closest professional field to what CiC is doing has no published preparation sequence at all. CiC's Construction Framework is more specified than its real-world analogue's professional standard.** Confidence: High for the absence on public pages; note that ALHFAM's members-only *Bulletin*, *Proceedings*, and A.S.K. archive were inaccessible, so the correct claim is "not published publicly," not "does not exist."

### 1d. The first-person/third-person split, and the anachronism problem

The field's own taxonomy maps onto CiC's emic/etic distinction closely enough to be worth adopting vocabulary from. IMTAL-Americas defines **"First/Third Person"** as its own third category — interpreters shifting between character and their own voice depending on visitor needs (https://imtal.wildapricot.org/definitions/). Conner Prairie uses **"second person"** for the same idea, its "opening doors" mode: costumed and in character, but with genuine back-and-forth that can admit some modern context. Catherine Hughes's dissertation locates the difference between museum theatre and first-person interpretation in *framing* — museum theatre names itself as theatre; first-person interpretation at Plimoth leaves the framing device implied but unnamed (https://etd.ohiolink.edu/acprod/odb_etd/ws/send_file/send?accession=osu1211932278&disposition=inline, **High**, extracted in full).

**CiC's architecture is already the best-specified version of this in the comparison set.** RCF V3.2 Part One states the boundary categorically: "A Representative never shifts into Facilitator mode. A Facilitator never speaks as though inhabiting the world. The transition between them must be architecturally clear to participants at all times." Conner Prairie's CEO, by contrast, describes anachronism handling as improvised craft — the airplane answered as a large bird, the cell phone as an unfamiliar small book — and explicitly names the cost: interpreters must invent these responses at a moment's notice. Shemika Berry, writing as a practitioner, argues the encounters are fundamentally unpredictable (https://www.accokeek.org/post/hear-us-see-us-voicing-the-past, **High**). CiC's anachronism bridge, whatever its current bugs, is a *mechanism* where the field has only trained judgment.

**Area verdict: PARTIAL.** Research-before-persona: ALREADY DOES THIS, and better-specified than the field. The Facilitator/audience-handling layer's *position*: REAL GAP against the one validated competency order in the field, where audience knowledge and unstructured contact come second and fourth of thirteen. One proportionality observation worth sitting with: **eight of Roth's sixteen chapters — half the standard text — are about the interaction layer. CiC gives it two of seventeen named steps and phases, both last, both least-completed.**

---

## 2. Worldbuilding in fiction, tabletop RPG design, and game design

### 2a. "Build the world before the character" is not an established principle. The opposite is closer to consensus.

This was the clearest result of the four passes, and it is nearly unanimous across three separate fields.

- **SFWA (the professional body for science-fiction and fantasy writers) publishes the argument against world-first directly.** Nathan Nance, "The Art of Story as Worldbuilding": "In writing, character affects plot. Plot affects worldbuilding. And worldbuilding affects character" — and names the danger of the Worldbuilding First approach as getting bogged down and never finding out who your characters are (https://sfwa.org/2019/10/16/the-art-of-story-as-worldbuilding/, **High**, verbatim confirmed on a targeted re-fetch). Suyi Davies Okungbowa, also on SFWA: "It's virtually impossible to do ALL of your SFF worldbuilding prior to writing your book/story" (https://sfwa.org/2019/05/03/from-the-inside-out-worldbuilding-through-extrapolation/, **High**).
- **The field's most-cited worldbuilding checklist explicitly refuses to be a gate.** Patricia C. Wrede's "Fantasy Worldbuilding Questions" states that it is not necessary for an author to answer all, or even any, of the questions in order to start writing — parenthetically adding "or to finish writing, either" (https://sfwa.org/2009/08/04/fantasy-worldbuilding-questions/, **High**). This is directly relevant: CiC's Doc_04/Doc_05 templates are the same genre of instrument, and CiC treats them as gates.
- **There is a named pathology for over-building first.** Brandon Sanderson claims coinage of "worldbuilder's disease" on his own site, and describes novels forming at the intersection of strong ideas across world, character, and plot — needing "a couple of good ideas in each of the areas" (https://www.brandonsanderson.com/blogs/blog/worldbuilding-tools-lecture-2025, **High** for the coinage and cross-cutting framing). M. John Harrison's harsher version — "the great clomping foot of nerdism," from "Very Afraid," uzwi.wordpress.com, 27 January 2007 — survives only in reproductions since the original was deleted (**Medium**).
- **Tabletop design has the strongest statement of all, and it is open-licensed so the text is authoritative.** The *Dungeon World* SRD, "First Session": **"Character creation is also world creation, the details on the character sheets and the questions that you ask establish what Dungeon World is like."** The same page: you may draw some maps, but not "a planned storyline or plot. You don't know the heroes or the world before you sit down." Its GM principles include "Draw maps, leave blanks" (https://www.dungeonworldsrd.com/gamemastering/first-session/, https://exposit.github.io/dw-srd/dw_gm.html, **High**). *Apocalypse World*'s MC agenda includes "Play to find out what happens" (**High** for the agenda text).
- **The games industry says it outright.** The Level Design Book (Robert Yang with Andrew Yoder) has a preproduction section headed **"avoid premature worldbuilding,"** instructing designers to "worldbuild only what you need," and citing *The Witness*, where the worldbuilding had to be reconciled with an already-existing blockout and puzzle design (https://book.leveldesignbook.com/process/preproduction/worldbuilding, **High**). Its economic argument for slicing early: "It is 'cheap' to delete or rebuild some rough blockout geometry," while throwing away finished art is expensive and wasteful (https://book.leveldesignbook.com/process/blockout, **High**).

The one credible world-first voice found — N.K. Jemisin's "iceberg" argument that only ten percent shows but the other ninety percent has to be there — is about **volume, not order**, and I could not verify her sequencing claims from the primary handout (**Medium**). And the genuine character-first position exists in RPG design (Sam Dunnewold, "Design Your Character Sheet First," https://diceexploder.substack.com/p/design-your-character-sheet-first, **High**) with its own iterative caveat: "it's also probably the last thing you should finalize."

### 2b. On the interaction/session layer specifically

Two findings.

**"Session zero" is a documented practice step that sits before session one and *bundles* character creation with world/campaign creation** — Justin Alexander traces the term to RPGNet in July 2003, with lineage through Aaron Allston's *Strike Force* (1988), 1990s Amber diceless communities "combining character creation with world-building," and *Burning Empires* (2006) as the first game whose designer explicitly said to spend a full session on it (https://thealexandrian.net/wordpress/41262/roleplaying-games/thought-of-the-day-evolution-of-session-zero, **Medium** — one researcher's account, though sourced). Alexander's better-known maxim — **"Don't prep plots, prep situations"** (https://thealexandrian.net/wordpress/4147/roleplaying-games/dont-prep-plots, **High**) — is real but scoped to scenario prep, not to world-vs-character order; don't overreach with it.

**Robin D. Laws's *Hamlet's Hit Points* treats the session layer as its own designed artifact — a beat structure, independent of world detail.** That is the useful shape for CiC: the Table is not a byproduct of world completeness; it is its own designed thing with its own grammar. CiC already believes this (CO-005's Track 3, world-neutral). The precedent supports it. **Medium** (secondary discussion only).

**Area verdict: PARTIAL.** CiC's *reason* for world-before-Representative is stronger than anything in these fields — Table Design V2.3 §10 grounds it in a formation-depth requirement, not convenience, and the anti-fabrication firewall (CO-003, Article 28) is a real constraint fiction writers don't have. **REAL GAP** on the "build only what you need, then iterate" half: CiC's per-world gate loop is strictly forward-only despite its own Part VII saying the workflow is not strictly linear.

---

## 3. Multi-agent AI system design and orchestration

This area produced the strongest external evidence in the document, and the most surprising result: **the literature's central recommendation is precisely what the Fable brief already asks for.**

### 3a. No framework recommends isolate-then-integrate. That absence is itself the finding.

I looked, via the dispatched pass, at LangChain/LangGraph multi-agent docs, LangSmith evaluation docs, AutoGen/AG2, and CrewAI. **None recommends validating individual agents in isolation before building orchestration. None warns against it by name either.** LangSmith's own agent-evaluation page names three evaluation types — final response, trajectory, and single step — and prescribes **no order** among them; its stated rationale for having three is diagnostic granularity, not sequence (https://docs.langchain.com/langsmith/evaluate-complex-agent, **High**).

Anthropic's "Building effective agents" (19 Dec 2024, https://www.anthropic.com/engineering/building-effective-agents) is a *scope* escalation ladder — don't build multi-agent unless the task needs it — **not** a build-order instruction. It should not be cited as endorsing component-first validation. **High.**

### 3b. Composition failure is real, measured, and large

Four primary sources, all of which I re-verified myself.

**The most directly relevant paper is about the shared layer.** Camilo Chacón Sartori, "The Specification Gap: Coordination Failure Under Partial Knowledge in Code Agents," arXiv 2603.24284 (25 March 2026). Across 51 class-generation tasks with specification detail progressively stripped from full docstrings (L0) to bare signatures (L3): **two-agent integration accuracy falls from 58% to 25%, while a matched single-agent baseline degrades from 89% to 56% — a 25–39 percentage-point coordination gap**, consistent across two Claude models (Sonnet, Haiku) and three independent runs. The gap decomposes into coordination cost (+16 pp) and information asymmetry (+11 pp), approximately independent and additive. Its recovery experiment is the load-bearing part: **restoring the full specification alone recovers the single-agent ceiling (89%), while an AST-based conflict detector achieving 97% precision at the weakest specification level adds no measurable benefit.** I fetched the abstract and confirmed every one of these numbers appears in it. Confidence: **High**.

The paper's own framing is that the problem is agents needing to agree on shared internal representations the specification leaves *implicit*. **For CiC this is close to a direct hit: the recommendation is make the shared layer explicit up front, and downstream detection tooling does not substitute for it.** That is what the brief's §9 (one structured record per addressable unit, typed `field_relations`, `register: emic/etic`) already proposes. The literature says that is the intervention that works, and that adding more monitors instead does not.

**Aneesh Pappu et al., "Multi-Agent Teams Hold Experts Back," arXiv 2602.01011** (1 Feb 2026; v4 28 May 2026). Self-organizing LLM teams consistently fail to match their own expert agent's performance **even when explicitly told who the expert is, with losses up to 41.1% on ML benchmarks.** Expert *leveraging*, not identification, is the bottleneck; the mechanism is "integrative compromise" — averaging expert and non-expert views rather than weighting expertise — which increases with team size and correlates negatively with performance. Notably, the same consensus-seeking improves robustness to adversarial agents. All verified in the abstract. Confidence: **High**.

**This one should worry CiC specifically.** "Integrative compromise, increasing with team size" is a formal, measured description of exactly the failure the four-voice roundtable's independent reviewer flagged as "closing-speaker synthesis bias" and "false unanimity," and exactly what Facilitator Governance §15 lists as unvalidated convergence drift. It is also the mechanism behind doc 10's headline finding. The paper says it gets worse with team size — which bears directly on CiC's three-vs-five world ceiling.

**Mert Cemri et al., "Why Do Multi-Agent LLM Systems Fail?" arXiv 2503.13657** (UC Berkeley et al.; v1 17 Mar 2025, v3 26 Oct 2025). 14 failure modes in 3 categories — system design issues, inter-agent misalignment, task verification — from 150 traces, inter-annotator κ = 0.88, with a 1600+ trace dataset. The paper attributes the bulk of MAS failure to organizational design and agent coordination rather than to individual agents' limitations. **Important citation discipline: the 41.77% / 36.94% / 21.30% category split lives in Figure 1 and on the authors' project site (https://sites.google.com/berkeley.edu/mast/), not in the abstract or body text — I verified this directly. Cite the site, not the paper, for those numbers.** Confidence: High for the taxonomy facts; Medium for the percentages' provenance.

**Christian Schroeder de Witt et al., "Open Challenges in Multi-Agent Security," arXiv 2505.02077**: individually safe agents can compose into unsafe systems; security in multi-agent systems is non-compositional; emergent multi-agent behaviors cannot be predicted by analyzing individual agents in isolation. The domain is security, so this transfers to quality/behavior by analogy, not directly — but it is the cleanest general statement of the principle. Confidence: High.

**Anthropic, "How we built our multi-agent research system"** (13 Jun 2025), which I fetched and confirmed: "Multi-agent systems have emergent behaviors, which arise without specific programming. For instance, small changes to the lead agent can unpredictably change how subagents behave." On evaluation: "it's best to start with small-scale testing right away with a few examples, rather than delaying until you can build more thorough evals" — they began with about 20 queries — and evaluate whether the correct *final state* was achieved rather than whether a specific process was followed. **The post does not describe the order in which they built the system; I checked. Do not claim it does.** It also flags, honestly and against CiC's interest, that "Some domains that require all agents to share the same context or involve many dependencies between agents are not a good fit for multi-agent systems." Confidence: High.

### 3c. The software-engineering precedent

Martin Fowler's "Continuous Integration" (rev. 18 Jan 2024) gives the cost shape: the longer between integrations, the more code to integrate and the longer it takes — but worse is the increase in *unpredictability*; because integration is about connections, twice the code can mean roughly four times the integration effort; teams historically spent months in "integration hell" (https://martinfowler.com/articles/continuousIntegration.html, **High**). **The transferable point is not that deferred integration is expensive — it is that its duration is unestimable.**

Alistair Cockburn's **Walking Skeleton (1996)** is the direct analogue of a thin slice through all layers, defined on his own site as "A thinly connected functioning architecture" (https://alistaircockburn.com/Bio, **High**). The fuller *Crystal Clear* (2004) definition is **Medium** — secondary only; his dedicated wiki page 404s at every URL form.

**Area verdict: PARTIAL, and the most encouraging result in this document.** REAL GAP: the composition-failure evidence says component-level validation systematically under-predicts composed behavior, and CiC's Freeze Criteria validate components. ALREADY DOING THE RIGHT THING: the literature's own primary remedy is an explicit shared specification layer, which is exactly what the redesign brief targets — and the specification-gap paper's finding that conflict-detection tooling adds nothing once the shared layer is explicit is a direct caution against solving this with more drift monitors.

---

## 4. Method-acting and performance-training precedent

Real, relevant, and honestly limited.

### 4a. Circumstances before character is real, as order-of-practice rather than doctrine

The published curriculum order of Stanislavski's own *An Actor's Work: A Student's Diary* (trans. Benedetti) puts Ch. 3 "Action, 'if', 'given circumstances'" well before Ch. 10 "Communication," with external and physical characterisation in Year Two (Part 2, "Embodiment," chs. 17–29) — per the Stanford Libraries contents listing (https://searchworks.stanford.edu/view/13769235, **High as a table-of-contents fact**). **This is a curriculum's structure, not a sentence in which Stanislavski states a rule. Do not upgrade it into a quoted prescription.**

Stella Adler's technique is described as examining the script closely to determine circumstances, then aligning action with them (Dramatics Magazine, **Medium**). Uta Hagen's nine questions place identity first ("Who am I?"), circumstances at 2–5, relationships at 6, objectives at 7–9 — **so Hagen is a clean circumstance-before-*interaction* precedent, not a circumstance-before-*character* one** (**Medium**; two sources give conflicting orderings, so treat the exact list as unsettled). Dramaturgical practice presents a world-of-the-play at the first rehearsal, before the first read (Educational Theatre Association, https://schooltheatre.org/dramaturgy-101/, **Medium-High**).

### 4b. Two real traditions start the interaction layer early — and one exam board prints the order

**Active Analysis** is the strongest precedent, and it is published with a numbered sequence by a UK exam board: read a bit of the play → discuss the main event → discuss each character's main action → **discuss the given circumstances of the bit** → put scripts down and **improvise the bit** → discuss results and refine actions → *then* discuss objective, relationship, super-objective → improvise again → discuss and re-read (OCR A Level Drama & Theatre, *Topic Exploration Pack: Practitioners – Stanislavski*, https://www.ocr.org.uk/Images/221759-practitioners-stanislavski.doc, **High**). The same pack records the shift: early Stanislavski analysed the play in depth around a table; Active Analysis got students on their feet exploring actively, with the stated rationale that a long analysis stage can soak up the actor's inspiration for the role. Independently corroborated by *Didaskalia* (peer-reviewed): actors "read an episode, discuss briefly the important facts and event(s), and then play it in their own words," with lines learned after the event is experienced psychophysically (https://www.didaskalia.net/issues/vol7no2/wain.html, **High**).

**Given circumstances are settled before the first partner improvisation; objectives, relationships and super-objective are worked after it.** That is a real, citable precedent for CiC starting table work before the Representative's fine calibration is finished.

**Meisner training is interaction-first outright.** The Neighborhood Playhouse — Meisner's own school — describes Year One as repetition, scene work, voice, movement and text, with **character development named as Year Two content** (https://neighborhoodplayhouse.org/programs, **High**). Partner responsiveness is trained as the foundation, with no character and no scene at the start.

### 4c. The honest limit

**No major acting tradition states a threshold rule of the form "partner work begins at stage N of character development," and the tradition is not unanimous.** Reputable contemporary studio pedagogy teaches the opposite order — solo homework first, partner exploration second (Terry Knickerbocker Studio, https://terryknickerbockerstudio.com/the-actors-rehearsal/, **Medium**). And Stanislavski did not *abandon* table work; the sources say minimised, reduced, or shortened.

**Area verdict: PARTIAL.** Given-circumstances-before-character: ALREADY DOES THIS, with real precedent. Early partner work: a legitimate, citable precedent for a design choice — **not inherited orthodoxy, and it should be presented to Mark as CiC's own choice supported by precedent, not as a rule CiC is violating.**

---

## 5. Iterative vs. waterfall — the central question, answered honestly

**Strict sequential order — fully finish layer one, then fully finish layer two, then build the interaction layer — is not documented as best practice in any of the four fields.** Not one source in any of the four passes recommends it. Several name it as a failure mode under its own names: "worldbuilder's disease" (Sanderson), "premature worldbuilding" (Level Design Book), "integration hell" and unestimable integration duration (Fowler), horizontal slicing's costs — no early feedback, risk of building the wrong thing, reduced flexibility (Thoughtworks, https://www.thoughtworks.com/insights/blog/slicing-your-development-work-multi-layer-cake, **High**), "phased"/"big-bang" integration (software engineering generally; **note that I could not verify ISTQB's or McConnell's actual wording — see Do not cite**).

The recommended alternative has the same shape everywhere it appears: **a thin, working slice through every layer, early, then deepen.** Cockburn's Walking Skeleton; the games industry's blockout and vertical slice; Anthropic's "start with small-scale testing right away with a few examples"; *Dungeon World*'s "draw maps, leave blanks"; Active Analysis's brief framing then straight onto the floor; Old Sturbridge Village's draft → scholar review → **pilot with visitors** → refine.

**But here is the finding that makes this a fair report rather than an indictment: CiC has already done this, twice, and both times it worked.**

The pre-V7 Alexandria/Theon prototype was a five-layer vertical slice on one world, and CO-008 records that the governing Table Design and Facilitator Governance documents "emerged from what those tests revealed." And `CiC_L3A_Phase_Structure_V1.1` sets the Gate to Prototype Alpha as "**Two-world table proven end-to-end**" — a two-world thin slice — which was satisfied on 2026-07-10, three days after the second world was finished, and immediately found real cross-world vocabulary contamination the same day.

**So the diagnosis is not "CiC is a waterfall." It is narrower and more actionable: CiC iterates at the whole-system level, occasionally and opportunistically, but never inside a world's own build loop. The per-world loop is strictly forward — Doc_01 through Doc_09, freeze, then Phases One through Seven — with no step at which a table result can block, reopen, or inform anything. Every one of the four table-discovered defects in §6 was routed sideways, into a Known Limits list or a separate branch's test record, not back into the gate that would have caught it in the next world.**

**Verdict: REAL GAP — but in the feedback path and the gate placement, not the layer order.**

---

## 6. CiC's own track record: does the evidence show real harm?

Mark asked for an honest yes or no. The answer is **yes, four documented instances of harm, and none of them argue for reordering the sequence.**

### 6a. Four defects that only the table could produce

1. **Cross-world vocabulary contamination, day one of the table's existence.** Commit `bb0698c`, 2026-07-10 17:36: "Representatives were adopting each other's terminology when responding to the public transcript. Updated the prompt guidance to explicitly forbid borrowing another world's vocabulary (e.g., Amma should not use 'raza' or 'qyama' from the Syriac tradition)." Both worlds had already cleared their own builds. Confidence: High.

2. **Anachronistic vocabulary under multi-voice pressure, and closing-speaker synthesis bias.** From the four-voice roundtable (`git show CiC-Fable-Experiment:World-Builds/Cross_World_Roundtable_Validation.md`, PART II). The record's own words on the first: it "suggests that under live, unscripted cross-world dialogue, a voice may reach for a familiar-sounding but temporally wrong word... **This was not previously tested by any single-world probe (all of which test a voice in isolation).**" The second is purely structural: "whoever speaks last in a multi-Representative roundtable gains an unearned rhetorical authority to characterize consensus, regardless of content-level disagreement." **Both were routed to Facilitator-Governance Known Limits §15 rather than into any world's build gate or the Construction Framework.** Confidence: High.

3. **The turn-cap incident.** `CiC_L3D_Table_Process_ThreeRepresentative_V1.0.md` §6: at a six-turn ceiling, later turns truncated or returned empty; root cause was the model emitting an interleaved extended-thinking block on every token-capped call, consuming the reactive turn's budget before visible text was written; fixed by disabling extended thinking on token-capped calls, confirmed across eight consecutive trials. **Unreachable at any single-world scale — it requires a chained multi-turn round.** Confidence: High.

4. **The sharpest instance: a table requirement that reached no deployed artifact for the project's entire life.** RCF V3.2 Part Five requires a Representative referencing another Representative to "anchor clearly to that world's own name in reported speech." IJC's Round 4 multi-voice test, 2026-07-20, found this convention "does not actually exist as instructional text in Marius's, Albina's, or Papnoute's real deployed Permanent Prompts." Commit `aab5205`'s own body goes further: "This was never operationalized as instructional text in **any** of the five live deployed prompts — confirmed by direct read, not assumed," including a self-correction that Theon had been believed to have it but the convention lived only in his build documentation. **A governing requirement, in the framework the whole pipeline follows, reached zero of five deployed artifacts, and only a multi-voice test on the sixth world surfaced it.** Confidence: High.

**The good news, stated as plainly:** the fix propagated. Commit `aab5205` wrote it into all five live prompts, each in that world's own idiom rather than copied wording — Chloe's from her letter-trust imagery, Mar Yausep's from precision about names, Papnoute's extending "a story belongs to the one who lived it," Albina's from manuscript-checking, Theon's from reading-as-a-door. I verified all six deployed prompts under `cic-poc/backend/data/` carry it today. This is the feedback path working — once, manually, at Mark's direct request, after six worlds.

### 6b. Three sequencing consequences visible in the artifacts

**The circular freeze gate.** Freeze Criteria (V7.3 and V7.4, identical) require "representative voices are accountable and appropriately grounded (per CO-014)" and "encounter testing is successful." Step 10 says the Representative emerges from "the completed and frozen world's ecology." The Representative must exist to satisfy freeze, and freeze must precede the Representative. World #1's Step-9 validation document resolves this by deferral, stating up front that four of Part VI's fifteen categories — Relational Safety, Adversarial Resistance, Encounter Testing, and the representative-voice component of Living Tradition — "require probing an actual built Representative in dynamic exchange. No Representative exists yet for this world." **The Framework partly anticipates this in its own text**, noting for Adversarial Resistance that "concrete adversarial test cases should be developed once the runtime layer exists and can actually be tested against." That is an honest and correct instinct — it just never became a second, named gate. Confidence: High.

**The blocked probe.** World #1's Phase Five independent verification recorded Relational Safety as "FAIL against deployment readiness / CANNOT BE SCORED against Part Eight's stated criterion — blocking," having confirmed by direct read that no handoff mechanism existed anywhere in the world's artifacts, and concluded: "World #1 must not be exposed to real participants until Phase Six exists and this exact probe category is rerun successfully against an actual handoff mechanism." **A probe category was structurally unscorable because Phase Six had not been reached yet — a pure consequence of ordering, correctly diagnosed at the time as "expected and non-blaming at this stage of the ten-step build sequence."** Confidence: High.

**Phase Seven contradicts its own number.** RCF V3.2 Phase Seven, "Encounter Ecology Mapping," opens: **"Before Representative construction begins, identify: what dimensions of the world generate meaningful encounter..."** — and is numbered last, after Boundary Testing and Facilitator Coordination. Empirically: **1 of 6 worlds produced one** (Syriac), and research doc 03 records it as "an explicitly retrospective audit... **inverting its own governing text's intended sequencing**." Confidence: High.

### 6c. The hardest number: the Facilitator's only channel from the world layer is the least-finished artifact in the pipeline

Facilitator Governance V3.6 §5 names its single data source verbatim: "Your curatorial judgment draws on structured knowledge about each available world. **The World Facilitation Brief produced at the completion of every world build — specifically Section B, the Facilitator Selection and Management Brief — is the source of this knowledge.**"

That artifact is produced at RCF Phase Six. Its status across six worlds, read directly:

| World | Phase Six artifact | Review status |
|---|---|---|
| Post-Apostolic House-Church | `CiC_W1_Phase6_Facilitation_Brief_B1-B6_DRAFT.md` | **Cleared review in full** (Section A and B1–B7) |
| Syriac | `Syriac_Phase6_Facilitator_Coordination_DRAFT.md` | **Cleared Round 1 + a dedicated MetaReview** |
| Alexandria | `Alexandria_Facilitation_Brief_v1_0.md` | No review artifact exists; produced 2026-07-17 while Step 10 was still underway, world "**NOT frozen**" per its own header |
| Desert-Monasticism | `CiC_W3_Phase6_Facilitation_Brief_DRAFT.md` | Produced by a separate integration pass, not the build thread; **unreviewed** (research doc 03: "remains unreviewed... no review-round file exists for it anywhere") |
| Hieronymian | `hal_Phase6_Facilitation_Brief_DRAFT.md` | Its own header: "**This brief has NOT itself cleared this project's own independent adversarial review process.**" |
| Imperial-Juridical | **none** | The last world built has no Phase Three, Four, Six or Seven artifact at all |

**Two of six worlds have a fully review-cleared World Facilitation Brief.** The Facilitator's structured knowledge of the portfolio is unratified for three worlds and absent for one. Confidence: High.

### 6d. The seam, measured

The three governing documents barely share vocabulary. Counts from the extracted full text:

| Measure | Result |
|---|---|
| Construction Framework V7.4 — occurrences of "table" | **0** |
| Construction Framework V7.4 — "multi-world" / "multi-representative" / "other representative" | **0** |
| Table Design V2.3 — references to any `Doc_0N` | **0** |
| Table Design V2.3 — references to any numbered build Step | **0** |
| Table Design V2.3 — references to the world's forces analysis | **0** (the single "forces" regex hit was "enforces") |
| Facilitator Governance V3.6 — references to any `Doc_0N` or numbered Step | **0** |
| Facilitator Governance V3.6 — occurrences of "forces" or "gravit" | **0** |
| Facilitator Governance V3.6 — total references to world-build artifacts | **4** (Permanent Prompt ×2, World Facilitation Brief ×1, World Capsule ×1) |
| RCF V3.2 — occurrences of "table" | 5 — the only real bridge, and a thin one |

**Confidence: High.** This is the measurable form of the brief's §5d diagnosis. The Facilitator's governing document has no vocabulary for the world-build's own analytical outputs — not underused, absent.

### 6e. What CiC gets right, said plainly

Three things should not be changed, and one should be actively defended.

- **Table Design V2.3 §10 is correct and well-argued.** "This is not a sequencing convenience. It is a formation depth requirement... A shallow Representative at the Table does not blend in. It is exposed... **The multi-world Table is not a context that compensates for insufficient world-building. It is a context that reveals it.**" No external source contradicts this. The Chacón Sartori result arguably supports it: a poorly-specified shared layer is where composition fails.
- **The construction-time/runtime split on cross-world contamination is drawn cleanly and correctly.** Constitution Article 3 makes construction-time contamination a defect that "must be caught before a world is advanced toward freeze." RCF V3.2 then states explicitly that "Runtime isolation between worlds at a shared multi-world table... is a runtime governance concern owned by Facilitator-Governance, **not a construction-time problem the builder must independently solve.**" That is a clean handoff, and I want to be clear I looked for a contradiction here and did not find one. The only issue is that the receiving mechanism is the one Facilitator Governance §15 names as unvalidated.
- **Facilitator Governance §15 is a model of intellectual honesty.** "The governance specified in this document is specified with more precision than it has been validated. The following limits are known and acknowledged. They are named here not to qualify the governance but to be honest about what has and has not been tested." Most projects do not write that sentence. The recommendation below is not to write it better — it is to make it a gate.
- **CiC's Construction Framework is more specified than its closest real-world professional analogue's standard.** ALHFAM publishes no preparation sequence. NAI's CIG publishes a topic list. NPS IDP has no character competency. Old Sturbridge Village called its own 2021 training calendar the first in decades. That context should temper any conclusion that CiC's process is behind the field.

---

## 7. Recommendations

The order is right. Do not reorder it. Six changes, ordered by evidence strength and cost.

**1. Add one gate, not a resequence: a "Table Readiness Round" as a named Phase Eight of RCF Step 10, and a corresponding Freeze Criterion.** The world stays first; the Representative stays firewalled; nothing above Step 10 is touched. The new phase runs the newly-built Representative at a table with **one** already-live Representative from a different world, on one question where the two worlds genuinely diverge, and grades three things the solo probes structurally cannot: cross-world vocabulary borrowing, anachronistic reach under multi-voice pressure, and whether the world holds its own position rather than converging. This is CiC's own Phase Structure gate ("Two-world table proven end-to-end") pulled down from the release level to the per-world level. It also gives the existing Freeze Criterion "encounter testing is successful" something it can actually mean — today it is unsatisfiable at the point it is stated. Evidence: all four defects in §6a; Pappu et al.'s finding that integrative compromise worsens with team size argues for testing at two before seating three.

**2. Resolve the two literal ordering contradictions, both of which are one-line edits.** Renumber RCF Phase Seven ("Encounter Ecology Mapping") to run where its own text says it runs — before Representative construction begins, i.e. as Phase Zero or as a Step 9 deliverable. It has been executed once in six worlds, retrospectively, and the number is why. Separately, split the Freeze Criteria into world-freeze criteria and representative-freeze criteria, so "representative voices are accountable" and "encounter testing is successful" sit in the second list rather than the first. World #1's validation document already improvised this split ("Part VI is sequenced across two stages of this world's build, and this document only closes the first") — codify what a build thread already had to invent.

**3. Make the seam a documented interface, since the count is zero.** Construction Framework V7.4 mentions the table zero times; Facilitator Governance V3.6 mentions forces and gravities zero times. Whatever the Pass 1 schema turns out to be, at least one document must name which world-build fields the Facilitator and turn-selector read, and the Construction Framework must name the table as a downstream consumer so a builder knows the obligation exists. The strongest external evidence in this document points here: Chacón Sartori's recovery experiment found that restoring the shared specification recovered the full single-agent ceiling while a 97%-precision conflict detector added *nothing*. **Read as a caution: making the shared layer explicit is the fix; adding a seventh drift monitor is not.** This reinforces brief §10 deliverable 5 rather than adding to it.

**4. Fix the Facilitator's single data channel, because two of six worlds have a ratified one.** The World Facilitation Brief Section B is, by Facilitator Governance's own words, "the source of this knowledge." Either bring Desert's, Hieronymian's and Alexandria's through review and write Imperial-Juridical's, or — better, and aligned with brief §9 — stop hand-authoring it and generate it from the dataset, so it cannot be the one artifact a build thread runs out of energy before finishing. Note the shape of the failure: the last world built skipped it entirely. A hand-authored artifact at the end of a 17-step sequence is the thing that gets dropped.

**5. Give table findings a routing rule, since sideways is where they currently go.** Both roundtable findings went into Facilitator Governance Known Limits §15 and stopped. The anchoring-convention gap sat in builder guidance and reached zero deployed prompts. The rule needs to be: **a finding from a table test is classified at the moment it is found as (a) a Facilitator/runtime matter, (b) a per-world artifact defect requiring propagation to every live world, or (c) a Construction Framework or template change**, and (b) and (c) carry the same propagation discipline CO-022 already established for name changes. Commit `aab5205` is the proof this works — it just took six worlds and a direct request from Mark to happen once.

**6. Two smaller items.** Reconcile CO-004's stated step numbers (Step 3 / Step 7) with what the framework implements (Step 1 / Steps 7–8) — an ADOPTED sequencing change order whose own numbers are stale is a governance-drift instance in exactly the area being audited. And extend the Prototype Testing Charter V1.0 to a multi-world configuration; it is currently written for a single named Representative, which means the first real participants would test the one thing Facilitator Governance §15 says is least validated with no charter covering it.

**What not to do.** Do not build the Facilitator/Table layer "earlier" — it was already first. Do not weaken the Step 10 firewall; CO-003 exists because the Representative was leaking into the build, Article 28 depends on it, and nothing in four fields' worth of methodology argues against it. Do not adopt "thin slice" as a replacement for the sequential build; the games industry's blockout, Cockburn's walking skeleton and Anthropic's twenty test queries are all *additions* to a real construction process, not substitutes for one. And do not treat the acting precedent as a mandate — no tradition sets a threshold rule, and reputable studio pedagogy teaches the opposite order.

---

## Do not cite

Fifteen items I or the dispatched passes could not verify. Nobody should quote these on my authority.

1. **Roth's chapter *contents*.** Only the table of contents was verified, from two renderings plus the Internet Archive record. No argument, quote, page-level claim, or terminology should be attributed to Roth. A full PDF circulating at trojanhorse.fi appears to be an unauthorized copy and was not opened.
2. **Roth's reported "five-sphere framework of knowledge"** (personal, local, occupational/domestic, stational, worldly) — appeared only in a search snippet of a Project MUSE review that could not be opened.
3. **Roth's reported terms "pseudo-first person," "hypothetical first person," "interactive third person"** — no source found for any of the three.
4. **Any ALHFAM published interpretation standard or training sequence.** Verified absent from ALHFAM's *public* pages. The members-only *Bulletin*, *Proceedings*, and A.S.K. archive were inaccessible. The correct claim is "not published publicly."
5. **Contents of every ALHFAM *Proceedings* article** cited by the FPI page (1997 and 1999 workshop papers; Kelleher's "Historical Interpretation 101," 2022). Citations verified; content entirely unread.
6. **NAI's own website content.** interpnet.com and nai-us.org both return 403 to automated fetching. All CIG detail here comes from an NAI-authorized trainer's flyer and NAAEE's listing.
7. **NPS IDP's Module 103 costumed-interpretation lesson plan** ("Is Living History or Costumed Interpretation Right for My Site?"). The nps.gov/idp URL is dead; title and topics come from search-index content only.
8. **Plimoth's pre-season small-group rehearsal** and Plimoth's "personation biographs" as a Plimoth-published artifact. The Yankee/newengland.com source 403s; the biographs detail is EXARC reporting Plimoth practice, not a Plimoth publication. This is load-bearing for "in-group rehearsal before public performance" — verify by hand.
9. **Colonial Williamsburg's own account of Nation Builder preparation** (4–8 hours/day primary-source reading; months of study before first appearing as Patrick Henry). colonialwilliamsburg.org 403s. The two relevant *Trend & Tradition* articles are real and worth a human read.
10. **John Luzader's reported statement** that very few collegiate courses in costumed interpretation exist. The source page failed three fetches and the search summary garbled his affiliation. This would be the most quotable confirmation of the "no field-wide standard" finding — verify the quote, title and date before using it.
11. **Jane Malcolm-Davies, "Borrowed Robes"** (*IJHS* 10(3), 2004) and its companion. All four access routes blocked. Its training findings are likely the most relevant in the literature and are entirely unverified.
12. **Mary Kay Cunningham, *The Interpreter's Training Manual for Museums* (AAM, 2004)** — the single most likely source for a documented training sequence. No table of contents obtained. Worth chasing.
13. **MAST's category percentages (41.77 / 36.94 / 21.30).** I confirmed directly that these do **not** appear in arXiv 2503.13657's abstract or body text — they live in Figure 1 and on the authors' Berkeley project site. Cite the site. An earlier automated read of the HTML guessed "~44/~32/~24" from the figure; those numbers are wrong.
14. **The "41%–87% production failure rate"** in arXiv 2605.03310. Verified only as an assertion in that preprint's abstract; the upstream source is unverified. Do not present as a measurement. The paper's architectural argument — coordination as a separable configurable layer — is fine to cite as its own contribution.
15. **ISTQB's and McConnell's actual wording on big-bang / phased integration.** The ISTQB glossary returns 403 and the syllabus PDFs were unextractable; *Code Complete* 2e ch. 29 section titles were verified but the text was not read. Use Fowler and Cockburn, which are verified, and describe big-bang integration as a widely-reported anti-pattern rather than quoting a standard.

Also flagged: **Cockburn's fuller *Crystal Clear* Walking Skeleton definition** (Medium — his dedicated wiki page 404s at every URL form; the Bio-page definition "A thinly connected functioning architecture" is verified). **Mythcreants' "Which Should Come First"** — 403 on two attempts, never loaded; do not quote. **Ron Edwards' Forge Provisional Glossary** — SSL failure; big-model.info is unattributed. **Schell's "Rule of the Loop" wording** — secondary only. **"Worldbuilder's disease" is confirmed *not* to be a TV Tropes page** — attribute to Sanderson's own site. **There is no NAI "Certified Interpretive Performer."** **The "conversational interpretation" citation** (M.K. Cunningham, *Public Garden* 16(3), 2001) is verified as a citation from Hughes's bibliography; the article is unread. **Vertical slice** has no first-party publisher or GDC definition I could reach — the Thoughtworks agile parent concept is the verified citation; the games-industry version is Medium.

---

*Compiled 2026-07-26 for `Ministry/Operations/Audits/CiC_Redesign_Research_2026-07-25/17_Build_Process_Sequencing_Methodology.md`. Deliberately does not re-cover doc 16's turn-selection ground, doc 04's template-verification ground, or doc 06's defect-rate ground; where a finding touches them it is because the build *sequence* is the cause rather than the schema or the review discipline.*
