Review cap ruling, don record audit fixes, 2026-10-13
Reviewer model: Opus 5.5
Verdict: BLOCKING

## Scope

The one targeted recheck ordered by the project lead's cap ruling of 13 October, branch `records/don-audit-fixes`, against the pass brief (scratchpad `BRIEF.md`). Limited to:

1. `ff180ee` - nine `use_note.means` corrections.
2. `c3c0988` - open-item commentary removed from seven live records (three force, four source), and `positions[1]` of `don.dw.what-we-did-with-the-power-we-had` rewritten.
3. `14f634d` - changes made in response to the independent review: the catholicus wording in `don.witness.boundary-is-doctrine` and `don.dw.the-word-catholic-and-no-door-today`, the Emeritus re-rendering, the source-record `divergence_note` and trailing spaces, three loci, the Tyconius manifestation in `don.force.transmission-caecilianist-victory`, and the `don.term.liber-regularum` means grammar.
4. `fd8fce4` - `horizon` of `don.core.donatism`, `description` of the three gravity records and the grief-and-vindication note of `don.craft.fidelis-voice` reverted to origin/main wording, keeping only the source-checked fixes.

Read-only on records. Nothing outside these commits was reviewed.

## BLOCKING

### B1. `don.core.donatism`, `horizon` - wrong count of Gregory letters that name rebaptism

- Exact text: "Four of his letters, directly read, still urge suppression, a council, and an inquiry. Two of them name Donatist rebaptism in Africa, and the 592 letter is addressed to a bishop in Numidia."
- Why: this is the factual fix kept inside the reverted field, and it is wrong against the vendored letters. Three of the four letters name Donatist rebaptism, not two. `gregory-great_epistolae-selectae_turchi1907.txt`: the 592 letter to Columbus, "post catholicum baptisma a Donatistis denuo baptizari" (about l.11739-11740); the 594 letter to Pantaleon, "rebaptizare" (about l.11908); the 594 letter to Victor and Columbus, "rebaptizantes" (about l.12041). The sentence as written also reads as though the 592 letter does not name rebaptism. That contradicts `don.gravity.rebaptism-boundary` in the same world (divergence_note and locus: "in Numidia in 592, in Africa in 594") and `don.gravity.rebaptism-boundary-marking` manifestations[2] ("reporting that Donatist rebaptism was spreading").
- Fix: "Four of his letters, directly read, still urge suppression, a council, and an inquiry. Three of them name Donatist rebaptism, and the 592 letter is addressed to a bishop in Numidia." This changes the count only. No other change to the reverted field. Re-run the field gate. The field is already under the `m1:readability/don` waiver per OG-35, and this edit adds no new failure.

### B2. `don.quote.donatus-quid-est-imperatori`, `sources[1].locus` - build material on a participant source card

- Exact text: "Book III, chapter 3 -- the Latin original, in Ziwsa's critical edition (CSEL 26), corrupted by OCR at this line"
- Why: brief item 3 says loci show to participants on source cards and must not leak build material. "Corrupted by OCR" describes this build's digitised scan, not Ziwsa's edition. "At this line" points to a line number that was correctly removed, so it now refers to nothing. The phrase also misleads: it tells a participant that the critical edition itself is corrupt. The same edition's clean transcription in the corpus reads correctly: `optatus_libri-vii-lat_ziwsa1893-csel26-tei.txt` l.3357, "quid est imperatori cum ecclesia?". Only the older scan (`optatus_libri-vii-critical_ziwsa1893.txt` l.6557) is garbled. Restoring the phrase does not keep a hedge on the claim. The OCR caveat is a build note and already stands in full in this record's `confidence.divergence_note`, which is where it belongs.
- Fix: "Book III, chapter 3 -- the Latin original, in Ziwsa's critical edition (CSEL 26)", which is the wording the earlier pass logged (OG, "Under `don.quote.donatus-quid-est-imperatori`"). The divergence_note's "No clean vendored transcription of this Latin exists in the corpus" is stale for the same reason. That is a build-field correction to log for the build thread, outside this recheck.

## NON-BLOCKING

1. `don.force.conference-of-411-verdict` `sources[0].locus`, restored text "not yet read into a specific claim": this is process narration on a source card. The same hedge stands in this record's `divergence_note` ("the material exists; it has simply not been read") and in its body, so the locus could drop it without losing the hedge. It is not a file path or line number, and the independent review asked for it, so it is left non-blocking. Recommend the build thread decide this together with B2. The `don.term.liber-regularum` locus dropped the parallel phrase "not read in depth by this build", so the two loci are inconsistent.
2. `don.story.gesta-apud-zenophilum` `use_note.means` now says "pieces of money". The spoken `text`, `tellable_as` and `don.dw.what-we-did-with-the-power-we-had` still say "pieces of silver". The Latin is "quadringentis follibus" (`optatus_appendix-decem-monumentorum-lat_ziwsa1893-csel26-tei.txt` l.314), and the vendored English uses both "money" (`optatus_against-the-donatists.txt` l.6198, 6552, 6776) and "silver" (l.6572). So both renderings are defensible, and this is a wording mismatch rather than a contradiction. The OG entry for `ff180ee` already logs it as out of scope. The rest of the line holds: the witnesses were asked about Lucilla's 400 (l.6776, 6800).
3. Stale catholicus hedges in build fields. `don.term.catholicus` (`divergence_note`, `senses.evidential`, `senses.informational`, the first source locus), `don.witness.boundary-is-doctrine` (`use_note.not_for`: "a claim that the pun on catholicus is attested beyond a modern editor's annotation", and the source locus "per Mabillon's annotation") and `don.dw.the-word-catholic-and-no-door-today` (`divergence_note`, `tensions`, `not_for`) all still say the turn reaches us only through Mabillon. The spoken fields and the catholicus means now state it directly, which is correct (see Verified). The direction of the mismatch is safe, because it makes the voice over-cautious. OG (14f634d entry) logs it for a change order. Small log error in the same OG entries: the passage sits in section XII of the sermon, not XI. The "XII. At vero memoratus episcopus" heading is at l.621, and the catholica sentence continues at l.646-649. Mabillon's note "XI. Subvenite" (l.740) refers to the preceding section.
4. `don.craft.fidelis-voice` grief-and-vindication note (origin/main wording, correctly reverted): "Isaac and Maximianus put to death together" is loose against the corrected story (Isaac died in prison; Maximianus was sunk alive). This is base wording, outside the listed fixes, and should be logged for the build thread, not changed here.
5. `don.gravity.church-of-the-martyrs` `description`: besides the listed fixes, "The Passio Donati sermon's own admonition describes a yearly commemoration" became "...sermon itself speaks of an anniversary day kept with devotion". That is outside the list in the review order, but it is named in OG-35 and it is a correct factual fix. The "IN SEQUENTEM SERMONEM ADMONITIO" is Mabillon's preface (pl8 l.103-125), and the sermon's own words are "anniversalis dies religiosa devotione ... celebratur" (sec. IX, l.541). It stands.
6. `don.term.liber-regularum` and `don.limit.theology-beyond-tyconius` `use_note.means` mix we-voice ("of ours", "our record", "we argued") with third person ("his side"). This is not a defect under the brief, because `means` is not a spoken field, but most means lines are third person.
7. `don.quote.emeritus-magno-argumento` `modern_rendering` keeps the Latin's single sentence, with a colon in place of "ut". The colon carries the explanatory link, and the clause after it elaborates the one thought, so this passes. "Device" in the sense of a ploy is slightly literary. The world's build already glosses "magno argumento" that way, and it does not mislead.

## Verified

Fourteen facts were checked against `cic/texts/`. Each item below gives the claim and the passage checked.

1. The catholicus turn is in the Donatist sermon's own text, not only in Mabillon's note. `monumenta-vetera-donatistarum_migne-pl8.txt` l.646-649: "qualis esse possit apostasia, si digne talis appellatur catholica. Nam et hoc ... ut eam vulgo dici fecisset catholicam, ubi impune committitur quicquid publico jure damnatur." The spoken lines "turned your word back on you, as the place where wrong goes unpunished" and "named the place where wrong is done and nobody is punished for it" are supported. Removing "A modern editor reports" is correct and returns both texts to the origin/main substance.
2. Honoratus of Sicilibba was wounded: sec. VIII, l.526-527, "Honoratum sanctissimi Scilibensis episcopi jugulum tribuni gladius etsi non penetravit, tamen compunxit."
3. The bishop of Advocata is rightly hedged "on Monceaux's reading" / "on one reading". Mabillon's own note (l.743-748) takes the "memoratus episcopus ex Abvocatensi oppido" to be Honoratus himself, so a separate Advocata bishop killed is one reading among others.
4. Mabillon dates the persecution to about 340: l.185 of the admonitio, "contigisse circa annum 340, aut paulo post". The vendoring header agrees.
5. The anniversary day was kept with devotion: sec. IX, l.541.
6. The 592 letter is addressed to Columbus, a bishop in Numidia: Turchi l.11651, "Columbo episcopo (Numidiae)", and the header at l.71.
7. The 592, 594 (Pantaleon) and 594 (Victor and Columbus) letters each name rebaptism: l.11740, 11908, 12041. Hence B1.
8. Donatus's retort in clean Latin: TEI Ziwsa l.3357. Hence B2.
9. The Emeritus Latin as given in the record ("Magno argumento veritas occultatur; ut cum ad inquisitionem nostram modicum quid ex parte adversa prolatum sit, cetera sileantur"). The rendering covers every element: "by a great device", "truth is hidden", the "cum" clause ("when we ask, the other side puts forward a small part") and "cetera sileantur" ("the rest is kept silent"). It adds nothing. Grade FK 8.0 / FRE 80.3, which passes.
10. Lucilla's 400 "folles", and witnesses asked about them: Ziwsa appendix l.314, 593, 632, 674, and the English l.6776, 6800.
11. The Cirta council narrative (the `means` date dropped as stronger than the record's disputed date): Optatus I.14, `optatus_against-the-donatists.txt` l.183. The record's divergence_note gives the date as 305, 307 or later, so dropping "around 305" is correct.
12. Deo laudes `means` ("the editors call it the Donatist counterpart of the Catholic Deo gratias") matches the record's quoted CIL note "Uti [Deo] gratias ... catholicorum, ita [Deo] laudes signum ac tessera fuit Donatistarum". The old "marked a gathering" was invented function, and removing it is correct.
13. The Macrobius `means` (Isaac died in prison; Maximianus sunk alive; both bodies given back) matches the corrected story `text`. The pl8 Passio Isaac et Maximiani (l.1627-1629, prison) agrees.
14. The Tyconius condemnation is reported, not witnessed: the `means` lines of `don.dw.room-for-dissent`, `don.limit.theology-beyond-tyconius` and `don.term.liber-regularum` now carry "reported", matching their `text`, `statement` and `plain_meaning`.

Checks by commit:

- **ff180ee, means lines:** all nine now agree with the corrected spoken fields. The one exception is non-blocking 2. No means line adds a claim. Every changed line keeps or strengthens its hedge: "reported" (Tyconius, three records), date left open (Cirta), editors' attribution (Deo laudes), "no following is attested" (liber-regularum), and "did not grant" in place of "never" (martyr-martyrdom). The 347-348 in the martyr-martyrdom means matches its `senses.informational`.
- **c3c0988, commentary removal:** every removed sentence was an open item, and each is restated in the OG entry added in the same commit: the 411 Layer-2 revisit, the Doc_08 Open Item 2 and 3 pointers, Gesta B-not-A, Monceaux IV and VI unread (the "sitting unread" and "unread volume" hedges stay in the bodies), and the Ziwsa second-edition question (the hedge "would settle the second-edition question row 1's own Verification Note leaves open" stays). No hedge on a claim was lost. The `positions[1]` rewrite keeps every fact: the troops that came with a bishop, the Bagai reconciliation, laws against heretics used on dissidents, no surviving defence. It adds nothing and grades FK 7.1 / FRE 62.3.
- **14f634d:** the Gesta B-not-A hedge is restored in `divergence_note`, and the trailing spaces in the Monceaux IV and VI bodies are stripped (confirmed). The Tyconius manifestation is identical to origin/main (`git diff origin/main` shows no manifestation change). The "Felix 314/315" locus is a widening, so it is safe. The liber-regularum means grammar now reads correctly.
- **fd8fce4, reverted fields:** each field was word-diffed against `git show origin/main:<path>`.
  - `don.core.donatism` `horizon`: differs only by the Gregory sentence (B1).
  - `don.gravity.church-of-the-martyrs` `description`: differs only by Mabillon c. 340, Honoratus, "On Monceaux's reading", and the anniversary-day fix (non-blocking 5).
  - `don.gravity.martyr-cult-identity` `description`: differs only by Mabillon c. 340, Honoratus and "On Monceaux's reading".
  - `don.gravity.rebaptism-boundary` `description`: differs only by "in Africa as late as the 590s. One of them is addressed to a bishop in Numidia." This is correct: Pantaleon was prefect of Africa, and Victor and Columbus were bishops of Africa.
  - `don.craft.fidelis-voice` note: differs only by "Honoratus" and "on one reading".
  - Other differences in these files against origin/main (loci, manifestations, the rebaptism-boundary divergence_note) come from earlier commits outside this recheck.
- **Readability of the spoken fields touched here:** `don.witness.boundary-is-doctrine` `text` FK 7.1 / FRE 75.4; `don.dw.the-word-catholic-and-no-door-today` `text` FK 7.8 / FRE 71.5; `don.term.catholicus` `plain_meaning` FK 4.9 / FRE 82.5; Emeritus rendering FK 8.0 / FRE 80.3. All pass.
- **Tense and tells:** the touched sentences are past tense for the community's own past ("One of our own preachers turned ..."). There are no added three-beat rhythms, "not X, but Y" pivots or assistant cadence.
