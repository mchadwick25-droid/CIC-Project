# Step 0 Movement-Scope Confirmations, Apologist Pair — Round 4 Independent Adversarial Review

**Reviewed documents (Revision 3, commit `4a25146a`):**
- `Build/worlds/grkap/Step0_Movement_Scope_Confirmation.md` (Atlas I.35)
- `Build/worlds/latap/Step0_Movement_Scope_Confirmation.md` (Atlas I.43)

**Prior rounds:** `Review-Artifacts/Step0_Round1_Review.md` (commit `09d94033`), `Step0_Round2_Review.md` (`17f981b7`), `Step0_Round3_Review.md` (`919ffcdb`), each duplicated under both worlds. Round 1: SUBSTANTIAL REVISION REQUIRED for both (I.35 A1–A14, four HIGH; I.43 B1–B9, four HIGH; plus a commissioned Era 1 sweep, Part C). Round 2: SUBSTANTIAL REVISION REQUIRED for both. Round 3: SUBSTANTIAL REVISION REQUIRED for both (I.35 R1–R11, one HIGH; I.43 R12–R16, no HIGH).

**Reviewer:** independent isolated agent. No involvement in either draft, in Revisions 1–3, or in Rounds 1–3.

**Overall verdicts:**
- **I.35 (Second-Century Greek Apologists): SUBSTANTIAL REVISION REQUIRED** *(narrowly — no HIGH finding. Every one of Round 3's eleven findings against this document is genuinely discharged, including the HIGH. What remains is two false statements about the repository inside §6's own revision history — one of them the recurrence of the exact defect §6 was rewritten to fix, the other a Round 3 finding reported as fixed that is still wrong — plus a Tier-paragraph enumeration that accounts for five of the six roster members it has just named.)*
- **I.43 (Latin Apologists): SUBSTANTIAL REVISION REQUIRED** — **one new HIGH finding**, older than this revision and missed by two prior rounds: Jerome's charge against Lactantius is quoted in words Jerome did not write, and the misquotation narrows the charge from "in his books and particularly in his letters" to "in his letters" — a restriction the document then builds into §2 A2's clearance reasoning and into §4 item 5's binding Doc_02 instruction. All five of Round 3's findings against this document are genuinely discharged.

Marking per Constitution Article 31: Simulated review — informational only, not an Article 31 substitute.

**A note on method.** Nothing was accepted from either document's §6, and nothing from Rounds 1–3 was taken as a premise; Round 3's own findings were re-tested as claims rather than adopted. Every finding below was re-derived directly from the repository: `cic/corpus-map/*.yaml` parsed and cross-joined with `yaml`; `records/<world>/` read and grepped file-by-file across **all** record subtypes in all seven built worlds, not `figure/` alone; `cic-website/data/world-census.json` parsed and field-tested; `CiC_L1_Constitution_V2_2.docx` (internal Version 2.3) and `CiC_L3B_Step0_Movement_Scope_Methodology_V1.0.docx` extracted from their `.docx` and read; the vendored XML in `cic/texts/` parsed and word-counted with `lxml` independently of every prior round's tables and of both documents' own numbers. Every passage either document presents as a quotation was matched against its source — including, this round, the ancient sources quoted from vendored translations rather than only the project's own records and maps. That last check is where I.43's HIGH comes from.

**Working-tree note.** Both documents and all six prior artifacts were read at `4a25146a` on branch `_round4review/apologists`, fetched from `candidate-worlds-step0-apologists`. No document content was altered; this artifact (duplicated into both worlds' directories) is the only file written.

---

## Part A — I.35, The Second-Century Greek Apologists: Round 3 findings re-tested

Each entry states what Revision 3 claims, what the repository actually shows, and whether the result is **(a) genuinely resolved**, **(b) addressed in form but wrong or incomplete in a new way**, or **(c) unfixed**.

### R1 [was HIGH] — "PAHC's own written records claim only Justin's voice specifically." **(a) Genuinely resolved, and the strongest fix in either document this round.**

§3 B3's governing paragraph is rewritten and every factual claim in it was re-derived from the files, not from Round 3:

| claim | verified |
|---|---|
| `pahc.source.second-third-century-remains.md` is `register: emic`, `evidentiary_weight: load-bearing`, `verification_state: verified-direct` | ✓ exact |
| its `author` field names Quadratus of Athens, Aristo of Pella and Melito of Sardis among **ten** sub-apostolic voices | ✓ exact — ten named authors, counted |
| per-author loci in its own body, *"Quadratus 70010… Melito 70117"* | ✓ verbatim |
| `pahc.quote.melito-no-phantom.md` is `emic`, of *Melito of Sardis, Fragment VII, "On the Nature of Christ"* | ✓ exact |
| it feeds `pahc.gravity.boundary-drawing` as *"a flagged candidate second voice"* | ✓ verbatim in the gravity's own body |
| carried at `evidentiary_weight: contested`, `formation_confidence: Contested` | ✓ exact |
| transmission via Anastasius of Sinai (7th c.) rather than Eusebius | ✓ exact, and the record says so in its own divergence note |
| `pahc.witness.jesus-as-god.md` cites *To Autolycus* II.15 **by locus, twice** | ✓ exact (lines 71–72 and 83–84) |
| Athenagoras, Aristides and the *Diognetus* author unclaimed by any PAHC `source`, `quote`, `gravity` or `doctrinal_witness` record | ✓ — and stronger than stated: a grep of **all fourteen** `records/pahc/` subtypes returns **zero** occurrences of "Aristides" or "Diognetus" anywhere, and every "Athenagoras" occurrence is the vendored `anf02` filename string |

The Tier's fallback roster and §4 item 7 are both corrected to match, and §4 item 7 now instructs Doc_01 to re-derive the finding from `source/`, `quote/`, `gravity/` and `doctrinal_witness/` rather than `figure/` alone. The HIGH is discharged. **Two residues inside the fix — see R19 and R20.**

*One thing the paragraph does not say, offered as a note rather than a finding:* Theophilus is cited a third time, outside the record types the paragraph enumerates — `pahc.demo.center-jesus-as-god.md` carries the same *"Theophilus of Antioch, To Autolycus II.15, c. 180 CE"* locus. It strengthens the document's own conclusion rather than qualifying it.

### R2 [was MODERATE] — the Encratite charge attributed to Irenaeus. **(a) Genuinely resolved.**

`records/syr/source/syr.source.tatian-address-to-greeks.md`, "THE ENCRATITE CHARGE, HANDLED HONESTLY," opens *"Eusebius accuses him of it and this world's figure record carries the charge."* §2 A2 now attributes the report to Eusebius and, usefully, explains in the same clause why Irenaeus appears two paragraphs earlier for a different proposition. Independently confirmed: Irenaeus' *AH* I.28 is headed *"Doctrines of Tatian, the Encratites, and others"* and reads *"Springing from Saturninus and Marcion, those who are called Encratites…"* — exactly the derivation the document attributes to it.

### R3 [was MODERATE] — the corpus map given twenty-one works in B1 and sixteen in B3. **(a) Genuinely resolved.**

`greek-apologists-second-century.yaml` parses to **16** work rows. B1 now states plainly that *"the five items named below are five of the sixteen, not additional to them,"* names them for their flags rather than as an addition, and closes *"B1's 'strong pass' stands at sixteen works."* The five are the three `provisional` Justin works (*Hortatory Address*, *On the Sole Government of God*, *Discourse to the Greeks*), Aristo of Pella and the Ambrose *hypomnemata* — items 7–9, 3 and 1 of the sixteen. No arithmetic now contradicts §3 B3's "16 / 15 of 16 / 2 of 16 / union all 16," each of which I re-derived by cross-joining the three maps on `(author, work)`.

### R4 [was MODERATE] — Part C credited for four Era 2 worlds. **(a) Genuinely resolved, and correctly at both sites.**

Verified from the census: Desert **I.3, era 2**; Cappadocian **I.5, era 2**; Imperial and Juridical **I.6, era 2**; Hieronymian **I.9, era 2**; Alexandria **I.2, era 1**; Syriac **I.7, era 1**; exactly 21 entries carry `era: 1`. §3 B3's bullet and §4 item 7 now both restore the four Era 2 worlds to this document's own direct check and confine the Part C credit to Alexandria and Syriac, and §4 item 7 no longer claims the sweep is "materially complete." The underlying result also re-derived clean: `records/desert/`, `records/hal/`, `records/cappadocian/` and `records/ijc/` hold no figure or source record for any I.35 roster name (the only near-hits remain `ijc.figure.justina.md` and `desert.search.unopened-volume-sweep.md`, which explicitly declines `anf02` and names Theophilus of Antioch as a homonym false positive). **A one-word residue — see R22.**

### R5 [was MODERATE] — Article 4's five commitments asserted as quoted and delivered as paraphrase. **(a) Genuinely resolved, in both documents, and this is the fourth round on this sentence.**

Extracted from `CiC_L1_Constitution_V2_2.docx` (internal Version 2.3) and diffed character-by-character against both headers. **All five commitments are now verbatim in both I.35 and I.43** — including the full fourteen-clause second commitment, the *"'became truly human'"* of the third, the *"under Pontius Pilate… bodily… on the third day… in glory to judge the living and the dead"* of the fourth, and the *"together"* of the fifth that Revision 2 dropped. The only variance is that the internal double quotation marks of commitment (3) are rendered as single quotes inside an outer double-quoted string, which is correct nesting, not an alteration. Article 4's closing instruction (*"the Construction Framework's Step 0 operationalizes it procedurally and must not restate it independently"*) is also verbatim in both. **One residue in I.43's body — see R26.**

### R6 [was MODERATE] — the Tatian dating relabelled rather than cited. **(a) Genuinely resolved and made binding.**

`syr.source.tatian-address-to-greeks.md` reads *"it is an apology addressed to Greeks, written before the events Eusebius describes"* — verbatim as quoted. §2 A2 now rests the pre-divergence dating on that citation rather than an unstated consensus, and §4 item 2 carries it as a requirement on Doc_01, on the same footing as I.43's Commodian dating item. The double standard Round 2 and Round 3 both flagged is gone. **A stranded pointer inside the fix is noted below as cosmetic.**

### R7 [was MODERATE] — Tatian's absence from the census `voices` field. **(a) Genuinely resolved.**

Verified from `world-census.json`, I.35 `voices`: Quadratus; Aristides of Athens; Justin Martyr; Athenagoras of Athens; Theophilus of Antioch; Melito of Sardis; *"The writer to Diognetus - anonymous, undated, and the most quoted of all of them"* — **seven, no Tatian**, and Tatian appears in I.35's census record only inside `sourcing` prose. §2 A2 now carries a dedicated paragraph naming the asymmetry, routing it to Doc_01 as a corpus-map/sourcing question rather than a roster question, and saying so without using it to dodge the ruling. This is the right shape of answer. **The distinction it draws is not held consistently three subsections later — see R23.**

### R8 [was MODERATE] — §6's "four" enumerating six. **(b) The internal arithmetic is fixed; the count put in its place is still wrong, and R8's actual substance is unaddressed and reported as discharged. See R18.**

### R9 [was LOW] — the four-options/four-models correspondence. **(a) Genuinely resolved.**

§3 B3 now carries an explicit correction stating that the options *"draw on the models; they do not mirror them,"* naming both mismatches (opponent has no option; exclude has no model, exclusion not being a cross-build mechanism at all). Exactly the fix required.

### R10 [was LOW] — PAHC's Justin corpus miscounted as nine. **(a) Genuinely resolved, and independently confirmed.**

`post-apostolic-house-church.yaml` parses to **eight** rows at `author: justin_martyr` — three `assigned` (*First Apology*, *Second Apology*, *Dialogue with Trypho*) and five `provisional` (*Hortatory Address*, *On the Resurrection (fragments)*, *On the Sole Government of God*, *Other Fragments from the Lost Writings of Justin*, *The Discourse to the Greeks*) — plus *The Martyrdom of Justin Martyr* at `author: martyrdom_of_justin`, `provisional`. The document now says eight-plus-one-non-Justin-*acta* and the arithmetic closes.

### R11 [was LOW] — §4 item 2 stating only the strong half of the Tatian asymmetry. **(a) Genuinely resolved.**

`syr.figure.tatian.md` verified: `evidentiary_weight: corroborating`, `narratable: false`, body *"Boundary-adjacent: Tatian predates the window…"* and *"without adopting him as a founding teacher."* §4 item 2 now carries the figure-level/source-level asymmetry alongside the `load-bearing` source claim, and instructs Doc_01 to weigh it. The qualification §3 B3 establishes now travels to the binding instruction.

### Round 3's N4 [LOW] sub-finding — **(c) UNFIXED, unmentioned, and now propagated to a second site. See R20 and R21.**

---

## Part B — I.35: findings against Revision 3

### R17. [MODERATE] §6 enumerates eleven Round 3 findings and then says the revision "addresses all fourteen findings directly" — the R8 defect class recurring inside the very paragraph rewritten to fix R8.

§6's Round 3 paragraph names, in order and in bold, **R1, R2, R3, R4, R5, R6, R7, R8, R9, R10, R11** — eleven. The paragraph that follows then lists the fixes, and the eleven fix-clauses map one-to-one onto those eleven findings (the PAHC rewrite; Eusebius; five-of-sixteen; the Part C crediting; the header's five commitments; the Tatian dating; the census `voices` asymmetry; §6's own count; the four-options softening; the eight-works count; §4 item 2's asymmetry). Its opening clause reads:

> *"This revision addresses all **fourteen** findings directly:"*

Round 3's Part B against I.35 contains exactly eleven numbered findings, R1 through R11. Fourteen is the count of **Round 1's** findings against this document, correctly stated one paragraph earlier (*"four HIGH findings… and ten further MODERATE/LOW findings (A5–A14)… Revision 1 addressed all fourteen"*), and it has been carried down into the Round 3 paragraph where it does not belong. No combination of Round 3's Part A regrades reaches fourteen either: Part A marks five entries (b) or (c), each of which routes to one of R1–R11 rather than standing as a separate finding.

This is the same species of defect as R8, in the same section, introduced by the revision written to correct R8 — and Round 3's own closing process note asked specifically for a heading-versus-summary sweep over §6 before submission.

### R18. [MODERATE] §6 now says "seven of Round 1's own findings had been only partially fixed" — Round 2 graded **ten** that way, and Round 3's R8 said so explicitly. The number is reported in §6's fix list as a discharged finding.

> §6, Round 2 paragraph: *"It also found that **seven** of Round 1's own findings had been only partially fixed (A5, A6, A8, A9, A10, A11, A14)."*
> §6, fix list: *"§6's own miscount is corrected to seven."*

Counted directly out of `Step0_Round2_Review.md`'s Part A headings, which grade each Round 1 finding (a)/(b)/(c):

| Round 1 finding | Round 2 grade |
|---|---|
| A1 | **(b)** *"Addressed in substance; the new material misreports the record it cites, and is one-sided."* |
| A2 | **(b)** *"The correction itself is right; its replacement claim is newly wrong."* |
| A3 | **(b) + (c)** *"the rule the revision puts in its place is refuted by the precedent cited two sentences later."* |
| A4 | (a), *"with a new arithmetic error, and a much larger fact still missing"* |
| A5, A6, A8, A9, A10, A11, A14 | **(b)** ×7 |
| A7, A12, A13 | (a) |

**Ten** Round 1 findings carry a (b) grade, not seven. Round 3's R8 said this in terms: *"Round 2's actual count of partially-addressed Round 1 findings is higher still (it graded A1, A2, A3 and A4 the same way)."* Revision 3 has fixed the arithmetic between the stated number and the names in the parenthesis — which was half of R8 — and left the substance R8 named untouched, while §6's fix list reports the item as corrected. The result is a §6 that is internally consistent and externally false about a file sitting in the same directory.

R17 and R18 together are the recurrence Round 3 predicted: three consecutive rounds have now found a miscount in this document's revision history, and each round's fix has produced the next one.

### R19. [MODERATE] The Tier's fallback paragraph names a six-member roster and then accounts for five of them — Theophilus, whose PAHC claim the same subsection establishes, is dropped from the accounting. Third consecutive round of defect in this one sentence.

> *"…the remaining roster is Athenagoras, Theophilus, Aristides, Quadratus, Melito, and the *Epistle to Diognetus* — all `confidence: assigned` on this candidate's own corpus map…"*
>
> *"The fallback candidate is accordingly thinner than even a corrected reading first suggests: a real but visibly thinner candidate, plausibly still a defensible Tier 1 on B1/B2 alone, built now around **three roster members with no claim against them (Athenagoras, Aristides, the *Diognetus* author) plus two more (Quadratus, Melito)** whose PAHC claims are load-bearing for the fragment collection as a whole but not `emic`-figure-level claims on their individual voices the way Justin's is."*

Three plus two is five. The roster named two sentences earlier has six members. Theophilus belongs to neither bucket by the document's own findings: he is not *"with no claim against him"* — §3 B3 establishes, correctly and verifiably, that `pahc.witness.jesus-as-god.md` cites *To Autolycus* II.15 by locus twice — and he is not among the fragment-collection authors either, since he is not named in `pahc.source.second-third-century-remains.md`'s `author` field (I checked: Quadratus, Aristo, Melito, Hegesippus, Dionysius of Corinth, Rhodon, Claudius Apollinaris, Polycrates, Serapion, Apollonius). He is the one roster member whose status is a third thing, and he is the one the sentence drops.

The correction paragraph immediately above this one does state Theophilus' position correctly, so the finding is against the Tier's own reasoning rather than against a fact. But the Tier paragraph is where Mark reads what the fallback candidate would actually be, and it now describes a five-member fallback while naming six. Round 2's N5 found this sentence dropping three census voices; Round 3's R1 found the claim it made about the roster false for two of six members; Round 4 finds its arithmetic short by one. Whatever is done next, this sentence should be rebuilt from the roster rather than patched again.

### R20. [LOW] The new PAHC paragraph says the "Athenagoras" hits in `records/pahc/` are filename strings "in `edition:` fields." One of eleven is; nine are in record body prose.

> §3 B3: *"the only 'Athenagoras' hits anywhere in `records/pahc/` are, again, bare filename-string artifacts (`anf02_hermas-tatian-athenagoras-theophilus-clement-alexandria.xml` in `edition:` fields), not textual claims."*

Enumerated directly — eleven occurrences across `records/pahc/`:

| site | field |
|---|---|
| `pahc.source.shepherd-hermas.md` | `edition:` — **the only one** |
| `pahc.quote.put-away-doubting-from-you.md` | `locus:` |
| `pahc.witness.prayer-and-struggle`, `…marriage-and-wealth`, `…outside-our-community`, `…doubt-and-asking`, `pahc.story.hermas-visions`, `pahc.craft.chloe-voice`, `pahc.demo.identity-collision-womens-authority`, `pahc.demo.identity-collision-divorce`, `pahc.quote.hermas-doubting` | record **body prose** — *"checked directly against cic/texts/anf02_…"* |

The substantive conclusion is right and I re-confirmed it: none of the eleven is a textual claim on Athenagoras. The field attribution is not, and the word *"again"* points back to the same wrong field name in the Alexandria bullet (R21). Minor in itself; recorded because the defect it belongs to has now survived three rounds and has just been copied into a second paragraph.

### R21. [LOW] The Alexandria bullet still says the `anf02` hits in `records/alx/` are "in unrelated records' own `edition:` metadata fields." Four are; three are in `locus:` fields. Round 3 recorded this and asked that it not be restated a fourth time; it is restated verbatim, and §6 does not mention it.

Enumerated directly: `alx.source.clement-stromateis`, `alx.source.clement-protrepticus`, `alx.source.clement-paidagogos`, `alx.source.clement-quis-dives` carry the filename in `edition:`; `alx.quote.to-believe-or-disbelieve`, `alx.quote.couches-and-trenchers-and-bowls`, `alx.quote.the-grades-here-in-the-church` carry it in `locus:`. Seven files, two field types.

Round 3's N4 note read, in full: *"Round 2 said 'an `edition:` field — six files'; the revision inherited the field name and dropped the count. Immaterial to the conclusion, recorded so it is not restated a fourth time."* It has been restated a fourth time, unchanged. The withdrawal of the fabricated Clement-citation detail that surrounds it is correct and I re-confirmed it independently — there are no Clement citations of Tatian, Athenagoras or Theophilus anywhere in `records/alx/`, and the only other "Theophilus" is Theophilus of Alexandria (bp. 385–412) in `alx.source.alexandrian-canonical-answers.md`.

### R22. [LOW] The R4 fix strands an "again" in the bullet below it.

> §3 B3, last built-world bullet: *"**Versus the remaining Era 1 entries**… no further material overlap found — **again** crediting the independent Round 1 review's own Part C sweep as the source of this finding."*

"Again" needs a prior Part C credit in the same list. There is no longer one: the Alexandria bullet credits a direct check against `records/alx/`, the five-built-worlds bullet now explicitly *withdraws* the Part C credit for the four Era 2 worlds, and the Ebionite bullet credits §2 A5. The word is a leftover from the sentence structure Round 3 condemned. The credit it carries is itself accurate — Part C's C7 does cover Montanism, Novatianism, the doctrinal-floor exclusions and the floor-question entries, and its Montanism entry does state the Tatian/Encratism finding the bullet reproduces (*"no ancient source makes Tatian a Montanist, and Irenaeus derives the Encratites from Saturninus and Marcion rather than from Phrygia"*). Only the "again" is stranded.

### R23. [LOW] "Three of this candidate's own roster" is applied to Aristo of Pella, whom §2 A2's own new paragraph excludes from "roster" on exactly the ground that excludes Tatian.

> §3 B3: *"whose own `author` field names, among the ten sub-apostolic voices it covers, **Quadratus of Athens, Aristo of Pella, and Melito of Sardis** — three of this candidate's own roster."*
> §3 B3, ten lines later: *"three more of this candidate's own roster — Quadratus, Melito, and (more narrowly) Theophilus."*
> §2 A2: *"Tatian's presence in this document rests entirely on the corpus map's own assignment… not on the census's own **roster-defining** field."*

Aristo of Pella is not among I.35's seven census `voices`; his presence rests on the corpus map alone, which is the precise ground on which §2 A2 declines to call Tatian a roster member. The same subsection then uses "roster" in the census sense for a different trio. The document is right that Aristo's fragments are on the map at `confidence: assigned`, and §4 item 4 carries his triple assignment properly, so nothing downstream is wrong — but the word "roster" is now doing two jobs in one paragraph, one of them against the distinction the revision was written to introduce.

*Cosmetic, not a finding:* §2 A2's *"Syriac's own source record, quoted immediately below"* points forward to a paraphrase; the quotation it describes is in the same sentence, and the text below renders it without quotation marks. And *"A5's full text, both sentences"* names as A5's full text the first of A5's three paragraphs; the two sentences quoted are exact, and the other two paragraphs are cited accurately elsewhere in the document.

---

## Part C — I.43, The Latin Apologists: Round 3 findings re-tested

**All five are genuinely discharged.** Each was re-derived independently.

### R12 [was MODERATE] — the header's false cross-reference to I.35's Revision 2. **(a) Resolved, and resolved the right way.**

The header no longer points at the sibling document at all. It states I.43's own practice and then performs it: all five of Article 4's commitments quoted verbatim from the Constitution, diffed character-by-character (see R5 above). The document now has an accurate, self-contained statement of how it treats the doctrinal floor, and it cannot go stale when I.35's header moves. **One residue in §2 A2's body — see R26.**

### R13 [was MODERATE] — §4 item 7 crediting Part C for the I.35 comparison. **(a) Resolved.**

§4 item 7 now credits Part C only for I.33 and the remaining Era 1 entries — accurate, C3 and C7 cover both — and states plainly that the I.35 comparison *"is, and was, this document's own direct check, as §3 B3 itself already states."* Verified against Round 1's Part C: C8's own summary bounds it to *"the nineteen Era 1 entries not already checked by the drafts"* (21 era-1 entries minus the two candidates), and no I.43-versus-I.35 comparison appears anywhere in C1–C8. The contradiction with §3 B3 is gone.

### R14 [was LOW] — Tertullian's 33 works placed on his census entry. **(a) Resolved, with the correction shown.**

`cic/corpus-map/tertullian-s-voice.yaml` parses to exactly **33** work rows, including *Ad Nationes*, *To Scapula*, *The Soul's Testimony*, *An Answer to the Jews* and *Apology (Apologeticus)*. Census I.17 carries `voices` and `sourcing` prose and no works array. §2 A5 now attributes the 33 to the corpus map and says so as a marked correction; §3 B3 already did.

### R15 [was LOW] — the Tier paragraph recharacterizing a binding scope item as an ordinary theological disclosure. **(a) Resolved, and well.**

The Tier paragraph now carries an explicit correction distinguishing the dating item (a scope question, prior to A2) from the floor-level theological disclosures (Minucius Felix's Christological absence, Lactantius' pneumatology, Arnobius' anthropology), in the same terms §2 A2's own M3 fix uses. The "ordinary theological disclosures already common to every candidate" phrasing is gone.

### R16 [was LOW] — Commodian's `provisional` corpus-map status undisclosed in B1. **(a) Resolved, and independently confirmed.**

`cic/corpus-map/latin-apologists.yaml` parses to **7** work rows: six at `confidence: assigned` (Arnobius; Minucius Felix; Lactantius ×4) and one at `provisional` — Commodian's *Instructiones* — whose note reads *"The entry is right if the usual 3rd-c. North African dating holds and wrong if the 5th-c. Gallic one does. Nothing in the corpus settles it."* B1 now carries the flag, the count and the quoted reason, and routes it to §4 item 1.

---

## Part D — I.43: findings against Revision 3

### R24. [HIGH] Jerome's charge against Lactantius is quoted in words Jerome did not write, and the misquotation converts "in his books and particularly in his letters" into "in his letters" — a restriction the document then makes load-bearing in §2 A2 and binding on Doc_02 in §4 item 5.

§2 A2, the paragraph answering Round 1's HIGH finding B3:

> *"Jerome (*Ep.* 84.7, to Pammachius and Oceanus) states directly that Lactantius, **"in his letters, and especially in those to Demetrianus,"** "denies the substance of the Holy Spirit, and by a Jewish error says that it is referred either to the Father or to the Son" — a charge against exactly Article 4's fifth commitment."*

The project's own vendored translation, `cic/texts/npnf206_jerome-principal-works.xml`, Letter LXXXIV (confirmed *"To Pammachius and Oceanus"*), section 7 (confirmed — the charge sits immediately after the paragraph numbered "7."):

> *"**Lactantius in his books and particularly in his letters to Demetrian** altogether denies the subsistence of the Holy Spirit, and following the error of the Jews says that the passages in which he is spoken of refer to the Father or to the Son and that the words 'holy spirit' merely prove the holiness of these two persons in the Godhead. **But who can forbid me to read his Institutes** — in which he has written against the Gentiles with much ability — **simply because this opinion of his is to be abhorred?**"*

Two defects, of different weights.

**(i) The quotations are not Jerome's words as this repository holds them.** Neither quoted string matches the vendored text. The second (*"denies the substance… by a Jewish error… referred either to the Father or to the Son"*) is a defensible closer rendering of the Latin — *"Spiritus sancti omnino negat substantiam et errore Iudaico dicit eum vel ad Patrem referri vel Filium"* — so I record it as a citation-form problem: quotation marks are used for a translation the document does not identify and that the project does not vendor.

**(ii) The first quotation is wrong in the vendored translation *and* in the Latin, and it is the half that carries the argument.** *"In libris suis et maxime in epistulis ad Demetrianum"* is "in his books, and especially in his letters to Demetrianus." It is not "in his letters, and especially in those to Demetrianus." The substitution of *books* by *letters* narrows Jerome's charge from Lactantius' written corpus generally — with the letters as its sharpest instance — to the letters alone. Jerome's very next sentence confirms the wider scope by asking who can forbid him to read the *Institutes* despite *"this opinion of his."*

The document then builds on the narrowed reading, twice:

> §2 A2: *"**A distinction §4 item 5 must carry, restored here (Round 2 finding):** the charge attaches **specifically** to Lactantius' letters to Demetrianus, which are lost and are not among the vendored texts in `cic/texts/` — **not to the *Divine Institutes* itself, which is vendored**. Doc_02's disclosure must not read as though the charge were located in the text this candidate actually holds."*
> §4 item 5: *"Jerome's charge (*Ep.* 84.7, to Pammachius and Oceanus, **targeting specifically his letters to Demetrianus — lost, not among the vendored texts**)… distinguishing clearly between the lost letters the charge attaches to and the vendored work this candidate actually holds."*

That the letters to Demetrianus are lost and unvendored is true and worth saying. That the charge attaches to them *rather than* to the *Divine Institutes* is not what the source says, and the document's own §2 A2 supplies material pulling the other way in the same paragraph: it names *"a two-spirits cosmology (II.8–9)"* in the vendored *Institutes*. I read Book II ch. ix directly — it is the passage in which God produces the Son and then *"another being, in whom the disposition of the divine origin did not remain,"* who *"was infected with his own envy as with poison, and passed from good to evil"* — precisely the binitarian-with-a-fallen-second-spirit structure ancient and modern critics attach to the pneumatological charge. The vendored *Institutes* is not outside the charge's reach.

**Why this is HIGH rather than MODERATE.** Round 1's B3 was a HIGH finding because this document gave its anchor figure a clean pass on the one Article 4 commitment where the ancient criticism is sharpest. Revision 1 supplied the disclosure; Revision 2 added a scope restriction that, as written, tells Doc_02 the charge does not touch the work this candidate actually holds. That restriction is not supported by the cited source, is contradicted by the project's own vendored translation of the very letter cited, and now sits inside a binding §4 obligation that will shape what a Doc_02 disclosure says about Lactantius and the Holy Spirit. It alters a claim about a source and about a binding disclosure — the project's own substantial/not-substantial bar, as stated in LPC's Round 5 clearance.

**What a fix requires:** quote *Ep.* 84.7 from the vendored NPNF text (or name whatever translation is used), restore "in his books and particularly in his letters to Demetrian," and rewrite the §2 A2 and §4 item 5 distinction as what it honestly is — the letters are lost and unvendored, so no *primary text* of the sharpest instance can be shown, while the charge itself is levelled at the corpus this candidate does hold. That is a stronger and more disclosable finding than the one the document currently makes, not a weaker one.

This is not a defect Revision 3 introduced. It entered at Revision 2, answering Round 2's B3-LOW, and Round 3 confirmed it discharged (*"Jerome's Demetrianus locus is restored with the lost-letters distinction"*) without testing the quotation against `cic/texts/`. It is recorded here as new because Round 4 is the first round to check it.

### R25. [MODERATE] §2 A2 and the Section A conclusion give incompatible readings of *Octavius* ch. XXIX, and Minucius Felix's A2 clearance rests on which one is right.

> §2 A2: *"The one place the text meets the charge directly, ch. XXIX, **denies that a crucified man could be God** and moves immediately to mocking Egyptian god-kings — it does not affirm the divinity **it declines to deny**."*
> Section A conclusion: *"…the fact that ch. XXIX **declines to deny Christ's divinity rather than denying it outright**."*

The first sentence contains both readings and cannot hold them together; the conclusion adopts only the second. Read directly from `anf04_tertullian4-minucius-felix-commodian-origen1-2.xml`, `div2 iv.iii`, ch. XXIX, the sentence in question is: *"in that you attribute to our religion the worship of a criminal and his cross… you wander far from the neighbourhood of the truth, in thinking either that a criminal deserved, or that an earthly being was able, to be believed God."* Whether that is a denial reaching Christ or a rejection of the pagan's characterization is exactly the live question — and it is the whole of the warrant, since the Section A conclusion states honestly that the clearance is *"an argument from silence plus external inference"* with *"nothing to affirm on this point."*

This is not a demand that the document resolve the question. It is a finding that the document currently answers it two ways in two sections, and that A2's clearance for one of four core figures is resting on the softer of the two without the document ever choosing it. One sentence in §2 A2 fixes it.

*Everything else in the Minucius Felix material re-derives exactly.* Counted independently from the XML: `\bJesus\b` **0**, `\bSon of God\b` **0**, `(?i)incarnat` **0**, `\bChrist\b` **2**, `(?i)crucifi` **2**, division length **23,819 words**. The two `Christ` hits are the ch. XXXVII *Argument* heading (*"Confession of Christ's Name"*) and the footnote *"Legat. pro Christ., ch. xxviii."*; the two `crucifi` hits are the ch. IX *Argument* heading (*"They Worship a Crucified Man"*) and the bracketed gloss at ch. XXIX. All four are ANF apparatus, exactly as §2 A2 and §4 item 3 state.

### R26. [LOW] The header promises verbatim quotation "wherever it must characterize one" of Article 4's commitments; the document's single such characterization is not verbatim.

> Header: *"this document quotes the floor's five commitments verbatim from Constitution V2.3 Article 4 **wherever it must characterize one**."*
> §2 A2: *"a charge against exactly Article 4's fifth commitment (the Spirit as Lord and giver of life, **worshiped and glorified with the Father and Son**)."*

Article 4: *"The Holy Spirit as Lord and giver of life, worshiped and glorified **together with the Father and the Son**."* The parenthetical drops *"together"* and one *"the"* — the same two words Round 3's R5 found dropped from I.35's Revision 2 header. The parenthetical carries no quotation marks, so it is a gloss rather than a false quotation, and the header's five are verbatim; the finding is that the header's stated practice and the one place it applies do not match, on a sentence that has now carried a finding in four consecutive rounds. One-clause fix: quote it, or drop *"wherever it must characterize one."*

### R27. [LOW] *De viris illustribus* 79 is cited for content it does not contain.

> §2 A2: *"All three misattribute to Arnobius what is Jerome's report alone (***De viris illustribus* 79**; *Chronicle* ad ann. 327): Jerome's account is that Arnobius' bishop refused to admit him, doubting a conversion prompted by a dream, and that Arnobius wrote the books as a pledge to obtain baptism."*

The vendored `npnf203_theodoret-jerome-gennadius-rufinus.xml`, *De viris illustribus* Chapter LXXIX, in full: *"Arnobius — flourished 295 — was a most successful teacher of rhetoric at Sicca in Africa during the reign of Diocletian, and wrote volumes Against the nations which may be found everywhere."* No dream, no bishop, no refusal, no pledge. That story is the *Chronicle*'s alone. The substance of the correction — that all three claims are Jerome's report rather than Arnobius' own admission, and that Jerome's version is the reverse of "at his bishop's insistence" — is right, and the census's *"if Jerome is to be believed"* hedge is verbatim from the I.43 `longDescription`. Only the compound citation over-reaches by one locus. Round 2's B6 marked this *"independently confirmed,"* so it has stood two rounds; it is small, and it is the same crediting-precision class the pair keeps failing.

### R28. [LOW] §6 says Round 2 returned "Twelve findings in all" and then enumerates thirteen.

> *"Twelve findings in all (B1(i)–(iv): …; B2: …; B3-LOW: …; B4-MODERATE: …; B8: …; B9: …; M1–M4: …)."*

Counted: B1(i), B1(ii), B1(iii), B1(iv) = 4; B2, B3-LOW, B4-MODERATE, B8, B9 = 5 more; M1, M2, M3, M4 = 4 more. **Thirteen.** Round 3's Part C headed thirteen entries and also called them twelve, so the error is inherited rather than invented — but it is a checkable statement about a file in the same directory, and it is the same enumeration-versus-count drift as I.35's R17/R18. Recorded once so the next revision does not carry it a third time.

### R29. [LOW] B4's "the same province" contradicts the Carthage/Numidia boundary the document now states three times.

> B4: *"a distinct pull for anyone following the North African thread through LPC and Donatism, **the same province and crisis** from the opposite side."*

§2 A5, B5 and §4 item 4 all now insist that Carthage sits outside this candidate's named regions, and the census gives I.43 *"Rome and Ostia; Sicca in Numidia; Nicomedia and Trier"* against I.17's and LPC's/Donatism's Carthage. The crisis is genuinely shared; the province is not. Round 3 flagged this as cosmetic; it is now the one sentence in the document that still reads as though the Carthage exclusion had not been drawn. Two words.

*Cosmetic, not a finding:* §4 item 7 renders Part C's scope as *"the entries not already checked by the drafts"* inside quotation marks; Part C's own words are *"the nineteen Era 1 entries not already checked by the drafts."* The claim carried is accurate.

---

## What checked out clean (verified directly this round, not carried from Rounds 1–3)

Recorded so a fifth revision does not disturb settled ground.

**Corpus maps, re-parsed and cross-joined:**
- `greek-apologists-second-century.yaml` — **16** rows; 15 also on `post-apostolic-house-church.yaml`; 2 also on `syriac-edessa-nisibis.yaml` (Ambrose *hypomnemata*; Tatian's *Address*); union **16**; assigned to I.35 alone **0**.
- Tatian's *Address* at `confidence: assigned` in all three maps; the note *"Tatian sits awkwardly across two entries… Mark may want a ruling on where his voice sits"* — verbatim.
- Aristo of Pella on three maps, with *"The Jewish-Christian current and pahc are both defensible; neither is demonstrated by the fragments"* — verbatim.
- The Ambrose *hypomnemata* — `provisional`, ruled 2026-08-26, *"greek-apologists-second-century is added, which is where the argument belongs, and syriac-edessa-nisibis is kept, which is how it reached us"*; the `provisional` reason is the date, and there is no Quadratus content of any kind.
- The three pseudonymous Justin works and their two distinct notes (*"Same position as the Discourse: transmitted under Justin, widely doubted"* for the *Hortatory Address* and *On the Sole Government of God*; *"Printed under the JUSTIN MARTYR div1; authenticity has long been questioned. Filed with its transmitted author per §6.2 - derive, don't assert - with the doubt recorded"* for the *Discourse*) — both verbatim, both attributed to the right work.
- *Epistle to Diognetus* — *"some put it after the entry's 200 CE close"* verbatim; vendored in `anf01`. *Dialogue with Trypho* ch. 47 — *"one of the era's few direct witnesses to the ebionite-nazoraean-current material"* verbatim.
- `post-apostolic-house-church.yaml` — 68 rows; the Justin arithmetic as at R10 above.
- `latin-apologists.yaml` — 7 rows, 6 `assigned` / 1 `provisional`; Mark's 2026-08-27 ruling verbatim including *"THE RULING SPLITS THE AUTHOR, WHICH IS WHAT `per work` MEANS"* and the Athanasius sentence; Arnobius *"MOVED 2026-08-27 from latin-pastoral-congregational-christianity"*.
- `tertullian-s-voice.yaml` — 33 rows. `latin-pastoral-congregational-christianity.yaml` — no work by Arnobius, Lactantius, Minucius Felix or Commodian.

**Built-world records:**
- All five PAHC Justin quotations in §3 B3 — `pahc.quote.moses-is-more-ancient` (`load-bearing`, 1 Apol. XLIV, *"an apologetic claim about chronology made to a pagan audience"*); `pahc.quote.those-who-lived-reasonably-are-christians` (`load-bearing`, tier 1, *"which cites this exact chapter for 'the Logos present in every race of men'"*); `pahc.quote.the-memoirs-of-the-apostles-are-read`'s divergence note; `pahc.figure.justin`'s `bridge_line`, `emic`, `narratable: true`, `locus: whole work` on both source records; `pahc.source.justin-dialogue`'s WEIGHT note and Ways-That-Never-Parted caution (which is a Doc_01 §2.1 caution, as the document says); `pahc.source.justin-first-apology`'s *"clearest inside evidence that the rival movements were live, contemporary, and undefeated."* All exact.
- `pahc.source.justin-first-apology`'s WEIGHT note independently confirms §3 B2's worship-practice claim: *"chapters 61 and 65-67 are the fullest early descriptions of baptism and Sunday worship anywhere in this world's base."*
- `syr.figure.tatian` (`corroborating`, `narratable: false`, *"Boundary-adjacent"*, *"without adopting him as a founding teacher"*, the Diatessaron `bridge_line`) and `syr.source.tatian-address-to-greeks` (`load-bearing`, *"Every argument for Tatian belonging to the Syriac East runs through the statement that he was an Assyrian"*, *"written before the events Eusebius describes"*) — all verbatim.
- The Antony pair — `alx.figure.antony` (`emic`, `narratable: true`, `illustrative`, *"Antony belongs at least as much to the Desert world… and the attribution is held open"*) and `desert.figure.antony` (`emic`, `narratable: true`, `load-bearing`); the `athanasius-vita-antonii` source pair exists in both worlds. `hal.figure.augustine` — *"STRICTLY AN OUTSIDE VOICE: Augustine belongs to his own (not-yet-built) world; this record draws on him ONLY as the other side of the correspondence"* verbatim; Donatism's Step 0 §A5 does place Augustine among that world's named opponents.
- `ijc.source.lactantius-de-mortibus` — `load-bearing`, referenced by exactly nine other IJC records, ch. 48 and *"the world's most direct witness to its own legal beginning"* verbatim. `grep -rn "Divine Institutes" records/` — **zero hits** across all seven built worlds; every Minucius/Arnobius/Commodian occurrence anywhere in `records/` is a vendored filename string.

**Governing documents:**
- Article 4's five commitments — verbatim in both headers (R5). Article 4's closing instruction — verbatim. Article 23's *"The Representative speaks about the world's opponents as the world understood them — honestly, without rehabilitating them into modern equals and without modern editorializing"* — verbatim, and correctly applied to the Trypho material. Article 20's scope clause (*"The scope of this duty is the marginalized within the community… It does not extend to the community's external opponents"*) — verbatim, and I.35's "Article 20 does not apply" is right.
- Methodology A5's two sentences, Section B's *"a phase-level process, run once when the project opens a new release phase, never a per-world process,"* and the Procedure's *"Test each candidate against A1 (and A2 or A3 as applicable)"* — all verbatim in both documents. A2's own text confirms the continuity/rival-current framing both documents use.
- LPC Step 0 §2 (*"A1 for Augustine, A2 for Cyprian"*; the "nothing else" line bounding what Step 0 tests; the Article 3 conclusion) and IJC §2 (*"both A1 and A2 apply, to different phases of the same continuous movement… not a forced either/or"*; the Homoian exclusion sentence) — both cited correctly in both documents, and both documents' "no precedent exists for a wholly pre-Nicene, non-straddling window" is the honest answer.
- LPC's state — no `records/lpc/`; **five** Step 0 review rounds on file, the fifth returning *"VERDICT: CLEARED — LOW/COSMETIC ONLY"*; Doc_01, Doc_02 and a full Source Registry present. Source Registry row 29 — **Excluded / Named Comparandum**, all three reasons verbatim, including *"credited with forging this world's own theological vocabulary, not with speaking as this world's own voice."*

**Census fields:** I.35 `voices` (seven, no Tatian), `region`, `dates`, `why` (including the naming-note quotation with its marked elision, and *"ATHENS IS NOT AMONG ITS NAMED REGIONS"*), `sourcing` (Tatian named here only); I.43 `voices` (five, Tertullian fifth, *"whose Apology of 197 begins the whole enterprise"* and *"has an entry of his own rather than a place in this one"*), `region`, `legacy`, `relationsSummary`, `sourcing` (*"Two of the four authors are barely datable"*), `why` (*"the least thin of the five gaps he ruled on"*, *"quadrupled the entry's corpus"*), `longDescription` (*"if Jerome is to be believed"*); I.17 Carthage, no works array; I.20 `Excluded - Doctrinal Floor (C1)` with *"Exclusion is not a judgment of unimportance"* in its `statusDescription`; I.24 Contested — Evidentiary; I.33 c. 200–268, Rome, Hippolytus/Callistus roster; era values I.2/I.7 = 1 and I.3/I.5/I.6/I.9 = 2; 21 entries at `era: 1`.

**Vendored text arithmetic, re-counted with `lxml` from the XML:**
- I.43 B1 — Minucius Felix **23,819**; Commodian *Instructiones* **15,008**; Arnobius **140,826**; *Divine Institutes* **241,990**; *Anger of God* **20,382**; *Workmanship of God* **18,840**; Fragments **3,932**. **Total 464,797** — exact, and the *Epitome* nesting checks to the word (Books I–VII 209,958 + Epitome 32,029 = 241,987, plus the division title = 241,990).
- I.35 B1 — Aristides at `anf09` (`div2 13.3-13.4`); Melito's fragment at `anf08` `div2 x.v` (confirmed: x.v is *"Melito, the Philosopher"*); Justin, Athenagoras ×2, Theophilus, Tatian and *Diognetus* all vendored whole across `anf01`/`anf02`; the Melito *Peri Pascha* caveat correctly scoped out of the "strong pass," with the census `voices` line quoted exactly.
- Ancient sources: Irenaeus *AH* I.28 (*"Doctrines of Tatian, the Encratites, and others"*; *"Springing from Saturninus and Marcion…"*) — correctly used in I.35. Lactantius *Div. Inst.* Book VII chiliasm and Book II chs. viii–ix two-spirits cosmology — both present as I.43 describes.

**Both documents' status discipline** — "DRAFT, Revision 3. Not yet independently re-reviewed. Not self-disposed. Not Approved to proceed," no build thread opened, next step routed through an independent round rather than self-disposal — remains exactly right, and both §6 sections say so.

---

## Verdicts

### I.35 — The Second-Century Greek Apologists: **SUBSTANTIAL REVISION REQUIRED** *(narrowly — no HIGH finding)*

**Round 3's HIGH is genuinely and thoroughly discharged, and every one of R2–R11 with it.** I re-derived the whole of §3 B3's PAHC paragraph from the files rather than accepting it: the load-bearing `emic` source record and its ten named authors, the per-author loci, Melito's `emic` quote record at `contested` weight and its place in `pahc.gravity.boundary-drawing`, the twice-cited Theophilus locus in `pahc.witness.jesus-as-god.md`, and the genuinely-unclaimed status of Athenagoras, Aristides and the *Diognetus* author — this last checked across all fourteen `records/pahc/` subtypes, not the four the paragraph names. The corrected statement is right, the Tier and §4 item 7 were brought into line with it, and the paragraph now keeps the corpus-map test and the records test apart while getting both of them right. That is the first time in four rounds this has happened.

The rest of the round's work also holds: the Encratite charge is Eusebius'; the sixteen-work arithmetic closes; the Part C crediting is confined to the two genuinely Era 1 worlds and the four Era 2 worlds are returned to this document's own check; Article 4's five commitments are verbatim, ending a three-round defect; the Tatian dating is cited and binding; the census `voices` asymmetry is named and correctly routed; the four-options claim is softened to what it can support; the Justin corpus is eight works plus one non-Justin *acta*; and §4 item 2 carries the figure-level asymmetry.

The verdict is not COSMETIC ONLY because three findings remain that are not cosmetic:

- **R17** — §6 enumerates eleven Round 3 findings and then states that the revision *"addresses all fourteen findings directly."* Round 3's Part B against this document contains eleven. The number is Round 1's, carried down from the paragraph above. This is the R8 defect class recurring inside the paragraph rewritten to fix R8, and Round 3 asked specifically for a §6 sweep that would have caught it.
- **R18** — §6 now says *"seven of Round 1's own findings had been only partially fixed."* Counted out of Round 2's own Part A headings, **ten** carry a (b) grade. Round 3's R8 said so in terms. §6's fix list reports the item as corrected.
- **R19** — the Tier's fallback paragraph names a six-member roster and then accounts for five, dropping Theophilus, whose PAHC claim the same subsection establishes. Third consecutive round of defect in this one sentence, after N5 and R1.

Plus **R20** and **R21** (a wrong `edition:`-field attribution, unfixed from Round 3 at one site and newly copied to a second), **R22**'s stranded "again," and **R23**'s two senses of "roster" in one paragraph.

None of these alters a test outcome, the Tier grade, or the substance of a binding obligation. Two of them are false statements about files sitting in the same directory as the document, and one is an enumeration gap inside the Tier's own reasoning. On this project's own bar — and on the standard Round 3 applied to I.43 for two false statements and three LOWs — that is substantial, and it is close to the line. The required work is small: three sentences and four clauses.

The repeat-failure pattern held for a fourth time, but it is visibly weakening. Round 2 introduced two HIGHs; Round 3 introduced one HIGH; Round 4 introduces none. What remains is concentrated almost entirely in §6, which is now the least reliable section of an otherwise substantially verified document.

### I.43 — The Latin Apologists: **SUBSTANTIAL REVISION REQUIRED**

**All five of Round 3's findings against this document are genuinely discharged**, each independently re-derived: the header states its own Article 4 practice and performs it verbatim, with no cross-reference that can go stale; §4 item 7 credits Part C for I.33 and the remaining Era 1 entries only and returns the I.35 comparison to this document; Tertullian's 33 works sit on the corpus map; the Tier paragraph distinguishes the scope question from the theological disclosures; and B1 discloses Commodian's `provisional` row with the map's own stated reason. The sourcing arithmetic reproduces to the word at 464,797, and the Minucius Felix counts reproduce exactly at 0/0/0/2/2 across 23,819 words. On its own review record this document had converged further than its sibling by Round 3 and it converged further again here.

The verdict is HIGH because Round 4 checked something no prior round did — the ancient sources quoted from vendored translations rather than only the records and maps:

- **R24 [HIGH]** — Jerome's charge against Lactantius (*Ep.* 84.7) is quoted as *"in his letters, and especially in those to Demetrianus."* The vendored NPNF text reads *"Lactantius in his books and particularly in his letters to Demetrian,"* and the Latin (*"in libris suis et maxime in epistulis ad Demetrianum"*) says the same. The misquotation narrows the charge from Lactantius' written corpus to his lost letters, and §2 A2 and §4 item 5 then build that narrowing into a binding instruction that *"Doc_02's disclosure must not read as though the charge were located in the text this candidate actually holds"* — against a source whose very next sentence asks who can forbid Jerome to read the *Institutes* *"simply because this opinion of his is to be abhorred,"* and against §2 A2's own citation of a two-spirits cosmology in the vendored *Institutes* II.8–9, which I read directly and which is exactly the structure the charge concerns. This is the same commitment — Article 4's fifth — on which Round 1's B3 HIGH was raised. The disclosure is present; its scope is wrong, in a way that understates what Doc_02 must disclose about the candidate's anchor figure.

Underneath it: **R25**, ch. XXIX read as a denial in §2 A2 and as a declining-to-deny in the Section A conclusion, with Minucius Felix's A2 clearance resting on which reading holds; and four LOW items — **R26** (the header's "wherever it must characterize one" against §2 A2's non-verbatim gloss, fourth round on this sentence class), **R27** (*De vir. ill.* 79 cited for the *Chronicle*'s content), **R28** (§6's "twelve" enumerating thirteen), **R29** (B4's "the same province" against the Carthage boundary the document now states three times).

R24 is not a defect Revision 3 introduced. It entered at Revision 2 and Round 3 confirmed it discharged without testing the quotation against `cic/texts/`. It is reported here because it is real, material, load-bearing on a binding obligation, and this is the first round to check it.

### Round 5 status

Not run. Neither document should open a build thread. Both should be revised against the findings above and re-reviewed, per `cic-build-cycle`'s review-gated discipline and both documents' own §6.

Three process notes for whoever runs the next revision:

1. **§6 is now the highest-defect section in I.35, by a wide margin.** R8 (Round 3), R17 and R18 (this round) are all in it, and R28 is its I.43 counterpart. Every number in a revision history should be counted out of the review file it describes, with the review file open, before the paragraph is written — and the count of a *prior* round should never be reused in the paragraph about a *later* one, which is exactly how R17 happened.
2. **Quotation checking has to reach the ancient sources, not stop at the records and maps.** Three rounds verified every corpus-map note, every record field and every census string in both documents, and all of them hold. R24 sat untouched through all three because nobody opened `cic/texts/npnf206` and read the letter. Any clause of the form "X states that…" about an ancient author is checkable against the vendored translation in one read, and both documents contain several.
3. **The one-sentence rebuild rule.** I.35's Tier fallback sentence has now carried a finding in three consecutive rounds (N5, R1, R19), each time because the previous round's patch was applied to the sentence rather than the sentence being rewritten from the roster. The same is true of the Article 4 header sentence across four rounds, which was finally fixed by writing it out in full rather than adjusting it again. A sentence on its third finding should be rebuilt, not repaired.
