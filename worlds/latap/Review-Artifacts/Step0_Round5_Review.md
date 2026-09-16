# Step 0 Movement-Scope Confirmations, Apologist Pair — Round 5 Independent Adversarial Review

**Reviewed documents (Revision 4, commit `4a72cf4a`):**
- `worlds/grkap/Step0_Movement_Scope_Confirmation.md` (Atlas I.35)
- `worlds/latap/Step0_Movement_Scope_Confirmation.md` (Atlas I.43)

**Prior rounds:** `Review-Artifacts/Step0_Round1_Review.md` (`09d94033`), `Step0_Round2_Review.md` (`17f981b7`), `Step0_Round3_Review.md` (`919ffcdb`), `Step0_Round4_Review.md` (`4d52aa28`), each duplicated under both worlds. Round 1: SUBSTANTIAL REVISION REQUIRED for both (I.35 A1–A14, four HIGH; I.43 B1–B9, four HIGH; plus a commissioned Era 1 sweep, Part C). Round 2: SUBSTANTIAL REVISION REQUIRED for both (I.35 N1–N7, two HIGH; I.43 thirteen findings, no HIGH). Round 3: SUBSTANTIAL REVISION REQUIRED for both (I.35 R1–R11, one HIGH; I.43 R12–R16, no HIGH). Round 4: SUBSTANTIAL REVISION REQUIRED for both (I.35 R17–R23, no HIGH; I.43 R24–R29, one HIGH).

**Reviewer:** independent isolated agent. No involvement in either draft, in Revisions 1–4, or in Rounds 1–4.

**Overall verdicts:**
- **I.35 (Second-Century Greek Apologists): NO SUBSTANTIAL REVISION REQUIRED.** All seven of Round 4's findings (R17–R23) are genuinely discharged. Five LOW items remain, all in the citation-precision and revision-history-bookkeeping classes; none changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary. **No HIGH and no MODERATE finding.**
- **I.43 (Latin Apologists): NO SUBSTANTIAL REVISION REQUIRED.** All six of Round 4's findings (R24–R29), including the HIGH, are genuinely discharged. One LOW item, introduced by this revision's own R29 fix, plus three cosmetic notes. **No HIGH and no MODERATE finding.**

The four-round repeat-failure pattern — each revision introducing at least one new material defect while correcting the last round's — **does not hold for Revision 4.** Round 2 introduced two HIGHs; Round 3 introduced one HIGH; Round 4 introduced no HIGH but three MODERATEs; Round 5 finds no HIGH and no MODERATE in either document. That is a genuine convergence, and it is recorded as such rather than softened into another conditional verdict.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

**A note on method.** Nothing was accepted from either document's §6, and nothing from Rounds 1–4 was taken as a premise; Round 4's own findings were re-tested as claims, not adopted. Every finding below was re-derived directly from the repository: `cic/corpus-map/*.yaml` parsed and cross-joined with `yaml`; `records/<world>/` read and grepped file-by-file across all fourteen record subtypes in all seven built worlds; `cic-website/data/world-census.json` parsed and field-tested; `CiC_L1_Constitution_V2_2.docx` (internal Version 2.3), `CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx` and `reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` extracted from their `.docx` and read; every vendored text cited in either document parsed and word-counted with `lxml` independently of both documents' numbers and of every prior round's tables; the prior four review artifacts opened and their findings counted out of their own headings. Per Round 4's own process note 2, **every clause of the form "X states that…" about an ancient author was checked against the vendored translation in `cic/texts/`** — Jerome *Ep.* 84.7 and *De vir. ill.* LXXIX in `npnf206`/`npnf203`, Minucius Felix *Octavius* ch. XXIX and the whole `div2 iv.iii` token counts in `anf04`, Lactantius *Div. Inst.* II.ix and VII in `anf07`, Arnobius *Adv. Nat.* II in `anf06`, Irenaeus *AH* I.28 in `anf01`, Eusebius *HE* IV.29 in `npnf201`. That last check is where I.35's one new substantive finding comes from.

**Working-tree note.** Both documents and all eight prior artifacts were read at `4a72cf4a` on branch `_round5review/apologists`, fetched from `candidate-worlds-step0-apologists`. No document content was altered; this artifact (duplicated into both worlds' directories) is the only file written.

---

## Part A — I.35: Round 4 findings re-tested

Each entry states what Revision 4 claims, what the repository actually shows, and whether the result is **(a) genuinely resolved**, **(b) addressed in form but wrong or incomplete in a new way**, or **(c) unfixed**.

### R17 [was MODERATE] — §6's Round 3 paragraph claiming to address "all fourteen findings." **(a) Genuinely resolved.**

§6 now opens that paragraph *"this revision addresses all **eleven** findings directly — not fourteen, which is Round 1's count carried down from the paragraph above where it does not belong; Round 3's own Part B against this document contains exactly eleven, R1 through R11."* Counted directly out of `Step0_Round3_Review.md`'s Part B headings: **R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11 — eleven**, no more and no fewer. The eleven fix-clauses that follow map one-to-one onto them. Correct, and correct with the reason for the earlier error stated.

### R18 [was MODERATE] — "seven of Round 1's findings had been only partially fixed." **(a) Genuinely resolved, and independently recounted.**

§6 now reads *"ten of Round 1's own findings had been only partially fixed — A1, A2, A3, A5, A6, A8, A9, A10, A11, and A14, counted directly from Round 2's own Part A headings, each graded (b) or worse — not seven, as an earlier revision stated."*

Recounted from `Step0_Round2_Review.md`'s Part A headings, without reference to Round 4's table:

| Round 1 finding | Round 2 grade |
|---|---|
| A1 | **(b)** |
| A2 | **(b)** |
| A3 | **(b) + (c)** |
| A4 | (a) — *"Withdrawn correctly — with a new arithmetic error, and a much larger fact still missing"* |
| A5, A6, A8, A9, A10, A11, A14 | **(b)** ×7 |
| A7, A12, A13 | (a) |

**Ten** carry (b) or worse, and they are exactly the ten the document now names. The substance R8 identified — not just the arithmetic between the number and the parenthesis — is now addressed.

### R19 [was MODERATE] — the Tier's fallback paragraph naming six roster members and accounting for five. **(a) Genuinely resolved, and rebuilt rather than patched, as Round 4's process note 3 asked.**

The sentence now sorts all six into three groups, and each group is right on the files:

| group | members | verified |
|---|---|---|
| Unclaimed by any PAHC record of any type | Athenagoras, Aristides, the *Diognetus* author | ✓ — grep of all fourteen `records/pahc/` subtypes: "Aristides" **0**, "Diognetus" **0** anywhere in `records/`; all **eleven** "athenagoras" hits are the vendored `anf02` filename string |
| Claimed by PAHC's `load-bearing` fragment-collection source record as an author, not at `emic`-figure level | Quadratus, Melito (Melito additionally an `emic` quote record and a gravity slot at `contested`) | ✓ — `pahc.source.second-third-century-remains.md` `author:` names Quadratus of Athens, Aristo of Pella, Melito of Sardis among ten; `pahc.quote.melito-no-phantom.md` `register: emic`, `evidentiary_weight: contested`, `formation_confidence: Contested`, feeding `pahc.gravity.boundary-drawing` as *"a flagged candidate second voice"* |
| Cited by locus, independently of the fragment collection, with no figure or source record claiming his voice | Theophilus | ✓ — `pahc.witness.jesus-as-god.md` cites *To Autolycus* II.15 at lines 72 and 84 |

Three plus two plus one is six, and the six named are all `confidence: assigned` on `greek-apologists-second-century.yaml` (rows 2, 4/5, 12, 13, 14, 16 of sixteen). The Tier's conclusion is correspondingly stated as a complication rather than a foreclosure, and §4 item 7 agrees with it. **One residue inside the same sentence, unchanged since Revision 2 and never yet flagged — see R34.**

### R20 [was LOW] — the "Athenagoras" hits attributed to `edition:` fields. **(a) Genuinely resolved, and exactly right.**

§3 B3 now reads *"once in an `edition:` field, once in a `locus:` field, and nine times inside record bodies citing that same filename as their own textual provenance."* Enumerated directly: `pahc.source.shepherd-hermas.md` line 18 (`edition:`); `pahc.quote.put-away-doubting-from-you.md` line 20 (`locus:`); and nine body-prose occurrences in `pahc.witness.prayer-and-struggle`, `…marriage-and-wealth`, `…outside-our-community`, `…doubt-and-asking`, `pahc.story.hermas-visions`, `pahc.craft.chloe-voice`, `pahc.demo.identity-collision-womens-authority`, `pahc.demo.identity-collision-divorce`, `pahc.quote.hermas-doubting`. **1 + 1 + 9 = 11.** The field-type breakdown is now stated correctly for the first time in four rounds.

### R21 [was LOW] — the Alexandria bullet's `edition:` attribution, restated a fourth time. **(a) Genuinely resolved.**

§3 B3 now reads *"four in unrelated records' own `edition:` metadata fields (`alx.source.clement-stromateis`, `-protrepticus`, `-paidagogos`, `-quis-dives`), three in `locus:` fields (`alx.quote.to-believe-or-disbelieve`, `-couches-and-trenchers-and-bowls`, `-the-grades-here-in-the-church`)."* Enumerated directly: exactly those seven files, exactly those two field types, four and three. The withdrawal of the fabricated Clement-citation detail stands, and I independently re-confirm the underlying result: there is no textual reference to Tatian, Athenagoras or Theophilus of Antioch anywhere in `records/alx/` — the only "Theophilus" is Theophilus of Alexandria in `alx.source.alexandrian-canonical-answers.md`.

### R22 [was LOW] — the stranded "again." **(a) Genuinely resolved, with the reason shown.**

The word is gone and the bullet now carries an explicit note that *"no prior bullet in this list still credits Part C, since the Alexandria bullet above is this document's own direct check and the built-worlds bullet explicitly withdraws the Part C credit for its four Era 2 worlds."* Verified against the document: the Alexandria bullet credits a direct check, the built-worlds bullet withdraws the credit for Desert/Hieronymian/IJC/Cappadocian, and the Ebionite bullet credits §2 A5. The credit the bullet does carry is itself accurate — Round 1's C7 covers Montanism, Novatianism, the doctrinal-floor exclusions (I.21, I.22), the floor-question entry (I.31) and the remaining possible-future-world entries, and its Montanism entry states the Tatian/Encratism finding the bullet reproduces.

### R23 [was LOW] — "roster" used in two incompatible senses. **(a) Genuinely resolved.**

The Aristo sentence now reads *"three of this candidate's own **corpus-map entries** (Aristo by corpus-map assignment alone, not the census `voices` field — see §2 A2's own distinction above)."* Verified: Quadratus (row 14), Aristo (row 3) and Melito (row 13) are all corpus-map rows; Aristo is not among I.35's seven census `voices`, and the parenthetical now says so on exactly the ground §2 A2 uses for Tatian. The later "three more of this candidate's own roster — Quadratus, Melito, and (more narrowly) Theophilus" is now unobjectionable, since all three *are* census `voices`.

---

## Part B — I.35: findings against Revision 4

**No HIGH. No MODERATE.** Five LOW items, one of them substantive enough to be worth a sentence in Doc_01's own working notes.

### R30. [LOW] §2 A2 attributes to Irenaeus, *Against Heresies* I.28, "directly," a description of Encratite practice that I.28 does not contain. The fact is right; the locus over-reaches by one item. Present since the original draft; first checked here.

> §2 A2: *"Irenaeus reports **directly** (*Against Heresies* I.28) that after Justin's martyrdom Tatian went on to found or lead the Encratite current **(rejecting marriage and wine on ascetic-dualist grounds)**, a genuine later divergence Irenaeus traces from Saturninus and Marcion rather than from any Phrygian or Eastern source."*

Read directly from `cic/texts/anf01_apostolic-fathers-justin-irenaeus.xml`, ch. XXVIII (*"Doctrines of Tatian, the Encratites, and others"*), the whole of what I.28 attributes to the Encratites is: *"Springing from Saturninus and Marcion, those who are called Encratites (self-controlled) preached against marriage… Some of those reckoned among them have also introduced abstinence from **animal food**… They deny, too, the salvation of him who was first created,"* with Tatian named as *"a hearer of Justin's"* who *"after his martyrdom… separated from the Church"* and, *"like Marcion and Saturninus, declared that marriage was nothing else than corruption and fornication."* **Marriage and flesh — not wine.** `(?i)wine` returns **zero** occurrences anywhere in I.28.

The wine detail is genuinely attested, but from a different source: the NPNF editor's note on **Eusebius, *HE* IV.29** (`cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml`) — *"These Encratites were heretics who abstained from flesh, from wine, and from marriage, not temporarily but permanently"* — the same *HE* IV.29 that `syr.source.tatian-address-to-greeks.md` names as the charge's own source. Everything else in the sentence is exact: the Saturninus/Marcion derivation, the post-martyrdom separation, and the absence of any Phrygian derivation.

This is the identical defect class as I.43's R27 (*De vir. ill.* 79 cited for the *Chronicle*'s content), which Round 4 graded LOW, and it is fixed the same way — either drop "and wine," or cite *HE* IV.29 alongside I.28, which the document's own Syriac source record already points at. It changes nothing downstream: A2's disclosure ruling, §4 item 3's Doc_02 obligation and the Tier are all unaffected.

### R31. [LOW] §6's Round 4 paragraph places five of Round 4's findings "in §3 B3." Four are; R19 is in the Section B conclusion, as the same sentence's own description of it shows.

> §6: *"found no new HIGH and seven MODERATE/LOW findings, **two of them in §6 and the remaining five in §3 B3**: … **R19**, **the Tier's fallback paragraph** naming a six-member roster and then accounting for only five…"*

R17 and R18 are in §6 ✓. R20 (the PAHC paragraph), R21 (the Alexandria bullet), R22 (the last built-world bullet) and R23 (the "roster" senses) are all in `### B3 — Uniqueness` ✓ — **four**. R19 is in `### Section B conclusion — Tier`, a sibling subsection of B3, not inside it; the document's own next clause calls it "the Tier's fallback paragraph," and its fix list one paragraph later does the same. The counts (seven, two) are right and every finding is correctly described and correctly fixed; only the section label for one of them is wrong.

### R32. [LOW] §6 says Round 4 "confirmed all eleven of Round 3's findings genuinely discharged." Round 4's Part A grades R8 **(b)**. The document is echoing an inconsistency inside Round 4 itself, not inventing one.

> §6: *"Round 4 independent adversarial review … **confirmed all eleven of Round 3's findings genuinely discharged** — including the HIGH, 'the strongest fix in either document this round'."*

`Step0_Round4_Review.md` Part A grades R1–R7 and R9–R11 **(a)**, and R8: *"**(b)** The internal arithmetic is fixed; the count put in its place is still wrong, and R8's actual substance is unaddressed and reported as discharged. See R18."* The accurate statement is *ten of eleven, with R8's substance carried forward as R18*. In fairness to the document, Round 4's own verdict section says *"Round 3's HIGH is genuinely and thoroughly discharged, and every one of R2–R11 with it"* — so the review file says both things, and the document followed the verdict rather than the grading table. The *"strongest fix in either document this round"* quotation is verbatim from Round 4's R1 heading. R8's substance is, in any case, now discharged by the R18 fix verified at Part A above.

### R33. [LOW] §6 states "ten … not seven" in its Round 2 paragraph and "— seven in fact" in its Round 3 paragraph, two paragraphs apart, without distinguishing what each number counts.

> §6, Round 2 paragraph: *"**ten** of Round 1's own findings had been only partially fixed … **not seven**, as an earlier revision stated."*
> §6, Round 3 paragraph: *"**R8**, 'four' of Round 1's findings partially fixed when six were enumerated (a seventh, A14, sits outside the parenthesis) — **seven in fact**."*

Both statements are true of different objects: Revision 2's §6 enumerated seven names (A5, A6, A8, A9, A10, A11 inside the parenthesis, A14 outside), while Round 2's Part A grades ten (b) or worse. Round 3's R8 itself made exactly this distinction (*"Round 2's actual count of partially-addressed Round 1 findings is higher still"*). But a reader meeting "not seven" and "seven in fact" two paragraphs apart, in the same section, on the same underlying question, meets an apparent contradiction. One clause — "seven names enumerated, ten actually so graded" — removes it.

### R34. [LOW] The Tier's fallback sentence names two of the three attribution-flagged corpus-map items §4 item 4 carries, omitting the Ambrose *hypomnemata*. Unchanged since Revision 2; not previously flagged.

> Tier: *"…plus the pseudonymous-Justin works and Aristo of Pella's fragments pending their own attribution questions."*
> §4 item 4: *"Confirm the status of the three pseudonymous Justin works, Aristo of Pella's triple assignment…, **and the Ambrose *hypomnemata*'s dual assignment and date question with Syriac Christianity**."*

The Ambrose *hypomnemata* is the one `provisional` row on this candidate's own map besides the three pseudo-Justin works (verified: `greek-apologists-second-century.yaml` row 1, `confidence: provisional`, *"`provisional` because the APOLOGIST half is a date question — the entry's window is 124-200 and this piece is undated"*), and it is the second of the two works dual-assigned with Syriac — which makes it directly relevant to a fallback scenario premised on Tatian's voice staying with Syriac. This is an incompleteness, not a false statement ("plus X and Y" does not assert "and nothing else"), and §4 item 4 carries the item correctly, so nothing downstream is wrong. Recorded because R19's own history is a sequence of enumerations in this one sentence that were short by one.

*Cosmetic, not findings:*
- *"A5's full text, both sentences"* (§2 A5) names as A5's full text the **first of A5's three paragraphs**. The two sentences quoted are verbatim, and the other two paragraphs (the Article 20 clause and the Article 21 strand clause) are used accurately elsewhere in the document. Round 4 recorded this as cosmetic; it is unchanged.
- *"Irenaeus is this document's own source, **two sentences above**"* (§2 A2) — the Irenaeus citation is four sentences above in the same paragraph.
- *"checked across all fourteen `records/pahc/` subtypes, not four **(Round 4 finding)**"* — accurate in substance (fourteen subtypes confirmed: `contested_claim`, `demonstration`, `doctrinal_witness`, `figure`, `force`, `gravity`, `honest_limit`, `quote`, `search_record`, `source`, `story`, `term`, `voice_craft`, `world_core`), but it was a verification note inside Round 4's Part A R1 and its verdict, not one of the numbered findings R17–R23.
- §4 item 7 instructs Doc_01 to re-derive the PAHC finding from *"`records/pahc/source/`, `quote/`, `gravity/`, and `doctrinal_witness/`"* — four subtypes — while §3 B3 now rests the finding on a fourteen-subtype check. The instruction should name the wider sweep it is now backed by.

---

## Part C — I.43: Round 4 findings re-tested

**All six are genuinely discharged, including the HIGH.** Each was re-derived independently, and the HIGH was re-derived from the vendored translation rather than from Round 4's quotation of it.

### R24 [was HIGH] — Jerome's charge against Lactantius quoted in words Jerome did not write. **(a) Genuinely resolved, at all three sites, and resolved the way Round 4's "what a fix requires" specified.**

§2 A2 now reads: *"Jerome (*Ep.* 84.7, to Pammachius and Oceanus) does not say Lactantius denies the Spirit's substance 'in his letters, and especially in those to Demetrianus.' The vendored translation (`cic/texts/npnf206_jerome-principal-works.xml`) reads: 'Lactantius in his books and particularly in his letters to Demetrian altogether denies the subsistence of the Holy Spirit, and following the error of the Jews says that the passages in which he is spoken of refer to the Father or to the Son'."*

Checked directly in `npnf206_jerome-principal-works.xml`, `div2` **Letter LXXXIV, "To Pammachius and Oceanus"**, in the paragraph opening **"7."** — the quoted string is **verbatim**, line breaks aside. Jerome's next sentence is also quoted verbatim: *"But who can forbid me to read his Institutes—in which he has written against the Gentiles with much ability—simply because this opinion of his is to be abhorred?"* The document now uses that sentence for exactly what it establishes: that the charge reaches the surviving, vendored corpus.

The three downstream consequences are all correctly rewritten and mutually consistent:

| site | now says | correct |
|---|---|---|
| §2 A2 | the charge is *"leveled at Lactantius' **books generally**, with the letters to Demetrianus named only as its sharpest instance, not its sole target"*; the lost letters are worth disclosing, *"but the charge does not attach to them **rather than** to the *Divine Institutes*"* | ✓ |
| §2 A2 | the vendored *Institutes*' two-spirits cosmology at II.8–9 is *"precisely the binitarian-with-a-fallen-second-spirit structure the ancient charge concerns, not a structure outside its reach"* | ✓ — read directly at `anf07` Book II ch. IX: God *"made another being, **in whom the disposition of the divine origin did not remain**"*, who *"was infected with his own envy as with poison, and **passed from good to evil**"* — both quoted strings verbatim; Book VII's chiliasm is likewise present (chs. XXIV *"Of the renewed world"*, XXVI *"Of the loosing of the devil, and of the second and greatest judgment"*) |
| §4 item 5 | *"leveled at Lactantius' books generally, 'particularly' his letters to Demetrianus — not at the letters alone"*, with Doc_02 required to say that no primary text of the sharpest instance survives while the charge reaches the corpus this candidate holds | ✓ — and the instruction is now the stronger, more disclosable one Round 4 said a correct fix would produce |

`grep -n "Demetrian"` across the document returns four hits, all consistent; **no residue of the narrowed reading survives anywhere.** The crediting is also right: the misquotation is described as *"entered at Revision 2 and left uncaught through Round 3"* — verified against git, the string *"in his letters, and especially in those to Demetrianus"* is absent from Revision 1 (`d950535f`) and present from Revision 2 (`fb054eef`) onward.

### R25 [was MODERATE] — incompatible readings of *Octavius* ch. XXIX. **(a) Genuinely resolved.**

§2 A2 now quotes the passage rather than characterizing it twice, and adopts one reading: *"reads 'you wander far from the neighbourhood of the truth, in thinking either that a criminal deserved, or that an earthly being was able, to be believed God' … that sentence rejects the pagan's own characterization of Christ as 'a criminal' rather than straightforwardly denying his divinity — **it declines to deny Christ's divinity rather than denying it outright**, and this document adopts that reading consistently."* The Section A conclusion's wording (*"declines to deny Christ's divinity rather than denying it outright"*) is now identical. The quoted sentence is **verbatim** from `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, `div2 iv.iii`, ch. XXIX.

All the Minucius Felix arithmetic re-derives exactly, counted independently with `lxml` over `div2 iv.iii`: `\bJesus\b` **0**, `\bSon of God\b` **0**, `(?i)incarnat` **0**, `\bChrist\b` **2**, `(?i)crucifi` **2**, division length **23,819 words**. The four apparatus hits are the ch. XXXVII *Argument* heading, the footnote *"Legat. pro Christ., ch. xxviii."*, the ch. IX *Argument* heading, and the bracketed gloss at ch. XXIX — none in Minucius' own prose, exactly as §2 A2 and §4 item 3 state.

### R26 [was LOW] — the header's "wherever it must characterize one" against a non-verbatim gloss. **(a) Genuinely resolved.**

§2 A2 now carries the fifth commitment in full: *"The Holy Spirit as Lord and giver of life, worshiped and glorified together with the Father and the Son."* Diffed character-by-character against `CiC_L1_Constitution_V2_2.docx` (internal Version 2.3) Article 4 — **exact**, *"together"* and both definite articles restored. The string occurs twice in the document (header and §2 A2) and is verbatim both times. I re-diffed all five commitments in **both** documents' headers against the Constitution: **all ten instances verbatim**, the only variance being commitment (3)'s internal double quotes rendered as single quotes inside an outer double-quoted string, which is correct nesting. Article 4's closing instruction is verbatim in both. No other place in either document characterizes a commitment in a way that would trigger the header's own rule.

### R27 [was LOW] — *De viris illustribus* 79 cited for the *Chronicle*'s content. **(a) Genuinely resolved.**

§2 A2 now reads: *"*De viris illustribus* 79 states **only** that Arnobius was 'a most successful teacher of rhetoric at Sicca in Africa during the reign of Diocletian' who 'wrote volumes Against the nations which may be found everywhere' — no dream, no bishop, no refusal, no pledge. The dream-and-bishop account is the *Chronicle*'s alone (ad ann. 327)."*

Read directly from `cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml`, **Chapter LXXIX**, whose entire text is: *"Arnobius Flourished 295. was a most successful teacher of rhetoric at Sicca in Africa during the reign of Diocletian, and wrote volumes Against the nations which may be found everywhere."* Both quoted fragments are **verbatim**; the chapter contains nothing else. The census hedge *"if Jerome is to be believed"* is verbatim from the I.43 `longDescription`. The Book II theology is also accurate: `anf06`, Book II, *"theirs is an intermediate state, as has been learned from Christ's teaching… neither immortal nor necessarily mortal… they may on the one hand perish if they have not known God, and on the other be delivered from death."*

### R28 [was LOW] — §6 saying Round 2 returned "twelve findings" while enumerating thirteen. **(a) Genuinely resolved, and independently recounted.**

§6 now reads *"thirteen findings in all, not twelve."* Counted out of `Step0_Round2_Review.md`'s Parts C and D: B1(i), B1(ii), B1(iii), B1(iv) = 4; B2, B3-LOW, B4-MODERATE, B8, B9 = 5; M1, M2, M3, M4 = 4. **Thirteen**, and the document's own enumeration names all thirteen in that order.

### R29 [was LOW] — B4's "the same province" against the Carthage exclusion. **(a) Genuinely resolved on substance.**

B4 now reads *"the same **crisis** from the opposite side."* Verified against the census: I.43 `region` is *"Rome and Ostia; Sicca in Numidia; Nicomedia and Trier"*; I.17 `region` is *"Carthage"*. The crisis is genuinely shared; the province is not, and the document no longer says it is. **One residue inside the fix — see R35.**

---

## Part D — I.43: findings against Revision 4

**No HIGH. No MODERATE.** One LOW item, introduced by this revision's own R29 fix.

### R35. [LOW] The R29 fix's new cross-reference points two of its three targets in the wrong direction.

> B4: *"the same crisis from the opposite side (correcting 'the same province,' Round 4 finding R29: Carthage sits outside this candidate's own named regions, **per §2 A5, B5, and §4 item 4 above**, even though Arnobius' Sicca is Numidian)."*

§2 A5 is above B4 ✓. **B5 is the next subsection below it**, and **§4 item 4 is two sections below that.** The document gets the direction right at the other end of the same chain — §2 A5 says *"see also §3 B3, §4 item 4, and B5's scale claim **below**"* — which is what makes this a slip rather than a convention. The three cross-references themselves are correct and the Carthage boundary is stated accurately at all four sites; only the word "above" is wrong. One word.

*Cosmetic, not findings:*
- §4 item 7 renders Part C's scope inside quotation marks as *"the entries not already checked by the drafts."* Part C's own words (C8) are *"the **nineteen Era 1** entries not already checked by the drafts."* The claim carried is accurate and Round 4 recorded this as cosmetic; it is unchanged.
- §4 item 3's *"all in ANF editorial apparatus (chapter headings and a footnote)"* compresses two chapter headings, one footnote **and one bracketed in-text gloss**. §2 A2's own fuller description in the same document is more precise; the binding instruction is the less precise one.
- The *Chronicle* notice at ad ann. 327 is not among the vendored texts in `cic/texts/` (no Jerome *Chronicle*), and the document does not say so, in a paragraph that is otherwise careful to flag the lost letters to Demetrianus as unvendored. The date is within the ordinary range (326/327), as Round 2's B6 independently confirmed, and the claim is a summary rather than a quotation — so this is a disclosure-symmetry note, not a citation error.

---

## What checked out clean (verified directly this round, not carried from Rounds 1–4)

Recorded so a further revision does not disturb settled ground. Everything below was re-derived from the primary file.

**Corpus maps, re-parsed and cross-joined on `(author, work)`:**
- `greek-apologists-second-century.yaml` — **16** rows; **15** also on `post-apostolic-house-church.yaml`; **2** also on `syriac-edessa-nisibis.yaml` (Tatian's *Address*; the Ambrose *hypomnemata*); union **16**; assigned to I.35 alone **0**. B1's "sixteen works, of which the five named are five *of* the sixteen" closes.
- Tatian's *Address* at `confidence: assigned` in all three maps; note verbatim, including *"Tatian sits awkwardly across two entries… Mark may want a ruling on where his voice sits"*.
- Aristo of Pella on three maps (`greek-apologists-second-century`, `post-apostolic-house-church`, `ebionite-nazoraean-current` per §2 A5), note verbatim: *"The Jewish-Christian current and pahc are both defensible; neither is demonstrated by the fragments."*
- The three pseudonymous Justin works and their **two distinct** notes, each attributed to the right work: *"Same position as the Discourse: transmitted under Justin, widely doubted"* (*Hortatory Address*, *On the Sole Government of God*); *"Printed under the JUSTIN MARTYR div1; authenticity has long been questioned. Filed with its transmitted author per §6.2 - derive, don't assert - with the doubt recorded"* (*Discourse to the Greeks*).
- Ambrose *hypomnemata* — `provisional` on its **date**, ruled 2026-08-26, Greek apologetic surviving only in Syriac; **no Quadratus content of any kind**. *Diognetus* — *"some put it after the entry's 200 CE close"* verbatim. *Dialogue* ch. 47 — *"one of the era's few direct witnesses to the ebionite-nazoraean-current material"* verbatim.
- `post-apostolic-house-church.yaml` — 68 rows; **eight** at `author: justin_martyr` (three `assigned`: *First Apology*, *Second Apology*, *Dialogue*; five `provisional`), plus *The Martyrdom of Justin Martyr* at `author: martyrdom_of_justin` — the "eight works plus one non-Justin *acta*" arithmetic closes.
- `latin-apologists.yaml` — **7** rows, six `assigned` / one `provisional` (Commodian's *Instructiones*), the map's reason verbatim: *"The entry is right if the usual 3rd-c. North African dating holds and wrong if the 5th-c. Gallic one does. Nothing in the corpus settles it."* Mark's 2026-08-27 ruling verbatim, including *"THE RULING SPLITS THE AUTHOR, WHICH IS WHAT `per work` MEANS"* and the Athanasius sentence. No *Epitome* row.
- `tertullian-s-voice.yaml` — **33** rows, including *Ad Nationes*, *To Scapula*, *The Soul's Testimony*, *An Answer to the Jews*, *Apology (Apologeticus)*. `latin-pastoral-congregational-christianity.yaml` — 77 rows, **no** work by Arnobius, Lactantius, Minucius Felix or Commodian.

**Built-world records:**
- `pahc.source.second-third-century-remains.md` — `register: emic`, `evidentiary_weight: load-bearing`, `verification_state: verified-direct`; `author:` names ten voices, Quadratus of Athens, Aristo of Pella and Melito of Sardis among them; body loci *"Quadratus 70010… Melito 70117"* verbatim.
- All five PAHC Justin citations in §3 B3 — `pahc.quote.moses-is-more-ancient` (`load-bearing`, 1 Apol. XLIV, *"an apologetic claim about chronology made to a pagan audience"*); `pahc.quote.those-who-lived-reasonably-are-christians` (`load-bearing`, `retrieval tier: 1`, 1 Apol. XLVI, *"the Logos present in every race of men"*); `pahc.quote.the-memoirs-of-the-apostles-are-read`'s divergence note verbatim; `pahc.figure.justin`'s `bridge_line` verbatim; `pahc.source.justin-dialogue`'s WEIGHT note and Ways-That-Never-Parted caution; `pahc.source.justin-first-apology`'s *"clearest inside evidence that the rival movements were live, contemporary, and undefeated."* All exact.
- `pahc.source.justin-first-apology`'s WEIGHT note independently confirms §3 B2: *"chapters 61 and 65-67 are the fullest early descriptions of baptism and Sunday worship anywhere in this world's base."*
- `syr.figure.tatian` (`corroborating`, `narratable: false`, *"Boundary-adjacent"*, *"without adopting him as a founding teacher"*) and `syr.source.tatian-address-to-greeks` (`load-bearing`, *"Every argument for Tatian belonging to the Syriac East runs through the statement that he was an Assyrian"*, *"THE ENCRATITE CHARGE, HANDLED HONESTLY. **Eusebius** accuses him of it"*, *"written before the events Eusebius describes"*) — all verbatim, and the Eusebius/Irenaeus split §2 A2 draws is exactly right.
- The Antony pair — `alx.figure.antony` (`emic`, `narratable: true`, *"Antony belongs at least as much to the Desert world… and the attribution is held open"*) and `desert.figure.antony` (`emic`, `narratable: true`, `load-bearing`); the `athanasius-vita-antonii` source pair present in both worlds. `hal.figure.augustine` — *"STRICTLY AN OUTSIDE VOICE…"* verbatim; Donatism's Step 0 §A5 does place Augustine among that world's named opponents.
- `ijc.source.lactantius-de-mortibus` — `load-bearing`, referenced by exactly nine other IJC records, ch. 48 and *"the world's most direct witness to its own legal beginning"* verbatim. `grep -rn "Divine Institutes" records/` — **zero** hits across all seven built worlds.
- Cross-world sweep re-run: `records/desert/`, `records/hal/`, `records/cappadocian/`, `records/ijc/`, `records/alx/` hold no figure or source record for any I.35 or I.43 roster name. Every apparent hit is a homonym or a filename string — `ijc.figure.justina`, Theophilus **of Alexandria** in `desert.*` and `alx.source.alexandrian-canonical-answers`, and the `anf02`/`anf06`/`anf07` filename strings.

**Governing documents:** Article 4's five commitments verbatim in both headers (R26 above) and Article 4's closing instruction verbatim in both; Article 23's *"The Representative speaks about the world's opponents as the world understood them — honestly, without rehabilitating them into modern equals and without modern editorializing"* verbatim and correctly applied to the Trypho material; Article 20's scope clause verbatim and I.35's "Article 20 does not apply" right; Methodology A5's first paragraph (both sentences) verbatim, Section B's *"a phase-level process… never a per-world process"* verbatim in both, the Procedure's *"Test each candidate against A1 (and A2 or A3 as applicable)"* verbatim; LPC Step 0 §2 (*"A1 for Augustine, A2 for Cyprian"*, the Article 3 conclusion, the "nothing else" line) and IJC §2 (*"both A1 and A2 apply, to different phases of the same continuous movement… not a forced either/or"*, the Homoian exclusion sentence) both cited correctly in both documents, and both documents' "no precedent exists for a wholly pre-Nicene, non-straddling window" is the honest answer; LPC's state — no `records/lpc/`, **five** Step 0 review rounds on file, Doc_01, Doc_02 and a full Source Registry, row 29 **Excluded / Named Comparandum** with all three reasons verbatim including *"credited with forging this world's own theological vocabulary, not with speaking as this world's own voice"*; `reference/L3B-World-Build-Methodology/CiC_Step0_Conclusion_FINAL_v2.docx` confirmed to hold **nine** worlds with **zero** occurrences of "apologist," "Athenagoras," "Minucius," "Arnobius" or "Lactantius"; `CiC_Step0_Era10_V1_0.md`'s six-section phase-wide structure and `CiC_World_Atlas_PreStep0_Survey_V0_1.md`'s *"It renders no floor verdicts of its own"* and *"A signal, not a B1 score"* both verbatim.

**Census fields:** I.35 `voices` (**seven**, no Tatian, the *Diognetus* line verbatim), `region`, `dates`, `why` (the naming-note quotation verbatim with its marked elision), `sourcing` (Tatian named here only), the Melito *Peri Pascha* line verbatim; I.43 `voices` (**five**, Tertullian **fifth**, both quoted clauses verbatim), `region`, `legacy`, `relationsSummary` (*"kept separate because a voice that distinct is its own entry"*), `sourcing` (*"Two of the four authors are barely datable"*, *"Just under half a million words"*), `why` (*"the least thin of the five gaps he ruled on"*, *"quadrupled the entry's corpus"*, the Arnobius genre/province move), `longDescription` (*"if Jerome is to be believed"*); I.17 Carthage, no works array; I.20 `Excluded - Doctrinal Floor (C1)` with *"Exclusion is not a judgment of unimportance"*; I.24 Contested — Evidentiary; I.33 c. 200–268, Rome, Hippolytus/Callistus roster; era values I.2/I.7 = 1, I.3/I.5/I.6/I.9 = 2.

**Vendored text arithmetic, re-counted with `lxml` from the XML, independent of both documents:**
- I.43 B1 — Minucius Felix **23,819**; Commodian *Instructiones* **15,008**; Arnobius **140,826**; *Divine Institutes* **241,990**; *Anger of God* **20,382**; *Workmanship of God* **18,840**; Fragments **3,932**. **Sum = 464,797** — exact to the word. The *Epitome* nesting also checks to the word: Books I–VII (29,673 + 28,551 + 31,204 + 34,704 + 25,916 + 31,529 + 28,381) = 209,958, + Epitome 32,029 = 241,987, + the division title = 241,990. *De Mortibus Persecutorum* (19,301) correctly excluded as IJC's.
- I.35 B1 — Aristides at `anf09` (`div2 13.3-13.4`); Melito's fragment at `anf08` `div2 10.5` (= x.v); Justin, Athenagoras ×2, Theophilus, Tatian and *Diognetus* all vendored whole across `anf01`/`anf02`; the *Peri Pascha* caveat correctly scoped out of the "strong pass."

**Both documents' status discipline** — "DRAFT, Revision 4. Not yet independently re-reviewed. Not self-disposed. Not Approved to proceed," no build thread opened, next step routed through an independent round rather than self-disposal — remains exactly right, and both §6 sections say so. Both headers' descriptions of Round 4's verdicts (I.35 *"SUBSTANTIAL REVISION REQUIRED, narrowly, no HIGH finding"*; I.43 *"SUBSTANTIAL REVISION REQUIRED, one HIGH finding"*) match `Step0_Round4_Review.md` exactly, and both §6 Round 1/Round 2 paragraphs' finding counts (I.35: four HIGH A1–A4 plus ten A5–A14; I.43: four HIGH B1–B4 plus five B5–B9) were recounted out of `Step0_Round1_Review.md`'s own headings and are right.

---

## Verdicts

### I.35 — The Second-Century Greek Apologists: **NO SUBSTANTIAL REVISION REQUIRED**

**All seven of Round 4's findings are genuinely discharged, and each was re-derived rather than accepted.** §6's Round 3 paragraph now says eleven, and Round 3's Part B does contain exactly eleven. §6's Round 2 paragraph now says ten, and Round 2's Part A does grade exactly those ten (b) or worse — this is the first round in which §6's arithmetic has survived an independent recount. The Tier's fallback sentence was rebuilt from the roster rather than patched for a fourth time, and all six members now sort into three groups that are each correct on the files. The Athenagoras field breakdown (1 `edition:` / 1 `locus:` / 9 body) and the Alexandria breakdown (4 `edition:` / 3 `locus:`) are both exactly right, ending a defect that had survived three rounds at one site and been copied to a second. The stranded "again" is gone with its reason stated, and "roster" now carries one sense per use.

Beyond the seven, the whole document was re-derived: the sixteen-work map and its 15/2/16/0 cross-join, the eight-plus-one Justin arithmetic, PAHC's five Justin records, the Syriac Tatian pair, the Antony and Augustine cross-build models, the Era 1 and Era 2 sweep results, Article 4, Articles 20 and 23, Methodology A5 and Section B, the LPC and IJC precedents, and every census string. **All of it holds.**

**No HIGH. No MODERATE.** Five LOW items remain — **R30** (the Encratite "wine" detail attributed to Irenaeus *AH* I.28, which names marriage and flesh; the detail belongs to Eusebius *HE* IV.29's own apparatus), **R31** (one of Round 4's seven findings located in "§3 B3" when it is in the Tier subsection), **R32** (Round 4 described as confirming all eleven Round 3 findings discharged when its Part A grades R8 (b) — an inconsistency Round 4 itself carries), **R33** ("ten … not seven" and "seven in fact" two paragraphs apart), and **R34** (the Tier's "plus" clause naming two of §4 item 4's three attribution items) — plus four cosmetic notes. Measured against this project's own substantial test (*"changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary"*), **not one of them does any of those four things.** A2 clears, B3's two binding figure questions stand, the Tier is Provisional Tier 1 conditional on two rulings, and every binding obligation in §4 is stated accurately.

R30 is the one item worth acting on before Doc_01, because it is a claim about a named ancient source at a named locus, and because the document's own Syriac source record already points at the right locus for it. The other four are one-clause repairs inside §6 and the Tier sentence.

### I.43 — The Latin Apologists: **NO SUBSTANTIAL REVISION REQUIRED**

**All six of Round 4's findings are genuinely discharged, including the HIGH — and the HIGH is discharged thoroughly rather than formally.** I read Jerome *Ep.* 84.7 in `cic/texts/npnf206_jerome-principal-works.xml` before reading the document's account of it: the vendored translation reads *"Lactantius in his books and particularly in his letters to Demetrian altogether denies the subsistence of the Holy Spirit,"* and the document now quotes that string verbatim, names the vendored file, drops the invented *"in his letters, and especially in those to Demetrianus,"* and rewrites both §2 A2 and §4 item 5 so that the charge reaches the vendored *Divine Institutes* rather than being confined to the lost letters. Jerome's next sentence and the *Institutes*' II.ix two-spirits passage are both quoted verbatim, and the resulting Doc_02 instruction is the stronger, more disclosable one Round 4 said a correct fix would produce. No residue of the narrowed reading survives anywhere in the document.

The five lighter findings are equally discharged: ch. XXIX is now quoted and read one way in both places; the fifth commitment is quoted in full and is character-exact against the Constitution; *De vir. ill.* LXXIX is quoted for what it actually contains — I read the chapter, and it is one sentence long — with the dream-and-bishop story returned to the *Chronicle*; §6's Round 2 count is thirteen and thirteen are enumerated; and B4 claims a shared crisis without a shared province.

Everything else re-derives: 464,797 words to the word, including the *Epitome* nesting; 0/0/0/2/2 across 23,819 words for the *Octavius*; seven corpus-map rows with one `provisional`; Mark's 2026-08-27 per-work ruling verbatim; 33 Tertullian works on the corpus map; LPC row 29's three reasons; IJC's nine citing records; the census's five voices with Tertullian fifth.

**No HIGH. No MODERATE.** One LOW item — **R35**, the R29 fix's *"per §2 A5, B5, and §4 item 4 above"*, where two of the three sit below B4 — plus three cosmetic notes. On this project's own substantial test, nothing here changes a claim's substance, a confidence rating, a sourcing conclusion, or a scope boundary. The document's own binding items are unaffected: the Tertullian/Article 21 boundary and both authors' dating remain the two open pre-Doc_01 questions, correctly stated in §4 and correctly reflected in the Tier.

### Round 6 status

**Not required for either document on the strength of this review.** Both documents have cleared an independent adversarial round without a call for substantial revision, which is the condition this project's own review-gated discipline attaches to eligibility for disposition. The LOW and cosmetic items above are worth a single fix pass, but a fix pass confined to them does not require a further adversarial round before the project lead sees the documents.

Two things this review does not do, and which remain the project lead's:

1. **Neither document self-disposes, and neither should.** Both still carry "Not self-disposed. Not Approved to proceed," no world file-code, and no build thread — correctly, because both are advisory candidate assessments for on-record entries that have not been selected into a release phase, and because §3's own framing note in each document concedes that Section B is a phase-level instrument being run outside its stated scope. A clean review verdict on the *document* is not a selection decision about the *candidate*.
2. **The binding items are still binding.** I.35's Justin ruling and Tatian ruling (§4 items 1–2) and I.43's Tertullian/Article 21 boundary and both authors' dating (§4 items 1 and 4) are unresolved by design, and both documents say so in the right places and at the right strength.

Three process notes, offered because they are the reason this round came out differently from the last four:

1. **The one-sentence rebuild rule worked.** I.35's Tier fallback sentence carried a finding in three consecutive rounds (N5, R1, R19) while it was being patched, and cleared on the first round after it was rewritten from the roster. The Article 4 header sentence has the same history across four rounds. Both are now clean. Whatever is done with R33 and R34 should be a rewrite of the sentence, not a further clause appended to it.
2. **Ancient-source checking is now the productive channel, and it is not exhausted.** Round 4's R24 and this round's R30 both came from opening a vendored translation instead of trusting a prior round's quotation of it. Both documents are now clean on every ancient quotation I could find in them, but the check is cheap and should be part of any future revision's own pass, not only a reviewer's.
3. **§6 remains the least reliable section of I.35**, and three of this round's five LOW items are in it — though all three are precision issues rather than the false counts of the last two rounds. The underlying habit worth keeping is Round 4's: count every number in a revision history out of the review file it describes, with that file open, and give each number an explicit subject so that two true numbers about different things cannot read as a contradiction.
