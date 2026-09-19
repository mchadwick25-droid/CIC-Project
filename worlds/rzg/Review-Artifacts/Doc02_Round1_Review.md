# Doc_02 (Source Ecology) / Source Registry / Source Acquisition Manifest — Round 1 Adversarial Review

**World:** The Reformed Cities — Zurich & Geneva (`rzg`)
**Reviewed at commit:** `3d624182` ("Draft Doc_02 (Source Ecology), Source Registry, and Acquisition Manifest"), branch `reformed-cities-doc01`
**Documents reviewed as co-equal outputs of the same step, per `cic-build-cycle` and `Source_Registry_Template.md`:**
- `World-Builds/Reformed-Zurich-and-Geneva/Doc_02_Source_Ecology.md` (DRAFT, Revision 1)
- `World-Builds/Reformed-Zurich-and-Geneva/Source_Registry.md`
- `World-Builds/Reformed-Zurich-and-Geneva/Source_Acquisition_Manifest.md`
**Reviewer stance:** cold adversarial review — no drafting context. This is document 1 to attack, not to polish.

---

## Verdict: SUBSTANTIAL REVISION REQUIRED

Four High findings, each of which changes a sourcing conclusion, a confidence rating, or the correctness of a claim a careful reader would notice as different once fixed — the `cic-build-cycle` bar for "substantial." Two of the four recreate failure patterns this exact world's own Doc_01 review history already found and fixed (self-certified claims about what a governing document says, and confidence-vocabulary inflation), and one is an outright non-discharge of a binding instruction from the already-approved Doc_01. The primary-source citation work itself (the vendored-file spot-checks below) is, by contrast, largely excellent — the defects are concentrated in cross-document attribution discipline and Registry schema fidelity, not in the underlying vendored-text handling.

---

## High findings

### H1 — Fabricated attribution: a book not named in the census's `sources` field is claimed to be named there, and repeated identically across all three documents

Doc_02 §3 states: *"what Doc_01 already cited from general knowledge — Bruce Gordon's *Calvin* and *The Swiss Reformation*, Scott Manetsch's *Calvin's Company of Pastors*, named in the census's own `sources` field but not independently verified or vendored this pass."*

Source_Registry.md row 11 states the same for *Calvin* and *The Swiss Reformation* together: *"Named in the census's own `sources` field; not checked against the actual books this pass."*

Source_Acquisition_Manifest.md §3 states: *"All three named in the census's own `sources` field; none independently verified or vendored this pass."*

I pulled the actual census entry (`cic-website/data/world-census.json`, id `the-reformed-cities-zurich-and-geneva`). Its `sources` field contains exactly one secondary-scholarship line: *"Scott Manetsch, Calvin's Company of Pastors (OUP, 2013), with Bruce Gordon, Calvin (Yale, 2009)."* **Bruce Gordon's *The Swiss Reformation* (Manchester, 2002) does not appear anywhere in this census entry** — I grepped the full serialized entry for both "Swiss Reformation" and "Manchester" and got zero hits on both.

The claim is also wrong on its other half: Doc_02 attributes the same three-book list to "what Doc_01 already cited." I grepped the complete text of `Doc_01_World_Identification_Boundaries_Orientation.md` for "Gordon," "Manetsch," and "Swiss Reformation" — **zero matches on all three.** Doc_01 never cites any of these three works.

So a real, correctly-titled book is attributed to two different governing documents (the census and Doc_01), neither of which actually names it, and the false attribution is repeated verbatim in all three sibling documents from this same drafting pass rather than caught by cross-checking one against another. This is the identical failure shape Doc_01's own Round 2 review caught and flagged as H1 there ("Revision 2 asserted in its own voice that Lutheran Wittenberg's Step 0 'does call' Trent its own 'direct doctrinal rival' — a quotation that does not exist anywhere in that document, discovered by the reviewer grepping the full tree"). It recurs here in the very next document, on a citation to a governing source rather than a quotation, but the mechanism — asserting in the builder's own voice that a specific document says something it does not say — is the same one this world's own build history has already named as its most serious defect category.

**Fix required:** correct the attribution in all three documents (Doc_02 §3, Registry row 11, Manifest §3) to state accurately that only Gordon's *Calvin* and Manetsch's *Calvin's Company of Pastors* are named in the census; that Gordon's *Swiss Reformation* is the builder's own addition from general knowledge, not a census or Doc_01 citation; and that none of the three is cited anywhere in Doc_01 at all (correct the false "what Doc_01 already cited" framing).

### H2 — A binding Doc_01 §8 item is not discharged, and its non-discharge is not even carried forward as an open item

Doc_01 §8 item 4 states, in terms explicitly binding on this document: *"The Anabaptist-origin correction... Doc_02 must state the Grebel/Blaurock/Manz origin correctly, without extending Zwingli-circle membership to Blaurock, and correct both the dossier's §5 and this world's own Step 0 §3 B3."*

I grepped the full text of Doc_02, the Registry, and the Manifest for "Anabaptist," "Grebel," "Manz," and "Blaurock." The only hit in any of the three documents is one clause in Doc_02 §2 (Zwingli's Author Gravity, *Influence*): *"The direct forerunner of ... the Anabaptist movement's own break from his circle (Doc_01 §7)."* That is a passing, generic gesture at the topic — it never states the corrected origin (Grebel baptizing Blaurock, who then baptized the others including Manz; Blaurock's own circle membership not established), never touches the Source Readiness Dossier's §5 correction, never touches Step 0 §3 B3, and — unlike Doc_01's own handling of its analogous out-of-scope propagation duty for the Dort boundary (explicitly named as "owed, not performed" in Doc_01 §8 item 3 and §9) — Doc_02's own §9 "Open items carried forward" list (seven items) does not mention this correction at all, whether as discharged, partially discharged, or still owed.

Doc_02's own header claims it is "grounded in `Doc_01_World_Identification_Boundaries_Orientation.md`... which this document does not reopen except where Doc_01's own §8 open items bind this document to act." This is one of those binding items, and it was silently dropped rather than acted on or disclosed as outstanding. This is exactly the "checkpoint, not just intent" failure the Registry Template itself warns against for a different mechanism (a claim without a corresponding row) — here it is a binding instruction without a corresponding discharge or disclosure.

**Fix required:** either state the Grebel/Blaurock/Manz correction accurately wherever the Anabaptist break is mentioned, and name the dossier/Step0 propagation correction as an owed-but-not-yet-performed item (parallel to how Doc_01 itself handled the Dort propagation duty) — or, if judged genuinely out of scope for Doc_02's own content, say so explicitly and carry it forward in §9 rather than omit it.

### H3 — Source Registry schema violation: "Boundary Status: Native" rows carry non-conforming "Excluded" text in the Exclusion Reason column, conflating subject-matter boundary with acquisition/availability status

`Source_Registry_Template.md`'s Entry Schema is explicit and repeated: **Exclusion Reason** is *"required if Excluded, blank if Native"* and its only two permitted values are **Out-of-Boundary** and **Named Comparandum**; **Licensed For** is *"required if Native, blank if Excluded."* The Template goes out of its way to insist that Boundary Status is a subject-matter judgment only — *"Boundary Status is never assessed by the date a piece of scholarship happened to be written... A source... whose own subject or origin belongs to a different era, place, or tradition is Excluded, however well-regarded"* — and that collapsing this distinction from a different one is exactly the failure mode an earlier version of this mechanism already produced and had to be redesigned to prevent.

Rows 13–17 of `Source_Registry.md` (the Consistory registers, the Ecclesiastical Ordinances, the Genevan Psalter, Beza's works, and Dentière's works) all set **Boundary Status = Native** (correct — these sources are squarely about this world) but then populate the **Exclusion Reason** column with text like *"Excluded — in copyright,"* *"Excluded — no traceable PD source located this pass,"* and *"Excluded — not yet searched for a PD source."* None of these is a permitted Exclusion Reason value, and the column is supposed to be blank whenever Boundary Status is Native. The same five rows also populate **Licensed For** — which per the Template should be the specific target a Native, usable source justifies — with conditional, not-yet-true text ("would license X if acquired; currently licenses nothing"), rather than either a real licensed use or a blank field.

This is a genuine, repeated (5 of 17 rows — essentially every row for a source that exists in this world's boundary but is not yet vendored) schema violation, using "Excluded" to mean "not currently acquired" rather than what the Template defines it to mean. The downstream risk this exact mechanism was built to prevent — a Native-marked entry being read by a person or a later automated process as usable — is currently caught only because Confidence is separately, correctly set to D/E on these rows, not because the Boundary Status/Exclusion Reason fields are used correctly. That is a fragile safety net: it depends on every future reader also checking Confidence, when the Template's own design puts a comparable safeguard in the Exclusion Reason/Licensed For pairing specifically so a reader does not have to cross-reference two axes to find out a row isn't usable.

**Fix required:** either (a) leave Exclusion Reason blank on rows 13–17 (since Boundary Status is genuinely Native) and move the acquisition-status information into the Verification Note, where it is in fact already substantively present, or (b) if the project judges the Template genuinely needs a third status for "Native, not yet acquired," raise that as a Template amendment (a methodology change, outside this build thread's own editing authority per `cic-build-cycle`) rather than inventing an unlisted convention silently inside one world's Registry.

### H4 — Confidence-vocabulary misuse: "documented" applied to a claim the same document immediately discloses as not vendor-verified, recreating a defect Doc_01's own Round 3 review already caught and Revision 5 already fixed

Doc_02 §7 states: *"this world's own transmission may include the Canons of Dort's international Reformed dimension and the documented (historiographically attested, not vendor-verified) Zurich/Geneva delegate participation."*

"Documented" is not a loose adjective in this project's vocabulary — it is the top rung of the fixed five-level confidence scale (Constitution Article 17, operationalized in Construction Framework V7.4: *"Documented — Multiple independent sources with no serious scholarly dispute. Permitted language: 'documented,' 'securely attested.'"*). Doc_01's own Round 3 review found and named exactly this defect on this exact claim: *"the Dort delegate-participation claim was upgraded from 'not independently verified' to 'documented' inside the new confirmation text, contradicting the hedge two sections earlier."* Doc_01's Revision 5 fixed it by using only the hedged form everywhere the claim appears, and Round 4 review independently confirmed that fix held. Doc_02 — drafted immediately after that fix was verified — reintroduces the word "documented" for the identical claim, parenthetically hedged in the same breath, which is precisely the "invisible movement from attested evidence into speculation" Article 17 exists to prevent (the word carries the top-tier claim even while the parenthetical disclaims it).

**Fix required:** drop "documented" and use only the hedged form Doc_01 settled on ("historiographically attested, not yet checked against a vendored primary source"), consistent with how this exact claim is worded everywhere else in this world's build.

---

## Medium findings

### M1 — Heidelberg Catechism "doctrinally continuous with both [strands]" overstates what the very source cited actually shows, and the Doc_01 §2 citation for it doesn't fully support it

Doc_02 §1 states the Heidelberg Catechism is *"not itself Zurich- or Geneva-authored but doctrinally continuous with both (Doc_01 §2)."* Doc_01 §2 itself only quotes the corpus map's description of the Catechism as *"a distinct pastoral/catechetical voice alongside Calvin's Geneva Catechism, from the Reformed tradition's German wing"* — it does not itself state "doctrinally continuous with both," so the parenthetical citation oversupports the claim.

More substantively: I read the vendored file directly (`schaff_second-helvetic-confession-heidelberg-catechism_1919.txt`) and it contains Schaff's own critical introduction to the Heidelberg Catechism, which states plainly that the Catechism — despite its authors being, in Schaff's words, "strict predestinarians" like every other Reformer of the era except late Melanchthon — *"nothing is said of a double predestination, or of an eternal decree of reprobation, or of a limited atonement... These difficult questions are left to private opinion."* Given that predestination is named by Doc_01 as one of this world's own cross-strand, load-bearing gravities, and given this specific nuance sits directly inside the very file Registry row 10 cites as its Verification Note locus, a blanket "doctrinally continuous with both" is a claim Doc_02 could have qualified from its own cited source and did not.

**Suggested fix:** either narrow the claim to the specific doctrines actually shared (sola scriptura, sacramental theology, church order) or note the Catechism's own documented reticence on double predestination specifically, and correct the Doc_01 §2 citation to point to what it actually says.

### M2 — Registry rows 11–12 (Gordon's *Calvin*, Manetsch) leave "Licensed For" unspecific, contrary to the Template's requirement

The Template states: *"A Native source with nothing named here is not yet usable downstream."* Rows 11 and 12 both fill Licensed For with *"General secondary-scholarship background only — not independently verified or vendored this pass"* rather than a specific gravity, force, lexicon term, or trait. This is a real if minor template-compliance gap, compounding H1 above (row 11 is also the row carrying the fabricated census attribution).

### M3 — Doc_02's own escalation self-assessment (§10) is markedly thinner than the standard this world's own Doc_01 was eventually held to

Doc_01's later revisions were specifically required, after repeated review findings, to run each of the four escalation categories explicitly and "fresh" rather than assert a conclusion (Round 3 and Round 4 both did this in named, itemized form). Doc_02 §10 states its conclusions ("makes no portfolio-level or cross-world decision... no escalation category applies") without running each category against specific candidate tensions the way Doc_01 was made to. My own fresh check (above, and in the Escalation section below) did not find a live category, but the document's own reasoning does not yet meet the bar this world's own review history has already established as necessary — worth requiring explicitly in the next revision rather than leaving it to a future round to catch again.

### M4 — Minor "Doc_02/G1" labeling drift between Doc_01 and the actual Manifest

Doc_01 §8 items 7 and 8 both refer informally to "Doc_02/G1" for what the Acquisition Manifest actually labels **G3** (the consistory registers) and **G1** (the Ecclesiastical Ordinances) respectively. Not a substantive defect — Doc_01's usage is clearly generic shorthand, not a specific label requirement, and the Manifest's own recommended priority order (G3 first) actually honors Doc_01's intent — but worth a one-line disambiguating note so a future reader tracing binding items by literal G-number isn't misled.

---

## Low findings

### L1 — Consensus Tigurinus intake header's claimed page range doesn't fully match the extracted text

The file's own intake header claims the extract covers "pp. 195–247 of the printed text." I checked the extracted text directly: the last visible printed page marker is **244**, and the file ends shortly after with no further page numbers. All claimed content (the prefatory letters, the Zurich pastors' reply, and all 26 numbered "Heads of Agreement," verified I through XXVI by direct inspection) is fully present, so this does not affect any substantive claim — but the stated page range should be rechecked against the print volume (it may include unnumbered closing matter, or may simply be off by a few pages).

### L2 — A vendored source does contain the string "Dort," referring to a different, unrelated event

Doc_02 §7 states "No vendored source in this corpus currently touches Dort directly in any case." This is true for the 1618–19 Synod discussed throughout Doc_01 §7 and Doc_02 §7 — but the Schaff volume (`schaff_second-helvetic-confession-heidelberg-catechism_1919.txt`) does contain one reference to "the synods of Wesel, 1568, of Emden, 1571, and of Dort, 1574" — an entirely different, earlier Dutch synod bearing the same place name. Worth a one-sentence disambiguating note so a future keyword search against this corpus isn't misread as contradicting this disclosure.

### L3 — Registry header's "Doc_02's own five-level narrative-confidence vocabulary" slightly overstates ownership

The five-level vocabulary (Documented / Widely Accepted / Dominant Modern Reconstruction / Contested / Inferential-Thin) is the project's standard vocabulary, defined by Construction Framework V7.4 and attributed there to Constitution Article 17 — not something Doc_02 itself originated. I checked Article 17 directly (`CiC_L1_Constitution_V2_2.docx`, internal text V2.3): it establishes the *principle* of a single fixed confidence vocabulary and a longer descriptive list of evidentiary categories, but the crisp five-term list Doc_02 actually uses lives in the Framework, not verbatim in Article 17 itself — Article 17 even carries its own disclosed note that "the Construction Framework must be updated to this Constitution's authoritative version before this replacement language fully governs." This is a pre-existing, disclosed, project-level document-versioning gap, not something Doc_02 introduced or is responsible for fixing (a "doc-hygiene fix on content that isn't your own thread's," per `CLAUDE.md`'s own default-action table — flag, don't touch). Doc_02's own citation ("Constitution V2.3 Article 17 (five-level confidence vocabulary)") matches how the Framework itself describes the vocabulary's origin, so this is not a citation error on Doc_02's part — noted here only as background context for whoever eventually reconciles Article 17 and the Framework.

---

## What checked out cleanly (documented for balance, not as a hedge on the findings above)

- **Corpus-map/file-count claims.** "Ten corpus-map rows across eight vendored files" is exactly correct — verified directly against `cic/corpus-map/the-reformed-cities-zurich-and-geneva.yaml`.
- **The newly-vendored Consensus Tigurinus file.** Its own intake header, its title-page quotation ("BETWEEN THE MINISTERS OF THE CHURCH OF ZURICH AND JOHN CALVIN, MINISTER OF THE CHURCH OF GENEVA"), and its 26 numbered "Heads of Agreement" (I verified the file contains exactly headings I through XXVI) all check out exactly as Doc_02 and the Registry describe them, including the deliberate exclusion of Calvin's separate 1556 "Second Defence... Against Westphal" from the vendored extract.
- **Translator/editor/date attributions.** Beveridge 1845 (Institutes), Waterman 1815 (Geneva Catechism), Jackson 1901/1912 (Zwingli), Schaff 1919 printing of the 1877 *Creeds of Christendom* Vol. III (Second Helvetic Confession/Heidelberg Catechism) — all verified directly against each file's own intake header and consistent with the real historical publication record.
- **Word-count asymmetry claim.** "Roughly four times the vendored word count" (Calvin ≈ 809,000 words vendored vs. Zwingli ≈ 217,000 words) checks out at ≈3.7×, a fair "roughly four times."
- **The declined G1 acquisition (Ecclesiastical Ordinances).** I independently fetched both sources named in the manifest. Schaff's CCEL §104 is confirmed to be Schaff's own narrative paraphrase interspersed with short quotations, not a full direct translation of the Ordinances — exactly as characterized. The archive.org item `calvino-theological-treatises` is confirmed via its own metadata (date: 1977, `licenseurl`: the Creative Commons Public Domain Mark 1.0) to be the Library of Christian Classics volume — its own table of contents lists "DRAFT ECCLESIASTICAL ORDINANCES (1541)" directly, confirming the identification — and the Public Domain Mark is correctly characterized as a user-applied label, not a rights determination. This is sound, disciplined reasoning, correctly declining a tempting shortcut.
- **Zwingli/Bullinger/Calvin dates**, the Sixty-Seven Articles' file location (verified at the exact claimed line range), Marie Dentière's corrected biography (anonymous 1539 work vs. signed 1561 preface) and Beza's status as unvendored — all restated accurately and consistently with Doc_01's own findings, with no drift found.
- **The Registry/Doc_02 confidence-axis separation.** The two different "confidence" concepts (Registry's A–E citation-reliability axis vs. Doc_02's five-level narrative vocabulary) are explicitly and consistently kept distinct throughout — the one place I found vocabulary bleed (H4 above) is a word-choice slip, not a structural conflation of the two systems.

---

## Escalation-category check (run fresh, not trusted from Doc_02's own §10 claim)

- **Representative identity, title, or voice decision:** does not apply. No such decision is made anywhere in these three documents.
- **Portfolio-level or cross-world strategic decision:** does not apply as a live decision. The declined G1 acquisition is genuinely an application of an existing PD-by-date rule, not a new rule. The sandbox-access anomaly noted in Doc_02 §9 item 7 (working access to archive.org/ccel.org where the project's general note says these are blocked) is a fact worth a coach thread's attention but is not itself a decision Doc_02 is making, and is already correctly flagged rather than acted on unilaterally.
- **Governance or methodology decision:** does not apply on its own terms, though H3 above (the Registry schema conflict) may eventually surface a real Template gap worth a genuine methodology conversation — noted as a possible future item, not a live decision this pass.
- **Unresolved tension the pipeline can't close on its own:** does not apply in the sense the category is designed for (no two already-cleared documents contradict each other, and no prior decision is being reopened). H1–H4 above are ordinary revision findings within this build thread's own authority to fix, not tensions requiring project-lead adjudication.

No escalation category is live. All four findings above are addressable by revision within this build thread's own ordinary authority.

---

## Recommendation

Revise Doc_02, the Source Registry, and the Acquisition Manifest together (they are co-equal outputs of the same step) to close H1–H4, then send the revised set through a fresh independent review round per `cic-build-cycle`. Given H1 and H4 each recreate a failure pattern this exact world's own Doc_01 review history already named and fixed, the revision should explicitly re-check for both patterns elsewhere in the revised text, not only at the specific locations named above.
