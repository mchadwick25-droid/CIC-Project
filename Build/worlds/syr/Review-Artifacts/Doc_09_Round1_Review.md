**Simulated review — informational only, not an Article 31 substitute** (Constitution Article 35, Section B)

**Document reviewed:** Doc_09_Story_Inventory.md, Story-Chunks/*, and Story_Index.xlsx, World #7: Syriac Christianity (Edessa/Nisibis)
**Review round:** 1
**Recovery note:** Verbatim original review-agent output, retrieved directly from the session transcript (`47f6719b-134c-455f-b73b-9be8fc43fd3e.jsonl`, tool_use_id `toolu_01DSgfKcEbtnH6n69UYTfxc8`), not a reconstruction or summary.

---

# Independent Adversarial Review: Doc_09 (Story Inventory), World #7 Syriac Christianity

## Overall Verdict: **NEEDS SUBSTANTIAL REVISION** — requires a second independent review round after fixing.

This is a well-constructed document overall — the Absent Stories section is genuinely specific, the No-Tier-5 discipline holds up under scrutiny, and the syrstory009 Tier 4 composite's element-by-element sourcing checks out against Doc_02/Doc_05 on every point I traced. But I found multiple substantive problems, including one that goes to the document's own explicit completion certification being factually false, and one that goes to the tier classification of the repository's single most load-bearing entry (its only Tier 1 story). These are not typo-level fixes — they require actual re-analysis — so this does not clear as-is.

---

## SUBSTANTIVE Findings

### 1. syrstory001's Tier 1 classification is not adequately justified against the Framework's own test, and is inconsistent with how this same document tiers comparably distant sources elsewhere

**File:** `Story-Chunks/syrstory001_ephrem-famine-death.md`, Tier Justification section; also `Doc_09_Story_Inventory.md` Section 2.

The Framework (framework_v74.txt, Part III) defines Tier 1 as: *"Direct textual attestation within or close to the world's horizon. Named author with identifiable social location. Datable with reasonable confidence."* Gennadius of Marseille's *De Viris Illustribus, Supplement* was written c. 470s–490s — roughly 100 years after Ephrem's 373 death and 60–80 years after this world's own 410 boundary closes. The chunk's own Tier Justification concedes this: *"despite the roughly hundred-year gap between event and source... the genre and specificity, not mere proximity, are what the Framework's own Tier 1 test asks after."*

This defense is weaker than it looks, for three reasons:
- The Framework's actual Tier 1 text foregrounds proximity ("within or close to the world's horizon") before genre; genre-based distinctions are explicitly a Tier 3 concern (hagiographic convention), not the stated Tier 1 test.
- This same document classifies other sources at comparable or *shorter* temporal distances at Tier 2/3, not Tier 1: Chronicle of Edessa (340 years later) → Tier 2; Theodoret (130–160 years later) → Tier 3; Jacob of Serugh's memra (125–150 years later) → Tier 3. Nothing in the Tier Justification explains why Gennadius's ~100-year gap earns a *higher* tier than sources that are closer in time.
- The document itself elsewhere treats **Jerome's own De Viris Illustribus 115 (392/3 CE)** — genuinely contemporary with Ephrem, in-window — as the gold standard for secure attestation (used this way in syrstory008's Usage Guidance: *"this world's own more securely attested record (Jerome, contemporary with Ephrem)"*). The famine-death story is sourced only to Gennadius's later *Supplement* to Jerome's work, not to Jerome's own contemporary entry — meaning the one genuinely in-window source covering Ephrem's biography does not corroborate this claim. The Tier Justification never engages this point, nor does it address what Gennadius's own basis/source for the claim was (contrast Tier 2's own definition, which explicitly asks about "collection history" and traceability to community memory — a question Gennadius's entry is never tested against).

This is the only Tier 1 entry in the entire repository; its classification deserves to actually survive scrutiny against the Framework's stated test, not just an assertion that genre trumps proximity. Recommend re-examining for Tier 2.

### 2. syrstory006 mischaracterizes what Doc_08's Force 2A-1 actually documents

**File:** `Story-Chunks/syrstory006_jacob-nisibis-deliverance.md`, Formation Ecology Connection: *"the very external force (Sasanian military pressure on the Roman-Nisibene frontier) that Doc_08 documents structurally (Force 2A-1 and its Roman-Nisibene antecedents)."*

I checked Doc_08 directly. Force 2A-1 is titled **"Sasanian State Persecution Under Shapur II"** and its full text (`Doc_08_Forces_Document.md`, lines 168–178) is specifically about the poll-tax persecution and episcopal martyrdom campaign within Persia (Simeon bar Sabbae, Shahdost, Barba'shmin, the 20-year vacancy) — not about the military sieges of Nisibis (338/346/350 CE) that this story is actually about. The word "siege" does not appear anywhere in Doc_08. These are related but genuinely distinct historical phenomena — internal state persecution of Christians vs. Roman-Persian frontier warfare over a fortress city — and Doc_08 documents only the former. A downstream builder who follows this citation to verify the military-pressure claim will not find it there.

### 3. Two sources Doc_09 actually relies on are missing from Source_Registry.xlsx, contradicting the document's own completion certification

**File:** `Doc_09_Story_Inventory.md` Section 3 (Absent Stories) cites: *"one source (Vööbus) explicitly flags the Acts of Miles as containing 'fable and fantasy'"* and, separately, *"Some reference tools, including syriaca.org's own Syriac Biographical Dictionary, have historically conflated the two figures"* (also referenced in Section 0's governance note: *"the standard Syriac hagiography catalog (syri.ac) has no entry for Aphrahat"*).

I checked all 51 rows of `Source_Registry.xlsx`. Neither Arthur Vööbus nor syriaca.org/syri.ac appears anywhere in the Registry — not in the pre-existing rows 1–42, and not in the nine new rows (43–51) that Doc_09's own governance note says were added specifically to cover "new sources surfaced at this step." (Vööbus *is* cited elsewhere in this world's documents — Doc_01, Doc_08 — but only for an unrelated claim about Peshitta/Rabbula dating, not for the Acts of Miles characterization used here.)

This directly contradicts Doc_09's Section 4 completion certification, which checks off: *"All new sources appended to Source_Registry.xlsx as Native entries (rows 43–51), consistent with the Registry's own dating-neutral Boundary Status rule."* That checkbox is not accurate — two sources this document actually leans on for specific evidentiary claims were never added. Neither gap is caught by `Story_Index.xlsx`'s "Source Cross-Reference" sheet, because that sheet is scoped only to the nine story chunks' front-matter Source fields, not to citations embedded in Doc_09's own prose (Section 0 and Section 3) — a real structural blind spot in the companion index, on top of the two gaps (Rousseau/Muraviev, Barnard) the workbook does honestly self-flag.

---

## COSMETIC Findings (apply directly, no re-review needed)

### 4. Story_Index.xlsx Source Cross-Reference sheet misattributes Peeters/Burgess between two stories

**File:** `Story_Index.xlsx`, "Source Cross-Reference" sheet, rows for syrstory003 and syrstory006.

The sheet lists "Peeters 1920/Burgess 1988" (Registry row #50) as part of syrstory006's *"Named Source(s) in Chunk Front-Matter."* But syrstory006's actual chunk front matter and body text never name Peeters or Burgess — only Theodoret and Ephrem's Carmina Nisibena. Meanwhile, syrstory003's chunk *does* explicitly cite "Paul Peeters's foundational source-critical study of the whole Jacob dossier (1920)" in its own Tier Justification — yet the Source Cross-Reference row for syrstory003 omits Peeters/row #50 entirely. This defeats the sheet's stated purpose (verification "by lookup... without rereading" the chunks): a reviewer trusting this sheet would conclude the wrong story cites Peeters. Simple fix: swap the attribution between the two rows.

### 5. Confidence-vocabulary drift within Tier 2

syrstory002's uncertain sub-claim is labeled "Contested" — matching the Framework's stated Tier 2 confidence ceiling ("specific details and attributions carry Contested confidence"). syrstory003's uncertain sub-claim (also Tier 2) is labeled "Inferential/Thin," a confidence level the Framework's text introduces starting at Tier 3. Minor, but an unexplained inconsistency between the two Tier 2 entries.

### 6. Unverifiable self-referential rigor claim repeated three times

The phrase "cross-confirmed independently by two separate research passes against the same primary-source quotation" (Doc_09 Section 2, syrstory006's chunk) asserts methodological rigor with no way for a reviewer to check what the two passes actually were, when, or how they differed — unlike other tier justifications in this same document, which name specific scholars and specific disputes (e.g., Bauer vs. Barnard). Not wrong, just opaque; consider naming what was actually checked or dropping the claim.

### 7. Aphrahat-conflation claim's actual scholarly backing isn't named in Doc_09's own prose

Doc_09 Section 3 attributes the Aphrahat/later-hermit conflation finding to unnamed "scholarship," while Source_Registry row #51 shows the actual backing is GEDSH's "Aphrahaṭ" entry (Brock) and Asmussen 1984. The claim is appropriately hedged ("this project's research finds...") and is registered, so this is a transparency gap, not a sourcing failure — but naming the source directly (as row #51 itself invites) would strengthen it.

---

## What I checked and found no problem with

- **No-Tier-5 compliance:** Traced syrstory009's five Source Identification elements individually against Doc_02 Sections 2/3 and Doc_05 Sections 1.1/3.1 — every element (qyama vow, bnat qyama choir performing Ephrem's madrashe, raza/shrara performed in worship, Diatessaron as normative text, combined Nativity-Epiphany calendar) is accurately traceable to the cited sections, with no invented content.
- **syrstory008 / Basil legend:** Internally consistent; correctly distinguishes the misidentification finding (Eusebius of Emesa) from the story's retained formation-ideal value, with appropriately restrictive retrieval conditions.
- **Jacob/Ephrem misattribution (syrstory006):** The Theodoret quotation is used correctly and consistently — it does show Jacob, not Ephrem, performing the miracle, matching the document's own claim.
- **Doc_04 cross-reference:** Verified the exact quoted language in syrstory007 ("be given this document's own reasoning for excluding the Ephrem-choir claim from Doc_04...") against `Doc_04_Gravity_Discovery.md` line 228 — it is an accurate, verbatim match, not a fabricated citation.
- **Doc_02 Section 7 / Doc_08 Section 6 cross-references** in the Absent Stories section: verified directly against both documents — the four named silences (lay believers, bnat qyama women, Jewish dialogue partners, enslaved/lower-status persons) are accurately carried forward.
- **Absent Stories specificity:** All six named gaps in Section 3 pass a genuine specificity test (named sources, named reasons, no placeholder language) — verified independently, not just by trusting the workbook's own self-audit.
- **Boundary Status of rows 43–51:** Checked each of the nine new Registry rows against the stated dating-neutral rule (Boundary Status turns on what a source speaks *for*, not when it was composed) — all nine are legitimately Native under this rule, since each analyzes or attests to a person/event within the 200–410 window even where the source itself postdates it.
- **Tier/confidence consistency across Doc_09 §2, the nine chunk files, and Story_Index.xlsx:** Checked all nine stories line by line — tier numbers and confidence labels match exactly across all three locations (aside from the Tier 2 vocabulary drift noted above, which is a labeling nuance, not a mismatch).

---

*(Agent metadata from original transcript: agentId a16a696e03ad23eef; subagent_tokens 148439; tool_uses 34; duration_ms 507967.)*
