# R2 recheck: nine Who profiles, era 2 batch 4

Scope: only what changed, checked against `R1_review.md` and `R1_changes.md`. The text that did not change was not reviewed again. The changes were read as a word diff from `7af15851` (the drafts as R1 saw them) to `98e841eb`, limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch4/`. Every new or changed attribution, identifier and records.json entry was opened at its line in the vendored file, with XML tags stripped, to confirm who is speaking there: the ancient writer, a document he quotes, the translator, or a note. Paulinus's records witness was read in Migne's Latin (PL 48). I did not edit the drafts, and I made no paid calls, model-API calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given.

Mechanical checks, all nine:
- Each audio script equals its brief once the opening `[calmly] ` and the single `[warmly] ` are removed (checked by script). In every script `[warmly]` sits before the closing sentence only.
- `grade_text` passes for all nine (FK at most 10, Flesch at least 60). Palladius (60.3), Philostorgius (60.7) and Rufinus (61.9) sit nearest the Flesch floor.
- Brief sentences: no new or changed sentence runs past 25 words. The longest new one is Sulpicius l.3 at 24 words. Pelagius l.1 at 26 is unchanged except for the date phrase, and R1 accepted it because most of it is Pelagius's own words.
- `briefLength` matches on all nine. All nine card and records files parse as JSON.

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Rufinus of Aquileia (MAJOR) | 405 | 2:30 | 7.6 | 61.9 | 405, at the cap |
| Pelagius (MAJOR) | 405 | 2:30 | 7.2 | 65.3 | 405, at the cap |
| Paulinus of Milan | 325 | 2:00 | 6.8 | 65.9 | 325, at the cap |
| Sulpicius Severus | 324 | 2:00 | 6.7 | 69.7 | 325, within |
| Honoratus of Arles | 325 | 2:00 | 6.6 | 70.0 | 325, at the cap |
| Palladius of Helenopolis | 327 | 2:01 | 7.5 | 60.3 | 325, within "about" |
| John Cassian (MAJOR) | 404 | 2:30 | 7.7 | 64.3 | 405, within |
| Possidius of Calama | 325 | 2:00 | 6.8 | 72.0 | 325, unchanged |
| Philostorgius | 326 | 2:01 | 7.9 | 60.7 | 325, within "about" |

## 1. The 2 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| Honoratus B1 (Gibson's reasoning reversed on the card and in records) | RESOLVED | Card uncertain #3 now reads "Gibson gives 426 and January 429 without naming a source. He uses them to date Cassian's prefaces". This matches npnf211 l.15545–15566: "as Honoratus was raised to the see of Arles in 426, the volume must have been published not later than that year, or he would have been termed 'Episcopus'", and Part III "cannot be later than 428, as Honoratus died in January, 429". Gibson cites no source for either date there. The records witness says the same. |
| Palladius B1 (Jerome's "villainous slave" told as settled; Epiphanius and Jerome not placed) | RESOLVED in substance, with one framing sentence left (N2) | The brief now reports both charges, says "Jerome wrote that a Palladius", and gives the dispute: "Notes to W. H. Fremantle's edition of Jerome take both for this Palladius. The historian Tillemont, they report, thought another Palladius may be meant." This matches endnote 5139 (npnf206 l.42611–42617): "According to Epiphanius, as well as Jerome, he was tainted with Origenism. Tillemont, however, thinks that another Palladius may be referred to in these passages." Jerome's text follows the note: "Palladius, no better than a villainous slave, tried to impart energy to the same heresy" (l.42617–42618). "The same heresy" is Origen's, from the sentence before on Rufinus. Giving the notes to "Fremantle's edition" and not to Fremantle is right: his preface says Lewis and Martley "also added most of the notes" (npnf206 l.492–494). In records.json both claims are retagged Contested, and the new contested_claim quotes the note exactly ("Palladius, bishop of Hellenopolis") and Clarke's note 241, "Palladius' unfavourable opinion of Jerome was reciprocated" (Clarke l.1119). The new opening sentence still says the foes "attacked him" (N2). |

**Both are resolved.** Palladius B1 leaves one smaller framing fault, N2.

## 2. R1 minor findings

**Rufinus of Aquileia**
- M1: RESOLVED. Socrates "declares that he was not only a witness of these cruelties, but also one of the sufferers", of the monks driven "out of the oratories by force" (npnf202 l.13739–13741). The card and the records witness now say only that, and the records add "he says nothing of prison or exile".
- M2: RESOLVED. "the Recognitions of Clement of Rome" is Gennadius's own phrase (npnf203 l.42469–42470).
- M3: RESOLVED. "died there in 410, by the notes to Fremantle's edition of Jerome" matches endnote 5438, "Rufinus who died a.d. 410, in Sicily" (npnf206 l.47992–47994).
- Drafter's own fix (npnf206 notes given to "the notes to Fremantle's edition"): correct for endnotes 5438 and 2489 (l.18428, "Concordia, near Aquileia"). The scorpion identification is not wrong under the new wording. Fremantle also makes it in his own voice in his npnf203 Prolegomena: "he died soon afterwards in Sicily, as we learn from Jerome's malicious words 'The Scorpion now lies underground…'" (npnf203 l.44448–44450). That Prolegomena is his by the title page ("Translated with Prolegomena and Notes, by … Fremantle", l.43985–43997). This is an observation, not a finding. Either wording holds. The trims ("the strait", "He lived at Jerusalem") change no claim.

**Pelagius**
- M1: RESOLVED. "Late in 415, by B. B. Warfield's date". Warfield is placed in l.3, and the records witness points to the contested_claim "The date of the Synod of Diospolis".
- M2: RESOLVED. "Innocent's successor Zosimus at first declared Pelagius orthodox, in 417." Warfield: "On the arrival of Pelagius' papers, this letter was followed by another (September, 417), in which Zosimus, with the approbation of the clergy, declared both Pelagius and Cœlestius to be orthodox, and severely rebuked the Africans" (npnf105 l.918–942). The card `dates`, the keyWorks "about" and the records claim all match. "In a letter to Innocent, Pelagius pointed to his letter to Demetrias" is right. Augustine says Pelagius sent the letter "addressing it to Pope Innocent, of blessed memory, of whose death he was ignorant" (On the Grace of Christ 32, npnf105 l.11154). The quotation at ch. 40 (l.11255) is from that letter.
- M3: RESOLVED. "Jerome of Strido, to whom Augustine appealed, wrote against him too." Fremantle's Prolegomena, on Jerome's Pelagian period: "Augustin from Africa and Ctesiphon from Rome appealed to him (272, 280) … and at length Jerome himself felt compelled to take the pen" (npnf206 l.1712–1720). Fremantle composed the Prolegomena himself (l.494). The build notes are gone from the records witness. "Warfield, who edited Augustine's books in English" rests on the title page, "The translation revised, and an introduction prefixed, by Benjamin B. Warfield" (npnf105 l.514–516). The changed card uncertain #1 now runs 43 words (N4).
- The cut of the Briton sentence leaves it on card uncertain #4, unchanged. "in Warfield's English" still names him, since l.3 now places him.

**Paulinus of Milan**
- M1: RESOLVED. "a Latin writer against the Pelagians", in the brief and on the card.
- M2: RESOLVED. "At Carthage in 412, by B. B. Warfield's date". Warfield's note: "Early in 412, or, less probably, according to the Ballerini and Hefele 411" (npnf105 l.885). This is R1's own wording. The Paulinus brief does not otherwise introduce Warfield, but the Rufinus form R1 named as the model does the same.
- M3: RESOLVED. "Paulinus of Milan was taking it down" at the first mention.
- M4: RESOLVED in the drafter's form, and the drafter's correction of R1 holds. The Migne note reads "Exstat apud Baronium (Ad ann. 418. num. 7) libellus a Paulino Diacono Coelestii accusatore missus ad Zosimum, cujus ex stylo facile quisquis intelliget unum eundemque esse qui et Vitam S. Ambrosii scripserit, et Caelestium ad judicium Aurelii vocaverit" (PL 48 l.3658–3664, OCR normalized). Baronius is cited as the place where the petition is printed, and the argument from style is the note's own. The records witness says exactly this. The new tag, Dominant Modern Reconstruction, agrees with the card's "an inference … Kaniecka takes them to be one man".

**Sulpicius Severus**
- M1: RESOLVED. "says without naming a source that he gave up a name at the bar" now matches the Inferential-Thin tag. "until death, to atone" is Gennadius's own word: "kept silent until his death, in order that by penitent silence he might atone" (npnf203 l.42557–42558).

**Honoratus of Arles**
- M1: RESOLVED. "Honoratus, later bishop of Arles" at the first mention, and "Edgar Gibson, who translated John Cassian". The trim "Arles called him" brings in a pronoun problem (N3).

**John Cassian**
- M1: RESOLVED. "Gennadius of Marseilles, who wrote late in the fifth century". Gibson: "the early date at which he wrote (a.d. 495)" (npnf211 l.14965–14969).
- M2: RESOLVED. "Gennadius, who sides with Cassian, believed an unsigned attack on works 'which the church of God finds salutary' was Prosper's." Gennadius: "I regard as his also an anonymous book against certain works of Cassianus, which the church of God finds salutary" (npnf203 l.43669–43670). The quotation stays inside Gennadius's words, and the belief is his.
- M3: RESOLVED. "Its speaker is Chaeremon, an old hermit near Panephysis in the Nile delta." Gibson: Archebius, "bishop of the neighbouring town of Panephysis", met them at Thennesus "at the mouth of the Tanitic branch of the Nile" and offered "an introduction to some celebrated Anchorites in his own neighbourhood… Archebius brought them first to Chæremon, who had already passed his hundredth year" (npnf211 l.15088–15108). The Delta is Gibson's too: "their first tour was not extended beyond the Delta" (l.15241). Chaeremon is the speaker of Conference XIII (l.38029–38033, per R1).
- M4: RESOLVED. "Gibson, and William Bright whom he quotes, call this teaching Semi-Pelagian." Gibson quotes Bright: "herein consisted the error called Semi-Pelagian" (npnf211 l.15659–15676). Gibson uses the name in his own voice too (l.15626, 15941). The records contested_claim matches.
- M5: RESOLVED. "Photius of Constantinople" (Walford l.38: "Photius, who was appointed to the Patriarchal see of Constantinople"). The sentence the identifier sits in leaves out Gibson's own gloss (N5).
- The cut "Gibson says no one can tell how far they keep the fathers' own words" leaves it on card uncertain #2, unchanged.

**Palladius of Helenopolis**
- M1: RESOLVED. "Cuthbert Butler, who edited the Lausiac History" (Moore l.903–906, per R1).
- M2: RESOLVED. "Tillemont, author of the Mémoires of 1707": Fremantle's Prolegomena, "Tillemont in his painstaking Mémoires (Paris, 1707)" (npnf206 l.1958). The quotation "another Palladius may be referred to in these passages" is exact (l.42616).
- The trims: "came from Galatia, he says", the Sozomen sentence, "It tells of monks and holy women…" and "journeys of thirty days on foot" are all still on the card (knownFor, legacy traces #1). "Its prologue says" is right: the line is in the Prologue, §5 (Clarke l.187), not the Preface Butler doubts. The trim "takes this John to be" to "takes him for" brings in a pronoun problem (N1).

**Possidius of Calama**
- M1: RESOLVED. "Crispinus, the Donatist bishop of Calama" is Cunningham's heading to Letter 66 (npnf101 l.32097). The Letter 88 note it attaches to reads "Crispinus was charged with an attempt to kill Possidius the bishop of Calama" (l.36712–36714).

**Philostorgius**
- M1: RESOLVED in the shorter form. "against Porphyry of Tyre". Socrates III.23 quotes Libanius on Julian outdoing "the Tyrian", and endnote 548 reads "Porphyry. See above, I. 9." (npnf202 l.11733–11735). The Socrates volume is "Revised, with Notes, by The rev. A. C. Zenos" (l.479), so the records witness's "A. C. Zenos's note" is fair.
- M2: RESOLVED. Walford VIII.12: "not only Basil the Great, but also Apollinaris, wrote against the Apology of Eunomius; but that Eunomius replied to him in five books" (l.316). The card now leaves the referent open. "Apollinaris of Laodicea" rests on VIII.11, the chapter before, where Photius writes "Apollinaris of Laodicea" (l.314).

**README**
- README-M1: RESOLVED. The README says the ordering years are the scan's, and gives the sources' years where they differ. Its wording "by Fremantle's and Richardson's notes" names the npnf206 endnote as Fremantle's, which the batch's own rule no longer does (N6).

## 3. Not taken: judgments

| Item | Drafter's reason | Judgment |
|---|---|---|
| Philostorgius M1, "a pagan critic of the Gospels" | The cited lines do not call Porphyry a critic of the Gospels | HOLDS. Libanius says Julian attacked "those books which made the man of Palestine both God, and the Son of God" and outdid "the Tyrian" (npnf202 l.11730–11734). That makes Porphyry a critic of the Christian books, but it does not say "Gospels". The short form adds no claim. |
| Honoratus B1, the optional second accession date from Migne's note | The note is unsigned, so naming its voice would need a role | HOLDS. R1 said leaving it out is not a fault. |
| Palladius 327 and Philostorgius 326 words | Within "about 325" | HOLDS, as R1 accepted for Sulpicius at 326. |
| Paulinus M4, Baronius | Baronius is cited only as the place the petition is printed | HOLDS. See §2, Paulinus M4. |

## 4. New or changed quotations, checked word for word

All exact, with their speakers confirmed: "a Palladius, 'no better than a villainous slave,'" (Jerome, npnf206 l.42617–42618). "another Palladius may be referred to in these passages" (endnote 5139, l.42616). "Palladius, bishop of Hellenopolis" (records, the same note, l.42611–42612). "Palladius' unfavourable opinion of Jerome was reciprocated" (records, Clarke note 241, l.1119). "Early in 412" (Warfield, npnf105 l.885). "induced to interest himself in it by his increasing regard for Augustin" (records, Fremantle, npnf206 l.42449). "which the church of God finds salutary" (Gennadius, unchanged words in a reframed sentence). No quotation fails, and no witness swap was found. Every new attribution names the voice that speaks at its line: the npnf206 endnotes as the edition's notes, Fremantle for his own prolegomena, Warfield for his introduction, Gibson for his prolegomena with Bright's words given as Bright's, and Zenos for the Socrates note.

## 5. New findings in changed text

### New blocking

None.

### New minor

- **N1 (Palladius, brief l.5).** "W. K. Lowther Clarke, its translator, takes him for John Chrysostom, bishop of Constantinople." The trim from "takes this John to be" leaves "him" with Palladius as the nearest antecedent ("Illness took him… where he was made bishop"). "The blessed John" sits only inside the quotation. Read aloud, the sentence says Clarke takes Palladius for Chrysostom. Clarke's note 238 is on "the blessed John" (Clarke l.1113). Fix: "W. K. Lowther Clarke, its translator, takes this John for John Chrysostom, bishop of Constantinople." (+1 word, 328.)
- **N2 (Palladius, brief l.9).** "Foes in the quarrel over Origen of Alexandria attacked him." This frame sentence settles the identification that the same paragraph then calls disputed ("Jerome wrote that a Palladius… Tillemont… thought another Palladius may be meant"), and that records.json now tags Contested. The dispute is told two sentences later, so the listener does hear both sides. That is why this is minor and not a new blocking finding. Still, the opening should not prejudge it. Fix: "Two foes in the quarrel over Origen of Alexandria attacked a Palladius." Card uncertain #1, "Epiphanius and Jerome, who attack him", is unchanged text, but it would read better as "who attack a Palladius taken to be him".
- **N3 (Honoratus, brief l.9).** "Hilary… wept and prayed until Hilary gave way. Later, Arles called him to be its bishop." With the trim from "Arles called Honoratus", the nearest antecedent of "him" is Hilary. Hilary did later become bishop of Arles, so the misreading is plausible and wrong at this point in the story. Fix: "Later, Arles called Honoratus to be its bishop." (Same word count, 325.)
- **N4 (Pelagius, card uncertain #1, `pelagius.card.json` l.36).** The changed sentence now runs 43 words: "Apart from his letter to Demetrias and his answers at Diospolis, his story comes through Augustine of Hippo, through Jerome of Strido, to whom Augustine appealed and who wrote against him too, and through modern editors…". Fix: "Apart from his letter to Demetrias and his answers at Diospolis, his story comes through his opponents. Augustine of Hippo wrote against him, and so did Jerome of Strido, to whom Augustine appealed. Modern editors such as B. B. Warfield take Augustine's side." (Fremantle, npnf206 l.1712–1720; Warfield as already placed.)
- **N5 (John Cassian, card uncertain #1, `john-cassian.card.json` l.40).** The M5 sentence, "Gibson adds that Photius of Constantinople calls him a Roman," sits in a birthplace item, and it drops Gibson's own gloss: Photius "calls him ῾Ρωμαῖος, which need mean no more than born within the Roman Empire" (npnf211 l.14992–14995). Without the gloss, Photius reads as a witness for a Roman birth, which Gibson says it need not be. Fix: "Gibson adds that Photius of Constantinople calls him a Roman, which, Gibson says, 'need mean no more than born within the Roman Empire'."
- **N6 (batch `README.md`).** The new README sentence gives Rufinus's 410 "by Fremantle's and Richardson's notes". The 410 is in endnote 5438 of the npnf206 edition, whose notes Fremantle says were mostly added by Lewis and Martley (l.492–494). Fremantle's own Prolegomena says only that Rufinus "died soon afterwards in Sicily" (npnf203 l.44449). The README is internal, but it should follow the batch's own rule. Fix: "Rufinus died in 410 by the notes to Fremantle's edition of Jerome and by Richardson's note".

No other new defect was found in the changed text. The new or changed records.json entries match their briefs and cards.

## Summary

| Profile | Words | Time @162 | FK | Flesch | R1 blocking resolved | New blocking | New minor |
|---|---|---|---|---|---|---|---|
| Rufinus of Aquileia (MAJOR) | 405 | 2:30 | 7.6 | 61.9 | – (0) | 0 | 0 |
| Pelagius (MAJOR) | 405 | 2:30 | 7.2 | 65.3 | – (0) | 0 | 1 (N4) |
| Paulinus of Milan | 325 | 2:00 | 6.8 | 65.9 | – (0) | 0 | 0 |
| Sulpicius Severus | 324 | 2:00 | 6.7 | 69.7 | – (0) | 0 | 0 |
| Honoratus of Arles | 325 | 2:00 | 6.6 | 70.0 | 1 of 1 | 0 | 1 (N3) |
| Palladius of Helenopolis | 327 | 2:01 | 7.5 | 60.3 | 1 of 1 | 0 | 2 (N1, N2) |
| John Cassian (MAJOR) | 404 | 2:30 | 7.7 | 64.3 | – (0) | 0 | 1 (N5) |
| Possidius of Calama | 325 | 2:00 | 6.8 | 72.0 | – (0) | 0 | 0 |
| Philostorgius | 326 | 2:01 | 7.9 | 60.7 | – (0) | 0 | 0 |
| README | | | | | | 0 | 1 (N6) |
| **Total** | | | | | **2 of 2** | **0** | **6 (N1 to N6)** |

Both R1 blocking findings and all 23 R1 minor findings are resolved, or taken in another form that holds. Every not-taken reason holds against its source. No witness swap and no new wrong attribution was found. The changes brought in no new blocking finding. They brought in six minor ones: two pronouns left loose by trims (N1, N3), one framing sentence that prejudges the Palladius identification (N2), one long card sentence (N4), one dropped qualifier (N5), and one README attribution (N6). Each fix is a one-sentence edit that needs no round 3 review. A targeted look at N2 alone would be enough if one is wanted.
