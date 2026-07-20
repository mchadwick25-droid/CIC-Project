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

**Second confirmed instance (L3B Citation Audit, Construction Framework):** Step 8's deployment-outputs instruction cited "Article 34" where the correct home is Article 35 (Deployment Standards and AI Resource Integrity) — the exact same Doorway-insertion off-by-one, in a different document. Also found in the same audit: a same-document internal inconsistency unrelated to the Article 34 insertion — Construction Framework cited the five-level confidence vocabulary as both Article 16 (wrong) and Article 17 (correct, Source Transparency/Confidence/Evidential Integrity) in two different sections. Confirms this isn't a one-off — every document with Level 1 citations needs the full audit, not a sample.

---

## Pattern: Sibling document citation drift

**Type:** Stale reference (mechanical, cross-document)

**Discovered:** CiC_L2A_Architecture_Map_V2_0 (Critic review, Item 4c, confirmed against live repository by Coach during Step 3)

**Description:** A document cites another document's version number (e.g., "Facilitator-Governance v1.4," "Representative Construction Framework v1.1"). The moment the cited document is revised, that citation goes stale — and nothing in the current pipeline systematically re-checks outbound citations when a document is updated. This risk is not limited to documents under active cleaning: even documents already marked CLEAN or serving as the governing reference (Project Status, System Level Map) can carry stale sibling citations, because a citation's staleness is a property of the citing document's currency, not the cited document's status.

**Example:** Architecture Map cited "Facilitator-Governance v1.4" and "Representative Construction Framework v1.1." Live repository check found the actual current files are `CiC_Facilitator_Governance_v3_2.docx` and `Representative_Construction_Framework_v2_0.docx`. Neither the Project Status doc (July 2026) nor the System Level Map V1.0 — both treated as current reference documents in this pipeline — cite these correct current numbers either (Status doc and System Level Map both cite "V3_3" for Facilitator-Governance and "V2_1" for the Representative Framework, neither of which exists as a file in the live folders).

**Why it passes surface checks:** Version pins read as precise and authoritative regardless of whether they're current. Nothing about the citation's form signals staleness — only a direct check against the live repository file listing catches it.

**Watch for in:** Every document-to-document version citation, in every level, including documents already marked CLEAN. Recommend a standing practice: before treating any citation to a sibling document's version as ground truth, verify it against the actual current filename in the repository rather than against another document's citation of it.

---

## Pattern: "CLEAN ✓" status does not guarantee current-standard compliance

**Type:** Filing hygiene (Rule: "No version history inside the document")

**Discovered:** L2B Builder and Coach Role Descriptions, both marked CLEAN ✓ / "Zero contamination" in Project Status (July 2026), while doing housekeeping ahead of the L2B batch review.

**Description:** Both `CiC_L2B_Builder_Role_Description_V1_0.docx` and `CiC_L2B_Coach_Role_Description_V1_0.docx` carry a "Version History" section in ratified text — the same category of prohibited content that was stripped from the Architecture Map. They were marked CLEAN because that review checked for contamination (world/Representative names) but not for filing-hygiene compliance with the "no version history in ratified text" rule, which either wasn't fully enforced yet at the time or was overlooked. Confirmed by diffing each against its own pre-rename duplicate: the version-history section is the only content added between the old and "clean" copies.

**Why it passes surface checks:** A CLEAN status from a prior review pass reads as permission to skip a document rather than as a claim scoped to whatever checks that pass actually ran. Nothing marks which standard a CLEAN rating was measured against, or when.

**Watch for in:** Do not skip a document solely because Project Status marks it CLEAN. At minimum, spot-check for filing-hygiene violations (version history, bracket annotations, delta notes, builder checklists) even on "clean" documents before treating them as done — this check is cheap (open the document, look for these four things) relative to a full Critic review, and should be standard practice before advancing any document past its current status.

---

## Pattern: Coach-side enumeration undercounts — a process lesson, not a document contamination pattern

**Type:** Review-prompt drafting discipline (applies to the Coach's own Step 2/Step 4 prompts, not to a document's content)

**Discovered:** L2B batch Critic review, Concept Paper. The Critic prompt's scope 2a manually enumerated "every section-level bracket annotation" with a parenthetical list — and the list omitted two real instances (`Status [MODIFIED]`, `Theological Foundation [NEW]`) and all five of the paired `Delta:` lines beneath modified section headers, despite the Coach having read and extracted all of them during Step 1.

**Description:** When a Coach prompt says "remove every X" and then illustrates with a parenthetical list, a Builder working literally from the list rather than the general rule will miss anything the list omits. The omissions here were not contamination the Coach failed to find — they were findings the Coach *did* surface in Step 1 and then failed to carry into the enumerated scope of Step 2.

**Why it passes surface checks:** A prompt that names several correct examples reads as thorough. The gap is invisible until someone (here, the Critic) re-derives the full list independently and diffs it against the prompt's enumeration.

**Watch for in:** Every future Critic and production prompt that uses "for example" / parenthetical-list style scoping for a removal category (brackets, Delta notes, stale citations, version pins). Going forward: state the general rule as the operative instruction ("remove every bracket annotation and its paired Delta note, wherever they appear"), and treat any illustrative list as non-exhaustive examples only — never rely on the list alone to bound what gets fixed. Where practical, verify counts with a direct text search (grep) before finalizing the prompt rather than enumerating from memory.

**Second confirmed instance (L3B Citation Audit, Pass 1):** The Coach's own regex for building the starting citation inventory (`Article [0-9]+`) only matched singular "Article N" and silently dropped every plural "Articles X and Y" citation across all three documents (e.g., "Articles 28 and 29"). The Critic's independent full-document search caught what the pattern-based inventory missed. No new errors surfaced from the missed citations this time, but it confirms even mechanical/regex-based inventories — not just manual enumeration — need the same "verify by independent search, don't trust the starting list" discipline. Any future grep-built citation or contamination inventory should account for plural/compound forms explicitly, not just the singular pattern.

**Third confirmed instance (L3C Representative Construction Framework):** Two separate Coach undercounts in the same review. (1) The plural-form citation miss recurred exactly as predicted — "Articles 18 and 12" was missed by the Coach's starting inventory, caught by the Critic's independent search. (2) A new variant: the Coach's scaffolding-tag count itself was wrong, not just a citation count — Coach counted six `[MODIFIED]`/`[NEW]` tagged headings, the Critic's independent count found seven (Coach had merged two separate Part Eight instances into one and missed that Part Five has only one, not two). Confirms the "verify by independent search, don't trust the starting count" discipline applies to every category of enumeration a Coach prompt states a number for — not just Article citations.

---

## Pattern: Live status/funding/world-roadmap content embedded in Level 3 methodology documents

**Type:** Level boundary violation (3A/3D containing 2C-style status content plus world-specific naming with no exception available)

**Discovered:** World Build Onboarding Framework v1.1 (per-world Round 3B sections) and CiC_Phased_Build_Path_v2_0 (Current Work Streams, Deliverables-with-Status tables, World Build Roadmap table, four Funding sections).

**Description:** A document that should describe world-neutral methodology (what a phase requires, what gates it passes, how a step works) instead tracks which specific world is doing what right now, what it costs, and when it will be funded. Unlike the parallel pattern already logged at 2A ("Status content masquerading as architecture"), this has no lexical escape hatch at Level 3: 2A permits the five-world-registry as a sole world-name exception, but 3A/3B/3C/3D have no such exception — any world name at all is a violation, not just an unpermitted one.

**Example:** Phased Build Path's World Build Roadmap table names Alexandria, Theon, Desert Christianity, and Ecumenical Communal with live Status values ("In Build," "Queued," "TBD"); its Current Work Streams table tracks "Alexandria V7 Alignment (1A) — coach thread onboarding in progress" as a live deliverable; its Funding sections describe grant-seeking strategy tied to specific phases. None of this is phase-structure methodology — it is project management and fundraising content wearing a methodology document's letterhead.

**Why it passes surface checks:** The document's title and framing ("Full Growth Roadmap," phase gates, governing principle) read as legitimate 3A content, and a reviewer focused only on prohibited-name-search would still flag the world names — but a reviewer might reasonably assume Level 3 documents get the same treatment as 2A's registry exception, and wrongly wave the names through. They don't: 3A has zero exception.

**Watch for in:** Any Level 3A/3B/3C/3D document with tables that have a "Status" column, dollar figures or grant/funding language, or a roadmap/tracker structure — these are structural tells that live-tracking content has been embedded in what should be a stable methodology document. The correct fix is usually a split: extract the world-neutral structural kernel (phase sequence, gates, what each phase proves) and relocate the rest to 2C Phase Status (live tracking) and/or a dedicated Ministry/Operations location for funding content.

**Resolved:** The funding and world-roadmap content was relocated to `Ministry/Funding/CiC_Ministry_Funding_Strategy_v1_0.docx`, per Clean File Structure V1.1's canonical folder tree (Ministry/[Category], out of scope for the Level 1-4 cleaning standard). The redundant status-tracking tables (Current Work Streams, per-phase Deliverables) were not carried forward at all — superseded by Phase Status, which already tracks live build status.

---

## Standing filing rule: World-specific documents never sit at Level 2, even temporarily

**Type:** Filing hygiene / process discipline (not a contamination type — a placement rule)

**Established:** Project lead directive, System Operations filing discussion. Confirmed against a real example: `alex_World_Deployment_Config_V7_r1.md` — a per-world document that supplements the system-wide `CiC_System_Operations_V7_r1.md` with Alexandria-specific selections (model pin, retrieval clusters, caching selections, Facilitator-context specifics, cross-build constraints).

**Rule:** Level 2 documents (2A/2B/2C/2D) describe system-wide, world-neutral architecture and parameters only. A world-specific companion or supplement to a Level 2 document — even one that explicitly references and extends it — belongs in that world's own `World-Builds/[World]/` folder, never in the Level 2 folder itself. Critically, such a document should not be created in advance of need: it comes into existence only once that world actually reaches the point in its build process that requires it (e.g., a Deployment Config is written when a world is ready for deployment, not scaffolded early as a placeholder). Do not pre-create empty or placeholder per-world operational documents for worlds that haven't reached that stage — this applies even when the master Level 2 document lists all five worlds in its registry (the registry entry is not license to build out a companion document ahead of the world's actual build progress).

**Watch for in:** Any future Level 2 document (especially 2D and any new operational-parameter documents) that spawns or references per-world companions. Verify each companion sits in `World-Builds/[World]/`, not the Level 2 folder, and confirm it was created only after that world's build reached the relevant stage — not scaffolded early "for completeness."

---

## Ruling: CO-012 scope does not include build-process model/tool names (Opus, Claude Code)

**Type:** Scope clarification (CO-012 operational-parameter-scrub rule)

**Raised by:** Critic review, L3A batch (Technology Engagement Brief Finding 2.1; Phase Structure kernel Finding 3.5). The Critic correctly identified that "Opus" and "Claude Code" appear pervasively in both documents and asked whether CO-012's "no vendor/tool names" language reaches them.

**Coach ruling:** No. CO-012 targets *deployment/runtime operational parameters* — the specific vendor, model, or tool a live deployment depends on, which is subject to change (see System Operations' own "Update trigger: Technology stack change / Model change") and therefore must be referenced via System Operations rather than hardwired. "Opus" and "Claude Code" as used in the Technology Engagement Brief and Phased Build Path describe *build-process governance roles* — who directs adversarial technical review, who executes implementation checks — not a swappable runtime dependency. This is Constitutionally sanctioned vocabulary: Article 35 §B of the locked Constitution V2.2 itself names "Opus output from dedicated adversarial review threads" as part of the project's own review architecture. A document describing the Opus-leads/Claude-Code-executes review structure is describing governance, not deployment.

**The distinguishing test:** Does the name describe *which model a Representative/Facilitator runs on at runtime* (a deployment parameter — CO-012 applies, point to System Operations / that world's Deployment Config) or *which role reviews/builds the system* (a governance-structure term — CO-012 does not apply, name it directly)? "Opus critic passed" (a gate criterion describing the adversarial review step) is the second kind. A sentence pinning a Representative's runtime model to a specific named model would be the first kind and should be scrubbed.

**Watch for in:** Every future Critic review of a document that discusses the review/build process (any document describing Coach/Critic/Builder roles, technology assessment, or adversarial review) will surface this same question. Apply the test above rather than re-litigating from scratch each time.

---

## Pattern: Proposing a structural split without cross-checking already-ratified siblings first

**Type:** Coach process discipline (parallel to "Coach-side enumeration undercounts" — a drafting-quality gap, not a document contamination type)

**Discovered:** L3B Construction Framework, Pass 2 Critic review. The Coach proposed a specific 8-step-to-10-step restructuring (Step 8 narrowed, new Step 9 "World-Side Deployment Preparation," new Step 10 "Representative Emergence") without first checking where the already-ratified Forces Framework V1.1 itself compiles Doc_08. The Critic caught two real problems: (1) the proposed split left Doc_07 and Doc_08 bundled at one step, which would leave Construction Framework contradicting Forces Framework V1.1's own step numbering (Forces Framework compiles Doc_08 at its own distinct Step 8); (2) the invented "deployment preparation" step doesn't correspond to anything in the V7 Upgrade Reference's actual definition of the 10-step sequence (Doc_01–Doc_09 plus Representative Emergence as Doc_10) — deployment production is a later, separate Layer 6 phase, not a numbered construction step.

**Why it passes surface checks:** A proposed split can look complete and reasonable on its own terms — it accounts for all the content that needs to go somewhere — while still drifting from what a sibling document, read independently, already committed to. The gap is invisible unless the sibling's own step/section numbering is checked directly, not inferred from memory of having read it once.

**Watch for in:** Any Coach-proposed structural split, restructuring, or renumbering — especially one that touches a build sequence, step numbering, or document-output mapping that a sibling document also describes. Before presenting a proposed split to the Critic for validation, cross-check it against every ratified sibling document's own account of the same structure, the same way item 11 (Consistency and value check) already requires for prose content — a structural proposal needs the same discipline, not just a content-consistency scan after the fact.

---

## Pattern: A document's own embedded historical remap table can itself be wrong

**Type:** Citation accuracy (parallel to "Citation drift after Level 1 renumbering," but a distinct failure mode)

**Discovered:** L3C Representative Construction Framework, Critic review. The document's Builder Verification section asserted an explicit article-renumbering table ("old Article 21 → new Article 26," "old Article 12 stays Article 12") as a record of work already done. Both entries in that table were wrong: old 21 actually maps to 28/29 (already confirmed twice elsewhere this project), and old 12 was actually consolidated into the current Article 18, not left standing alone. The resulting ratified-body citations (Article 26, Article 12) were themselves wrong as a direct consequence of trusting the table.

**Description:** This is a more specific and more dangerous variant of the general "don't trust a document's self-description of its own citation currency" rule (previously established for phrases like "all Article references updated to v7.4.1 numbering"). Here the document doesn't just *claim* to be current — it provides an explicit, itemized, seemingly-verifiable remap table, which reads as far more trustworthy than a vague claim of currency. That extra specificity is exactly what makes it dangerous: a reviewer is more likely to accept a itemized table at face value than a bare assertion.

**Why it passes surface checks:** An explicit old-number-to-new-number table looks like evidence of careful prior work, not a claim needing verification. Both wrong entries in this table also happened to look internally plausible (a Confidence/Author-Gravity Article near the 25-27 cluster; a low-numbered Article "staying the same" isn't inherently suspicious).

**Watch for in:** Any document — especially one produced by an earlier revision cycle — that includes its own remap table, changelog, or Builder Verification claiming specific old-to-new citation mappings. Every mapped citation must still be verified by content against the current ground-truth Constitution list, exactly as if no table existed. The table is a hypothesis to check, never a source of truth.

---

## Pattern: Builder-inserted content lacks the explicit formatting its siblings carry

**Type:** Step 6 verification discipline (production-quality defect, not a contamination type)

**Discovered twice.** (1) L3C Representative Construction Framework: the Builder inserted a new `Doc_09` item into an existing bulleted list (Doc_01 through Doc_08), but the new paragraph was missing the `<w:numPr>` bullet-numbering properties and the `<w:rPr>` run formatting (font, size) every other item in that same list carried — it would have rendered without a bullet and in a different font than its siblings. (2) L3D Facilitator-Governance: the Builder added a new closing "Constitutional Grounding" section (heading + one body paragraph), but neither paragraph carried the explicit `<w:rPr>` (Georgia font, navy `#1F3864`, 17pt heading / 12pt body) and `<w:spacing>` properties every one of the document's other 16 section headings and body paragraphs carried — it would have rendered in the base Heading1 style's default blue `#2E74B5` at 16pt instead, visibly inconsistent with the rest of the document.

**Description:** When a Builder inserts new content into a docx by writing a fresh `<w:p>` element (rather than duplicating and editing an existing sibling paragraph), Word's default paragraph/run properties silently fill in wherever explicit overrides are omitted. The inserted text is substantively correct and reads correctly in plain-text extraction (via pandoc or similar) — plain-text conversion does not surface formatting at all — so a check that only verifies wording will find nothing wrong. The defect is only visible by opening the actual rendered document or inspecting the XML directly.

**Why it passes surface checks:** Every verification method used so far in this project's Step 6 process — pandoc plain-text extraction, grep, word/phrase search — strips or ignores paragraph and run formatting entirely. A Builder's own self-report ("verified by direct search") is typically also text-only. Both instances were caught only because the Coach went one level deeper and inspected the raw `document.xml`, comparing the new paragraph's `<w:pPr>`/`<w:rPr>` against a known-good sibling paragraph's.

**Watch for in:** Any Step 6 verification where the production prompt asked the Builder to insert new content into an existing structure (a new list item, a new section, a new table row) rather than only editing existing text in place. For these cases, Step 6 must include an XML-level check — not just a text-level one — comparing the new paragraph(s)' `<w:pPr>` and `<w:rPr>` against an existing sibling paragraph of the same kind, and correcting any missing formatting before filing. Text-only verification is not sufficient when the production prompt calls for new paragraphs, only when it calls for edits to existing ones.

**Third confirmed instance (L2B World Build Onboarding Framework):** The Builder rewrote two "Question N:" verification-question paragraphs (Round Two Q3 and Checkpoint Two Q1) in full, replacing stale deployment-output-count content with corrected pointer language. Every other "Question N:" paragraph in the document splits into two runs — a bold "Question N: " label run followed by a non-bold body run — but both rewritten paragraphs collapsed into a single run with the entire line (label and body) bolded. Caught by a python-docx sweep checking every "Question " paragraph's run structure for the two-run bold-label pattern, not by reading a single example. Confirms the pattern extends to *rewrites* of existing paragraphs, not just newly *inserted* ones — replacing a paragraph's full run content (rather than only its text) can just as easily drop the run-split structure as inserting a fresh paragraph can drop formatting entirely.

**Watch for in (updated):** The same XML-level check applies whenever a production prompt asks a Builder to substantially rewrite an existing paragraph's content, not only when it asks for brand-new insertions. Where a document has a repeating paragraph-type with an internal run-split convention (e.g., a bold label followed by unbolded body text), sweep *every* instance of that paragraph type programmatically and compare run structure, rather than spot-checking only the paragraphs the prompt explicitly touched.

---

## Pattern: A document's own internal summary count drifts as its own content grows

**Type:** Stale reference (mechanical, internal to a single document — distinct from citation drift or sibling-document drift)

**Discovered:** L3D Facilitator-Governance, Critic review. Section 10's introductory line ("At the multi-world table, three additional drift signals require monitoring") was correct when written at v3.0, when three multi-world signals existed. v3.1 added a fourth signal (competitive recruitment drift) and v3.2 added a fifth (mode-dominance drift), but neither revision updated the summary line that introduces the list — so the document shipped for two full version cycles internally contradicting itself: an intro claiming "three" immediately followed by a list of five. This was a second, separate count error beyond the one the project's V7 Upgrade Reference had already flagged (Section 14's "nine" vs. the actual eleven) — the same class of error, occurring twice in one document, at two different points that summarize the same underlying list.

**Description:** Unlike citation drift (caused by an external renumbering event) or sibling-document drift (caused by another document being revised), this is a document accumulating content across its own version history without re-checking its own internal summary statements against what that content now adds up to. Every additive revision that appends to a list, a count, or an enumeration creates a new opportunity for this — and because each individual revision only adds one item, no single version-to-version diff looks alarming.

**Why it passes surface checks:** Each revision in isolation is a small, correct, additive change (exactly as this project's convention of "no existing content removed, only added" requires) — the drift is only visible when the summary statement and the full list it summarizes are checked against each other directly, which a version-by-version diff will not surface.

**Watch for in:** Any document with an introductory or summary sentence that states a specific count of items it is about to list (drift signals, principles, boundary types, output counts) — especially documents with a long, incremental Version History showing multiple additive revisions to the same section. Count the actual list independently and check it against every summary statement that claims a count, not just the most prominent one (this project's V7 Upgrade Reference had already flagged the prominent instance; the second, quieter instance in the same document was caught only by the Critic's independent full-document search).

---

## Pattern: Fourth confirmed instance of Coach-side enumeration undercount

**Type:** Review-prompt drafting discipline (Coach-side enumeration undercounts — see original entry above for Type/first three instances)

**Discovered:** World Build Onboarding Framework (L2B), Step 1 pre-review. The Coach's own grep-based text-extraction count found 31 world/Representative-name hits (Alexandria ×17, Theon ×2, gendered pronouns ×3), but the Critic's independent python-docx paragraph-level count found the true numbers were higher: Alexandria ×20, Theon ×3, gendered pronouns ×4 (he×2, his×2).

**Description:** This was later independently re-verified by the Coach directly against the source docx via python-docx and confirmed the Critic's higher count was correct. Root cause suspected: pandoc plain-text line-wrapping can split or obscure matches that a paragraph-level (not line-level) count catches correctly. This is the fourth confirmed instance of this general pattern in this project (see the "Third confirmed instance" entry above for the first three).

**Why it passes surface checks:** A grep/pandoc-based count reads as an authoritative enumeration once it's been run and produces a specific number — nothing about the output signals that some matches were split across wrapped lines or otherwise missed. Only an independent paragraph-level count (python-docx) against the actual document structure surfaces the gap.

**Watch for in:** Every future Coach Step 1 and Critic Step 3 count-sensitive contamination claim. Standing lesson reinforced: grep/pandoc-based enumeration is not sufficient on its own for count-sensitive contamination claims — a python-docx paragraph-text-based full-document string count should be run as a cross-check before finalizing any specific numeric contamination count, both at Coach Step 1 and at Critic Step 3.

---

## Pattern: Critic findings must be verified against primary sources before being folded into a production prompt — confirmed false claim caught

**Type:** Critic review reliability (distinct from Coach-side enumeration undercounts — this is a factual claim error, not a count error, and originates with the Critic rather than the Coach)

**Discovered:** World Build Onboarding Framework (L2B), same review as above. The Critic's Step 3 review claimed "System Operations V1.0 already carries [a] pointer," stating that AI-tool-assignment governance is routed to the Deployment Standards document per Constitution Article 35 §B.

**Description:** The Coach checked System Operations V1.0 directly and found zero references to AI tools, Article 35, or Deployment Standards anywhere in it — the claim was false. The correct governing citation (Article 35 §B naming the Deployment Standards document) was itself accurate and verified against the Constitution text directly, but the claim that System Operations already implements it was not accurate; that document does not yet exist.

**Why it passes surface checks:** A Critic citing a correct Article number alongside a plausible-sounding claim about a sibling document's content reads as verified — the accurate half of the claim (the Article citation) lends false credibility to the inaccurate half (the assertion that System Operations already carries the pointer). Nothing distinguishes the verified part from the unverified part in how the claim is stated.

**Watch for in:** Any Critic finding that makes a specific factual claim about a THIRD document's content (not the document currently under review) — such claims must be independently verified against that third document directly before being relied upon in a production prompt. Critic review is simulated/informational and can itself contain unverified assertions; a correct citation elsewhere in the same claim does not make the rest of the claim true.

---

## Pattern: RETRACTED — "Doc_07 Transmission Tension" was a Coach search-scope error, not a false tracker claim (corrects the previous version of this entry)

**Type:** Coach-side verification gap — searched an incomplete set of locations and concluded a real thing didn't exist

**What happened:** During the Corrections Tracker merge, the Coach searched only `World-Builds/Alexandria/` for "Tension Seven," "trans-generational," and related terms, found nothing, and concluded the v2.0 draft's claimed resolution (Doc_07 Section 3C's "Seventh Tension (Transmission Tension)," added per a Forces Integration Review finding) did not hold up. This was recorded as a confirmed false-resolution finding and folded into Corrections Tracker V1.1 as "Unverified — do not treat as resolved."

**The correction:** Prompted by the project lead's "I have never heard of that until now," the Coach re-searched the full repository, including `Archive/`, rather than only the live world-build folder. `alex_Doc07_V7_r1.docx` — the actual construction-record document the correction referred to — exists in `Archive/Alexandria-Build-History/Alexandria-v7/`, not in `World-Builds/Alexandria/` (which holds a differently-structured, reorganized set of numbered content files, not the original Doc_01-Doc_09 construction records). That file contains Section 3C's Tension Seven — The Transmission Tension, worded almost exactly as the tracker described, with a version-history line reading "Section 3C — Tension Seven (Transmission Tension) added per Forces Integration Review Priority 2 finding." The content also correctly propagated forward into the actual deployed Representative document, `Theon_Representative_V7_r1.docx`, as item 7 of a named tensions list, including the specific "not named explicitly, shapes the urgency" deployment-voice instruction the tracker described. The original v2.0 tracker entry was accurate in every detail. Corrected back to Resolved in Corrections Tracker V1.2.

**Why it passed the Coach's own check:** The Coach's verification instinct (search before trusting a "Resolved" claim) was correct in principle, but the search was scoped to only the live per-world folder. Construction-time build records (the Doc_01 through Doc_09 sequence a Construction Framework build produces) are commonly relocated to `Archive/[World]-Build-History/` once a world's build history is archived, while the live `World-Builds/[World]/` folder holds a different, reorganized content set for ongoing deployment work. A search that stops at the live folder will produce a false negative for anything that lives only in the construction-history archive.

**Watch for in:** Any verification of a claim about world-build construction content (anything referencing a Doc_01-Doc_09-style document, a Checkpoint, or a build-history reference). Search `Archive/[World]-Build-History/` (or equivalently named build-history archive folders) in addition to the live `World-Builds/[World]/` folder before concluding referenced content doesn't exist. The underlying discipline — verify a "Resolved" claim against the actual file rather than trusting the tracker's word — remains correct and should stay standard practice; what needs correcting is that the verification search itself must be as thorough as the claim being checked, covering every plausible location, not just the most obvious one.

---

## Pattern: A ratified document's own paragraph-ordering can be wrong even when its text content is correct

**Type:** Step 6 verification discipline (structural placement defect, distinct from the "missing formatting" pattern above — here the paragraphs are correctly formatted, just placed in the wrong position relative to a section heading)

**Discovered:** Corrections Tracker V1.1. Four corrected items (C1, C4, C5, C8) were moved into what was intended to be "Section 4 — Resolved Corrections" using `heading_paragraph.addprevious(element)` for each item — which inserts every element immediately *before* the heading, not after it. The result: all four items rendered as an unlabeled continuation of the preceding section (Section 3), sitting entirely before the "Section 4" heading text, rather than under it. The text of every moved paragraph was correct; only the structural position relative to the heading was wrong. Not caught until the next revision cycle, when a spot-check of the full paragraph order (not just a text/keyword search) surfaced it.

**Why it passes surface checks:** A pandoc plain-text or grep-based verification confirms every expected string is present in the document and reads top-to-bottom in a plausible-looking order — the section headings and the content are all there, just not correctly nested relative to each other. Only a full ordered paragraph dump (every non-empty paragraph, in document order, with its index) makes the misplacement visible.

**Watch for in:** Any Step 6 verification that moves or re-sections existing paragraphs to sit "under" a heading (rather than only inserting new content or editing text in place). Insert relative to the heading's already-first-child element (or use `addnext` on the heading itself, chaining forward) rather than `addprevious` on the heading — and always confirm with a full ordered-paragraph dump of the affected region, not just a keyword search, that moved content actually sits after the heading it's meant to belong to.

---

---

## Pattern: A live Representative's deployed prompt can drift from its own World-Builds construction record, silently and legitimately

**Type:** Level 5 (per-world) construction-record staleness — distinct from contamination; the deployed content is correct, the *construction record describing it* is what's wrong.

**Discovered:** 2026-07-19, System Hub. A cross-world audit flagged Bethlehem Circle's (Hieronymian) deployed Permanent Prompt as containing content — an Origenist/Pelagian controversy passage — absent from the reviewed `World-Builds/` copy. Checked whether this was a one-off: diffed all four then-deployed worlds' Permanent Prompts (and, separately, their World Capsule Cores) between `World-Builds/` and `cic-poc/backend/data/`. All four showed real drift; two of four Capsule Cores also drifted. Traced via `git log` on the deployed files: a legitimate, Opus-reviewed, live-tested engineering workstream ("Fable plan") had been directly editing deployed prompts in response to real live-testing findings (length ceilings, register calibration, repetition, lexicon-term coverage gaps) — each fix verified against the running backend before committing — entirely within `cic-poc/`, never touching `World-Builds/`.

**Why it passes surface checks:** Nothing here is contamination or a mistake — every deployed change was itself reviewed and live-verified, often more rigorously than a paper review could manage. A reviewer checking `World-Builds/` alone (the normal review substrate) sees a clean, internally consistent, Opus-reviewed document and has no signal that live reality has since moved past it. The gap only appears when the deployed file and the construction-record file are diffed directly against each other — no single-sided review, however careful, surfaces it.

**Watch for in:** Any live/deployed world, at any periodic Coach verification pass — not just when a specific finding prompts a look. Diff every deployed Representative artifact (Permanent Prompt, World Capsule Core, lexicon/story chunks) in `cic-poc/backend/data/[world]_world/` against its `World-Builds/[World]/` counterpart. A zero diff is the expected healthy state, not an assumption to skip checking. When a real diff is found: sync `World-Builds/` to match the deployed (live-verified) version — the deployed side wins, since it's the one actually tested against the running system — and record the sync with the specific commit(s) responsible, not just "content updated."

---

*End of current log. Add new entries above this line as they surface.*
