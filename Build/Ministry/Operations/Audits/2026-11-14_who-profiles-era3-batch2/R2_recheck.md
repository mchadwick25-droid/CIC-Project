# R2 recheck: era 3 batch 2

Scope: only what changed, checked against `R1_review.md` and `R1_changes.md`. Text that did not change was not reviewed again. I read the changes as a word diff from `c99df43f` (the version R1 reviewed) to `05d852ff` (HEAD), limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch2/`. I opened every new or changed sentence, quotation, identifier and `records.json` entry at its line in the vendored file. I checked who is speaking at each line: the ancient writer, a document he quotes, the translator, or an editor's note or apparatus. The OCR files (Wright's Joshua, Nau PO 8, Brooks PO 17, Chabot's Michael t.1, Hamilton and Brooks, Kugener, Brooks's Select Letters, Bar Hebraeus, Migne PL 67, 72 and 83, Krusch) were read by line and searched tolerantly. I did not edit the drafts, and I made no paid calls, model-API calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5, 7, 9, 11 and 13.

Mechanical checks, all ten:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`. No tag appears in a brief or card. The Severus tag has moved (N5).
- `grade_text` passes for all ten (FK at most 10, Flesch at least 60). Ferrandus (61.5) and Severus (62.1) sit nearest the floor.
- Sentences: no new or changed narrator sentence runs past about 25 words. The longest new ones are Ferrandus l.5, "A short book on church writers, printed with Isidore of Seville's works, says the Romans asked whether a man may be condemned after death." (24), and Severus l.1, "Evagrius seems to give 519, Brooks notes, but Severus's sermons, kept in date order, decide it." (16).
- `briefLength` matches on all ten: "about 2 minutes 30 seconds" on Severus, Caesarius and Benedict, "about 2 minutes 20 seconds" on Julian (378 words, 2:20), "about 2 minutes" on the rest. All ten cards and `records.json` parse as JSON, and `records.json` has exactly the ten ids. Every `file` named in a card's sources exists under `cic/texts/`, including the four new ones (Nau PO 8, Brooks PO 17, Chabot's Michael t.1 on Joshua; Bar Hebraeus on Julian; Arevalo's Isidore on Ferrandus).

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Joshua the Stylite | 325 | 2:00 | 5.9 | 76.7 | within "about" 324 |
| John Rufus | 321 | 1:59 | 8.2 | 64.8 | within |
| Brigid of Kildare | 322 | 1:59 | 6.6 | 70.9 | within |
| Zachariah Rhetor | 324 | 2:00 | 7.8 | 63.2 | within |
| Severus of Antioch (MAJOR) | 404 | 2:30 | 7.8 | 62.1 | 405, within |
| Caesaria of Arles the Elder | 316 | 1:57 | 6.5 | 73.0 | within |
| Caesarius of Arles (MAJOR) | 403 | 2:29 | 6.7 | 73.7 | 405, within |
| Julian, missionary to the Nobadae (MAJOR) | 378 | 2:20 | 7.2 | 68.6 | 405, within |
| Ferrandus of Carthage | 321 | 1:59 | 8.3 | 61.5 | within |
| Benedict of Nursia (MAJOR) | 405 | 2:30 | 7.0 | 71.2 | 405, at the cap |

## 1. The 5 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| Joshua B1 (Wright's Dionysius of Tell-Mahre told as settled) | RESOLVED | Brief l.11: "It survived inside a later Syriac chronicle. Wright took its compiler for the patriarch Dionysius of Tell-Mahre. The French scholar François Nau calls him the Pseudo-Dionysius, writing in 775." Wright: "a later historian, Dionysius of Tell-Mahré, patriarch of the Jacobites (ob. A. Gr. 1156, A.D. 845)… The solitary manuscript… is preserved in the Vatican Library" (l.292–297), "no. CLXII" (l.305–306). Nau, in his introduction to the Didascalia of Jacob (signed "F. Nau", po08 l.47741–47747): "le Pseudo-Denys écrivait en l'année 1086 des Grecs (775 de notre ère)", then "Pseudo-Denys, Vatican, ms. syr. 162" (l.48221–48226). Brooks: "the so-called Dionysius" (po17 l.714). Chabot: "la chronique authentique de Denys de Tell-Mahré… Cet ouvrage est perdu, à l'exception d'un seul chapitre" (t.1 l.63094–63099). Card `legacy.traces` 1, `uncertain` 4 ("the compiler he calls Dionysius of Tell-Mahre") and the new `uncertain` 5 give both sides, each to its owner. Records: the Wright claim is Contested and marked as his 1882 attribution, the Nau claim is Dominant Modern Reconstruction, and the new `contested_claim` holds all four witnesses. One source title is wrong (N2). |
| Brigid B1 (the Life not said plainly to be written long after her) | RESOLVED | Brief l.3: "He wrote her Life in Latin long after her death, at the brothers' request, from what he says elders had handed down. It is hagiography, and mostly miracles." Brief l.9 opens "How long after her Cogitosus wrote is disputed." Card `uncertain` 1: "written long after her death. It is hagiography and mostly miracles." Cogitosus: "pauca de pluribus, a majoribus et peritissimis tradita" (PL 72 l.58494–58496). Basnage: "probatque non coaevum, sed recentiorem fuisse Cogitosum, qui Brigidae viventis virtutes a majoribus tantum inaudiverat" (l.58468–58472, OCR run together) and "Vita Brigidae quam descripsit tota miraculis scatet" (l.58442–58446, across columns). The new records claims (Widely Accepted for "long after"; Documented for "tota miraculis scatet") and the renamed contested claim, with Stokes's 800–835 added, match. R1's l.9 wording was not taken word for word (no "places Muirchu in the 690s"), but the brief now says plainly what the coordinator asked, and the card keeps White's dates. |
| Caesaria B2 (false absence: "All that is known of her") | RESOLVED | Brief l.3: "Her story comes almost wholly from her brother's Life." Card `uncertain` 1 adds "Bruno Krusch adds that Venantius Fortunatus held her up as an example." Krusch: "neque vero Casaria ipsius artem effugit pia soror, quam non semel proposuit exemplum imitandum" (l.35667–35668). The records `absent_details` say nothing that makes the Life the only witness. The new Fortunatus records claim duplicates an old one under a second tag (N6). |
| Julian B1 ("he" after Payne Smith) | RESOLVED | Brief l.5: "notes that John belonged to the party that refused Chalcedon". Payne Smith says it of John (preface l.286–290, as R1 read it). |
| Ferrandus B2 (the book on church writers told as anonymous) | RESOLVED | Brief l.5: "A short book on church writers, printed with Isidore of Seville's works, says…". Card `legacy.traces` 1: "Gallandi calls its author unknown; Baronius, as Gallandi reports, and Faustino Arevalo, Isidore's editor, give it to Isidore." Gallandi: "incertus auctor libelli de xii Scriptoribus ecclesiasticis, qui Isidoro Hispalensi et Ildefonso Toletano subjici solet" (pl67 l.68266–68268) and "Vidit hunc anonymi locum Baronius, quam Isidoro Hispalensi ascribit" (l.68296–68297). Arevalo: "CAPUT XI. Ferrandus, Carthaginiensis Ecclesiae diaconus" (pl83 l.121204–121205), "Hactenus Isidorus" after chapter XLVI (l.120535–120536), and Miraeus's doubt about the twelve chapters (l.120512–120515). The new source entry ("Isidore of Seville, or an unknown author"), the records witness and the new `contested_claim` match. |

## 2. R1 minor findings

**Joshua the Stylite**
- M1: RESOLVED. Brief "a priest and abbot near Edessa"; card `keyWorks` "abbot of a convent near Edessa". Wright: "one Sergius, the abbot of a convent in the district of Edessa" (l.337–338).
- M2: RESOLVED in card `dates` ("that winter and the early part of the next year"; Wright "that winter and the earlier part of the following year", l.342). The brief's "in the months after" is right on the facts, but the R1 wording it carries opens with an unclear "He" (N1).
- M3: RESOLVED. "Wright says the Chronicle is generally counted among the most valuable sources for its time." ("generally acknowledged", l.172.)
- M4: RESOLVED. "the Romans" in the brief and `keyWorks`; Wright's note: "literally, the Romans" (l.448). The records keep Wright's "Greeks" as his English, which is right.
- M5: RESOLVED. Two sentences, 11 and 23 words.
- Length: RESOLVED. 325 words. The cuts leave no dangling reference. The quote now ends at "from the convent of Züknin." (Wright l.388–390), a clean cut inside the copyist's note. "He promises to send on whatever else is worth recording, 'if I remain alive'" tells Joshua's "whatever happens in the times that are coming and is worthy of record, I will write it down and send it to thee… if I remain alive" (l.4404–4406) fairly.

**John Rufus**
- M6: RESOLVED. "Zachariah Rhetor" in brief l.5, card `remembered` 2, `uncertain` 1, the Kugener source's author and the records witness. No "Zachariah of Mitylene" is left in the batch outside the Zachariah texts, where it is Brooks's identification, and the Severus card's source title, which is the book's own.
- M7: RESOLVED. "the monastery of Juvenal, bishop of Jerusalem." Nau: "il y demeurait en paix quand il arriva à l'épiscopat" (po08 l.2134). "John answered that Juvenal had been the companion of Judas" follows cleanly.
- M8: RESOLVED. 321 words. "Its German editor, Richard Raabe, asks whether the author of the Plerophories wrote it too, and leaves the question open." (Raabe l.609–610, as R1 read it.)
- M9: RESOLVED. The succession claim is Dominant Modern Reconstruction, witness "Nau's introduction (po08 l.372-376), an editor's inference"; the heading claim stays Documented.

**Brigid of Kildare**
- M1: RESOLVED. Brief l.1 "In her great church on the plains of the Liffey"; l.13 "crowds came to her church"; card `traces` 1 and 2. Cogitosus: "in campestribus campi Liffei" (l.58512–58513). The new records claim gives "Kildare" to White (l.3748–3749) and the Lismore Life (l.18604).
- M2: RESOLVED in brief, card `uncertain` 2 and the Basnage records claim ("in ejus templo operari solita", l.58466).
- M3: RESOLVED. "the year Saint Columcille was born" (Annales Cambriae l.2399); "put four years between his birth and her death" keeps the Nennius extracts' "Columbae" as the same man without a second name.
- M4: RESOLVED in card `uncertain` 2 and the records' contested claim (Stokes's index, l.21226).
- M5: RESOLVED. "one heart and one counsel".
- M6: RESOLVED. "reports her birth as 439 and gives her death as 518".

**Zachariah Rhetor**
- M10: RESOLVED on the point R1 raised: both sides are in the brief. The wording "the chronicle's first editor" is not quite right (N3).
- M11: RESOLVED. The missing signature is gone from the brief, and card `uncertain` 2 adds "he may possibly have been a nominee of Anthimus, Brooks says" (note 4, l.385–386). The new brief wording, "to become bishop", reads as a motive (N4).
- M12: RESOLVED. Card `uncertain` 1 and the records add Bar Salibi's "Zachariah the Rhetor and bishop of Melitene" (l.260–262), "an error for 'Mitylene'" (l.357–358).
- M13: RESOLVED. "By Brooks's identification he died or lost his see between 536 and 553." Brooks: "died or was deposed between 536 and 553" (l.366–367).

**Severus of Antioch**
- M14: RESOLVED. "He fled, and E. W. Brooks… dates the flight to 29 September 518. Evagrius seems to give 519, Brooks notes, but Severus's sermons, kept in date order, decide it." Brooks: "on Sept. 29 fled from Antioch" (l.200) and "Evagr. (iv. 3) seems to place his flight in 519… the homilies… which are arranged chronologically, and end with Lent 518, are decisive" (l.213–217). The 519 is Brooks's reading, and the sentence gives it to him.
- M15: RESOLVED. "Zachariah says he was baptized…"; "Evagrius tells this from a Life of Severus, which Brooks takes for Zachariah's." Evagrius: "as is narrated by the author of the life of Severus" (l.7013–7014); Brooks's note "Used by Evagrius" (l.97). The records witness now says Evagrius is not a second witness.
- M16: RESOLVED. Two sentences.
- Length: RESOLVED. 404 words. The cut letter sentence stays in the card and records. The `[warmly]` tag moved at the same time (N5).

**Caesaria of Arles the Elder**
- M7: RESOLVED in the brief: "until they died" ("usque diem transitus earum", l.37217). The records claim on the same passage still reads "until the day of her death" (N7).
- M8: RESOLVED. "Caesarius wrote a Rule for them." 316 words.
- M9: RESOLVED. "held up Casaria, Caesarius's pious sister, as an example to follow", with no quotation marks.

**Caesarius of Arles**
- M10: RESOLVED. "Caesarius signed first at a council in Orange".
- M11: RESOLVED. "what he often said of clergy" (l.37137–37140).

**Julian, missionary to the Nobadae**
- M1: RESOLVED. "John says Julian longed… Justinian disliked it, John writes, because Julian opposed the Council of Chalcedon. So the emperor told bishops…". Each pronoun now has one reading.
- M2: RESOLVED. The repeated close is gone; `[warmly]` sits before "John calls Julian 'their teacher.'" `briefLength` is now "about 2 minutes 20 seconds".
- M3: RESOLVED. Card `uncertain` 1 and 3, the new source entry and the records note. Bar Hebraeus: "presbyter quidam orthodoxus, nomine Julianus, Constantinopoli ministerio addictus papae Theodosii Alexandrini" (l.14056–14059) and the empress's letter to the duke of the Thebaid (l.14159–14168). "from the thirteenth century" follows the file header (1226–1286).

**Ferrandus of Carthage**
- M4: RESOLVED. "in the year Theodor Mommsen, its editor, gives as 546".
- M5: RESOLVED. "Its author says that he himself became a monk…".
- M6: RESOLVED. Two sentences.
- Length: RESOLVED. 321 words. "He made a short digest of church laws as well." left the brief; `keyWorks` keeps the Breviatio.

**Benedict of Nursia**
- M7: RESOLVED. "Gardner gives his birth as about 480, and the editor Francis Gasquet as 480." Card `dates` matches. Gardner l.12628; Gasquet l.172–173.
- M8: RESOLVED. "Saint John the Baptist" (Gregory, "the oratory of St. John Baptist", l.5612–5613). "on a high mountain," left the brief to hold the cap, and nothing hangs on it.

**README**
- M9: RESOLVED. "Simeon of Beth Arsham (about 530) falls in the same years and is skipped as a live person entry." Its sentence that the Brigid brief marks the Life as written long after her is now true.

## 3. New findings

- **N1 MINOR (`joshua-the-stylite.brief.txt` l.7, audio; item 4; a pronoun that can be heard as Joshua, carried by R1's own fix wording).** "Joshua counts his years in the old Greek era, and Wright adds our own years. By Wright's reckoning the last date in the book is 28 November 506. He and the German scholar Theodor Noeldeke place the writing in the months after." Wright appears only as a possessive in the sentence before. Joshua is the paragraph's subject, so a listener can hear "He" as Joshua placing his own writing. The placing is Wright's: "I have thought myself justifed in assigning the composition of the work to that winter and the earlier part of the following year, which is also Noeldeke's opinion" (l.339–344). Fix, brief and audio: "Wright and the German scholar Theodor Noeldeke place the writing in the months after." Scored: 325 words (2:00), FK 5.9, Flesch 76.7.

- **N2 MINOR (`joshua-the-stylite.card.json` `sources.about`; item 1; a source misnamed).** The new entry is titled "Introduction to the Chronicle of Michael the Syrian", author J.-B. Chabot. The cited passage (t.1 l.63094–63099) is not Chabot's Introduction. The file's own notice says the Introduction "ne pourra être livrée qu'à la fin de la publication" (l.62759–62760). The passage sits in "La Chronique de Michel le Syrien. Note de M. l'abbé J.-B. Chabot. Extrait des comptes rendus de l'Académie des Inscriptions et Belles-Lettres" (l.62857–62869), bound into the volume. (R1's B1 called it "Chabot, introducing Michael the Syrian", and the drafter took the title from there.) Fix: title "Note on the Chronicle of Michael the Syrian (Comptes rendus of the Académie des Inscriptions), bound with tome 1".

- **N3 MINOR (`zachariah-rhetor.brief.txt` l.7, audio, card `uncertain` 4, records witness and contested claim; item 1; "first editor" against a held line, carried by R1's own fix wording).** "Land, the chronicle's first editor, gives him book seven as well." Kugener says only that the chronicle "a été éditée en 1870 par Land" (l.17146–17149). Brooks, in the file the brief cites, says that extracts from "the same work" in a Vatican manuscript were "published with a Latin translation by Mai in 1838" (l.255–259). So Land was not its first editor, only the first to print the British Museum text. Fix, brief and audio: "Land, its editor of 1870, gives him book seven as well." Card `uncertain` 4: "Land, its editor of 1870, gives him book seven as well, as Brooks reports." Records: "Land, who edited the chronicle in 1870 (Kugener l.17146-17151)". Scored with N4: 324 words (2:00), FK 7.7, Flesch 63.6.

- **N4 MINOR (`zachariah-rhetor.brief.txt` l.9, audio; item 1; a hedge given a motive, carried by R1's own fix wording).** "Brooks suggests, with a 'perhaps,' that he had come over to Chalcedon's side to become bishop." Brooks: "at a later time, conforming perhaps to the Chalcedonian faith, was made bishop of Mitylene" (l.364–366). Brooks links the two events in time and says nothing of a purpose. "To become bishop" tells a motive, which the card's own `uncertain` 3 does not ("that he accepted Chalcedon when he became bishop"). Fix, brief and audio: "Brooks suggests, with a 'perhaps,' that he came over to Chalcedon's side when he became bishop." (Scored with N3 above.)

- **N5 MINOR (`audio/severus-of-antioch.audio.txt` l.13; item 13; a tag moved off the closing line, not recorded).** Before R1 the `[warmly]` tag stood before the closing sentence, "In the letter to Misael, Severus says God alone is…", as the pattern asks ("`[warmly]` goes before the closing line", `Who_Profile_Pattern.md` l.40). It now stands before "Brooks reckons his letters once numbered at least 3,759; a Syriac version made in 669 keeps 123." That puts the warm tone on a count. No R1 finding asked for this and `R1_changes.md` does not mention it. The brief is unchanged at this point. Fix: move `[warmly] ` back to just before "In the letter to Misael". The brief needs no change.

- **N6 MINOR (`records.json`, `caesaria-of-arles-the-elder`; item 1; one claim tagged two ways).** The B2 fix added "Venantius Fortunatus more than once held up Casaria, Caesarius's pious sister, as an example to follow; Krusch's note on her name cites Fortunatus's poems and a Gregory of Tours manuscript", tagged Dominant Modern Reconstruction. The record already held "Venantius Fortunatus more than once held up the pious sister Casaria as an example", with the same witness (Krusch l.35667–35668; "Fortunatus not held"), tagged Inferential-Thin. That leaves one claim in the record with two confidence levels. Fix: delete the older Inferential-Thin entry. The new one is fuller and carries note 8 (l.34757–34758).

- **N7 MINOR (`records.json`, `caesaria-of-arles-the-elder`, claim 2; items 1, 12; records left behind the M7 fix).** The claim reads "they were enclosed so that none might go out of the convent door until the day of her death". The Life says "usque diem transitus earum nulli liceat foris ianuam egredi de monasterio" (l.37217–37218): their own deaths. This is the reading M7 fixed in the brief, so brief and records now disagree. Fix: "until the day of their death".

No new or changed quotation is misquoted. I found no new absence claim that a held file contradicts, no editor's year given to an ancient writer, and no contested point told as settled. No namesakes are merged: Juvenal, the two Caesarias, Columcille and Columba, the two Dionysii and Julian and Julian of Halicarnassus are all kept straight in the new text. Card, brief and records otherwise agree after the changes.

## Totals

R1 findings: all 5 blocking are RESOLVED, and all 36 minor are RESOLVED. None is PARTLY or NOT RESOLVED. Three minor fixes (Joshua M2, Zachariah M10, Zachariah M11) were applied as R1 worded them, and that wording carries the new N1, N3 and N4. Caesaria M7 is resolved in the brief, and N7 brings the records into line.

New: 0 blocking, 7 minor (N1 and N2 `joshua-the-stylite`; N3 and N4 `zachariah-rhetor`; N5 `severus-of-antioch` audio; N6 and N7 `records.json` for `caesaria-of-arles-the-elder`). Every fix above was checked against the line it cites. The brief fixes (N1, N3 with N4) were scored with `grade_text` on a scratch copy.
