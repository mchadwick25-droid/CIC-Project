# Step 0 Review, Round 3 — The Society of Jesus

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Targeted recheck against Round 2's findings, plus re-verification of every sourcing claim the resync touched. This is the final round under the project's three-round cap.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md`, Revision 3.
**Checked against:** Round 2 findings S1, S2, M1–M3, m1–m4; the live `cic/corpus-map/the-society-of-jesus.yaml` and `the-tridentine-church.yaml`; `worlds/_cross-world/LIBRARY-DECISION-LOG.md` point 5; `cic/texts/REGISTRY.yaml`; `cic-website/data/world-census.json`; and the vendored files in `cic/texts/`, including the title pages of all nine works added 2026-09-25.

## Verdict

**ESCALATE. Round 3 of 3; no fourth revision round.** Revision 3 carried out all five of Round 2's required resync tasks correctly (see Confirmed accurate). But one new substantial finding remains, S1 below. The document's coverage window for the order's institutional voice after 1556 is wrong. It rests on two vendored volumes that do not cover the years the document says they do. One of them is mislabelled in the corpus-map itself.

The fault is mostly upstream of the document's own drafting. Round 2 of this review supplied the "Lainez (General 1558–65) ... thin after c. 1580" re-dating without checking the volumes' own title pages. The corpus-map's Polanco row names the wrong volume. Revision 3 followed both faithfully. Even so, the claim as it stands is actually wrong, not merely improvable. Correcting it changes a sourcing conclusion, which is the skill's own test for a substantial revision. Under the cap, that goes to Mark, not to a fourth round.

## Findings

### Substantial

**S1. The post-1556 institutional coverage window rests on misdescribed volumes (B1, B2, B5, Tier, §4 item 5).** The document says the vendored institutional voice extends "past Ignatius's 1556 death into Lainez's generalate" (B2). It says it reaches "the 1560s–80s, via Lainez, Salmeron, Nadal, and Polanco" (B5, §4 item 5). It calls the sourcing "strong ... for the order's own early institutional administration (to roughly 1580)" (Tier). B1 and B2 describe the Lainez volume as his "letters and acts as second Superior General (1558–65)". The volumes' own title pages say otherwise:

| Vendored file | Document / corpus-map says | Title page actually reads | Reaches past 1556? |
|---|---|---|---|
| `lainez_epistolae-et-acta-v1-lat_1912.txt` | letters and acts as second General (1558–65) | "TOMUS PRIMUS / 1536-1556" (l. 76–78) | No. It ends before his generalate. |
| `polanco_chronicon-v1-lat_1894.txt` | *Chronicon*, Vol. I, 1894 | "TOMUS QUINTUS / (1555)", Madrid 1897 (l. 97–106); body opens "ANNUS 1555" (l. 135) | No. It covers the single year 1555. |
| `nadal_epistolae-v1-lat_1898.txt` | Nadal's letters (no range given) | "TOMUS PRIMUS / (1546-1562)" | Yes, to 1562. |
| `salmeron_epistolae-v2-lat_1906.txt` / `-v3-` | *Epistolae*, Vols. II and III | "TOMUS PRIMUS / 1536-1565" and "TOMUS SECUNDUS / 1565-1585" | Yes, to 1585. |

The corrected picture is as follows. The institutional voice is dense to 1556, carried by Ignatius, Lainez Tomus I, Polanco's 1555 volume, and the letters. It runs on to 1562 through Nadal's letters, and it has Nadal's *Scholia*. From 1562 to 1585 it rests on one correspondent alone, Salmeron. Salmeron wrote as a provincial in Naples, not from the order's central government. Nothing vendored gives Lainez's own voice as General (1558–65), nor Borgia's (1565–72) or Mercurian's (1573–80).

So "strong ... to roughly 1580" overstates the holdings. A fair statement would be "strong to 1556, partial to the early 1560s, and a single correspondent's thread to 1585." This does not change the Tier or the direction of §4 item 5: missionary and global reach is still thin after 1552, and the Jesuit Relations still need assessing. But it does change a sourcing conclusion that is binding on Doc_02. Left as it is, Doc_02 would go looking for Lainez's generalate and the Polanco *Chronicon*'s early years in files that do not contain them.

### Minor

- **m1. Some revision narration is still in the body.** Examples: "up from the ten this document previously counted" (B1, l. 55); "than previously counted here — 19 works, not ten" (Section B conclusion, l. 79); "than previously recognized" (Tier, l. 81). These are cosmetic, but they are the same class of narration Round 2's M3 asked to be stripped. None of the Revision 1 / Revision 2 / "corrected" / finding-number forms Round 2 listed survives. The Status line and §6 name "Revision 3" only as status metadata, which is acceptable.
- **m2. Volume labels are inherited from the corpus-map without the actual tomus.** "*Epistolae et Instructiones*, Vol. 22" is MHSI series number 22, which is Tomus I of Ignatius's letters (l. 56: "TOMUS PRIMUS"). Read beside "the full 12-volume ... edition", "Vol. 22" looks like an error. "Salmeron ... Vols. II and III" are in fact Tomus I and Tomus II: the complete two-volume MHSI Salmeron letters, not a partial set. These labels are fixable alongside S1.
- **m3. The Tier headline promises "one real remaining condition" but then sets out three.** They are the second-witness status of the Constitutions and *Adnotationes*, the English-translation gap, and the post-1556 scale gap. This is a wording issue.
- **m4 (carried from Round 2 m3, not addressed).** §0 still does not mention the census's existing `statusWord` "Researched — strong candidate" and its Tier 1 `statusDescription`. This does not affect the outcome.

### Flag to the Library thread's owner (outside this document; not touched here)

- **L1. The Polanco row is mislabelled in three places:** the corpus-map (`the-society-of-jesus.yaml`: "Vol. I"), REGISTRY.yaml, and the file header ("Vol. I of a 6-vol. series ... 1894"). The file is Tomus V (1555), printed 1897. This is a real Library defect, and it is the root cause of part of S1.
- **L2. The Salmeron corpus-map titles and file headers say "Vol. II" and "Vol. III",** and the Vol. II header says "A vol. 'I' was not found digitized this pass". The files are Tomus I and Tomus II, which is the complete edition. The "II/III" numbering comes from the Google scan item IDs (`...02salmgoog`, `...03salmgoog`), not from the edition.
- **L3 (carried from Round 2 m4).** All nine 2026-09-25 file headers still say "Per this project's own INTAKE.md rule, this ... text is a second witness, never primary evidence". That contradicts the corpus-map notes and LIBRARY-DECISION-LOG point 5 for the clean-scan files. The Constitutions and Nadal *Adnotationes* corpus-map notes still carry "Correction (2026-09-25): this note previously called..." narration inside a canonical surface.

## Confirmed accurate

All five of the checks the brief asked for pass.

- **Sourcing count.** The corpus-map lists exactly 19 works, and all 19 `source_file`s exist in `cic/texts/`. I recomputed the word counts myself: 3,370,675 across all 19, and 1,385,753 across the original ten. Both match B1 exactly. The role and confidence labels B1 gives match the corpus-map. That holds for Boero (context, provisional), the *Memoriale* (tradition, assigned, clean scan), Polanco and Ribadeneira (context), and Ribadeneira's OCR flag.
- **Constitutions and *Adnotationes* are second witness.** B1, the Tier and §4 item 1 all now describe them as second witness, not PRIMARY, under the scan-quality ruling. LIBRARY-DECISION-LOG point 5 exists as cited ("Scan quality, not language, now decides quotability ... Mark's OCR ruling 'a' (2026-09-25)"). Its flagged-file list names both files. Both corpus-map notes say "stays second witness ... not yet quotable verbatim." The Ganss copyright caveat is kept correctly as a separate, language-only gap.
- **The Trent split is stated as settled fact.** `the-society-of-jesus.yaml` gives the Waterworth canons/decrees as `role: context`, `confidence: assigned`. `the-tridentine-church.yaml` gives them as `role: tradition`, `confidence: assigned`, with the note "Native/foundational here". B3, the Section B conclusion and §4 item 3 all state this as settled and disclosure-only. The dangling "described elsewhere" reference is gone.
- **B2 attribution is fixed.** It now credits Coleridge's own narration and a Coleridge footnote citing Alcazar, not Xavier's letters. Both passages are verbatim in `francis-xavier_life-and-letters-v1_coleridge1872.txt`:
  - l. 3507–3509: "spiritual reading in the Bible and the Imitation of Christ"
  - l. 4531–4536: footnote 6, "We are told by Alcazar (Chrono-Historia ...) ... he gave each monk at Monte Cassino a copy of the book de Contemptu Mundi, i. e. the Imitation of Christ"
- **Round 2 M1 is fixed.** A4 and §0 now present both rationales, the Catholic-renewal voice and the Evagrian echo, as this thread's own reading. Neither is attributed to Mark any longer.
- **Round 2 m1 and m2 are fixed.** The corpus-map quote, "since this is not the Society's own composed voice", is now verbatim. The two census fields are quoted separately, and both are verbatim against `world-census.json`: `sourcing` "founder-corpus gravity needs standard discipline"; `statusDescription` "a discipline for any account of it to apply, not a straightforward strength to claim".
- **Round 2 M3(b) is fixed.** `Step0_Review_Round1.md` is now present on this branch.
- **Earlier anchors re-checked and unchanged.** I spot-checked these again:
  - Trent Session III, "the Symbol of faith which the holy Roman Church makes use of" (l. 12339–12340)
  - the single Chalcedon occurrence in the decrees (l. 19846, disciplinary)
  - the Autobiography's Manresa Trinity passage (l. 825ff.)
  - the Exercises' Incarnation contemplation (Mullan l. 2225ff.)

  All read as the document states.

## Disposition

**ESCALATE to the project lead, per the three-round cap.** This is not a request for a fourth open-ended round. The rest of the document holds, including Section A, Tier 1, and §4 items 1–4 and 6. It is otherwise ready for "Approved to proceed".

The unresolved item is S1. It is a bounded correction: re-date the post-1556 coverage in B1, B2, B5, the Tier and §4 item 5 to match the table above, and carry the m1–m3 cleanup in the same pass. Recommended options for Mark:

1. **(Recommended) Authorise a single bounded correction under his direction.** Apply S1 and m1–m3 only, followed by a spot-check limited to those lines rather than a full review round. In parallel, the Library thread corrects L1 and L2 at source, so the document and the corpus-map agree.
2. **Approve to proceed as is.** S1 would be registered as an open gap binding on Doc_02, recording that institutional coverage after 1556 is thinner than the document states. Doc_02 would re-establish coverage from the title pages itself.
3. **Hold the world** until the Library thread fixes L1 and L2, then take option 1.

Two points for the audit trail. First, part of S1 comes from Round 2 of this review, which supplied the unverified "Lainez (General 1558–65) ... c. 1580" re-dating. That is logged here as a disagreement between rounds, per the skill's rule, not silently overwritten. Second, whichever option Mark chooses, S1 and L1–L3 belong in this world's gap tracking so they do not go quiet.
