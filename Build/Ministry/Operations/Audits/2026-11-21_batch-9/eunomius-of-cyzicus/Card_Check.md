# Card check: Eunomius of Cyzicus (`eunomius-of-cyzicus`)

**FIX** (four changes), and **one item for Mark**: quote 2 has no held print behind its words.

## Checked

- Starting card: `Card.existing.json` equals the census card. Every field not listed in `Card_Edits.md` is word for word. The added list items come after the old ones, in order. The changes are the two corrections plus the extended Socrates and Sozomen title in `sources.about[1]`.
- The two corrections are justified. "The greater part of the church" is Sozomen 6.26, `npnf202` 39172-39177, and it is what the brief says. "Freese ... gives 393" is `photius_library-v1_freese1920.txt` 1988, "Eunomius (d. 393)", which shows the old line ("No source in the Library gives the year ... of his death") was wrong.
- Validator, on a scratch census with the card and brief set in: no errors for this entry except the ones the release step clears (no `secondReading` on the three quotations of six words or more; the two long modern quotations not yet in `tools/quote_renderings.json`). Keys allowed; six `quotationOriginals`, one for each of the brief's quoted spans.
- Quotations under six words ("Unbegotten", "unlike", "or rather"), checked at card. Each `printed` stands at its line: Whiston 38 has "Unbegotten" and "or rather", and Walford 246 has "unlike". Each rendering matches its print. The Greek behind them, in the PG 29 scan, agrees: ἀγέννητον ... μᾶλλον δὲ αὐτό ἐστιν οὐσία ἀγέννητος (99678-99681).
- Quote 1 is printed from Whiston 38, verbatim. It is a held English print of the sentence, and the modern English follows the scan's Greek where the two differ. Under the damaged-scan rule this is right.
- New items spot-checked against their lines: the Theodosian Code (7064, 7074-7075, 7100, 7127-7130, 7134); canon 1 of 381 (`npnf214` 13969-13973); Sozomen; Photius. They hold, and American spelling is used throughout.

## Quote 2 (Basil's answer): no held print stands behind the quoted words

The modern words are "I too would say that God's being is unbegotten. But I would not say that 'unbegotten' is his being." They render Basil's Greek, Against Eunomius 1: Ἐγὼ δὲ τὴν μὲν οὐσίαν τοῦ Θεοῦ ἀγέννητον εἶναι καὶ αὐτὸς ἂν φαίην, οὐ μὴν τὸ ἀγέννητον τὴν οὐσίαν. The rendering is faithful to that Greek.

But the Greek is held only in `basil_opera-omnia-pg29-grc-lat_migne1857.txt`. That is the OCR of one print (Migne). The corpus map marks it "second witness for quotation until checked against the page image". `tools/quote_scan_readings.json` lists no reading for it. The file scans the sentence twice: at 101276-101277 with the fault "Ἐτγὼ", and clean at 102840-102841. Both scannings are of the same print, so neither counts as "another held print" to confirm the other. No English translation of the sentence is held.

The `printed` the card gives (`npnf208` 4027-4030) does not stand behind the quoted words. It is not even Jackson's own summary: Jackson is quoting Dorner, *Christologie* i. 906 (the note at 4024-4026 names him). And it gives only the second half of Basil's point (unbegotten "is not a name indicative of the essence of God"). It says nothing of the first half, that Basil himself would call God's being unbegotten. Jackson's Greek endnote at 4030-4036 is from Adv. Eunom. iv, a different sentence.

**This comes to Mark**, as batch 8's three quoted spans with no clean print did. The options are:
- (a) Have someone check the PG 29 page image, list the reading in `tools/quote_scan_readings.json`, and print the Greek.
- (b) Drop the quotation marks in the brief and tell Basil's answer in the narrator's words, with the outline's evidence.
- (c) Keep it as is, with the `uncertain` note corrected below.

The card cannot settle this itself.

## Changes

1. `quotationOriginals[5].work`. Old: "Jackson's summary of Basil, Against Eunomius 1, in the Prolegomena to Basil's works (editor's English, not Basil's sentence)". New: "Dorner's summary of Basil, Against Eunomius 1, as Jackson quotes it in the Prolegomena to Basil's works (an editor's English, not Basil's sentence)".
2. `quotationOriginals[5].uncertain`. Old: "The English printed here is Jackson's summary of Basil's point, not his sentence, and confirms its sense." New: "The English printed here is Dorner's summary of Basil's point, quoted by Jackson, not his sentence. It confirms only the second half, that unbegotten does not name God's being."
3. `briefReferences[5]`. Old: "Jackson's Prolegomena: the main point of Basil's answer is that unbegotten names a condition of existence, not the being of God." New: "Dorner, as Jackson's Prolegomena quotes him: the main point of Basil's answer is that unbegotten names a condition of existence, not the being of God."
4. In `sources.about`, the entry titled "Prolegomena to Basil's Letters and treatises (tr. Blomfield Jackson)" is wrong. Old: `"author": "Basil of Caesarea"`. New: `"author": "Blomfield Jackson"`. The Prolegomena are Jackson's, and the card cites them only for his words and the words he quotes.

## Not found, left in

- "His master's tomb" (an `uncertain` line in the starting card) glosses Philostorgius's "the master". It is listed as not found, and it is not wrong, so it stays.
