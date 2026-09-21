# Doc_08 — Forces Document, and `lpc_Force_Index.md`: Latin Pastoral-Congregational Christianity
## Round 1 Independent Adversarial Review

**Marked per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.**

**Review date:** 2026-09-15.

**Documents under review (co-produced, reviewed together per their own Status lines):**
- `Doc_08_Forces_Document.md` (413 lines) — nine sections, six cells, seventeen forces. DRAFT, no prior review round, drafted 2026-09-15 on the project lead's direction.
- `lpc_Force_Index.md` (108 lines) — claims to be "generated from `Doc_08_Forces_Document.md`'s own prose by script, not maintained beside it… Re-deriving it is the check: regenerate and diff, and any difference is a real divergence rather than a stale copy" (Index, header and line 5).

**Governing standard, read at source, not reviewed:**
- `L4-Templates/[world-code]_Forces_Document.md` (full, 832 lines).
- `L3A-Shared-Methodology/CiC_L3A_Forces_Framework_V1.1.docx`, `word/document.xml` unzipped and tag-stripped in full.
- `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx`, same treatment, Part VII Step 8 and Part III located and quoted at source.
- `L1-Foundation/CiC_L1_Constitution_V2_2.docx`, same treatment; Articles 17, 19, 22 located by content search (the docx's own filename says V2_2, its own text declares 2.3 — noted, not re-litigated here).
- `anthropic-skills:cic-forces-index` (the indexing standard this review's five governing questions are drawn from).
- `World-Builds/Donatism/Doc_08_Forces_Document.md` (full) and `World-Builds/Imperial-Juridical-Christianity/Doc_08_Forces_Document.md` (full) — read specifically for the unfilled-Layer-2 precedent question.

**Read at source and independently re-run, not trusted from Doc_08's own account:**
- **The index was re-derived from Doc_08's prose by hand, cell by cell**, and diffed against both of the index's own views (Master Table and By-Connected-Gravity), rather than diffed only against Doc_08. This is the test the review brief asked for and the one the Index's own header invites.
- **Every quotation attributed to a vendored primary source** was searched in the flattened (tag-stripped, entity-unescaped) text of `anf05_hippolytus-cyprian-caius-novatian.xml` and the npnf10x volumes: "it is the shepherd that is chiefly wounded in the wound of his flock"; "your suffrage and God's judgment" / "ancient venom"; "by the judgment of God and the favour of the people, he was chosen to the office of the priesthood… while still a neophyte"; "thousands of certificates were daily given, contrary to the law of the Gospel"; "even of the plenary Councils, the earlier are often corrected by those which follow them."
- **Every "Doc_N §X finds/says Y" claim** was checked by opening Doc_N at §X directly: Doc_04 §2, §7 items 4 and 6; Doc_05 §2.3, §4.3, §9.1, §7; Doc_06 §2.3 (via the Lexicon Index), §5 item 7; Doc_07 §2G, §3A; Doc_02 §2, §6, §7; `Lexicon_Deployment_Index.md` §6, §7; `lpc_Decision_Log.md`'s 2026-09-15 entries.
- **Doc_04's confirmed-gravity list** was read directly from Doc_04 §3/§4 (the "Candidate 1–8" per-candidate sections and the Classification Summary table), not from Doc_08 §1's restatement of it.
- **The Force Index's own two internal views** (Master Table §1 and By-Connected-Gravity §3) were cross-checked against each other, not only against Doc_08, because a script that produces two disagreeing views of its own single source has failed on its own terms regardless of which view is "right."
- **Truncation** in the Index's Force-name and Cross-Cell-Connection-description columns was measured by character count (Python), to establish whether it is a content problem or a mechanical rendering artifact.

### A check that failed and was confirmed before being trusted

My first read of Doc_08 §6's Author-Gravity sentence ("the lexicon's own index records nine of nineteen entries carrying an Author Gravity note") assumed it was simply restating whatever `Lexicon_Deployment_Index.md` currently says, and nearly went unchecked. Opening that Index directly (§6, line 129) found **"8 of 19 entries carry an Author Gravity note"** as the final, twice-independently-re-verified figure (Round 2 and Round 3 each re-parsed all nineteen). This is a defect in Doc_08, not in my check — recorded below as H3 — but it is recorded here too, per the assignment's own instruction, because it was a claim I almost let pass on the assumption that a specific number attached to a specific citation would not be wrong.

A second near-miss: my first pass on the Index's "eight documented local instances" of editorial matter (Doc_08 §2B-5) assumed this was simply false, since `Lexicon_Deployment_Index.md` §7 states plainly "**Seven** entries." Before writing that up as a flat fabrication, I checked `lpc_Decision_Log.md`'s own 2026-09-15 entries and found Doc_07 Round 2 logged an eighth instance of its own (the `ad nostra subsellia` tag in Doc_07 §2G, printed from inside an NPNF `<note>` span without being marked as such). The aggregate figure of eight is therefore plausible. What survives as a real defect, and is reported as such at M5 below, is narrower than "the number is wrong": Doc_08 cites two sections as jointly "registering" all eight, but neither section, read on its own terms, actually shows eight — the Lexicon register shows seven, and Doc_07 §2G's own live text does not flag its own eighth instance at all (only the Decision Log does, uncited by Doc_08).

### Method

I hold no prior position on any finding in this document. Every quotation was checked against the vendored text directly, not against Doc_08's own citation of it. Every "Doc_N §X" cross-reference was opened at the destination, not assumed accurate because it reads fluently. The Index's claim to be script-generated and driftless was tested by literally re-deriving it, not by sampling a few rows and extrapolating soundness.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**Findings: 4 HIGH · 5 MEDIUM · 3 LOW · 1 COSMETIC — 13 in total.**

**What holds up.** The six-cell matrix itself is substantively sound. All seventeen forces are present in the cells the template and the Forces Framework specify, correctly distributed (1A:2, 1B:3, 2A:4, 2B:5, 3A:1, 3B:2). Every quotation I traced to the vendored ANF/NPNF text — the shepherd/flock line, the suffrage/venom fragments, the neophyte line, the certificates line, the plenary-councils line — reproduces its source exactly, including the `[X]` bracket convention correctly marking every recapitalization I could verify (this matches the Decision Log's own claim of three caught-and-fixed recapitalizations before commit). Both required transmission entries (2B-5, 3B-2) are present as their own named forces, never folded into another entry. All fifteen cross-cell connections in Section 4 carry the correct direction and match the Index's own Cross-Cell Connection Map exactly on that dimension. Doc_08's restatement of Doc_04's confirmed gravities correctly maps all eight Candidates (1–8) to G1–G8 with the correct Primary/Supporting/Tensional classifications, and none is invented or dropped.

**What does not.** The Index's central claim — that it is machine-derived from Doc_08's prose and therefore cannot drift — is falsified by direct re-derivation: the Index's own two internal views disagree with each other on which forces connect to which gravities in at least four rows, one gravity's connected-force list is materially incomplete against Doc_08's own Section 5 text, one force's confidence rating is silently dropped from the summary, and the by-confidence table asserts "Contested — 0" two lines above prose that names the one Contested force. Two of Doc_08's own upstream citations name the wrong document. One number contradicts its own cited source. The document's central judgement call — leaving Layer 2 unfilled at the two transmission forces — is defended by an argument that does not survive contact with the Forces Framework's own "not optional" language or with the sibling Donatism precedent, which faced the identical problem and wrote a real Layer 2 instead of leaving the field blank.

---

## The five forces-index review questions, answered directly

**1. Does every force in the index appear in the prose matrix, and vice versa — no drift?**
**No — checked by re-derivation, not assumed.** All seventeen force IDs appear in both documents with matching names and cells (no force is missing or invented on either side). But the Index's own two internal views of *the same source document* disagree with each other, which is drift the Index's own "regenerate and diff" test is specifically designed to catch and did not catch itself. See H1.

**2. Does the by-gravity view show every confirmed gravity from Doc_04 with at least one connected force?**
**Yes on the coarse test, no on the accuracy test.** Checked against Doc_04 §3/§4 directly (not Doc_08's restatement): all eight of Doc_04's confirmed Candidates (mapped 1:1 to G1–G8, classifications matching) have at least one connected force in the Index's by-gravity view — no row is empty. But G4's row (`1B-3`, `2A-2`) is materially incomplete against Doc_08's own Section 5 prose, which states G4 connects to "every force in Cell 2A" (1B-3, 2A-1, 2A-2, 2A-3, 2A-4 — five forces, not two). See H1.

**3. Are both required transmission entries (Cell 2B, Cell 3B) present as their own rows, not folded into another force?**
**Yes, cleanly.** `2B-5` and `3B-2` are both present as distinct, named forces in both Doc_08 and the Index, both flagged `Transmission: YES`, and no other force is misattributed as a transmission entry. This is the one review question with no qualification attached.

**4. Do the cross-cell connections in the index match Section 4's prose exactly, including direction?**
**Yes, on direction and mapping.** All fifteen connections in Index §4 match Doc_08 §4's table exactly on from/to/direction, including the one deliberate non-connection (`2A-2 → none`) and the one causation-disclaimed coincidence (`3A-1 → 3B-1`, "coincides with, does not cause"). The Index's descriptive text for several connections is truncated mid-sentence (a mechanical defect, M4 below), but the mapping and direction themselves are not affected.

**5. Does Layer 2 in the prose matrix actually avoid modern analytical vocabulary?**
**Mostly, with one clear violation on direct spot-check.** Thirteen of the fourteen forces that carry a Layer 2 entry read as period-appropriate, inhabited prose with no imported sociological/political vocabulary; several contain verified verbatim quotations. **Force 3B-1's Layer 2 does not clear this bar**: "he is answering Tuesday's problem" is a modern American office idiom, not a rendering of any 4th/5th-century self-understanding, and it sits inside an entry Section 8/9 characterize as "left unfilled" when it in fact contains this sentence. See M1/M2.

---

## The two judgement calls, verdicts stated plainly

### Judgement Call 1 — leaving Layer 2 unfilled at 2B-5 and 3B-2 (and the related handling of 3B-1)

**Verdict: not a clean application of the From-Within Principle — closer to a gap dressed up as a principle than the document's own framing admits, though the underlying instinct is not unreasonable.**

The argument Doc_08 gives — "transmission is a force this world did not experience… supplying one would invent an experience" (§3, Force 2B-5) — has a real textual hook: the Forces Framework's own Section 1 says "where even inferential reconstruction is unsupported, the builder names the absence and documents the limit rather than supplying modern interpretation as substitute." That much is fair.

But it does not survive three closer checks:

- **The Framework's own Three-Layer Documentation Requirement is stated in absolute terms, not conditional ones:** "Every force identified in every cell must be documented at three layers. **This is not optional.** All three layers are required for every force… A force documented at Layer 3 without Layer 2 is a force that has been imposed from outside rather than inhabited from within." Doc_08 §9 admits exactly this state of affairs for three forces and still ticks the box.
- **Sibling precedent does not support leaving the field blank.** Donatism's own Doc_08 faces the structurally identical problem at its own transmission force (2B-2, "survival through the hostile party's own manuscript tradition") — a transmission mechanism that also acted on the record after the world's own community stopped producing it. Donatism's Doc_08 does not leave Layer 2 empty. It writes: *"This world's own record does not show its own actors reflecting on this condition directly… This is a genuine absence, not a filled silence: whatever this world understood itself to be doing when its own texts were produced, its own understanding of how those texts would or would not survive is not recoverable from what remains."* That is a real Layer 2 entry — it documents the absence as a finding, in the world's own record, rather than declining to write anything under the header. lpc's Doc_08 chooses the latter.
- **The template's own instruction for exactly these two force slots already prescribes the softer remedy, and Doc_08 does not use it.** The generic template's Force 2B-2 (Transmission) Layer 2 instruction ends: "transmission-as-experienced is often less visible in the sources than transmission-as-observed — **apply Reported-Experience Status where appropriate**." The 3B-2 (Transmission in Ending) instruction: "In the world's own vocabulary, **or Reported-Experience Status where not recoverable**." Both anticipate this exact difficulty and name a specific fallback. Doc_08 does not apply Reported-Experience Status to either entry — it applies nothing, with a meta-note explaining why.

A further problem undercuts Doc_08's own account of what it did: **Force 3B-1 is not actually "left unfilled."** Its Layer 2 contains two full sentences ("A bishop writing against a live error for the people in front of him is not producing an inheritance; he is answering Tuesday's problem"), yet Section 8 groups it with the two genuinely blank entries ("Three Layer 2 entries are deliberately not written: 2B-5 and 3B-2… and 3B-1") and Section 9 repeats the claim ("three Layer 2 entries deliberately unfilled… (2B-5, 3B-2, 3B-1)"). This is not a hair-splitting distinction: it means the document's own certification misdescribes its own text, and the one entry that *does* contain prose is the one carrying the anachronism identified at review question 5.

**Recommended fix:** rewrite 2B-5 and 3B-2's Layer 2 on Donatism's model — state what the record does and does not show about the *transmitting* agents' own stated self-understanding (the ANF/NPNF prefaces are a real, recoverable, non-invented source for exactly this: Victorian editors routinely stated their own purposes in their own front matter, and this build has not checked them), rather than declaring the layer inapplicable. Correct 3B-1's characterization in Sections 8 and 9 to reflect that it does carry content, and remove or rewrite the anachronistic sentence.

### Judgement Call 2 — Section 9's completion checklist, each tick tested independently

**Verdict: most ticks are earned; four are not, and the document's separate claim that "the checklist is a structural certification and not a substitute for independent review" is honestly maintained regardless.**

| Item | Tested independently | Earned? |
|---|---|---|
| All six cells populated, 17 forces | Recounted directly from Section 3 headers | **Yes** |
| Every force at all three layers | 2B-5 and 3B-2 have no Layer 2 content at all | **No** — the item's own language ("every identified force documented at all three layers") is false for two forces, not merely qualified |
| Layer 2 uses world's own vocabulary, no modern overlay | Spot-checked across all fourteen filled entries | **No** — "answering Tuesday's problem" (3B-1) is a direct modern-idiom violation |
| Transmission in 2B and 3B | Confirmed present as own forces, not folded in | **Yes** |
| §5 connects every confirmed gravity to ≥1 force | All eight confirmed against Doc_04 directly | **Yes in substance** — but "checkable in `lpc_Force_Index.md`'s by-gravity view" overstates the Index's own reliability (H1) |
| Cross-cell connections documented — fifteen | Recounted directly from Section 4's table | **Yes** |
| Confidence calibration in §3, summarized in §7 | §7's own bucketing (16 Documented/Widely-Accepted + 2B-3 separately Contested = 17) is internally consistent | **Yes, for Doc_08 §7 itself** — the defect lives in the Index's derivative summary, not in §7's own text |
| Five governing principles confirmed | Each tested at Section 8 | **From-Within: no** (3B-1 anachronism); **Proportionality, Named-Tension, Cross-Cell: yes**; **Transmission Specificity: yes on its own narrow terms** (agents, conditions and selection effects are genuinely named at Layer 1/3 — the missing-Layer-2 problem is a Three-Layer-Requirement violation, not a Transmission-Specificity one) |
| Reported-Experience Status applied where appropriate | Searched the full matrix for the term | **No** — used once, as the builder's own unlabeled variant "Reported-Experience-**adjacent**," never in the form the template and Constitution actually define |
| Named scholarly tensions at full strength — three | Cross-checked against Doc_01/Doc_02 §8/Doc_06's CT tags | **Yes** |
| §6 connects transmission synthesis to Doc_02 Author Gravity findings | Confirmed present, but see H3 for the number inside it | **Yes, structurally** — the connection exists; one figure inside it is wrong |

**On the document's own distinction between certification and disposition:** this is maintained honestly. The Disposition states plainly "Not disposed… a structural certification rather than a disposition" and does not claim the checklist substitutes for review. That specific honesty holds even though several individual ticks above do not.

---

## HIGH

### H1 — The Force Index's central claim ("generated by script… cannot drift") is false: the Index contradicts itself across at least six distinct points, checked by direct re-derivation

**Site:** `lpc_Force_Index.md` header/line 5; Master Table (§1); By-Confidence-Level (§2); By-Connected-Gravity (§3).

**What re-derivation found, laid out so it can be re-run:**

*(a) Master Table "Connected Gravities" disagrees with the By-Gravity view for four forces.* Re-deriving each force's gravity connections from Doc_08 §5's own canonical "Gravity-by-Gravity Force Connections" prose (the section the By-Gravity view is built from) and comparing to the Master Table column:

| Force | Master Table shows | Doc_08 §5's own canonical list actually supports | Discrepancy |
|---|---|---|---|
| `1B-1` | G2, G3, G5 | G3, G5 only (§5's G2 entry lists 1A-1, 2B-1, 2B-2 — not 1B-1) | G2 unsupported |
| `2A-1` | G1, G2, G8 | G1 only (§5's G2 and G8 entries do not name 2A-1) | G2, G8 unsupported |
| `2B-1` | G2, G6, G7 | G2, G6 (§5's G7 entry lists 2A-4, 3B-1 only — not 2B-1, even though 2B-1's own Layer 3 text at §3 explicitly claims "connects to… G6/G7 in phase two") | G7 unsupported — and this one traces to a genuine contradiction between Doc_08 §3 (Force 2B-1's own prose) and Doc_08 §5 (the canonical gravity list), which the Index inherited rather than caught |
| `2B-2` | G8 only | G8 **and** G2 (§5's G2 entry explicitly lists "2B-2 (the rival claim it was built against)") | G2 missing — the Index under-counts here, in the opposite direction from the first three rows |

*(b) The By-Gravity view (§3) itself is incomplete against Doc_08 §5's own text for G4.* Doc_08 §5 states: "**G4** … Connected forces: **1B-3** …, **2A-2** …, and **in truth every force in Cell 2A**, since G4 is the channel through which external pressure reaches an ordinary believer." Cell 2A contains four forces: 2A-1, 2A-2, 2A-3, 2A-4. The Index's By-Gravity row for G4 (§3, line 57) shows only `1B-3, 2A-2` — two of the five forces Doc_08's own text says are connected. 2A-1, 2A-3 and 2A-4 are silently dropped.

*(c) `3A-1`'s confidence rating is dropped from the Master Table and from the by-confidence total.* Doc_08 §3 states plainly for Force 3A-1: "**Confidence: Documented.**" The Index's Master Table row for `3A-1` (§1, line 28) shows a bare `—` in the Confidence column. The By-Confidence-Level table (§2) lists 13 Documented forces and 3 Widely Accepted forces — 16 total — against 17 forces in the matrix. `3A-1` appears in none of the five confidence buckets; it has been dropped from the count entirely, not merely mis-shown.

*(d) The by-confidence summary contradicts its own next paragraph.* Index §2 states "**Contested** — 0: *none*" in the summary table, then two lines later states in prose: "**2B-3 carries the one Contested element**, and what is contested is its *placement*…" Both cannot be true in the same section: either the count is 0 or it is 1, and Doc_08 §7 itself (correctly) treats 2B-3 as its own separate Contested-adjacent case, distinct from both the Documented/Widely-Accepted bucket and a clean 0.

**Why this matters.** The Index exists specifically so a reviewer does not have to reread Section 5 to check gravity connections, and its header makes the strong claim that regenerating it from Doc_08's prose and diffing is *the* check, because a script cannot introduce drift a human editor could. That claim is the whole reason a Force Index is required at all (per the `cic-forces-index` standard). It is disproven by the Index disagreeing with itself, using only the tools the standard itself prescribes.

**Fix.** Regenerate both the Master Table and the By-Gravity view from a single pass over Doc_08 §5 (not from Layer 3 prose scattered across §3, which is evidently where the Master Table's extra/missing gravities are coming from), reconcile the 2B-1/G7 contradiction between Doc_08 §3 and §5 before regenerating anything, restore 3A-1's confidence rating, and fix the Contested count to 1 (or state precisely why 2B-3's dual fact/placement classification does not fit the five-level bucket, and represent that nuance rather than a bare 0).

---

### H2 — Two of Doc_08's own citations name the wrong document: "Doc_05 §3A" should be "Doc_07 §3A," used twice for a load-bearing claim

**Site:** Doc_08 §3, Force 2B-4, Layer 3 (line 191): *"Doc_05 §3A finds the crossing is textual rather than successive."* Doc_08 §3, Force 3B-2, Layer 3, item 1 (line 249): *"Continuity across the gap is textual, not successive (Doc_05 §3A)."*

**What I found.** Doc_05 has no section labeled "§3A" anywhere — its subsections use decimal numbering (3.1, 3.2, 3.3, 4.3, 9.1, etc.), never letter suffixes. The actual source of this exact finding is **Doc_07**, which does have a section labeled "3A" — `### 3A. Memory Structures — applied` (Doc_07, line 173) — and states, two lines later: *"The 133-year documentary silence is therefore not only an evidentiary gap but a feature of the world's own memory structure — continuity across it is textual, not successive."* Doc_07 §8 item 3 restates this explicitly as material handed forward to Doc_08: *"§3A gives Doc_08 its starting point: continuity across the 133-year gap is textual rather than successive."*

**Why this matters.** This is the specific mechanism Doc_08 relies on to claim "this is the only mechanism by which this world's formation logic demonstrably crosses its own 133-year silence" (Force 2B-4) and to ground one of transmission's three stated effects (Force 3B-2). The finding itself is real and correctly stated in substance — but attributed to the wrong document, twice, in a way that would send a checking reader to Doc_05, where they would not find it, rather than to Doc_07, where they would.

**Fix.** Replace both instances of "Doc_05 §3A" with "Doc_07 §3A."

---

### H3 — Doc_08 §6 states "nine of nineteen" Author-Gravity entries; the cited source's own final figure is "8 of 19"

**Site:** Doc_08 §6, "Connection to Author Gravity Findings (Doc_02)" (line 342): *"the lexicon's own index records nine of nineteen entries carrying an Author Gravity note."*

**What I found.** `Lexicon_Deployment_Index.md` §6 (line 129) states, as its final, twice-independently-re-verified figure: **"8 of 19 entries carry an Author Gravity note."** Round 1 originally found 7 Yes/11 No across eighteen entries (before `lpclex019` existed); Round 2 and Round 3 each independently re-parsed all nineteen and both confirmed the same total. There is no version of this count, at any point in the Lexicon Index's own document history, that reaches nine.

**Why this matters.** This is a directly checkable number attached to a named source, used to support Section 6's argument that "forces analysis and Author Gravity analysis agree from opposite directions." The underlying argument does not depend on the exact figure being 8 vs. 9, but the number as stated is simply wrong against its own cited source — the same category of defect as H2, and evidence of a pattern concentrated specifically in Section 6 / the two transmission forces, not scattered randomly across the document.

**Fix.** Correct "nine of nineteen" to "eight of nineteen."

---

### H4 — Judgement Call 1 (see above): leaving Layer 2 unfilled at 2B-5 and 3B-2 does not satisfy the Forces Framework's own "not optional" Three-Layer requirement, and departs from sibling precedent without using the template's own prescribed fallback

Full analysis under "Judgement Call 1" above; logged here as a HIGH finding because it is a stated, deliberate departure from an explicit, absolute rule in the governing Framework document ("This is not optional. All three layers are required for every force"), not an oversight, and because the certification in Sections 8–9 asserts principle-compliance for a state of the document that, on inspection, is closer to an uncorrected gap. **Fix:** as stated above — write substantive Layer 2 content for 2B-5 and 3B-2 using the Donatism-precedent model, or explicitly apply Reported-Experience Status per the template's own instruction; correct 3B-1's mischaracterization as "unfilled."

---

## MEDIUM

### M1 — Force 3B-1 is mischaracterized as "left unfilled" in Sections 8 and 9 when it contains actual Layer 2 prose

**Site:** Doc_08 §3, Force 3B-1, Layer 2 (line 236): *"A bishop writing against a live error for the people in front of him is not producing an inheritance; he is answering Tuesday's problem."* Contrast Doc_08 §8 (line 362): *"Three Layer 2 entries are deliberately not written: 2B-5 and 3B-2… and 3B-1."* And §9 (line 377): *"three Layer 2 entries deliberately unfilled and each reasoned (2B-5, 3B-2, 3B-1)."*

**Why this matters.** Two of the three named entries (2B-5, 3B-2) are genuinely blank; the third contains two sentences of content. Grouping all three under the same "unfilled" description misstates what the document itself does, and obscures that the one entry with content is also the one carrying the anachronism at M2.

**Fix.** Revise Sections 8 and 9 to describe 3B-1 accurately (a Layer 2 entry that states directly that this world's formation logic did not know it was producing a lasting inheritance) rather than grouping it with the two blank entries.

### M2 — "answering Tuesday's problem" is a modern-idiom violation of the From-Within Principle, inside the one nominally-"unfilled" Layer 2 entry that actually has content

**Site:** Doc_08 §3, Force 3B-1, Layer 2 (line 236), quoted above.

**Why this matters.** This is the specific defect review question 5 asks reviewers to spot-check for. "Tuesday's problem" is a distinctly modern, informal, deadline-culture idiom with no plausible period register; it is exactly the kind of phrase the governing test ("would someone formed within this world recognize this as an honest account of how they understood what was happening to them?") is designed to catch, and it does not survive that test.

**Fix.** Remove the phrase; state the same point ("he was answering an immediate pastoral demand, not writing for posterity") without the anachronistic idiom, or remove the sentence if the entry is meant to remain a stated absence rather than inhabited prose.

### M3 — Section 9's "Reported-Experience Status applied" tick is not genuinely earned

**Site:** Doc_08 §9 (line 385): *"[x] Reported-Experience Status applied where self-understanding is historically uncertain but formationally central."* Compare the only occurrence of the concept in the body: Force 3B-1, Layer 2 (line 236): *"Marked as Reported-Experience-**adjacent** and left unfilled."*

**What I found.** The template and Forces Framework both define Reported-Experience Status as a specific labeling convention (Constitution Article 17; Forces Framework §3: "the content is documented as the world's own self-understanding rather than asserted as historically established fact"). Doc_08 never applies this status in its defined form anywhere in the six-cell matrix — the one place it gestures at the concept, it uses a self-invented, undefined variant ("-adjacent") attached to an entry that, per M1, is not actually unfilled.

**Why this matters.** This is a narrow but real overstatement: the checklist item claims something was done that the document's own text does not show being done in the form the governing documents define.

**Fix.** Either apply Reported-Experience Status properly to an entry that genuinely warrants it (2B-5 or 3B-2's Layer 2, once rewritten per H4/JC1), or amend the checklist item to state honestly that the status was considered but not found to apply, in the manner Imperial-Juridical-Christianity's own Doc_08 does at its own equivalent checklist line ("not applied; this document's own honest assessment is that no Layer 2 entry's self-understanding is uncertain enough… flagged here as a considered absence, not an oversight").

### M4 — Mechanical truncation in the Index: two Force names and several Cross-Cell-Connection descriptions are cut off mid-word/mid-sentence at a fixed character limit

**Site:** Master Table (§1), rows `1A-2` and `2B-5`; Cross-Cell Connection Map (§4), rows including `1A-2→2B-3`, `2A-3→2B-4`, `3A-1→3B-1`.

**What I found.** Measured directly: the `1A-2` Force-name cell reads "…in Romanized provincial North Afr" and the `2B-5` cell reads "…through a 19th-century tra" — both exactly **88 characters**, with no ellipsis and no regard for word boundaries. Every other Force name in the table is under 88 characters and is not truncated, confirming a fixed-width cutoff in whatever produced the Master Table rather than a content error. The same pattern (text cut off mid-sentence, no ellipsis) appears in several rows of the Cross-Cell Connection Map's descriptive column, e.g. "...appears at both ends of the matrix with" (missing "opposite sign") and "...secured by copying, not by the" (missing "siege").

**Why this matters.** This is exactly the kind of defect the assignment's own guidance anticipates ("a regex capturing `**bold**` as italic" and its neighbors) — a mechanical script artifact, not a content distortion, but one that degrades the Index's usability as the authoritative, at-a-glance reference it is meant to be, and further undercuts the "generated by script, cannot drift" confidence claim in the header.

**Fix.** Remove the fixed-width truncation (or raise the limit and add an explicit ellipsis) in whatever renders the Master Table's Force column and the Connection Map's description column.

### M5 — "Eight documented local instances… registered at `Lexicon_Deployment_Index.md` §7 and at Doc_07 §2G" is not verifiable from the two sections actually cited

**Site:** Doc_08 §3, Force 2B-5, Layer 3, item 2 (line 205); Doc_08 Disposition (line 411): *"the corpus-wide editorial-apparatus question (to which §2B-5 adds this world's eighth local instance)."*

**What I found.** `Lexicon_Deployment_Index.md` §7 states explicitly: *"**Seven** entries rest near 19th-century editorial matter…"* — and lists exactly seven. The plausible source of an eighth is `lpc_Decision_Log.md`'s 2026-09-15 entry for Doc_07 Round 2, which logs a specific new instance: the Latin tag `ad nostra subsellia` in Doc_07 §2G, "printed from inside an NPNF `<note>` span without being marked as such… An eighth local instance of the corpus-wide editorial-apparatus item." But Doc_07 §2G's own live text does not flag this itself — it quotes `ad nostra subsellia` as ordinary primary-source material, with no disclosure that it sits inside an editorial `<note>` span. A reader who "opens the destination" exactly as instructed — the Lexicon Index §7, and Doc_07 §2G — finds seven documented instances in the first and zero flagged in the second; the eighth exists only in the Decision Log, which Doc_08 does not cite here. Separately, the Disposition's phrasing — "§2B-5 **adds** this world's eighth local instance" — reads as though Force 2B-5 *itself* constitutes a new instance of the phenomenon, which it does not: 2B-5 is a synthesis discussing the phenomenon, not an occurrence of editorial matter being mistaken for the world's voice.

**Why this matters.** The number 8 is probably right in aggregate, but the citation trail Doc_08 gives cannot be independently verified from what it names, and the Disposition's own phrasing about what "adds" the eighth instance is not coherent on inspection.

**Fix.** Cite `lpc_Decision_Log.md`'s 2026-09-15 entry (or add the `ad nostra subsellia` instance to the Lexicon Index's own §7 register, where the other seven live) as the source of the eighth instance, and correct the Disposition's phrasing so it does not imply Force 2B-5 itself is a new instance.

---

## LOW

### L1 — Doc_08's "G1"–"G8" gravity notation is never explicitly tied to Doc_04's own "Candidate 1"–"Candidate 8" numbering

**Site:** Doc_08 §1 and throughout.

**What I found.** Doc_04 names its confirmed gravities "Candidate 1" through "Candidate 8" (with classifications) throughout its own text; it never uses "G1"–"G8." Doc_08 introduces "G1"–"G8" as though it were an existing convention. The correspondence is in fact exact and correct (checked directly: Candidate 1→G1 Primary, …, Candidate 8→G8 Tensional, all match), so this is not a substantive error, but a reader moving from Doc_08 back to Doc_04 to check a claim has to infer the mapping rather than being told it.

**Fix.** Add one sentence at Doc_08 §1 stating that "G1"–"G8" here correspond directly to Doc_04's "Candidate 1"–"Candidate 8," in the same order.

### L2 — Force 2B-2's Layer 2 uses the same italic convention as verbatim quotations for what appears to be invented dialogue

**Site:** Doc_08 §3, Force 2B-2, Layer 2: *"I stood before the magistrate and did not deny Him, and I say this man may come back. — And the peace of the church is not any man's to give out of his own suffering, however real. Both in earnest; that is the difficulty."*

**What I found.** This two-voice passage carries no citation and does not correspond to any single quoted line found in the vendored ANF05 text (searched directly; no match). Elsewhere in the same document, italics reliably mark a genuine verbatim quotation carrying the `[X]` recapitalization-bracket convention (e.g., "*[I]t is the shepherd…*," "*[Y]our suffrage…*"). Here the same typographic treatment is applied to what reads as the builder's own dramatized composite of "both voices" in the confessor/bishop tension, with no bracket and no citation distinguishing it from a real quotation.

**Why this matters.** Given this world's own documented history of editorial matter being mistaken for the world's voice, and the project's general strictness about quotation, an unmarked invented passage dressed in the same typography as a sourced quotation is a needless ambiguity, even though Layer 2 is legitimately allowed to be interpretive/inhabited prose.

**Fix.** Either remove the italics from this passage to distinguish it visually from genuine quotations, or add a note that it is the builder's own composite rendering rather than a citation.

### L3 — "the benches" (Force 1B-3, Layer 2) is a possible physical-culture anachronism

**Site:** Doc_08 §3, Force 1B-3, Layer 2: *"What had to be argued could be argued in the language the people in the benches already spoke."*

**What I found.** Fixed congregational seating (pews/benches) is not well-attested for third-century North African basilican worship, where standing congregations are more typical of the period's known liturgical archaeology; Doc_07 §2G's own material-culture lens, by contrast, carefully labels its architectural inferences and does not assume seating. This is a minor, easily-missed detail rather than a load-bearing claim.

**Fix.** Replace "in the benches" with a more period-neutral phrase ("in the assembly," "in the congregation") unless a specific source for congregational seating at this world's basilicas can be cited.

---

## COSMETIC

### C1 — Doc_08's gravity names are abbreviated from Doc_04's full Candidate names without flagging the abbreviation

**Site:** Doc_08 §1, e.g. "G5 Conciliar Authority Theory" vs. Doc_04's "Candidate 5 — Conciliar Authority Theory (Egalitarian vs. Hierarchical)"; "G2 Penitential Discipline" vs. "Candidate 2 — Penitential Discipline: the Reintegration of the Failed." Content and classification match in every case; only the full qualifying phrase is dropped. No fix required beyond noting it, since nothing is misrepresented.

---

## Additional checks: quote fidelity, cross-references, and Article 19

**Quotations, verbatim.** Every quotation I could locate a plausible source phrase for was traced and matched exactly, including capitalization outside the bracket-marked letter: the shepherd/flock line (ANF05), the suffrage/venom fragments (ANF05, same letter, correctly presented as two separate fragments rather than stitched into a false continuous quote), the neophyte line (Pontius, ANF05), the certificates line (ANF05 — and note the vendored text also contains a second, editorially-glossed variant, "against the Gospel law" rather than "contrary to the law of the Gospel," which is exactly the confusion `Lexicon_Deployment_Index.md` §7 already flags for a *different* chunk; Doc_08 uses the correct, non-editorial wording here), and the plenary-councils line (NPNF104). I found no instance in Doc_08 of editorial `<note>` material being quoted as the world's own voice — a clean result worth stating plainly, since this world has a documented history of exactly that failure mode elsewhere.

**Cross-references to upstream documents.** Beyond H2/H3/M5 above, every other "Doc_N §X" claim I opened checked out: Doc_04 §2's declined coercive-capacity candidate (Force 1A-2, 2B-3); Doc_04 §7 item 4 (Manichaean half undeveloped) and item 6 (411 *Gesta* unread); Doc_05 §9.1 (G1 as ecological hub — the wording is close enough to Doc_05's own "nothing else in this world has that reach" that the citation is not merely accurate but well-matched); Doc_05 §4.3 (congregational leverage and its limit); Doc_05 §2.3 (the confessor stem-occurrence count, twenty across eight vendored Augustine volumes — confirmed exactly, including the eight-volume figure, which correctly excludes npnf109, Chrysostom); Doc_06 §5 item 7 (the headword-sweep/translation discovery-method finding behind `lpclex019`); Doc_02 §2 and §6 (both quotations checked and correctly section-attributed).

**Article 19 / invention.** No Layer 1 historical claim was found asserted without a traceable source. No Layer 3 formation claim invents a fact not already present upstream. The one place inhabited prose comes closest to invention without a citation is L2 above (the 2B-2 dialogue), which is a labeling ambiguity rather than a fabricated historical claim. The 133-year silence is held as a genuine silence in this world's own record throughout — I did not find any point where Donatism-territory material is used to fill it, and Doc_08 explicitly and correctly states the discipline at Force 3B-2 ("the interval is richly attested through sources that are Donatism's territory... the temptation is to fill it from World #4, and the binding forbids it").

**Section 1 and the Disposition, re: the four undisposed inputs.** Per the assignment's instruction, this is checked only for honesty, not re-litigated. Doc_08 §1 and the Disposition state accurately that Doc_04–07 are complete, independently reviewed, and undisposed because CO-022 forbids self-disposition against open escalation categories, and that this document was drafted on the project lead's direction. This matches Doc_07's own Disposition and the Decision Log's account exactly. No finding here.

---

## Is the deliverable adequate to proceed to Doc_09?

**Not as drafted.** Doc_09 (per `anthropic-skills:cic-story-repository` and the Construction Framework) will need to cite Doc_08's gravity-force connections and confidence ratings the way Doc_08 itself cites Doc_04 and Doc_05 — and the two sections of this deliverable most likely to be leaned on for that (the Index's by-gravity view, and Section 6/the transmission forces' upstream citations) are exactly where the defects concentrate. Unlike Doc_07's Round 1 (a single self-contained argument-quality defect plus two narrow compliance gaps), this review found the *load-bearing infrastructure* of the co-produced deliverable — the claim that the Index cannot drift from Doc_08, and the citation trail supporting two of the three transmission-related synthesis claims — to be unsound on direct testing, not merely imperfect at the margins. None of this touches the underlying six-cell matrix's substantive force identifications, which are sound, well-sourced, and proportionate. But the specific reason a Force Index is required at all — so a reviewer or a downstream builder does not have to reread Section 5 to trust the gravity connections — fails on its own terms here. A revision pass should: reconcile and regenerate the Index from Doc_08 §5 (not from scattered Layer 3 prose); fix the two wrong document citations and the one wrong count; rewrite Layer 2 for 2B-5 and 3B-2 (or apply Reported-Experience Status properly); correct 3B-1's mischaracterization and its anachronism. None of this requires new source research — it is a correction pass over material already in hand.

---

## CO-022 escalation assessment

Checked directly against Doc_04, Doc_05, Doc_06, Doc_07's own current disposition records and against Doc_08's own Section 1/Disposition. **Representative identity, title, or voice — does not apply**, confirmed; Doc_08 makes no such decision. **Portfolio-level or cross-world — four items, none decided here**, matches the inherited items named across Doc_04–07 (the corpus-wide editorial-apparatus question; the *Boundary Structures*/*Boundary Ecology* inconsistency; the Key Texts/Key Sources template mismatch; the Doc_07 pre-M4 lens-structure item) — accurately restated, though see M5 for how the "eighth local instance" is attributed within that first item. **Governance or methodology — open, unchanged, four items**, confirmed. **Unresolved tensions — one open**, the 411 *Gesta*, confirmed relied on for nothing in this document's own analysis. **This review's own findings do not add a fifth item to any category.** H1–H4 and M1–M5 are all correctable inside this document's (and the Index-generation script's) own editing authority — they are quality and accuracy defects in a draft, not new portfolio-level, governance, or representative-identity questions, and none of them requires the project lead's decision the way the four already-open items do. I did not find grounds to escalate beyond what Doc_08 itself already discloses.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**4 HIGH · 5 MEDIUM · 3 LOW · 1 COSMETIC — 13 in total.** Not adequate to proceed to Doc_09 as drafted. The six-cell matrix's substance is sound and well-sourced; the co-produced Index's core "generated by script, cannot drift" claim is not, and two upstream citations plus one figure need correcting before this deliverable can be trusted the way a downstream builder or reviewer is meant to trust it without rereading Doc_04–07 in full. A single focused revision pass — regenerate the Index from Section 5, fix H2/H3/M5's citations and count, rewrite the two blank Layer 2 entries or apply Reported-Experience Status honestly, correct 3B-1's description and anachronism — should be sufficient; no new source research is required.

*End of Round 1 review. Simulated review — informational only, not an Article 31 substitute.*
