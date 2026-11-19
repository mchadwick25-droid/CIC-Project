# Card check: Tatian

Card checker, batch 6 (2026-11-19), under `Card_Check_Prompt.md`. Read: `tatian.brief.txt`, `tatian.card.json`, `Card_Edits.md`, `Card.existing.json` (identical to the census card for `tatian`), and each cited line in its file.

**Verdict: FIX** (four changes below, two of them with entries for `tools/quote_scan_readings.json`).

## 1. Each edit is justified

- **legacy.remembered[2], "Cyrus" to "Cyrrhus".** Justified. The brief says "Theodoret of Cyrrhus", and the census entry `theodoret-of-cyrrhus` is named "Theodoret of Cyrrhus". Only the spelling changes.
- **sources.about, Epiphanius added.** Justified. The brief's "only that writer puts him there" rests on Panarion 46.1 (EP 15995–16008) and Holl's note "nur durch Epiph. überliefert" (EP 16018).
- **sources.about, Theodoret via Maran added.** Justified, and required: Q3 cites this file (TH 14984–14987).
- **briefReferences, 16 lines.** Each was checked against the brief. One part names something the brief no longer tells (FIX 1).
- **quotationOriginals, four entries.** Each modern span is word for word in the brief. Each printed and original wording stands at its file and lines. Three of them carry scan faults copied from the OCR (FIX 2 to 4).

## 2. Nothing else moved

A field-by-field diff against `Card.existing.json` shows only the listed changes: legacy.remembered[2], two entries added at the end of sources.about, and the new briefReferences and quotationOriginals. Every other field is word for word and in order.

## 3. References

One part names something the brief no longer tells. Epiphanius 46.1 is cited for "a school in Mesopotamia", but the brief says only that Tatian "went east, to the land between the Tigris and the Euphrates". Some parts are kept because they show where the brief's claims come from: Crescens (the brief's "a philosopher at Rome"), "Chaldean" (the brief's "Babylonian"), Isho'dad of Merv (the source for Ephrem's commentary) and the Codex Fuldensis (the Latin form).

**FIX 1.** `briefReferences[9]`
- Old: "Epiphanius, Panarion 46.1, Greek of Karl Holl: from Rome to the East and a school in Mesopotamia; Holl notes that only Epiphanius gives the place."
- New: "Epiphanius, Panarion 46.1, Greek of Karl Holl: from Rome to the East, to Mesopotamia; Holl notes that only Epiphanius gives the place."

## 4. Census rules

The card uses only allowed keys and has no `briefLength`. There are four entries for the brief's four quoted spans, and none for a span the brief no longer quotes. Every cited file is in `sources`: anf02 and Otto 1851 under ownWords, anf01 and Otto 1872 under about. No briefReferences entry has quotation marks. No audit, review or ruling is named. Spelling is American. No entry has a `secondReading` yet: all four spans are new and wait for step 7, as the card prompt directs.

## 5. Originals

The outline renders Q1 and Q2 from Otto's Greek, and the card carries both. Q3's printed wording is itself the Greek. No Greek of "the self-controlled" is cited. But an original on a live card has to read as the page prints it, not as the OCR garbles it. The rule this batch applies (see the Ignatius check): a scan fault inside an original stands only if a reading in `tools/quote_scan_readings.json` resolves it. That reading must be confirmed by a held print of the same words, or the fault must be a stray mark that is plainly no part of the text. Otherwise the original is left out. Here every fault meets that test.

**FIX 2.** `quotationOriginals[0].original` (Q1). Line 12199 prints "Adıwalov" for Ἀθηναίων, and line 12200 has a stray "δ" run into καϑ᾽. Otto's own note prints the same clause cleanly at lines 1686–1688 ("τῇ Ῥωμαίων / μεγαλαυχίᾳ καὶ τῇ ᾿Αθηναίων ψυ- / χρολογία... τῆς καϑ᾽ ἡμᾶς").
- Old: "χαίρειν εἰπὼν καὶ τῇ Ρωμαίων μεγαλαυχία καὶ τῇ Adıwalov ψυχρολογίᾳ, δόγμασιν ἀσυναρτήτοις, τῆς δκαϑ᾽ ἡμᾶς βαρβάρου φιλοσοφίας ἀντεποιησάμην"
- New: "χαίρειν εἰπὼν καὶ τῇ Ῥωμαίων μεγαλαυχίᾳ καὶ τῇ Ἀθηναίων ψυχρολογίᾳ, δόγμασιν ἀσυναρτήτοις, τῆς καϑ᾽ ἡμᾶς βαρβάρου φιλοσοφίας ἀντεποιησάμην"
- Readings to add:
  - file `cic/texts/tatian_oratio-ad-graecos-grc-lat_otto1851.txt`, lines "12199", scan "τῇ Ρωμαίων μεγαλαυχία καὶ τῇ Adıwalov", reads "τῇ Ῥωμαίων μεγαλαυχίᾳ καὶ τῇ Ἀθηναίων", kind "OCR misread; the same edition prints the clause cleanly in its note, lines 1686-1688".
  - file `cic/texts/tatian_oratio-ad-graecos-grc-lat_otto1851.txt`, lines "12200", scan "τῆς δκαϑ᾽ ἡμᾶς", reads "τῆς καϑ᾽ ἡμᾶς", kind "OCR ran a stray letter into the word; the same edition's note reads καϑ᾽ ἡμᾶς, line 1688".

**FIX 3.** `quotationOriginals[3].original` (Q2). The OCR has set a single letter into the text twice: "Δ" at line 14239 and "δ" at the start of line 14241. These are the edition's margin letters. Neither belongs to the sentence, and Ryland's English (AG 7464–7471) has nothing for either.
- Old: "Γινώσκων δὲ λοιπὸν τίς ὁ ϑεὸς καὶ τίς Δ ἡ κατ᾽ αὐτὸν ποίησις, ἕτοιμον ἐμαυτὸν ὑμῖν πρὸς τὴν ἀνάκρισιν τῶν δογμάτων παρίστημι, μενούσης μοι δ τῆς κατὰ ϑεὸν πολιτείας ἀνεξαρνήτου."
- New: "Γινώσκων δὲ λοιπὸν τίς ὁ ϑεὸς καὶ τίς ἡ κατ᾽ αὐτὸν ποίησις, ἕτοιμον ἐμαυτὸν ὑμῖν πρὸς τὴν ἀνάκρισιν τῶν δογμάτων παρίστημι, μενούσης μοι τῆς κατὰ ϑεὸν πολιτείας ἀνεξαρνήτου."
- Readings to add:
  - file `cic/texts/tatian_oratio-ad-graecos-grc-lat_otto1851.txt`, lines "14239", scan "τίς Δ ἡ", reads "τίς ἡ", kind "OCR set the edition's margin letter into the line".
  - file `cic/texts/tatian_oratio-ad-graecos-grc-lat_otto1851.txt`, lines "14241", scan "δ τῆς", reads "τῆς", kind "OCR set the edition's margin letter into the line".

**FIX 4.** `quotationOriginals[2].printed` (Q3). This is a printed wording that stands only because it copies a scan fault: "Evgov" is the OCR's misreading of Εὗρον. Maran's Latin at TH 14994 reads "Nactus sum", that is, "I found".
- Old: "Evgov δὲ κἀγὼ πλείους ἢ διακοσίας βίβλους τοιούτας ἐν ταῖς παρ᾽ ἡμῖν ἐκκλησίαις τετιμημένας, καὶ πάσας συναγαγὼν ἀπεϑέμην, καὶ τὰ τῶν τεσσάρων εὐαγγελιστῶν ἀντεισήγαγον εὐαγγέλια."
- New: "Εὗρον δὲ κἀγὼ πλείους ἢ διακοσίας βίβλους τοιούτας ἐν ταῖς παρ᾽ ἡμῖν ἐκκλησίαις τετιμημένας, καὶ πάσας συναγαγὼν ἀπεϑέμην, καὶ τὰ τῶν τεσσάρων εὐαγγελιστῶν ἀντεισήγαγον εὐαγγέλια."
- Reading to add: file `cic/texts/apologists-fragmentary_reliquiae-corpus-apologetarum-vol9-grc-lat_otto1872.txt`, lines "14984", scan "Evgov", reads "Εὗρον", kind "OCR misread, Greek letters read as Latin".
- "τοιούτας" is left as scanned. The usual text has τοιαύτας, but no held print confirms what Otto's page reads.

The validator cannot catch any of these faults. Its fold drops every Greek letter, so the original-wording check on Greek reads nothing. Only "evgov" and "adiwalov" survive the fold.

## 6. Not found, and anything clearly wrong left in

The card writer listed no claims as not found. Nothing else in the card is clearly wrong: the existing claims stand in their sources, and none contradicts the brief.
