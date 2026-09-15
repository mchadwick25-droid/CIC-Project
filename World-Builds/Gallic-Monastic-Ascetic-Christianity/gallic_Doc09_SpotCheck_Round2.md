# Doc_09 — Story Inventory: Independent Adversarial Spot-Check, Round 2 (bounded)

**Reviewer:** fresh-context subagent (model opus), no drafting involvement, no Round 1 involvement.
**Date:** 2026-09-10.
**Scope:** BOUNDED verification of the Round 1 fix round only — each finding checked at its own locus (and at every locus it touches), plus the three cross-cutting checks the commission named. Not a fresh full review.
**Documents under check:** `gallic_Doc09_Story_Inventory.md`; `Story-Chunks/gallicstory001–014`; against `gallic_Doc09_Review_Round1.md`.

**Governing text located and read.** `L3B-World-Build-Methodology/CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` was extracted directly (`word/document.xml`, 723 lines of running text) and read at the four-tier passage. Vendored primaries re-read directly from `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml` by div id (a div-scoped extractor, not line numbers), and `cic/texts/npnf203_…`. Every quotation reported below was re-verified at its own locus in this pass — none is carried from Round 1's say-so.

---

## Verdict

**Residual issues found.** Eleven of the twenty-two dispositions are clean. Eleven are not: three High-severity findings have surviving residue at loci the fix round did not visit, one Low "fix" **introduced a new factual error by adopting a Round 1 claim that is itself wrong**, and the fix round introduced a systemic new defect (build-thread annotations inside deployment-facing Story Text, against fourteen standing assertions that none remain).

The established failure pattern recurred, in all three of its forms:
- *a fix asserted is not a fix applied* — H1's own fabricated phrase still stands in Section 7(a); M9's map is still wrong on six of nine rows while the Document Log claims it was ground-truthed;
- *the same defect recurring where the fix round did not touch* — "at Tours" (H2) survives twice in gallicstory007's apparatus; "Trier" (L2) survives in eight further places, one of them inside the sentence announcing the L2 fix;
- *a claim reused without re-verification at its own locus* — L3's chapter "correction" was applied on the Round 1 reviewer's word; at the locus, the original citation was right and the correction is wrong.

---

## HIGH

### H1 — CF V7.4 quotations in Section 2 and six chunks — **PARTIALLY FIXED (residual)**

**Section 2 and all six chunks: CONFIRMED FIXED.** The four-tier text now in Section 2 is CF V7.4's own wording. Verified phrase by phrase against the extracted docx:

- Tier 1: *"Direct textual attestation within or close to the world's horizon. Named author with identifiable social location. Datable with reasonable confidence…"* — exact.
- Tier 2: *"Stories transmitted in collected form with identifiable collection history, traceable to the world's own community memory… Academic consensus treats the tradition as authentic even where individual attribution or detail cannot be verified. The collection itself is evidence of what the community remembered and valued."* — exact; the ellipsis correctly elides one intervening sentence.
- Tier 3: *"Material attributed to specific figures or moments…"*, *"Hagiographic narrative is a specific type within this tier"*, *"the miracle sequence"*, *"recognizable hagiographic conventions"*, and *"The formation ideal communicated is credible evidence; the specific events claimed are not."* — all exact.
- Tier 4 and No Tier 5 — exact.

The two fabricated phrases Round 1 named are gone from all six chunks. gallicstory001, 003, 014 now quote Tier 3's genuine sentence; 008, 010, 012 now quote Tier 2's genuine sentence. Confirmed by grep: `"the formation ideal it communicates is the evidence, not the specific events claimed"` — 0 hits in the world build; `"individual attribution may be uncertain, but the tradition itself is treated as authentic"` — 0 hits.

**RESIDUAL 1 — the fabricated Tier 2 phrase survives in the main document, at Section 7(a).** Line 169 still reads:

> This document's own reasoning is that Tier 2's **"individual attribution may be uncertain"** does not describe a named author's account of his own encounter with a named man…

`grep -c "attribution may be uncertain" cf74.txt` → **0**. This is the same Donatism paraphrase H1 condemned, still inside quotation marks and still attributed to the Framework's Tier 2 — in the passage that carries the document's *load-bearing* Cassian tier ruling. The fix round proves it knew the correct text: gallicstory012's Tier Justification (line 83) makes the identical argument and now quotes CF correctly (*"academic consensus treats the tradition as authentic even where individual attribution or detail cannot be verified"*). Section 7(a) was simply not visited.

**RESIDUAL 2 — the fix round mis-locates the text it says it retrieved. The four-tier framework is CF V7.4 Part II, not Part V.** CF V7.4's part boundaries, read directly:

| CF V7.4 line | Heading |
|---|---|
| 87 | Part I — World Identification & Boundaries |
| **142** | **Part II — Evidence Development** |
| 277 | Part III — Ecological Reconstruction |
| 417 | Part IV — Interpretive & Theological Development |
| **443** | **Part V — Encounter Development** |

"Story and Narrative Sources Assessment" (line 248), "The four-tier story classification framework" (line 251), the Tier 1–4 definitions (252–268), "No Tier 5" (269), and "Story Inventory Requirement" all sit inside **Part II**. Part V is Encounter Development (encounter philosophy, world package, facilitator apparatus) and contains no tier material.

Doc_09 asserts "Part V" for this content in at least six places: header line 6 ("Part V — Story Classification, Story Inventory Requirement"), line 10 ("CF V7.4 Part V (the four-tier classification, quoted at Section 2)"), Section 2 line 37 ("Re-read directly from the Construction Framework V7.4 extracted text (Part V)"), Section 10 line 208, Document Log line 220, and the H1 fix entry itself at line 223 ("**CF V7.4 Part V's actual text** retrieved from the cached extraction"). Round 1 did not catch this, but the H1 fix re-asserted it while claiming to have gone to the governing text — which is evidence the retrieval was not made by navigating to the named Part.

### H2 — editorial place-names in Story Text; Section 4 audit rows — **PARTIALLY FIXED (residual)**

**Fixed and confirmed:**
- gallicstory003 Node note: "Ligugé"/"Poitiers" removed, both named as editorial (Gibson's, Roberts's). ✓
- gallicstory004 Story Text: "the monk of Ligugé" removed. ✓
- gallicstory006 Story Text and Node note: "Marmoutier" → "Martin's own dwelling"; verified against `Dial.` III.15 (div `ii.iv.iii.xv`), which names only "that wooden seat of his… placed in the small open court which surrounded his abode." ✓
- gallicstory007 Story Text: "Of the funeral at Tours" → "Of the funeral, at the city his body was brought to". ✓ Independently re-verified: `Ep.` III (div `ii.iii.iii`, 13,069 chars, read whole) contains **zero** occurrences of "Tours". The letter says only "the whole city poured forth to meet his body."
- Section 4 audit rows updated for all four chunks (lines 94, 95, 97, 98). ✓ Propagation to Section 4: passes.

**RESIDUAL 3 — "at Tours" survives twice in gallicstory007, including in a field the Document Log claims was fixed.** The Document Log (line 224) says the fix landed "in gallicstory003, 004, 006, 007's Story Text/**Node notes**". gallicstory007's Node note was not touched:

- Line 51, *Node note*: "Tours (the northern node), **at Condate and then at Tours**, 397."
- Line 79, *Tier Justification*: "a bishop dying of fever on a peacemaking journey, among disciples, and **buried at Tours** before a vast crowd…"

Both assert exactly the claim H2 said `Ep.` III does not support, in the same chunk whose Story Text was corrected on that ground.

**RESIDUAL 4 — "Marmoutier" survives in gallicstory006's own front-matter.** Line 36, *Retrieve-When*: "what 'ridiculous fancies about visions' meant **inside Marmoutier**" — seventeen lines above the Node note that says `Dial.` III.15 does not name Marmoutier. The Document Log's "Naming/term propagation check" (line 245) claims the four H2 corrections "were checked against every chunk"; this one was missed inside the corrected chunk itself.

### H3 — Egyptian/Eastern origin disclosed in Story Text / Formation Ecology Connection — **CONFIRMED FIXED**

Both loci, both chunks. Verified in the chunk bodies, not the front-matter:

- **gallicstory010**, Story Text line 54: "Among the examples of **the Egyptian fathers** that Cassian set down for **the monks of Gaul** is this one… **received into Gallic cells as Egypt's own saying, not this world's own invention**." Formation Ecology Connection line 64 also carries it: "**Egypt's own exchange, transmitted, not Gaul's own invention** (Doc_04 §7; Doc_05 §7.2; Doc_06 §4(a))." ✓
- **gallicstory013**, Story Text line 70: "Cassian records how the question of grace and effort came up **in Egypt** — not in a school, but between two friends at the hour of prayer, **at the cell of an Egyptian elder near Panephysis**, written down afterward **in Gaul** for the brothers at Lérins." Formation Ecology Connection line 86: "the argument's own origin is **received Egyptian experience, not a Gallic house's invention**." ✓

This is the consequential one Round 1 named, and it is properly closed at both required levels.

### H4 — "Built from" line-range disclosure — **PARTIALLY FIXED (residual)**

**Fixed and confirmed.** The new paragraph at line 13 is honest and does the work asked: it states the ranges "were not independently reproducible against either a freshly-rebuilt flattening or Doc_05's own review-corrected search_record ranges for the same file, and this drift was not disclosed in the original draft"; it discloses the divergence from an Approved sibling; and it establishes the authority explicitly — "they are retained as a drafting note but are **not the authoritative locus for verification** — the div id is." That is establishment, not gesture. I independently re-verified eight div ids against the XML and all are correct (`ii.ii.x` = *Vita* IX; `ii.ii.xi` = *Vita* X; `ii.iv.iii.xv` = *Dial.* III.15; `ii.vi.ii.l` = *SH* II.50; `iv.iii.ii.v`/`vi` = *Inst.* II.5–6; `iv.iii.v.xxvii` = *Inst.* V.27; `iv.iii.iv.xix` = *Inst.* IV.19).

**RESIDUAL 5 — Section 10(a), the exact locus Round 1 named, was not updated.** H4's closing sentence was: "Half the verification handle **Section 10(a)** points reviewers to is broken." Section 10's Review requirement (line 212) still reads:

> **(a)** spot-check every quoted phrase in every Story Text against `npnf211`/`npnf203`/the Hilary file directly **at the div ids and line ranges given**

It still directs the next reviewer to the handle the document has just declared non-authoritative. One-clause fix.

---

## MEDIUM

### M5 — gallicstory013 Conference number — **CONFIRMED FIXED**
Source field now reads "*Conferences* XIII.1–3 — **the Third Conference of Abbot Chæremon**", with the correction and the reason stated. Verified against npnf211: "XII. **The Second Conference of Abbot Chæremon. On Chastity. Not translated.** XIII. **The Third Conference of Abbot Chæremon.** On the Protection of God." Story Text line 71 agrees ("At the opening of his Thirteenth Conference"). ✓

### M6 — gallicstory011 quotation splice — **CONFIRMED FIXED**
Tier Justification now reads: "introduced, at *Conf.* XVIII.15, as '**the other instance of Abbot Paphnutius**'". Verified at div `iv.vi.ii.xv`: "Now let us give **the other instance of Abbot Paphnutius**…" The *Conf.* II.5 phrase "as we promised to do" is gone. ✓

### M7 — Gibson's "buffalo" gloss — **CONFIRMED FIXED, and the Round 1 claim independently upheld**
Story Text now reads: the anchorites called him "Bubalis" (**Gibson's editorial note glosses this as 'the buffalo'; the text itself does not translate the name**). I checked the raw XML rather than the flattened text, because a flattener inlines notes and would have made the Round 1 finding look wrong:

```
gave him the name of\nBubalis,<note n="2090" id="iv.vi.ii.xv-p2.2">
  <p class="endnote" id="iv.vi.ii.xv-p3"> i.e., the Buffalo. On
  Paphnutius see the note on Conf. III.</p></note>
```

"i.e., the Buffalo" is inside `<p class="endnote">`. Round 1 was right; the fix is right. ✓

### M8 — gallicstory004 "defensor" footnote — **CONFIRMED FIXED**
The narrative identification is withdrawn and the withdrawal disclosed (line 61). Verified at *Vita* IX (div `ii.ii.x`): the ancient text says only "It was believed that this Psalm had been chosen by Divine ordination, that Defensor might hear a testimony to his own work"; the Vulgate *defensor* identification is Roberts's footnote. ✓

### M9 — Section 9 item 6 gravity map — **PARTIALLY FIXED (residual)**

I recomputed ground truth independently, extracting every bold gravity header from each chunk's Formation Ecology Connection section (a first regex pass under-reported G6 because its headers nest italics — `**G6 — *virtus***` — so I re-ran with a corrected pattern).

**Ground truth (bold gravity headers, Formation Ecology Connection sections, all 14 chunks):**

| Gravity | Chunks that name it | Map in Section 9 item 6 | Delta |
|---|---|---|---|
| G1 | 002, 003, 004, 005, 006, 012, 014 | 004, 012, 014 | **missing 002, 003, 005, 006** |
| G2 | 014 | 014 | ✓ |
| G3 | 013 | 013 | ✓ |
| G4 | 005, 008, 009, 013 | 005, 008, 009, 013 | ✓ |
| G5 | 001, 003, 007, 010, 012, 013 | 001, 007, 010, 012 | **missing 003, 013** |
| G6 | 001, 002, 003, 004, 005, 006, 007, 014 | 003, 004, 005, 006 | **missing 001, 002, 007, 014** |
| G7 | 008, 009, 010, 011, 013 | 009, 010, 011, 013 | **missing 008** |
| G8 | 001, 002, 007 | 002, 007 | **missing 001** |
| G9 | 004, 005, 006, 012 | 004, 005, 012 | **missing 006** |

The two errors Round 1 named are gone: "G2: 008" and "G4: 008, 004" are corrected. But **six of nine rows are still incomplete**, and the map's own parenthetical (line 200) claims otherwise:

> the map above is **checked directly against each chunk's own Formation Ecology Connection**

It was not. The G7 omission is the sharpest demonstration: the fix note states "gallicstory008 names G4, not G2" — correct — but 008's Formation Ecology Connection names *both* G4 and "**G7's temporal skeleton**", and 008 was not added to G7's list in the same edit. Likewise 006's "**G1 × G9**" was read for neither G1 nor G9.

The map's *purpose* claim — "every Primary and Supporting gravity, and both Tensional ones, has at least one story" — remains true. The map itself is not the ground truth it now says it is.

### M10 — Section 5 rows 2, 7, 10 — **CONFIRMED FIXED (one small inconsistency)**
Checked against `gallic_Source_Registry.md`:
- **Row 7:** Registry Licensed-For = "Egyptian-to-Gallic transmission-and-adaptation; Castor/Apta Julia dedication; dress/daily-life (**Institutes I.10**)". Section 5 now quotes the narrowing parenthetical in full and discloses the judgment call. ✓
- **Row 2** ("Martin-circle correspondence context") and **row 10** ("General corpus completeness"): judgment-call language added and explicitly recorded as a judgment, not asserted as covered. ✓

*Minor:* the Document Log (line 232) says judgment-call language was disclosed "at rows 2, 7, 10 **and the section's closing summary**"; the closing summary (line 134) still says "**two** (rows 2, 10) required this document's own judgment call," which does not match the three rows actually carrying it.

### M11 — Section 5 row 9 confidence for gallicstory013 — **PARTIALLY FIXED (residual)**
The gallicstory013 row is now correct: "A (dedication) / **B** (editorial Lérins/abbot identification) / C, **except *Conf.* XIII**". This matches the Registry exactly: row 9 = "A (dedication text) / B (editorial identification of Lérins/abbot) / C (content, except Conf. XIII)". ✓

**RESIDUAL 6 — the identical misstatement survives one row above.** Section 5's **gallicstory012** row (line 128) still gives row 9's confidence as "**A (dedication) / C (content)**" — the same dropped B tier M11 was raised about, in the only other row in the document that cites row 9. The fix corrected the row Round 1 named and not the row beside it.

### M12 — Section 9 item 1 novelty claim — **PARTIALLY FIXED (new residual)**
The specific overclaim is corrected: the sentence now credits Doc_05 §4.4, which does indeed quote "a certain Ruricius, one of the citizens, pretending that his wife was ill" and "multitudes of the citizens … previously … posted by the road" (Doc_05 line 262, §4.4). ✓

**RESIDUAL 7 — the rewritten sentence carries a fresh false novelty claim.** It now reads: "the full election scene's mechanics — **the absent reader is new here**". It is not. Doc_05 **§3** (line 216) already quotes it:

> at Martin's election, when the reader **"failed to appear,"** a bystander **"laying hold of the Psalter, seized upon the first verse which presented itself to him,"** which named Defensor (*Vita* ch. IX, `ii.ii.x`, file lines 766–787, read this pass…)

The M12 fix checked Doc_05 §4.4 (the section Round 1 named) and did not check the rest of Doc_05 for the element it was newly asserting as novel.

### M13 — gallicstory005 SH II.50 vs Dial. III.11–13 — **FIXED at all four named loci; two new defects introduced**
Confirmed corrected in the Confidence field (lines 12–21, now spelling out that *SH* II.50 narrates the earlier phase, the plea before the execution, and *Dial.* III.11–13 the later visit), the Source field (lines 29–35, "a related but distinct episode, **not independent corroboration** of this chunk's own narrated events"), and the Tier Justification (line 90, "sharing the setting … and Martin's principle **without narrating the same events**"). "The best-corroborated Martin narrative" and "independently … converging" are gone from the substantive claims. ✓

**RESIDUAL 8 (new defect, two parts, both in gallicstory005):**
1. The Story Text's correction note is self-contradictory. Line 66 reads: *"Sulpitius's Sacred History narrates an earlier phase of the same affair, **in his own voice** (corrected, Round 1 review finding M13 — **not "the same affair… in his own voice,"** which overstated the overlap…)."* The parenthetical disclaims the exact wording the corrected sentence uses.
2. The Final Assembly Instruction (line 106) still certifies: "Story Text read against its tier register: it names the author, the narrator, and **the second corroborating work** in the telling" — reinstating, in the chunk's own sign-off, the corroboration framing M13 removed everywhere else.

---

## LOW

### L1 — "he"/"said he" restored — **CONFIRMED FIXED (both chunks, verified at source)**
- **gallicstory012**, line 67: `"Come," said he, "see in the meanwhile the old men…"`. Source, div `iv.v.ii.ii`: `"Come," said he, "see in the meanwhile the old men who live not far from our monastery…"` — exact. ✓
- **gallicstory011**, line 69: `"possessed by a most fierce demon, he made known all the craft of his secret plot, and the same man who had conceived the accusation and the cheat betrayed it"`. Source, div `iv.vi.ii.xv`: `For possessed by a most fierce demon, he made known all the craft of his secret plot, and the same man who had conceived the accusation and the cheat betrayed it.` — exact. ✓

### L2 — "Trier" vs "Treves" — **PARTIALLY FIXED (residual)**
Verified at source: `Ep.` III writes "while you were dwelling at **Treves**"; "Trier" occurs nowhere in the vendored volume. gallicstory005's Node note and Story Text are corrected. ✓

**RESIDUAL 9 — the same defect stands in eight further places, one of them inside the sentence that announces the fix:**

| File | Line | Text |
|---|---|---|
| `gallic_Doc09_Story_Inventory.md` | 98 | Section 4, gallicstory007 row: "**Bassula at Trier**, …" — *in the same audit cell that states* "finding L2 also fixed — 'Trier' in gallicstory005 corrected to the vendored volume's own 'Treves.'" |
| `gallic_Doc09_Story_Inventory.md` | 59 | Story Index: "**Trier** and the Ithacian Communion" |
| `gallic_Doc09_Story_Inventory.md` | 195 | Section 9 item 1: "the full **Trier** sequence" |
| gallicstory005 | 4 | Story-Title: "**Trier** and the Ithacian Communion" |
| gallicstory005 | 16 | Confidence field: "Martin's plea at **Trier** *before* Priscillian's execution" |
| gallicstory005 | 47 | Retrieve-When: "Doc_08 Force 2A-3 (the imperial court at **Trier**)" |
| gallicstory005 | 98 | Usage Guidance: "this world's own memory of **Trier**" |
| gallicstory007 | 57, 79 | Story Text "then living at **Trier**"; Tier Justification "(Bassula, at **Trier**)" — narrative prose, the category L2 named |

The two gallicstory007 instances are the more serious: they are the identical defect in a chunk the fix round *did* open (for H2), and one is in Story Text.

### L3 — Sarabaite citation, "or rather", "as we have seen" — **NOT FIXED; the one change made INTRODUCES A NEW ERROR**

Round 1's L3 had three parts. Only one was acted on, and it was acted on wrongly.

**(a) The Sarabaite chapter — the "correction" is itself incorrect.** Section 6 item 7 now reads:

> **The Sarabaite** (*Conf.* **XVIII.4**, corrected, Round 1 review finding L3 — the prior draft cited XVIII.7, **the chapter on the anchorites' origin, not the Sarabaites'**; lexicon 069)

I extracted Conference XVIII's chapters by div id. The actual headings:

| Chapter | div | Heading |
|---|---|---|
| IV | `iv.vi.ii.iv` | Of the three sorts of monks which there are in Egypt |
| V | `iv.vi.ii.v` | Of the founders who originated the order of Cœnobites |
| **VI** | `iv.vi.ii.vi` | **Of the system of the Anchorites and its beginning** |
| **VII** | `iv.vi.ii.vii` | **Of the origin of the Sarabaites and their mode of life** |

So: **XVIII.VII *is* the Sarabaites' own chapter.** XVIII.VI is the anchorites' origin. XVIII.IV is the three-kinds overview, which only mentions them in passing ("The third is the reprehensible one of the Sarabaites"). Round 1's L3 was wrong on both halves of its claim, and the fix round adopted it without going to the locus — the exact "quotation/claim reused without independent re-verification" pattern the commission asked me to hunt. **The original draft's XVIII.7 was correct and should be restored**, with the editorial gloss removed.

Related, at the same edited locus: the item quotes the category as "**the reprehensible third kind**". `grep` over the whole vendored volume: 0 hits. The text reads "the reprehensible one of the Sarabaites." A new unverified quotation, introduced at a locus the fix round touched.

**(b) "or rather" — NOT FIXED.** Section 6 item 9 (line 155) still reads: "…**to provide against my forgetfulness**". Source (*Commonitory* ch. 1): "such as may aid my memory, **or rather, provide against my forgetfulness**". The excision is still unmarked, and the quotation also silently adds "to". Not mentioned anywhere in the Document Log.

**(c) "as we have seen" — NOT FIXED.** Section 4's gallicstory014 row (line 105) still lists "**the serpents' yielding 'as we have seen'**". The chunk's own Story Text (line 67) attaches it correctly — to the serpents *never being a danger*, not to their yielding ("cedit turba serpentium"). The audit row and the chunk still disagree in exactly the way Round 1 described. Not mentioned in the Document Log.

The Document Log's L3 entry (line 238) describes L3 as consisting solely of the chapter citation, which is why (b) and (c) were never reached.

### L4 — Eucherius harbour image — **CONFIRMED FIXED (all three loci)**
- Section 5 (line 132): harbour image "named only in gallicstory014's Retrieve-When, as a retrieval trigger, not rendered in its Formation Ecology Connection"; what the connection draws is "crying signs". ✓
- Section 6 item 13 (line 159): same correction, consistently worded. ✓
- gallicstory014 confirms both: Retrieve-When line 45 names "G2's harbour image (Doc_04 G2)"; Formation Ecology Connection line 77 draws "Eucherius's admiration of the Egyptian fathers' 'crying signs' (row 26, Doc_04 G6)". ✓

Propagation across the three loci: passes.

### L5 — gallicstory003 *Vita* VI import — **CONFIRMED FIXED**
Story Text line 51 now opens at the VII locus: "**'As Hilarius had already gone away, so Martin followed in his footsteps'**". Verified at div `ii.ii.viii`: "As Hilarius had already gone away, so Martin followed in his footsteps; and having been most joyously welcomed by him, he established for himself a monastery not far from the town." The exile/return narration is gone from Story Text. ✓

*Minor:* the Node note (line 43) still frames the monastery as one "Martin founded **after Hilary's return**" — a *Vita* VI framing carried in apparatus rather than Story Text. Low severity; Section 4's audit claim is about Story Text elements and holds. Flagged for the build thread's judgment only.

### L6 — gallicstory006 Confidence overreach — **CONFIRMED FIXED**
Confidence field now states only what the locus states — Brictio, whom Martin "could not be induced to remove… from the presbyterate" — with the withdrawn claim named. The Source field adds the same limit. Verified against div `ii.iv.iii.xv`, which fixes nothing about Brictio's status at time of writing. ✓

### L7 — gallicstory012 *Conf.* XI.2 description — **CONFIRMED FIXED**
Source field now reads: "*Conferences* XI.2 — the **first Conference of the second part** of the Conferences (…XI.1 is the first *chapter*, 'Description of the town of Thennesus,' and XI is the first Conference)". Verified: "The Second Part of the Conferences of John Cassian. **XI. The First Conference of Abbot Chæremon. On Perfection. Chapter I. Description of the town of Thennesus.**" Exactly right. ✓

### L8 — gallicstory010 Story-Title — **CONFIRMED LEFT AS DRAFTED, reason stated and accurate**
The title still reads: `Pæsius and John — "Never has the sun seen me eating"; "nor me angry"`. The Document Log (line 243) records the decision and the reason (a title is a compressed retrieval label, not quoted text under the fidelity rule; Round 1 itself ranked it lowest and noted the Story Text is correct). The Story Text (line 56) does carry "said he" intact, matching div `iv.iii.v.xxvii` exactly. The disposition is honestly recorded. ✓

---

## Contestable judgment — *Dial.* II.12 (Section 6 item 3 / Section 8 item 2) — **RECORDED AT BOTH LOCI; representation incomplete**

**Propagation: passes.** The "recorded as a disagreement" language appears at both required places:
- Section 6 item 3, line 145: "**Recorded as a disagreement, not a settled ruling (Round 1 review):** the reviewer pressed the opposite case… the disagreement is carried forward rather than resolved by this document's own say-so, per `cic-build-cycle`'s rule that two reviews disagreeing gets logged, not quietly decided."
- Section 8 item 2, line 181: "**Recorded as a disagreement, not a settled ruling (Round 1 review; see Section 6 item 3):** … the reviewer's counter-case, that the choice leaves the Representative unable to retrieve *any* woman-centred narrative at all, is carried forward as unresolved rather than decided here."

**RESIDUAL 10 — the record omits the two load-bearing halves of the reviewer's argument.** Round 1's case had four parts. Two are carried (no retrievable woman-centred story; the material sits where retrieval cannot reach it). Two are not carried at either locus:

1. **The internal-inconsistency argument** — that this ruling is "in tension with how the document handles **every other Article-20-limited case** (it builds the story and carries the limit in the apparatus, e.g. Brictio, the objecting bishops at 004)." This is the strongest form of the objection, because it turns on the document's own practice rather than on a value judgment, and it is absent from both loci.
2. **The concrete proposed remedy** — "a Tier 3 chunk with **Gallus's rule-making named in Usage Guidance**." Section 6 item 3 gestures at "framed openly as what it is" but does not record the specific construction the reviewer proposed, which is what a future pass would need to weigh.

A recorded disagreement that drops the reviewer's evidence and remedy is a weaker artifact than the one `cic-build-cycle` asks for. One or two sentences at each locus closes it.

---

## Cross-cutting check 1 — Propagation

| Finding | Loci required | Result |
|---|---|---|
| H1 | Section 2 + 001, 003, 008, 010, 012, 014 | Named loci ✓; **Section 7(a) missed** (Residual 1) |
| H2 | 003, 004, 006, 007 + Section 4 rows | Story Texts ✓, Section 4 ✓; **007 Node note + Tier Justification missed; 006 Retrieve-When missed** (Residuals 3, 4) |
| M9 | one map | **Six of nine rows still incomplete** (M9 above) |
| M10 | rows 2, 7, 10 + closing summary | Rows ✓; **closing summary still says "two"** |
| M11 | Section 5 row 9 | 013 row ✓; **012 row missed** (Residual 6) |
| L2 | gallicstory005 | Node note + Story Text ✓; **8 further instances** (Residual 9) |
| L4 | Section 5 + Section 6 item 13 + chunk 014 | All three ✓ |
| Contestable judgment | Section 6 item 3 + Section 8 item 2 | **Both present ✓** (content incomplete — Residual 10) |

---

## Cross-cutting check 2 — New defects introduced by the fix round

**RESIDUAL 11 (systemic) — build-thread review annotations are now inside deployment-facing Story Text, while all fourteen chunks certify that none are.**

Every chunk's Final Assembly Instruction still asserts: "**No brackets or builder notes remain.**" That is now false in twelve of fourteen chunks, and specifically false *inside Story Text* in eight:

| Chunk | "(corrected, Round 1 review …)" notes in **Story Text** | in Formation Ecology Connection |
|---|---|---|
| 003 | 1 | 0 |
| 004 | 2 | 0 |
| 005 | 1 | 0 |
| 006 | 1 | 0 |
| 007 | 1 | 0 |
| 010 | 1 | 1 |
| 011 | 2 | 0 |
| 013 | 1 | 1 |

Story Text is the retrievable, participant-facing narrative written under Constitution Article 23 "from inside the world's own consciousness," in this world's close-third-person convention. A parenthesis reading "corrected, Round 1 review finding H2 — the prior draft named 'Ligugé'; … 'Ligugé' occurs in this world's vendored volume only in Gibson's editorial prolegomena to Cassian" (gallicstory004, mid-Story-Text) is build-thread apparatus inside the deployed artifact. gallicstory004's opening sentence is now 61% correction note by character count.

This is not a reason to hide the corrections — the disclosure discipline is right. It is a reason to move them: the Node note, the Source field, or a per-chunk correction line beneath the front-matter all carry them without contaminating the register. If they stay where they are, the fourteen "No brackets or builder notes remain" certifications must be amended, since a standing false self-certification is exactly the class of defect this build's reviews keep finding.

Other new defects, listed above at their findings: the self-contradictory M13 note and the reinstated "second corroborating work" certification in gallicstory005 (Residual 8); the wrong Sarabaite chapter and the unverified "reprehensible third kind" quotation (L3); the false "the absent reader is new here" (Residual 7).

---

## Cross-cutting check 3 — Word-count / structural claims

**Closing summary (line 252) — accurate.** Recomputed against the chunks:

- "seven Tier 1" — 002, 004, 005, 006, 007, 012, 013 = **7** ✓
- "four Tier 2" — 008, 009, 010, 011 = **4** ✓
- "three Tier 3" — 001, 003, 014 = **3** ✓
- "zero Tier 4" ✓; total 14 ✓
- "Tours seven, Marseilles six, Lérins one, cross-node none" ✓ (matches §3.2; "across two nodes" is consistent with the world's Tours / Lérins–Marseilles two-node structure held since Doc_01 §6)
- "Thirteen further candidates named" — Section 6 items 1–13 = **13** ✓ (Salvian correctly recorded as yielding none, not counted)
- "Six Absent Stories" — Section 8 items 1–6 = **6** ✓
- "Two construction rulings" — Section 7(a), (b) = **2** ✓

**Document Log disposition (line 248) — count-accurate, substance-inaccurate.** "all four High, nine Medium, and seven of eight Low findings fixed" matches Round 1's tally (H1–H4 = 4; M5–M13 = 9; L1–L8 = 8). But on this check's evidence the substantive claim does not hold: H1, H2, H4, M9, M11, M12 and L2 all have surviving residue at loci the log lists as "fixed", and L3's single change is an error. The line "**every fix was independently re-verified against source before being applied**" (repeated at lines 14, 214 and 222) is falsified at minimum by L3, where the source contradicts the change made, and by Residual 7, where Doc_05 contradicts the new claim.

---

## What to fix, numbered

1. **Section 7(a), line 169** — replace the fabricated `"individual attribution may be uncertain"` with CF V7.4's actual Tier 2 wording (`"academic consensus treats the tradition as authentic even where individual attribution or detail cannot be verified"`), as gallicstory012's Tier Justification already does. *(H1)*
2. **Header lines 6, 10, 37; Section 10 line 208; Document Log lines 220, 223** — change "Part V" to **Part II — Evidence Development** for the four-tier classification and the Story Inventory Requirement. Part V is Encounter Development. *(H1 / new)*
3. **gallicstory007 lines 51 and 79** — remove "at Tours" from the Node note ("at Condate and then at Tours") and from the Tier Justification ("buried at Tours"); `Ep.` III names no city. *(H2)*
4. **gallicstory006 line 36** — remove "Marmoutier" from Retrieve-When; the same chunk's Node note declares it editorial. *(H2)*
5. **Section 10, line 212(a)** — stop directing the next reviewer to "the div ids **and line ranges** given"; cite div ids only, per the line-13 disclosure. *(H4)*
6. **Section 9 item 6, line 200** — rebuild the gravity map against the table in this report (G1 gains 002, 003, 005, 006; G5 gains 003, 013; G6 gains 001, 002, 007, 014; G7 gains 008; G8 gains 001; G9 gains 006), or restate the map explicitly as a *principal-instance* list and drop the claim that it is "checked directly against each chunk's own Formation Ecology Connection." *(M9)*
7. **Section 5, line 128** — give row 9's confidence for gallicstory012 as "A (dedication) / B (editorial Lérins/abbot identification) / C (content, except *Conf.* XIII)", matching the Registry and the gallicstory013 row. *(M11)*
8. **Section 9 item 1, line 195** — strike or qualify "the absent reader is new here"; Doc_05 §3 (line 216) already quotes the reader who "failed to appear" and the bystander "laying hold of the Psalter." *(M12)*
9. **Section 6 item 7, line 151** — **restore *Conf.* XVIII.7** as the Sarabaite locus and delete the editorial gloss; XVIII.VII is "Of the origin of the Sarabaites and their mode of life", XVIII.VI is the anchorites', XVIII.IV is the three-kinds overview. Also replace the unverified `"the reprehensible third kind"` with the text's own "the reprehensible one of the Sarabaites" (XVIII.4) or drop the quotation marks. Record that Round 1's L3(a) was itself wrong. *(L3)*
10. **Section 6 item 9, line 155** — restore or ellipse "or rather" in "such as may aid my memory, or rather, provide against my forgetfulness", and drop the interpolated "to". *(L3, unaddressed)*
11. **Section 4, gallicstory014 row, line 105** — reattach "as we have seen" to the serpents never being a danger, not to their yielding, matching the chunk's own Story Text. *(L3, unaddressed)*
12. **"Trier" → "Treves"** in the eight remaining places: main doc lines 59, 98, 195; gallicstory005 lines 4, 16, 47, 98; gallicstory007 lines 57, 79. Decide separately whether the chunk filename and Story-Title are retrieval labels exempt under the L8 reasoning — and say so if they are. *(L2)*
13. **gallicstory005 line 66** — rewrite the self-contradictory M13 correction note (it disclaims the wording the corrected sentence uses); **line 106** — remove "the second **corroborating** work" from the Final Assembly Instruction. *(M13)*
14. **All fourteen chunks** — either move the "(corrected, Round 1 review finding …)" annotations out of Story Text and Formation Ecology Connection into the Node note / Source field / a per-chunk correction line, **or** amend the fourteen "No brackets or builder notes remain" certifications. The eight Story Text instances (003, 004, 005, 006, 007, 010, 011, 013) are the priority. *(new defect)*
15. **Section 6 item 3 and Section 8 item 2** — add the two omitted halves of the reviewer's case: the internal-inconsistency argument (every other Article-20-limited case is built as a story with the limit in the apparatus — Brictio, the objecting bishops at 004) and the proposed remedy (a Tier 3 chunk with Gallus's rule-making named in Usage Guidance). *(contestable judgment)*
16. **Section 5, line 134** — "two (rows 2, 10)" should be three (rows 2, 7, 10), matching the Document Log's own description of the M10 fix. *(M10, minor)*
17. **Document Log line 248 and the Status/Disposition lines (14, 214, 222)** — the claim that every fix was independently re-verified against source before being applied does not survive items 8 and 9 above and should be amended rather than repeated.

Items 1, 2, 3, 9 and 14 are the ones that falsify a claim the document makes about itself, and are the substantive gate. Items 5, 6, 7, 8, 10–13, 16 are one-line corrections. Item 15 is two sentences at each of two loci.

---

## What holds

H3 is fully closed at both required levels in both chunks — the consequential finding of Round 1, and the fix is exactly right. M5, M6, M7, M8, L1, L4, L5, L6, L7 are clean, and I re-verified each against the vendored text at its own locus rather than accepting the fix note. M10 and M11 are substantively right where they were applied. H4's disclosure paragraph is honest and does establish div ids as authoritative — and the div ids themselves are correct, spot-checked at eight loci. Section 4's audit rows were genuinely updated for all four H2 chunks. L8's non-fix is honestly reasoned and correctly recorded. The disagreement language reached both of its loci. All structural counts in the closing summary are accurate. No new fabricated quotation was introduced into any Story Text; the two new unverified quotations found ("the reprehensible third kind"; the "individual attribution may be uncertain" survivor) are both in the main document's apparatus, not in narrative.

**Disposition: Residual issues found. Not clear to proceed until items 1–3, 9 and 14 are closed; items 4–8 and 10–17 should go in the same pass.**
