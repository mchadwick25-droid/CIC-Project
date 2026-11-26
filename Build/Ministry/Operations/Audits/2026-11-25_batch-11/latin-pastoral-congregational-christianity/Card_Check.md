# Card check: Latin Pastoral Christianity in Africa (`latin-pastoral-congregational-christianity`)

Checker: the card checker, who did not write the card. Read: `CLAUDE.md` (Trust and source fidelity), Kit Part 1, `kinds/tradition.md`, the card role, the final brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, `Card.existing.json`, `latin-pastoral-congregational-christianity.card.json` and `Card_Edits.md`. `Entry_Texts.not-applied.md` is ignored, as instructed. Every cited line below was re-opened in `cic/texts/`.

**Verdict: FIX.** The ten edits in `Card_Edits.md` hold, and the census rules pass. The remaining problem is in the old wording the card kept. Kit Part 1 (Rigor) says a judgment that only a modern work makes "stays out of the story and the card", and check 1 asks for no modern opinion anywhere on the card. Several claims listed as not found are exactly that, and three are contradicted by held lines. The changes are listed under **Changes** below. They are deletions or the fewest words that fix each problem.

## What holds

1. **Edits and evidence (check 1).** Each of edits 1-10 stands on its cited lines: `why` (Pos 2013-2016, 2058-2069; ANF 27959-27968); `teaser` dates; `voices[2]`; the six new `legacy` sentences (Bap 11416-11418; PL38 99282-99292 with Opt 2588; Pos 4204-4209, 4071-4073; Proc 2206-2214; PL67 42540-42541, 43120-43121); the letter's words in story 0 (ANF 28796-28799, 28818-28819); Musurillo moved; story 2's saying, psalms, will and caveat (Pos 4073-4076, 4925-4929, 4983-4984; Latin 4030-4033, 4888-4891, 4944-4945); Burns and Brown moved. Every item the outline, review and fresh read send to the card is on it, as `Card_Edits.md` lists. Leaving the Pelagians off is right under Kit Part 1 ("explain it or leave it out"). Each `modernWorks` note says what the work covers, and none says what it argues.
2. **Nothing else moved (check 2).** A field-by-field diff of `Card.existing.json` against the card shows changes only in `why`, `teaser`, `voices[2]`, `legacy` (the old text kept as a prefix), story 0 text and sources, story 1's source note, and story 2's verification, text, caveat and sources. The new keys are `uncertain`, `sources`, `quotationOriginals` and the three `modernWorks`. All are listed. A character diff of the story texts matches the listed old and new wording exactly.
3. **briefReferences (check 3).** The card has none.
4. **Census rules (check 4).** There are three `quotationOriginals`, one for each of the brief's three quoted spans. Each `modern` is the brief's wording exactly. Each `printed` and `englishPrinted` was checked by hand at its lines: Goldbacher CSEL 34 at 6521-6524 (the stray "•r>" left out) with NPNF 25511-25516; Hartel at 2293-2296 with ANF 29119-29122; Weiskotten at 4556-4561 (the hyphen breaks joined, "X5" left out) with 4588-4593. Goldbacher CSEL 57 at 18295-18300 agrees. Every span has six words or more, so none carries `secondReading`. Each cited file is in `sources`. No audit file is named. American spelling holds outside the printed wording. Validator: a scratch copy of the census, with the card merged and the brief as `longDescription`, kept outside the repository, was run through `node tools/validate-census.mjs <copy> --skip-quotes` as one node process. Result: 629 movements, 736 edges, 0 errors, 4 warnings, all on other entries. The quote check was checked by hand, as above.
5. **"checked at card" (check 5).** No quotation is under six words. None applies.
6. **The new `sources` notes and `uncertain`** were re-read at the outline's lines: Hartel letters 744-767, 2920-2927, 2968-2976, 6228-6243, 7578-7590, 10800-10930 and 15418-15434; ANF 27938-27991 and 30170-30189; PonL 41414-41432, 41510-41530 and 41560-41600; Knopf 4876-4881; Possidius 1803-1863, 2199-2203, 3148-3210, 3595-3605, 3980-3986, 4080-4149, 4279-4327 and 4573-4581; Goldbacher 6560-6690; NPNF 25605-25618, 38000-38010, 38136-38141 and 38240-38258; Optatus 151-218, 301-304 and 2588; Retr 6833-6838; CatE 1793-1810; Eus 37412-37415; Jerome 57616-57623; CyLap 345-351; Calvin 25387-25392. They hold, with one exception: the Sermon 310 note overstates what the sermon says (change 11).
7. **Census entry (check 7).** No new entry is needed, since this is a tradition with its own census entry. `relationsSummary` stays unchanged, which is right.

## Rulings on the writer's flags

- **"He died on 28 August": found, so it stays.** Prosper's Chronicle, at the year 430, says Augustine "moritur V. kl. Sept." (`prosper_chronica-minora-1-lat_mommsen1892.txt` 54204-54208). Prosper is an old witness from the same century, so this is not modern reckoning. Weiskotten's note at Pos 149 cites the same entry.
- **"Augustine, seventy-five": clearly wrong, so it goes.** Possidius, the held witness, says "he lived seventy-six years" (Pos 4919-4920). Seventy-five comes only from a modern reckoning of his birth year against that figure. Kit Part 1 bars it from the card (change 5).
- **"Sneer" and "It was not subtle." (story 0): a judgment of blame against the held letter, so they go.** The letter that the card now quotes goes straight on: "in doing which he acted quite rightly, because he is a person of eminence" (ANF 28799-28800). Only the ANF editor's note calls it "a very obscure passage, and is variously understood" that "seems, in a slight degree, to reflect on" the withdrawal (28827-28833). The card's reading is a modern one stated as the narrator's own, and leaving out the letter's own praise softens the record. The story's teaser ("write to ask why") and its caveat ("the hostile one") make the same claim. The letter's own heading gives its business: the clergy "Remind the Carthaginian Clergy of Their Duty, and Instruct Them What to Do in the Case of the Lapsed, During the Interval of the Bishop's Absence" (28791-28796). See changes 1-4.
- **The legacy's later judgments: they go, except the settled events.** Six sentences are modern judgments of influence that no old source makes, and they fail Kit Part 1 Rigor and check 1: "What it left behind ...", "Cyprian's letters laid the ground ...", "Augustine's sermons shaped ...", the three catechumenate and penance sentences, and "Latin Christianity's basic ideas ...". "Later, the Donatists quoted them in their own defense" is true (Bap 11243, 11416), but it loses its referent when those sentences go, and the new sentence "Both churches claimed Cyprian ..." already says it. So it goes too (change 7). These stay:
  - "The Vandals took the province in the 430s." Possidius gives the overrunning at 3980-3986. Prosper, at the year 439, says Gaiseric took Carthage "dolo pacis" (54560).
  - The Arab conquest and the slow end of Latin Christianity there. Both are Widely Accepted events outside the window, so they are told plainly.
  - The Calvin sentence. It rests on a later writer who quotes Augustine (Calvin 25389-25391).
- **The other claims listed as not found:**
  - Found: "the crowd in the amphitheater" (Hartel Ep. 59, 9665-9668, "in circo in amphitheatro ... ad leonem denuo postulatus"); "everyone sacrifice" ("ob sacrificia quae edicto proposito celebrare populus iubebatur", 9667-9668); Fabian executed (Eus VI.39, 37414); Possidius "cataloged his works" (his Indiculus, Pos 3089); "in the summer of 430" and "The city fell the following year" (Prosper 54204-54208 with Pos 4082-4083, 4147, 4071-4073).
  - Struck as modern judgments (changes 5, 6, 8, 9, 10): the teaser's "the parish before the word existed"; `voices[0]` "fullest surviving picture"; `voices[2]` "most extensively documented working pastor"; story 1's caveat "lightly edited in transmission"; story 2's closing sentence, which is also a "not X but Y" turn.
  - Contradicted by the held letter (change 3): "in ordinary dress". Letter 5 sets out the precautions, which are visits in turn, not in crowds, one priest with one deacon (Hartel 757-767; ANF 28973-28995), and dress is not among them.

## Changes

1. **documentedStories[0].title**
   Old: `Cyprian’s Flight and the Sneer from Rome`
   New: `Cyprian’s Flight and the Letter from Rome`
2. **documentedStories[0].teaser**
   Old: `The clergy of Rome, whose own bishop has just been killed, write to ask why.`
   New: `The clergy of Rome, whose own bishop has just been killed, write to his clergy about their duty while he is gone.`
3. **documentedStories[0].text** (three changes)
   - Old: `‘the blessed father Cyprian has for a certain reason withdrawn’, and went on to quote the Gospel:`
     New: `‘the blessed father Cyprian has for a certain reason withdrawn’, said he had ‘acted quite rightly, because he is a person of eminence’, and went on to quote the Gospel:` (ANF 28799-28800, verbatim)
   - Old: `and fleeth.’ It was not subtle. Cyprian’s reply,`
     New: `and fleeth.’ Cyprian’s reply,`
   - Old: `to do it in shifts and in ordinary dress so as not to draw attention.`
     New: `to do it in shifts so as not to draw attention.`
4. **documentedStories[0].caveat**
   Old: `Cyprian preserved even the hostile one;`
   New: `Cyprian preserved even the letter from Rome;`
5. **documentedStories[2].text** (two changes)
   - Old: `Augustine, seventy-five, watched churches burn`
     New: `Augustine watched churches burn`
   - Old: ` The city fell the following year. It is the last documented scene of the most documented pastor of antiquity, and it is a scene of penitence rather than triumph.`
     New: ` The city fell the following year.`
6. **documentedStories[1].caveat**
   Old: `a separate court-style record whose text has been lightly edited in transmission.`
   New: `a separate court-style record.`
7. **legacy.** Delete these eight sentences, each with its following space, and leave everything else as it stands:
   - `What it left behind is the working vocabulary of Western church life.`
   - `Cyprian's letters laid the ground for how the West thinks about the bishop's office and the unity of the church.`
   - `Later, the Donatists quoted them in their own defense.`
   - `Augustine's sermons shaped Christian preaching for well over a thousand years.`
   - `These congregations also worked out the catechumenate, the training of new believers before baptism.`
   - `They worked out the practice of penance too.`
   - `Both became the pattern for Western sacramental discipline.`
   - `Latin Christianity's basic ideas about what a local church is took shape largely in these two African towns.`

   The legacy then opens: `The North African church itself did not survive. The Vandals took the province in the 430s. The Arab conquest came in the seventh century. After it, Latin Christianity there slowly died out. In Geneva, Calvin wrote that he could fill a whole book with Augustine's words on God's choice of the saved. Both churches claimed Cyprian: ...`, and the rest runs unchanged.
8. **voices[0]**
   Old: `Cyprian of Carthage — bishop through persecution and plague, whose letters are the fullest surviving picture of how a third-century congregation actually ran`
   New: `Cyprian of Carthage — bishop through persecution and plague, who led his church by letter from hiding`
   Evidence: Hartel 2968-2976 and ANF 30184-30186 ("absent in body, I was not wanting ... in my advice"); the brief, "From hiding he led his church by letter".
9. **voices[2]**
   Old: `Augustine of Hippo — bishop of Hippo Regius until his death in 430, and the most extensively documented working pastor of the ancient world`
   New: `Augustine of Hippo — bishop of Hippo Regius until his death in 430`
10. **teaser** (an entry field, for `Card_Edits.md` Entry fields 2)
    Old: `Roman North Africa, the 250s to 430 CE — the parish before the word existed: bishops gathering`
    New: `Roman North Africa, the 250s to 430 CE: bishops gathering`
11. **sources[12].note** (Sermon 310)
    Old: `Cyprian's feast was kept through all Africa, by Christians, pagans, Jews and heretics alike.`
    New: `Through all Africa and the lands overseas, Augustine said, there was no Christian, pagan, Jew or even heretic who did not speak with his people of Cyprian's feast day.`
    Evidence: PL38 99256-99260 ("per Africam totam transmarinasque regiones, non Christianus solum, sed Paganus, aut Judaeus, aut etiam haereticus poterit inveniri, qui non nobiscum dicat Natalem martyris Cypriani"). The sermon says they speak of the feast day. It does not say they kept it.

Release applies changes 1-9 and 11 to the card fields and change 10 to the entry's `teaser`, along with the Entry fields in `Card_Edits.md`. Changes 1-6 sit inside `documentedStories`, which Entry fields 4 already covers. No other field changes.
