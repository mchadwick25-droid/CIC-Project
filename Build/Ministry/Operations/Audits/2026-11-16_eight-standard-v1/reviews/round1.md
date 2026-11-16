# Round 1 review — eight Standard v1 briefs plus two examples

## Step 0 — blind pair (recorded before reading anything else)

TEXT X is the stronger Standard v1 brief. Concretely:
- Setting first: X opens on year (335), region (the Roman East), the context (churches still split over Arius ten years after Nicaea), place (Alexandria in Egypt) and the tradition by a census-style name ("Alexandrian Christianity"). Y opens straight on the Tyre scene with no tradition, no region and no context.
- No modern scholar: Y names Archibald Robertson, a modern editor, to carry a claim ("more than half of what survives was written in those years of hiding"). X has none.
- Modern-English quotations: Y keeps old printed wording ("For He was made man that we might be made God"; "begotten not made, One in essence with the Father"). X renders them ("He became human so that we might be made God"; "begotten, not made").
- Impact: X gives impact with witnesses (Gregory on hypostases/persons and the written confession; Jerome on Marcella; Cyril). Y's impact is thinner: a sermon's opening line of praise and the Cyril line, with no stated consequence of his stance beyond survival in hiding.
- Personal then impact: X runs personal (Tyre, Nicaea, exiles, death) then impact (Gregory, Antony/Marcella, Cyril). Y is all personal plus praise.
- Y does have small strengths X lacks (Peter as successor, the search of tombs, "in his absence"), but none of them outweighs the three structural misses above.

After the full read: TEXT X is the new Standard v1 Athanasius (branch `claude/cft-eight-v1`), and TEXT Y is the old bar text (`origin/main`). The preference was given with concrete reasons before I knew which was which, and it favours the new brief. No finding.

---

# Round 1, full checklist

The reviewer was Opus, fresh and independent. No model or API calls were made, and no repo file was changed. Every line check below was done by hand against `cic/texts/`. The readability figures are from `python3 -m engine.m1.profile_readability --report`.

Comparators (drift guard 2):
- **The eight:** each one was read beside `gregory-of-tours.brief.txt` (the Standard v1 example) and beside its own old bar text (`git show origin/main:...`). Methodius's old text was also used as the thin-record model.
- **Gregory of Tours and Benedict:** each was read beside its own `origin/main` text and the old bar Athanasius.

## Readability (all pass the floor and ceiling)

| Brief | Words | Grade (full) | Reading ease (names out) | Words/sentence | Joins/100 | Short sentences |
|---|---|---|---|---|---|---|
| Origen | 389 | 9.4 | 73.2 | 16.9 | 0.8 | 13% |
| Methodius | 373 | 9.3 | 74.2 | 17.8 | 0.3 | 5% |
| Constantine | 398 | 8.9 | 76.0 | 18.1 | 0.5 | 5% |
| Athanasius | 391 | 9.0 | 78.6 | 18.6 | 0.8 | 10% |
| Ephrem | 378 | 9.1 | 77.8 | 18.9 | 0.8 | 0% |
| Gregory of Nazianzus | 382 | 9.6 | 75.1 | 18.2 | 0.8 | 5% |
| Gregory of Nyssa | 375 | 9.4 | 71.2 | 18.8 | 1.1 | 0% |
| John Chrysostom | 390 | 9.0 | 70.6 | 17.7 | 0.8 | 9% |
| Gregory of Tours | 396 | 9.3 | 74.8 | 20.8 | 1.5 | 11% |
| Benedict of Nursia | 430 | 8.8 | 80.8 | 20.5 | 0.7 | 5% |

No modern scholar's name, and no "editor", "translator", "scholar" or "historians", appears in any of the ten briefs. I checked this with grep and again by reading.

---

## 1. Origen — CLEARS (compared against Gregory of Tours and the old Origen)

**Craft**
- *Storytelling.* The line of the story: a martyr's son becomes Alexandria's teacher, is driven out by his bishop, and leaves the church a way of reading Scripture that it kept and a speculation that it condemned. It can be retold. Weakest sentence: "Later the bishops of Caesarea and Jerusalem ordained him a priest." It stands against the Athanasius model, "from the severed hand to the exiles". It carries the story to Demetrius in the next sentence. Pass.
- *Flow.* Weakest link: "Its church is the one the tree calls Alexandrian Christianity, and Origen's father was among those arrested." Two unrelated facts are joined only by "and". Compare the bar's "In his eighteenth year he took charge of teaching the faith in Alexandria, because everyone else had fled." Pass, with a non-blocking note (N1).
- *No AI tells.* Weakest: "His great work was on Scripture." It is a paragraph that opens on a thesis. It is earned at once by Hebrew, the Hexapla and Job. Model: Chrysostom's opening. Pass.
- *No hanging sentences.* The close is "Three centuries after his death, the acts of a council at Constantinople list his name among condemned heretics." It is the bar's own close and finishes the contested thread. Model: Ephrem's close. Pass (see N2).
- *Everything relevant.* Every sentence on a source (the Philocalia, Job) now carries a consequence. The "why he mattered" idea is there: body, soul and spirit. Pass.

**Rigor.** These claims were checked in the file:
- Eusebius on the persecution and the letter.
- Jerome on Demetrius (npnf203 40532-40538), Tyre, sixty-nine and Hebrew.
- The Job preface (npnf206 47003-47012).
- Athanasius, De Decretis 27 (npnf204 28647-28691).
- The Pontus brothers (Eusebius VI.30).
- Methodius, Pamphilus and the 553 anathema.

Every causal link is sourced: "because everyone else had fled", Demetrius "enraged", Job defended "by pointing to those marks". The refs say no source ties the Demetrius quarrel to the move to Caesarea, and the brief only puts them in sequence. Witnesses are named where trust turns. Eusebius's own defence of Origen is shown in the last paragraph. Nothing is invented.

**Quotations**
- Q20, "Be careful not to change your mind because of us." It matches the FINAL and covers every clause.
- Q21, "the hardworking Origen". It matches the FINAL.

**Shape and length.** The setting comes first (around 202, Alexandria, Egypt, the tradition, the persecution), then personal, then impact. 389 words is about 2:36. The refs give a length line: four stances with consequences.

**Findings**
- N1 (NON-BLOCKING): the weak "and" join in sentence 2 (above). It could tie the tradition to the arrests or to the city.
- N2 (NON-BLOCKING): the brief closes on the 553 condemnation. Working rule A64 asks that the close "still says what they changed or defended, with its witness". The old bar closed the same way, so this is a note for the coordinator, not a regression. One fix would be to move the contested paragraph before the Athanasius/Pontus paragraph, so the close is Athanasius calling on Origen as a witness.
- N3 (NON-BLOCKING): "around 202" and "231" are McGiffert's regnal-year conversions. The card's What is uncertain must say so, as the refs plan.

## 2. Methodius of Olympus — CLEARS (compared against Gregory of Tours, old Methodius and old Origen)

**Craft**
- *Storytelling.* The line: a Lycian bishop who argued with Origen over the body left an answer that later defenders of the faith leaned on. Pass.
- *Flow.* Weakest: "He also wrote a Banquet of the Ten Virgins, in which ten women in turn praise the chaste life." It connects to nothing. Compare Nyssa's "Macrina had turned him around once before ..." Pass narrowly (N4).
- *No AI tells.* None found. Model: Chrysostom's opening. Pass.
- *No hanging sentences.* The close, "He named him among the bishops and martyrs whose words witness to the church's faith in Christ.", finishes the story. Pass.
- *Everything relevant.* The Banquet sentence is the one side fact. The fig-tree passage carries the "why he mattered" idea. Pass.

**Rigor.** These were checked in the file:
- Socrates VI.13 (npnf202 18135-18154): "Worthless characters", the retraction, Xenon.
- Eusebius via Jerome (npnf203 51484-51490).
- Jerome's Letter 70, "ably answered" and the ten thousand lines (npnf206 16535-16545).
- Epiphanius's "vir apprime doctus acerrimusque veritatis patronus" and "ad verbum omnia transcribam" (Oehler 27050-27057 and 19228-19237).
- Photius.

Every causal link is sourced. Both witnesses are marked as partisan. No modern scholar is named.

**Quotations.** Q19 is unchanged. It is judged current English, matches the FINAL, and is verbatim at anf06 35400-35402.

**Shape and length.** The setting comes first. 373 words, within the 2:30 stretch.

**Findings**
- N4 (NON-BLOCKING): "two of Origen's admirers tell an odd story about it". Eusebius's question ("after having said this thing and that of his doctrines") does not itself tell the story of attack and then praise. Jerome reads it that way, as the refs admit. A small recast would hold it to what Eusebius says, for example "Eusebius ... also complained of it".
- N5 (NON-BLOCKING): "That reply is lost" rests on an editor's note. It is widely accepted and traced in the refs, so it is acceptable. The refs offer a version that drops it.
- N6 (NON-BLOCKING, for the coordinator): Methodius grew from 243 to 373 words. The pattern still cites it as the thin-record model "about 240 words". The added material is real sourced stance and consequence (Epiphanius, Porphyry, Theodoret), so this is not padding. But the pattern's model is now stale (see R6).

## 3. Constantine the Great — CLEARS (compared against Gregory of Tours and old Constantine)

**Craft**
- *Storytelling.* The line: a vision before the bridge led to freedom for the churches, a council he chaired, and a quarrel he could not end. Pass.
- *Flow.* Weakest link: "The Christians' meeting places were to be given back." A short flat line follows a 41-word sentence. Compare Origen's "because everyone else had fled". Pass.
- *No AI tells.* None found. Pass.
- *No hanging sentences.* The close is the burial custom. It is joined to Sozomen's judgment, and it finishes the story. Pass.
- *Everything relevant.* Pass.

**Rigor.** These were checked in the file:
- Life I.28: the oath, "hard to believe", and "Conquer by this" (npnf201 61196-61206).
- Lactantius's dream.
- The Milan edict (anf07 10680-10686).
- Eusebius's letter on "the insertion ... of that single word homoousios" (npnf202 3046-3053).
- Socrates I.25-27.
- Sozomen II.34 (npnf202 30674-30698).

"Sat among them" is supported by Life III.10 (npnf201 64428). The vision is told as contested, with both witnesses and their leanings. The homoousios gloss carries no quotation marks, which resolves the comparison's attribution flag.

**Quotations**
- Q4, "Conquer by this," unchanged. It matches the FINAL.
- Q5, "your fellow servant," matches the FINAL. See R4 for its citation.
- Q7, "the first of the emperors who began to be zealous for the Church", unchanged. It matches the FINAL.

**Shape and length.** The setting comes first (312, Rome, the tradition, the persecution). The region is left implicit. 398 words is about 2:39. The refs give a length line.

**Findings**
- N7 (NON-BLOCKING): the Milan sentence runs 41 words. It reads in one breath only with effort. It could be split at "so that".
- N8 (NON-BLOCKING): Q7 closes with the full stop outside the quotation mark. The printed sentence goes on ("and to bestow upon her high benefactions"). The comparison asked for an ellipsis, no stop, or the clause. The stop outside the mark is a fair answer, but it differs from the other nine briefs' style.

## 4. Athanasius of Alexandria — CLEARS (compared against Gregory of Tours and old Athanasius)

**Craft**
- *Storytelling.* The line: accused with a severed hand, he held to "begotten, not made" through five flights. He made peace over words, and the church followed him. Pass.
- *Flow.* Weakest: "That stand cost him his city again and again." It opens a paragraph on a thesis. It is earned by a sourced cause (Socrates on unity, Gregory on Julian). Model: Nyssa's "But it was his sister ...". Pass.
- *No AI tells.* None found. Pass.
- *No hanging sentences.* The close on Cyril finishes the story. Pass.
- *Everything relevant.* The creature argument is kept. Pass.

**Rigor.** These were checked in the file:
- Socrates I.27 and I.29 (npnf202 5027-5036, 5086-5118).
- Sozomen's rumour (30008-30016).
- Socrates I.8 (2792-2797).
- I.35, Trier (5356-5372).
- The Festal Index, 328, 335, the four flights and 373 (npnf204 64077-64533).
- Gregory, Oration 21.33 and 21.35 (npnf207 30354-30433).
- The Life of Antony, "his attendant" (31195-31199).
- Jerome on Marcella (npnf206 26085-26096).
- Cyril (Pusey 5392-5394).

Gregory is marked as a panegyrist ("who praised him in a sermon"). Tyre and Trier are told as contested.

**Quotations**
- Q1, "begotten, not made." It matches the FINAL.
- Q2, "He became human so that we might be made God." It matches the FINAL.
- Q3, "our blessed Father Athanasius, praised by all." It matches the FINAL.
- All three cover every clause.

**Shape and length.** 391 words is about 2:36. The refs give a length line.

**Findings**
- N9 (NON-BLOCKING): "a young deacon". Socrates (2794-2796) and the Gregory note say "deacon", not "young". The word is carried over from the old bar. Either trace it or drop it.
- N10 (NON-BLOCKING): the sentence on the Life of Antony and Marcella sits in the place of a stance and its consequence. But Jerome says Marcella heard of Antony by word of mouth, from Athanasius, Peter and the priests of Alexandria, not from the book. The brief does not claim the book caused it, which is correct, but a listener may infer it.

## 5. Ephrem the Syrian — CLEARS on the brief text; release is held on record item R2

**Craft**
- *Storytelling.* The line: a deacon who ran the famine relief had spent his years fighting rival teachers in song, and the schools of the East traced themselves to him. Pass.
- *Flow.* Weakest: "His years in Edessa had been spent against rival teachers." It is a summary opener. Compare the bar's "Ephrem feared the people would absorb them, so he wrote hymns ...", which the brief keeps. Pass.
- *No AI tells.* None found. Pass.
- *No hanging sentences.* The close, "In his telling, the schools ... began with Ephrem.", finishes the thread. Pass.
- *Everything relevant.* Pass.

**Rigor.** These were checked in the file:
- Palladius 40 (Clarke 471): the cell, the rich, "hospitaller", 300 beds, death after a month.
- Sozomen III.16 on Harmonius (npnf202 32081-32102).
- Barhadbeshabba (Scher 20434-20442, 20738-20743): the school opened, transferred, "les écoles se multiplièrent dans l'empire des Perses".

Barhadbeshabba is placed as the Nisibis school's own historian, writing late, and his account is told as "in his telling". Sozomen and Ephrem's own homily are set against each other on Harmonius against Bardaisan.

**Quotations**
- Q8, "Look, on your behalf I appoint myself to run the shelter." It matches the FINAL. The verdict was "changes meaning", and the FINAL keeps the ambiguous "on your behalf".
- Q9, "It tainted my pure ears." Unchanged.

**Shape and length.** 378 words. There is no length line in the refs, which is non-blocking at 3 words over the stretch.

**Findings**
- N11 (NON-BLOCKING): the pattern's model "Ephrem, which opens on the famine and closes on it" no longer describes this brief. The famine now closes paragraph 1 (see R6).

## 6. Gregory of Nazianzus — CLEARS (compared against Gregory of Tours and old Nazianzus)

**Craft**
- *Storytelling.* The line: from a borrowed house he preached the Trinity until the city's churches filled again. He gave up the see, and the church kept his teaching on Christ's full humanity. Pass.
- *Flow.* Weakest: "Many bishops had called him there from Asia Minor." It is flat. Compare Origen's "because everyone else had fled". Pass.
- *No AI tells.* None found. Pass.
- *No hanging sentences.* The close on Justinian, 553, finishes the story. Pass.
- *Everything relevant.* Pass.

**Rigor.** These were checked in the file:
- Sozomen VII.5, "as I believe" and the Anastasia passage (npnf202 40644-40660). The brief rightly tells this as his belief.
- The farewell, Oration 42.26 (npnf207 40853-40868), told loosely, without marks.
- Agatho (npnf214 25195-25206).
- Justinian (23134-23138).

The resignation is told only as far as Socrates and Sozomen agree. The refs say plainly that the record does not tie the emperor's order to the sermons, and the brief does not claim it.

**Quotations.** Q10 to Q14 each match the FINAL. Q11 and Q12 are split around "he wrote to Basil" with no change of words.

**Shape and length.** 382 words. There is no length line in the refs. Non-blocking.

No findings beyond the length line.

## 7. Gregory of Nyssa — DOES NOT CLEAR (compared against Gregory of Tours and old Nyssa)

**Craft**
- *Storytelling.* The line: an exile who came home inherited Basil's fight with Eunomius. An imperial law named him as a mark of the true faith, and the church set its seal on his canons. Pass.
- *Flow.* Weakest: "He also wrote that the Holy Spirit is 'of the same rank as the Father and the Son.'" This "He also wrote" line reads as a list. Compare Nyssa's own bar model, "But it was his sister who persuaded him". Pass narrowly.
- *No AI tells.* None found. Pass.
- *No hanging sentences.* The Great Catechism paragraph stands on its own. Nothing before it leads into it, and nothing after it follows from it. See B1. Fail, folded into B1.
- *Everything relevant.* Pass.

**Rigor.** These were checked in the file:
- The Life of Macrina (Clarke 184, 214-218): the exile under Valens, the parents' prayers.
- Nazianzus, Letter 11 (npnf207 46252-46258).
- Basil's Letters 225 and 237 (npnf208 39561-39574, 40844-40852).
- CTh 16.1.3 (6886): "gregorio episcopo nysseno". The brief honestly says the law "gives no reason".

The editors' universal-salvation dispute is rightly kept off the brief.

**Quotations.** Q15, Q16 and Q17 each match the FINAL.

**Findings**
- **B1 (BLOCKING), checklist 15.** The Great Catechism paragraph tells a stance, the restoration of those lying in sin and of all creation. It tells no consequence, and it does not say plainly that the held record shows none. The writer's refs flag this themselves: "Gap for the reviewer: this stance has no sourced consequence in held files. I did not fill it." Standard v1 says: "Where the record stops, the brief says so."
  - The fix is a rewrite of that passage. One way is a clause saying that the held record does not show how this teaching was received. Avoid ending it on a bare "how" (Writing Standard).
  - Another way is to tie the paragraph to the canon and council material that follows, if a held source makes that link.
- N12 (NON-BLOCKING): "and the new emperor Gratian called the exiles home. One of them was Gregory of Nyssa". Gregory's own text gives his exile under Valens, and Socrates V.2 gives the general recall. The link between the two is a reasonable inference, widely accepted, but no single source states it.

## 8. John Chrysostom — DOES NOT CLEAR (compared against Gregory of Tours and old Chrysostom)

**Craft**
- *Storytelling.* The line: the preacher who shamed a fallen consul made enemies at court, was deposed and died in exile, and his body brought his followers home. Pass.
- *Flow.* Weakest: "He rebuked men in office too." It is joined at once to Socrates's cause. Pass.
- *No AI tells.* None found. Pass.
- *No hanging sentences.* The close on Proclus finishes the story. Pass.
- *Everything relevant.* Pass.

**Rigor.** These were checked in the file:
- Socrates VI.5 (npnf202 17316-17365): the tide of unpopularity, the first eunuch consul, the sanctuary law, under the altar table, "added insult to cruelty".
- VI.3, the law courts and Diodore's literal sense (17139-17185).
- VI.2, the ordination (17097-17110).
- Palladius on the hospitals (Moore 3768-3776) and Pityus (6392-6410).

**Quotations.** Q18, "Glory to God for all things." Unchanged, and it matches the FINAL. See R1 and R4 for its record.

**Findings**
- **B2 (BLOCKING): a claim not in the cited file.** The brief says "In 438 Bishop Proclus of Constantinople carried John's body home in procession and restored him to the church's communion." Socrates VII.45 (npnf202 21453-21474) says Proclus "brought back to the Church those who had separated themselves", and that "the admirers of that prelate were conciliated, and again associated in communion". It is the followers who are restored to communion, not John. The old bar did not have this clause. It is new in v1 and unsourced. Cut it, or source it to a held text that says it.
- N13 (NON-BLOCKING): "carried John's body home". Constantinople was his see, not his home (Antioch). The old "back to the city" was exact.
- N14 (NON-BLOCKING), checklist 16: "the Antiochene church of Syria" matches neither census name: "Antiochene Exegetical Christianity (Chrysostom-centered)" and "Antioch in Chrysostom's Day". It can also be confused with another tree tradition, "The Church of Antioch in the Third Century". The pattern allows plain words, but the name should be the census's.

## 9. Gregory of Tours (Standard v1 example; only its quotations changed) — CLEARS

`git diff origin/main` shows only the seven quotations changed. The bar copy and the era3/batch5 copy are identical.

**Quotations.** G1 to G7 each match the comparison's FINAL.
- G1 and G6 follow the held Latin of the MGH edition, dropping Dalton's "all" and taking "hac", "this".
- G4 follows the Latin "believe" and "churches".
- G2 keeps "People lamented, he says". Brehaut prints "many were lamenting and saying" (lines 844-851).
- G7 has no held Latin. The comparison says so.

Craft is unchanged from the version Mark approved. The new wording reads naturally and has no archaic forms left.

**Shape and length.** 396 words. Length is unchanged from Mark's approval.

## 10. Benedict of Nursia (Standard v1 example; only its quotations changed) — CLEARS

The diff shows only G8 to G12 changed. The bar copy and the era3/batch2 copy are identical.

**Quotations.** G8 to G12 each match the FINAL. G8, "You do many evil things.", follows the held Latin "Multa mala facis" (AASS Mart. III 79157-79162) and drops "daily", the 1608 translator's word. See R5.

**Shape and length.** 430 words, up from 423 at Mark's approval, because the renderings run longer. The tradition comes in sentence 4, not in the first two or three. Both points were in the version Mark approved, so they are non-blocking notes only.

---

## Record findings (these do not change the brief text, but they hold release)

- **R1 (BLOCKING for release).** In `Build/Ministry/Operations/Audits/2026-11-16_eight-standard-v1/quotation-originals.json`, two `modern` fields carry the comparison's working notes: Constantine Q7, "... zealous for the Church (unchanged; the sentence continues in the source)", and Chrysostom Q18, "Glory to God for all things. (unchanged; repoint the citation to lines 1610-1611)". The README says this file goes into the census cards at release. As it stands, it would put process commentary in front of visitors. Strip both notes to the bare rendering.
- **R2 (BLOCKING for release, Ephrem).** Q8 was judged "changes meaning". The ruling of 2026-11-16 says "Any difference in meaning is marked as uncertain on the card, and both readings are kept ... Only then may the rendering carry quotation marks." The comparison drafts the card note ("On your behalf" may mean "as your agent" or "for your sake"; "hospitaller" means one who runs a house of care for strangers, the poor and the sick). But `quotation-originals.json` carries no uncertainty note, and the eight's cards are not yet written. Put the note in the record that feeds the card.
- **R3 (NON-BLOCKING).** For the "minor" verdicts, the comparisons draft card notes: Q2, Q3, Q6, Q12, Q13, Q15 and Q19, and G2 and G9 to G12. None of them is in `quotation-originals.json`, or in the `uncertain` field of the Gregory and Benedict cards. If "any difference in meaning" is read to cover a nuance, these belong on the cards too. The coordinator should decide.
- **R4 (NON-BLOCKING): citations that disagree.**
  - Q1: the record cites Pusey's Cyril at 4574, but the refs cite npnf204 19679.
  - Q5: the record cites npnf201 63903-63904, which is Constantine's letter to Alexander and Arius, written before Nicaea. The refs and the brief's context ("sat among them ... as he wrote") point to the letter after Nicaea, at 64593-64594.
  - Q18: the renderings were made on npnf109 1990-1997, and the comparison says to repoint to 1610-1611. The record cites Palladius (Moore) 6498-6499. The wording is identical in all three, so meaning is not at risk, but the card should cite one span and the record should say which one.
- **R5 (NON-BLOCKING): FINALs written by the comparer.** G1, G4, G6 and G8 (and, more lightly, Q8, Q11 and Q15) take a FINAL that neither renderer produced, made by checking against the held Latin. In each case this is closer to the original. But the printed line on the card will then hold a word the rendering drops (G8 "daily", G1 "all"). Add one line to the card saying that the modern English follows the Latin there.
- **R6 (NON-BLOCKING; doc hygiene, flagged and not touched; pattern edits need Mark's quoted words under guard 1).** Several references are now stale:
  - In `Who_Profile_Pattern.md`, "The bar": "The eight's texts are not changed for it"; "Methodius, with little known, takes about 240 words"; the Ephrem model "opens on the famine and closes on it"; and the readability table of the corrected eight.
  - The table in `Who-Profiles/bar/README.md` (the old word counts, and the "three archaic quotes" line).
  - The refs headers name `<id>.v1.txt` files that are not in the repo.
- **R7 (NON-BLOCKING): length across the batch.** All ten now sit at 373 to 430 words, at or past the 2:30 stretch. None aims under 2:00. Each addition I checked is sourced stance and consequence, not padding. But "length follows the person" is no longer visible across the bar. Gregory of Nazianzus, Gregory of Nyssa and Ephrem have no length line in their refs. This is for the coordinator to weigh.

---

## Blind pair

TEXT X (new Athanasius) is stronger than TEXT Y (old bar Athanasius):
- X opens on its setting and names the tradition in the census's words.
- X names no modern scholar, where Y names Robertson.
- X's quotations are in modern English, where Y keeps the printed wording.
- X gives two sourced impact threads: Gregory on hypostasis and person, and Jerome on Marcella.

The judgment was made with concrete reasons before I knew which was which. No finding.

## Summary table

| Brief | Bar compared against | Craft | Rigor | Quotations | Access | Shape/length | Blocking | Verdict |
|---|---|---|---|---|---|---|---|---|
| Origen | Gregory of Tours; old Origen | pass | pass | pass | pass | pass (389) | none | CLEARS |
| Methodius | Gregory of Tours; old Methodius | pass | pass | pass | pass | pass (373) | none | CLEARS |
| Constantine | Gregory of Tours; old Constantine | pass | pass | pass | pass | pass (398) | none | CLEARS |
| Athanasius | Gregory of Tours; old Athanasius | pass | pass | pass | pass | pass (391) | none | CLEARS |
| Ephrem | Gregory of Tours; old Ephrem | pass | pass | pass (text) | pass | pass (378) | R2 (record) | CLEARS (brief); release held on R2 |
| Gregory of Nazianzus | Gregory of Tours; old Nazianzus | pass | pass | pass | pass | pass (382) | none | CLEARS |
| Gregory of Nyssa | Gregory of Tours; old Nyssa | fail (B1) | fail (B1) | pass | pass | fail (B1) | B1 | DOES NOT CLEAR |
| John Chrysostom | Gregory of Tours; old Chrysostom | pass | fail (B2) | pass | pass | pass (390) | B2 | DOES NOT CLEAR |
| Gregory of Tours | its old text; old Athanasius | pass (unchanged) | pass | pass | pass | pass (396) | none | CLEARS |
| Benedict of Nursia | its old text; old Athanasius | pass (unchanged) | pass | pass | pass | pass (430, approved) | none | CLEARS |

Batch-level blockers for release: R1 and R2.
