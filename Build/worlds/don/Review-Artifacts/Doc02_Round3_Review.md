# Doc_02 (Source Ecology) + Source Registry + Source Acquisition Manifest — Round 3 Independent Adversarial Review

**World:** Donatism (`don`)
**Documents reviewed:** `Doc_02_Source_Ecology.md`, `Source_Registry.md`, and `Source_Acquisition_Manifest.md` — all three read in full, together, as the co-equal Step 2 outputs they are.
**Reviewer:** independent adversarial review thread (Opus), 2026-09-01. This reviewer did not draft, and has no memory of drafting, any of the three documents, Round 1, or Round 2.
**Method:** every Round 1 and Round 2 finding was re-verified against the primary or governing source directly — never against the revised documents' own account of them, and never by accepting Round 1's or Round 2's own suggested fix wording, which this build's Decision Log records as a repeat source of new defects. Every quotation introduced or altered this revision was traced to its named source and checked character-by-character. The `git diff` between the Round-2-response commit (`9caf7bea`) and its predecessor (`4788e5c5`) was read in full so that new material could be separated from carried material. New defects were hunted independently, including in material neither prior round touched.
**Checked against:** `cic/texts/npnf104_augustine-anti-manichaean-anti-donatist.xml` (*On Baptism* Book I chs. 1–6 read in full; Prolegomena Chapter II read in full; *Contra litteras Petiliani* and the Felicianus/Prætextatus passages); `cic/texts/npnf101_augustine-confessions-letters.xml` (Letter XLIII read in full; Letter LXXXVII read in full; the complete div3 letter index enumerated); `cic/texts/optatus_against-the-donatists.txt` (Book I chs. XVI–XIX, the full apparatus notes 14.2, 41.2, 42.1, 49.1, 150.1, the book headings, the provenance header, and the Appendix Zenophilus material); `cic/texts/npnf102_...xml`; `cic/texts/README.md`; `cic/corpus-map/donatism.yaml` (all twelve entries, line by line); `Build/reference/L3B-World-Build-Methodology/Source_Registry_Template.md` V1.0; `CiC_L3B_Formation_World_Construction_Framework_V7.4.docx` Part II and Step 2 (extracted from `word/document.xml`); `CiC_L1_Constitution_V2_2.docx` Articles 20, 23, 26 (extracted); `Build/reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` (extracted); `Doc_01_World_Identification_Boundaries_Orientation.md` and `Step0_Movement_Scope_Confirmation.md` (both Approved to proceed); `don_Decision_Log.md`; the `cic-build-cycle` skill text in full; `Build/worlds/ijc/build/SOURCE-REQUEST-MANIFEST.md`, `Build/worlds/desert/build/SOURCE-REQUEST-MANIFEST.md`, `Build/worlds/desert/build/DECISION-LOG.md`, `Build/worlds/alx/build/SOURCE-REQUEST-MANIFEST.md`, and the `records/*/` search-record and source-record trees; `Build/worlds/ijc/Doc_02_Source_Ecology.md`; and a live egress test of the network claim.

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**3 high, 6 medium, 15 low.**

This is said first and plainly, because it matters for how the rest of this review is read: **this revision is a real, large improvement, and its single hardest task was done well.** Round 2's H2 — the Maximianist rebaptism-theology paragraph, which the prior draft built on a nineteenth-century précis it had also misread — has been rebuilt on Augustine's own vendored *On Baptism*. I opened `npnf104` and read Book I chapters 1 and 5 myself. Both quotations are character-exact, both are correctly located at I.1.2 and I.5.7, the who-asserts-what polarity is now right in both directions (Cresconius asserts the season-of-delay account; Augustine refutes it; the reception itself is common ground), the dropped refutation clause is restored and correctly attributed, and Registry rows 3 and 31 are re-scoped to match. That is the best single piece of work in this document's three-round history, and it should not be touched.

Twenty-four of Round 2's thirty-three findings are fully fixed, seven partially, two not at all. Round 2's only wholly-unfixed item (L2/L1, the `Doc_01 §3, B2` citation) is now fixed at both sites. Nothing on either prior round's "checks out clean" list was disturbed — I re-verified each item independently, including reading Letter LXXXVII in full to re-confirm row 6's Ep. 87 licensing constraint, which remains exactly right.

The verdict is nonetheless SUBSTANTIAL, and I have tested it hard against the brief's own caution about a third straight substantial round. It survives that test on three findings, each checkable in under a minute, each introduced or left standing by this revision:

1. **A negative claim about the evidentiary record, made in the discharge of a constitutional duty, that the vendored corpus refutes — again, in the same bullet, one round later.** §6 and Registry row 30 both report that the translator's "Ep. clxii" lead "cannot yet be run to ground" and that the second female actor it names "remains unidentified." She is in `npnf101`, in Augustine's Letter XLIII §26, which is one of the eleven letters in this Registry's own row 6. Row 30 records having grepped that very file. This is structurally the same failure as Round 1's H5.
2. **Eight new cross-references introduced this revision, all wrong** — five of them pointing at a Manifest section that does not exist, three of them pointing at a section that asserts the opposite rights posture from the row that cites it. The Manifest was correctly rebuilt on the project's own three-way split; the Registry was not re-pointed to match, and Doc_02 §1 now contradicts the Manifest outright about whether the *Gesta* is an acquisition request.
3. **A fabricated governance convention.** "G1" is glossed in the Manifest as a project-wide gate, and cited to `cic-build-cycle`. The skill contains no such term. The project's actual usage — in three other worlds' manifests, a Decision Log, and four search/source records — makes G1 the *first numbered item* in a world's own Source Request Manifest. This is the same failure class this world's Doc_01 Round 1 graded high ("G4 in this build's own launch process — no such gate exists"), and it entered in direct response to Round 2's L7 asking for a gloss.

The failure pattern `don_Decision_Log.md` names under "Standing process notes" has recurred, in its now-familiar shape: **every one of the three high findings sits at a point where a reviewer told the build thread to do something, and the build thread did it without opening the file that would have checked it.** Round 2 said "run the Ep. 162 lead to ground" → the lead was declared unrunnable. Round 2 said "restructure the Manifest" → it was restructured and nothing that points into it was updated. Round 2 said "give G1 a one-clause gloss and a pointer" → a gloss was invented and pointed at a skill that does not contain it. Round 2's own guidance predicted exactly this in its item 3, and it happened anyway.

None of the three requires research. All three are closed by opening a file that is already in the repository.

---

## What checks out clean

Stated at length, because most of this is now right and a fourth revision must not disturb it.

**Both prior rounds' clean lists survive intact.** I re-checked each item independently rather than carrying it forward:

- **Registry row 6's Ep. 87 licensing constraint.** I read Letter LXXXVII in `npnf101` in full. It is dated a.d. 405, to Emeritus. §6 is precisely the conciliar-authority reproach and names the Maximianists explicitly ("the council of the followers of Maximianus who were cut off from you… was of no authority against you, because their number was small compared with yours; and yet claim for your council an authority…"). "Maximian" occurs exactly once in the whole letter, in that section; §7–§8 concern the civil powers, Romans 13, and the emperors, and do not mention them. The row's positive licence and its negative constraint are both exactly right. **This remains the single best piece of discipline in the document set and must survive untouched.**
- **The 256-council double entry.** Row 10 (`anf05`, `role: antecedent`, `confidence: assigned`, Registry Confidence B) and row 11 (`npnf214`, `role: tradition`, `confidence: provisional`, Registry Confidence C, "not to be cited at row 10's confidence"), the a.d. 257 heading discrepancy recorded in row 11, §1's "kept distinct" paragraph, and the §9 item 6 forward watch — all present, all unchanged, all verified against `donatism.yaml` this session.
- **The Augustine letters split.** All eleven numerals still exact against the corpus map; the 168-letter volume claim independently confirmed (`grep -c 'type="Letter"'` on `npnf101` returns exactly 168); the div3 derivation, the eight-or-more Donatist-vocabulary cut, Letter LXXVI by its title's address, and the 2026-08-26 attribution all still exact.
- **The four five-dimension Author Gravity entries.** Optatus, Augustine, Petilian, Cyprian — twenty dimension headings across four entries, none missing. Petilian's Transmission History paragraph is unchanged and is still the sharpest paragraph in the document.
- **The Lucilla quotations and the I.16 citation.** Re-grepped and re-read: thirteen occurrences in the vendored Optatus; "XVI. The quarrel of Lucilla against Caecilian" exact; "the Schism, after the consecration of Caecilian, was effected at Carthage through a certain mischief-making woman named Lucilla" exact; "Majorinus, a member of the household of Lucilla — at her instigation, and through her bribes — was consecrated Bishop by Betrayers" exact. The Author Gravity reading built on them is correct and is a better discharge of Article 20 than the blank it replaced. **The core of this bullet must not be softened** — H2 below asks for it to be *extended*, not trimmed.
- **The two NPNF104 Prolegomena quotations**, as quotations, both re-verified verbatim, including the sentence that spans the p. 387 page break.

**H2 of Round 2 is fully and well fixed — verified against the primary text, not against the document's account of it.** In `npnf104`:
- *On Baptism* Book I, Chapter 1, §2 reads "For Felicianus,[note] when he separated himself from them with Maximianus, was not held by the Donatists themselves to have lost either the sacrament of baptism or the sacrament of conferring baptism. For now he is a recognized member of their own body, in company with those very men whom he baptized while he was separated from them in the schism of Maximianus." Doc_02 §1's quotation is exact; the ellipsis covers only a note marker; the citation "I.1.2" is correct.
- *On Baptism* Book I, Chapter 5, §7 reads "For the condemnation of the party of Maximianus, and their restoration after they had been condemned, together with those whom they had sacrilegiously, to use the language of their own Council, baptized in schism, settles the whole question in dispute, and removes all controversy… For as they themselves are obliged to confess that those whom Felicianus baptized in schism received true baptism, inasmuch as they now acknowledge them as members of their own body…" Doc_02's quotation is exact and its ellipses elide nothing that changes the sense; the citation "I.5.7" is correct.
- The Cresconius passage is now rendered with the correct polarity and with the refutation clause restored: "Augustin refutes the statement from its inherent contradictions and from the language of the Synod against the Maximianists" is verbatim, and Doc_02 attributes it to Augustine rather than absorbing it. Row 31 is correctly re-scoped to "**Not** the primary evidence for the reception itself."
- The *Psalmus* quotation "Why rebaptize us… when you do not repeat the rite upon your once expelled but now restored Maximianists?" is verbatim in the Prolegomena's *Psalmus* account, and the *Contra Cresconium* dating parenthetical ("four books, c. 406, 'some say as late as 409'") is exact against "wrote (406 A.D., some say as late as 409) *Contra Cresconium Grammaticum Partis Donati, libri IV*."

**The Manifest's three-way restructure is correct in its own terms, and its rights determinations all verify.** It now follows the shape `Build/worlds/ijc/build/SOURCE-REQUEST-MANIFEST.md` established: §1 open public-domain requests, §2 confirmed-unavailable-in-public-domain recorded-not-requested, §3 consultation-only never-vendored. **No in-copyright work is given a Destination filename**, and §2 says so explicitly in its own voice ("Nothing below gets a Destination filename"). Rights status verifies on every item: Burkitt 1894, Ziwsa CSEL 26 (1893), Mommsen/Meyer 1905, Migne PL 8, Petschenig CSEL 51–53 (1908–1910), and Monceaux IV–VI (1912–1922) are all public domain; Lancel SC 194/195/224/373 (Cerf, 1972–1991) and CCSL 149A (Brepols, 1974), Babcock (SBL 1989), Pharr (Princeton 1952, Lawbook Exchange reprints), Tilley TTH 24 (1996), and Maier TU 134/135 (1987/1989) are all in copyright. §2's closing sentence correctly distinguishes buying-or-consulting from vendoring. Round 2's L5, L6 and L15 are all fixed: Mommsen is now "two volumes (the first in two parts)," Migne is "compiled 1844," the two mechanical vendoring steps are named with the correct command (`python cic/engine/texts_registry.py --write-readme`, which I confirmed exists at that path), and the IJC precedent on Pharr is cited and quoted exactly.

**The network-access disclosure is honest and I independently corroborated it again.** A live `curl` to `archive.org/metadata/theodosianilibri02code` from this session returns `curl: (56) CONNECT tunnel failed, response 403`. The disclosure's instruction to open each link before treating rights status as final remains the right posture.

**The Discovery methodology note is honest, and it is the best new addition in this revision.** I verified that `records/don/` does not exist while `records/{alx,desert,fix,hal,ijc,pahc,syr}/` do. The note states plainly that no contemporaneous `search_record` was kept, that the Discovery column was reconstructed at drafting and revision time rather than logged as searches happened, that this is not the running record V7.4 describes, and that a future pass would have to open the directory going forward rather than back-fill. It does not overclaim a mechanical process, it does not claim completeness, and it names the specific project mechanism this world is not using. **This is exactly the disclosure Round 2's M15 asked for and it should be preserved verbatim.**

**The saturation statement is honest in the direction that matters.** It says the V7.4 field-bibliography sweep has **not** been run, that the recall and PRESS instruments are "a start on the required field-bibliography sweep, not a substitute for it," that no unproductive search is named because none was run as a dedicated sweep, and that the prior checks each closed "part of what the prior check found without closing all of it." I tested that last claim: Round 1's PRESS named Tilley, Maier and Lancel — all three now dispositioned (rows 35, 36, and Lancel named at row 14). Round 2's PRESS named Monceaux, Ziwsa and Petschenig — all three now rowed (40, 38, 39). Round 1's and Round 2's recall misses at Edwards and Tengström remain undispositioned. So "closing part, not all" is accurate, not a formula. Round 2's L8 is adequately discharged.

**Round 2's M1 (priority-review flags) is fixed, and the re-run holds up.** Rows 23, 24, 32 and 33 are added, exactly as Round 2 asked; row 26 (Brown) is removed with a stated reason that is correct on the trigger's own third conjunct (its licence already excludes vivid, specific claims, so the trigger cannot reach it); rows 30 and 31 are excluded with a correct reason (both verified directly this session, so not builder-prior-knowledge); the false claim that the trigger had been re-run "mechanically" is gone. Rows 32 and 33 no longer contradict their own Verification Notes.

**Round 2's M7 (the Frend thesis) is fixed, and fixed well.** §5 now separates the uncontroversial distributional claim from the contested explanation of it in one clean sentence ("This distribution is uncontroversial; the fuller account of *why* it holds is not"), names Frend's native-social-protest/Punic-substrate thesis as his, names Shaw and Brown as the standard correctives, marks its own Brown attribution as field knowledge rather than a re-read, declines to adjudicate, and §8 now carries the dispute under **Contested**. The substantive claim is also correct: Shaw's *Sacred Violence* and Brown's essays in *Religion and Society in the Age of Saint Augustine* are indeed the standard correctives to Frend's sociological reading. Rows 23 and 24 carry matching, correctly-scoped priority flags.

**Round 2's M8 is fixed.** The "Category 4" label is gone from §10, replaced with an accurate description of the corpus-map item as a process finding routed for census-level/System Hub correction. §9 item 7 and §9 item 8 are both now named and routed in §10.

**Round 2's M9, M10, M11, M12, M14, M15, M16 are all fixed.** Row 31 no longer presents "held valid" as a quotation and now quotes "the baptism of these was valid" correctly. Row 29's two mis-attributions are both corrected — I extracted the Step 0 Conclusion and confirmed that "one man's rigorist stance and irregular consecration as a rival bishop, rather than a broader community's own interpretive tradition" sits under "Excluded on the person-defined-movement ground (the new second criterion)," that "Real redundancy risk against Donatism" sits under "Possible future worlds… From this review cycle," and that the corpus map has no Novatian entry, so the orthodoxy judgment is correctly re-pointed at the Step 0 Conclusion. Doc_01 §7 item 6 is discharged via Manifest §1 item 5 (Petschenig). The Registry now follows the Manifest's honesty on the Gallica lead rather than the reverse, and both now describe it as a digitization of the Migne volume rather than a manuscript listing. The **Added** column is restored alongside Discovery. Row 37 exists for the *Psalmus*, closing the checkpoint gap.

**Round 2's M4, M5, M6 (wording half), L1–L6, L9, L12, L14, L15 are fixed.** §8's Inferential/Thin band now carries the Lucilla line, modelled on IJC's Justina line, exactly as Round 2's option (a) required. "carries Book VII" is gone and replaced with a claim the vendored apparatus actually supports — I checked notes 42.1 and 49.1 and confirmed the Siricius and Lucian/Claudian list additions, confirmed the file runs BOOK THE FIRST through BOOK THE SEVENTH and stops, and confirmed the translator's Preface is not in the vendored file (it is referred to three times and never present). Row 1's Verification Note now records all three divergent datings and the file's own translator-attribution caveat, both verbatim accurate against the provenance header. The Petilian chronology now reads "letters spanning the years around 400 — the first answered by Augustine's *Answer* Book I (c. 400), and a further reply from Petilian himself that occasioned Augustine's Book III (c. 401–402)," which is exactly what the Prolegomena supports ("He replied with one book to so much as he had received, c. 400 A.D.… Meanwhile Petilian responded to the first issue, and this necessitated a third book, c. 401 or 402 A.D."), with the false "specifically dated" gone. Row 13 now states `role: context`. Doc_02 §5 and row 28 now both cite Step0 §3 B2. §7's cross-reference now points to §3, which does rely on the distinction. The Maximian/Maximianus homonym is flagged in §4. Row 35 no longer quotes a chapter title it disclaims having checked. The *Passio Marculi* dating is now attributed to Frend (row 23).

**The corpus map is still represented accurately.** All twelve entries still have a corresponding row; every `role:` and `confidence:` string quoted in a Verification Note still matches `donatism.yaml` character-for-character; the internal `context`/`tradition` inconsistency on the letters cluster is still disclosed in §1, row 6, §9 item 7 and §10, and still correctly refused as something this build thread may fix.

**Article 20, Article 23 and Article 26 are all still quoted correctly**, verified against the extracted Constitution this session, as are the Framework's three bounding conditions and the against-the-grain "specific textual trace" requirement.

---

## HIGH

### H1. The second woman in the "Ep. clxii" lead is not unidentified. She is in Augustine's Letter XLIII §26 — vendored in `npnf101`, and one of the eleven letters in this Registry's own row 6. Two documents assert a false evidentiary absence in the discharge of Article 20, one grep away from the search row 30 records having run.

**Doc_02 §6, Gender bullet:**

> "This is a second, currently unidentified female actor inside this world's own internal history, flagged here for Doc_09's Story Inventory rather than pursued further in this pass. **The citation cannot yet be run to ground:** the number does not match any letter in the vendored NPNF corpus carrying that content…"

**Registry row 30:** "…so the letter this second lead actually points to **remains unidentified**. It is not simply absent from the vendored corpus; **it has not yet been found there under its own name**."

**Doc_02 §9 item 5** carries it forward as an open item "once that citation's own numbering can be reconciled with the vendored corpus."

It has been found. The vendored `npnf101` contains, at Letter XLIII (a.d. 397, "To Glorius, Eleusius, the Two Felixes, Grammaticus"), §26:

> "Let them at last become sensible of what they have done; for in the lapse of years, by a just retribution, their work has recoiled upon themselves. **Ask by what woman's instigation Maximianus** (said to be a kinsman of Donatus) **withdrew himself from the communion of Primianus**, and how, having gathered a faction of bishops, he pronounced sentence against Primianus in his absence, and had himself ordained as a rival bishop in his place,—precisely as Majorinus, under the influence of Lucilla, assembled a faction of bishops, and, having condemned Cæcilianus in his absence, was ordained bishop in opposition to him."

and, four sentences later:

> "…that you give no more weight to the Council of Secundus of Tigisis, **which Lucilla stirred up against Cæcilianus** when absent… than you give to the Council of Maximianus, **which in like manner some other woman stirred up against Primianus** when absent, and against the rest of the multitude throughout Africa which was in communion with him."

That is, precisely and completely, what Vassall-Phillips's note reports: "a woman like Lucilla was subsequently the cause of a schism within a schism — of a later schism amongst the Donatists themselves." Augustine draws the Lucilla parallel himself, in those words, in the same paragraph.

**The identification is not a guess — it converges three ways.** The translator cites "Ep. clxii" three times in the vendored file, and all three contents land in Letter XLIII:

| Apparatus note | What it cites "Ep. clxii" for | Where it is in Letter XLIII |
|---|---|---|
| 150.1 (on I.16) | a woman like Lucilla causing a later schism among the Donatists | §26, quoted above |
| 41.2 (Appendix, on the 400 *folles*) | "Cf. Optatus i, 16; cf. S. Aug. Ep. clxii; con. Parmen. i, 3" | the three "money of Lucilla" passages, incl. "Lucilla, a very wealthy woman, whom he had offended" |
| 14.2 (on *purgare*) | Augustine's use of *purgare* for the purgation of Felix | the Felix of Aptunga material — "the case of Felix of Aptunga was not forgotten, and he too was acquitted… after an investigation by the proconsul" |

Vassall-Phillips is citing Augustine's letters in an older (pre-Maurist) numbering in which the letter NPNF prints as XLIII carried the number 162. Whether or not the build thread wants to assert that numbering equivalence formally, **the content is found, in a vendored file, in a letter this Registry already rows as Native, Type P (row 6).**

**Why this is high, and why it is the most serious finding in this review:**

**(a) It is a false assertion of evidentiary absence in the discharge of a constitutional duty** — the same defect, in the same bullet, that Round 1 graded as its most serious finding (H5). Article 20's primary duty is "making structural absence visible… name whose voices the sources structurally omit, why they are omitted, and what that omission means." Reporting a woman as unreachable when a vendored Native source attests her does not under-perform the duty; it misstates the record in the participant-facing direction the Article governs.

**(b) It forecloses a second against-the-grain trace of exactly the kind §6's own reasoning identifies.** The bullet's best sentence is its Author Gravity point: "a hostile source that needs a woman's real agency and standing… in order to make its own accusation land is a specific against-the-grain textual trace, not an absence." That argument applies with *equal* force to Letter XLIII §26 — Augustine's whole rhetorical move requires that a woman really did have the standing to stir up a council of bishops against a sitting primate, and requires his Donatist readers to grant it. She is anonymous in the source, which is itself the finding: the founding schism's woman is named and the internal schism's woman is not, in the same paragraph, by the same hostile author. That is a sharper Article 20 observation than either the blank Round 1 found or the unrunnable lead this draft reports.

**(c) The check was one command, and row 30 records having run it.** Row 30's Discovery column reads "direct text search / grep against `cic/texts/optatus_against-the-donatists.txt` **and** `cic/texts/npnf101_augustine-confessions-letters.xml`," and its Verification Note reports "**7 occurrences**" of Lucilla in `npnf101`. All seven of those occurrences are inside Letter XLIII. The row counted the hits and did not read them.

**(d) It sends a closed question forward to Doc_09 as an open one**, and it leaves row 6 licensed only for "Broader Donatist–Caecilianist exchange" when a second, specific licence is now available.

**Fix.**
1. In §6, replace "The citation cannot yet be run to ground…" with the finding: the content the apparatus points to is Augustine's Letter XLIII §26 (`npnf101`, Registry row 6), which reports both that Maximian withdrew from Primian's communion at a woman's instigation and that "some other woman stirred up" the Council of Maximianus against Primian — so the "later schism amongst the Donatists themselves" is the Maximianist schism on Augustine's own testimony, not on inference, and the second female actor is attested but unnamed. Note the older/Maurist numbering divergence as the explanation for "clxii," at the confidence the evidence supports (the three-way content convergence above), without asserting a formal concordance the build has not checked.
2. Extend the Author Gravity reading, do not merely record the fact: the asymmetry between a *named* Lucilla and an *unnamed* second woman, in the same Augustinian paragraph, is itself the structural-absence finding Article 20 asks for.
3. Add to row 6 a second, specific licence for Letter XLIII §26 on this point, and to row 30 the corrected verification trail. Consider whether §8's Inferential/Thin band needs a line for the second woman parallel to the Lucilla line.
4. Correct §9 item 5: the lead is closed as to content; what remains open is her identity, which the sources do not supply.
5. Note the incidental gain: Letter XLIII is dated a.d. 397 in the vendored volume, which places this testimony within a few years of the Maximianist reception §1 reconstructs — a firmer datum than the current forward-flag.

---

### H2. Eight Manifest cross-references were added to the Registry this revision and all eight are wrong — five point at a section that does not exist, three invert the acquisition posture of the row that cites them — and Doc_02 §1 now contradicts the Manifest outright about the *Gesta*.

The Manifest's restructure (Round 2's H1) was done correctly. What was not done is the propagation. `git diff 4788e5c5 9caf7bea` shows that the old Registry carried bare `Source_Acquisition_Manifest.md` references with no section numbers; **this revision added section numbers to eleven of them**, against the *old* Manifest's per-item numbering (item 1 = *Gesta*, 2 = Tyconius, 3 = CTh, 4 = Passiones, 5 = supporting works) rather than the new categorical one.

The Manifest now has exactly three numbered sections: §1 OPEN requests (public domain), §2 Confirmed unavailable in public domain, §3 Consultation-only secondary scholarship. **There is no §4.**

| Row | Points to | Where the work actually is | Effect |
|---|---|---|---|
| 14 (*Gesta*) | §3 | §2 | §3 is "Consultation-only **secondary scholarship**" — the *Gesta* is a primary conciliar record |
| 15 (Tyconius) | §2 | §1 | **Inverted.** Row says "public-domain Latin edition… identified as a real acquisition candidate"; §2 is "Confirmed unavailable in public domain" |
| 16 (CTh 16) | §3 | §1 | **Inverted.** Row says "public-domain Latin critical edition identified"; §3 is "never vendored" |
| 17 (*C. Cresconium*) | §4 | §1 | Section does not exist |
| 18 (*C. ep. Parmeniani*) | §4 | §1 | Section does not exist |
| 19 (*Passio Marculi*) | §4 | §1 | Section does not exist |
| 35 (Tilley TTH 24) | §4 | §2 | Section does not exist |
| 36 (Maier) | §4 | §2 | Section does not exist |
| 38, 39, 40 | §1 | §1 | Correct — the three rows added this revision |

And in Doc_02 §1, of the *Gesta* and the *Codex Theodosianus* Book 16:

> "**Both are flagged for Source Acquisition in the accompanying manifest.**"

The Manifest says the opposite of half of that. Its §2, where the *Gesta* sits, opens: "These are named for completeness and **to close off the temptation to reach for them, not as things to acquire.**" The *Gesta* is the source Doc_02 §1 itself calls load-bearing and row 14 licenses for "Donatist bishops' own recorded words at length" — and the two co-equal Step 2 outputs now disagree, in plain language, about whether it is being requested.

**Why this is high and not a formatting nit.** `cic-build-cycle` names this failure by name under *Naming and term propagation*: "Whenever a name or term changes, check every file it appears in… A fix that lands in the narrative document without the index being updated to match is not a complete fix." The Registry is the artifact downstream steps read; the Manifest is the artifact that reaches a person. Three of these pointers tell a reader the opposite of the row's own rights determination, on the exact axis Round 2's H1 existed to repair; five send a reader to nothing at all; and one contradiction sits in Doc_02's own §1 prose rather than in a pointer. A revision that fixed the rights posture in one document and left the other three sites asserting the pre-fix posture has fixed the paragraph, not the finding.

**Fix.** Re-point all eight (14→§2, 15→§1, 16→§1, 17→§1, 18→§1, 19→§1, 35→§2, 36→§2), and correct Doc_02 §1 to state what the Manifest actually concludes: the *Codex Theodosianus* Book 16 is an open public-domain acquisition request (Manifest §1 item 3), while the *Gesta* is recorded as confirmed unavailable in the public domain and not requested (Manifest §2), with the consequence Round 2 already named — no vendored text, Emeritus's recorded words unavailable for quotation, and §1's claim about them standing at referenced-only until that changes. Then re-read every remaining cross-reference in all three documents against its target, rather than against a memory of what the target used to be.

---

### H3. "G1" is glossed as a project-wide gate and cited to `cic-build-cycle`. The skill does not contain the term, and the project's own usage in three other worlds makes G1 the first numbered *item* in a world's Source Request Manifest, not a gate.

**Manifest, decision block:**

> "'G1' is this project's own shorthand for **the source-acquisition decision point in a world's build** — the moment a Source Acquisition Manifest like this one is put to the project lead for a real choice, distinct from the procedural self-dispositions the build thread makes on its own (**`cic-build-cycle`**; see also `Build/worlds/desert/build/records/search_record/desert.search.apophthegmata-pd-english.md` for the same usage in another world's build)."

**(a) The cited governing document does not contain the term.** I read `cic-build-cycle`'s SKILL.md in full and searched it. "G1" does not appear anywhere in it — not in the five stages, not in the escalation categories, not in the disposition vocabulary. The distinction the sentence draws (project-lead decisions vs. build-thread self-disposition) *is* in the skill; the label G1 is not, and the citation as placed reads as sourcing the definition.

**(b) The definition is wrong against the project's own usage.** `Build/worlds/desert/build/SOURCE-REQUEST-MANIFEST.md` §3 reads:

> "### G1 — Budge, *The Paradise or Garden of the Holy Fathers* (1907), vols. 1–2 — **P1**"
> "### G2 — consult-only acquisitions (decision, not download) — **P2**"

`Build/worlds/alx/build/SOURCE-REQUEST-MANIFEST.md` runs **G1–G5** as a numbered gap table ("**G1** | `alx.search.stromateis-iii-english`…"). `Build/worlds/desert/build/DECISION-LOG.md` reads "Open items for Mark (manifest): **G1** — Budge… **G2** — confirm consult-only availability." Four `records/` files use it the same way ("manifest G1, priority P1"; "requested from Mark alongside vol. 2 (manifest G1)"; "manifest request G1 is FULFILLED").

**G1 is Gap/Request #1 within one world's own manifest.** It is not a gate, not a decision point, and not project-wide. Under the real convention, the Donatism Manifest's six §1 items would be G1–G6 — which is why its own decision block reads oddly: it says "For each of the **six items** in §1: acquire, decline, or defer," under a heading that names only "G1."

**(c) It is propagated into three places and load-bearing in one of them.** Doc_02's header ("the project lead's G1 decision"), §9 item 1 ("for the project lead's decision at G1"), and §10 ("**G1 is the route already provided for it**") — where it is doing work inside the escalation-category assessment, the one paragraph in the document that governs whether it may be self-disposed at all. Doc_02 gives no gloss and no pointer; the only definition in the document set is the wrong one.

**Why this is high.** This world's own Doc_01 Round 1 graded a fabricated governance artifact as one of four high findings, in the Decision Log's own words: "a fabricated governance citation ('G4 in this build's own launch process' — no such gate exists)." This is the same artifact type, in the same world, in the document that goes to the project lead, with a citation to a governing document that does not support it — and it entered as the direct response to Round 2's L7 asking for "a one-clause gloss and a pointer." The gloss was invented rather than looked up, though four files in the repository define the convention by use.

**Fix.** Either (a) adopt the project's actual convention — number the §1 items G1–G6 and say so, matching `Build/worlds/desert/build` and `Build/worlds/alx/build`, with Doc_02 referring to "the Manifest's G-items" rather than "G1" as a gate — or (b) drop the label from all four sites and say plainly what is meant: the Manifest is put to the project lead for an acquisition decision, distinct from the procedural self-dispositions the build thread makes on its own (`cic-build-cycle`, *Disposition*). Do not cite `cic-build-cycle` for the label either way. Do not invent a third convention.

---

## MEDIUM

### M1. Registry row 15 and Manifest item 1 both point at "row 38" for the Burkitt edition. Row 38 is Ziwsa's Optatus. Burkitt 1894 — the top item on the acquisition list, with a Destination filename and three URLs — has no Registry row at all.

**Row 15:** "Public-domain Latin edition (**Burkitt 1894**, row 15 remains the work-level entry; **see row 38 for the edition**)…"
**Manifest §1 item 1** (Burkitt): "**Registry rows 15, 38.**"

Row 38 is "Karl Ziwsa (ed.), *S. Optati Milevitani libri VII*, CSEL 26 (Vienna: Tempsky, 1893)" — a different editor, a different author, a different work, a different century of scholarship. Manifest item 2 (Ziwsa) also cites row 38, correctly, so the same row is claimed by two different editions one item apart.

This is not only a bad pointer. This revision added Registry rows for four newly-named editions — Ziwsa (38), Petschenig (39), Monceaux (40), and earlier Tilley (35) and Maier (36) — establishing the practice that a named edition gets a row. **Burkitt is the one §1 item that is fully actionable** (public domain, three located Internet Archive identifiers, a Destination filename) and it is the one that did not get one. A project lead who acquires it has nowhere in the Registry to record its arrival, and row 15 will still say "not currently vendored" with a pointer to somebody else's book.

**Fix.** Add a row for Burkitt 1894 (P, B, Native, licensed as the critical Latin edition attaching to row 15's work, Verification Note recording that the bibliographic record was cross-checked but the volume not opened), and re-point row 15 and Manifest item 1 to it.

---

### M2. Registry row 37 dates the *Psalmus contra Partem Donati* to "c. 393 per the Prolegomena's own dating." The Prolegomena gives no date for it — and c. 393 is incompatible with the one thing the row is licensed for.

**Row 37:** "Augustine, *Psalmus contra Partem Donati* (Abecedarian psalm, **c. 393 per the Prolegomena's own dating**; not independently re-verified)… Licensed For: **Earliest attested use of the Maximianist-reception argument** in rhetorical form, cited in Doc_02 §1 as pre-dating *Contra Cresconium*."

**(a) The attribution is to something the source does not say.** I read the Prolegomena's *Psalmus* paragraph and its neighbours. Chapter II states it is arranged "so far as may be, in chronological order, following the dates suggested by the Benedictine edition," and it places the *Psalmus* between the Hippo council of 393 and a work "answered… during the year 393," then moves on with "We pass to the period of his co-bishopric with the aged Valerius, which dates from 395 A.D." **No date is stated for the *Psalmus* anywhere.** c. 393 is an inference from position. Presenting it as "the Prolegomena's own dating" makes an inference into an attested date — the identical move Round 2's M6 found and the revision corrected two sentences away in the same document ("specifically dated to c. 398–400").

**(b) The date contradicts the content the row exists to license.** The quotation Doc_02 §1 draws from the *Psalmus* is "Why rebaptize us… when you do not repeat the rite upon your **once expelled but now restored Maximianists**?" The Maximianists were not restored in 393. On the vendored file's own endnote to *On Baptism* I.1.2: the Cabarsussa synod was convened in 393; Bagai condemned them in 394; "the larger fraction… was **subsequently** forced into reunion" — the reception of Felicianus and Prætextatus that Doc_02 §1 reconstructs, conventionally c. 397. A psalm of c. 393 cannot refer to a restoration that had not happened, and the Prolegomena's own narrative notes only that Augustine's presbyterate was "a time marked in Donatist annals by the Maximianist **separation**."

The load-bearing half of Doc_02 §1's use — that the argument predates *Contra Cresconium* (406) — survives either way. It is the Registry's dating and its attribution that fail.

**Fix.** Either drop the date ("dated to Augustine's presbyterate on the Prolegomena's own chronological arrangement, which supplies no explicit date; the Maximianist reference requires a date after the reception of Felicianus, c. 397, and the tension is noted rather than resolved"), or state the tension explicitly and flag the row for priority review. Do not carry a date the source does not give against content the date excludes.

---

### M3. Rows 30 and 31 correctly moved to Confidence A — but rows 3 and 6 now describe direct session verification of the exact loci they license while sitting at B, and the distinguishing rule Round 2 asked to be stated once is not stated.

The Template: "**A** — Verified this session against an accessible primary source, translation, or authoritative reference. **B** — Specific work/locus named, not independently re-checked this session."

Rows 30 and 31 are now A, and that is right — both were verified directly this session and both say so.

But this revision also rewrote rows 3 and 6 to record direct session verification, and left them at B:

- **Row 3**, Licensed For: "the Maximianist rebaptism-consistency argument, **quoted directly at Book I chapter 1 §2 and chapter 5 §7**"; Verification Note: "**Book I chs. 1 and 5 directly read and quoted this session**"; Discovery: "direct text search / grep and read against `cic/texts/npnf104…`". Confidence **B**.
- **Row 6**: "Letter LXXXVII **read in full this session** and confirmed to name the Maximianists explicitly." Confidence **B**.

Row 3 is the row on which this entire revision's best work rests. A downstream builder reading its Confidence letter is told the material was "not independently re-checked this session"; the same row's Verification Note tells them it was. Two fields of the most load-bearing row in the Registry now contradict each other.

There is a coherent rule available — A when the *specific licensed thing* was fully verified, B when the licensed work as a whole was not re-collated — but under it, row 3's licence *is* the specific verified thing, so it should be A, not B. Round 2's M2 anticipated this precisely: "If the build thread's reasoning is that A requires re-collating a whole work rather than a specific locus, say so once in a note rather than encoding it silently in every row." No such note was added, and the calibration is now internally inconsistent rather than merely conservative.

**Fix.** State the rule once, in a note above or below the table, and apply it consistently. Whichever rule is chosen, rows 3, 6, 30 and 31 must land in the same place as each other for the same reason.

---

### M4. Registry row 30's Verification Note asserts a check against "the NPNF-numbered Letter CLXII **in the vendored `npnf101`**." That letter is not in the volume. Round 2's L13 asked for the opposite disclosure and the fix inverted it.

I enumerated the volume's own letter index: the `div3 … type="Letter"` sequence runs `…CLI, CLVIII, CLIX, **CLXIII**, CLXIV, CLXV…`. There is no `n="CLXII"`. The volume contains 168 letters and Letter CLXII is not among them.

What *is* in the file is an endnote to Letter CXXXVII, which says so in the editor's own words: "This sentence having been misunderstood by Bishop Evodius, who quotes and comments upon it in Letter CLXI. Augustin, in replying **in Letter CLXII.**, writes a few sentences, which, **as the letters then exchanged with Evodius have been omitted in this selection**, we here insert:—" followed by an excerpt marked "(Letter CLXII. sec. 6, 7)."

So the row's substantive conclusion is right — the NPNF Letter CLXII is Augustine's reply to Evodius, and the excerpt concerns the virgin birth and the nature of miracle, with no bearing on Lucilla or any schism. But the Verification Note — the field whose entire job is "what was checked, when, against what" — describes a check against a letter in a volume that does not contain it, without disclosing that the whole basis is two sections quoted inside a footnote to a different letter. Round 2's L13 asked for exactly the inverse statement: "add to row 30 that Letter 162 is absent from the vendored NPNF101 selection." The revision asserted its presence instead.

(Doc_02 §6's own wording — "the number does not match any letter in the vendored NPNF corpus carrying that content" — is defensible as written; this is a Registry-only defect. Both are superseded in substance by H1 above.)

**Fix.** Record what was actually available: NPNF omits Letters CLX–CLXII from its selection; §§6–7 of Letter CLXII survive in the volume only as an editorial insertion in an endnote to Letter CXXXVII, and that excerpt concerns the virgin birth. Then fold in H1's finding, which supersedes the negative claim entirely.

---

### M5. §10's escalation-category assessment over-triggers Category 2, tests the wrong condition in its own opening sentence, and is not compatible with the self-disposition the same section plans.

**Doc_02 §10:**

> "**none of the three documents decides a new portfolio-level or cross-world question on the grounds of this world's own ecology.** … The Manifest puts an acquisition and rights-posture decision to the project lead — a decision made for reasons external to this world's own ecology (the project's public-domain-only vendoring policy) — **which is exactly the kind of choice this category exists to route to him** rather than settle internally; it is labeled as such here rather than left implicit, and G1 is the route already provided for it."

**(a) The opening sentence tests the wrong condition.** The category is "anything decided **for a reason external to this specific world's own ecology**." Denying that any document "decides a portfolio-level question **on the grounds of this world's own ecology**" denies something the category does not cover — by definition a portfolio-level decision is not made on this world's ecological grounds. As written the sentence clears a bar nobody set.

**(b) On the substance, the category does not apply, and Round 2 was wrong to suggest it does.** The Manifest decides nothing portfolio-level. The public-domain-only rule is already decided, in `cic/texts/README.md`; the Manifest *applies* it. What it asks the project lead is an ordinary per-world operational acquisition question, which is what a Source Request Manifest is for — and the project has run exactly this three times before (`worlds/{desert,alx,ijc}/SOURCE-REQUEST-MANIFEST.md`) without treating the world's Step 2 output as un-disposable in consequence. A decision *governed by* an already-settled cross-world policy is not the same thing as a decision *made* for reasons external to the world's ecology.

**(c) As written, the label and the disposition are incompatible** — the same conflict Round 2's M8 found at Category 4 and the build thread corrected there, reproduced one paragraph earlier at Category 2. `cic-build-cycle`: "Before disposing of any document, check it against these four categories. **If any apply, stop and escalate directly to the project lead — do not self-dispose, regardless of how clean the review came back.**" §10 says the Manifest is "exactly the kind of choice this category exists to route to him," and then closes "Pending independent adversarial review **before self-disposition**." Both cannot stand.

**Fix.** Rewrite the paragraph to test the category's own condition and reach the answer the project's own precedent supports: the Manifest applies the project's already-settled public-domain-only rule and puts a routine per-world acquisition choice to the project lead through the ordinary manifest route; it does not decide a portfolio-level question, and Category 2 is not triggered. Keep the labeling instinct — the category does require that any genuinely portfolio-level item be labeled as such — but do not label something as triggering a category and then self-dispose over it. See the independent escalation assessment below, which reaches this conclusion separately.

---

### M6. Rows 35, 36 and 40 write acquisition status into the Licensed-For field instead of a licensing target — the same defect Round 1's M6 required fixing at row 21, and against the pattern the same file applies correctly at rows 14–18.

The Template is explicit twice: "**Licensed For** *(required if Native…)* — The specific gravity, force, lexicon term, or Representative trait this source justifies. **A Native source with nothing named here is not yet usable downstream**," and "For anything Native, name its Licensed-For target before moving on. A source without one is not finished being processed."

- **Row 35** (Tilley TTH 24), Licensed For: "**Not currently vendored.** Reported to be the standard English edition covering rows 19, 20, and 22… Confirmed unavailable in the public domain (recorded not requested)."
- **Row 36** (Maier), Licensed For: "**Not currently vendored.** Reported to be the standard collected documentary dossier… Confirmed unavailable in the public domain (recorded not requested)."
- **Row 40** (Monceaux, new this revision), Licensed For: "**Not currently vendored.** Standard older literary history of Donatism, reported to print the Donatist documentary and martyr-narrative corpus… — see `Source_Acquisition_Manifest.md` §1."

None names a licensing target. All three place vendoring/rights status — which belongs in the Verification Note, where rows 14, 15, 16, 17, 18 and 19 correctly put it — in the field reserved for what the source justifies. Round 1's M6 required this exact correction at row 21, and the fix there is the right model: row 21 now reads "**Not yet licensed** — chronological/genealogical content only; no claim in this document's own build rests on this source yet; use to be determined at Doc_09."

**Fix.** Move the status text into each row's Verification Note and either name a licensing target or write "Not yet licensed" on row 21's own pattern. This is the field Doc_03 and every step after it reads to decide what may be drawn on.

---

## LOW

**L1. The Registry's `Added` column now carries review-round labels — the standing clean-documents rule's own prohibited form.** Rows 30–36 read "2026-09-01, `don` build thread (**Round 1 revision**)"; rows 37–40 read "(**Round 2 revision**)." `don_Decision_Log.md`: "the construction documents themselves stay clean, substantive content — **no inline revision annotations, no 'corrected in vN' markers, no review-round commentary** woven into the analysis." I record the genuine tension: Round 2's M14 asked that the append be made visible, and the Template defines `Added` as provenance metadata, so *some* distinguishing mark is legitimate. A neutral one — "second pass," "third pass," or simply a distinct timestamp — discharges M14 without naming a review round. Note also that Round 2's M13 instance 4 is only half fixed: the saturation statement still opens "This Registry **closes this revision pass**."

**L2. The saturation statement's internal contradiction survives, verbatim.** It opens "This Registry closes this revision pass on the sources identified…" and closes "This is **not yet closed** with a saturation statement in the full Construction Framework V7.4 sense." Round 2 named this as "a small internal contradiction worth removing." It was not removed.

**L3. Row 40 reintroduces the "P/S" hybrid Type that rows 35 and 36 were corrected away from in the same revision.** Round 2's L11 recorded the hybrid as an inconsistency with sibling practice (IJC: "Rows 18–21 use Type **P**… not a hybrid 'P/S' code"). Rows 35 and 36 are now P; row 40, a structurally identical case (a modern scholarly volume that prints primary texts), is P/S. Whatever the right answer, the Registry should not hold both within four rows of each other.

**L4. Doc_02 §1's "secured state assistance to suppress it" is uncited, in a document whose Registry carries an explicit constraint against a near-identical claim.** Row 6 licenses Letter LXXXVII expressly *not* for "a claim that the proconsular machinery was invoked specifically against them." The claim is well-supported in the vendored corpus — the Prolegomena's Ep. 70 summary ("the state was called upon to enforce his ejection," row 31) and *Contra litteras Petiliani* ("Optatus Gildonianus advancing with a military force… sucking back Felicianus and Prætextatus once again within their pale"; "whether Optatus did not compel him against his will to return to your communion," row 4) — and naming one of them costs a clause and puts the claim inside the Registry.

**L5. Doc_02 §1 attributes the "season of delay" to "the Council of Bagai."** The Prolegomena says only "**The Synod** had granted a season of delay." The identification is very probably right (the next clause is "the language of the Synod against the Maximianists," and the vendored endnote fixes that as Bagai, 24 April 394), but it is an inference presented inside the sentence that introduces the quotation, where it reads as the source's own words.

**L6. Doc_02 §1's gloss narrows and blurs the summary's claim.** "so that **the returning clergy's** baptism 'was valid'" — the source says "The Synod had granted a season of delay during which **all who returned** should be held innocent… **the baptism of these** was valid." Two small losses: "all who returned" is narrowed to clergy, and the distinction row 3's primary text keeps sharp (the clergy's own baptism versus the baptisms they *conferred*, which is the point at issue) is blurred.

**L7. Row 20 says the *Passio Isaac et Maximiani* has the "Same PL8 location… as row 19."** Row 19 locates the *Passio Marculi* at PL 8, cols. 760–766. The two texts share a volume, not a location. "Same volume and access status" is the accurate phrase.

**L8. Doc_02 §9 item 1's list of the Manifest's subjects omits two of the Manifest's six §1 items** — Ziwsa's CSEL 26 Optatus and Monceaux — both newly added this revision, both public-domain acquisition candidates.

**L9. The Manifest silently elides inside its quotation of the corpus README.** It renders "In-copyright editions are referenced by `source` record and never vendored"; the README reads "In-copyright editions **(Holmes 2007, Ward 1975)** are referenced by…". The elision changes nothing substantive, but this is a document that quotes a rule in order to bind itself to it.

**L10. Round 2's L10 (the Maximian homonym) is discharged in Doc_02 only.** The Registry's rows 17, 18 and 20 carry no cross-warning, and the Comparandum-Note apparatus exists for exactly this hazard. Doc_03 and Doc_09 read the Registry.

**L11. Edwards (TTH 27, 1997) and Tengström (1964) remain undispositioned** after being named by two prior rounds' coverage instruments. V7.4: "every named work is dispositioned — rowed, or excluded with a reason." Babcock is now dispositioned in Manifest §2 and Lancel at row 14, so the practice exists; these two were missed.

**L12. §2 presents the Lucian/Claudian addition as evidence where the apparatus hedges it.** Note 49.1 reads "he **evidently** added in his second edition the names of Lucian and Claudian"; note 42.1 states the Siricius addition flatly. Doc_02 §2 gives both as "the evidence of." A one-word hedge restores the distinction — the same class of loss Round 1's L7 flagged on the Tyconius condemnation.

**L13. The priority-review flag section names what it flagged and explains two exclusions, but says nothing about eleven other builder-prior-knowledge rows it silently releases** — 14, 15, 16, 17, 18, 34, 35, 36, 38, 39 (and, differently, 37). Round 2's M1 asked for "naming which rows were considered and released and why." The release is probably right in every case (none currently licenses a vivid, specific claim), but a one-sentence statement of that reasoning is what makes the trigger auditable rather than assertable.

**L14. Doc_02's two named governing instruments give different priority-review triggers, and the divergence is not noted.** V7.4 Step 2: "Flag entries resting at **Confidence C or below** that are intended to support a vivid, specific claim." Source Registry Template V1.0 (re-keyed 2026-08-05): flag on `discovery_channel: builder-prior-knowledge` + `verification_state` + `evidentiary_weight`. The Registry applies the Template's, which is the later instrument and the right choice — but under V7.4's own text, row 12 (Petilian's letters, Confidence C, licensed as "this world's own fullest surviving primary voice") would flag and does not. A sentence saying which trigger is applied and why closes it.

**L15. Doc_02 uses "G1" three times with no gloss and no pointer.** The only definition is in the Manifest, and it is wrong (H3). Whatever replaces it, Doc_02 should carry a clause or a pointer rather than a bare label in its header, §9 and §10.

---

## Round 1 disposition table (carried forward)

Round 1's body carries 34 findings (H1–H5, M1–M16, L1–L13). Status as of this revision:

| Round 1 | Status now | Note |
|---|---|---|
| H1 (eighth book) | **Fixed** | Error gone; Round 2's residue ("carries Book VII") also gone; apparatus notes 42.1/49.1 verified this session |
| H2 (Homoian import) | **Fixed** | No residue; §6's only IJC comparison is accurate and attributed |
| H3 (missing manifest) | **Fixed** | Manifest exists and is correctly structured — but nothing pointing into it was updated (R3 H1) |
| H4 (Maximianist binding) | **Fixed** | Discharged from vendored *On Baptism* I.1.2 / I.5.7, verified this session |
| H5 (Lucilla) | **Partial** | Core fixed and excellent; the second lead now carries a false absence claim (R3 H1) |
| M1 (Doc_01 §2 A5 ×5) | **Fixed** | |
| M2 (Doc_01 §7 item 8) | **Fixed** | |
| M3 (row 13 citation) | **Fixed** | |
| M4 (row 12 qualifier) | **Fixed** | |
| M5 (three missing rows) | **Fixed** | Rows 32, 33, 34 |
| M6 (row 21 licence) | **Fixed** | And is the model rows 35/36/40 should follow — R3 M6 |
| M7 (rows 19–21 at D) | **Fixed** | |
| M8 (row 29 confidence/note) | **Fixed** | |
| M9 (row 29 reasoning) | **Fixed** | (b)(c)(d) fixed at Round 2; (a) still unsourced but the row is flagged |
| M10 (§4 per-source evaluation) | **Fixed** | All five items, all three texts |
| M11 (§5 four categories) | **Fixed** | And the Frend dispute now named (R2 M7) |
| M12 (Petilian dating) | **Partial** | Wording now correct and verified; still carried by no Registry row |
| M13 (discovery fields) | **Fixed** | Columns present; the absent search_record now honestly disclosed |
| M14 (Article 23 scope) | **Fixed** | Verbatim correct; inversion named |
| M15 (corpus-map role) | **Fixed** | Disclosed in §1, row 6, §9 item 7, §10 |
| M16 (forces lens) | **Fixed** | Substantive; §9 item 8 now routed in §10 |
| L1 (Shaw pointer) | **Fixed** | |
| L2 (Doc_01 §3 B2) | **Fixed** | Both sites — Round 2's only wholly-unfixed item is closed |
| L3 (Step0 B2/B5) | **Fixed** | |
| L4 ("verbatim" label) | **Fixed** | |
| L5 ("two centuries") | **Fixed** | |
| L6 (Article 26) | **Fixed** | |
| L7 (Tyconius hedge) | **Fixed** | Same hedge-loss class recurs at §2's Optatus entry — R3 L12 |
| L8 (a.d. 257) | **Fixed** | |
| L9 (IJC reuse) | **Fixed** | |
| L10 (broken sentence / status) | **Fixed** | Status line added; saturation requirement acknowledged |
| L11 (edition on row 1) | **Fixed** | With the file's own caveat carried |
| L12 (row 6 pointer) | **Fixed** | |
| L13 (Author Gravity deferral) | **Fixed** | |

**Round 1: 31 fully fixed, 3 partial (H5, M12, and H3 in its propagation), 0 unfixed.**

---

## Round 2 disposition table

| Round 2 | Status | Note |
|---|---|---|
| H1 (Manifest rights posture) | **Partial** | Manifest correctly rebuilt on the three-way split; no Destination on any in-copyright item; but every pointer into it is wrong (R3 H2) and the G1 gloss is invented (R3 H3) |
| H2 (Maximianist polarity/source) | **Fixed** | Rebuilt on *On Baptism* I.1.2 / I.5.7; both quotations verified exact and correctly located; polarity, refutation clause and row scoping all correct. **The best work in this revision** |
| M1 (flag list not re-run) | **Fixed** | 23, 24, 32, 33 added; 26 removed with a correct reason; "mechanically" dropped; 30/31 excluded with a correct reason |
| M2 (rows 30/31 → A) | **Partial** | Both moved to A correctly; calibration rule not stated; rows 3 and 6 now inconsistent (R3 M3) |
| M3 (apparatus / content / Ep. 162) | **Partial** | (a) fixed — now "the vendored edition's own translator's apparatus"; (b) fixed — content restored to "among the Donatists themselves"; (c) **inverted** (R3 M4, superseded by R3 H1) |
| M4 (Article 17 marking for Lucilla) | **Fixed** | §8 Inferential/Thin line added on the IJC model |
| M5 ("carries Book VII") | **Fixed** | Clause dropped; Preface-not-vendored disclosed; row 1 records the three-way dating divergence |
| M6 (Petilian dating) | **Partial** | Wording fixed and verified against the Prolegomena; the chronology is still carried by no row (Round 2 asked for row 4 or row 31 to carry it) |
| M7 (Frend thesis unmarked) | **Fixed** | Named in both §5 bullets; §8 Contested line added; rows 23/24/26 all consistent |
| M8 (Category 4 label) | **Fixed** | Label deleted; item correctly described as a process finding — but the same conflict now appears at Category 2 (R3 M5) |
| M9 ("held valid") | **Fixed** | Now "the baptism of these was valid," exact |
| M10 (row 29 mis-attributions) | **Fixed** | Both corrected; both verified against the extracted Step 0 Conclusion this session |
| M11 (Doc_01 §7 item 6) | **Fixed** | Petschenig CSEL 51–53 in Manifest §1 item 5; rows 17/18 updated; §10 states the discharge |
| M12 (Gallica contradiction) | **Fixed** | Both documents now say "digitization of the Migne volume," both say unconfirmed |
| M13 (clean documents) | **Partial** | All five named instances fixed; new round labels introduced in the `Added` column and "closes this revision pass" retained (R3 L1) |
| M14 (`Added` column dropped) | **Fixed** | Restored alongside Discovery, with appends distinguished |
| M15 (no search_record) | **Fixed** | New Discovery methodology note; honest, accurate, and verified against the absence of `records/don/` |
| M16 (*Psalmus* not rowed) | **Fixed** | Row 37 added — carrying a new dating defect (R3 M2) |
| L1 (Doc_01 §3 B2, both sites) | **Fixed** | |
| L2 (§7 cross-reference) | **Fixed** | Now points to §3, which does rely on it |
| L3 (row 13 `role:`) | **Fixed** | |
| L4 (row 1 translator caveat) | **Fixed** | Verbatim against the provenance header |
| L5 (Manifest bibliographic slips) | **Fixed** | Both |
| L6 (vendoring steps omitted) | **Fixed** | Provenance header + `texts_registry.py --write-readme`, command path confirmed |
| L7 (G1 undefined) | **NOT FIXED — worse** | A gloss was written; it is wrong and cited to a skill that lacks the term (R3 H3) |
| L8 (saturation: unproductive searches) | **Fixed** | The requirement is named and its non-satisfaction explained |
| L9 (no Status line) | **Fixed** | |
| L10 (Maximian homonym) | **Partial** | Doc_02 only; Registry silent (R3 L10) |
| L11 (P/S hybrid) | **Partial** | Rows 35/36 → P; row 40 reintroduces P/S (R3 L3) |
| L12 (row 35 chapter title) | **Fixed** | |
| L13 (Letter 162 absent from corpus) | **NOT FIXED — inverted** | The row now asserts the letter's presence (R3 M4) |
| L14 (*Passio Marculi* dating) | **Fixed** | Attributed to Frend, row 23 |
| L15 (Pharr / IJC precedent) | **Fixed** | Cited and quoted exactly |

**Round 2: 24 fully fixed, 7 partial, 2 not fixed.**

---

## Mandated reviewer coverage checks (Framework V7.4, Step 2, "Doc_02 review requirement")

Run fresh, against a third instrument set — the field's standard reference and prosopographical instruments, the current critical editions, and the standard translation series — chosen so that a revision tuned to Rounds 1 and 2 is not simply re-tested against itself.

### Ten-item relative-recall test

| # | Work | In Registry? |
|---|---|---|
| 1 | A. Mandouze, *Prosopographie chrétienne du Bas-Empire I: Prosopographie de l'Afrique chrétienne (303–533)* (Paris: CNRS, 1982) | **No** |
| 2 | M. Labrousse (ed./trans.), *Optat de Milève: Traité contre les donatistes*, Sources Chrétiennes 412–413 (Cerf, 1995–1996) | **No** |
| 3 | Y. Duval, *Loca sanctorum Africae: le culte des martyrs en Afrique du IVe au VIIe siècle*, 2 vols., CEFR 58 (Rome, 1982) | **No** |
| 4 | M. Edwards (trans.), *Optatus: Against the Donatists*, TTH 27 (Liverpool, 1997) | **No** |
| 5 | E. Tengström, *Donatisten und Katholiken* (Göteborg, 1964) | **No** |
| 6 | M. A. Tilley (trans.), *Donatist Martyr Stories*, TTH 24 (Liverpool, 1996) | **Yes** — row 35 |
| 7 | J.-L. Maier, *Le Dossier du Donatisme*, TU 134/135 | **Yes** — row 36 |
| 8 | S. Lancel (ed.), *Actes de la Conférence de Carthage en 411*, SC 194/195/224/373 | **Yes** — named at row 14; Manifest §2 |
| 9 | W. H. C. Frend, *The Donatist Church* (Oxford, 1952) | **Yes** — row 23 |
| 10 | M. Petschenig (ed.), *Scripta contra Donatistas*, CSEL 51–53 | **Yes** — row 39 |

**Relative recall = 5/10**, level with Round 2 on a harder list.

*(Bibliographic details for items 1–5 stated at Confidence B on this reviewer's own field knowledge, not re-checked against a library catalogue this session — the same standard this review applies to the documents.)*

The pattern has moved one notch and changed shape. The Registry now holds the interpretive monographs, the documentary dossier, the standard translation of the martyr corpus, and — new this revision — three public-domain critical editions. Two categories it still holds none of:

- **The field's standard reference instruments.** Item 1 is the sharpest miss in three rounds, because it is the instrument that settles precisely what this revision left open. `PCBE I` is where Lucilla, Felicianus of Musti, Prætextatus of Assuris, Petilian of Constantina, Emeritus of Caesarea and — critically — the anonymous "other woman" behind the Council of Maximianus are each fixed, dated and cross-referenced to their attesting texts. H1 above was findable by grep; the identification and dating work that follows from it is what item 1 exists for. Item 3 bears directly on §5's two Confidence-C material-culture bullets and §4's martyr-cult ecology, both of which the document itself flags as named-but-unexploited.
- **Any current critical edition.** Row 1's work is now attached to Ziwsa (1893, row 38) — correct as a public-domain route, and the right answer to the second-edition question the row leaves open — but Labrousse's SC 412–413 has been the reference edition since 1996, and Edwards's TTH 27 the standard English, and neither is named anywhere in three documents.

Items 4 and 5 remain undispositioned after being named at Round 1 and Round 2 (see L11).

### PRESS question, asked verbatim

> "Name up to three sources you would expect a bibliography of this world to contain that this registry does not hold. If you can name none, say so explicitly."

**Answer — three, all dispositioned "should be rowed":**

1. **A. Mandouze, *Prosopographie chrétienne du Bas-Empire, I: Prosopographie de l'Afrique chrétienne (303–533)* (Paris: CNRS, 1982).** The standard prosopographical instrument for exactly this world's people. **Disposition: row it (S, B, Native), licensed for the identification and dating of named — and unnamed — individuals in this world's own record, and add it to Manifest §3 (in copyright, consultation-only, never vendored). It is the instrument that would carry H1's second woman as far as the evidence allows.**
2. **Y. Duval, *Loca sanctorum Africae: le culte des martyrs en Afrique du IVe au VIIe siècle*, 2 vols., Collection de l'École française de Rome 58 (Rome, 1982).** The standard epigraphic and topographic corpus of the African martyr cult. **Disposition: row it (S/M, B, Native), licensed for the evidentiary basis of §5's *Deo laudes* and basilica bullets and §4's martyr-cult ecology — the two places this document names a category and admits it has not exploited it — and add to Manifest §3.**
3. **M. Labrousse (ed. and trans.), *Optat de Milève: Traité contre les donatistes*, Sources Chrétiennes 412–413 (Paris: Cerf, 1995–1996).** The current critical edition and translation of this world's earliest narrative source. **Disposition: attach to row 1 alongside Ziwsa (row 38) and add to Manifest §2 (in copyright, Cerf, recorded not requested) — so that row 1's second-edition question has both its public-domain route (Ziwsa) and its current-scholarship route named, rather than resting on a 1917 translator's footnote.**

I can name more than three; the instrument caps the answer at three.

---

## Escalation-category assessment (run independently, not accepted from §10)

Against `cic-build-cycle`'s four standing categories, on the current content of all three documents.

- **Representative identity, name, or title decisions** — not touched by any of the three. §10 is correct.

- **Portfolio-level or cross-world strategic decisions** — **does not apply**, and §10's assessment as written is not sustainable (M5). The category's own condition is "anything **decided** for a reason external to this specific world's own ecology." The Registry's Novatian row *records* a portfolio-level exclusion Step 0 already made and §10 is right about that. The Manifest *applies* the already-settled public-domain-only rule in `cic/texts/README.md` and puts a routine per-world acquisition choice to the project lead — which is what a Source Request Manifest is for, and which three sibling worlds have done without their Step 2 outputs becoming un-disposable. A decision governed by a settled cross-world policy is not a new cross-world decision. §10 should say so, drop "exactly the kind of choice this category exists to route to him," and fix its opening sentence, which tests the wrong condition. **This is a disagreement with Round 2**, which advised the opposite; see the Category 4 entry below.

- **Governance or methodology decisions** — **does not apply.** The Article 20/23 routing applies existing constitutional authority and the IJC precedent for it. The corpus-map ruling of 2026-08-26 is applied, not made. §9 item 8's forces-lens observation is a System Hub process finding of the same class as the two already standing in `don_Decision_Log.md`, and §10 now names and routes it correctly — the underlying claim about `Imperial-Juridical-Christianity/Doc_02_Source_Ecology.md` is accurate: I searched that document and "Forces Framework V1.1 Section 4 (Step 2 entry)" appears in its header and nowhere else in the file.

- **Unresolved tensions the pipeline can't close on its own** — **does not apply as an escalation, but one item must be logged.**
  - The corpus-map `context`/`tradition` inconsistency is **not** a Category 4 item, for the reasons Round 2 gave and I independently confirm: it is an infelicitous rationale inside a generated census file whose role assignments are themselves correct and already ruled on; it contradicts no cleared master document; and the pipeline can close it through the coach-thread/System Hub channel Step0 §3 B1 and §5 already established. §9 item 7 routes it correctly and §10 no longer mislabels it. **This is now right and should not be re-opened.**
  - **There is one genuine review-to-review disagreement to log.** Round 2 advised that "Acquisition posture and rights policy are decided for reasons external to this world's ecology; that is the category's own definition," and that §10 should say so. The build thread adopted that reasoning into §10 in the document's own voice. On the skill's own text and on the project's own three-world precedent, I find that reasoning wrong (M5), and the adopted wording is not sustainable alongside the self-disposition the same section plans. This is "two reviews disagreeing with each other" in the category's own words. **Disposition: log it in `don_Decision_Log.md` as a review-to-review disagreement with Round 3 superseding Round 2 on the skill's own text — following this world's own recorded precedent for Doc_01 Round 2 — rather than escalating it. A disagreement settled by reading a file that is already in the repository is not a tension the pipeline cannot close.** The prior disagreement Round 2 logged (its M5/M6/M8 supersessions of Round 1) is still not recorded: the Decision Log's Doc_02 entry remains "to be completed when review concludes," which is correct while review is in progress but must be discharged before disposition.

**Assessment: no escalation category applies once §10's Category 2 framing is corrected. But §10 as written cannot be disposed of, because it labels an item as triggering a category and then plans to self-dispose over it — the same structural error Round 2 found at Category 4 and the build thread corrected there.**

**On disposition eligibility and completeness.** The Registry's saturation statement and the Discovery methodology note are, together, the most honest self-description this document set has produced: the field-bibliography sweep is not claimed, the absent `search_record` is disclosed rather than implied, the recall and PRESS instruments are described as a start rather than a substitute, and Doc_02 §10 mirrors all of it. **Preserve this.** V7.4's "A Registry without a saturation statement is not complete" is satisfied in the sense that matters — the statement exists and names its own limits — while the Registry itself remains knowingly partial, which §10 says in the document's own voice.

---

## Guidance for the revision pass

1. **H1 is a research task that takes one command and yields a better paragraph than the one it replaces.** `grep -n "Lucilla" cic/texts/npnf101_augustine-confessions-letters.xml` returns seven hits; all seven are in Letter XLIII; §26 is the answer. Read it before rewriting the bullet, and let the *named Lucilla / unnamed second woman* asymmetry do the Article 20 work — it is a sharper finding than either the blank Round 1 found or the unrunnable lead this draft reports.
2. **H2 and H3 are mechanical and neither requires a judgment call.** Eight pointers, one contradicted sentence in Doc_02 §1, and one label. For H3, open `Build/worlds/desert/build/SOURCE-REQUEST-MANIFEST.md` §3 and `Build/worlds/alx/build/SOURCE-REQUEST-MANIFEST.md` before writing anything about G1 — the convention is defined by use in four files.
3. **Do not adopt this review's suggested wording without opening the file.** This is the fourth consecutive round in which a reviewer-supplied fix has become the next round's finding: Round 1's H1/M12 wording → Round 2's M5/M6; Round 2's L7 → this round's H3; Round 2's L13 → this round's M4; Round 2's escalation advice → this round's M5. Where I have proposed replacement wording above, treat it as a description of what needs to be true, not as text to paste. In particular, **do not paste my Letter XLIII gloss** — read §26 and write what it says.
4. **When a document is restructured, re-read every pointer into it.** H2 exists because the Manifest was rebuilt correctly and nothing that references it was re-read. Before this revision closes, open each of the three documents and follow every `§`, `row N`, and named-file reference to its target.
5. **Nothing in "What checks out clean" above may be disturbed.** Above all: Registry row 6's Ep. 87 licensing constraint, re-verified against the letter itself for the third consecutive round; the *On Baptism* I.1.2 / I.5.7 rebuild and its two quotations; the 256-council double entry and §9 item 6; the Augustine letters split; the four five-dimension Author Gravity entries; the Lucilla quotations and the I.16 citation; the two NPNF104 Prolegomena quotations; the §6 Article 23 restatement and the IJC inversion sentence; the §4 five-item evaluations; the forces-lens paragraph; the §5 Frend-dispute framing; the Manifest's three-way structure and its network disclosure; and — new and best this revision — the Discovery methodology note and the saturation statement's honesty about what was not done.
6. **Round 4 should be short, and it should be the last.** Of the twenty-four findings here, three highs and six mediums are localized to single sentences, rows or pointers, and fifteen lows are wording. The document's substance is now largely right: its sourcing conclusions hold, its quotations are exact, its confidence map is defensible, its central discipline — naming what this world's evidence cannot do — is better executed than in either prior version. What has repeatedly failed is not the reasoning but the last mile: the check that a pointer resolves, that a label is real, that a negative claim was actually tested. That is the whole of what is left.

---

*Review artifact filed per `cic-build-cycle`: review rounds exist as files, not claims. This review was conducted independently of the build thread that drafted the documents, and independently of Rounds 1 and 2, against primary and governing sources directly rather than against any document's own account of them. Where this review disagrees with Round 2 (the Category 2 escalation framing, M5), the disagreement is recorded as such rather than resolved silently, and rests on the governing skill's own text and on the project's own three-world manifest precedent.*
