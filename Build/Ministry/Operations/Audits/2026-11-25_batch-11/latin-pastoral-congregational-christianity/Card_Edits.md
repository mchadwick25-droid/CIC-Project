# Card edits: Latin Pastoral Christianity in Africa

Starting card: `Card.existing.json` (the census entry's card fields, a field-by-field match with `cic-website/data/world-census.json`; a tradition has no `card` field). New card: `latin-pastoral-congregational-christianity.card.json`. Brief: `latin-pastoral-congregational-christianity.brief.txt` (final; no `Grade_Fixes_Applied.md` or `Grade2_Fixes_Applied.md` in the folder). Every field and item not listed below is word for word, in the same order. The new keys (`uncertain`, `sources`, `quotationOriginals`) come at the end, and each documented story's new `modernWorks` comes after its `sources`.

## How a tradition's card is shaped here

The same choices as the sibling `roman-church-third-century` card in this batch. `tools/validate-census.mjs` has no card for a tradition (`checkCard` refuses a `card` on anything but a person, and the quotation checks run only for persons and councils). So the file keeps the tradition entry's own fields:

- `sources`: a top-level list in the format the tree page already shows (`work`, `type`, `note`), with `file` added to each item. Each note says what that source holds, and carries the outline's remaining "for the card" items at their source.
- `quotationOriginals`: the `cyril-and-methodius` format, at the top level. The validator does not check it for a tradition, so a scratch check (the validator's fold; tags stripped, line-end hyphens joined, the scans' stray line numbers dropped) found each `printed` and `englishPrinted` at its lines, each file among `sources`, and each `modern` one of the brief's three quoted spans.
- `uncertain`: a list, as on a person card.
- Each documented story's modern work moves to that story's own `modernWorks`, which `checkModernWorks` allows.

## Quotations

The brief quotes three spans, and each has one entry. All three run six words or more, so none carries `secondReading`. Each was re-read at its lines.

1. **Q1.** Printed (Latin): `augustine_epistulae-1-123-lat_goldbacher-csel34.txt` 6521-6524, "non ego illorum lacrimas ... finis sermonis mei factus est." The scan prints "•r>" (a misread line number) before "plenissima"; it is left out, and the entry's `uncertain` says so. English printed: `npnf101_augustine-confessions-letters.xml` 25511-25516, "I did not move them to weep ... the abuses denounced." (The sheet's E3 range 6467-6524 holds it; the outline's 6521-6524 is right.)
2. **Q2.** Printed (Latin): `cyprian_epistulae-lat_hartel1871-csel3-tei.txt` 2293-2296, "solus rescribere nihil potui ... sententia gerere." (TEI `<lb/>` tags stripped.) English printed: `anf05_hippolytus-cyprian-caius-novatian.xml` 29119-29122, "I have not been able to reply by myself ... the consent of the people." The outline gives 29117-29122; the words stand on 29119-29122.
3. **Q3.** Printed (Latin): `possidius_vita-augustini_weiskotten1919.txt` 4556-4561, "Si autem ministri adsint ... quae timentur avertere". The scan breaks "subveni- / X5 tur" and "ex- / hortantur"; the words are joined and the misread line number "X5" left out, as its `uncertain` says. Goldbacher's Latin (`augustine_epistulae-critical_goldbacher-csel57-pars4.txt` 18295-18300) agrees and is in `sources`. English printed: the same file, 4588-4593, "But if the ministers are present ... all the things they fear". The outline gives 4588-4592; the last words, "power to avert all the things they fear", stand on 4593. Its `uncertain` keeps the outline's note that "ministri" is the clergy (Outline, Quotes, Q3).

## Card fields

1. **why** (the brief no longer makes these claims; a modern name; Do not say).
   Old: "told his congregation to nurse their pagan neighbors through the plague that now bears his name,"
   New: "told his congregation, when plague struck, that caring only for their own was nothing great,"
   Old: "Augustine preached to the same Hippo congregation several times a week for thirty-five years, and stenographers took down much of what he said."
   New: "at Hippo, Augustine preached in church and in homes, and listeners, the rival church's people too, brought shorthand writers to take down what he said."
   Evidence: brief, "told them that caring only for their own was nothing great"; P2, `anf05...xml` 27961-27967. Outline, Do not say: "Christians nursed pagans" (no nursing detail; P2, P3); "the Plague of Cyprian" (a modern name); "he preached several times a week for thirty-five years" ("Not in the held lines used"). The approved-before-the-kit brief made the nursing and the weekly-preaching claims, and the finished brief makes neither (Kit Part 1: a short text may not repeat a claim the brief no longer makes). The new words carry Cut first 2 (shorthand writers) and length move 9 (preaching in church and in homes), both "for the card": B1, `possidius...txt` 2013-2014 ("In private and in public, at home and in the church, Augustine taught and preached"), 2063-2069 ("Even the heretics themselves ... bringing reporters and taking down what was said"). "the rival church's people" for Possidius's "heretics": R5, E6 (Widely Accepted, as in the brief).

2. **teaser** (contradicts the brief's dates; claims not held).
   Old: "c. 240s to 430 CE" / New: "the 250s to 430 CE"
   Old: "bishops burying plague victims, preaching to the same faces every week," / New: "bishops gathering their people through plague, judging their quarrels,"
   Evidence: brief, "From the 250s to 430"; "the bishop gathered the people"; "judged their quarrels". Burying is in no held line (Outline, Do not say, "Cyprian nursed the sick"); "every week" is the claim removed in edit 1.

3. **voices[2]** (a date only modern reckoning gives; the brief no longer makes it).
   Old: "bishop of Hippo Regius for thirty-five years," / New: "bishop of Hippo Regius until his death in 430,"
   Evidence: Source_Sheet, section 5: Augustine's consecration as bishop (395 or 396) is modern reckoning; Kit Part 1, Rigor. The approved-before-the-kit brief said "from 395 until his death in 430"; the finished brief does not. 430: V7, Setting (Widely Accepted). (`voices` is not one of the short texts the role names; the checker may hold this back.)

4. **legacy** (new: What came of it, which the outline sends to the card). Old ends: "... took shape largely in these two African towns." New adds six sentences:
   - Both churches claimed Cyprian; Augustine's answer. W1, `npnf104...xml` 11243-11246, 11416-11418 ("cling with us to the example of Cyprian for the preservation of unity"). Outline, What came of it 1 ("card, with B6").
   - Cyprian's table. B6, `augustine_sermones-1-340-lat_migne-pl38.txt` 99269-99292 (damaged print, second half confirmed by the Latin in the note at `optatus_against-the-donatists.txt` 2588). "table" is glossed as an altar (Source_Sheet, Explain it, "Cyprian's table").
   - Possidius kept Letter 228 for priests. W3, `possidius...txt` 4206-4209 ("very useful, even necessary, for the proper conduct of the priests"). Outline, What came of it 3.
   - Hippo burned after his death. V9, `possidius...txt` 4071-4073 (Latin 4026-4027). Outline, What came of it, and Do not say ("Hippo was burned after his death (card)").
   - The Cypriana. W2, `procopius_wars-3-4-vandalic_dewing1916.txt` 2206-2214. Outline, What came of it 2.
   - Facundus. W5, `facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865.txt` 42540-42541 ("beatus Cyprianus Carthaginiensis antistes et martyr"), 43120-43121 ("sapientissimus atque clarissimus Ecclesiarum Christi magister Augustinus"), re-read here. Outline, What came of it 4.

5. **documentedStories[0].text** (clearly wrong: the quoted words are not the letter's).
   Old: "‘the blessed father Cyprian has withdrawn’" / New: "‘the blessed father Cyprian has for a certain reason withdrawn’"
   Old: "‘the hireling, who is not the shepherd, seeth" / New: "‘the hireling, whose own the sheep are not, seeth"
   Evidence: `anf05...xml` 28796-28799 ("the blessed father ... Cyprian has / for a certain reason withdrawn"); 28818-28819 ("But the hireling, whose own the sheep are not, seeth the wolf coming, and leaveth the sheep, and fleeth").

6. **documentedStories[1].sources[1].note** (a modern work named in a source note; moved).
   Old: "The court-style record of the two hearings; English in Musurillo, The Acts of the Christian Martyrs (Oxford, 1972)."
   New: "The court-style record of the two hearings."
   Added: `documentedStories[1].modernWorks`, Musurillo's book (title, author, year, publisher as the note gave them; the `note` says what it covers). Not held, so no `url`.

7. **documentedStories[2]** (clearly wrong against the held primary text, Possidius in Weiskotten's Latin and English; the story was marked as not yet read against it).
   - verification. Old: "from reference summaries; primary text not yet read" / New: "checked directly against the primary text".
   - text. Old: "and quoted to his companions a saying he had made his own: ‘He is no great man who thinks it a great matter that trees and stones fall and mortals die.’" / New: "and took comfort in a wise man’s saying: ‘He is not to be thought great who thinks it strange that wood and stones should fall and mortals die.’" Evidence: `possidius...txt` 4073-4076 ("he was consoled by the thought of a certain wise man who said: "He is not to be thought great who thinks it strange that wood and stones should fall and mortals die.""); Latin 4030-4033. Possidius does not say he quoted it to his companions.
   - text. Old: "He asked that the four penitential psalms — the ‘Psalms of David that deal with repentance’ — be copied out in large letters and fixed to the wall opposite his bed," / New: "He asked that ‘the shortest penitential Psalms of David’ be copied out and fixed to the wall opposite his bed," Evidence: 4925-4929 ("he commanded that the shortest penitential Psalms of David should be copied for him ... as they hung upon the wall"); Latin 4888-4891 ("Psalmos Davidicos, qui sunt paucissimi de poenitentia ... contra parietem positos"). "four" is only Weiskotten's note on which are shortest (5963-5965, modern); "in large letters" is in neither.
   - text. Old: "‘because as a poor man of God he had nothing to leave’" / New: "‘because as a poor man of God he had nothing from which to make it’". Evidence: 4983-4984; Latin 4944-4945.
   - caveat. Old: "‘the penitential ones’" / New: "‘the shortest penitential Psalms of David’". Evidence: as above.

8. **documentedStories[0].sources and [2].sources** (moved: modern works). Removed, word for word as they stood: `{"work": "J. Patout Burns, Cyprian the Bishop (Routledge, 2002)", "type": "reference", "note": "On the flight, the Roman letter and the lapsed controversy."}` and `{"work": "Peter Brown, Augustine of Hippo: A Biography, new ed. (California, 2000)", "type": "reference", "note": "On the last years and Possidius’ account."}`. Added: each story's `modernWorks`, the same words split into `title`, `author`, `year`, `publisher` and `note` ("new ed." dropped from the title). Neither is held, so neither has a `url`. Source_Sheet, Library sweep ("Modern on the card: Burns 2002 and Brown 2000 (not held; Modern works list at most)").

9. **uncertain** (new). Six items:
   - Cyprian's withdrawal: his reason, with "so as not to stir the riot further" (Recheck move 3, "card"; K1, CyL 2968-2976, `anf05...xml` 30172-30188), and the charge against it (K2; Source_Sheet, section 5).
   - The charge behind the split, its falsity in Optatus, Felix cleared, and no fixed year (R1, R2, R8: `optatus...txt` 207, 217, 303; Outline, Do not say, "in 311" and "the rival church's charge as fact").
   - The rival church through its enemies, and its size by Possidius's account (R4, Opt 153; R5, `possidius...txt` 2060-2063; Outline, Do not say, "the Donatists were the majority": card). Possidius's own words are kept ("a large multitude of the Africans", "lain prostrate") in place of the outline's "the larger church", which goes further than the line.
   - Who the heretics were at the Gladness, and Optatus's different use of the word (E6, R5, R6; Outline, Connection and Words to explain).
   - The plague rests on Pontius, with the dead in the streets and the sick left (length move 10, "card"; P1, `anf05...xml` 27940-27955).
   - Dates resting on modern reckoning (Source_Sheet, section 5; Outline, Leave out, last item).

10. **sources** (new). Twenty-one old sources, each with `file`, re-read at the lines below. The notes carry every item the outline marks for the card:
   - Hartel's Latin letters: Cut first 3 and the B1 money for confessors and poor, with the confessor gloss (K3 744-751, K4 757-767); K6 (2920-2927); Recheck move 3 (K1); Recheck move 1 and Cut first 4 (L5 6228-6233, L6 6239-6243); the B1 long penance (L3 7578-7590); Cut first 7 (P4 10800-10858, P5 10893-10930); Cut first 8 (D1 15418-15434). "in Numidia" is left out (Outline, Do not say).
   - ANF 5: length moves 10 and "by rank" (P1, P3 27981-27990); the Roman letter (K2).
   - Hartel's On the Lapsed: length move 8 (S5, CyLap 345-351).
   - Hartel's Pontius and Acta: the B1 "sent into exile" (S6, PonL 41430-41432); length moves 7 and "the door", and the B1 girls guarded (D3 41513-41516); Cut first 5, the cloths (D4 41583-41597); the twenty-five gold pieces (D4).
   - Knopf: D3 (4878-4880).
   - Possidius: Recheck move 5 and Cut first 10 (H1 1803-1818, H2 1861-1863); Cut first 2 and length move 9 (B1); R5 (2201-2202); "and men of any sect" and the B1 mealtime and fasting (B3 3150-3161); the forced service, told of his letters in worldly cases as the Do not say requires (B4 3206-3209); Recheck move 7 (B5 3597-3604); length move 6 (S7 3982-3985); V9 (4067-4070); the B1 siege and last preaching (V6 4082-4087, 4127; V7 4147-4148; V8 4936-4938); Cut first 11 and Recheck move 6 (V2 4281-4285, V3 4318-4326); the B1 crowd in the church (V4 4575-4580).
   - Goldbacher, Letter 29: "of a former bishop" (E1 6279-6281); the Opening's "serving under the aged bishop" (E1, NP1 25607-25611); E4 and E5 (Leave out, "card at most"; AugEp34 6529-6588); Recheck move 4, the psalms and hymns until the light failed (E6 6647-6687).
   - NPNF 1.1, Letter 93: B9 (38240-38258) and B10, with the confiscation the review fix pass sent to the card (38000-38010, 38136-38141).
   - Retractations and the Psalm: Cut first 9 (H5, Retr 6833-6838; PsD 1293-1294).
   - On Instructing Beginners: Cut first 6 (B2, CatE 1793-1810).
   - Sermon 310: B6 and B7 (99254-99292).
   - Optatus in English and Latin; On Baptism (W1); Procopius (W2); Eusebius (S4, 37413-37414); Jerome (P6, 57618-57622); Facundus (W5); Calvin (`calvin_institutes-christian-religion-vol2_beveridge1845.txt` 25389-25391, "Were we disposed to frame an entire volume out of Augustine", in Book III, ch. 22), which supports the legacy's existing Calvin sentence.

Every Cut first item marked "for the card" is now on the card, in `why`, `legacy`, `uncertain` or a `sources` note: 2, 3, 4, 5, 6, 7, 8, 9, 10, 11; so are the outline check's B1 items, the recheck's moves 1 and 3 to 7, the length moves marked "card" (6 to 10), the review fix pass's four marked "card", What came of it 1 to 4, and the heart's "Carried on the card" line (K4, P5, E6, B2, B5, H1). Not carried: the Pelagians (B8, Leave out "card"): Possidius's line gives no plain sense of what they taught, and Kit Part 1 bars naming it without one; `pelagianism` tells it.

## Entry fields

For release to apply once the checker passes them. Release also sets `longDescription` from the brief.

1. **why:** edit 1.
2. **teaser:** edit 2.
3. **relationsSummary:** no change. "From the 310s" spans both contested years (311, 312) and agrees with the brief's "soon after the great persecution of the early 300s".
4. **voices, legacy, documentedStories:** edits 3 to 8.
5. **uncertain, sources, quotationOriginals:** new on the entry; edits 9 and 10 and Quotations.
6. **documentedStories[0], [1] and [2].modernWorks:** edits 6 and 8.
7. **modernWorks (new):** the printed editions and translations the outline used to read its old texts (Source_Sheet, abbreviations), all printed before 1931:

```json
[
 {"title": "S. Thasci Caecili Cypriani Opera omnia (Corpus Scriptorum Ecclesiasticorum Latinorum 3.1-3.3)", "author": "Wilhelm von Hartel (ed.)", "year": "1868-1871", "note": "The Latin text of Cyprian's treatises and letters, with the Life attributed to Pontius and the Acta Proconsularia."},
 {"title": "Ante-Nicene Fathers 5: Fathers of the Third Century: Hippolytus, Cyprian, Caius, Novatian", "author": "Alexander Roberts and James Donaldson (ed.); R. E. Wallis (tr.)", "year": "1886", "note": "English translations of Cyprian's letters and treatises and of Pontius's Life of Cyprian, with the editors' notes."},
 {"title": "Ausgewählte Märtyrerakten, third edition", "author": "Rudolf Knopf (ed.); Gustav Krüger (rev.)", "year": "1929", "publisher": "J. C. B. Mohr (Paul Siebeck), Tübingen", "note": "Includes the Acta Proconsularia of Cyprian in Latin."},
 {"title": "Sancti Augustini Vita scripta a Possidio episcopo", "author": "Herbert T. Weiskotten (ed. and tr.)", "year": "1919", "note": "Possidius's Life of Augustine in Latin and English, with Augustine's Letter 228 and the editor's notes."},
 {"title": "S. Aureli Augustini Hipponiensis Episcopi Epistulae (Corpus Scriptorum Ecclesiasticorum Latinorum 34 and 57)", "author": "Alois Goldbacher (ed.)", "year": "1895-1911", "note": "The Latin text of Augustine's letters, among them Letters 29, 93 and 228."},
 {"title": "Nicene and Post-Nicene Fathers, first series, 1: The Confessions and Letters of St. Augustine", "author": "Philip Schaff (ed.); J. G. Cunningham (tr.)", "year": "1886", "note": "English translations of Augustine's Confessions and letters, with notes on their dates."},
 {"title": "Nicene and Post-Nicene Fathers, first series, 4: Augustine, The Writings against the Manichaeans and against the Donatists", "author": "Philip Schaff (ed.); J. R. King (tr. of On Baptism)", "year": "1887", "note": "English translation of Augustine's On Baptism, Against the Donatists."},
 {"title": "Sancti Aureli Augustini Retractationum Libri Duo (Corpus Scriptorum Ecclesiasticorum Latinorum 36)", "author": "Pius Knöll (ed.)", "year": "1902", "note": "The Latin text of Augustine's Retractations."},
 {"title": "Sancti Aureli Augustini Scripta contra Donatistas (Corpus Scriptorum Ecclesiasticorum Latinorum 51)", "author": "Michael Petschenig (ed.)", "year": "1908", "note": "The Latin text of Augustine's writings against the Donatists, among them his Psalm against the Party of Donatus."},
 {"title": "S. Aureli Augustini Hipponiensis Episcopi De catechizandis rudibus liber unus", "author": "Joseph Patrick Christopher (tr.)", "year": "1926", "publisher": "The Catholic University of America, Washington", "note": "Augustine's On Instructing Beginners in Latin and English, with a commentary."},
 {"title": "The Work of St. Optatus, Bishop of Milevis, against the Donatists", "author": "O. R. Vassall-Phillips (tr.)", "year": "1917", "note": "English translation of Optatus, with notes and the appended records of the early hearings."},
 {"title": "S. Optati Milevitani Libri VII (Corpus Scriptorum Ecclesiasticorum Latinorum 26)", "author": "Carl Ziwsa (ed.)", "year": "1893", "note": "The Latin text of Optatus."},
 {"title": "Procopius, History of the Wars, Books III and IV: The Vandalic War", "author": "H. B. Dewing (tr.)", "year": "1916", "note": "Greek text and English translation of Procopius's account of the war in Africa."},
 {"title": "Nicene and Post-Nicene Fathers, second series, 1: Eusebius, Church History", "author": "Arthur Cushman McGiffert (tr.)", "year": "1890", "note": "English translation of Eusebius's Church History, with notes."}
]
```

8. **Not changed, for release to weigh:** the census `dates` ("c. 240s-430") and `start` (246) begin before the brief's "From the 250s to 430". The role does not name them, so they are left; edit 2 brings the teaser to the brief.
9. **entry:** the census `entry` is null for this movement, so there are no current `tile`, `intro`, `summary` and `recordHolds` to rebuild. See `Entry_Texts.md`.

## Not found (left in place)

- teaser: "the parish before the word existed" (a judgment no old source makes).
- voices[0]: "whose letters are the fullest surviving picture of how a third-century congregation actually ran"; voices[2]: "the most extensively documented working pastor of the ancient world"; voices[3]: Possidius "cataloged his works" (no held line in the sheet).
- legacy: "The Vandals took the province in the 430s"; "The Arab conquest came in the seventh century. After it, Latin Christianity there slowly died out." (outside every held line used); "Cyprian's letters laid the ground for how the West thinks about the bishop's office and the unity of the church"; "Augustine's sermons shaped Christian preaching for well over a thousand years"; "These congregations also worked out the catechumenate ... Both became the pattern for Western sacramental discipline"; the closing sentence. Each is a later judgment. The Calvin sentence is found (Calvin, above).
- documentedStories[0]: "Decius’ order that everyone sacrifice" (Outline, Do not say, "ordered everyone in the empire to sacrifice": the held lines give a persecution whose order called for sacrifice); "the crowd in the amphitheater" (Hartel Ep. 59 has "amphitheatro", 9666, not re-read for this); "in ordinary dress" (Letter 5 gives turns and no crowds, `anf05...xml` 28973-28995, no dress); "The Roman clergy, whose bishop Fabian had just been executed". Also for the checker: "It was not subtle." and the title's "Sneer" are a judgment, and the same letter says of the withdrawal "in doing which he acted quite rightly, because he is a person of eminence" (`anf05...xml` 28799-28800). Not an edit this role makes, since no held line contradicts the letter's quoted words now that they are corrected.
- documentedStories[1]: caveat, "whose text has been lightly edited in transmission".
- documentedStories[2]: "in the summer of 430"; "Augustine, seventy-five" (Possidius gives seventy-six years at his death, 4919-4920); "He died on 28 August" (not in Possidius; Weiskotten's note cites Prosper, 149); "The city fell the following year" (Possidius says only that Hippo was burned after his death); "It is the last documented scene of the most documented pastor of antiquity, and it is a scene of penitence rather than triumph" (a judgment).

## Validator

A scratch copy of the census, with this card merged into the entry and the brief as `longDescription`, kept outside the repository, through `node tools/validate-census.mjs <copy> --skip-quotes`: 629 movements, 736 edges, 10 eras, 0 errors, 4 warnings, all on other entries (short names). The full run with the quotation check was killed for memory on this machine, both on the copy and on the live census. That check reads only person and council entries, so this card cannot change its result. The tradition's quotations were checked by the scratch fold check above. The entry-level `modernWorks` above was not in the scratch run.
