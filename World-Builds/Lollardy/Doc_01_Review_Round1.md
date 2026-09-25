# Doc_01 Review, Round 1 — Lollardy

**Reviewer:** independent adversarial review agent (Opus), 2026-09-25, per `cic-build-cycle` discipline. Full first-round review.
**Document reviewed:** `World-Builds/Lollardy/Doc_01_World_Identification_Boundaries_Orientation.md` (DRAFT).
**Checked against:** `Step0_Movement_Scope_Confirmation.md` (Revision 3) and `Step0_Review_Round1–3.md`; `worlds/_cross-world/dossiers/lollardy_Source_Readiness_Dossier.md`; `cic-website/data/world-census.json` (entry `lollardy`, at HEAD); `cic/corpus-map/lollardy.yaml`; `worlds/_cross-world/LIBRARY-DECISION-LOG.md` (2026-09-25 ruling, point 5); Constitution V2.3 (`reference/L1-Foundation/CiC_L1_Constitution_V2_2.docx`, internally "Version 2.3"); Forces Framework V1.1; `worlds/witt/witt_Doc_01_...md`. Every quote was re-checked against the vendored files in `cic/texts/`: `fasciculi-zizaniorum_shirley1858.txt`, `foxe_acts-and-monuments-v3_cattley-townsend1837.txt`, `wyclif_select-english-works-v3_arnold1871.txt`, and `hus_de-ecclesia-the-church_schaff1915.txt`.

## Verdict

**SUBSTANTIAL REVISION REQUIRED. Not approved to proceed.** 1 Critical, 8 Substantial, 12 Minor.

The document holds Step 0's settled points. The window, the eleven-work count and Tier 2 are unchanged. The Hussite corpus-map question is left to Mark. The English-Reformation line is never asserted. Its engagement with the Hussite dependency is honest in structure.

Four things fail, though. One quotation is a composite spliced from two passages, with a word added. The Strand Determination rests on claims the vendored corpus itself contradicts. Most Latin and Foxe quotations are silently normalized away from the OCR. And several "Documented" labels sit on claims the cited text doesn't make.

## Findings by severity

### Critical

**C1. §2 (Beginning point): the Arnold "quotation" is a composite that no single passage contains.** The document gives, as one quotation: "This allusion to the earthquake 1382 ... [condemned] at London by Archbishop Courtenay in May, 1382" (lines 10742 and 11189 ff.). These are two separate editorial notes, about 450 lines apart and printed in the reverse order:
- line 11189: `a  This  allusion  to  the  earthquake  1382,  on  May  19  {Fasc.  Zizaniomm,` … `fixes  so  far  the  date  of  this` … `treatise.`
- line 10741–42: `composed, it  would  seem,  not  long  after  the  holding  of  the  council  convened` / `at  London  by  Archbishop  Courtenay  in  May,  1382.`

The bracketed "[condemned]" appears in neither. Line 10742 says "council convened," not condemned. The splice makes Arnold appear to corroborate the condemnation, which neither note does. This is the fabrication-in-a-quote defect this project names as most serious for source fidelity. Fix: quote each note separately and verbatim, with its own line number. Claim only what the notes support: Arnold dates two tracts (not "several," and not sermons) by the May 1382 council and earthquake. The condemnation of the twenty-four conclusions stands as **Widely Accepted** on its own, not as corroborated by Arnold.

### Substantial

**S1. §4 Strand Determination: the two-strand finding does not survive the vendored evidence, and it falls back into the sequential reasoning it disclaims.**
- *Strand A's evidence predates this world's own window.* The only named evidence is *De Ecclesia* and *De Veritate Sacrae Scripturae*, conventionally dated c. 1378 (Widely Accepted). §2 places the start at c. 1379–82. It also assigns the earlier Oxford-academic phase to "the larger world Lollardy emerged from, not to Lollardy itself." A strand can't be evidenced from material the document itself puts outside the world.
- *"Closed 1382 … No later actor in this window continues to argue Lollard doctrine in this specific Latin-academic … form" is contradicted by the vendored corpus.* Foxe's Hereford process calls Walter Brute "a lay person, learned" (line 10722). Brute writes that he was "required that I should write an answer in Latin to all those matters" (lines 11162–66, 1391–93). *Fasciculi Zizaniorum* preserves the Twelve Conclusions and Purvey's articles in Latin. Beyond the corpus, Oxford Wycliffism continued past 1382 until Arundel's Oxford measures of 1407–11 (Widely Accepted).
- *Strand B is defined as lay and "without requiring Latin literacy," but its named members don't fit.* Thorpe is a priest by his own account ("we have taken upon us the office of priesthood," Foxe c. line 21340 ff.). Brute answered in Latin. The Wycliffite Bible's Earlier Version is widely held to be a product of the Oxford circle.
- *The simultaneity claim is load-bearing but unsupported and unrated.* It rests on Arnold's Middle English material. The document itself concedes that material is collective, and its dating to Wyclif's lifetime is itself contested. The simultaneity claim gets no confidence tag.
- *Net effect:* for about 1382–1520 the document describes one strand. What separates "A" from "B" is the genre and audience of one author's output, plus the fact that "A" ended first. That is sequential development and a register difference, not a finding of divergent authority structure or ecological orientation across the window (Art. 21 definition).

Fix: re-run strand determination on recurring-ecology evidence across the whole window. One candidate the evidence does show is learned or clerical Lollardy (Oxford men, Purvey, Thorpe, Brute) alongside household lay networks. The other outcome open is a strand-singular finding, with that difference carried as internal plurality under Art. 16. The reviewer doesn't prescribe which. Revise §4, §5 Cell 2B, §10.4, and the Strand B references in §3 to match.

**S2. Quote fidelity: Latin and Foxe quotations are silently normalized away from the vendored OCR, and the document states they were "verified directly against the vendored Latin text."** LIBRARY-DECISION-LOG point 5 says "No model ever retypes a source." Step 0 A1 set this world's own precedent of reproducing OCR artifacts exactly. Instances:
- Heading, line 28381 ff.: vendored text is `SKQUUNTrU  CONCLUSIONES     LoLLAUDORUM     IN     QUODAM` / `LIIiKLLO  PORRECT^E       PLENO       PARLIAMENTO       RKCJNI  '` / `AnCLLE,` … The document gives clean "SEQUUNTUR … LOLLARDORUM … LIBELLO PORRECTAE … REGNI ANGLIE".
- Conclusion IV: vendored `onmes    Jiommes.    nisi   smt   pauci,    m   idolatnam`. The document gives "omnes homines... in idolatriam". Its ellipsis also silently drops the qualifier *nisi sint pauci* ("except a few"), which strengthens the claim.
- Conclusion IX: vendored `domiui  et  domiure`, given as "domini et dominae". The corollary is vendored as `fictam  indul-` / `gentiain  a  pcena  et  a"''  culpa`, given as "fictam indulgentiam a poena et a culpa".
- Foxe on Arundel, line 32309–10: vendored `WicklifF  for  cvcr  after`, given as "Wickliff for ever after".
- Thorpe, line 20623: vendored "penned with his own Hand." The lower-case form is at the contents entry, line 389; cite whichever one is quoted.
- Wrong line citation, given twice (§3, §5): Conclusion IV is at **lines 28485–28523**, not "28603 ff." Line 28603 is in Conclusion VI.
- Translation inside quotation marks: "feigned with a higher angelic power" renders *fictum potestate angelis altiori*. The Latin means a power *higher than the angels'*, not an angelic power.
- "in Wyclif's own words per the Twelve Conclusions": the Conclusions *report* what the *doctor evangelicus* says in his *Trialogus*. They don't quote Wyclif's words.

Fix: give each quote either verbatim OCR with artifacts, or an explicitly labeled normalized reading next to the verbatim string. Correct the line numbers. Mark paraphrase and translation as such. **Library-thread flag (not this document's to fix):** `cic/corpus-map/lollardy.yaml` calls the *Fasciculi* scan "clean, not flagged under Mark's OCR ruling 'a'". The cited passages show real garbling (`SKQUUNTrU`, `idolatnam`, `domiure`, `a"''  culpa`). That classification should be re-checked before this text serves as primary evidence.

**S3. §1, §2 (Ending point, Chilterns, Catalysts): the Amersham evidence is misdated and over-read, and it is the ending boundary's own evidence.** The one vendored attestation (lines 32322–35) is a sentence inside Foxe's polemic against Cope. It says "in the beginning of king Henry VIII," under "Longland, being then bishop of Lincoln." Foxe defers the actual account: "when we come to that time … shall hereafter more amply … appear." That account is in a later volume, which is not vendored. The document turns this into "the first two decades of the sixteenth century" and "c. 1506–1522 … under Bishop Longland." But Henry VIII's reign began in 1509, and Longland was bishop of Lincoln only from 1521 (Widely Accepted). The 1506 Amersham burnings fall under Henry VII and Bishop Smith, and appear nowhere in the vendored text. Fix: date the vendored attestation to Longland's episcopate (1521–22) and label it Documented only for what the sentence says. Describe it as a forward reference, not a trial record. If the window's own "c. 1520" end is kept, note that the cited closing event falls just after it.

**S4. §1, §2, §4: social-composition claims about the Twelve Conclusions exceed the vendored text.**
- "posted publicly and addressed to Parliament by *named* lay adherents": the heading (`IN QUODAM LIBELLO PORRECTAE PLENO PARLIAMENTO`) names no one. The text speaks as *nos procuratores Dei* (line c. 28604). The public posting and any link to the "Lollard knights" come from chronicle tradition. Whether the authors were lay or clerical is itself uncertain. Labeled Documented, and called "a public lay articulation" in §4, this needs Widely Accepted at most for the posting, and an open or Contested tag for lay authorship.
- §2 uses *domini et dominae* (Conclusion IX) as evidence that "women appear in the record as participants." In the text, lords and ladies testify that they dare not tell the truth to their confessors out of fear. They appear as penitents in general, not as Lollard participants. "Laypeople of both sexes" also flattens *domini/dominae* (lords/ladies). Fix: withdraw the inference, or support it with evidence that actually shows it.

**S5. §1 Distinctive Contribution (ground 2) and §1 wording: the Hussite comparison overreaches, and one label contradicts Step 0.** "Nothing comparable anchors the Hussite world's own corpus" is an unchecked comparative claim about another world, carried at Documented/Widely Accepted. Czech vernacular preaching is on record in the Hussite Step 0 itself (§1: Hus "began preaching reform in Czech at Prague's Bethlehem Chapel in 1402"), and a Czech vernacular Bible tradition is Widely Accepted. Fix: hold ground 2 open, as ground 3 already is, or narrow it to what is documented, such as the English manuscript-survival scale. Separately, §1 calls the Hussite world "a batch-mate." Step 0 §3 B3 and B5 state that it belongs to a separate, later batch (2026-09-25).

**S6. §2 Catalysts, 1401: "William Sautre burned as a heretic — the first Lollard executed under the new statute."** The Widely Accepted account is that Sautre was burned under a royal writ in early March 1401, before *De heretico comburendo* was enacted in that same parliament. Fix the claim. The old-style-date note on Foxe's `a.d.hoo` (read as 1400) is reasonable, but say that the OCR reading is itself garbled.

**S7. §5 "What was it responding to": the confidence is mislabeled.** "The lack of vernacular Scripture access" is labeled "Documented, per the cited Twelve Conclusions text." None of the twelve conclusions addresses vernacular Scripture. Fix: source it properly, for example to the translation project itself or to Arundel's constitution via Foxe as the authorities' *reaction*, or relabel it.

**S8. §1 and §6: a stale census phrase is reintroduced and attributed to the census.** "It 'carries the contest rather than the conclusion' (dossier §6)" is presented as "the discipline the census itself models." That wording is not in the live census. Step 0 Round 1 S6 and Round 2 R2-S3 found it was removed on 2026-09-20, and Step 0 was revised specifically to stop quoting it. The dossier still carries it, stale. This is a regression of a cleared defect. Fix: anchor the framing to the live `relationsSummary` ("Contested influence line to the English Reformation"), which the document already quotes correctly. Optionally add the live source note: "The contested question of Lollardy's influence on the English Reformation belongs to the Reformation period itself."

### Minor

- **M1.** Step 0 cleared on **2026-09-25** (Step0_Review_Round3), not 2026-09-15 (header, §8).
- **M2.** §7 items 1–2: Step 0 §4 makes these "binding on Doc_01 and Doc_02," but Doc_01 relabels them "binding on Doc_02." Item 5 is conditional in Step 0 ("if VI.4 is ever added"), but Doc_01 presents it as unconditionally binding. Restate them faithfully. Engaging item 5 anyway is harmless.
- **M3.** §2 London: the 1414 statute was enacted at the Leicester parliament. "London" as the seat of 1395's Parliament is Widely Accepted, not Documented "per the heading." The heading says only *pleno parliamento*.
- **M4.** §2 Historical Pressures: the Foxe passage is Foxe's own paraphrase ("where it was decreed, that …"), not a quotation of the constitution. The quote also stops mid-clause at "approved" without an ellipsis. Arundel's constitutions restricted unlicensed preaching generally, not "preaching from English Scripture."
- **M5.** §2 Brute: "lay Herefordshire landholder" is not the source's wording. Use the vendored self-description, "sinner, lay-man, husbandman, and a Christian … of the Britons" (line 11162–63), and "a lay person, learned, of our diocese" (10722). This bears on S1.
- **M6.** §3: "Conclusions I, VI, and IX" for "confession, indulgences, and the power of the keys." Conclusion VI concerns clergy holding secular office. Re-map these.
- **M7.** §3: Thorpe's Examination is grouped with "public or quasi-public doctrinal proclamation directed at Parliament." It is an account of a private examination before Arundel. §2 also cites it as attesting household reading circles. Check that against the text, or drop it.
- **M8.** §9 cites "Article 3 (No Forward-Projected Specificity)." That rule sits in the Constitution's front matter, not Article 3, and it binds Level 1 documents.
- **M9.** §5 Cell 3A: "contested arrival of Lutheran-influenced ideas" is imprecise. The Lollard–Reformation *link* is contested, not the arrival itself. Cell 2A's "requiring continuous underground adaptation" drifts toward Layer 3. Otherwise §5 stays properly Layer-1 and Step-2-orienting.
- **M10.** §1 "many-times-removed line": the document's own characterization. It pre-judges the contest in the minimizing direction, which is the mirror of overclaiming. Use the census's neutral wording.
- **M11.** Process narration inside a document bound for a canonical surface: "the two forces this document's own task explicitly names" and "three refusals this document's own task explicitly asked to be checked" (§5). Remove it at revision (CLAUDE.md, live/canonical surfaces).
- **M12.** §2 London / Geographic Centers: Tanner is described as "already-verified." Per Step 0 §4.1, cite Step 0's §3 B1 correction rather than lean on the census "Verified" tag's authority. The existence of the archive.org item is what is actually on record.

## Confirmed accurate

- Census `floorNote` (both sentences) and `relationsSummary` ("Contested influence line to the English Reformation"): verbatim at HEAD.
- Schaff on Hus: "Huss appropriated paragraph after paragraph from his predecessor and transferred them often with little verbal change to his own pages." Verbatim at `hus_de-ecclesia-the-church_schaff1915.txt` lines 1514–16.
- Foxe: "the good martyrs of Amersham," "in the beginning of king Henry VIII," and Longland as bishop of Lincoln (lines 32322–29). Badby "a tailor and a layman" (19229), with Foxe's "a.d. 1409 … first day of March," so the old-style explanation is correct. "1392. Letter of the King against Walter Brute" (index, line 327). Brute's process before the bishop of Hereford (10690 ff.).
- *Fasciculi*: the heading's content, including *ANNO EJUS CIRCITER XVIII*. Conclusion I's *novercam suam magnam ecclesiam Romanam* and temporalities. Conclusion IV's *doctor evangelicus … in suo Trialogo … panis altaris est habitualiter corpus Christi*. Conclusion VIII's *surdis imaginibus de ligno [vel] lapide … prope consanguineae ad idolatriam … imago usualis de Trinitate est maxime abominabilis* (28672 ff.). The IX corollary's indulgence *a poena et a culpa* (28778–81). In substance, all three "refusals" are present in the text. What fails is the verbatim rendering (S2).
- Arnold's two notes each exist, at 10742 and 11189. Only their splicing fails (C1).
- Step 0 consistency: the window of c. 1380–1520 is unchanged; eleven vendored works; Tier 2 not reassigned. The document does not cite the Decision Log at all, so there is no "ERA 7" error. The Hussite corpus-map question is left explicitly to Mark (§7.7).
- The English-Reformation line: the document never asserts causation and carries it as Contested throughout. Only the S8 attribution and M10 wording need attention.
- Constitution Art. 21 quotes are verbatim, and Art. 3's cross-world-contamination language is correctly characterized in §6.
- `worlds/` listing is accurate. Wittenberg's 1517–1580 window and "territorial, state-recognized magisterial Reformation" match `witt` Doc_01.

## Disposition

**Revise and resubmit for Round 2.** C1 and S1–S8 each change a claim's substance, confidence rating, sourcing conclusion, or scope-boundary evidence, so each is substantial under this project's definition. S1 in particular changes the Strand Determination finding itself.

Round 2 should be a targeted recheck of these findings only. It should re-verify every revised quote character by character against the vendored file.

No escalation category is triggered at Round 1. Two items go to the Library thread, flagged here and not touched by this review. First, the *Fasciculi* "clean scan" classification (S2). Second, the dossier's stale §1, §2 and §5 (seven works, "no context-role material yet") and its stale census phrase (S8).
