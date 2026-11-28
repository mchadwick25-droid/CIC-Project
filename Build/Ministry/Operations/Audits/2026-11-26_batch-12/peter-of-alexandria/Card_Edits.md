# Card edits: Peter of Alexandria

Card: `peter-of-alexandria.card.json`. Old card: `Card.existing.json`. Everything not listed here is word for word as it was.

## New

1. `shortDescription` (new field, Stage Two Kit section 1): two sentences from the brief's paragraphs 1 and 2 (persecution that began in 303; the fallen; Melitius; beheaded in 311).
2. `briefSources` (new): the old sources the brief draws on, each with its file: Peter's canons and letter (ANF 6 and the Pedalion Greek), the bishops' letter and account (ANF 6), Eusebius, Athanasius, Epiphanius, Socrates I.9, Nicaea canon 6 and Trullo canon 2.
3. `timeline` (new, Stage Two Kit section 2): five periods from the brief, outline and source sheet. Sources for lines: Eusebius VII.32 (EUS 43260-43268), VIII.2 (EUS 43484-43492), IX.1 (EUS 47567-47572), IX.6.2 (EUS 47995-47998); canons 1, 2, 3, 5, 6-7, 10, 12 (ANF6 26607-26626, 26677, 26723, 26806, 26892, 27161, 27482; canon 14 from the existing keyWorks line); the bishops' letter and account (ANF6 16710-16757, 16822-16844); Peter's letter (ANF6 27789-27804); Athanasius, Apology 59 (ATH 24776-24783) and 11 (ATH 22465); Epiphanius 68.3 (EPI 43724-43750, per the outline); Socrates I.9 (SOC 3206-3214) and I.15 (SOC 4005-4008); Nicaea canon 6 (NPNF14 3405-3407); Vincent, Commonitory 79 (VINC 14433-14438); Trullo canon 2 (NPNF14 26741-26745); Balsamon and Zonaras, "in every collection of Canons" (ANF6 25779-25784). Two dates carry a note: the canons' year (existing uncertain item); Eusebius's Book 7 reason for the death (EUS 43266-43268 against 47995-47998).
4. `quotationOriginals`, Q1 (brief paragraph 1, canon 1): `modern` changed to the brief's wording: old "They did not come to this by their own choice. The weakness of the flesh betrayed them. For they show the marks of Jesus in their bodies." New "They did not come to this by deliberate choice. They were betrayed by the weakness of the flesh, since they show the marks of Jesus in their bodies." Printed, Greek, lines and `uncertain` unchanged (re-read: ANF6 26616-26618; PED 49722-49723). `secondReading` "same" removed, since the rendering changed; release sets it.
5. Q2 (brief paragraph 6, Peter's letter): new entry. Modern: "Take heed of this. Do not share communion with him until I meet him with some wise and sensible men, and see what he has in mind." Printed (re-read, ANF6 27802-27804): "take ye heed to this, and hold no communion with him, until I meet him in company with some wise and discreet men, and see what the designs are which he has thought upon". Lines 27802-27804, not the outline's 27801-27804, since line 27801 holds the barred clause. The Latin is not held, so English alone. No `secondReading`.
6. Q3 (brief paragraph 8, Eusebius IX.6.2): `modern` changed. Old "He was seized for no cause, when no one expected it. All at once and with no reason given, as though on Maximinus's order, he was beheaded." New "He was seized for no cause at all, without warning, and suddenly and without reason, as if Maximinus had ordered it, he was beheaded." Printed and lines unchanged (re-read EUS 47996-47998). `secondReading` removed as in 4. The Greek is in a damaged scan only (EUS-G 17556-17560, "διαξιμίνου"), so English alone, as before.
7. Old Q2, Epiphanius, Panarion 68.3 ("Peter's case was for mercy and kindness..."): removed, because the brief no longer quotes it. The Oehler and Migne files stay in `sources`.
8. `briefReferences`: two added at the end: Eusebius IX.1 (the order letting Christians worship again; Maximinus would not accept it); Nicaea canon 6 (Alexandria's authority over Egypt, Libya and the Pentapolis; NPNF14 3405-3407).
9. `sources.about`: added Canon 6 of the Council of Nicaea (NPNF14 file) and Vincent of Lérins, Commonitory 79 (NPNF 11 file), both for the timeline.
10. `sources.about`: Bell and Hefele stay. The card's `uncertain` quotes Bell ("need not be taken very seriously"), and the validator checks that quote against the card's `sources`, so removing Bell fails it. Release moves both to `modernWorks` only together with a change to that quote's home.
11. `uncertain`: one item added at the end. Eusebius gives two statements about why Peter died (Book 7, EUS 43263-43268; Book 9, EUS 47995-47998). Outline, Do not say: no cause is given in the story.

## Clearly wrong

None found.

## Not found / left in place

- `briefReferences` item 9 (Epiphanius 68.3, Greek: "mercy and kindness" against "truth and zeal") names the line of the removed quotation. The brief still draws on Panarion 68 (item 4), but not on that sentence. Left in place for the check to rule on.
- `keyWorks`, Letter to the Church at Alexandria: "telling his people to hold no communion with Melitius" leaves out "until I meet him". It does not contradict the brief, so it is untouched.
- `knownFor` and the entry's `teaser` use "Great Persecution", which the outline says is not a source's phrase, and "Meletius"/"Melitius" differ between them.

## Entry fields

- `teaser`: "Bishop of Alexandria through the Great Persecution, who wrote the rules for those who had lapsed, broke with Meletius of Lycopolis, and was beheaded in 311." Change "Meletius" to "Melitius" (the brief and census spelling) and name what "lapsed" means, for example: "who wrote the rules for taking back Christians who had given way under torture, broke with Melitius of Lycopolis, and was beheaded in 311." The "Great Persecution" label needs a plain gloss or "the persecution that began in 303".
- `longDescription`: the brief (`peter-of-alexandria.brief.txt`), final newline removed.
- `dates`, `start`, `end`, `activeYear`: unchanged; the brief and card say bishop from about 300, died 311.
- `why`, `relationsSummary`: the census entry has neither key; nothing to change.
- `modernWorks` (new on the entry; none held today). Rights: all public domain by date (CORPUS-USE.md rules; the files' own headers):
  - Title "Jews and Christians in Egypt: The Jewish Troubles in Alexandria and the Athanasian Controversy, Illustrated by Texts from Greek Papyri in the British Museum", author "H. Idris Bell (ed.)", year "1924", note: edits the papyri of the Melitian church and sets out the early evidence on the schism. (Also listed in `sources.about`, where it reads "Jews and Christians in Egypt, chapter on the Melitian schism", Harold Idris Bell.)
  - Title "A History of the Councils of the Church, from the Original Documents, volume 1", author "Charles Joseph Hefele; William R. Clark (tr.)", year "1872", publisher "T. & T. Clark, Edinburgh", note: covers the councils to Nicaea, with Peter's canons and the Melitian dispute. (Also listed in `sources.about`.)
  - Title "Ante-Nicene Fathers, volume 6", author "James B. H. Hawkins (tr.)", year "1886", note: English of Peter's canons, letter and fragments, with the Greek word behind the marks of Jesus, used to clarify the Greek.
  - Title "Nicene and Post-Nicene Fathers, series 2, volume 1: Eusebius, Church History and Life of Constantine", author "A. C. McGiffert (tr.)", year "1890", note: English of the Church History with notes on the persecution's years, used to clarify the Greek of the death passage.
  - Title "Pedalion of the Noetic Ship of the One Holy Catholic and Apostolic Church of the Orthodox", author "Agapios and Nikodemos the Hagiorite", year "1886" (fourth edition; first printed 1800), note: prints the Greek of Peter's canons with the later commentaries, used to find the Greek of canon 1.
  The Bell, Hefele and Hawkins titles and years rest on the files' headers; the titles of the ANF 6 and NPNF 1 volumes as printed there should be confirmed at release.

## Validator

Run on a census copy outside the repository: the only errors left are release's own: `secondReading` absent on the three quotations (set from the blind renderings), the three stale renderings in `tools/quote_renderings.json` (two replaced, one removed), and the new renderings awaiting that registry.

## After review 3: modern views out of uncertain (Mark, 2026-11-28, "b")

Item numbers are the 1-indexed positions before this edit. Items 2, 7 and 10 are deleted; the rest move up.

- Item 2
  - Old: "Harold Idris Bell, who edited papyri of the Melitians in 1924, thinks the sacrifice charge "need not be taken very seriously", and that Epiphanius had good sources, probably bishops of Egypt banished to Palestine. He reads the two accounts as stages of one quarrel. Charles Joseph Hefele, historian of the councils, says the first letters show neither man was in prison when the split began, and that Epiphanius was mistaken on the main points."
  - New: deleted
  - Evidence: Nothing from an old source; the whole item argues or reads (Bell, Hefele). Deleted.
- Item 4
  - Old: "Sozomen says Peter ordained Arius a deacon and later cast him out over the Melitians. Sozomen's translator, Chester Hartranft, notes that no one else links Arius with the Melitians early. Archibald Robertson, editor of Athanasius, says such tales "deserve little credit"."
  - New: "Sozomen says Peter ordained Arius a deacon and later cast him out over the Melitians."
  - Evidence: Kept: SOC 27560-27563 (Sozomen: ordained deacon by Peter, who afterwards cast him out over the Melitians). Cut: Hartranft's note (SOC 27556) and Robertson's judgment.
- Item 5
  - Old: "The Genuine Acts of Peter, a later Passion, tell of his last night, a vision about Arius and his death at the tomb of Mark. McGiffert calls them "spurious and historically quite worthless.""
  - New: "The Genuine Acts of Peter, a later Passion, tell of his last night, a vision about Arius and his death at the tomb of Mark."
  - Evidence: Kept: ANF6 25834-25838 (the Genuine Acts, in Anastasius's Latin), 26078-26113 (night, boy in vision, Arius), 26284-26286 and 26323 (tomb of Mark). Cut: McGiffert's judgment (EUS 43251-43253).
- Item 7
  - Old: "The date of the split is given as 301 (Robertson), about 304 or 305 (Hefele) and probably 305 (Bell)."
  - New: deleted
  - Evidence: Dates rest on Robertson, Hefele and Bell alone; no old source gives them. Deleted.
- Item 9
  - Old: "The year of the canons is read two ways. Hawkins and McGiffert give 306, counting from Peter's own words, "the fourth passover of the persecution". Nikodemos, in the Greek book of church law, gives 304."
  - New: "Peter dates his canons by his own words, "the fourth passover of the persecution". Nikodemos, in the Greek book of church law, gives 304."
  - Evidence: Kept: ANF6 26657 and PED 49718 (Greek: τέταρτον ἤδη Πάσχα ἐπικατείληφε τὸν διωγμὸν), PED 49702-49703 (Nikodemos: 304). Cut: Hawkins's and McGiffert's 306 (ANF6 25777-25778).
- Item 10
  - Old: "On the prison, Bell thinks Peter and Melitius were set free soon after the quarrel began, probably when the persecution paused."
  - New: deleted
  - Evidence: Bell's guess only; no old source. Deleted.
- Item 11
  - Old: "That Peter himself was in hiding when he wrote to his people is Bell's and Hefele's reading. The account kept with the four bishops' letter says only that the priests he had appointed were in hiding."
  - New: "The account kept with the four bishops' letter says that the priests Peter had appointed were in hiding. It does not say where Peter was."
  - Evidence: Kept: ANF6 16836-16838 (presbyters, then in hiding, to whom Peter had given power). Cut: the Bell and Hefele reading.
- Item 12
  - Old: "Eusebius gives the ninth year of the persecution for Peter's death. McGiffert reckons that year from February 311 to February 312 and puts the death not long before the spring of 312. Hawkins and Bell give 311, and the day, 25 November, comes from the Egyptian church's later reckoning."
  - New: "Eusebius gives the ninth year of the persecution for Peter's death, and no day. The Genuine Acts of Peter give the day as 25 November."
  - Evidence: Kept: EUS 43266-43267 (ninth year); ANF6 26415-26417 (Acts: beheaded on 25 November). Cut: McGiffert's reckoning, Hawkins's and Bell's 311, and the Egyptian reckoning (ANF6 25770-25771, Hawkins's note).

Nothing else on the card changed. `sources` is unchanged. After this edit no quote in `uncertain` rests on a modern work, so Bell and Hefele in `sources.about` are no longer needed for the validator; they stay, and moving them is a release choice.

### Entry fields

`modernWorks`, in addition to the list above, each note saying what the work covers:
- Hartranft (tr.), Sozomen's Church History in NPNF 2, volume 2, with notes: English of Sozomen with notes on his text. No longer cited anywhere on the card.
- Robertson (ed.), Athanasius, Select Works and Letters, NPNF 2, volume 4, with Prolegomena: English of Athanasius's Apology against the Arians with an introduction to his career and the period. Cited now only in a `sources.about` title.
- Bell, Hefele, McGiffert and Hawkins stay as already listed.
