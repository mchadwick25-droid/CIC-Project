# Opus fourth read of the three limits — 2026-10-27

Ordered by Mark's cap ruling (System Hub Decision Log, 2026-10-27). A fresh reader, who also ran the real citation-card filter to see what a visitor reads. Three blocking findings and six should-fix items; Mark then ruled a second time: apply all fixes and order a fifth read of the whole shipped surface (`opus-honest-limits-read-5.md`).

**Fourth read of the three honest-limit records (read-only). Two of them are not ready, and both problems sit in text this read was asked to check.**

How the text reaches people (checked in the engine). The voice is given `statement`, `use_note.means` and `not_for`. `why_sources_cannot_answer` is removed when the package is built (engine/m2/builders.py:719). But each source's `locus` is shown to the visitor on the citation card, after `display_locus` runs (engine/m4/citation_cards.py:174, SourceList.tsx:23). I ran the real `display_locus` on all three records to see what a visitor would read.

## (1) Verdicts
- **don** (records/don/honest_limit/don.limit.fate-of-those-who-end-their-own-lives.md): **NEEDS CHANGES**, with two blocking findings.
- **alx** (records/alx/honest_limit/alx.limit.faith-alone-later-frame.md): **NEEDS CHANGES**, should-fix only. It is safe.
- **pahc** (records/pahc/honest_limit/pahc.limit.assurance-and-the-dead.md): **NEEDS CHANGES**, with one blocking finding.

None of the three is ready for `use_note.status: reviewed` yet.

## (2) Findings

**1. BLOCKING (don, line 18): the visitor's citation card names a method.** The card shows the Optatus locus as: "...some of the Donatists 'cast themselves down headlong from the summits of lofty mountains' to win a martyr's name -- verified directly against cic/texts/optatus_against-the-donatists.txt, line 2014...". The method was taken out of the statement but is still shown to the visitor beside a suicide question. The file path and line number also leak, because `display_locus` only strips them inside parentheses. Corrected locus (I tested it through `display_locus`; the card then reads "Against the Donatists, Book III, chapter 4: an opponent's charge…"):
`locus: "Against the Donatists, Book III, chapter 4 (optatus_against-the-donatists.txt, line 2014): an opponent's charge that some Donatists sought death out of desire for a false martyrdom; not a Donatist teaching"`

**2. BLOCKING (don, line 42): Judas is put back beside a suicide question.** The `not_for` line "a claim that Petilian's line about Judas is a Donatist teaching on suicide" goes to the voice as a "Not for:" line. In a turn about a death by suicide, it hands the model the traitor who hanged himself, the "son of perdition". The Cap ruling says the third round removed exactly this, yet it is still here. The statement does not use Petilian, so the guard protects nothing. **Delete that line.** The Petilian note stays in `why_sources`, which no one hears.

**3. BLOCKING (pahc, lines 125–127): the citation card judges a grieving visitor's belief.** The Justin source's card reads: "some who are called Christians … say … their souls are taken to heaven when they die; Justin says do not imagine they are Christians." A visitor who believes their loved one is in heaven would read that as a ruling against their belief. That is the defect the Cap ruling named. The statement does not use Justin at all, so the sources list and the statement also disagree. **Delete the `pahc.source.justin-dialogue` entry from `sources`.** Also delete the `not_for` line "a claim that Justin's view in Dialogue 80 was the view of the whole network", which is ambiguous anyway: it is not clear whether "Justin's view" means his own view or the one he rejects. Corrected `divergence_note`:
`divergence_note: "Ignatius's letters carry a three-way scholarly split on date (see pahc.contested.ignatius-dating)."`
Justin stays in `why_sources` as material that was searched.

**4. SHOULD FIX (don, line 23): "Our enemies" is plural, but the only source listed is Optatus.** The plural leans on Augustine, who is not listed. Corrected sentence:
"Optatus, who wrote against us, charged some of our people with seeking death to be counted as martyrs."

**5. SHOULD FIX (don, lines 25–26): the closing lines read like a rule being recited, and "No condition on one" is unclear.** "One" grammatically points back to "verdict"; heard aloud, the phrase means nothing. Corrected:
"It is not mine to judge anyone who has died this way. Nor is it mine to set terms on their fate."
(I avoided "hangs on" on purpose.)

**6. SHOULD FIX (don, line 29, the search notes): the Monumenta account leaves out one of its three Donatist texts.** The file's own header (lines 3–14) lists the Sermo de passione Donati et Advocati (c. 340) as Donatist-authored. Its line 627 reads "in nostro certamine occidi ab inimico triumphus est", and line 638 "coronat in caelo". That line is arguably nearer the subject than Petilian, so the claim at line 33 that Petilian is "the nearest Donatist-voiced line" is wrong. Replace "It holds Donatist martyr texts, the Passio Marculi and the Passio of Isaac and Maximian, which place their martyrs in heaven;" with:
"It holds three Donatist texts: a sermon on the sufferings under Leontius and Ursacius, which says that in our contest to be killed by the enemy is the triumph and that the Church is crowned in heaven; and the Passio Marculi and the Passio of Isaac and Maximian, which place their martyrs in heaven;"
At line 33, change "is the nearest Donatist-voiced line found in what was read; it speaks of a traitor" to "speaks of a traitor".

**7. SHOULD FIX (pahc, lines 130–131): "made perfect in love, by God's grace" can be heard as a test the dead had to pass.** 1 Clement 50 (anf01 lines 2124–2125) reads "those who, through the grace of God, have been made perfect in love". Grace is what makes them perfect. The spoken line puts grace in a side clause, which makes "perfect in love" sound like a requirement. Corrected, and closer to the source:
"Clement of Rome wrote that those whom God's grace has made perfect in love now have a place among the godly."

**8. SHOULD FIX (alx, line 75): "nothing is wanting to faith".** For a B2 reader, "wanting" reads as "desiring", which misleads. Corrected: "and that faith lacks nothing."

**9. SHOULD FIX (alx, line 79, the search notes): a "faith alone" hit in the Clement search is not reported.** Stromateis V.6 (anf02 line 41905) speaks of priests "clothed in faith alone, and expecting their own individual abode". The record frames the Clement search as finding only Stromateis I.9. Add:
"Clement, Stromateis V.6, sets believers 'clothed in faith alone, and expecting their own individual abode' below the Gnostic; that too is faith beside knowledge, not faith against works."
(Stromateis II.4, line 32187, is about how the first cause is known and can be left out.) The absence claim still holds.

**10. Nits:**
- **alx line 77:** in a voice dated 180–254, "reaches us only in Rufinus's Latin" refers to a translation made around 405. Suggest "survives only in Rufinus's later Latin".
- **pahc line 129:** "spoke of the faithful dead in two ways" echoes "the two ways" in that world's own vocabulary (it is in `nearest_material` and in a `not_for` line). Suggest "said two things about the faithful dead".
- **pahc line 133:** the Ignatius source has the Father raising "us who believe in Him [the Father] by Christ Jesus". Suggest "those who believe in him through Christ Jesus".
- **don, the search notes:** the Passio Marculi tells the death as an execution but does not itself argue against the charge. Use "stands against the charge" rather than "answers the charge".

**What I confirmed holds:**
- Optatus III.4 (line 2014 and its context): Optatus is blaming the violence of the Macarian period on the bands Donatus of Bagaia raised. He says some of the same class sought "a false martyrdom" through death. "Charged … seeking death to be counted as martyrs" is fair. "A quarrel over who may be called a martyr" is supported, though Optatus's wider aim there is the blame for the violence.
- The Monumenta account is accurate: the executioner pushes Marculus over (line 1234, "in praeceps impulit martyrem"). His soul goes to heaven (lines 1257–1263, "coelum petit … ad aeternas sedes"), and Isaac and Maximian are taken "ad coelum" (line 1422).
- The other line references in the don search notes check out: Petilian (npnf104 line 15887), Contra Gaudentium (lines 73276–78 and 75702), and Augustine's charges (npnf104 lines 16889, 17232, 19485).
- Every alx and pahc quote and line number checks out against cic/texts/, including Origen on Romans (lines 13333–13338 "sine operibus sola fide", 13414 "non futurorum, sed praeteritorum"), Polycarp 9, Trallians 9 and Polycrates.
- "By God's grace" is faithful to 1 Clement 50.
- No statement gives a verdict, promises a destination, or carries crisis wording.
- "It was not a teaching about the dead" lands correctly: it separates the visitor's question from the old quarrel.
- With findings 1, 2 and 5 fixed, the don statement is plain rather than cold. It leaves the warmth to the Facilitator and the turn, which is right.
- Format: `means` is one sentence in all three, and `not_for` lines are within the limit with none opening on an imperative verb. Years are inside each window, all source ids exist, and the cells fit.

## (3) What I could not verify
- **A record outside this review needs the same check.** `don.contested.augustine-precipice-charge` (records/don/contested_claim/, lines 42–52) carries "thrown from the cliff" and Augustine's Judas verdict. Its text and `not_for` lines ship and could be retrieved alongside the don limit. It should get the same safety check.
- **The searches the records report.** I spot-checked "faith alone" in ANF 2, 4 and 9 only. I did not re-run the pahc record searches, the Letter 185 locus, or the Monumenta 303–340 file.
- **How often citation cards actually appear for honest_limit citations.** I traced the code path but did not run a live turn.
