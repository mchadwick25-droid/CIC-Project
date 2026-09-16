# Church in Conversation — Standard Review & Build Checklist

*Reference document for the Coach role. This is the default scope applied to every Critic prompt (Step 2) and every production prompt (Step 4), for every document, unless the Coach explicitly narrows scope for a stated reason (e.g., System Operations, which is intentionally exempt from several of these checks — see Section E). Not a governance document — a working checklist to keep review scope consistent across dozens of documents instead of being redrawn from memory each time.*

*Update this file when a new check earns its place — i.e., when a real finding reveals a gap in the checklist itself, not just a gap in one document. Cross-reference the Pattern Log (`CiC_Cleaning_Pattern_Log.md`) for the worked examples and reasoning behind each item.*

---

## A. CHECK ONE — Generalization Integrity (all six contamination types)

Every document gets scanned for all six, not just the ones that happen to be obvious. A category coming back clean should be stated, not silently skipped — a silent category is indistinguishable from an unchecked one.

1. **Name residue** — any specific world name, Representative/voice name, or named artifact (e.g., "Holding Document v1") that shouldn't appear at this document's Level.
2. **Shape residue** — the hardest to catch. An instruction, rubric, or maturity/readiness descriptor that implicitly assumes one world's formation pattern (textual, philosophical, oral, liturgical, communal, etc.) as the default "complete" or "correct" shape, even with zero names present. Test: would this instruction/descriptor register as achievable for a world whose formation axis looks nothing like the world(s) most influential during this document's drafting?
3. **Theological-gravity residue** — treating one tradition's theological concerns (e.g., allegorical exegesis, philosophical synthesis, sacramental precision) as more central or more evidentially demanding than others by default.
4. **Gendered residue** — default pronouns, voice assumptions, or authority-figure framing that isn't genuinely world-neutral.
5. **Register-clustering residue** — vocabulary or tone (academic register, specific rhetorical style) presented as the default rather than one of several valid registers a world might use.
6. **Doctrinal-framework residue** — assuming a specific doctrinal architecture (a particular orthodoxy/heterodoxy classification model, a specific authority structure) as universal rather than world-derived.

## B. CHECK TWO — Rule 1A / 1B (Level 1 documents only)

- **Rule 1A — No Downstream Causation.** A Level 1 document may not assert or depend on a downstream construction finding.
- **Rule 1B — No Forward-Projected Specificity.** A Level 1 document may state that something will eventually exist but may never state or assume its shape. For Level 3 methodology documents, Shape residue (A.2) is the operative equivalent check — apply that instead.

## C. Level-specific CANNOT-CONTAIN rules

- **2A (Architecture):** World names permitted only via the five-world registry exception. No live per-world status (that's 2C). No restated Level 3 methodology instructions (descriptive-not-formative check — a "Governed by: [Level 3 doc]" citation is fine; restating the instruction itself is not).
- **2B (Entry):** No world name, no Representative/voice name, no methodology steps, no formation content, no current project status.
- **2C (Status):** Live status content lives here — this is the document that 2A/3A/3B/3C/3D content should point *to*, not duplicate.
- **2D (Operations) and any future operational-parameter document:** Exempt from the name/status prohibitions below — see Section E.
- **3A/3B/3C/3D (Methodology):** No world name at all, no Representative/voice name at all — **no five-world-registry exception at Level 3**, unlike 2A. No live status, no funding/monetization content, no per-world build tracking.

## D. Filing, naming, and citation hygiene — every document

1. **Scaffolding removal.** Remove in full, no replacement text: Version History sections, Builder Verification / Builder Checklist sections, bracket annotations (`[MODIFIED]`, `[NEW]`, or similar — including any "[formerly X]" parenthetical), and every paired `*Delta: ...*` note. The substantive content a Delta note describes stays; only the tag and the note go. Search the full document independently — do not rely on an illustrative list, and check for both singular and compound/plural forms of whatever pattern you're removing (e.g., "Article 28" and "Articles 28 and 29" are both citations; a regex tuned to only the singular form will silently undercount).
2. **Unrecognized governing authority.** Remove any reference to a document that claims governance/constitutional authority but doesn't appear in the current locked Document Precedence Rule (only Vision, Constitution, and Essential Experience are supreme). "Holding Document v1" is the recurring confirmed instance — check for it and for any other superseded interim-authority document.
3. **Constitution/Level-1 citation accuracy — full audit, not a sample.** Every "Article N" (and "Articles N and M") citation gets checked against the actual current locked Constitution V2.2 text, not assumed correct because the document claims to be "updated to current numbering." Known drift sources: the Article 34 ("Doorway Not a Home") insertion shifted the former 34/35/36 cluster to 35/36/37 in every document that predates it; an earlier remap moved old 20→33, 21→28/29, 22→31, 23→32. A document can have correctly fixed one remap and still carry the other, undetected. Cross-check for internal consistency too — the same concept cited with two different article numbers in the same document is a strong signal one of them is wrong.
4. **Sibling-document citation drift.** Every citation to another CiC document's version number is checked against that document's actual current filename in the live repository — never trusted because it looks precise, and never trusted because another document cites the same number (staleness can propagate). Where practical, reduce sibling citations to name-only (drop the version number entirely) rather than hardwiring a pin that will go stale the next time that sibling is revised — especially important when multiple documents in the same batch are being re-versioned together.
5. **CO-012 operational-parameter scrub — two-way.** No hardwired vendor name, tool name, specific token count, cost figure, or platform name in any governance/methodology document. Replace with a pointer to System Operations (`reference/L2D-System-Operations/CiC_L2D_System_Operations_V1.0.docx`). Search independently across the whole document/batch — don't stop at the first confirmed instance. **Exception:** build-process governance vocabulary ("Opus," "Claude Code" as review/oversight roles) is not a CO-012 violation — see Section E for the test. This check runs both directions: (a) scrub operational specifics *out* of the document under review, and (b) check whether the document surfaces any operational parameter, deployment consideration, or configuration detail that *isn't yet captured* in System Operations — if so, flag it as a candidate System Operations update rather than just deleting it. System Operations is a living reference that should grow as documents are cleaned, not a one-way dumping ground.
6. **"CLEAN ✓" is not permission to skip.** A prior CLEAN rating from Project Status or any other source is scoped to whatever checks that pass actually ran, not a guarantee of current-standard compliance. At minimum, spot-check any "clean" document for the scaffolding items in D.1 before treating it as done.
7. **World-specific documents never sit at Level 2, even temporarily.** A world-specific companion or supplement to a Level 2 document (e.g., a per-world Deployment Config) belongs in that world's own `worlds/[World]/` folder, never in the Level 2 folder — and it should not be created in advance of need. It comes into existence only once that world's build actually reaches the stage requiring it.
8. **Naming convention.** `CiC_[Level]_[DocumentName]_V[Major].[Minor].docx`. No version history, bracket annotations, delta notes, or builder checklists in ratified text — the version number in the filename (and matching internal title/header/footer) is the sole self-identification.
9. **Filing policy.** Only the latest ratified version stays in the working/master directory. Superseded originals and duplicates move to `Archive/` (generally `Archive/Superseded-Housekeeping/` for this cleaning project's own superseded inputs). Don't delete without an explicit instruction; don't leave superseded copies sitting alongside the ratified version either.

## E. Exceptions — read before applying D.5 and C

- **System Operations (and any future document explicitly designed to hold operational parameters)** is the intentional sink for vendor names, token counts, per-world build status, and similar content. Do not apply C's name/status prohibitions or D.5's vendor-name scrub to a document whose stated purpose is to hold that content — that would defeat the document's purpose. Confirm the document's stated purpose before applying or waiving these checks.
- **CO-012 boundary test:** does the name describe *which model/tool a Representative or Facilitator runs on at runtime* (a deployment parameter — CO-012 applies, point to System Operations) or *which role reviews/builds the system* (a governance-structure term, e.g. "Opus leads, Claude Code executes" — CO-012 does not apply, sanctioned per Constitution Article 35 §B)? Apply this test rather than re-litigating from scratch each time "Opus" or "Claude Code" appears in a document about the review/build process itself.

## F. Consistency and value check (beyond contamination)

Confirm the document is internally consistent with everything already ratified this cycle — not just clean of contamination. Check for: drift from a sibling document's own current account of shared methodology (e.g., does this document's description of how Forces integrates match Forces Framework's own description), duplication or contradiction with content now living in System Operations or Phase Structure, and any other case where two ratified documents would give a builder conflicting instructions. Healthy redundancy (a document correctly restating its own governing article) is fine; contradiction is not.

**Change Orders Register cross-check — V7 upgrade pass.** Before finalizing Step 2 scope, check the Change Orders Register for any approved-but-not-yet-implemented change order that affects the document under review (e.g., CO-013's pending deployment-output count expansion), and fold implementation into this review rather than treating the document as done once it's merely decontaminated. The goal of this whole project is not just removing what's wrong but bringing each document up to the current state of V7 thinking — a document can pass every contamination check and still be behind on an approved architectural decision.

**V7 Upgrade Reference cross-check — every document, every review.** Check the document under review against every applicable item in `reference/Project-Reference/CiC_V7_Upgrade_Reference.md`'s 15-item upgrade table (level structure/Layer language, Forces split, Representative Emergence ordering, build sequence step count, confidence vocabulary, story tiers, deployment output count, DOCX/MD format, context isolation, three-tier retrieval, Author Gravity discipline, TC-001 fabrication prohibition, 2A/2B/2C sublevel structure, Holding Document supersession, Doorway Not a Home). A document can be fully decontaminated and still be a full generation behind the current architecture (e.g., an 8-step build sequence when the current standard is 10) — that gap is real work, not contamination, and needs a scope decision (fold into the current batch vs. dedicated follow-on task) before drafting the Critic prompt, same as any other structural finding under G.3. That reference document also holds the full six-type CHECK ONE taxonomy with named per-world shape-residue profiles (Alexandria, Desert Christianity, Early Communal) — use those specific profiles for Section A.2 (Shape residue) rather than the generic description alone.

## G. Coach process discipline (applies to how prompts are drafted, not to document content)

1. **State the general rule, not just an illustrative list.** "Remove every X, wherever it appears — search the full document" is the operative instruction; any list of examples is non-exhaustive and must be labeled as such. A Builder working literally from an example list will miss whatever the list omits.
2. **Verify enumeration by direct search, not memory** — including your own Step 1 read. Regex/grep-built inventories need the same discipline: account for plural/compound forms explicitly, not just the most common singular pattern.
3. **Surface structural/scope questions before drafting a Critic prompt**, don't resolve them unilaterally — e.g., "does this document actually belong at this Level," "does this need a split," "where does new content go." Get a decision, then draft.
4. **Verify Step 5 by reading the produced document directly from the repository** — never accept a Builder's self-report as sufficient confirmation.
5. **State checklist coverage in one sentence with every Critic/production prompt.** When presenting a Step 2 or Step 4 prompt, include a single confirming sentence that the full standard scope was applied to this specific document — contamination (all six CHECK ONE types), CO-012 (pointing to System Operations rather than deleting outright), scaffolding/citation/filing hygiene, and the V7 Upgrade Reference cross-check — not a generic list, but scoped to what was actually checked for this document. This is a visible receipt that the checklist governed the prompt, not a substitute for actually running it.
6. **Insert new content by copying and editing a sibling paragraph, never by writing a fresh `<w:p>` from scratch**, when a production prompt calls for adding a list item, section, or table row. A fresh paragraph silently drops whatever explicit `<w:pPr>`/`<w:rPr>` formatting its siblings carry (see Pattern Log: "Builder-inserted content lacks the explicit formatting its siblings carry," confirmed twice). If content was inserted freshly anyway, Step 6 must include an XML-level formatting check against a sibling paragraph, not just a text-level one.

## H. Deployment/construction-record sync check (Level 5, live worlds only)

Applies whenever a periodic verification pass touches a world that has any live/deployed
artifacts in `cic-poc/backend/data/[world]_world/` — a distinct check from A-G, which govern
Level 1-4 document contamination and hygiene.

1. **Diff every deployed Representative artifact against its `worlds/[World]/`
   counterpart** — Permanent Prompt, World Capsule Core, and a spot-check of lexicon/story
   chunks. A zero diff is the expected healthy state, not something to assume without
   checking (see Pattern Log: "A live Representative's deployed prompt can drift from its own
   worlds construction record, silently and legitimately," 2026-07-19).
2. **A real diff is not itself a defect to fix by reverting.** Check `git log` on the deployed
   file first — if the change is a reviewed, live-verified engineering fix (not an
   unreviewed edit), the deployed version is very likely the one that should win. Sync
   `worlds/` to match it, don't revert deployment to match the (now-stale) construction
   record.
3. **Record the sync with real provenance** — cite the actual commit(s) responsible in the
   decision log, not just "content updated." Do not embed provenance notes inside the prompt
   files themselves; they're clean runtime prose by design (no headers, no markdown) and a
   note inserted there risks shipping as part of what a participant's Representative actually
   says.
4. **Do this at every periodic Coach verification pass for any world with live deployment**,
   not only when a specific complaint or finding prompts a look — the gap is silent by
   construction (see Pattern Log entry) and won't surface on its own.

---

*This checklist supersedes ad hoc scope-drafting for every future Critic and production prompt. When a document's situation requires deviating from it, state explicitly which items are being waived and why (as with System Operations, Section E) rather than silently narrowing scope.*
