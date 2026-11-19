## Council profiles, era 7 batch 2, round 2: Part D (Colloquy of Poissy 1561)

**Council.** `colloquy-of-poissy-1561`
**Files rechecked.** `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era7/colloquy-of-poissy-1561.brief.txt`, `audio/colloquy-of-poissy-1561.audio.txt`, `colloquy-of-poissy-1561.entry.json`, `records.json` key `colloquy-of-poissy-1561` (112 claims, 12 contested claims, 7 absent details; equal to `working/records_colloquy-of-poissy-1561.json`, checked by script), and the README "Colloquy of Poissy (about 2:30)" line. Scope: `git diff f6c9d034 HEAD` (branch `claude/cft-councils-era7-batch2`, HEAD `15a6c7bd`), against `R1_review.md` Part D and `R1_changes.md` Part D.
**Brief.** 400 words by `wc -w` (2:30 at 160 wpm, at the ceiling). `grade_text`: FK 7.41, Flesch 66.29. Longest sentence 25 words ("In January 1562 a royal edict ..."). No sentence over 25 words.
**Audio.** Equals the brief with `[calmly] ` at the start and `[warmly] ` before the last paragraph, and no other tag (checked against the diff: every changed line in the audio matches the brief's change).
**Reviewer.** Fresh Opus, full effort, first sight of the drafting and the round 1 fixing. Read and grep only; no repo file edited; no model, network or paid calls. Scratch copies at `/tmp/claude-0/-home-user-CIC-Project/af34472b-cc0a-504c-a9aa-6aa7f1f6ba1a/scratchpad/poissy_r2/`.

Abbreviations as in round 1 (HE1, AYM, LAI8, PAL2, SARPI, WAT, MELV).

## Verdict: REVISE (0 blocking, 1 substantial, 4 minor)

The blocking fix holds. Read whole in the History, Beza's sentence on the Supper is a concession and a limit together, and the brief now gives both. The speech's "nous fommes faits participans de fon corps & de fon fang par une maniere fpirituelle, & moyennant la foy, auffi véritablement que nous voyons les Sacremens" (HE1 l.28526-28529) stands behind "truly shared ... by faith". Its distance clause stands behind the second sentence (HE1 l.28512-28517). The narrative puts the concession first, "combien qu'il nous fuft véritablement offert & communiqué en icelle" (HE1 l.28711-28712), as the brief now does. Every round 1 finding is closed, and every changed quote is verbatim.

One new substantial point comes from the D-S1 fix. The brief now has Sarpi speak for "the Catholic side" as "the friar Paolo Sarpi", with nothing about his stance. The entry, this batch's Regensburg and Trent briefs, and D-S5 all place him as hostile to the papal court (D2-S1). Three minor points are in new entry text: an identification of Catherine's two meetings given without its witness, a word ("canonists") that the cited Waterworth lines lack, and a condition told as done. The fourth minor point is the length test: four small cuts, which pay for D2-S1.

## Round 1 findings

| ID | Status | Evidence |
|---|---|---|
| D-B1 | CLOSED | Brief p.4: "Beza said believers truly shared in Christ's body and blood in the Supper, by faith. But in distance of place, his body was as far from the bread and wine as the highest heaven from the earth." Read whole: HE1 l.28512-28533 (speech) and l.28707-28727 (narrative). The speech answers "fi nous rendons Jefus Chrift abfent ... nous refpondons que non". It limits the distance to "quand il eft queftion de fa prefence corporelle", then says that despite the distance "nous fommes faits participans de fon corps & de fon fang par une maniere fpirituelle, & moyennant la foy, auffi véritablement que nous voyons les Sacremens à l'œil". "Truly" is the speech's "auffi véritablement" and the narrative's "véritablement offert"; "shared in" is "faits participans"; "by faith" is "moyennant la foy". "In a spiritual way" is not said, but "by faith" carries it, and nothing is added. "In the Supper" is the speech's context ("la faincte Cène") and the narrative's "en icelle". The order follows the narrative, which is the account of what set off the uproar ("Cefte feule parole ... fut caufe que les prelats commencèrent à bruire", l.28713-28716). Records `claims[109]` (HE1 l.28523-28529, participant) holds it. |
| D-S1 | CLOSED, with a new point | Brief p.2: "It tells the Reformed side, and prints the prelates' own decisions." True: HE1 l.28996-29013, 33690-33729, 33924-35113. Names and first names in place (PAL2 l.1; SARPI l.677-678). Records `claims[110]`, `[111]` in place. See D2-S1: Sarpi's side. |
| D-S2 | CLOSED, with a new point | Entry `calledBy` and records `claims[67]` now put Catherine's "Colloque gracieux" after Lorraine's reply and on the confession. AYM l.25537-25548 read whole: "Depuis ladite Refponce faite ... je trouvé bon que nosdits Prelatz & Evéques entraffent en quelque Colloque gracieux avec lesdits Miniftres fur les Articles de leur dite ConfeJJion de Foi; mais aiant veu que de deux Communications qu'ils avoient faites à deux divers jours ..." Letter dated "le 18. jour d'Octobre 1561" (AYM l.25619-25620, OCR "iS."). Quote verbatim. See D2-M1. |
| D-S3 | CLOSED | Entry `decided[1]`: "After the first session, the History says, ..."; "Baum and Cunitz date the resolution to 10 September, from Vermigli's letter of 12 September." HE1 l.28996 "Sur cefte première entrée de conférence" (no date); note l.29024-29025 "le lendemain de la séance, le 10 septembre, comme cela se voit par la lettre de Vermigli à Bullinger, du 12 sept." `claims[25]` agrees. The second sentence's "They" still reads as the prelates. |
| D-S4 | CLOSED | Entry `datesNote` and `claims[100]`. HE1 l.27895-27898, in the editors' note: "Une autre édition porte le titre : La première Harangue ... le mardy neufiesme jour de Septembre ... recueillie et rédigée par escript, ainsi que ledict de Besze la prononçoit, 1561 in-8°." "Early" is right (1561). `witness_kind` now `modern reconstruction`. |
| D-S5 | CLOSED | Entry `record`: Sarpi "A Venetian Servite friar; Catholic but hostile to the papal court. Pallavicino wrote against him. Our scanned copy is garbled at the date of the first session." SARPI l.677-678 "Father Paul the Venetian, of the Order of the Servi"; l.42787 "The ſecond of September of the King,Queei)," (garbled; "garbled" is right). Pallavicino: "A Jesuit writing against Sarpi; for the papal court." PAL2 l.1 "della Compagnia di Gesù ... rifiutasi ... un'istoria falsa ... sotto nome di Pietro Soave Polano". |
| D-M1 | CLOSED | "Some prelates murmured": HE1 l.28717-28718 "dont les uns difoient : Blafphemavit". |
| D-M2 | CLOSED | "barred from": HE1 l.33717-33718 "leur fera défendue la demeure en fon Royaume". Sentence 24 words. |
| D-M3 | CLOSED | Teaser: HE1 l.33703-33711 "en casque ledit de Beze & fa compagnie ne veulent prefentement confeffer & foufcrire la confeffion dudit faind facrement ... de ne les plus ouïr en façon que ce foit". Sentences 17, 10 and 18 words. |
| D-M4 | CLOSED | Huguenot note. HE1 l.27839-27841 ("douze, avec 22 députés des Eglifes ... appelles & introduis") and l.30629-30630 ("douze miniftres & non plus, fans que mefmes les députés des Eglifes y fuffent admis"). |
| D-M5 | CLOSED, with a new point | LAI8 l.39599-39605 read. See D2-M3. |
| D-M6 | CLOSED | Entry `uncertain[0]`: "Baum and Cunitz show that its Poissy chapter copies La Place in many passages." |
| D-M7 | CLOSED | `claims[9]` carries the OCR note; SARPI l.42787. |
| D-M8 | CLOSED | `claims[104]` `later narrative`. |
| D-M9 | CLOSED | Entry `outcome[8]`, the Scottish `traditions` note, `claims[83]`. MELV l.33940 "[by Mr James Melvill *"]", l.33950-33951 "[letter by MR JAMES MELVILL TO THE BRETHREN ASSEMBLED AT THE CONFERENCE OF FALKLAND.]", l.33964-33966 "as witnesseth Colloquium Poissiaconum in Gallia, anno 1561". Year: running head "THE CONTINUATION OF 1607" (l.33905), Falkland "the 15 of Junij" (l.33936). |
| D-M10 | CLOSED, with a new point | Entry `outcome[7]`, `claims[81]`. WAT l.9099-9102: "the articles proposed at the Conference of Poissy, were secretly submitted to Simonetta, Castagna, Boncompagno, Paleotto, and Castelli, to be examined". Quote verbatim. See D2-M2. |
| D-M11 | CLOSED (README); Open-Gaps entry still to be made | The README line now ends "and so does what came of it, in the crown's, the Catholic historian's and the edict's own words." Open-Gaps has no Poissy or Palatine census entry yet (`grep -n -i "poissy\|palatin"` Open-Gaps.md: one hit, l.3566, "Lewis the Palatine" for Worms). `R1_changes.md` Part D words the entry; the coordinator owns it. |

## Blocking

None.

## Substantial

**D2-S1. Substantial (a partisan witness given a side that is not quite his, and a label out of step with the batch).** Brief p.2: `The Catholic side speaks through Jesuits who came with the pope's legate. So do two rival historians of Trent, the friar Paolo Sarpi and the Jesuit Sforza Pallavicino.`
- This new text, from the D-S1 fix, gives Sarpi to "the Catholic side" and calls him only "the friar". The listener cannot weigh him. Yet he is the brief's one witness against the History on whether Beza was stopped ("Sarpi says he was told to conclude", p.4; SARPI l.42837-42838).
- The entry, as D-S5 fixed it, says "Catholic but hostile to the papal court". The Regensburg and Trent briefs of this batch now both read "The Venetian friar Paolo Sarpi was hostile to the papal court" (R1_changes Part A, A-M6; Part B, "Sarpi label"). Pattern C1 and Who item 6: a partisan witness carries his side, with one label across councils.
- Held lines: SARPI l.677-678 "Father Paul the Venetian, of the Order of the Servi"; records `claims[110]`; his stance as the Trent records cite it (SARPI l.8820-8836, Trent `claims[13]`).
- Fix, brief (replace the second sentence; 20 words): `So do two historians of Trent, the Jesuit Sforza Pallavicino and Paolo Sarpi, a Venetian friar hostile to the papal court.` "Rival" goes: the two sides, now named, carry it, and the entry `record` keeps "Pallavicino wrote against him". The sentence costs 5 words. The cuts under "Length test" pay for them.
- Checked on a scratch copy: with the cuts, 400 words, FK 7.50, Flesch 65.65, longest sentence 25 words.

## Minor

**D2-M1. Minor (an identification without its witness, in new text).** Entry `calledBy`: `These were the meetings of 24 and 26 September.` Records `claims[67]`: `(the meetings of 24 and 26 September)`.
- The letter gives only "deux Communications qu'ils avoient faites à deux divers jours" (AYM l.25545-25546). The dates are Polanco's (entry `datesNote`, "Polanco dates the third to Wednesday 24 September and the last to Friday 26 September"). The editors' note on Beza's speeches gives the same days (HE1 l.27898-27899, "le 24 et le 26 septembre"). The identification is sound, but it is the profile's, not the letter's.
- Fix, entry `calledBy` (replace the sentence; 15 words): `Her two meetings "à deux divers jours" fit the sessions Polanco dates to 24 and 26 September.` (Use the entry's own quote marks, single quotes.)
- Fix, records `claims[67]`: `(the two meetings fit the sessions of 24 and 26 September, which Polanco dates)`.

**D2-M2. Minor (a word that the cited lines lack).** Entry `outcome[7]` and `claims[81]`: `secretly submitted to canonists at Trent in 1562`. WAT l.9099-9102 names the five men but does not call them canonists. Waterworth does so elsewhere: Simonetta for "his intimate acquaintance with canon law", with Castagna, Boncompagno, Paleotto and Castelli as his assistants (WAT l.7353-7358); "Castagna ... one of the most able canonists of his day" (l.10501-10502); "canonists, Boncompagno, Fachenetti, Paleotto, Lancellotto, to whom Castelli was [after]wards added" (l.9762). The word holds. Fix: records `claims[81]` witness `council-of-trent_canons-and-decrees_waterworth1848.txt l.9099-9102; for "canonists", l.7353-7358, 9762, 10501-10502`. Entry unchanged.

**D2-M3. Minor (a condition told as done).** Entry `traditions` (the-society-of-jesus): `It came in as a college, not a new order, and under another name.` The act received the Society "à la charge qu'ilz seroient tenuz prandre aultre tiltre que de société de Jésus ou de Jésuites" (LAI8 l.39603-39605), "on condition that they be bound to take another title". Whether they took one is not in the act. Fix (15 words): `It came in as a college, not a new order, on condition it take another name.`

**D2-M4. Minor (length: four small cuts, −5 words).** See "Length test".

## Length test

Brief before: 400 words, 2:30 at 160 wpm. I tested each sentence for whether a cut would lose a decision, a side or a source.

- P1, the scene. "About noon on 9 September 1561 ... at Poissy": the opening scene the pattern asks for (C8). One cut: "great" refectory (−1). It is the History's "grand refectoir" (HE1 l.27648), but as scene-setting it carries no decision, side or source. "The king sat with his mother, Queen Catherine": she is needed later. The count of cardinals and bishops: needed, because "That count" in P2 places it with its witness. "Bare-headed at a barrier ... Beza spoke for them": the refused party in the room; keep.
- P2, whose account. The 1580 title with no author, "long credited", and Reuss's view are the pattern's first duty here. One tightening: "thought Beza directed the work and" → "thought Beza directed it and" (−1). "It tells the Reformed side, and prints the prelates' own decisions": needed (D-S1). The Jesuits, and the two historians as D2-S1 places them (+5): needed.
- P3, the stake. "In July an assembly resolved that the ministers should have a safe-conduct and be heard." → "In July an assembly resolved to give the ministers a safe-conduct and a hearing." (−1; HE1 l.25997-25998 "auroient faufconduict pour l'y trouver, & y eftre ouis"). The aim sentence and its tag: keep. The edict at the close answers it.
- P4, Beza's sentence and the uproar. Each sentence carries a sourced act, with its witness tag ("the History says", "Sarpi says"); the "told to conclude" dispute needs both witnesses. Keep all.
- P5, the Catholic replies. Lorraine's "son, not lord": his own voice; keep. "On 26 September the Jesuit Diego Laínez spoke to the queen in Italian." → "On 26 September the Jesuit Diego Laínez spoke to the queen." (−2). The language is a Polanco detail (LAI6 l.3747) with no decision, side or source in it; the entry's `record` keeps it. His words to her: his side's own voice; keep.
- P6, the formula and the refusal. The queen's order, the rejection "as captious", and the conclusion's "one God, one king, one faith and one law": each is a decision in the prelates' own words; keep.
- P7, what came of it. Catherine's letter and Pallavicino's verdict: the crown's and the Catholic historian's voices, which the README names; keep.
- P8, the edict. Its terms and its "one fold" are the edict's own words, and "still" keeps the close from saying the hope ended. Keep.

No sentence repeats another. There is no summing-up line, no double attribution, and no clause that restates the README's reason. The brief earns its length. The four cuts above are a few words each, so they are Minor. They are worth taking to pay for D2-S1 without passing the ceiling.

**Counts.**
- Before: 400 words, 2:30 (2.50 min), FK 7.41, Flesch 66.29, longest sentence 25 words.
- Cuts alone (no D2-S1): 395 words, 2:28 (2.47 min), FK 7.38, Flesch 66.14, longest 25 words.
- Cuts plus D2-S1: 400 words, 2:30 (2.50 min), FK 7.50, Flesch 65.65, longest 25 words ("In January 1562 a royal edict ...", unchanged). The new Sarpi sentence is 21 words by the splitter's count. All checked with `grade_text` and `working/grade.py` on scratch copies.

**README line.** "Colloquy of Poissy (about 2:30)" stays true either way: 400 words is 2:30, and 395 is 2:28. The reason given (standing and Catholic witnesses placed; scene, sentence and uproar, replies, refusal, and what came of it) matches what the brief keeps after the cuts. No change is needed. One note for the coordinator, outside this council: the batch README's "None was written to the ceiling" (l.19) sits beside four briefs that are each exactly 400 words. I leave the wording to the coordinator, since it covers all four.

## Verified

- Every changed brief sentence, against its source line in context: p.1 (Navarre dropped; HE1 l.27647-27651 has Orléans and the King and Queen of Navarre besides Catherine, so dropping them takes nothing false from the brief); p.2 (D-S1); p.3 "to see if they could be reunited with the Roman Church" (HE1 l.25998-25999 "afin d'advifer fil y auroit moyen de les reunir à l'Eglife Romaine", which is faithful); p.4 (D-B1, D-M1); p.6 "reached a formula" without "then" (HE1 l.33193-33203, 33383-33395) and "barred from" (D-M2).
- Every changed or added entry and records quote, verbatim: "quelque Colloque gracieux" (AYM l.25542-25543); "the articles proposed at the Conference of Poissy" (WAT l.9099-9100); "as witnesseth Colloquium Poissiaconum in Gallia, anno 1561" (MELV l.33964-33965); the "Tuesday" title (HE1 l.27895-27898); the Jesuit act (LAI8 l.39602-39605). Translations: "partakers ... in a spiritual way and through faith, as truly as they see the sacraments" (claims[109]) is faithful to HE1 l.28526-28529. "Sets out to refute a false history published under the name Pietro Soave Polano" (claims[111]) is faithful to PAL2 l.1, "rifiutasi ... un'istoria falsa divolgata ... sotto nome di Pietro Soave Polano".
- Split or joined sentences: `calledBy` (D-S2) keeps "Catherine wrote" in the first half, and the second half is D2-M1. `decided[1]` (D-S3) keeps "the History says" on the resolution and gives the date to Baum and Cunitz. `datesNote` (D-S4) is its own sentence and keeps the History on "about noon". The Jesuit note (D-M5) puts the act's tag in the first sentence; the second carries the act's terms, see D2-M3. Each claim sits with its witness.
- The audio matches the brief line for line in the diff, with the two tags only.
- No entry sentence over 25 words in the changed strings (counted: the longest is `decided[1]`'s first sentence, 22 words; `outcome[7]`'s first sentence, 24 words).
- An observation, not a finding, because the text is unchanged and the point is not blocking. Brief p.7, "Catherine wrote that the meetings bred disputes upon disputes", widens her letter a little. The letter says this of the two meetings after Lorraine's reply (AYM l.25545-25548), and the five-and-five came after them. A word-neutral wording, if the fixer wants it: "Catherine wrote that two meetings bred disputes upon disputes, far more than union." It also agrees with the new `calledBy`.

## Searches run

No new or changed absence in the brief, entry or records. The changed text asserts no "not held" or "no source". Searches run for the points above:
- AYM l.25495-25640, the whole Catherine letter (heading, body, date line); `grep -i "octob|1561|jour"` in that range for the date.
- HE1 l.28480-28540 and l.28695-28745, the whole speech passage and the whole narrative of the uproar; `grep` for "abjent|ejloigné du pain|fommes faits participans|niere Jpirituelle|combien qu'il nous fuft|Blafphemavit" for line numbers (hits l.28513, 28516, 28527-28529, 28711, 28718; l.10964 and 28878 are other passages).
- HE1 l.28994-29030 (the resolution and the editors' date), l.27836-27842 and l.27890-27900 (deputies; the edition title), l.30624-30632, l.33700-33720, l.37064-37074 (the edict's "en une mefme bergerie"), l.27645-27652 ("grand refectoir").
- WAT: `grep -n -i "canonist"` (hits l.1539, 2877, 3388, 3874, 4001, 9731, 9742, 10503, 10723) and `grep -n -i "Boncompag|Paleott|Castelli|Castagna"` (l.7357-7358, 9101-9102, 9762, 9881-9882, 10502 and others); read l.7350-7360, 9094-9112, 9755-9763, 10501-10504.
- SARPI l.673-680 and l.42785-42789; PAL2 l.1 (title); LAI8 l.39598-39606; MELV l.33938-33970 and `grep "1607|Falkland"` in l.33700-34100.
- Open-Gaps.md: `grep -n -i "poissy|palatin"`.
- The other era 7 briefs: `grep -o` for Sarpi sentences (label comparison for D2-S1).

## Counts

Round 1 findings: 17 (D-B1, D-S1 to D-S5, D-M1 to D-M11). All 17 are closed; 4 are closed with a new point (D-S1, D-S2, D-M5, D-M10). D-M11's Open-Gaps entry is still to be made by the coordinator.
New: Blocking 0. Substantial 1 (D2-S1). Minor 4 (D2-M1 to D2-M4).
Brief: 400 words (2:30) before; 395 (2:28) with the cuts alone; 400 (2:30) with the cuts and D2-S1.
