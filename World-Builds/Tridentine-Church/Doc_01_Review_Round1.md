# Doc_01 Review — Round 1: The Tridentine Church

**Document reviewed:** `World-Builds/Tridentine-Church/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT, as committed in 138919e3e)
**Checked against:** `Step0_Movement_Scope_Confirmation.md` (Revision 3, current on disk); `worlds/_cross-world/dossiers/the-tridentine-church_Source_Readiness_Dossier.md`; `cic/corpus-map/the-tridentine-church.yaml`; vendored files `council-of-trent_canons-and-decrees_waterworth1848.txt` and `barlow_brutum-fulmen_1681.txt` in `cic/texts/`; `worlds/ijc/Doc_01_World_Identification_Boundaries_Orientation.md` (the strand precedent Doc_01 invokes); Constitution on disk (`reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx`).
**Reviewer role:** independent adversarial review, Round 1, per `cic-build-cycle`. Every quotation below was re-checked by direct grep and line-level reading of the vendored file. None was taken on the document's own "verified" claim.
**Date:** 2026-09-25

---

## Verdict

**SUBSTANTIAL REVISION REQUIRED.**

There are 13 findings: 2 High, 5 Medium, 6 Low. Six are substantial: H1, H2, M1, M2, M3 and M4.

- **H1** is the recurring defect this project names explicitly: a quotation attributed to the wrong text and wrongly tagged Documented.
- **H2** is the stale Step 0 status. Doc_01 still repeats it and builds an escalation claim and a next-step gate on it. Neither exists any more.
- The rest of the document is sound. The Step 0 corrected framing is respected, the Bellarmine attribution is clean, and three of the four canon quotations are exact.

---

## Findings by severity

### HIGH

**H1. The Session XXI "item 8" quotation is misattributed. It is not Trent's text and it is not from Session XXI. (Substantial)**

§5 says Session XXI "lists, among the condemned reformist positions catalogued in its preparatory articles, item 8 (verified verbatim, lines 6179–6182)". The line numbers do hold that wording. But those lines are:

- in Waterworth's own 19th-century historical introduction (roman-numeral pagination, page cxxxv), not in the conciliar text;
- under his **Session XIII** narrative (heading c. line 6123). They sit among the "ten articles, extracted from the conflicting writings of the Protestants, on the holy Eucharist", which were handed to the Fathers on 2 September **1551** (c. lines 6136–6141). They are not from Session XXI (16 July 1562);
- the editor's report of a list of Protestant propositions given to the theologians. They are not a canon or decree of the Council.

The heading that Doc_01 says is "titled in the vendored text" ("On Communion in one kind, and the Communion of little children") does not appear anywhere in the file. The real heading, c. line 18003, is "ON COMMUNION UNDER BOTH SPECIES, AND ON THE COMMUNION OF INFANTS."

§5 then closes with "Documented for all four, as the canons' own verbatim text". For this item, that claim is false.

**Required fix:** replace the quotation with Session XXI's own **Canon I** (c. lines 18006–18009): "If anyone saith that, by the precept of God, or by necessity of salvation, all and each of the faithful of Christ ought to receive both species of the most holy sacrament of the Eucharist; let him be anathema."

The existing sentence about the Church's power to withhold the chalice is accurate. Support it with **Chapter II**, "The power of the Church as regards the dispensation of the Sacrament of the Eucharist" (c. lines 17928–17938). If the 1551 article list is kept at all, label it as Waterworth's historical narrative of the Session XIII preparations (role: context, editor's frame). Do not present it as Session XXI's text.

**H2. Doc_01 repeats the stale Step 0 status and builds on it. (Substantial: it changes Doc_01's sourcing-dependency claim and its escalation assessment)**

The Step 0 document on disk now correctly reads "Approved to proceed" in two places:

- its header, line 3: "Independently reviewed at Revision 3 … Approved to proceed.";
- its §6 Disposition, line 107: "Independently reviewed and cleared - Approved to proceed."

The fix landed in commit 6ab982613, before Doc_01's own commit 138919e3e. Doc_01 still says the opposite in four places:

- The header note (line 10) says Doc_01 "does **not** treat Step 0 as formally Approved to proceed".
- §7 item 10 carries the discrepancy as an open item.
- §8's Escalation-category assessment names Step 0's status as "one named, unresolved tension". It routes that tension toward the project lead under the "unresolved tensions the pipeline can't close" category.
- §8 Next step makes Doc_02 conditional on "the Step 0 status question (§7 item 10)" being resolved.

**Required fix:**

- Remove the header note and §7 item 10.
- State in the header that Doc_01 builds on Step 0 Revision 3, Approved to proceed (see `Step0_Review_Round3.md`), which it does not reopen. This is the same form IJC's Doc_01 uses.
- Delete the escalation claim.
- Remove the gate on the next step.

A note for the Step 0 thread only, which Doc_01 should not act on: both Step 0 status lines still also say "DRAFT, Revision 3" next to "Approved to proceed". This is a small residual wording oddity. Flag it; do not touch it.

### MEDIUM

**M1. The Society of Jesus distinctiveness argument asserts a clean separation that the vendored corpus itself contradicts. (Substantial: a scope-boundary claim)**

§1 and §3 describe this world as "the deliberative and legislative body" and the Jesuits as "one executing order among several … they occupy different positions relative to its authorship." The Waterworth file this world treats as its own tradition voice records Jesuits inside the deliberation:

- Lainez, "of the Society of Jesus", in the first period (c. line 4902);
- Salmeron opening debates in the second and third periods (c. lines 8625–8633, 9168–9201, 10383);
- Diego Lainez, "the general of the Jesuits", casting a **vote** on the episcopal-jurisdiction question. The narrative says his "vote and reasoning … appear to have produced the greatest impression on the congregation, one entire sitting of which was occupied in hearing him" (c. lines 8672–8675, 9382–9385). Lainez also persuades the Italian prelates (c. line 9490).

The corpus-map role split is still valid. The Canons and Decrees are the Council's corporate composed voice, which is not the Society's own voice. What does not hold is "authorship vs. execution" stated as the historical distinction.

**Required fix:** name the overlap openly. Jesuit theologians and the Jesuit General took part in drafting and voting. Then restate the distinction in terms of the unit of world:

- this world is the whole-church, conciliar and institutional ecology;
- the Society of Jesus is one order's own formation logic (the Exercises, the Constitutions, the colleges), which both helped shape Trent and carried it out.

Borromeo's "executor" framing deserves the same care. His role in Rome during the third period, as Pius IV's cardinal-nephew, is Widely Accepted in the secondary literature, though this reviewer did not check it in the vendored text.

**M2. The Strand Determination has a real reasoning gap. It avoided the plurality trap, but its evidence base is too narrow. (Substantial)**

What it does well: the section honestly refuses to count the Council → Catechism → Borromeo sequence as strand plurality. It also builds a genuine case for a genre and audience variation. That part is well done.

Three problems remain:

**(a) The singular case uses the mirror image of the same trap.** Its main argument is that all three bodies of material sit on "the same implementation chain", each "answerable to and derived from the Council's own settlement." That is causal derivation used to argue unity. IJC's Round 1 review (see IJC Doc_01 revision history) flagged exactly this move: folding a figure into a strand by sequential or derivational reasoning rather than testing its actual ground of authority. Derivation does not show a shared ground. The ground itself has to be examined.

**(b) The section never tests the one ground-of-authority divergence the vendored corpus documents directly.** That divergence is episcopal versus papal/curial. Waterworth's narrative of the third period records a long, organized split over two questions:

- whether episcopal residence is "of divine right" (c. lines 7584–8177);
- whether episcopal jurisdiction comes immediately from God or through the Pope (c. lines 9376–9490, 9684, 9847). Fifty-three Fathers backed the Archbishop of Granada's divine-right clause; Lainez argued the papal-derivation side.

Regnans in Excelsis, which is also this world's tradition text, opens with papal plenitude of power committed "to one alone upon Earth, namely, to Peter … and to Peter's Successor" (Barlow, c. lines 2278–2290).

That is a candidate for a distinct ground of authority in exactly the sense IJC's own three-strand finding used: episcopal office held by divine right, set against authority derived through Petrine primacy. It may resolve to strand-singular. The Council avoided defining the question, and both sides stayed in communion. But Article 21 requires the section to engage it. Genre differences are not enough.

**(c) Most of the vendored corpus is left out of the three bodies considered.** The analysis omits:

- the Missal and the Breviary (the worship register);
- Bellarmine's four devotional-ascent works (the one clearly interior and contemplative formation voice in the corpus);
- Pole;
- Pius V's letters.

If any material could show "a genuinely distinct organizing conviction" in formation logic, it is Bellarmine's contemplative material.

**Also in this section:** "Contested (within this document's own reasoning, not in the secondary literature specifically)" misuses the five-level vocabulary. Contested rates a claim that is disputed in scholarship. It does not describe the author's own open question. Present the open question as a named Doc_04 test with no confidence tag, or rate the claim properly.

**Required fix:** rebuild the "case for plurality" and the working determination so that they:

- test the episcopal/papal ground of authority directly against the vendored evidence;
- bring in the liturgical and devotional material;
- stop using derivation as the argument for singularity.

The conclusion can stay strand-singular if the evidence supports it, stated as provisional.

**M3. The claim that before 1517 the Church faced "no organized, doctrinally systematic challenge" is an overclaim with no confidence tag. (Substantial)**

§2 defends the beginning point by saying that "before 1517, the Catholic Church faced no organized, doctrinally systematic challenge of the kind Trent's own canons anathematize clause by clause." Two counterexamples undercut this:

- **The Hussite movement.** From the 1420s it ran a Utraquist church with its own organization and doctrinal program, and the Basel Compactata (1436) conceded the lay chalice. That is the very issue Session XXI later rules on. The Hussite and Bohemian Brethren movement is itself a portfolio candidate with its own dossier and Doc_01.
- **Lollardy.** It is in this same batch, and Step 0 B3 names it.

The confidence tag attached covers only "1517 as the conventional opening date". The categorical sentence is left untagged.

**Required fix:** narrow the claim to what is defensible. 1517 opens the specific Lutheran and Reformed controversy that Trent's canons answer, and that controversy reached a scale and spread that earlier dissent did not. Tag the narrowed claim accordingly. Doc_02 can then cross-reference the Hussite and Lollard precedents.

**M4. "Documented that the window's later third is currently unevidenced in the vendored corpus" is wrong. (Substantial: a confidence rating and sourcing conclusion)**

§2's ending-point paragraph and Cell 3A both call 1600–1650 unevidenced. But this world's own tradition-role files include Bellarmine's devotional works, which are mostly from 1615–1620:

- *De ascensione mentis in Deum*, 1615;
- *De aeterna felicitate sanctorum*, 1616.

Doc_01's own §2 already places them "late 16th/early 17th century". Pius V's letters are a 1640 *printing*. Step 0 §1 claims only something narrower: that the named institutional developments of the later period (Propaganda Fide, the Index, the Roman Inquisition, the new active orders) are not yet engaged.

**Required fix:** restate the gap as follows. The later third is **thinly** evidenced, by devotional material only. Its institutional developments are not engaged by any vendored source. Correct Cell 3A to match. Also narrow "late 16th/early 17th century" for Bellarmine to "early 17th century (c. 1615–1620)".

**M5. The dossier-staleness carry-forward (§7 item 8) is incomplete. (Not substantial)**

Item 8 correctly carries the stale §4 Pole and Borromeo entries. The dossier is stale in more places than that, and some of them bear directly on claims Doc_01 makes:

- **§1 table.** It still lists the Canons and Decrees as role **context**, confidence **provisional**. The corpus-map (checked directly) now reads **tradition / assigned**. Doc_01 §1 relies on the corpus-map value as a "settled cataloguing fact". The dossier therefore contradicts Doc_01's own Documented claim and should be named.
- **§1.** It lists only four assigned works. The corpus-map now carries fourteen files.
- **§5.** It recommends that this world "treat Borromeo only as a named figure … not attempt his own voice." The Library's original-language ruling has overtaken this.
- **§6.** It says "no Pole, no Borromeo in English". It also says the floor clears as "uncontroversially Nicene/Chalcedonian". That second phrase conflicts with Step 0's corrected A1 framing, which says Trent does not reaffirm either council by name.

**Required fix:** extend item 8 to name these entries, so that Doc_02 does not inherit them.

### LOW

**L1. The forces sketch is mostly Layer 1 only, with some drift.**

- Cell 3B's "a data point for Doc_04 on the limits of the authority this world's canons assert" is a Layer 3 (formation-impact and gravity) move.
- Cell 2B's "a likely contributor to why this world's own … self-presentation survives so richly" is an untagged inference.
- No cell carries a confidence tag, although the Forces template asks for one at Layer 1.
- Putting *Regnans in Excelsis* (1570, mid-window, aimed at an outside sovereign) in **Internal / Ending-Transforming** is questionable. It reads more naturally as External/Ongoing, and Cell 3A is left empty. Name the placement as provisional for Doc_08.

**Fix:** trim the Layer 3 phrasing, add confidence tags, and mark the placement as provisional.

**L2. The Regnans quotation has been normalized.** The vendored OCR reads ", Egnuans in Excelfis , cui dataeft Omnisin Calo ce? in Terra Po-teftas" (c. lines 2311–2316) and ": E that reigneth on 7 high » to whom is given all Power in Heaven & in Earth" (c. lines 2271–2276). The drop-caps are lost. Doc_01's rendering matches in substance, but it presents a normalized reading as if it were verbatim.

**Fix:** say "normalized from garbled OCR" and cite the lines.

**L3. A cross-reference in the Session XXII gloss is wrong.** The gloss says "Trent's own decrees elsewhere permit vernacular catechetical instruction … per §3 above". §3 does not establish this. The correct sources are:

- Session XXII, the chapter "On not celebrating the Mass everywhere in the vulgar tongue" (c. lines 18611–18617);
- Session XXIV reform decree ch. VII (c. lines 21069–21077).

The claim itself is accurate.

**L4. A second cross-reference is wrong.** §3 attributes Session IV to "Step 0's own floor-clearance discussion". Step 0 A1 does not mention Session IV. Step 0 §0 mentions "scripture-and-tradition" only in general terms.

**Fix:** correct the cross-reference, or cite Session IV from the vendored file directly.

**L5. "Incidental" misstates Step 0.** §2 and §7 item 7 say Step 0 flagged its narrower scope description as "incidental". Step 0 §4 item 7 does not say this. It discloses the mismatch and assigns the window decision to Doc_01. Doc_01's own decision to adopt 1517–1650 is legitimate and well argued. Present it as Doc_01's decision, not as Step 0's characterization.

**L6. Two citation-label issues.**

- "Article 3 (No Forward-Projected Specificity / no invented detail)". On the Constitution text on disk, Article 3 governs Level 1 documents presupposing the shape of future artifacts. The ban on invented detail belongs to Article 28's Anti-Fabrication Prohibition. Drop the gloss.
- A fleet-level note, not for this document to fix: the repo holds Constitution **V2_2**, while build documents cite V2.3.

---

## Confirmed accurate

- **Session VI Canon IX** (lines 13681–13686): verbatim. The gloss on "sufficient without any cooperation of the will" reads the canon accurately.
- **Session XXII Canon IX** (lines 18702–18708): verbatim. The ellipsis stands for "for that it is contrary to the institution of Christ". The "vulgar tongue *only*" reading is accurate.
- **Session XXIV Canon IX** (lines 20252–20261): the quoted portion is verbatim. The scope reading (clergy in sacred orders and Regulars under solemn vow) is accurate. The ellipsis omits two further condemned clauses, but these do not change the reading.
- **Session III preface**, "extirpating of heresies, and the reforming of manners" (c. lines 12320–12322): verbatim.
- **Step 0's corrected creed framing:** Doc_01 nowhere says Trent reaffirms the Nicene Creed or Chalcedon by name. It does not repeat the dossier's "uncontroversially Nicene/Chalcedonian". Step 0's underlying evidence was independently re-verified:
  - "the Symbol of faith which the holy Roman Church makes use of" (line 12339);
  - the Creed recited from line 12344;
  - "Chalcedon" appears once in the decrees, at Session XXIII ch. XVI (line 19846), as "the sixth canon of the Council of Chalcedon" on attaching the ordained to a church. That is a disciplinary use, not a doctrinal one. The two other occurrences, at lines 2820 and 11383, are in Waterworth's introduction.
- **Bellarmine:** only the four genuine works are cited. The *Notes of the Church* file is correctly identified as a Church of England opponent tract, role: context. This matches the corpus-map, where the row's author is `church-of-england-anon-1687`.
- **Corpus-map roles** cited in §1, §3 and §7 match `the-tridentine-church.yaml`:
  - Waterworth: tradition/assigned, double-placed as context for the Society of Jesus;
  - Barlow: split into bull texts (tradition) and commentary (context);
  - Borromeo, the Catechism and the Bellarmine works: tradition.
- **§7 item 9 (EEBO):** correctly keeps the item-specific archive.org check on the Pole file separate from the broader EEBO rights re-check. A repo search finds no record that the broader re-check has been done.
- **Dates and facts confirmed:**
  - the three periods and their popes;
  - twenty-five sessions;
  - Trent as an imperial prince-bishopric;
  - Roman Catechism 1566 under Pius V;
  - *Regnans* 1570, and that it failed to depose Elizabeth;
  - the Sarpi status (it matches Step 0 §4 item 2).
- **Living Tradition Status:** correctly left PENDING as a project-lead act. The Article 28 historical-versus-living distinction is handled with care.

---

## Disposition

**Round 1: SUBSTANTIAL REVISION REQUIRED.** Doc_01 is not Approved to proceed.

**Substantial findings to fix (6):** H1, H2, M1, M2, M3, M4.

**Non-substantial fixes to make in the same pass (7):** M5, L1–L6.

**Round 2** should be a targeted recheck of only these items against the vendored files:

- H1: re-grep the replacement Session XXI Canon I and ch. II text;
- H2: header, §7 and §8;
- M1: engagement with the overlap;
- M2: the strand section's treatment of the episcopal/papal question and the omitted material;
- M3 and M4: the corrected claims and their confidence tags.

This is the first of the three capped rounds.

No escalation category is triggered by this review. The H2 "tension" that Doc_01 escalated no longer exists.
