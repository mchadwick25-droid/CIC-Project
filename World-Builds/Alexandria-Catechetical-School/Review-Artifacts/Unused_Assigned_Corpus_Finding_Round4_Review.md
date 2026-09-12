# Unused Assigned Corpus Finding (Peter / Theognostus / Pierus) — Round 4 Independent Adversarial Review

**Simulated review — informational only, not an Article 31 substitute.**

World: Alexandria (Catechetical-School) Formation World · Reviewed: `Analysis/Unused_Assigned_Corpus_Finding_2026-09-09.md` (Round 4 draft, revised after Rounds 1–3) and the **OG-6** entry in `Open_Gaps_Tracking.md`
Reviewer role: independent adversarial. Did not author the finding document, any of the three prior review artifacts, the discovery pass, or any Doc_04 round. Brief: **do not trust §11.** Verify each of Round 3's four substantial findings against the patch and against primary sources; audit the corrected OG-6 entry; independently re-run the new §6.2 and the screened §6.1; and state plainly whether any route to a Doc_04 classification change remains, including outside the frame of all prior rounds.
Method: `git log`, `git show --stat` and `git diff 09c23d6..a44648c` read hunk by hunk, plus `git diff --stat b50302d^..a44648c` and `git status --porcelain` to confirm the pass's total footprint; `Open_Gaps_Tracking.md` read in full and its heading structure enumerated with `grep -n '^#'`; `cic/corpus-map/alexandria-catechetical.yaml` re-parsed with PyYAML (14 `anf06` rows enumerated, `confidence` field tallied); `anf06…xml` tag-stripped and read directly for the **whole Peter fragment division** (`div2 ix.vi`, lines 27779–28157) so that ANF's provenance note for *each* of Fragments I–IX could be read rather than taken from Round 3's table, for the Theognostus division (`div2 vi.v`, 15787–15957), for Canon IV and Canon IX (26757, 27036), and for the Dionysius epistles (`div3 iv.iii.ii`, 9780–11706, all fourteen epistle headings and their source notes); `Doc_04` §0–§9, `Doc_02` §2 (Streams 3, 5, 7, 8, 12) and §6, `alx.gravity.martyrdom-contemplative-tension`, `alx.source.dionysius-extant-fragments`, `alx.source.alexandrian-canonical-answers` read in full; the three prior review artifacts read in full before the document.
Date: 2026-09-09

---

## VERDICT: SUBSTANTIAL REVISION REQUIRED

**The headline is correct for the fourth time, and I could not break it.** "This material is **not structural**" survives. I re-ran every route the prior three rounds ran, checked Round 3's C3 / T2 / generation-step results against the sources myself, and ran one route no round has named — whether this corpus generates a candidate **Tensional** gravity (confessor-authority vs episcopal-authority), which is a different question from Round 3's organizing-force generation step. It fails. See §E. I state plainly, as the brief asks, that **I know of no route to a Doc_04 classification change.**

**Round 3's four findings are three RESOLVED and one PARTIALLY RESOLVED whose fix introduced a new error**, and the new error is the same one three rounds have now caught in three different places: a source claim engaged, or asserted, at a scope its evidence does not carry. The correction Round 3 demanded at N3-3 — recast "contradicted" as "omission" — was right, and the recast landed everywhere Round 3 asked. But the *replacement* claim is false against the record it describes, and unlike its predecessor it is false in the ledger too.

**What is genuinely better this round, and should be said first.** The four fragment provenances in §6.1 are exactly right against ANF's own notes; "one saying in three witnesses" is right and I verified it by reading III, IV and VIII in full; the Theognostus disciple-of-Origen correction is verbatim and its consequence is drawn correctly and against the document's own interest; §6.2's three route results are fairly represented against Doc_04 and Doc_02, and the Askesis / Participation↔Perception precedent is invoked exactly as Doc_04 §2 writes it; the OG-6 defect list now matches the document's three-produced / two-pre-existing structure; and the pass's footprint is still, verifiably, five files and nothing else.

Counts this round: **3 substantial, 14 cosmetic** (12 of the 14 carried unrepaired from Round 3). Substantial-finding trajectory: **8 → 8 → 4 → 3.** The disposition (§9 Option B, escalated, not self-disposed) remains sound and should stand.

---

## A. ROUND 3's FOUR — VERIFIED INDEPENDENTLY

I did not read §11 as evidence. Each was checked against `git diff 09c23d6..a44648c`, against the document body, and against the primary source.

| Round 3 | Subject | Round 4 status |
|---|---|---|
| N3-1 | OG-6's defect list drops §5.4, inflates the T1↔T4 cell to a free-standing defect | **RESOLVED** |
| N3-2 | §6.1's C4 evidence unscreened; III/IV/VIII one saying; §5.2's "non-Origen voice" | **RESOLVED** |
| N3-3 | §5.3's "contradicted" charge reads a scope-limited clause at a wider scope | **PARTIALLY RESOLVED — FIX INTRODUCED NEW ERROR** (N4-1) |
| N3-4 | "§6.1 … the last untested route" self-contradicting | **RESOLVED** |

### N3-1 — **RESOLVED.**

The patch rewrites `Open_Gaps_Tracking.md` lines 266–291 (−15/+22). The entry now reads *"**Three defects produced by this corpus**… — the §-numbers are the finding document's"* and enumerates **§5.1**, **§5.3** and **§5.4**, with the T1↔T4 cell demoted to *"Its sub-finding"* inside item 2, and a separate paragraph *"Two further defects found along the way, pre-existing and NOT produced by this corpus"* carrying **§5.2** and **§5.5**. That is exactly the document's own §1 / §8 structure, and the Option B recommendation *"scoped reopen of Doc_04 §5.1–§5.4"* is now covered by an enumeration that actually states §5.4. The stale Round 2 citation *"(SUBSTANTIAL, 8 new)"* is corrected to *"8+10"*, Round 3 is added at *"4+12"*, and a new paragraph puts the negative route results on the ledger. I checked every factual assertion in the rewritten block against disk: the 14-assigned / 2-opened parse (my own PyYAML run returns 14 `anf06` rows, 8 of them `confidence: assigned`), Alexander's zero records, the *Sacra Parallela* provenance for Fragment VI, the two-freezes split, and the untouched `records/worlds.yaml` pin. All hold.

**Against the brief's third test — does it match the file's entry conventions?** Substantively yes; typographically no. OG-6 is still a `##` heading (line 247) where OG-1 through OG-5 are all `###` (77, 93, 104, 207, 240), so it still renders as a new top-level section rather than a sixth ledger item. Round 3 raised this as c-6; it is unrepaired. Cosmetic, and recorded as c-6 below rather than counted against N3-1, whose substance did land.

### N3-2 — **RESOLVED, and accurate to ANF's own notes.**

I read the whole of `div2 ix.vi` rather than checking the four notes Round 3 tabulated, so that a fifth unscreened fragment could not hide. The provenances the document now prints are verbatim correct:

| Fragment | ANF's own note | Document's gloss | Verdict |
|---|---|---|---|
| II — On the Godhead | *"from the Acts of the Council of Ephesus, i. and vii. 2.—Galland."* | *Acts of the Council of Ephesus* (431) | ✓ |
| III — On the Advent | *"Apud Leontium Byzant., lib. i., contra Nestor. et Eutych."* | Leontius of Byzantium, *contra Nestorianos et Eutychianos* | ✓ |
| IV — On the Sojourning | *"Ex Leontio Hierosolymitano, contra Monophysitas, Ap. Mai."* | Leontius of Jerusalem, *contra Monophysitas* | ✓ |
| VIII — On St. Matthew | *"From the Treatise of the Emperor Justinian against the Monophysites."* | Justinian's treatise against the Monophysites | ✓ |

"5th–6th-century christological-controversy excerpt" is right for all four, and applying the §5.1 screen to them on the same terms is right. *(A control the document does not need but which I ran: Fragment IX, which §6.1 does not cite, carries no provenance note beyond "Or, from a treatise on theology" and repeats Fragment II's Annunciation material — so the section's evidence base is not quietly wider than it is screened.)*

**"One saying in three witnesses" is right**, and the three quotations are transcribed exactly. III closes an exposition of Luke 22:48 with *"Both things therefore are demonstrated, that He was God by nature, and that He was man by nature"*; **IV is that sentence and nothing else** (the whole fragment is one line); VIII is Justinian quoting Peter on the *Matthew* parallel of the same betrayal-kiss, ending *"both things therefore are together proved, that He was God by nature, and was made man by nature."* Same exposition, same clause, three quoters. The document's *"Counting them as three independent attestations inflates the evidence"* is exactly the right conclusion, and it is drawn against its own evidence.

**The §5.2 Origen-disciple correction is accurate and its consequence is carried through correctly.** ANF's Theognostus notice reads, verbatim: *"That he was a disciple of Origen, or at least a devoted student of his works, is clear from Photius."* The document quotes it exactly, places him **inside** Doc_04 §0's Discipline One (Origen SYSTEMIC screen), and concludes he *"cannot lift it."* That is right. On the brief's follow-up — **can frag. III still corroborate C3 at all?** — yes, and the document says the right thing in the right register. Being an Origen disciple removes the fragment's value as *Origen-independent* corroboration; it does not remove its value as a datum. It remains a distinct author, writing c. 260 (i.e. inside the 254–296 interval), whose surviving text carries divine-pedagogy vocabulary. The document's landing — *"an Origen disciple, quoted selectively by Athanasius in post-Nicene polemic. It corroborates C3 and reclassifies nothing (§6.2)"* — is the accurate residue, and §5.2 correctly keeps the whole passage flagged as *"Texture, offered as corroboration and explicitly not as a classification argument."* I re-verified the frag. III quotation verbatim at `div2 vi.v`.

### N3-3 — **PARTIALLY RESOLVED; the fix introduced a new error.**

**The half that landed is real and is exactly what Round 3 asked for.** The heading is now *"[SUBSTANTIAL — omission] T4 carries no documentary witness among its manifestations."* The scope concession is stated in the document's own voice — both loci say *"**its interior** is preserved in hagiography and martyrology only,"* the interior verdict stands, *"the wording is **not contradicted**."* I re-verified both loci: `alx.gravity.martyrdom-contemplative-tension`'s `description` and `Doc_04` line 137 (*"but its interior is Tier-3 hagiography / Coptic martyrology, held at **Inferential-Thin**"*). And the recast **is** fully propagated, which the brief asked me to check specifically: §8 now reads *"§5.3 (a documentary witness omitted from T4's manifestations)"*; §9 Option B now reads *"add Peter's canons to T4's `manifestations`… leaving the Inferential-Thin interior verdict untouched"* in place of *"correct T4's 'hagiography and martyrology only'"*; §9 Option A now reads *"T4's documentary omission"* in place of *"a contradicted characterization"*; and §8's bolt-on paragraph is reworded to match. §1 required no change (it names §5.3 only by number and never characterised the charge) and correctly received none.

**The replacement claim is false.** See **N4-1**. In short: T4's `manifestations` do carry a documentary witness — *"Dionysius's persecution letters — flight, confession, the lapsed"* — and this world holds them at `Documented` / `verified-direct` / specificity A.

### N3-4 — **RESOLVED.**

The heading is now plainly *"### 6.1 C4 Logos-Centered Unity"*; the completeness claim is gone; the "half-route named and not run" paragraph is deleted and replaced by a new **§6.2** carrying C3 Dependency, T2 and the generation step as run results. I checked §6.2's three results against the sources rather than against Round 3's write-up:

- **C3.** `Doc_04` §3.3 grounds C3's Supporting status on Dependency: *"removed while C1 and C2 remain, the practices persist but lose their explanatory ground — it is a meta-framework… not an independent organizing force."* §6.2's reasoning — Theognostus frag. III generates no practice; the only practice-cluster in the corpus (Peter's canons) grounds itself on episcopal authority and Scripture, so removing C3 leaves it standing — is a correct application of that test, and I reach the same verdict. **C3 remains Supporting.** ✓
- **T2.** `Doc_04` §3.6 T2's community pole is `Inferential-Thin`; §6.2's reasoning is the one `alx.source.alexandrian-canonical-answers` already supplies and §6 already applies. Correctly stated. ✓
- **The generation step.** The candidate is properly generable on Doc_04 §1's own rule (*"elements recurring across multiple Doc_02 streams"*): Stream 3 carries *"fasting, vigils, penitential practice,"* Stream 7 carries *"discipline and the reintegration of the lapsed,"* Stream 8 carries the two persecutions — all three verified verbatim. The Dionysius→Peter→Timothy→Theophilus chain is real and is the chain `alx.source.alexandrian-canonical-answers` itself names. **The Askesis and Participation↔Perception precedent is invoked exactly as Doc_04 §2 writes it** — Askesis: *"a genuine urban ascetic practice, but as a practice serving C2, not an organizer in its own right"*; D-A: *"it is what mutual Scripture-engagement (C1) and soul-transformation (C2) produce, not what produces them."* §6.2's *"it is what the ecology does under persecution, not an independent organiser"* is a faithful structural parallel. **The route result is correct: not a gravity.** ✓

The *reporting* of that last result is over-strengthened relative to the run it summarises — **N4-3** below. The route inventory claim itself (*"no remaining untested route"*) I tested against a route outside all four rounds' frame; see §E.

---

## B. §11's OWN ACCURACY — CHECKED AGAINST THE PATCH

Round 2 found §11 overstating; Round 3 found it honest. **Round 4: §11 does not materially overstate what landed.** I matched each of its five claims to the hunk that implements it:

| §11 Round 3 → 4 item | Landed? |
|---|---|
| 1. §6.1 — one saying, and the four provenances screened | ✓ both paragraphs present at lines 455–472, and correct against ANF |
| 2. "Non-Origen voice" withdrawn | ✓ lines 282–289, quotation verbatim |
| 3. §5.3 recast, retitled, propagated to §1, §8, §9 Option B | ✓ retitle, §8 and §9 Option B all landed. **§1 did not change** — and needed no change; the claim names one locus more than the patch touches (c-13) |
| 4. §6.2 added | ✓ lines 484–509 |
| Also: OG-6's defect list corrected | ✓ `Open_Gaps_Tracking.md` −15/+22 |

The closing line *"This entry is written to the same standard"* is fair for §11 itself. It is not fair for **§10**, which the same revision left untouched and which is now stale in two ways — but §11 makes no claim about §10, so this is a finding against §10 (**N4-2**), not against §11.

One inherited overstatement, in the same class Round 3 recorded: §11 item 3 says the recast was propagated to §1; the header's Round 3 summary says *"Of Round 2's 8: **7 resolved**, 1 partial"* where Round 3's own summary line reads *"6 RESOLVED · 1 RESOLVED FOR ITS OWN LOCUS BUT NOT CARRIED FORWARD · 1 PARTIALLY RESOLVED"* and its opening says *"Six of the eight are cleanly resolved."* Both cosmetic (c-13, c-14). The three round counts in the header (8+8, 8+10, 4+12) are exactly right against the three artifacts.

---

## C. NEW SUBSTANTIAL FINDINGS (Round 4)

### N4-1 [SUBSTANTIAL — the replacement claim is false against the record it describes, and it is in the ledger] "T4's manifestations carry no documentary witness" is not true

This is the brief's fourth independent check, and I read the record rather than the document's account of it. `alx.gravity.martyrdom-contemplative-tension`'s `manifestations`, in full:

1. *"Leonides's martyrdom and the young Origen restrained from joining him (HE VI.1-2 — story lead)"* — Eusebius, narrated.
2. *"Origen's imprisonment and torture under Decius (HE VI.39)"* — Eusebius, narrated.
3. *"**Dionysius's persecution letters — flight, confession, the lapsed**"*
4. *"the contemplative pole: the school's ascent language (Stromateis; the Address)"*

Item 3 is a documentary witness on the martyrdom pole by the document's **own** definition. §3.4 defines what makes Peter's epistle documentary — *"documentary, first-person, and contemporaneous… It is not hagiography"* — and Dionysius's persecution letters satisfy every clause: first-person letters written by the bishop of Alexandria during and immediately after the Decian persecution, on the identical subject matter (§5.3's own list leads with flight, the lapsed, and confession). I read them: Epistle I *To Domitius and Didymus*, Epistle III *To Fabius* (Dionysius's own account of the Alexandrian confessors, the lapsed and the martyrs), Epistle IV *To Cornelius* — fourteen epistles at `div3 iv.iii.ii`. The world's own source record `alx.source.dionysius-extant-fragments` carries them at `citation_specificity: A`, `verification_state: verified-direct`, `formation_confidence: **Documented**`, `evidentiary_weight: load-bearing`, and its body names *"Decian persecution as lived experience, the lapsed and their reintegration."*

So the claim *"T4's `manifestations` list contains **no documentary witness at all**, only narrated and hagiographic material"* is false twice over: item 3 is documentary, and item 4 (*Stromateis*, the *Address*) is a treatise and an oration — neither narrated nor hagiographic. The document's own preceding sentence concedes the problem without seeing it: *"three of that record's four manifestations are Eusebius/**Dionysius**-derived."*

This is not a wording slip, for three reasons. It is the **section heading** (*"T4 carries no documentary witness among its manifestations"*). It is **in the ledger** — OG-6 item 2 reads *"T4's `manifestations` carry **no documentary witness** — only narrated and hagiographic material"* — so the one project-lead-facing artifact this pass leaves behind now asserts it. And it is in the **remedy**: §9 Option B asks the lead to add Peter's canons *"as its **only** documentary witness,"* which would enter a false uniqueness claim into Doc_04 and the record store if executed as written. That makes it a sourcing conclusion and a scope boundary — substantial on this project's own definition.

**What survives is real, and is narrower.** Peter's canons are distinctive against T4's existing manifestations in two ways that Dionysius's letters are not, and either one carries the finding:

- **They are juridical, not narrative.** Nothing in T4's manifestations is *legislation about* martyrdom — a text in which the church rules on flight, bribery, self-offering and the readmission of the lapsed, rather than narrating or lamenting them. §5.3's own Elucidation II paragraph already establishes the point (the canons' standing is *synodical*, *"after the manner of synodical decisions"*), and this is precisely what makes the T1 × T4 intersection argument work: T1's bishop-authority pole **adjudicating** T4's martyrdom pole. That sub-argument, and the missing T1↔T4 Interaction Matrix cell, are untouched by this correction and stand.
- **They are outside Eusebius's selection.** T4's other three martyr-pole manifestations are Eusebius-mediated — the two `HE` citations directly, and the Dionysius letters by the record's own admission (`work` field: *"surviving mostly through Eusebius's quotation and later catenae: doubly mediated"*). Peter's canons reach the corpus through the canon-law tradition instead, and via a second vendored witness (npnf214 `div2 17.6`). Given that Doc_04 §0 runs a Eusebius screen as a named subordinate discipline, "T4's martyr pole rests entirely on Eusebius-mediated material" is a **stronger** finding than the one the document now makes, and it is true.

**Required:** restate §5.3's heading and claim to one of the two surviving forms (juridical witness absent; or no non-Eusebius-mediated witness), correct the same sentence in OG-6 item 2, and change §9 Option B's *"as its only documentary witness"* to match. Do **not** simply revert to Round 2's "contradiction" wording — Round 3 was right about that, and this correction is a further narrowing in the same direction, not a reversal.

### N4-2 [SUBSTANTIAL — the disclosure section is again inaccurate about what is on disk] §10 was not updated in this revision

§10 is the section Round 2's most serious finding produced, and its stated standard is its own: *"**Files this pass adds** — stated as of this revision, and **verifiable on disk rather than promised**."* The revision that made this the Round 4 draft did not touch it. `git diff 09c23d6..a44648c` contains no §10 hunk. Two consequences, both checkable in seconds:

1. **The file list is incomplete.** It names this document, the Round 1 review, the Round 2 review and the OG-6 entry. `git show --stat a44648c` adds a fifth file in the same commit: `Review-Artifacts/Unused_Assigned_Corpus_Finding_Round3_Review.md` (+230 lines), which exists on disk. A section that says "verifiable on disk rather than promised" now omits one of the five things this pass has put on disk.
2. **The status bullet contradicts the header.** §10 reads *"**Not cleared.** **Two** adversarial rounds have both returned SUBSTANTIAL REVISION REQUIRED. This is the **Round 3 draft**."* The header at line 5 reads *"Round 4 draft (revised after three adversarial rounds)"* and enumerates all three. A reader of §10 alone would take the document to be one round less tested than it is and would not know a third review artifact exists.

The direction of the error is the opposite of Round 1's finding S-8 — this understates rather than inflates the document's standing — but the defect class is identical, and it is the class this document has now been caught in three times (Round 1 header, Round 2 §10, here). The remedy is four words and one list item; what makes it substantial is that §10 is the section a project lead reads to learn what actually changed on disk, and it is now wrong about that.

**Required:** add the Round 3 review artifact as item 4 (renumbering OG-6 to 5), and change the "Not cleared" bullet to *"Three adversarial rounds… This is the Round 4 draft."* If a Round 4 artifact is added, that too.

### N4-3 [SUBSTANTIAL — a route result reported at a strength its own run does not support] §6.2's generation-step verdict

The brief asked whether penitential-reintegrative discipline is *fairly* tested against Doc_04's six tests. The precedent invocation is fair (verified above). The reporting is not, in two connected ways.

**(a) The Persistence verdict is hardened, and the qualifier that was dropped is the load-bearing one.** §6.2 reports: *"Tested against the six tests it **fails**: Persistence fails in the early phase, and Dependency fails decisively."* The run it summarises (Round 3 §E) reads: *"**Persistence — FAILS the early phase.** It is a crisis response to Decius (250) and Diocletian (303–311); there is no Clement-phase attestation of it as an organising cluster. **At best PARTIAL, on the pattern `Doc_04` used for C5.**" The dropped clause matters, because **C5 is a Supporting gravity that carries exactly that PARTIAL** — `Doc_04` §3.5: *"Persistence — assessed first and is the critical test → **PARTIAL PASS**."* On Doc_04's own precedent an early-phase persistence failure does **not** disqualify a candidate; it temporally qualifies it. So the document reports two failures where its source ran one PARTIAL (non-disqualifying by the world's own precedent) and one FAIL. The single decisive test is Dependency, and saying so plainly would be both true and stronger. Round 3's Repetition **PASS** is likewise not reported, so a reader is given "it fails the six tests" with the pass and the partial removed.

**(b) The verdict clause contradicts itself.** *"**Not a gravity; Supporting at most; nothing existing moves.**"* In Doc_04's scheme **Supporting is a gravity classification** — C3, C4 and C5 are Supporting gravities. "Not a gravity, Supporting at most" therefore says two incompatible things, and the second of them, read literally, concedes that this corpus could add a Supporting gravity to Doc_04 — which would be a Doc_04 classification change and would sit against §1's headline. The hedge *"nothing **existing** moves"* does not close that gap. Doc_04 §2's own vocabulary for a declined candidate of exactly this shape is available and unambiguous: Askesis is *"not a gravity (urban supporting practice only)… a practice serving C2, not an organizer in its own right."* The OG-6 version of this same result is already clean (*"it fails the six tests on Doc_04's own Askesis and Participation↔Perception precedent"*) and carries neither defect — so the ledger is right and the document is wrong, which is the inverse of N4-1 and worth noticing as such.

**This does not change the outcome.** I re-ran the candidate independently and reach the same place: it is not a gravity, it fails Dependency decisively on the D-A and Askesis precedents, and its practice-cluster sits inside T1's bishop pole and C2's restorative dimension. The finding is that a correct result is reported at a strength its own working does not support, in the section on which the document's closing "no remaining untested route" claim rests.

**Required:** report the run as it was run — Repetition PASS, Persistence PARTIAL (on the C5 precedent, therefore not disqualifying), Dependency FAIL (decisive, on the Askesis / D-A precedent) — and replace *"Supporting at most"* with Doc_04 §2's own formula for a declined candidate.

---

## D. COSMETIC FINDINGS

**Every one of Round 3's twelve cosmetics is unrepaired.** I confirmed by string search that each locus is unchanged, and personally re-verified c-1, c-2, c-4, c-6, c-7 and c-8 against the sources. §11's Round 3 → 4 entry claims no cosmetics, so this is not a false claim — but six of the twelve have now survived two rounds and three have survived three.

- **c-1.** §6.1 (line 479) still prints *"the theological ***centre***"* where `Doc_04` line 120 reads **"center"**, and still truncates *"…makes the other gravities cohere"* without an ellipsis (the source continues *"into one ecology rather than four activities"*). Round 3 c-1.
- **c-2.** §3.1 (line 98) still says a bare grep for `peter` *"returns two Origen commentary records — the apostle and the *Gospel of Peter*."* I re-ran it: the only two hits are the anf09 **filename** inside `edition:` fields (`alx.source.origen-comm-john.md:18`, `alx.source.origen-comm-matthew.md:18`). "The apostle" is not a hit at all. Round 2 c-5, Round 3 c-2 — a control note offered as evidence of rigour that has now been wrong for three rounds.
- **c-3.** §5.4 (line 365) still calls *"From his demonstration that the soul was not pre-existent to the body"* a heading; it is inside endnote 2382, and the heading is *"Of the Soul and Body."* Round 2 c-6, Round 3 c-3.
- **c-4.** §5.3 (line 322) still folds Canon IV into *"Canons I–V — a graded penitential scale."* I read Canon IV: it is the **refusal** of the scale — *"To those who are altogether reprobate, and unrepentant, who possess the Ethiopian's unchanging skin… Let no fruit grow on thee henceforward for ever."* Round 2 c-7, Round 3 c-4.
- **c-5.** §5.3's *"Fragment I is confessor-prestige asserting ordaining authority against the office"* still over-reads Fragment I, whose stated grievances are that Meletius *"is not contented with the letter of the most holy bishops **and martyrs**,"* is *"invading my parish,"* and seeks *"pre-eminence."* The confessor testimony is on Peter's side. Round 2 c-6, Round 3 c-5. *(This one now does double duty: it is also why §E's new tensional-generation route fails.)*
- **c-6.** OG-6 is still a `##` heading (`Open_Gaps_Tracking.md` line 247) where OG-1…OG-5 are `###` (77, 93, 104, 207, 240). Round 3 c-6.
- **c-7.** §2's table still says `Doc_04` was *"read in full (all 9 sections)."* It has ten, §0–§9, and §0 is the one §5.1 turns on. Round 3 c-7.
- **c-8.** §3.5's *"14 works assigned to Alexandria from anf06"* still uses "assigned" in the membership sense three lines from `confidence: assigned` in the field sense; my PyYAML parse gives **8** of the 14 at `confidence: assigned`. Round 2 c-3, Round 3 c-8.
- **c-9.** §6.1 and now §6.2 are both filed as subsections of §6, *"The Article 21 substitute (Cross-Stratum Test),"* which neither is about. With §6.2 added, the mis-filing is worse than when Round 3 raised it: the document's entire route inventory now hangs off a heading that names a different test, and OG-6 gives no locus for it. Round 2 c-9, Round 3 c-9.
- **c-10.** *"roughly a quarter-century earlier"* (line 376) is still the outer edge of a 14–25 year range and still understates against the Origenist controversy, the second element of the phrase it measures itself by. Round 3 c-10.
- **c-11.** §9 Option C still calls §5.1 *"a plain factual error"* though `Doc_04` §0's sentence is a hedged collective (*"…reaching us **largely** through Eusebius"*) that is true of Heraclas. Round 1 C-5, Round 2 c-10, Round 3 c-11 — three rounds.
- **c-12.** §3.4's Canon XI sentence still has no clear subject in its first clause. Round 3 c-12.
- **c-13.** *(new)* §11 item 3 says the §5.3 recast was *"propagated to §1, §8 and §9's Option B wording."* §8 and §9 changed; **§1 did not** (and needed no change — it names §5.3 only by number). One locus more than the patch touches.
- **c-14.** *(new)* The header's Round 3 summary — *"Of Round 2's 8: **7 resolved**, 1 partial"* — rounds Round 3's own three-category tally (*"6 RESOLVED · 1 RESOLVED FOR ITS OWN LOCUS BUT NOT CARRIED FORWARD · 1 PARTIALLY RESOLVED"*, and *"Six of the eight are cleanly resolved"*) into the document's favour. Defensible, since Round 3 also wrote that the item-6 fix *"landed exactly where Round 2 asked"* — but it attributes to Round 3 a count Round 3 did not give.
- **c-15.** *(new)* OG-6 now carries **two** route-test lists: the "Finding: NOT structural" paragraph still says *"Routes tested and failed: C5 Persistence, T1 pole separation, T3, T4 confidence, C4, and the Cross-Stratum Test"* — the pre-Round-3 list — while the later paragraph adds C3 Dependency, T2 and the generation step. Not false, but a lead reading top-down meets the short list first. Fold the first into the second.

---

## E. THE HEADLINE, RE-TESTED — AND A ROUTE OUTSIDE ALL FOUR FRAMES

**"NOT structural" is correct. Fourth round, fourth confirmation.**

**Re-confirmed on re-run, against the sources rather than the prior artifacts:** C1/C2 (nothing in this corpus reduces Scripture or soul-transformation; additive material cannot demote a Primary, and the stratum qualification is §6's business, run and unchanged); C3 Dependency (`Doc_04` §3.3's test applied correctly — the canons ground on episcopal authority and Scripture, not divine pedagogy; **Supporting** confirmed); C4 (fails on `Doc_04` line 120's practice-cluster criterion, and fails harder now that its witnesses are correctly screened and correctly counted); C5 Persistence (`alx.figure.didymus` was always the disproof, and it is already inside the store); T1 pole separation (`Doc_04` line 132's *"not a polarity within one person"* is verbatim, and the document's inversion of the discovery pass is right — a proven one-man overlap would have been evidence **against** T1); T2; T3 (Fragment VI is real, correctly quoted, correctly screened for its *Sacra Parallela* transmission, and strengthens without reclassifying); T4 (the canons are juridical throughout and contain no martyr's interior; Inferential-Thin stands — a verdict N4-1 does not disturb); the Article 21 Cross-Stratum Test / OG-4 (unchanged, for the reason `alx.source.alexandrian-canonical-answers` already supplies in its own voice).

**The route I ran that no prior round has named.** Round 3 opened the generation step and ran it for an *organizing-force* candidate. It did not run the generation step for a **Tensional** candidate, and Doc_04 generates those under a different rule (§3.6: *"two genuinely distinct poles with real population, institutional, or practice-cluster separation"*). This corpus supplies the most obvious one it could: **confessor/martyr authority vs episcopal authority.** Peter's Fragment I is the Melitian rupture in one paragraph; Canon X permanently bars clergy who volunteered, lapsed and re-contested; Canon XIV has Peter citing letters imprisoned martyrs sent *to him*; Dionysius's Decian letters supply the earlier instance; Streams 7 and 8 both carry it. On Doc_04 §1's generation rule it is generable, and it is in neither the §1 candidate table nor the §2 not-advanced list. I ran it:

- **Repetition — weak PASS at best.** Two streams, two persecution crises, no early-phase instance.
- **Persistence — FAILS, and not in the recoverable C5 way.** The confessor pole exists only while there is persecution to make confessors. After 313 it does not attenuate; it has no referent, and what remains (the Melitian schism) is a jurisdictional dispute between bishops.
- **Pole separation — FAILS, which is fatal for a Tensional.** Confessors are not a population, an institution or a practice-cluster; they are a transient status conferred by an external force (`alx.force.persecution`, which the T4 record already relates to). And the corpus's own best instance cuts against the reading: in Fragment I, Peter's complaint is that Meletius *"is not contented with the letter of the most holy bishops **and martyrs**"* — the martyrs' authority is **on Peter's side**, not opposite it. This is the substance of the unrepaired cosmetic c-5, and it closes the route.
- **Dependency — FAILS.** Remove it while T1 and C1/C2 remain and nothing collapses: the authority question is T1's, the readmission practice is the penitential cluster Round 3 already tested and declined, and the scriptural argument is C1's.

**Result: not a Tensional gravity; nothing moves.** It fails on the same criterion by which Doc_04 §2 already declined Individual–Communal (*"it lacks the population/institutional/practice-cluster separation a tensional pole requires"*).

**Stated plainly, as the brief asks: I cannot find any route — inside or outside the frame of the prior three rounds — to a Doc_04 classification change on this material.** Every organizing-force candidate has been run, the Tensional generation step has now been run, the Article 21 substitute has been run, and the confidence-rating routes (T2's community pole, T4's interior) fail on a distinction this world's own record store already draws and states in its own voice. The headline has been upheld four times, and the case under it has narrowed at every round rather than strengthening — which is itself the strongest evidence that the headline is right. What remains genuinely open is not a route; it is **§3.5's unaudited remainder**, and above all **Alexander of Alexandria's *Epistles on the Arian Heresy*** — `assigned`, directly transmitted rather than florilegium-mediated, zero records, and by the document's own §5.4 the stronger end of the T3 chain. That is a different pass, correctly named and correctly not pursued here.

---

## F. DISCIPLINE COMPLIANCE

| Requirement | Result |
|---|---|
| Declines to self-dispose | **PASS, verified on disk.** `git diff --stat b50302d^..a44648c` shows the pass's entire footprint as **five files**: the finding document, `Open_Gaps_Tracking.md`, and the three review artifacts. No Doc_01–Doc_09 file, no `records/alx/` file, no corpus-map edit, no `records/worlds.yaml` change (still pinning `packages/alx/2026-09-04T16-41-49Z`), no recompile, no `Gravity_Index.xlsx` created. `git status --porcelain` is empty, so what I read is what is committed. §8's four reasons, §9's three grounded options, §10's negative inventory and OG-6's *"Status: OPEN — awaiting project-lead disposition"* all hold. Escalation categories 2 and 4 correctly identified. |
| No unverifiable project-lead attribution | **PASS.** `grep -n "Mark"` over the document returns **nothing**. §3.2 dates the npnf214 split (2026-08-26) without attributing the ruling, though the corpus map itself says *"on Mark's ruling"* — the more conservative choice, and the right one. §8 cites the S6.2 declaration by date. §10: *"No claim that any of this was seen or approved by the project lead."* The corrected OG-6 introduces no attribution. |
| Claims no status it has not earned | **PASS at the header; FAIL at §10.** The header states all three prior outcomes accurately (8+8, 8+10, 4+12 — all verified against the artifacts), says *"Round 4 review pending — this document is NOT cleared, and no disposition has been assigned to it,"* and adds an unflattering trajectory note in its own voice. §10 contradicts it — **N4-2**. Note the direction: §10 *understates* the document's standing. The failure is accuracy about disk state, not self-promotion. |
| Grounded options preserved | **PASS.** Three options with cost, precedent and stated reason; a named recommendation; the portfolio-level §7 decision separated out and explicitly not run; the recompile/re-admission question reserved to the project lead. Option B's wording inherits N4-1 and must be corrected with it. |
| Still declines to edit Doc_04 / records / compile | **PASS.** Verified above. §10's negative inventory is accurate on every line except the file list. |
| Accurate self-report of its own revision | **PASS with two carry-throughs.** Checked against `git diff 09c23d6..a44648c`, not against §11's prose: all four substantial items landed as body edits, and the OG-6 correction landed as claimed. c-13 (one locus over-claimed) and c-14 (a tally rounded in its own favour) are the exceptions, both cosmetic. No phantom claims this round. |
| Ledger entry accurate against the document | **PASS on structure (N3-1 resolved); FAILS on one clause.** OG-6's enumeration now matches §1/§8 exactly and its factual content checks out line by line — but item 2 carries N4-1's false claim into the one project-lead-facing artifact, and c-15 leaves two route lists standing. |

---

## G. SUMMARY

- **Overall verdict: SUBSTANTIAL REVISION REQUIRED.**
- **Headline: CORRECT, re-confirmed a fourth time and against a route no prior round ran.** "Not structural" survives C1, C2, C3, C4, C5, T1, T2, T3, T4, the Article 21 Cross-Stratum substitute, Round 3's organizing-force generation step, and Round 4's Tensional generation step. **No route to a Doc_04 classification change is known to me, inside or outside the prior rounds' frame.** §9 Option B, escalated, should stand — extended to cover N4-1's restatement.
- **Round 3's four: 3 RESOLVED** (N3-1, N3-2, N3-4) · **1 PARTIALLY RESOLVED, FIX INTRODUCED NEW ERROR** (N3-3 → N4-1).
- **New substantial: 3** — N4-1 §5.3's replacement claim ("no documentary witness") is false against T4's own manifestations and is propagated into OG-6 and the Option B remedy; N4-2 §10 was not updated and now misstates the round count and omits the Round 3 artifact from a list whose stated standard is on-disk verifiability; N4-3 §6.2's generation-step result is reported at a strength its own run does not support, with a self-contradicting verdict clause.
- **New cosmetic: 3** (c-13, c-14, c-15) plus **all twelve of Round 3's carried unrepaired**; three of those (c-2, c-11, and the c-5/c-6 family) have now survived three rounds.
- **What this revision got right and must not lose.** The four fragment provenances are exactly right against ANF's own notes, and I checked all nine fragments rather than the four the document names, so the screen is complete and not merely applied where it was demanded. "One saying in three witnesses" is right and is the kind of correction that costs the author something. The Theognostus disciple-of-Origen correction is verbatim, and the consequence is drawn to the document's own disadvantage and stopped in exactly the right place — corroboration survives, screen-lifting does not. §6.2's Askesis and Participation↔Perception invocations are faithful to Doc_04 §2 word for word, and the generation-step candidate is genuinely well-generated from Streams 3, 7 and 8. OG-6 now matches the document it summarises and carries the negative route results, which is the right instinct for a ledger. The scope concession at §5.3 — conceding that the sentence it had attacked was not wrong — is the hardest kind of correction to make and it was made cleanly and propagated. And the footprint discipline is unbroken across four commits: five files, nothing in `records/`, nothing in Doc_01–Doc_09, nothing recompiled.

*(This is a simulated AI review. It does not substitute for the Article 31 external scholarly review that OG-4 still requires. A qualified subject-matter reviewer on the transmission of Dionysius's Decian correspondence through Eusebius's selection, on the standing of the Alexandrian penitential canons as synodical rather than personal instruments, and on the Melitian chronology would be the accountable test of §5.3, §5.4 and §6.1.)*
