# Step 0 Review, Round 1 — Devotio Moderna / Brethren of the Common Life

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline.
**Document reviewed:** `Step0_Movement_Scope_Confirmation.md` (Revision 1, drafted 2026-09-25).

## Verdict

**Substantial revision needed.** Two conclusions probably survive revision — the floor clears, and Tier 1 — but the grounding behind both is what Step 0 exists to supply, and several findings change a process-standing claim, a sourcing conclusion, or a scope boundary. Some errors are directly contradicted by the vendored files the document says it "read," suggesting the reading claims are overstated.

## Findings

### Substantial

**S1. §0/§5's "no prior Step 0 record of any kind" is false.** The census entry carries `statusWord: "Researched — strong candidate"` and `statusDescription: "Tiered Strong (Tier 1) on a rich base — customaries, the brothers' and sisters' lives, rapiaria and the Imitation."` Per `git log`, the statusWord read "...(Era 6 Step 0)" before commit 06c1b75c (2026-09-25 07:04) dropped the tag. This is the same situation Lollardy's own Step 0 correctly carries forward; this document instead re-derives Tier 1 as if fresh, never acknowledging an earlier tier existed or that it rested on a different, currently-unvendored source base (see S11). **The Hussite Step 0 makes the identical error** — its census entry is likewise "Researched — strong candidate / Tiered Strong (Tier 1)."

**S2. A3 contains a date error inside its load-bearing argument.** A3 says Kempis "died in 1471 — nearly a century after Groote, well past this world's own 1517 close." 1471 is 46 years *before* 1517, not past it. The same sentence claims Kempis "was born the year Groote founded the movement," treating 1380 (the census window's own start year) as a founding date with no support — the census's own documented story dates the first house to Groote's 1374 deed, and its `longDescription` says "after his death in 1384 his followers organized." §6 then calls "Kempis's 1380–1471 dates" "uncontested historical fact" — the birth year is only approximate ("c. 1380" per the vendored header and Benham's own preface).

**S3. B1's "fourteen surviving letters" misstates what the source says.** Acquoy's own introduction in the vendored file (c. line 891) describes the Hague codex as containing 66 letters, 64 attributable to Groote — Acquoy edited 14 of them. "Epistolae XIV" is the scope of this edition, not the number of letters that survive (outside knowledge: Mulder's 1933 edition prints ~76). The vendored file itself, with its 14 EPISTOLA headings, is complete as vendored — the error is in how the document characterizes total survival.

**S4. The claim that Groote's own voice exists only in Latin is wrong — the vendored Founders volume already contains his own writing in PD English.** B1 and the Section B conclusion frame the missing English Groote translation as the one real gap. But `kempis_founders-of-the-new-devotion_arthur1905.txt` contains: Ch. XVIII's *Publica protestatio* in the first person (c. line 4147); the "Resolutions and Intentions... not confirmed by vows" (c. line 4223) — the census's own named self-rule text; excerpted letters (c. line 2745); an appendix letter to the Bishop of Utrecht (c. line 5097). Acquoy's own introduction (c. line 690) confirms the Protestatio and related texts were printed in Kempis's own Vita. This improves the actual sourcing picture but means B1/Section B/§4 item 2 mischaracterize it, and suggests Founders wasn't read closely enough to catch this.

**S5. Filing Groote's Latin letters as "PRIMARY... not a second witness" conflicts with this project's own governing rule — a methodology question, not a revision-only fix.** `cic/texts/INTAKE.md` (line 24, c. line 161) states original-language files are "second witnesses — never primary evidence for a Representative," citable where no English rendering exists but still carrying that label; LPC's own Doc_02/08/09 consistently apply "second witness, second limb" to Latin-only material. The "PRIMARY" framing for the Jesuit Constitutions/Nadal precedent this document leans on exists only in REGISTRY notes and the Jesuit dossier — no actual ruling was found behind it, and the Groote REGISTRY row itself doesn't say PRIMARY (only the corpus-map note does). **This is presenting a departure from a written project rule as settled practice. Per CLAUDE.md, a governance/methodology decision always goes to Mark — this needs his call, not a self-resolved revision.**

**S6. A1/B4/B5's "never challenged church authority at all" is contradicted by the vendored sources and the census.** Founders (c. line 2754): "many prelates of the Church were opposed to him... he was forbidden to preach by an edict"; Ch. XVIII is a defensive profession of faith against accusations of unorthodoxy; the appendix letter pleads for a suspended preaching license to be restored. Census: "forbidden to preach the year before for attacking the clergy's concubines." (Outside knowledge: the vowless communal life was formally attacked at Constance in 1418.) The movement submitted to authority rather than breaking from it, but its relationship to that authority was genuinely contested — and deriving the floor clearance from "never challenged authority" is a non sequitur regardless, since Article 4 concerns Trinitarian/Christological commitments, not ecclesiastical authority.

**S11. The gap disclosure is incomplete and internally inconsistent, weakening the Tier 1 grounding.** The Section B conclusion claims "only one real disclosed gap" while B2 names a second (institutional decline) in the same document. More significantly: the census's own sourcing/voices name unvendored material the earlier Tier 1 (S1) evidently rested on — customaries, the Sisters' lives (Deventer/Diepenveen), rapiaria, Zerbolt's *Spiritual Ascents*, Van Engen's in-copyright *Basic Writings* — and the women's side of the movement (the census's own named voice) has zero vendored representation, including the Salome Sticken story. The document never reconciles its own three-work base against this wider named record. (Unverified lead: J. P. Arthur also translated Zerbolt's *Spiritual Ascent*, 1908, and Kempis's *Chronicle of Mount St Agnes*, 1906.)

### Moderate (real, not independently substantial)

- **S7.** B5's "never a dispersed geography" is contradicted by Founders (c. line 3793): communities spread to "Westphalia and Saxony," outside the Low Countries — and the document's own §1 places Luther's Brethren-linked household at Magdeburg, Saxony.
- **S8.** The Imitation's Kempis authorship is treated as settled and "read this pass," but the vendored Benham preface itself (c. lines 490–640) calls Kempis's authorship "the erroneous notion that he was its author" and argues for a 13th-c. "Abbot John Gersen" instead. Kempis authorship is the mainstream modern view but needs a `formation_confidence` tag and disclosure that the vendored edition's own front matter disputes it.
- **S9.** "Documented both-directions influence" overstates the Luther/Erasmus direction, which is contested in scholarship (Post 1968 rebutted Hyma's thesis; the census's own wording is more careful — "a household connected with the Brethren"). The Jesuit direction has a real vendored anchor the document missed (Xavier's Letters Vol. 1, early companions reading the Imitation, Ignatius distributing *De Contemptu Mundi*).
- **S10.** B3 calls Lutheran Wittenberg "already-source-ready" when the census lists it as "Built & Live" (`Build/worlds/witt`); B3 also silently swaps the dossier's own comparison target (Anabaptist Movements) for Wittenberg without disclosing the substitution, though the underlying claim (neither witt's nor the Jesuits' corpus-map cross-references this world) checks out.
- **S12.** A1's floor check is asserted, not assessed against any specific passage (directly relevant text — Groote's Protestatio, Imitation Book IV — went uncited), and its "read this pass" claim conflicts with the vendored file headers' own "not independently spot-checked beyond the opening pages and a mid-document sample."
- **S13.** §0's selection-history account conflicts with the Hussite Step 0's own account of the same event (both cannot be accurate as written) — worth a decision-log entry per CLAUDE.md's "Track gaps" rule rather than left as an unreconciled discrepancy between two documents.

### Minor

- Article 4 quotations verbatim-checked against the Constitution, no finding.
- Boilerplate XML caveat inapplicable (files are .txt).
- Em-dash vs. hyphen inconsistency in a quoted census field.
- **Canonical-file error outside this document:** the vendored Benham file's own header and REGISTRY.yaml both give the publisher as "London: Cassell & Company, 1886"; the actual vendored title page reads "London: John C. Nimmo... 1886." Worth its own fix in `cic/texts/`.

### Confirmed accurate

Groote's 1384 death, Kempis's 1471 death, rights bases, archive.org IDs, file sizes, all four Imitation books present, Founders containing the Lives of Groote/Radewijns/followers, both sibling corpus-maps lacking a cross-reference, the Tridentine Pole/Borromeo comparison, and the Hussite/Lollardy corpus characterizations.

## Disposition

Per `cic-build-cycle`: S1–S6 and S11 are errors, not thoroughness points — meets the project's own bar for substantial revision. **S5 should go to Mark directly rather than be resolved in revision** — it's a governance/methodology question (whether Latin-original material can be filed as primary rather than second-witness), not something this document's own revision can self-settle. This is Round 1 of the three-round cap.

**Noted in passing:** the Hussite Step 0's own "no prior gate" claim (its own §0/F1, this review's own S1) shares the identical census-record problem found here.
