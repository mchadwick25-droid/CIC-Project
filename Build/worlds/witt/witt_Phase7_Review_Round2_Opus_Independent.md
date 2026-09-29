# Independent Adversarial Review — Round 2 (Opus, cross-model independent)
## Target document: `witt_Phase7_Encounter_Ecology_Mapping_DRAFT.md`

**Date:** 2026-09-28
**Reviewer:** Claude Opus 5.5, running as a separate review agent with fresh context. This reviewer did not draft, revise, or previously review any Phase Five/Six/Seven document.

**What this review is.** `witt_Phase7_Review_Round1.md` carried forward the same disclosure as the Phase Five and Phase Six reviews: it was conducted within the drafting thread. This is the genuinely independent, cross-model pass that disclosure named as outstanding. CLAUDE.md requires it: "Opus reviews every adversarial-review round." Round 1's conclusions were re-checked here, not assumed.

**Verdict: SUBSTANTIAL.** Round 1's verdict was "COSMETIC ONLY." This review finds four substantial findings and one cosmetic defect. The cosmetic defect is fixed directly. Two of the substantial findings overturn claims that Round 1 specifically stress-tested and passed.

---

## Section 1 — What this review checked

- **Governing text.** RCF V3.2 Part Nine, Phase Seven, read from the `.docx`. The quotation in §0.1 matches the source. §0.2's claim that Phase One through Phase Eight all sit under Part Nine, "Construction Process Summary," is **confirmed**: Part Nine begins at the heading "Part Nine: Construction Process Summary," Phases One to Seven follow as subsections, and "Part Ten: Governing Commitments" follows them.
- **`witt_Doc_09_Story_Inventory.md` §5 ("Absent Stories")**, read in full.
- **`witt_World_Profile.md` §8, §10 and its Document Log** (line 795, the 2026-09-19 change order). §10 does carry "Status: Verbatim", sourced to Doc_07 §8, so §6.1's premise is confirmed.
- **`witt_Doc_04_Historical_Gravity.md` §7** (the Gravity Index test table). No gravity carries a Formation-test **F**, so §4's claim is confirmed. G10 carries a partial **p** on Formation, which §4 does not mention (a minor omission, not a finding). G13's only **F** is on Persistence ("beyond" the founder).
- **`witt_GoLive_Adversarial_Review_Round1.md`** finding N-1 and its third re-confirmation pass.
- **The Permanent Prompt `.txt` line 31**, counted sentence by sentence, and the compiled runtime `prompt.txt`.
- **Primary sources:** `luther_works-v2-selected_jacobs-spaeth1916.txt` 14857–14860 ("I can get no farther than to men's ears; their hearts I cannot reach"), verified verbatim.

## Section 2 — Round 1's findings, re-checked

- **Round 1 Finding 1 ("inflected," not "inherited"). Confirmed.** Doc_10 §1 reads "not merely inflected."
- **Round 1 Finding 2 (Doc_10 §1's "Section 5 (Honest Limits)" cross-reference error, logged as OG-41). Confirmed** as a real defect, correctly logged and not fixed.
- **Round 1 Finding 3 (Part Nine). Confirmed.**
- **Round 1 Finding 4 (the witt/syr synthesis-status comparison). Not re-contested.** The witt half is confirmed. The syr half was not re-verified by either review, as Round 1 itself disclosed.
- **Round 1 Finding 5 (the 1543 material "already correctly bounded at Step 8"). Not confirmed; overturned.** See P7-S1.

---

## Section 3 — Substantial findings

### P7-S1. §8's "genuinely favorable" cross-world claim about 1543 is contradicted by the record. The Step-8 document was the root cause of the blocking 1543 defect.

**Claimed** (§8, §11, and repeated in OG-42): witt's 1543 material "was already named, bounded, and correctly resolved (existence acknowledged, content Facilitator-carried)" at World Profile §8, produced at Step 8, "before Representative construction began." It is offered as "a genuine, favorable difference from syr's own finding." Round 1 Finding 5 checked this against World Profile §8's current text and confirmed it.

**Found.** At Step 8, World Profile §8 did not say that. `witt_GoLive_Adversarial_Review_Round1.md` finding N-1 quotes the Step-8 text: "the Representative must be able to acknowledge both texts' existence **and, for the 1543 treatise, its documented seven-point programme**" and "whose actual recommendations we can state; we speak to their existence and their documented content plainly when asked." N-1 identifies this paragraph as **the root cause** of BLOCKING finding B-1. It recurred twice from that paragraph: once into the Doc_10 prompt draft, and once into five compiled runtime records. The text now in §8 comes from a **change order dated 2026-09-19** (World Profile Document Log, line 795), after Representative construction, prompted by the go-live review. Round 1 checked the current text without checking the Document Log, so it confirmed a post-hoc correction as though it were the Step-8 state.

**Consequence.** The "favorable, checked cross-world difference" is not supported. The record shows the opposite: witt's Step-8 document got this boundary wrong in the direction of fabrication risk, and correcting it took a blocking go-live finding and several re-confirmation passes. §8 and §11 need to be rewritten, and so does the matching sentence in OG-42 (by a new OG entry; OG-42 is append-only).

### P7-S2. §3's claim that witt's record names no evidence-absent domain is false. Doc_09 §5 does exactly that.

**Claimed** (§3; Open Item 4): witt's construction record "does not appear to name any dimension in the third, evidence-absent category the way syr's Doc_09 Absent Stories did for enslaved persons." All six Honest Limits domains are "thin-but-real."

**Found.** `witt_Doc_09_Story_Inventory.md` §5 is titled **"Absent Stories."** It contains a tested-and-refused candidate (witt-ABS-01, "A village congregation's ignorance at visitation") and a "wider Absent Stories pattern": "**No woman's own story.** ... There is no version of any story in this inventory that can be retold from a woman's own perspective without crossing into invention"; "**No peasant's story, and no story of 1525 at all**"; "**No parish Sunday, no ordinary pastor's own voice.**" Doc_10 §3 quotes two of these directly, and Phase Seven says it read Doc_10 in full. Open Item 4 ("should be checked directly by whoever next has time") could have been answered with one file read. The §9 table's Q2 column, and the §3 "distinct category" paragraph, need revising to separate the evidence-absent domains (a woman's own account; the peasants' side of 1525; an ordinary pastor's or parish's own voice; material culture, where "no material-culture source is vendored in this library at all") from the thin-but-real ones.

### P7-S3. §3 misdescribes the prompt's Honest Limits paragraph, and the document treats a non-runtime artifact as "the deployed Permanent Prompt."

**Claimed** (§3): "The Permanent Prompt's own single paragraph on these domains (paragraph 31) ... six sentences for six domains."

**Found.** Line 31 of `witt_Representative_Permanent_Prompt_Nikolaus.txt` has **ten** sentences covering **seven** limits: household reception, a woman's account, the pastor's own voice, the Reformed-cities break, 1525, 1543, and the post-founder years. It does **not** mention material culture (World Profile §8 domain 6) at all. It does include the pastor's-voice limit, which is not among World Profile §8's six. The conclusion (brief, not encyclopedic) survives. The evidence stated for it does not.

More broadly, Phase Seven follows Phase Five in calling the `.txt` "the deployed Permanent Prompt" (header §1; §2; §6.1). It is not the deployed artifact. `engine/m4/world_loader.py:128` loads `compiled/prompt.txt`, which has a different structure and different rules (Phase Five Round 2, S-1). That matters for this audit's own question: whether the Representative *as actually constructed* is organized around encounter. The actual construction is the compiled prompt: voice_craft's "What we keep returning to" and "How we word things," the world_core fields, and roughly 20,000 words of terms and chunks. Phase Seven never examines it.

### P7-S4. The document's evidence base inherits Phase Five's defects, and it presents authored illustrations as "actual Representative output."

**Claimed** (§2): "Phase Five's own probe results ... are independent, already-completed evidence **at the level of actual Representative output** that G4/G7/G11, G2/G3, G5, and G8 function as encounter rather than information." §3 similarly: "confirmed here directly against actual Phase Five probe output rather than assumed." §11: "independently confirmed under adversarial pressure by Phase Five's own probe results."

**Found.** Phase Five's responses were composed by the drafting thread. Its own Open Item 6 says "All probes and responses were authored and scored for this document." They are not Representative output (Phase Five Round 2, S-4). Meanwhile, actual Representative output on several of these same dimensions exists and is not used: the live witt–rzg table (G8's must/free pacing, G10's Supper boundary, G11's hymn-singing, all voiced live); the live 1543 turns; and the 28/28 M3 battery. Phase Five Round 2 also finds that some thin-domain passes that Phase Seven leans on as "held" are themselves mis-scored: AN-3 and CL-3 feign not knowing names the runtime prompt carries, and CL-1 is contradicted by live output. §3's per-domain "held" statements and §11's verdict need re-deriving once Phase Five is re-settled.

---

## Section 4 — Cosmetic defect, fixed directly (2026-09-28)

- **C-1.** §2 quoted SA-1 as saying "the promise itself is the whole of what we teach." That phrase does not appear in Phase Five's SA-1, or anywhere in Phase Five. It is replaced with a phrase SA-1 actually contains, "We did not weigh it first and believe it after," which supports the same point: authority through formation, not argument. The fix is recorded here rather than as an inline note, to keep the canonical document free of process narration.

## Section 5 — Disposition and escalation

**Verdict: SUBSTANTIAL** (P7-S1 to P7-S4). P7-S1 overturns the document's headline favorable finding. P7-S2 overturns a stated negative finding. Both had been specifically stress-tested and passed in Round 1.

**Round 1 and Round 2 disagree** (COSMETIC ONLY versus SUBSTANTIAL). That is a build-cycle escalation category, and it is logged in `Open_Gaps_Tracking.md` OG-43. Phase Seven is also built on Phase Five and Phase Six, both of which are now SUBSTANTIAL at Round 2.

**Recommendation:** treat "Approved to proceed" as suspended, and revise last, after Phase Five and then Phase Six, per the project lead's decision recorded against `witt_Phase5_Review_Round2_Opus_Independent.md` §5. This review does not change the document's status line itself. Phase Seven's own Open Item 3 remains valid and should be completed in that revision: read Doc_04 and Doc_07 directly. This review checked Doc_04 §7 and confirmed §4's Formation-test claim, but did not re-read Doc_07.
