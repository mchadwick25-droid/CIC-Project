# Card check: The Post-Apostolic House Churches

Checker: did not write the card. Read: `CLAUDE.md` (Trust and source fidelity), Kit Part 1, `kinds/tradition.md`, the card role, the final brief (`post-apostolic-house-church.brief.txt`, after `Grade_Fixes_Applied.md` and `Grade2_Fixes_Applied.md`), `Outline.md`, `Source_Sheet.md`, `Review.md`, `Fresh_Read.md`, `Card.existing.json`, `post-apostolic-house-church.card.json`, `Card_Edits.md`, `Entry_Texts.md`. Every line cited below was re-opened in `cic/texts/`.

## Verdict: FIX

Fourteen changes, below. Everything not listed passes.

## What passes

- **Nothing else moved (check 2).** A field-by-field diff of `Card.existing.json` against the card: the only changes are `why`, `voices[1]`, `voices[6]`, the `legacy` paragraph added at the end, `file` on each source, the added text in `sources[1]`, `[2]`, `[4]`, `[5]`, `[7]`, `[8]`, six new sources, and the new `uncertain` and `quotationOriginals`. Each is listed in `Card_Edits.md`. `people` is word for word.
- **Edits 1 to 12 in `Card_Edits.md` (check 1).** Each stands on its cited lines, re-read: anf01 2395-2398, 1916-1943, 3232-3235, 3403-3405, 3531-3562, 3608-3618, 5851-5856, 8272-8289, 8503-8508, 8854-8869, 16232-16240, 16414 (the kiss; `Card_Edits.md` says 16413), 16448-16452, 16518-16526, 39823-39853; anf07 12524, 12585, 12706-12738, 12827, 12910-12920 (footnote "Probably running water"), 12960-12970, 13087-13095, 13112-13116; anf02 1005-1026, 4946-4952; mirbt 2789-2797; npnf201 16634-16636, 16679-16684, 25082-25117, 31136-31140, 31415-31434, 31527-31553, 31659-31666; npnf204 68815-68823; jerome-chron 42193-42262. Every Cut first item marked for the card is on it. Nothing in `Review.md` or `Fresh_Read.md` sends anything else. "Bithynia" and "deaconesses" are gone, as the Do not say and the fresh read require. Except as in fixes 4 and 5, no modern date, identification or opinion is stated as content.
- **Quotations (checks 4, 5).** The brief quotes three spans, and the card has one entry for each. All three run six words or more, so none carries `secondReading` and none is "checked at card". Each `printed` and `englishPrinted` stands at its file and lines: Pliny, mirbt 2790-2791 and npnf201 19492-19494; Justin, 1apol-grc 1759-1762 and anf01 16502-16505 (with its endnote stripped); the Didache, anf07 12700-12706 (with its footnotes stripped). All four renderings were checked clause by clause against their originals and hold, nothing added. **Pliny's damaged scan:** mirbt 2790 reads "sohti". The second held print, the editor's endnote at anf05 60209-60211, reads "Soliti essent Christiani, stato die, ante lucem convenire, carmenque Christo, quasi Deo, dicere secum invicem". That confirms the reading, so the Latin may print, as the role allows, with the misreading named in its `uncertain`. **The Greek was checked by hand:** every letter matches the file, but the accents are stored as different code points (fix 7).
- **The validator.** The full run was killed for memory (V8 out of memory) on a scratch copy of the census, with the card's fields merged into the entry, the brief as `longDescription`, the four new entry texts and the proposed `modernWorks`. Run with `--skip-quotes` instead: 629 movements, 736 edges, 10 eras, 0 errors, 4 warnings, all short names on other entries. The quotation spans were checked by hand, as above, along with every quoted span in the card's prose (`legacy`, the `sources` notes, `uncertain`). Each is at a cited line. The real census was not edited.
- **Entry texts.** `tile`, `intro`, `recordHolds` and the rest of `summary` hold against the final brief, the outline (the heart, Setting, Do not say) and the sheet. They add no claim the brief does not hold. The scores were re-run: tile grade 7.9, ease 69.6; intro 7.6, 64.1; summary 7.8, 73.2; recordHolds 6.9, 71.0; craft check 0 on each. The representative (Chloe, as in `cic-website/data/worlds/post-apostolic-house-church.json`) and the intro frame ("… is a representative voice for the Christian tradition of …") are kept.

## Household by household, and "met in their homes"

- **What the brief and heart claim.** The brief and the heart do not say that Christians met household by household, or met in homes. The essence says they "met together, and their letters greet one another household by household". The heart's "small gatherings" was corrected to "met together" (Outline, Correction to the heart's wording), and the Do not say reads "Do not say where they met".
- **What the sheet and sources hold for the greetings.** Two passages in Ignatius, both held, both Documented (Source_Sheet I4, I5):
  - anf01 8503-8508: "I salute the families of my brethren, with their wives and children … I salute the house of Tavias".
  - anf01 8868-8869: "the wife of Epitropus, with all her house and children".

  No other held letter in the story (Rome's, Polycarp's) greets a household. The brief's "their letters" therefore stands on Ignatius's letters alone. It is true as worded, but it is thinner than it sounds.
- **What the sources hold on where they met:**
  - Justin, 1apol-grc 1759-1760: "all … gather in one place", with no building named.
  - The Acts of Justin (later and anonymous; Outline, Leave out), anf01 29302-29312. Asked "Where do you assemble?", Justin answers "Where each one chooses and can" and denies that they all meet in one place. His own meeting is where he lodges, "above one Martinus, at the Timiotinian Bath".
  - Hermas, anf02 4946-4952: bishops "received into their houses the servants of God". This is hospitality, not a meeting.
  - Pliny gives no place.
- **voices[5] ("The gatherings met in their homes, but no record says whose").** The not-found listing is right. No held line says the gatherings met in members' homes, and none contradicts it, so under the role it stays and is listed. Two things for release and Mark:
  - It goes against the outline's Do not say ("Do not say where they met").
  - "but no record says whose" is a sentence of the kind Kit Part 1 bars: it only says what is missing.

  Out of scope here: the entry's `topics` ("Communion: Households gave thanks over bread and cup …"; "Sin and forgiveness: One community's manual …"; "Church leaders: Some places had one bishop, others a group of elders") repeat wording the outline's Do not say bars. They were not rebuilt in this batch.

## The not-found list

The list in `Card_Edits.md` is right in what it lists, with three corrections:

- **"around 155" (voices[2], sources[3]) is not merely not found. A held source contradicts it.** Jerome's Chronicle sets Polycarp's martyrdom after Lucius Caesar's Parthian triumph, under Marcus Aurelius ("Persecutione orta in Asia Polycarpus et Pionius fecere martyrium", jerome-chron 42977-42979). The live polycarp-of-smyrna card says the same, and calls 155-156 McGiffert's reckoning. See fix 4.
- **sourcing's "no enslaved member … speaks to us in words of their own" is contradicted.** It was not listed. Hermas, a member at Rome (on this card's `people`), opens his own book: "He who had brought me up, sold me to one Rhode in Rome" (anf02 649). See fix 3.
- **Not found but not listed, to add (each left in place):**
  - legacy: "the basic rhythm of Christian worship shows up earliest here" (a judgment).
  - legacy: "either in a full common meal or as the bread and wine alone". No held line sets these as two forms. Pliny's later common meal (mirbt 2793-2794) and Ignatius's love-feast (anf01 8286-8287) are the nearest.
  - floorNote: "What they confessed is part of the raw material the creed was later drawn from, not a departure from it" (a judgment, and a "not X but Y" turn).
  - sourcing: "Individual, first-person voice stays thin throughout". This is a judgment. Ignatius, Polycarp, Hermas and Justin all write in the first person.

The rest stand as listed. "c. 107-117" (voices[0], sources[0]) is not contradicted: Jerome sets Ignatius's journey to the beasts in Trajan's eleventh year (jerome-chron 42194-42200). "c. 165" for Justin agrees with the live justin-martyr card.

## FIX

**1. `quotationOriginals[1].work`, and `sources[10].work` (the CC BY-SA attribution).** The Greek file's header says "Attribution and share-alike travel with any quotation" (CC BY-SA 4.0, Trustees of Tufts University, Perseus Project). The card names only Rauschen, so it does not carry the attribution. `Card_Edits.md` leaves it to release, but the card is what gets published. The Evagrius card sets the precedent: the licence is named in the title of the work (Decision-Log 2026-11-22, "CC BY 4.0, credited on the card").
- `quotationOriginals[1].work`
  - Old: "Justin Martyr, First Apology 67.3 (Greek, ed. Gerhard Rauschen, 1911)"
  - New: "Justin Martyr, First Apology 67.3 (Greek, ed. Gerhard Rauschen, 1911; digital edition by the Perseus Project, Trustees of Tufts University, CC BY-SA 4.0)"
- `sources[10].work`
  - Old: "Justin Martyr, First Apology, in Greek (ed. Gerhard Rauschen)"
  - New: "Justin Martyr, First Apology, in Greek (ed. Gerhard Rauschen; digital edition by the Perseus Project, Trustees of Tufts University, CC BY-SA 4.0)"
- **For Mark (not this check's call).** On 2026-11-12 he ruled that the CC BY-SA Lactantius quotes on the Tertullian link be replaced with the public-domain print (Decision-Log 2026-11-13, data release 40). The Library log of 2026-10-28 skips share-alike texts. No public-domain print of this Greek is held: Goodspeed 1914's OCR holds no Greek, and the Otto 1879 file holds the doubtful works only. So the choice is his:
  - (a) print the Greek with the attribution above (recommended, since it is one sentence and is credited);
  - (b) print the English alone until a public-domain scan of Rauschen 1911 is vendored.

  The live `justin-martyr` card quotes the same file with no attribution (λόγον ὄντα, line 1231). That is another thread's matter, flagged here.

**2. `sources`: add the second print that Quote 1's Latin rests on.** `quotationOriginals[0].uncertain` cites "an editor's note in Ante-Nicene Fathers 5", and the decision to print the Latin depends on it. Every cited file must be in `sources`. Add after the last item:
```json
{
 "work": "Pliny the Younger, Letters 10.96.7, the clause on the dawn hymn, in an editor's note (Ante-Nicene Fathers, volume 5)",
 "type": "primary",
 "file": "cic/texts/anf05_hippolytus-cyprian-caius-novatian.xml",
 "note": "An editor's note prints in Latin the clause of Pliny's letter on the Christians' dawn hymn, reading soliti."
}
```

**3. `sourcing` (contradicted by Hermas, anf02 649).**
- Old: "no woman, no enslaved member, and no non-literate believer — the majority of this movement — speaks to us in words of their own."
- New: "no woman and no non-literate believer — the majority of this movement — speaks to us in words of their own."

**4. `voices[2]` and `sources[3].note` (contradicted by jerome-chron 42977-42979).**
- `voices[2]`
  - Old: "He was put to death at Smyrna around 155; his own congregation recorded his death."
  - New: "He was put to death at Smyrna; his own congregation recorded his death."
- `sources[3].note`
  - Old: "recounting Polycarp's death around 155, written partly"
  - New: "recounting Polycarp's death, written partly"

**5. `voices[6]` (whose word ministrae is).** Pliny writes "ex duabus ancillis, quae ministrae dicebantur" (mirbt 2795-2796), "who were called ministrae". The card makes it his own word for an office. The outline's Do not say holds to "who were called".
- Old: "are named only by their Roman interrogator's own word for their office — never by their own names."
- New: "are named in their Roman interrogator's letter only by what they were called — never by their own names."

**6. `sources[2].note`, the Didache (contradicted by anf07 13022-13027).** The manual says "every prophet that speaketh in the Spirit ye shall neither try nor judge". The three days and the money test are given for the apostle (anf07 13018-13022).
- Old: "and test the traveling apostles and prophets who come to them: one who stays three days, or asks for money, is a false prophet."
- New: "and tells them how to receive the traveling apostles and prophets who come to them: an apostle who stays three days, or asks for money, is a false prophet."

**7. `quotationOriginals[1].printed` (verbatim, at the code-point level).** The card's Greek writes its accents as tonos (U+03AC, U+03AD, U+03AF, U+03CC, U+03CD, U+03CE). The file writes them as oxia (U+1F71, U+1F73, U+1F77, U+1F79, U+1F7B, U+1F7D), at 13 places. The two forms are canonically equal (NFC), and the validator's fold passes either. But a plain search of the file does not find the card's string. Copy the file's own characters from lines 1759-1762:
- Old (tonos): "Καὶ τῇ τοῦ ἡλίου λεγομένῃ ἡμέρᾳ πάντων κατὰ πόλεις ἢ ἀγροὺς μενόντων ἐπὶ τὸ αὐτὸ συνέλευσις γίνεται, καὶ τὰ ἀπομνημονεύματα τῶν ἀποστόλων ἢ τὰ συγγράμματα τῶν προφητῶν ἀναγινώσκεται, μέχρις ἐγχωρεῖ."
- New (as in the file): "Καὶ τῇ τοῦ ἡλίου λεγομένῃ ἡμέρᾳ πάντων κατὰ πόλεις ἢ ἀγροὺς μενόντων ἐπὶ τὸ αὐτὸ συνέλευσις γίνεται, καὶ τὰ ἀπομνημονεύματα τῶν ἀποστόλων ἢ τὰ συγγράμματα τῶν προφητῶν ἀναγινώσκεται, μέχρις ἐγχωρεῖ."

**8. `uncertain[1]` (contradicted by 1apol-grc 1759-1760).** Justin gives his Sunday as that of "all who live in the towns or in the country", and Ignatius states his rule for every church (anf01 8278-8282).
- Old: "The thanksgiving. The witnesses differ, and none of them says his custom was everyone's."
- New: "The thanksgiving. The witnesses describe it differently."

**9. `uncertain[2]` (contradicted by anf01 39833-39836, Source_Sheet S3).** Irenaeus places the letter in Clement's time, sent by "the Church in Rome", and does not say Clement wrote it. Eusebius does: "He wrote it in the name of the church of Rome", npnf201 16679-16680.
- Old: "and Irenaeus and Eusebius say the same."
- New: "Irenaeus places the letter in Clement's time, and Eusebius says Clement wrote it in the church's name."

**10. Entry field `modernWorks` (the role: each modern work the outline used to clarify an old text goes there).** `Card_Edits.md` leaves out ANF 3, ANF 5 and ANF 9 "since nothing on the card rests on them alone". That is not the role's test. The outline uses ANF 3 for Tertullian's "ruler of a province" (Setting), ANF 5 for the Latin Quote 1 prints, and ANF 9 for 1 Clement (Beat 2). Add, in year order among the others:
```json
{"title": "Latin Christianity: Its Founder, Tertullian (Ante-Nicene Fathers, volume 3)", "author": "Alexander Roberts and James Donaldson (ed.)", "year": "1885", "note": "English translation of Tertullian's works, among them his Apology."},
{"title": "Fathers of the Third Century: Hippolytus, Cyprian, Caius, Novatian, Appendix (Ante-Nicene Fathers, volume 5)", "author": "Alexander Roberts and James Donaldson (ed.)", "year": "1886", "note": "English translations of third-century writers, with editors' notes, one of which prints in Latin the clause of Pliny's letter on the Christians' dawn hymn."},
{"title": "The Gospel of Peter, The Diatessaron of Tatian, … The Epistles of Clement (complete text), … (Ante-Nicene Fathers, volume 9)", "author": "Allan Menzies (ed.)", "year": "1896", "note": "English translation of the complete text of Rome's letter to Corinth, from the manuscript found in 1873."}
```
In the Rauschen entry's `note`:
- Old: "The Greek text of Justin's two Apologies."
- New: "The Greek text of Justin's two Apologies, held in the Perseus Project's digital edition (Trustees of Tufts University) under CC BY-SA 4.0."

**11. Entry field `entry.tile` (the manual is one witness).** The brief gives the Two Ways as what "a short manual, whose writer, date and place no one knows" teaches, and the outline's Do not say keeps the manual's practice to "this one manual". The tile gives it as everyone's.
- Old: "Newcomers learned the Two Ways, of life and of death, before baptism."
- New: "A short manual taught newcomers the Two Ways, of life and of death, before baptism."
- Rescored: 192 words, grade 7.9, ease 70.0, pass; craft 0.

**12. Entry field `entry.summary` (Kit Part 1, Explain it or leave it out).** The summary names two letters and says what neither said.
- Old: "Rome wrote to Corinth when the church there removed some of its elders, and Ignatius of Antioch wrote to the churches of Asia as a prisoner."
- New: "When the church at Corinth removed some of its elders, Rome wrote in their defense. Ignatius of Antioch, a prisoner, urged the churches of Asia to act as one around their bishops."
- Evidence, from the brief: "Men appointed with the whole church's consent, who served blamelessly, could not justly be removed"; "Each church, he urged, should act as one around its bishop".
- Rescored: 87 words, grade 7.3, ease 71.3, pass; craft 0.

**13. `Card_Edits.md`, Not found: add the four items above, and move "around 155" and "no enslaved member" to the corrections (fixes 3, 4).** This is a change to the record only; nothing on the card moves for it.

**14. `Card_Edits.md`, edit 9 evidence: "16413" → "16414"** (the kiss, anf01 16414). This is a change to the record only.

Edited nothing else; nothing committed.
