# CHURCH IN CONVERSATION
## V7 Upgrade Reference — Coach Orientation

*Review criteria · Build criteria · Contamination detection · Pipeline · V7 upgrades*

## Purpose of This Document

This document orients the Coach thread to the full scope of work in the current cleaning and upgrade pass. Every document in the CiC repository is being reviewed and cleaned against two simultaneous standards: (1) contamination detection — removing what should not be there, and (2) V7 upgrade implementation — ensuring every document reflects the V7 architecture that the locked Level 1 foundation now governs. A document that is clean of contamination but still reflects pre-V7 architecture is not ready to file.

## The Pipeline — How Every Document Moves

Every document passes through six steps. Do not skip steps. Do not blend Critic and Builder roles.

- **Step 1:** Coach reads the document from the repository and produces a pre-review assessment — what this document is, what job it does, and every issue identified organized by type.
- **Step 2:** Coach drafts the Opus Critic review prompt and presents it to the project lead for approval before sending.
- **Step 3:** Opus Critic reads the document from the repository and conducts the full adversarial review. Findings come back to the project lead.
- **Step 4:** Coach reads the Critic findings and produces a decision table — Accept, Defer, or Reject for each finding, with reasoning. Project lead makes the final call.
- **Step 5:** Coach drafts the Opus production prompt specifying exactly what to change, based only on approved findings. Project lead sends to Opus Critic thread.
- **Step 6:** Opus Builder applies approved changes and writes the corrected file to the repository. Coach reads the new file and runs a verification pass. If changes were substantial, a second Critic pass is requested before filing.
- **File and commit:** When verification passes, project lead files the document and runs the Git commit: `git add .` / `git commit -m 'description'` / `git push`

Log every document's pipeline status in `Build/reference/Project-Reference/CiC_Cleaning_Pattern_Log.md`. Add new contamination patterns to the log as they are discovered.

## The Cleaning Standard — Two Checks on Every Document

### Check One — Generalization Integrity (Six Contamination Types)

Every sentence is tested: could this have been written by someone with zero exposure to any specific world, Representative, theological tradition, or formation gravity — working only from the Mission and the Five Convictions?

**Type ONE — Name Residue.** Any world name, Representative name, figure name, place name, or tradition name appearing in a governance or methodology document as if universal. The five-world registry is the only permitted exception in Level 2A documents, and only as an architectural identifier — not as a status report.
- Watch for: "Alexandria has progressed furthest," "realized for one world (Alexandria)," "Origen," "Theon," any named artifact of a specific world.
- The test: replace the name with a different world. Does the sentence still make sense? If not, the name is load-bearing and must be replaced with world-neutral language.

**Type TWO — Shape Residue.** Structural assumptions drawn from specific worlds appearing as universal features of Christian formation. No proper nouns required — the contamination is in the assumed shape.
- **Alexandria shape:** single towering intellectual figure at the center, Logos theology, Greek philosophical register, contested textual tradition, fracture along orthodoxy/heterodoxy lines, intellectual encounter with Scripture as the formation axis, connection to a specific living tradition.
- **Desert Christianity shape:** anchoritic strand centering, martyrological combat frame, elder-disciple relational structure, apophthegmata as primary source type, suffering and resistance as default register, embodied ascetic practice as the formation axis, withdrawal from the world as the governing posture.
- **Early Communal / Ecumenical-Communal shape:** Pachomian koinonia structure, shared daily life as the formation axis, communal theology, ordinary faithfulness as the default register, household and table as governing images.
- The test: does this sentence apply without modification to a fourteenth-century English lay mystic, a seventeenth-century German Pietist, a twentieth-century African independent church, and a second-century North African martyr community simultaneously? If not, it is contaminated.

**Type THREE — Theological and Gravity Residue.** Specific theological concepts or gravity types appearing in methodology as examples of what formation universally involves. These belong to particular worlds — when they appear as universal examples they are contamination.
- Watch for: Logos, theosis, apatheia, koinonia, hesychasm, kenosis, apophthegmata, anamnesis, perichoresis used as methodology examples.
- Also watch for: gravity-type assumptions — assuming every world has a textual gravity, a Christological gravity, a master-disciple relational gravity, or a doctrinal controversy at its center.

**Type FOUR — Gendered Residue.** Any pronoun or behavioral assumption written around a specific Representative presenting itself as universal standard.
- Watch for: "his tradition," "he argues," any behavioral example that only fits a particular Representative type.
- Correct to: "their tradition," neutral constructions throughout.

**Type FIVE — Register Clustering.** Examples, illustrations, or assumed world shapes that all share the same era, geography, or intensity register — when the system is designed for throughout history and today.
- Watch for: multiple examples all ancient, all Egyptian/Near Eastern, all intellectually contested, all ascetically intense, all martyrdom-shaped.
- The system must serve equally: gentle, stable, devotional, contemplative, contemporary, non-Western, oral, communal, affective traditions.

**Type SIX — Doctrinal Framework Residue.** Any assumption that formation worlds will be organized around doctrinal controversy, creedal precision, or a particular soteriology.
- Watch for: "the world's defining tension between orthodoxy and heresy," "the doctrinal controversy at the center of this world's formation," any maturity framework that treats doctrinal precision as the marker of mature formation.
- Many worlds organize their formation around hospitality, grief, wonder, embodied labor, vernacular Scripture, affective encounter — not doctrinal controversy.

### Check Two — Rule 1A and Rule 1B Compliance

- **Rule 1A: No Downstream Causation** (Constitution Article 36). A document may only be revised for reasons internal to its own level. No world build finding, Representative construction finding, or lower-level document may be the actual or stated cause of a revision.
- **Rule 1B: No Forward-Projected Specificity** (Constitution Preamble). A document may state that something will eventually exist. It may never state or assume the shape it will take. Existence claims are safe. Shape claims are not.

### Additional Check for Level 2A Documents — Descriptive Not Formative

Level 2A documents describe where things live and what each level may and may not contain. They never govern what methodology steps require — that belongs to Level 3.
- The test: does this sentence tell a builder what to do, or where to look? "Discover: what holds the world together" is telling a builder what to do — a Level 3 sentence misfiled at Level 2A.
- Correct form: "Produces: [world-neutral description of the output]. Governed by: [Level 3 document name] — see that document for requirements."
- Token budgets and operational parameters are permitted at Level 2A — these are listed as PRODUCES items in the System Level Map's CANNOT CONTAIN table.

## Filing and Naming Convention — Applied to Every Output

- Filename: `CiC_[Level]_[DocumentName]_V[Major].[Minor].docx`
- No version history inside the document. Version history belongs in the Change Orders Register.
- No bracket annotations: `[NEW]`, `[MODIFIED]`, `[RENUMBERED FROM]` — all prohibited in ratified text.
- No delta notes: `*Delta: ...*` notes under section headers — all prohibited.
- No builder checklists: Builder Verification sections — prohibited even when labeled "not part of ratified document."
- Version pins: Do not hardcode version numbers on Level 3 documents — they drift silently. Cite Level 3 documents by name only. **Only the four locked Level 1/2A references carry version numbers: Vision V2.0, Constitution V2.2, Essential Experience V2.1, System Level Map V1.0.**

## V7 Upgrades — What Every Document Must Now Reflect

Every document in the repository was built before or during the V7 transition. The cleaning pass implements these upgrades everywhere they are relevant. When reviewing any document, check not only for contamination but for whether the document still reflects the pre-V7 architecture the new governance has superseded.

| # | Upgrade | Old (Pre-V7) | New (V7) | Constitutional Home | Watch For in Documents |
|---|---|---|---|---|---|
| 1 | Level Structure | Ten sequential Layers | Four-level hierarchy (L1-L4) plus WB sequence and Representative Emergence (R). Level 2 split into 2A/2B/2C. Three tracks within Level 3. | System Level Map V1.0 | References to "Layer N" without mapping to current Level/Track. Layer-based content that belongs at a different Level. |
| 2 | Forces Framework Split | Single-pass forces analysis at one step | Split: preliminary identification at Step 3 (Doc_03), full synthesis at Step 7 (Doc_08). Forces Framework moved to Level 3A. | Forces Framework (L3A), CO-004 | Documents that still show forces as a single undivided step, or that list Forces Framework under Level 1. |
| 3 | Representative Emergence | Representative introduced during world build | Representative emerges LAST as Doc_10, after world is fully complete. Influences nothing above it. | Constitution Article 3, CO-003 | Any document implying Representative precedes or shapes the world. Any build sequence where Rep is not the final step. |
| 4 | Build Sequence | 8 steps | 10 steps: Doc_01–Doc_09 plus Representative Emergence (Doc_10) | Construction Framework (L3B) | References to "8-step sequence," any build sequence diagram or list that stops at 8 or omits Rep Emergence as a named distinct step. |
| 5 | Confidence Vocabulary | Three-level scheme in Construction Framework | Five-level scheme now constitutional: Widely Accepted, Dominant Modern Reconstruction, Inferential/Thin, Contested, Not Attested | Constitution Article 17 | Any document using the old three-level confidence scheme. "Holding Document Section 7" references — replace with Article 17. |
| 6 | Story Tier Classification | Old tier definitions in Construction Framework | Four tiers (Tier 1-4), Tier 5 prohibited. Constitutional (Article 19). Construction Framework must be reconciled. | Constitution Article 19 | References to Tier 5 as permitted. "Holding Document Section 9" references — replace with Article 19. Old tier definitions. |
| 7 | Deployment Output Count | Seven outputs (stale — in old Article 34) | Count delegated to Deployment Standards document (not yet scoped). Current System Level Map shows nine. CO-013 adds two more (eleven total). | Constitution Article 35, System Level Map V1.0 | Hardcoded "seven outputs." Any document pinning a specific output count rather than delegating to Deployment Standards. |
| 8 | DOCX/MD Format Distinction | Format choice implicit/inconsistent | Architectural rule by level (CO-006): DOCX = human-facing governance/build docs. MD = runtime documents loaded into AI context. | System Level Map V1.0, CO-006 | MD files used for governance documents. DOCX files used for runtime outputs. Wrong format for the content type. |
| 9 | Context Isolation Architecture | Not formally named as constitutional boundary | Each Representative is a separate API call. Only its own Capsule Core + Permanent Prompt + public transcript in each call. This IS the Article 3 boundary. | Constitution Article 3 | Any document describing Representatives sharing context, or implying worlds can bleed into each other at runtime. |
| 10 | Three-Tier Retrieval | Not established | Tier 1: World Capsule Core (always present). Tier 2: World Priority Layer (session start, CO-013). Tier 3: World Context Layer (on demand). | CO-013, System Level Map V1.0 | Documents that still describe only two retrieval tiers (Core + Context Layer) without the Priority Layer. |
| 11 | Author Gravity Discipline | Not formally required | Every primary source assessed for Author Gravity before gravity confirmation. High-risk authors flagged. No gravity confirmed from unexamined source. | Constitution Article 26 | Any methodology document that does not include Author Gravity assessment as a required step in the build sequence. |
| 12 | TC-001 Fabrication Prohibition | Not formally named | Fictional biography prohibited in Representative. No invented temporal position, family, personal history, or named persons. Rep built only from completed world ecology. | Constitution Article 3, TC-001 | Any Representative document that includes invented biography, personal backstory, or content not derivable from the world ecology. |
| 13 | 2A/2B/2C Sublevel Structure | Single "Level 2" undivided | 2A: stable architecture. 2B: onboarding (read once). 2C: living status documents (read every session). Different readers, update frequencies, governing questions. | System Level Map V1.0, CO-002 | Documents filed or referenced as generic "Level 2." Content in wrong sublevel (e.g. status content in 2A, architecture in 2C). |
| 14 | Holding Document Authority | "Holding Document v1" carried provisional constitutional authority during V7 transition | Holding Document superseded by locked Constitution V2.2. No longer a governing authority. All references must be replaced with current governing document. | Constitution V2.2 Document Precedence Rule | Any remaining "Holding Document v1" references asserting constitutional authority. Replace with Constitution V2.2 article citations or flag as open gap. |
| 15 | Doorway Not a Home | Not established | New Article 34 (Constitution V2.2): system is a doorway, not a home. Never designed for dependency, return engagement as end in itself, or relational sustenance. | Constitution Article 34 | Any document that defines success as return engagement, session duration, or emotional dependency. Any design that optimizes for these. |

## Build Criteria — What Every New or Corrected Document Must Achieve

### For Level 2A Documents
- **Descriptive only:** Describes what each level produces and cannot contain. Never prescribes how.
- **World-neutral:** No world name beyond the five-world registry. No Representative name. No world build findings. No formation content.
- **Status-free:** No current project status. No per-world progress. No maturity ratings benchmarked against one world. Status belongs in 2C Phase Status.
- **Cohesive with System Level Map V1.0:** Every level's PRODUCES and CANNOT CONTAIN must match the System Level Map exactly.
- **Current document references:** Every document reference is name-only for Level 3 documents. Version numbers only for the four locked Level 1/2A references.

### For Level 2B Documents
- **Onboarding purpose:** Answers: how do I enter the system correctly? Read once per new builder.
- **No current status:** Does not describe where the project is right now. Status belongs in 2C.
- **Reflects V7 vocabulary:** Uses Level/Track language, not old Layer language. References current document names and levels.
- **Role-specific:** Builder, Coach, and Critic role descriptions use generic role language — no voice names, no world-specific examples.

### For Level 2C Documents
- **Living documents:** Accurately reflect current project state. Updated as gates open, corrections are resolved, change orders are adopted.
- **Clear separation:** Change Orders Register: architectural decisions only. Corrections Tracker: document-level content fixes only. Phase Status: per-world progress only.
- **Receives from 2A:** Tracks status of items whose architecture is defined in 2A. Never defines architecture itself.

### For Level 3 Documents
- **Methodological authority:** The Constitution governs what; Level 3 governs how. Level 3 documents are the authority on what each step requires.
- **World-neutral:** No world name, no Representative name, no world-specific historical content, no operational parameter values.
- **V7 build sequence:** All Construction Framework references must reflect the 10-step sequence, the forces split, and Representative Emergence as the named final step.
- **Confidence vocabulary:** All confidence references use the five-level constitutional scheme (Article 17), not the old three-level scheme.
- **Story tiers:** All story tier references use the four-tier scheme (Article 19), Tier 5 explicitly prohibited.

## Known Open Governance Gaps — Watch For These

These are items that have been identified as missing from the current architecture. When any document references these, flag them as open gaps rather than resolving them:

- **Deployment Standards document:** Highest priority governance gap. Required by Constitution Article 35. Not yet scoped. All deployment output counts and gate requirements belong here. Never hardcode output counts — always reference this document.
- **World Maturity Framework:** Referenced as a Layer 8 deliverable. Not yet built. When built, its criteria must be axis-neutral — not benchmarked against any single world's realization.
- **Construction Framework reconciliation:** Must be updated to reflect five-level confidence vocabulary (Article 17) and four-tier story classification (Article 19). This is an open flag in Articles 17 and 19.
- **Facilitator Calibration Library:** Not yet built. Equal in importance to the fierce-without-recruiting calibration library. Phase 2 deliverable.
- ~~**Facilitator Governance V3.3 Section 14:** BLOCKING Phase 1. Stale drift signal count — says nine signals, actual count is eleven. Must be corrected before Phase 1 implementation.~~ **RESOLVED** (cleaning cycle, `CiC_L3D_Facilitator_Governance_V3.3.docx`): corrected to eleven, plus a second undocumented count error found in the same pass (Section 10 intro said "three additional" multi-world signals against a list of five — also corrected).
- **Facilitator-Governance design-vs-runtime distinction:** Open structural question raised during the same review. Table Design's Construction Note explicitly states it "generates the Table Runtime Document... loaded into the AI system," distinguishing a design document from a separate runtime artifact. Facilitator-Governance has no equivalent statement despite reading throughout in direct operational address. Not yet resolved: whether Facilitator-Governance is the design document for a not-yet-built separate runtime artifact (defensible under DOCX=governance/MD=runtime), or whether it is itself functioning as the runtime document and its DOCX filing should be reconsidered. Flag when encountered; do not resolve without a dedicated pass.
- **Article 20 (Marginalized-Voices Affirmative Duty):** Not yet formally assigned to a home in most Level 2-3 documents. When encountered, recommend Layer 4 (construction side) and Layer 2/7 (participant-facing and runtime carriage) as candidates.

---

*Church in Conversation · V7 Upgrade Reference · Coach Orientation Document · Not ratified text — reference only.*
