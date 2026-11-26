# Card check: Alexandrian Christianity (`alexandria-catechetical`)

Checker who did not write the card. Read: `CLAUDE.md` (Trust and source fidelity), Kit Part 1, `kinds/tradition.md`, the card role, the final brief (`alexandria-catechetical.brief.txt`), `Outline.md`, `Review.md`, `Fresh_Read.md`, `Card.existing.json`, `alexandria-catechetical.card.json`, `Card_Edits.md`, `Entry_Texts.md`. Every cited line below was re-opened in `cic/texts/`.

## Verdict: FIX

Six changes, below. Everything else checked holds.

## What holds

- **Nothing else moved (check 2).** A field-by-field compare of `Card.existing.json` with the card: `why`, `sourcing`, `floorNote`, `relationsSummary`, `voices`, `people` and `sources[0]`, `sources[1]` (bar the added `file`) are word for word. `legacy` and `sources[2]` differ only by Card_Edits 1 to 4 and 6.
- **Edits 1 to 9 (check 1).** Each stands on its lines: Soc 13913-13915; GN 47450-47451 (the joint editing is only the editor's heading, GN 47442-47443, so its removal is right); E-en 43201-43204; Ath 31215-31223; HP 10942-10943, 11712-11734, 11884-11890; E-en 28537-28576, 32796-32813, 32914-32916, 33201-33203, 34353-34356, 34818-34843, 34974-34982, 35122-35124, 35189-35198, 39552-39577 (the vision stays in Dionysius's voice), 41312-41316, 41374-41381; Ph 14-18, 76. Every Cut first and Leave out item marked "card" is on it, as Card_Edits lists. Fixes_Grade2 1c/1d were withdrawn (Recheck_Grade2), so their absence is right.
- **Quotations (checks 4, 5).** Three entries for five spans, each broken quotation as one entry, the form the validator names (`validate-census.mjs` line 227). Each `printed` is verbatim at its lines (E-en 32918-32925 with endnote 1798 removed; Cl 26369-26372; E-en 41368-41369). Each `original` is verbatim as the scan prints it (E-gr 1613-1614; E-gr 10734-10735, hyphen joined). Greek checked by hand: καὶ γυναικῶν δὲ Ἡραΐς ἔτι κατηχουμένη τὸ βάπτισμα, ὥς πού φησιν αὐτός, τὸ διὰ πυρὸς λαβοῦσα, τὸν βίον ἐξελήλυθεν; μήτε, εἰ λόγος αἱροίη, μεταπείθεσθαι καὶ συνομολογεῖν αἰδούμενοι. Apparatus: "24 αἴροι EBD … αἵρεῖ ATTR" (E-gr 10750); "ἐποιοῦντο μὲν … ἐποιούμεϑα von Darm bezeugt" (E-gr 10747), the governing verb at E-gr 10730. All three run six words or more, so no `secondReading` and none "checked at card": right. The renderings hold against original and print. Every quoted span in card prose (legacy, Book VI note) is found at its cited lines. Every cited file is in `sources`. American spelling throughout; no audit, review or ruling named.
- **briefReferences (check 3):** none on the card. **Census entry (check 7):** none (an existing tradition).
- **Validator.** Scratch census copy outside the repository, card merged, brief as `longDescription`, the proposed `modernWorks` and `relationsSummary`: the full run was killed for memory; `--skip-quotes` gives 0 errors, 4 warnings (all on other entries). Run again with the FIX items below merged: 0 errors, 4 warnings. The quotes were checked by hand, as above.

## Rulings asked for

1. **Bardy's `modernWorks` note: FIX.** Kit Part 1 (Accessibility) and check 1 say a modern work's line covers, never argues. Moving it "word for word" means it moves without being reworded. It does not override the standard every line meets. The note also states a modern claim of priority ("first argued"). Its `year` "1932" is not held in the Library. Published bibliographies give the article as *Recherches de science religieuse* 27 (1937), 65-90, so "1932" looks wrong as well. Hold to what is held and drop the year (FIX 1).
2. **voices[4], Didymus as the school's head: FIX.** The voice is clearly wrong against two held old sources, and it is the stronger case beyond Rufinus. Rufinus's Latin history says Didymus "scholae ecclesiasticae doctor exsisteret", became the church school's teacher, approved by Athanasius (E-gr 29902-29903, Rufinus XI.7; chapter title E-gr 29066). Sozomen, Church History III.15, calls him "president of the school of sacred learning in Alexandria" (npnf202 31950-31955). So "no surviving primary account actually says so" is false. "in its final generation" stands on no held line. Fewest words that put it right: FIX 2, with the two sources it adds (FIX 3) and Sozomen's translator (FIX 4).
3. **`relationsSummary` cut: PASS.** "real at one disputed point and denied as a general continuation" is a modern scholarly verdict stated as content (Kit Part 1, Rigor; check 1). The held old sources tested give no Alexandrian teacher in Antony's life (Ath 31215-31223). The cut changes no edge and no other entry. "A contested influence" still matches the census edge's Contested rating, so it does not run against "leave connections out for now". Apply Card_Edits, Entry fields 2, as written.

## FIX items

**FIX 1. `modernWorks`, Bardy entry** (Card_Edits, Entry fields 3).
- Old: `{"title": "Aux origines de l'École d'Alexandrie", "author": "Gustave Bardy", "year": "1932", "note": "The 1932 study that first argued, against Eusebius's tidy succession-list, that Alexandria's teaching looked more like a sequence of private Christian tutors than one formal institution — the opening move in a scholarly debate that remains unsettled today."}`
- New: `{"title": "Aux origines de l'École d'Alexandrie", "author": "Gustave Bardy", "note": "A study of the early history of Christian teaching at Alexandria."}`

**FIX 2. `voices[4]`** (clearly wrong; Rufinus E-gr 29902-29903; Sozomen npnf202 31950-31955).
- Old: `later tradition remembers him as heading the school in its final generation, though no surviving primary account actually says so.`
- New: `the Latin church history of Rufinus says he became the teacher of the church's school, and the fifth-century historian Sozomen calls him its president.`
- The rest of the voice stays word for word.

**FIX 3. `sources`, two new items at the end** (each cited file in `sources`).
- `{"work": "Rufinus, Church History, Book XI (Latin), ed. T. Mommsen", "type": "primary", "note": "Rufinus's chapter on Didymus the Blind, who became the teacher of the church's school.", "file": "cic/texts/eusebius_werke-bd2-2-historia-ecclesiastica-vi-x-rufinus-x-xi-grc-lat_schwartz-mommsen1908.txt"}`
- `{"work": "Sozomen, Church History, Book III", "type": "primary", "note": "Its chapter on Didymus the Blind, president of the school of sacred learning in Alexandria.", "file": "cic/texts/npnf202_socrates-sozomen-ecclesiastical-histories.xml"}`

**FIX 4. `modernWorks`, NPNF 2 entry** (FIX 2 now uses its Sozomen; translator at npnf202 21654).
- Old author: `"A. C. Zenos (tr. of Socrates)"`
- New author: `"A. C. Zenos (tr. of Socrates); Chester D. Hartranft (tr. of Sozomen)"`
- Old note: `"English translation of Socrates's Church History, with notes."`
- New note: `"English translations of the Church Histories of Socrates and Sozomen, with notes."`

**FIX 5. `quotationOriginals[0].uncertain`** (clearly wrong). Origen is not named in the sentence before Herais. The sentence before is about the second Serenus (E-gr 1610-1613). He was last named as "τῶν ᾿Ωριγένους φοιτητῶν" at E-gr 1489, in the chapter on his pupils (E-en 32885-32890).
- Old: `He himself renders αὐτός, which points back to Origen in the sentence before;`
- New: `He himself renders αὐτός, which points back to Origen, whose pupils the chapter lists;`

**FIX 6. Entry texts (`Entry_Texts.md`).** Each other claim checks out against the brief, outline and sheet. The intro keeps Theon and his frame. The dates follow the brief. No quotation marks are used. Two items fail Part 1, Explain it:
- **tile.** It names Origen's teaching on the three parts without saying what it means.
  - Old: `Origen wrote that Scripture has a body, a soul and a spirit, as a person does.`
  - New: `Origen wrote that Scripture has a body, a soul and a spirit, as a person does. Its plain story feeds the simple, and its deeper senses feed those who have gone further.`
  - Brief, paragraph 4; Ph 76.
- **summary.** "the Word" is not explained.
  - Old: `Clement taught that the Word first urges people on, then trains them, then teaches them.`
  - New: `Clement taught that the Word, his name for Jesus, first urges people on, then trains them, then teaches them.`
  - Brief, paragraph 3; Cl 19998-19999.
- `intro` and `recordHolds`: PASS.

## Not found, left in place (check 6)

The writer's Not found list was re-checked and holds as listed. One finding, recorded here and not changed under the role's rule: several of those claims are unsourced judgments of the kind Kit Part 1 keeps off the card. They are:
- `why`, "a method that shaped how much of the church has read the Bible ever since"
- `legacy` paragraph 1
- `legacy` paragraph 2, "set the standard for … languages" and "Ambrose and Jerome … careful about saying so"
- voices[2], "the first Christian to attempt a systematic account"
- `floorNote`, "around 399–400"

Each needs a held line or a change order. That is for release to log in Open Gaps, not for this card pass. Nothing else clearly wrong was found left in.
