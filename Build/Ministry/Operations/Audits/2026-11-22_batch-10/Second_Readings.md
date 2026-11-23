# Second Readings (batch 10, B10-01 to B10-29)

## Method

The comparer did not do the blind readings. For each id in `Second_Reading_Key.md`:

1. Our wording was checked against the brief (`<slug>/<slug>.brief.txt`, whitespace joined) and against the card entry's `modern` (`<slug>/<slug>.card.json`). All 29 wordings stand once, word for word, in their briefs, and all 29 equal the `modern` of the entry the key names. The key's file and lines match the entry's `file`/`lines` (printed) or `originalFile`/`originalLines` (original) in every case.
2. Our wording was set beside the blind rendering (`Second_Readings_Blind_A.md`, `_B.md`, `_C.md`).
3. Where they differ, the cited lines in `cic/texts/` and the card's `printed` or `original` were opened. For B10-06 and B10-28, the Latin behind the English was also opened (below).
4. Verdicts: SAME (same meaning), MINOR (a difference a listener would not take differently), MEANING (a listener would understand something different).

### Spans checked

Each request's word count was compared with the whitespace tokens of the card's `printed` (or `original`). All 29 match, so the counts are tokens of the card's text. The three mismatches the blind readers raised are miscounts or stray marks, not wrong spans.

- **B10-08.** Reader A counted 32 words and guessed the 33rd was Ἐγὼ, from the next sentence. The guess is wrong. The card's `printed` is 32 Greek words plus one free-standing mark (" after τριάκοντα, line 113737, where the scan has a stray quote for a raised stop). The span runs from Πρῶτον to διατριδῆς, and A's rendering covers exactly it.
- **B10-09.** Reader A counted 31 words and guessed the request took in "An sola". The guess is wrong. The card's `printed` is 31 Latin words plus two free-standing colons ("laudanda es :", "praeferenda es :", as the scan prints them at 815-816). The span ends at "possunt", and A's rendering covers exactly it.
- **B10-16.** Reader B counted 58 words. The sentence from "Wherever" to "assenting to." (lines 45775-45780) is 60 whitespace tokens, equal to the card's `printed`. B's count is a miscount; B rendered the right span.

### The OCR doubt at B10-17

Reader B read the scan's "his qui interpretabar" (PL 23, line 31113) as "his quae interpretabar". The scan does print "qui". As printed it cannot stand: "qui" with a first-person verb would mean "I who", which does not fit "his". The parallel "illis, que tu ante transtuleras" and Fremantle's English (npnf203, 51325-51331, "what was in my translation") both need the neuter "quae". The same scan drops ae to e throughout ("Greco", "que", "Ecclesie", "Heec"), so a damaged "quae" is likely, though a printer's slip cannot be ruled out without the page. No second Latin print is held. Either way the sense is the same, and ours ("what I translated") is the "quae" reading. The card keeps the scan's spellings ("Greco", "que") in `original`, so "qui" stands as printed; no correction is needed, but the `uncertain` could say so (below).

### Latin opened

- **B10-06.** Mansi V (`cic/texts/mansi_sacrorum-conciliorum-collectio-tomus-5-431-441-lat_welter-facsimile1901.txt`, 88759-88763) reads "contra tuam injuste & inique facta sunt sanctitatem, nec si ambas manus meas quilibet abscindat, patior assentire ... divina mihi cooperante gratia & animae imbecillitatem roborante". It bears out the card's "wickedly" (inique) and "weak soul".
- **B10-28.** Halm (`cic/texts/sulpicius-severus_libri-qui-supersunt-chronica-vita-martini-lat_halm1866-csel1.txt`, 5891) reads "mihi tam reos quam accusatores displicere", the accused first, as the card's `uncertain` says.

## Verdicts

| id | piece, entry | verdict | reason |
|---|---|---|---|
| B10-01 | council-of-ephesus-431 [0] | SAME | Same four questions and answers. Ours drops "And", which the card ties to Nau's French. |
| B10-02 | council-of-ephesus-431 [1] | SAME | "humbly begged" = "asked humbly"; "gained nothing" = "achieved nothing". |
| B10-03 | council-of-ephesus-431 [3] | MINOR | Ours drops the opening "For" (the card says why). "Mother of God" vs "God-bearer (Theotokos)" for θεοτόκον, the standard English title, as Hefele's and Pusey's English give it. "union without mixing" = "union without confusion". |
| B10-04 | eutyches [0] | MINOR | "was from two natures" vs "came to be from two natures" for γεγενῆσθαι. Perry's English has "was of Two Natures". The closing "I confess" stands on line 2289, as reader A notes and the card says. |
| B10-05 | eutyches [1] | SAME | "grown old with them" = "grown old with". Ours goes on past the page break. The tail, "heretics, and in confessing the true faith", stands at line 23504, "Heretics and in the Confession of the Orthodox Faith", as the card says. |
| B10-06 | theodoret-of-cyrrhus [0] | MINOR | Reader A followed Jackson ("illegally", "my weakness"). Ours follows the Latin, Mansi V 88759-88763: "inique" (wickedly), "animae imbecillitatem" (weak soul). The same refusal, "even if someone cuts off both my hands". |
| B10-07 | theodoret-of-cyrrhus [1] | SAME | "took the form" = "took on the form". |
| B10-08 | theodoret-of-cyrrhus [3] | SAME | Same four heights in cubits and the same longing. "It" is the pillar named just before in the brief; A supplies "[a pillar]". "this life on earth" = "this life spent on earth". |
| B10-09 | pelagius [0] | MINOR | "you are rightly praised" vs "you are rightly to be praised" for "jure laudanda es"; "rightly" carries the "deserve". "set above" = "ranked above". |
| B10-10 | pelagius [1] | SAME | "wholly poison" = "pure poison"; "clearly food" = "plainly food". |
| B10-11 | pelagius [2] | SAME | "passage" = "place" for locus, in letters being read. |
| B10-12 | john-cassian [0] | SAME | Same contrast: seem opposed, are in harmony. |
| B10-13 | john-cassian [2] | SAME | "wholesome" = "healthy and helpful"; "brands as harmful" = "labels as harmful". |
| B10-14 | john-cassian [3] | MINOR | "rules" vs "Institutes". The card's `uncertain` reads Institutes as the elders' rules of life, not the title. "May we set" vs "may manage to set". |
| B10-15 | rufinus-of-aquileia [0] | SAME | Same words. |
| B10-16 | rufinus-of-aquileia [1] | MINOR | "which he teaches soundly elsewhere" vs "a truth he speaks of elsewhere in a strictly orthodox way"; "left it out as not his own" vs "as something foreign to him and not genuinely his". Same two choices, same rule of faith. |
| B10-17 | rufinus-of-aquileia [2] | SAME | "what I translated" = "the things I was translating". Both take the scan's "qui" as "quae" (above). |
| B10-18 | frumentius [0] | SAME | "common talk" = "popular rumour"; "priest" = "presbyter". |
| B10-19 | frumentius [1] | SAME | "could we find" vs "shall we find", both a question that expects none; "carry it through in this way" = "carry these things out as you have". |
| B10-20 | frumentius [2] | SAME | "with all speed" = "as quickly as possible". |
| B10-21 | frumentius [3] | SAME | "this rank" = "this rank in life"; both make Athanasius the one "guilty of countless crimes". The card's βίου and ὢν are the hand reading of the scan's βίον and ὧν. |
| B10-22 | mesrop-mashtots [0] | SAME | Same three denials and the same image; "on stone" vs "on the stone". |
| B10-23 | mesrop-mashtots [1] | SAME | "as if they were" = "as if they had been". |
| B10-24 | mesrop-mashtots [2] | SAME | "bright and well taught" = "intelligent and educated". |
| B10-25 | ulfila [0] | MINOR | "those who confessed his holy only Son" vs "the confessors of his holy only-begotten Son". "Only Son" is the usual English for unigenitus, and "confessed" keeps the profession of faith, though "confessors" says more plainly that they held to it under persecution. "made sure they would serve him" = "provided for them to serve him". |
| B10-26 | ulfila [3] | SAME | Ours quotes the core, "subject and obedient in all things"; reader C renders the whole clause around it. |
| B10-27 | priscillian [0] | MINOR | Ours makes the clause a standalone rule, "No one should be forbidden", and C keeps it "[we urged] not to forbid it". The brief's "what he and his friends had always urged" supplies the frame. "despises" vs "having scorned". |
| B10-28 | priscillian [1] | MINOR | Ours puts the accused first and C, following Roberts, puts the accusers first. Ours follows the Latin, "tam reos quam accusatores" (Halm 5891). "As much as" holds either way. |
| B10-29 | priscillian [2] | SAME | "loathed ... So they cut down its founder" = "hated it so much that they put its founder to death". Same sword, same public laws. |

## Counts

- SAME: 20 (B10-01, 02, 05, 07, 08, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23, 24, 26, 29)
- MINOR: 9 (B10-03, 04, 06, 09, 14, 16, 25, 27, 28)
- MEANING: 0
- Total: 29

## Card changes needed

`secondReading` to set (no `original` needs correcting):

| card | entry | secondReading |
|---|---|---|
| council-of-ephesus-431 | quotationOriginals[0] | same |
| council-of-ephesus-431 | quotationOriginals[1] | same |
| council-of-ephesus-431 | quotationOriginals[3] | minor |
| eutyches | quotationOriginals[0] | minor |
| eutyches | quotationOriginals[1] | same |
| theodoret-of-cyrrhus | quotationOriginals[0] | minor |
| theodoret-of-cyrrhus | quotationOriginals[1] | same |
| theodoret-of-cyrrhus | quotationOriginals[3] | same |
| pelagius | quotationOriginals[0] | minor |
| pelagius | quotationOriginals[1] | same |
| pelagius | quotationOriginals[2] | same |
| john-cassian | quotationOriginals[0] | same |
| john-cassian | quotationOriginals[2] | same |
| john-cassian | quotationOriginals[3] | minor |
| rufinus-of-aquileia | quotationOriginals[0] | same |
| rufinus-of-aquileia | quotationOriginals[1] | minor |
| rufinus-of-aquileia | quotationOriginals[2] | same |
| frumentius | quotationOriginals[0] | same |
| frumentius | quotationOriginals[1] | same |
| frumentius | quotationOriginals[2] | same |
| frumentius | quotationOriginals[3] | same |
| mesrop-mashtots | quotationOriginals[0] | same |
| mesrop-mashtots | quotationOriginals[1] | same |
| mesrop-mashtots | quotationOriginals[2] | same |
| ulfila | quotationOriginals[0] | minor |
| ulfila | quotationOriginals[3] | same |
| priscillian | quotationOriginals[0] | minor |
| priscillian | quotationOriginals[1] | minor |
| priscillian | quotationOriginals[2] | same |

The originals opened (Hefele 7243-7245 for Ephesus [3]; Evagrius 2285-2289 for Eutyches [0]; PL 23 31111-31115 for Rufinus [2]; PG 25 92806-92814 for Frumentius [2] and [3]) stand as given.

Flagged for the card's owner, not a `secondReading` change:

- rufinus-of-aquileia [2]: the `uncertain` could note that the scan prints "his qui interpretabar", which the sense, the parallel "illis, que", and Fremantle's English read as "quae".
- theodoret-of-cyrrhus [0]: the `uncertain` says the Latin is a damaged scan and does not cite lines. Mansi V 88759-88763 reads cleanly enough to confirm "inique" and "animae imbecillitatem", and the note could cite them.
