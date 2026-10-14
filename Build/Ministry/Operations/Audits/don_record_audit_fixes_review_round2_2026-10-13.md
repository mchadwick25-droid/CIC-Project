Review round 2, don record audit fixes, 2026-10-13, reviewer: independent Opus subagent (targeted recheck of round 1 blocking items and the edits made after it)

Verdict: DOES NOT CLEAR. 6 blocking items; all fixed before round 3.


Scope: only what changed since round 1 (41 files modified after review1_B.md was written, plus the items named in the brief), checked against review1_A.md, review1_B.md and log_round1_fixes.md. I compared against `git show HEAD:` and graded fields with engine.m1.gates.grade_text. I edited nothing in the repo. All 236 don records parse.

Verdict: NOT CLEAR. 6 blocking items. All of them are small and mechanical. Five are leftover copies of errors that round 1 corrected elsewhere. One is a meaning shift in a readability rewrite. None needs a new research round.

---

## BLOCKING

### R2-B1. don.dw.who-jesus-was-among-us, `text` (spoken). Macrobius's addressee: leftover from round-1 B6
- Exact text: `And a bishop writing to his own congregation about two of their number put to death closed by urging them to hurry after the two`
- Why: The closing was fixed, but "his own congregation" was not. Mabillon's note (monumenta-vetera-donatistarum_migne-pl8.txt ~l.1500-1513) says Macrobius was the Donatists' hidden bishop *in Rome* and wrote `ad plebem Carthaginis`. The story records, don.figure.macrobius and don.dw.what-belonging-cost now say "the church at Carthage", so this record contradicts them.
- Fix: `And a bishop writing to the people of Carthage about two of their number put to death closed by urging them to hurry after the two` (whole field FK 7.7 / FRE 74.9).

### R2-B2. don.dw.written-by-our-opponents, `text` (spoken). Ingentius and Macrobius errors left in a touched record
- Exact text (a): `There is a court transcript in which a notary confesses, under threat of torture, that he forged the letter proving our central accusation, and that he did it working for our side.`
- Exact text (b): `One bishop's own letter to his own congregation.`
- Why (a): Round 1's B8 and the ministerial-purity fix were applied, but this record was missed. Ingentius was a decurion (optatus_against-the-donatists.txt l.5745). He admitted only that he "did add to this letter" (l.5704). "Working for our side" is Apronianus's charge, and Ingentius denied part of it (l.5718-5735). don.demo.mostly-legend's turn now says "a town councillor ... added false lines", so the two records contradict each other.
- Why (b): The same addressee error as R2-B1.
- Fix (a): `There is a court transcript in which a town councillor admits, under threat of torture, that he added false lines to the letter proving our central accusation.` Fix (b): `One bishop's own letter to the church at Carthage.` (Whole field after both fixes: FK 7.0 / FRE 73.5.)

### R2-B3. don.dw.room-for-dissent, `text` (spoken) and `sources[1].locus`. "Ring" where the source has a crown
- Exact text: `wine in his cup take the shape of a ring shining with blood and light.` Locus: `the ring of blood and light in the cup; the dream of combat and the crowning`
- Why: The Latin is `corona descendens intra calicis oras ... splendido sanguineoque colore diffulgens` (pl8 l.1463-1467). Both story records were corrected to "crown", and so was don.figure.maximianus-martyr's bridge_line in this round. These are the last two copies of "ring" in records/don.
- Fix: text `... take the shape of a crown shining with blood and light.` (FK 6.8 / FRE 74.4). Locus: `the crown of blood and light in the cup; the dream of combat and the crowning`.

### R2-B4. Participant-facing loci that still carry corrected errors (brief item 3: loci show on source cards)
- don.dw.what-belonging-cost `sources` (Macrobius row): `Macrobius writing to his own congregation at Carthage about two of their number, and ...`. Fix: `Macrobius writing to the church at Carthage about two of their number, and ...` (keep the rest).
- don.demo.mostly-legend `sources` (acta row): `the town councillor confessing under threat of torture that he forged the letter, working for our side`. Fix: `the town councillor admitting under threat of torture that he added false lines to the letter`. "Working for our side" was a charge, and he denied part of it (l.5718-5735).
- don.demo.power-against-dissenters `sources` (bagai row): `the council, the reception, and the general who enforced it with troops`. Fix: `the council, the reception, and the bishop who enforced it with troops` (Optatus Gildonianus; see don.source.augustine-answer-to-petilian).

### R2-B5. don.gravity.martyr-cult-identity, `description`. The readability rewrite moved a caveat's scope and broke an antecedent
- Exact text: `Three distinct texts point to it. Donatists voiced or wrote each one. So do inscriptions cut in stone. No literary go-between stands in the way at any point.`
- Why: At HEAD, "with no literary go-between at any point" applies to the inscriptions only. Split off as its own sentence, it now reads as applying to the three texts as well, which overclaims: they reach us through manuscripts and editors. "So do inscriptions" now follows "Donatists voiced or wrote each one", so it says the inscriptions voice or write. A smaller point in the same field: HEAD's "Its core reality is documented on grounds largely independent of ..." became "shown by evidence mostly free of ...". This drops the word "documented", which is a confidence term. Restore it.
- Fix: `Three distinct texts, each voiced or written by Donatists, point to it. So do inscriptions cut in stone, with no literary go-between at any point.` and `Its core reality is documented on grounds largely independent of the hostile framing of Optatus and Augustine.` (Whole field with the first fix: FK 7.2 / FRE 61.5. Re-grade with the second fix, which should stay above 60.)

### R2-B6. don.core.donatism, `horizon`. Lost subject, and a broken hyphen from the rewrite
- Exact text: `Numidia is its own heartland. There it is dominant in numbers. Several of its best- known bishops ...` and `That state is the Catholic-aligned power that judges disputes and uses force. Its whole pattern of refusing imperial legitimacy is defined against that power.`
- Why: HEAD names the subject: "this communion's own heartland" and "This communion's whole pattern". In the rewrite, "its" points back to Carthage in the first case and to the Roman state in the second. The second now says the state refused imperial legitimacy. Attribution is lost, which is a (c) failure. "best- known" is a folded-YAML artefact: the raw file breaks the line after "best-", and the parsed text gets a space.
- Fix: `Numidia is this communion's own heartland.` / `Several of its best-known bishops` (keep it on one line) / `This communion's whole pattern of refusing imperial legitimacy is defined against that power.` (Whole field: FK 6.8 / FRE 60.4.) Optional: `Donatus succeeded him from c. 313` should say "succeeded Majorinus", because "him" could point to Felix.

---

## NON-BLOCKING

1. Round-1 B1 (Purpurius) had a wrong premise. The fix is still correct. Purpurius's letter *to Silvanus* also says the bill of accusation is true and warns of "the flame" (optatus_against-the-donatists.txt l.6204, continuing the letter at l.6202). Both letters therefore call the charge true. The new bridge_line ("to the clergy and elders of Cirta") is accurate. The dw records that say "in the same letter said he knew the accusation was true" are also accurate. No contradiction.
2. Build fields that still carry corrected errors. Each conflicts with corrected spoken records; fix when convenient:
   - don.dw.what-we-did-with-the-power-we-had `positions[3]`: "a general's troops enforcing".
   - don.quote.the-shores-are-covered `modern_lens_note`: "a general's troops".
   - don.demo.power-against-dissenters body: "The general enforcing".
   - don.story.macrobius-letter-isaac-maximianus `modern_contrast`: "the same fate may be asked of any of them".
   - don.story.macrobius-letter `use_note.means`: "two men tortured to death".
   - don.story.acta-purgationis-felicis `use_note.means`: "forged the letter for the Donatists". He added lines, and the agent claim was a charge.
   - don.demo.mostly-legend body: "notary's confession".
   - don.source.passio-isaac-et-maximiani body: "to his own congregation".
3. Tyconius. The lead's premise "no record calls him a layman" does not hold. don.term.liber-regularum `senses.informational` ("by a Donatist layman", unattributed in its first sentence) and `use_note.means` ("a Donatist layman ... his side condemned him", with no `perhibent` hedge) still say it. These are build fields. Attribute the first to Monceaux, as the second sentence of informational already does, and hedge the condemnation. The `senses.personal` closing, "the church that condemned its author", drops the hedge that the sentence before it uses ("a reported condemnation"). Suggested: "the church said to have condemned its author". The opening aphorism of the same field (round-1 B-7) is still there; it is low priority.
4. don.contested.ministerial-purity `held_against[0]`: "the charge that he acted as an agent for the accusing side, which he denied". He denied going to Numidia and admitted Mauritania "on commercial business" (l.5722-5735). "Which he partly denied" or "and he denied having been to Numidia" is exact. The acta story's text, "Ingentius denied that he had been to Numidia", is already exact.
5. Out-of-scope items from round 1 are not logged in Build/worlds/don/Open_Gaps_Tracking.md. The working tree has no change outside records/don. These are don.figure.axido-and-fasir `dates.display` and `divergence_note` ("Donatist petition ... in Optatus's appendix"), which now contradict the corrected locus, and don.figure.isaac body ("the people holding the whips were the traditores"). CLAUDE.md requires that they be logged.
6. Style in the rewritten gravity fields: "honoring" (American spelling) sits beside "practised" (British). The opening "Three distinct texts carry it. Donatists voiced or wrote each one. So it recurs very strongly." is choppier than it needs to be. Not a defect against the bar.
7. Unchanged in this round, so noted only: don.dw.hypocrites `text`, "the sea giving them back for six days". The Latin is `post bis ternos dies` (pl8 l.1858): after six days of watching, the bodies came ashore. The story records' "driven back toward shore again and again, for six days" is close to the same reading, so the world is consistent. Leave it.

---

## Verified

(a) Round-1 blocking items, checked in the records:
- A-B1 books: stray ", ." removed.
- A-B2 not-a-death-wish text and locus, and the death-wish demo locus: now say the two wait with arms stretched out and the readers are urged to hurry. Matches pl8 l.1918-1919 `Tendunt ad vos e caelo jam brachia ... Properate`.
- A-B3 hypocrites: "the two are waiting for them, and that they should hurry after them". Correct.
- A-B4 and A-B5: "Several of those letters" in power-we-had and never-settled. The 320 hearing is now "heard sworn witnesses on a charge ... that named four hundred pieces of silver". Correct.
- A-B6 who-jesus: "on the last night" (text and locus) is correct; the addressee is still wrong (R2-B1). what-belonging-cost: "tortured and put to death, one in prison and one drowned alive". Correct (pl8 l.1627-1628, 1742).
- A-B7 passio-marculi tellable_as: "On the last night of his four days at Novapetra, after a day of fasting" (FK 6.1 / FRE 81.8). Correct (pl8 l.1049-1050). "Before dawn" is supported by `dum adhuc aliqua noctis momenta superessent` (l.1114).
- A-B8 Ingentius: "town councillor" in the story text and tellable_as (FK 7.1 / FRE 62.3), the mostly-legend demo turn, and ministerial-purity held_against and concedes. Correct. Residual copies are at R2-B2 and R2-B4.
- A-B9 silver: the text now says "gave four hundred pieces of money ... Sworn witnesses confirmed the gift" (FK 9.6 / FRE 65.4). positions[0] matches HEAD word for word; only the line wrap changed. The locus "four hundred pieces of silver from Lucilla" is restored.
- A-B10: resolved by design. `_READABILITY_EXCLUDED_FIELDS = {("quote","text"), ("story","text")}` at engine/m1/gates.py:502, and grading skips them at l.532.
- Part-B B1 Purpurius bridge_line (FK 5.6 / FRE 79.8): accurate (see non-blocking 1).
- Part-B B2 axido-and-fasir: source_id is now don.source.optatus-against-the-donatists, and the locus is III.4.
- Part-B B3 doubled-towns: "two rival churches where there should have been one" (FK 7.2 / FRE 66.2). "Side by side" is gone.

(b) Non-blocking fixes applied: 1 (gesta divergence_note), 2 (power-we-had divergence_note "the bishop"), 3 (washed: "is reported to have condemned" in the note and the locus), 4 (the five loci cleaned), 5 (undiscovered-traditor attribution plus two source rows; FK 6.8 / FRE 68.2), 6 (woman-authority "It was said that she kissed"), 8 ("seventeenth-century editor" in both records), 9 (what-belonging-cost: four edits, FK 7.8 / FRE 70.4), 10 (older-than-the-schism: "at Carthage" dropped), 11 (baptism-threshold present tense; FK 6.6 / FRE 76.7), 12 (who-decides: "survives in our own keeping"), 15 (macrobius bridge_line FK 6.6 / FRE 80.6; maximianus-martyr body). All are present and correct.
Lead's extra edits, also correct:
- agonistici: quick_meaning FK 5.2 / FRE 71.8, plain_meaning FK 6.8 / FRE 60.1. Matches Enarr. Ps. 132.6, `Agonisticos eos vocant ... Sic eos appellamus` (pl36-37 l.123418-123424).
- liber-regularum: plain_meaning FK 5.9 / FRE 77.5, quick_meaning FK 4.7 / FRE 76.6. "One of ours" is correct (see non-blocking 3).
- episcopus locus: correct.
- constantine bridge_line: "accept the emperor as a judge" (FK 7.2 / FRE 65.6).
- world_core: "Two of them name Donatist rebaptism in Africa. The 592 letter is addressed to a bishop in Numidia." Consistent with don.source.gregory-the-great-register-of-letters (II.46 to Columbus of Numidia, 592).
- maximianus-martyr bridge_line: "a crown, red as blood and bright as light, come down into his cup". Closer to the Latin (`corona descendens intra calicis oras ... splendido sanguineoque colore`) than HEAD's "ring". FK 4.1 / FRE 89.8.

(c) The four readability rewrites, compared clause by clause with HEAD:
- church-of-the-martyrs: every fact, hedge and attribution survives. Grade 9.2/51.6 -> 7.3/61.3. The Mabillon c. 340 and "On Monceaux's reading" sentences come from the round-0 correction that part-B review accepted; they are backed by the record's own body note. "The Macarian repression of 347-348" lost its date in one sentence, but the date is kept later in the field.
- martyr-cult-identity: 9.5/50.1 -> 7.0/62.3. Facts kept, except for the scope shift at R2-B5.
- rebaptism-boundary: 8.9/52.3 -> 7.4/60.7. All facts kept. The Gregory Africa 594 / Numidia 592 split is the accepted round-0 correction.
- world_core horizon: 9.8/47.7 -> 6.7/60.9. Facts and dates kept. The attribution loss and the hyphen are at R2-B6.
- fidelis-voice flavor note (FK 5.6 / FRE 65.9): all names kept. "On one reading" (Advocata) is the accepted hedge.
- what-belonging-cost positions[1] (FK 4.9 / FRE 82.5): the corrected closing is kept. "At times" for "at intervals" is not a change of meaning.

Residual grep across records/don, spoken fields: "his own congregation" (who-jesus, written-by-our-opponents), "notary ... forged ... working for our side" (written-by-our-opponents) and "ring" (room-for-dissent) remain; all are listed above. These have no remaining spoken hits: "any of them / any of you" as the Macrobius closing, "tortured to death", "a general"/"the general" for Gildonianus, "four days before", "four days' fasting", "Every one of those letters".

Vendored-text spot checks this round (15):
1. Purpurius to Silvanus: "the bill of accusation ... are true" and "before the flame burst forth" (Optatus Appendix, l.6202-6204).
2. Purpurius to the Cirta clergy: "Be careful that no one knows ... What is contained in the bill of accusation is true" (l.6208).
3. Fortis to Silvanus, Sabinus to Silvanus and Sabinus to Fortis end "let no one know". Fortis to the clergy does not (l.6212-6224), so "Several" is right.
4. Ingentius: "I am a decurion of the Ziquenses" (l.5745).
5. Ingentius: "I did add to this letter, through my grief on account of Maurus my guest", under threat of torture (l.5700-5704).
6. Apronianus's Numidia/Mauritania charge. Ingentius denies Numidia and admits Mauritania "on commercial business" (l.5718-5735).
7. Gesta: "four hundred pieces of money ... given by the noble woman Lucilla" (l.6198). Sworn witnesses: "Do you know that the money was received from Lucilla?" "We do know it" (l.6576-6580).
8. Passio Marculi: `ultimum quatridui illius diem jejunio terminavit` (pl8 l.1049).
9. Passio Marculi: vision as night was ending (`majora noctis spatia exacta`, l.1077-1080). Sentence brought while night remained (l.1114-1117).
10. Macrobius: crown descending into the cup, blood-red and bright (l.1463-1467).
11. Macrobius: Maximianus tears out the emperor's eye, and a youth crowns him (l.1682-1692).
12. Macrobius: Isaac's cry `Traditores, venite, salvate vestram unitatis insaniam` (l.1640).
13. Mabillon's note: Macrobius was the hidden Donatist bishop in Rome; the letter is `ad plebem Carthaginis` (l.1500-1513).
14. Macrobius's closing, `Tendunt ad vos e caelo jam brachia ... Properate` (l.1918-1919), and `post bis ternos dies` (l.1858).
15. Optatus III.4: Axido and Fasir called "Captains of the Saints", "a reign of terror" (l.2002). Enarr. Ps. 132.6 agonistici (pl36-37 l.123418).
