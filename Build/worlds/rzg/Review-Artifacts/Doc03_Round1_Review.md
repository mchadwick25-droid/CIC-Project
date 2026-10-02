# Doc_03 (Lexicon Candidate List) — Round 1 Independent Adversarial Review

**World:** The Reformed Cities — Zurich & Geneva (`rzg`)
**Document under review:** `Doc_03_Lexicon_Candidate_List.md`, DRAFT, Revision 1
**Reviewed against:** `Doc_01_World_Identification_Boundaries_Orientation.md` (Approved to proceed, Rev. 5), `Doc_02_Source_Ecology.md` (Approved to proceed, Rev. 3), `Source_Registry.md`, `Source_Acquisition_Manifest.md`, and the vendored primary texts in `cic/texts/` (`calvin_institutes-christian-religion-vol1/2/3_beveridge1845.txt`, `calvin_geneva-catechism_waterman1815.txt`, `calvin-zurich-pastors_consensus-tigurinus-mutual-consent-sacraments_beveridge1844.txt`, `zwingli_selected-works_jackson1901.txt`, `zwingli_latin-works-correspondence-vol1_jackson1912.txt`, `schaff_second-helvetic-confession-heidelberg-catechism_1919.txt`), plus `Build/reference/L4-Templates/Deployment_Lexicon_Chunk_Template.md` for the four recognized CT Contest Types (Meaning / Historical scope / Application to this world / Relationship to present-day traditions).
**Method:** every one of the 18 candidates' claimed textual grounding was checked directly against the vendored files (grep + direct read, not taken on the document's own word); every internal cross-reference to Doc_01 or Doc_02 that used a section number or quotation mark was independently re-opened and checked against that document's actual text.

**Reviewer's own note on where this review was run:** run in an isolated worktree checked out on branch `worktree-agent-a980499415e1d68a6`, not `reformed-cities-doc01` (that branch was checked out in the main repo tree and could not also be entered here). Doc_01/02/03, the Source Registry/Manifest, and all vendored primary texts were read via `git show reformed-cities-doc01:<path>` — git objects are shared across worktrees even though the branch itself is checked out elsewhere. This file was copied onto `reformed-cities-doc01` by the main build thread after the fact.

---

## Verdict: Substantial revision required

Two of Doc_03's own internal citations to Doc_01 and Doc_02 attribute specific findings — one of them a quoted phrase — to sections that do not contain them. This is the exact fabricated/misattributed-citation failure mode this world's build has already been caught on twice (in Doc_01 and Doc_02). A third, repeated defect misnumbers a Source Registry row three separate times, breaking the row-level traceability the Registry exists to provide. None of this is cosmetic; all three recur or are load-bearing for how Doc_04 and Doc_06 will use this document. Everything else — the 18 candidates' actual textual grounding, the Strand column's defensibility, the Prophezei exclusion, the CT term's real-world accuracy — checks out well, and the document does the Step 3 job it claims to do without overreaching into Doc_06 territory. This is a document that is mostly sound but cannot proceed with two fabricated cross-references standing.

---

## Findings

### 1. [CRITICAL] Fabricated quotation and citation: Doc_01 §5 does not say what §4's CT-contest description attributes to it

**What was checked:** the CT candidate's contest description in §4: *"...the same tension Doc_01 §5 names when it observes that Beza's own later, harder predestinarian and Eucharistic positions were 'developed at the Genevan Academy,' not settled once for all by the 1549 document."* This attributes a direct quotation — "developed at the Genevan Academy" — to Doc_01 §5, describing it as a statement about Beza's Eucharistic positions.

**What was found:** Doc_01 §5 (Strand Determination) never mentions Beza's Eucharistic positions, never mentions the Genevan Academy, and does not contain the quoted phrase anywhere. A full-text search of Doc_01 shows "Genevan Academy" occurring exactly once in the entire document — in §2 (Geographic Centers), describing Geneva as "the seat of ... the Genevan Academy Calvin founded in 1559" — a plain biographical fact about the Academy's founding, with no connection to Beza, Eucharistic doctrine, or the Consensus Tigurinus. Doc_01's only discussion of Beza's later doctrinal development (§7, the Dort scoping section) concerns his *Tabula praedestinationis* (predestination, 1555) and the Arminius/Dort throughline — it says nothing about Eucharistic positions "developed at the Genevan Academy," and it is in §7, not §5.

**What's wrong and where:** `Doc_03_Lexicon_Candidate_List.md` §4, the CT candidate entry, attributes a quoted phrase and a substantive claim to Doc_01 §5 that Doc_01 §5 (or any other section of Doc_01) does not contain. This is fabrication at exactly the point — the one CT-tagged, most-scrutinized candidate in the document — where accuracy matters most, and it is the same failure mode (a source or locus that doesn't say what's claimed) already caught twice in this world's Doc_01 and Doc_02. Must be removed or rewritten to cite only what Doc_01 actually says, or dropped if no real Doc_01 support exists for the analogy being drawn.

---

### 2. [CRITICAL] Fabricated cross-reference: Doc_02 §8 does not carry the "Contested" finding attributed to it, and the error is repeated twice

**What was checked:** the Memorial/Commemoration candidate (Cluster 3, §1) states: *"a position the Consensus Tigurinus modifies rather than simply restates, a real difference Doc_02 §8 carries as Contested (whether the Heidelberg Catechism's own, and the Consensus's own, mature statements fully preserve or substantially soften Zwingli's own original emphasis)."* The same claim is repeated in §6 (Open Items): *"carried as the same Contested finding Doc_02 §8 already names for the Heidelberg Catechism's own predestination emphasis, applied here to the Supper specifically."*

**What was found:** Doc_02 §8 (Confidence Map) lists exactly three items under "Contested": (1) whether the Heidelberg Catechism's joint Ursinus/Olevianus attribution is genuinely co-equal or Ursinus-principal; (2) whether the Heidelberg Catechism's treatment of predestination is as developed as Calvin's or more restrained; (3) the degree to which Bullinger's thin vendored corpus understates his real centrality to the Zurich/Geneva bridge. A full-text search of Doc_02 for "soften," "memorial," and "Zwingli...emphasis" returns zero matches anywhere in the document. Doc_02 nowhere discusses whether the Heidelberg Catechism or the Consensus Tigurinus "preserve or soften Zwingli's original emphasis" on the Supper — that topic does not appear in Doc_02 at all, under any confidence level.

**What's wrong and where:** Doc_03 invents a Doc_02 §8 "Contested" finding about the Supper/memorial question that does not exist, and does so twice (§1 Cluster 3 table, and §6 Open Items) rather than once — meaning this is a load-bearing claim carried forward as though independently established, not a passing aside. Doc_03 may well have a legitimate point that this question is genuinely contested (the actual PV flag and Doc_01 §4's own finding that formation "genuinely changed substantially" between the strands support treating it as a live tension) — but it must say so as *its own* judgment, or correctly cite whatever Doc_02 content (if any) actually bears on it, not manufacture a citation to a document section that was reviewed and Approved to proceed on the strength of not containing fabricated claims.

---

### 3. [HIGH] Repeated Source Registry row misattribution: "row 13" is cited three times for content that is actually row 14

**What was checked:** every Registry row number Doc_03 cites, against `Source_Registry.md`'s actual rows.

**What was found:** Source Registry row 13 is *Registers of the Consistory of Geneva* (Confidence D, Manifest item G3). Row 14 is *Calvin's "Ecclesiastical Ordinances" of 1541* (Confidence E, Manifest item G1). Doc_03 cites "Registry row 13" three separate times while describing the Ecclesiastical Ordinances specifically and, in two of the three instances, while also citing Confidence E (row 14's own confidence level, not row 13's D):
- §1, Consistory candidate row: "established under the 1541 Ecclesiastical Ordinances ... not itself vendored (**Registry row 13, Confidence E**)" — row 13 is Confidence D, not E; the Ecclesiastical Ordinances is row 14.
- §2, Author-Gravity Concentration: "the Ecclesiastical Ordinances themselves remain unacquired (**Registry row 13**)" — should be row 14.
- §6, Open Items: "the Ecclesiastical Ordinances remain unacquired, **Source Registry row 13**/Manifest G1" — this one explicitly pairs the wrong row number with the *correct* Manifest item (G1 is in fact the Ecclesiastical Ordinances request), confirming the row number itself is the error, not a different mental model of what the Ordinances are.

The Cluster 4 section header also cites "rows 13/16 not yet acquired" for Church Order and Authority — row 16 is Beza's own works, which has no connection to any Cluster 4 candidate (Consistory, Excommunication, Antistes, Elder); this looks like the same row-tracking slip bleeding into the header.

**What's wrong and where:** a citation to a specific, numbered, append-only Registry row is exactly the kind of claim this project's fidelity discipline exists to make checkable — and re-checking it here shows it points to the wrong row, consistently, in three places plus a header. This must be corrected to row 14 throughout (and the stray "16" in the Cluster 4 header removed or corrected) before this document proceeds; a Registry citation that resolves to the wrong row is a broken pointer, not a stylistic slip.

---

### 4. [HIGH] Consistory and Elder are characterized as having no vendored textual grounding, but the underlying doctrinal concept is directly present in Calvin's own vendored Institutes

**What was checked:** Doc_03's claim (§0, §1, §2, §6) that Consistory and Elder are "named from general knowledge and Doc_01's own findings rather than from a vendored text using the term itself," "unverified against a primary source." I searched `calvin_institutes-christian-religion-vol3_beveridge1845.txt` (Registry row 3, Confidence A, Native) directly.

**What was found:** the term "consistory" occurs 9 times in vendored Institutes Book IV, including "the consistory of elders, which was in the Church what a council is in a city" and "the consistory ordained by the Spirit of Christ" (Book IV, ch. 11, on church discipline). More directly: Book IV ch. 3 §9 states Calvin's own doctrine of the office in almost exactly the terms Doc_03 uses to define the candidate term Elder — *"By these governors I understand seniors selected from the people to unite with the bishops in pronouncing censures and exercising discipline."* This is Calvin's own vendored, Confidence-A text explicitly defining a lay office (seniors "selected from the people," i.e., not clergy) that joins pastors in exercising disciplinary censure — the same substance Doc_03's own one-line world-meaning gives for Elder ("A layperson, not ordained clergy, holding formal disciplinary authority").

**What's wrong and where:** Doc_03's flag is directionally cautious rather than dangerous (it under-claims rather than fabricates, and honestly avoids the specific failure mode of overclaiming primary-text support — see Finding 6 below), but it is still factually inaccurate as stated. The real distinction that should have been drawn, and was not, is between (a) the *general Reformed theological doctrine* of the consistory and the lay elder — vendored, in Calvin's own words, Confidence A — and (b) *Geneva's own specific 1541 institutional practice* (weekly sessions, the actual composition and case history of the Consistory) — genuinely unvendored, Confidence D/E. As written, §1's Consistory and Elder rows, §2, and §6 all state or imply that no vendored text uses these terms at all, which is not true. This should be corrected before Doc_04/Doc_06 treat these two candidates as having zero textual grounding, since they in fact have real, direct grounding for the general doctrine even though the Geneva-specific institutional history does not.

---

### 5. [MEDIUM] CT Contest Type is never identified against the Constitution Article 26 / Deployment Lexicon Chunk Template's four recognized types

**What was checked:** whether the one CT-tagged candidate's contest (§4) is actually one of the four types the project recognizes (per `Deployment_Lexicon_Chunk_Template.md`, CT Contest Type section): Meaning, Historical scope, Application to this world, Relationship to present-day traditions.

**What was found:** the described contest — whether the Consensus Tigurinus's formula "represents a genuine theological synthesis or a diplomatically ambiguous formula" — is a real and recognizable instance of the **Meaning** type (a live disagreement about what the term/formula actually meant and accomplished within its own historical context, with two named sides). It is not Historical scope, Application-to-this-world, or Relationship-to-present-day-traditions. However, Doc_03 never states which of the four types applies — it describes the contest but does not label it.

**What's wrong and where:** this is defensible at the candidate-list stage, since Doc_03 explicitly defers full CT treatment to Doc_06 (§6: "Doc_06 should carry both readings forward, tagged, rather than resolve to one"), and the Chunk Template's own instruction to state the type by name is a Doc_06 chunk-assembly requirement, not a Step 3 one. Still, since Doc_03 already commits to a specific contest description here, and since the cic-lexicon-index skill's own review bar treats an unlabeled contest type as "the single most common gap in lexicon work," Doc_03 should name the type (Meaning) explicitly now rather than leave Doc_06 to re-derive it.

---

### 6. [MEDIUM] The CT contest's own factual premise ("scholarly opinion is divided") carries no confidence tag and no citation

**What was checked:** whether the CT contest description in §4 is grounded per Article 17's five-level confidence vocabulary, given that no secondary scholarship on the Consensus Tigurinus is vendored for this world (Doc_02 §3: no secondary scholarship vendored at all; Registry rows 11–12, Gordon and Manetsch, are consultation-only and not cited for this specific claim).

**What was found:** the claim that "scholarly opinion is divided" on whether the Consensus Tigurinus is a genuine synthesis or a diplomatic fudge is asserted as a bare fact, with no confidence level attached and no source named — unlike most other confidence-sensitive claims elsewhere in Doc_01/Doc_02, which are consistently tagged (e.g., "Dominant Modern Reconstruction confidence," "not independently verified against a primary vendored source"). This is a real, well-attested historiographical debate in Reformation scholarship in general terms, so it is not implausible — but as written it is asserted from the builder's own general knowledge with no calibration, on the one candidate in the entire document carrying the CT tag.

**What's wrong and where:** `Doc_03_Lexicon_Candidate_List.md` §4 should tag this claim with an explicit confidence level (e.g., Widely Accepted that a scholarly debate exists on this point; the debate's own resolution remains Contested) consistent with how confidence is handled everywhere else in this world's build, rather than leaving the CT candidate's own contest — the one place Article 26 governance applies — as the one unflagged assertion in the document.

---

### 7. [MEDIUM] Excommunication's Strand assignment (Geneva) is a defensible but unexamined judgment call against Doc_01 §5's own three named strand dimensions

**What was checked:** Doc_01 §5 grounds Strand Determination in three named dimensions — Practice, Authority structure, Formation emphasis. Excommunication is assigned Strand = Geneva.

**What was found:** the underlying doctrine of excommunication is discussed in Calvin's Institutes (Book IV, "Of the Discipline of the Church, Its Principal Use in Censures and Excommunication") in general, universal-church theological terms — not framed there as Geneva-specific. Doc_03's own one-line world-meaning ties the candidate specifically to "the Consistory's own most severe disciplinary tool" and "the specific authority Calvin fought to keep independent of the civil council (Doc_01 §5, the Perrinist crisis)" — i.e., it is Strand-tagged Geneva on the strength of a specific historical application (the Perrinist crisis), not on the strength of the doctrine itself being Zurich-absent.

**What's wrong and where:** this is a reasonable call given the corpus's own asymmetry (no vendored Zurich source discusses an analogous disciplinary conflict), but it is not clearly derived from Doc_01 §5's own three-dimension test the way the other Cluster 4 Strand assignments are (Consistory and Elder map cleanly onto the Authority-structure limb; Antistes onto no strand-crossing at all). Worth a one-line justification in revision rather than an implicit assumption that "the SC tag already covers the shared-doctrine reading, so Geneva-strand covers the historical-application reading" — that reasoning is never actually stated.

---

### 8. [LOW] Confession (of Faith)'s Strand assignment (Shared) is illustrated entirely by Zurich-sourced content

**What was checked:** the Confession (of Faith) candidate, tagged Strand = Shared.

**What was found:** its entire one-line world-meaning cites only the Second Helvetic Confession (Zurich, Bullinger, 1566) as "this world's own most mature example." No Geneva-side confessional document is cited (none is vendored — there is no Geneva Confession of 1536/37 in this corpus), so within this document's own evidentiary base, "Shared" is asserted as a genre-level claim about the wider Reformed tradition rather than demonstrated from this world's own two strands.

**What's wrong and where:** not necessarily incorrect (confessions as a genre plainly exist on both sides of the Reformed world generally), but as written the candidate's own grounding shows only Zurich content while being Strand-tagged Shared — worth a one-line acknowledgment that the Geneva-side confessional analog is not directly vendored, the same kind of disclosure the document does carefully elsewhere (e.g., for the Genevan Psalter).

---

### 9. [LOW] Imprecise quotation of the Consensus Tigurinus's ninth Head of Agreement

**What was checked:** the exact CT quotation in §4 (candidate: Sign and the Thing Signified): *"though we distinguish, as we ought, between the signs and the things signified, yet we do not disjoin"* them.

**What was found:** the actual text (the ninth Head of Agreement) reads: *"though we distinguish, as we ought, between the signs and the things signified, yet we do not disjoin the reality from the signs, but acknowledge that all who in faith embrace the promises..."* Doc_03's quotation is verbatim up to "disjoin," but then closes the quotation marks and appends its own word "them" outside the quote — which silently substitutes "the signs and the things signified [as a pair]" as the object of "disjoin," where the actual text's object is "the reality from the signs." The substantive point survives, but the appended "them" is not what the source says is being not-disjoined.

**What's wrong and where:** given this world's build history of exactly this defect (misattributed and mis-transcribed quotes), any truncated quotation that adds unquoted words changing the implied grammatical object should be avoided — either quote through "the reality from the signs" in full, or rephrase outside quotation marks entirely.

---

### 10. [COSMETIC] Candidate term name uses the singular ("Sign and the Thing Signified") against the CT's own plural heading

**What was checked:** the CT document's own ninth Head of Agreement heading: "THE SIGNS AND THE THINGS SIGNIFIED NOT DISJOINED BUT DISTINCT" (plural throughout). Doc_03's candidate term is singular.

**What was found:** the singular form is a defensible generalization to the standard theological shorthand for this doctrine, and is not itself a misquotation (the running quotation elsewhere is plural and accurate). Worth noting for Doc_06 so the eventual chunk file's Aliases field captures both forms.

---

## Positive findings (no defect — confirmed accurate)

- All 18 candidates' claimed textual grounding was independently checked and found substantively accurate, with the two exceptions above (Consistory/Elder characterization, Finding 4): Predestination, Election, and Providence are confirmed present in both Calvin's Institutes (heavily) and Zwingli's Selected Works (thinly), matching the stated AG-risk asymmetry exactly. Disputation and the Sixty-Seven Articles are confirmed at the cited location (`zwingli_selected-works_jackson1901.txt`, ~line 4485). Sola Scriptura's substance (not the Latin phrase, which is a modern label, correctly not claimed as a verbatim source phrase) is directly attested in the Sixty-Seven Articles' own preface. The Lord's Supper, Spiritual Presence, Memorial/Commemoration, and Mutual Consent are all grounded in the vendored Consensus Tigurinus and Institutes text. The CT document's title-page quotation ("the Ministers of the Church of Zurich" / "John Calvin, Minister of the Church of Geneva") is verbatim accurate. The "26 Heads of Agreement" claim is confirmed by direct count of the document's own numbered sections (I–26). Antistes is confirmed verbatim in the Schaff volume ("chief pastor (Antistes) at Zurich, Dec. 9, 1531"). Excommunication's textual presence (though not its Strand tag, see Finding 7) is confirmed (28 occurrences in Institutes Book IV). Catechism, Confession, and Reformation are all adequately grounded for candidate-list purposes.
- The disclosed exclusion of "Prophezei" is accurate: the term does not appear anywhere in `zwingli_selected-works_jackson1901.txt` or `zwingli_latin-works-correspondence-vol1_jackson1912.txt` (confirmed by direct search), and no equivalent English term is used consistently enough to ground a candidate — the document's own disclosure is honest and correctly reasoned.
- Doc_03 does **not** overclaim primary-text support anywhere for Consistory or Elder — if anything it under-claims (Finding 4) — and this specific failure mode (the one explicitly flagged as historically dangerous for this world) is avoided.
- The Strand column is, apart from Findings 7–8, well-grounded in Doc_01 §5's own three named dimensions (Practice, Authority structure, Formation emphasis) and the explicit "shared confessional core" list Doc_01 §5 itself states (predestination, sola scriptura, rejection of the Mass, the post-1549 spiritual Supper reading) — this is not an arbitrary or merely asserted column.
- The Author-Gravity concentration discussion in §2 correctly and thoroughly carries forward Doc_01 §8/Doc_02 §2's Calvin-concentration finding, correctly scopes it to the Sovereignty-of-God cluster plus Spiritual Presence and Excommunication, and correctly instructs Doc_04 to weight cross-strand convergence over corpus volume — this discharges the task's Author-Gravity check with only the Finding 4 nuance.
- The document does the Step 3 job and no more: it stays at one-line world-meanings and preliminary tier/tag/flag level throughout, explicitly declines to produce deployment chunks or full three-level entries (§0), and correctly defers Related-Terms reciprocity checks and the companion index to Doc_06/a later pass rather than fabricating them now.
- The five-level Article 17 confidence vocabulary and the Registry's separate A–E confidence scale are not conflated anywhere in this document — every reference to a Registry confidence letter is correctly labeled as a Registry citation (apart from the row-number errors in Finding 3), and Doc_02's own "Contested" finding is correctly distinguished from the Registry's D/E confidence tiers.

---

## Summary

Two fabricated/misattributed cross-references to Approved-to-proceed upstream documents (Doc_01 §5's non-existent Beza quotation, Doc_02 §8's non-existent Supper-emphasis "Contested" finding, the latter repeated twice) plus a three-times-repeated wrong Source Registry row number make this document unfit to proceed as written, despite otherwise-solid and independently-verified source grounding across all 18 candidates and a defensible Strand architecture.
