# Church in Conversation — Cleaning Pattern Log

*Running log of contamination patterns and review insights surfaced during the Level 2+ cleaning pass. Purpose: sharpen future review prompts so the same pattern doesn't have to be rediscovered independently in each new document. Not a governance document — a working reference for the Coach and Critic threads.*

*Entries are added as patterns surface. Newest entries appended at the bottom of their type grouping is not required — chronological order by discovery is fine.*

---

## Pattern: Status content masquerading as architecture

**Type:** Type ONE (Name residue) / Level boundary violation (2A containing 2C content)

**Discovered:** CiC_L2A_Architecture_Map_V2_0 (pre-review, Step 1)

**Description:** A document that is supposed to describe stable system architecture instead reports which specific world has cleared which gate, reached which maturity level, or progressed furthest through a validation layer. The architectural point (what a layer requires, what "mature" means for it) gets fused with a status report on one world's progress against that requirement.

**Example:** "Alexandria has progressed furthest but Living Tradition Status Confirmation (Article 29) has not been confirmed for Alexandria, and the full V7 Validation Layer has not been executed end to end." (Layer 5 Maturity rating, Architecture Map)

**Why it passes surface checks:** If the world name is a permitted one (present in the five-world registry, as Alexandria is), a simple name-search contamination check will not flag it — the name itself is allowed to appear. The violation is structural, not lexical: this content belongs in Level 2C Phase Status (which tracks per-world gate status), not in a Level 2A document (which describes the gate itself, world-neutrally). Only a check against what the *document level* is permitted to contain — not just which proper nouns are permitted — catches this.

**Watch for in:** Any Level 2A document with maturity ratings, progress notes, or world-specific examples embedded in what should be stable architectural description. Also worth checking Level 3A/3B/3C/3D methodology documents for the same fusion (methodology description contaminated with one world's construction history).

---

## Pattern: Maturity framework shape assumption

**Type:** Type TWO (Shape residue) / Type THREE (Theological and gravity residue, adjacent)

**Discovered:** CiC_L2A_Architecture_Map_V2_0 (pre-review, Step 1 — flagged by project lead before Critic review, not yet confirmed by Critic)

**Description:** A document that rates formation worlds against a maturity framework may quietly assume that mature formation looks like intellectual depth, textual density, or doctrinal precision — because those were the markers of whichever world was most developed when the framework was written. The maturity descriptors themselves ("substantially realized," "partially realized," "not yet initiated," and what evidences each) carry the shape even when zero world names or figure names appear anywhere in the framework's definitions.

**Example:** Not yet isolated as a specific sentence — flagged as a category to check in the Architecture Map's per-layer Maturity sections, where "high," "medium," and "low" maturity are asserted without the document ever stating what evidence would look like for a world whose formation axis is oral, communal, or affective rather than textual and doctrinal. Needs Critic confirmation before treated as a confirmed finding rather than a hypothesis.

**Why it passes surface checks:** This is the hardest tier of contamination to catch. No proper noun, no world reference, no theological term needs to appear — the bias lives in which *kind* of evidence the maturity scale treats as legible. A reviewer checking only for names or explicit theological vocabulary will find nothing. It only surfaces when a reviewer actively asks: "would this maturity descriptor register as 'mature' for a world whose formation looks nothing like Alexandria's — e.g., a twentieth-century African independent church community, or a fourteenth-century English lay mystic?"

**Watch for in:** Any document with maturity ratings, readiness assessments, validation rubrics, or stage-based progression language — especially Level 2A architecture documents and the Level 3 Validation Layer / Encounter-Success Evaluation Rubric methodology once built.

**Confirmed by Critic review (Architecture Map, Item 7):** No explicit contaminated maturity descriptor was found — the risk was latent, not yet realized in stated language, and the Critic correctly declined to invent a finding. But a concrete instance of the adjacent risk was confirmed: the Layer 5 source-ecology framing ("Discover: Sources, Visibility, Boundaries, Historiography") privileges written/attested sources by vocabulary choice alone, with no world name or theological term present. An oral, material, or liturgical world would read as under-resourced against this framing even though nothing in it names a world. Corrected language should assess "what the evidence is and is not — including oral, material, and liturgical attestation — with maturity judged by rigor of handling, not textual volume." Also confirmed clean by the same review: a six-lens ecology reconstruction set (Human, Community, Worship, Organizational, Intellectual, Ministry) that treats Intellectual Ecology as one of six co-equal lenses is axis-plural and does NOT itself carry this residue — worth preserving as a positive model of what axis-neutral framework language looks like.

---

## Pattern: Layer instruction masquerading as architecture

**Type:** Descriptive-not-formative violation (Level 2A specific)

**Discovered:** CiC_L2A_Architecture_Map_V2_0 (pre-review, Step 1)

**Description:** A document describes what a level or layer produces by listing the specific steps, discovery questions, or output criteria involved — telling a builder what to do rather than pointing to where the methodology that governs those steps lives. This is Level 3 content misfiled at Level 2A: the document usurps the authority of the Construction Framework (or whichever Level 3 document actually governs the step) instead of referencing it.

**Example:** "Discover: What holds the world together? What captures attention? What defines maturity? What defines authority?" followed by "Output: Historical Gravity (Doc_02)" and "Governed by: Construction Framework v7" (Layer 5.2, Architecture Map). The "Governed by" line is present and correct — but the "Discover:" line still restates the methodology instruction itself rather than only pointing to it.

**Why it passes surface checks:** Passes a name-search contamination scan completely — no world names, no Representative names, no theological vocabulary. It reads as reasonable, even helpful, summary content, which is exactly why it's easy to miss: the violation is about *which document has the authority to state this*, not about whether the content is accurate.

**Watch for in:** Any Level 2A document with "Discover:" / "Output:" / "Governed by:" style language, enumerated gate lists, or step-by-step walkthroughs that reproduce methodology rather than only citing it. Level 2A documents that include a "Governed by: [Level 3 document]" citation alongside the restated instruction are a particular tell — the citation shows the author knew the authority lived elsewhere but included the instruction anyway.

---

## Pattern: Unrecognized governing authority

**Type:** Rule 1A/1B-adjacent (parallel constraint) / Foundational conflict

**Discovered:** CiC_L2A_Architecture_Map_V2_0 (Critic review, Item 4b)

**Description:** A document asserts that some named artifact holds "constitutional authority" or governs another document's content, when that artifact does not appear anywhere in the locked Level 1 foundation's own precedence structure. The claim is usually a holdover from an earlier project phase (a transitional or interim document) that was never formally retired once its content was absorbed into the ratified foundation.

**Example:** "Holding Document v1 (provisional constitutional authority over build documents during V7 transition)" — asserted repeatedly across four layers of the Architecture Map. The locked Constitution V2.2 Document Precedence Rule names exactly three supreme governing documents (Vision, Constitution, Essential Experience). No fourth document holds constitutional authority. The Holding Document exists only in the Archive folder.

**Why it passes surface checks:** No prohibited proper noun, no world name, no Representative name — a name-search scan finds nothing wrong. The violation only surfaces when a reviewer checks a cited authority against the *current* locked precedence structure rather than assuming a citation is valid because it looks like normal governance language.

**Watch for in:** Any document that cites a named framework, protocol, or "document" as a source of binding authority — cross-check every such citation against the current Document Precedence Rule and the current Level 1/2A inventory before accepting it.

---

## Pattern: Citation drift after Level 1 renumbering

**Type:** Stale reference (mechanical, not contamination, but governance-critical)

**Discovered:** CiC_L2A_Architecture_Map_V2_0 (Critic review, Item 4d)

**Description:** When an Article is inserted into the Constitution (as Article 34, Doorway Not a Home, was inserted during the Level 1 rebuild), every citation to an Article number at or after the insertion point in downstream documents becomes silently wrong by exactly one, unless every downstream document is re-audited. A document can have already correctly remapped an *earlier* renumbering (e.g., old 20→33) and still carry this newer, later drift undetected, because the two remaps happened at different times and a partial audit catches the one it was looking for.

**Example:** Architecture Map correctly remapped old Article 20→33, 21→28/29, 22→31, 23→32 (an earlier remap), but missed that Article 34's insertion shifted the former 34/35/36 cluster: citations reading "Article 34" for AI Resource Integrity or Deployment Standards should read Article 35; "Article 35" for Sole-Builder Stewardship should read Article 36.

**Why it passes surface checks:** The citations look plausible and internally consistent — they're wrong by exactly one, in the same direction, across a contiguous cluster, which reads as normal rather than as an error. Only a full article-by-article verification against the current locked Constitution catches it.

**Watch for in:** Every downstream document with Constitution Article citations, especially any that predates the Article 34 insertion. A full citation audit (not a spot check) is warranted across Level 2A, 2B, 3A–3D before those documents are considered clean.

---

## Pattern: Sibling document citation drift

**Type:** Stale reference (mechanical, cross-document)

**Discovered:** CiC_L2A_Architecture_Map_V2_0 (Critic review, Item 4c, confirmed against live repository by Coach during Step 3)

**Description:** A document cites another document's version number (e.g., "Facilitator-Governance v1.4," "Representative Construction Framework v1.1"). The moment the cited document is revised, that citation goes stale — and nothing in the current pipeline systematically re-checks outbound citations when a document is updated. This risk is not limited to documents under active cleaning: even documents already marked CLEAN or serving as the governing reference (Project Status, System Level Map) can carry stale sibling citations, because a citation's staleness is a property of the citing document's currency, not the cited document's status.

**Example:** Architecture Map cited "Facilitator-Governance v1.4" and "Representative Construction Framework v1.1." Live repository check found the actual current files are `CiC_Facilitator_Governance_v3_2.docx` and `Representative_Construction_Framework_v2_0.docx`. Neither the Project Status doc (July 2026) nor the System Level Map V1.0 — both treated as current reference documents in this pipeline — cite these correct current numbers either (Status doc and System Level Map both cite "V3_3" for Facilitator-Governance and "V2_1" for the Representative Framework, neither of which exists as a file in the live folders).

**Why it passes surface checks:** Version pins read as precise and authoritative regardless of whether they're current. Nothing about the citation's form signals staleness — only a direct check against the live repository file listing catches it.

**Watch for in:** Every document-to-document version citation, in every level, including documents already marked CLEAN. Recommend a standing practice: before treating any citation to a sibling document's version as ground truth, verify it against the actual current filename in the repository rather than against another document's citation of it.

---

## Pattern: "CLEAN ✓" status does not guarantee current-standard comp