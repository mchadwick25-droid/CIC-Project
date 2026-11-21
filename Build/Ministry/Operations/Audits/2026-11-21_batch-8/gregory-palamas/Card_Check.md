# Card check: Gregory Palamas

Batch 8, 2026-11-21. Independent checker; I wrote neither the brief nor the card. New card (no census entry, no starting card), so every field was checked against its evidence in `Card_Edits.md`. Every Greek wording was read by hand, letter by letter, against its file, because the validator folds Greek. Files are under `cic/texts/` unless noted.

**Verdict: FIX** (4 changes, below; FIX 4 needs the coordinator, and through it Mark).

## 1. Each field justified

Spot-read against the files:
- Kantakouzenos on his birth, the court and the "very young" departure (KAN1 32723-32726: πάνυ παιδικῇ τῇ ἡλικίᾳ). The name "Γρηγόριος ὁ Παλαμᾶς" is at 32723 (the scan prints "0" for ὁ), not 32722; this is a slip in `Card_Edits.md` only.
- Philotheos on the sixty-three years (PHIL 8243-8247).
- Covel (COVEL 29751-29753).
- Gregoras's own voice at GRE3 528 ("ἔγωγε ἔφασκον").

All hold as the card states them.

## 2. Nothing else moved

Not applicable: no starting card.

## 3. References

Checked against the brief and `gregory-palamas.brief.v1.txt`. Two name what the brief does not tell (FIX 1, FIX 2):
- The brief gives only "deceivers and navel-souls", not "liars, Messalians".
- The brief does not tell the Slavonic Philokalia.

The other nine stand, and none has quotation marks. One note: the brief's "eighteenth century" for the Philokalia rests only on the Library's own file header (PHK1 lines 2 and 9, Venice 1782). The book's text (PHK1 38) names the Venice edition but gives no year. The card asserts no year, so nothing changes on the card.

## 4. Census rules

- Keys: all allowed. No `briefLength`.
- Five quoted spans, five entries, each `modern` exactly the brief's.
- [0] and [4] are under six words and carry "checked at card". [1], [2] and [3] carry no `secondReading`.
- Every cited file is in `sources`. No audit, review or ruling is named.
- Spelling: "Saviour" in `legacy.remembered[2]` is card prose paraphrasing Covel, not printed wording (FIX 3).

## 5. Originals, read by hand

- **[0] "navel-souls." KEEP.**
  - The Greek Ὀμφαλοψύχους (KAN1 32673) is clean.
  - The Latin Omphalopsychos (KAN1 32701) is clean.
  - The rendering is exact.
- **[3] Gregoras, "in labor with ..." KEEP.**
  - The Latin "dogmata polytheismi / simulque atheismi parturiret" (GRE3 552-553) is clean.
  - Leaving the Greek out is right: ὀδίνοντα (GRE3 530) has no confirming print.
  - The rendering follows the Greek ὠδίνοντα τὰ τῆς πολυθεΐας ἅμα καὶ ἀθεΐας δόγματα, clause by clause.
- **[4] "The heavenly to the heavenly." KEEP as the half-print it is.**
  - "εἰς τὰ ἐπουράνια" (PHIL 8236) is clean.
  - The first half, "éns-/ράνια", is unreadable between ἐπουράνια and οὐράνια. The English holds either reading, and `uncertain` says so.
  - "Philotheos's own echo at line 8243" is accurate as worded. It is his narration using the word, not a second report of the dying words, and the card does not claim it confirms anything.
- **[1] the navel-souls answer (PHK2 42167-42170) and [2] chapter 107 (PG150 67527-67533): the Greek is right letter for letter, but as the rule now stands it cannot be printed (FIX 4).**
  - **What the Greek says.** For [1], read by hand: οἱ δ᾽ ὀμφαλοψύχους τούτους ὀνομάζοντες, πρὸς τῷ συκοφαντεῖν σαφῶς ὧν κατηγοροῦσι· τίς γάρ ποτε τούτων ἐπ᾽ ὀμφαλοῦ λέγει τὴν ψυχήν; The rendering is fair. The main verb comes later (ἔδειξαν, 42173), and `uncertain` says the quotation stops at the question.
  - **[2] read by hand.** Migne and the Philokalia (PHK2 45852-45860) agree on every word, and each resolves the other's faults:
    - προποῦσαν/προσοῦσαν, ἔχφανσιδ/ἔχφανσιν, ὁμόÀoyo;/ὁμό-λογος, ᾿ἀχείνην/ἐχείνην;
    - the Philokalia's ха!, ко!, "9" and ἐνέρ-упау against Migne's χαὶ, δ᾽ and ἐνέργειαν.

    The rendering matches clause by clause.
  - **The fault.** Both entries read χ as κ. [1] has it in one word (χα-τηγοροῦσι). [2] has it in nine words, and in Migne's Latin-letter xat and xal, which the Philokalia confirms only as χαὶ. No held print anywhere shows κ in these words.
  - **What precedent requires.** The batch 6 ruling left χ-for-κ Greek out (Irenaeus [0] and [1]). Batch 7 did the same for a lone χατηγορεῖτο (`eusebius-of-caesarea/Card_Check.md`, entry [6]). Under that rule both Greek wordings are left out.
  - **No fallback.** Migne's facing Latin cannot stand in either. [1] has "cos" and "nnimam" at PG150 64679-64683. [2] has "iucommunicabilem" and "el" at 67565-67568. No held print confirms those readings, and no English of either work is held. Leaving the Greek out therefore leaves both spans with no printed wording.

## 6. "Not found" claims and anything left wrong

- **Left off: correct.** This covers the Who card's unrechecked items (captivity, Lemnos, Combefis, the Bollandists and the rest) and "past his boyhood". None was rechecked to a held line.
- **"Present" at 1351: correct.** KAN3 10399-10410 says the emperor was present, not that he presided.
- Nothing else found wrong.

## Fixes

**FIX 1.** `briefReferences[0]`
- Old: `John Kantakouzenos, Histories, volume 1: Barlaam, a monk from Calabria, goes to a simple hesychast, hears of the joy beyond words and the light seen with bodily eyes, and turns on the hesychasts, calling them deceivers, liars, Messalians and navel-souls; Kantakouzenos, later emperor, is Palamas's ally.`
- New: `John Kantakouzenos, Histories, volume 1: Barlaam, a monk from Calabria, goes to a simple hesychast, hears of the joy beyond words and the light seen with bodily eyes, and turns on the hesychasts, calling them deceivers and navel-souls; Kantakouzenos, later emperor, is Palamas's ally.`

**FIX 2.** `briefReferences[9]`, last sentence
- Old: `The Philokalia of Venice and the Slavonic Philokalia of Optina: his writings on prayer.`
- New: `The Philokalia of Venice: his writings on prayer.`

**FIX 3.** `legacy.remembered[2]`, one word
- Old: `the light which shone about our Saviour was God himself`
- New: `the light which shone about our Savior was God himself`

**FIX 4.** `quotationOriginals[1]` and `[2]`. This is a methodology question, so it goes to Mark (CLAUDE.md, "Governance or methodology change: always ask"). I recommend option (a) because the Greek is not in doubt: two independent editions agree on every word of [2], and the scans read real chi correctly in the same lines (ἀλλαχοῦ, PG150 67525). The rule that would change was itself a checker's application of Mark's guidance, and batch 7's Eusebius [6] would then be reopened under the same rule.

- **(a) If Mark rules that χ read for κ is a letter-form fault, like θ/ϑ,** both entries KEEP as written, with these readings:

```json
{"file": "cic/texts/philokalia_ton-ieron-neptikon-v2-grc_tzelatis1893.txt", "lines": "42168", "scan": "ὧν χα-", "reads": "ὧν κα-", "kind": "OCR misread (χ for κ)"},
{"file": "cic/texts/palamas_opera-omnia-pg150-grc-lat_migne1865.txt", "lines": "67527", "scan": "ἀχούσῃς", "reads": "ἀκούσῃς", "kind": "OCR misread (χ for κ)"},
{"file": "cic/texts/palamas_opera-omnia-pg150-grc-lat_migne1865.txt", "lines": "67528", "scan": "ἀμέθεχτον", "reads": "ἀμέθεκτον", "kind": "OCR misread (χ for κ)"},
{"file": "cic/texts/palamas_opera-omnia-pg150-grc-lat_migne1865.txt", "lines": "67529", "scan": "᾿ἀχείνην μοι νόει τὴν ἀνεχφοίτητόν τε χαὶ ἀνέχφαν-", "reads": "ἐκείνην μοι νόει τὴν ἀνεκφοίτητόν τε καὶ ἀνέκφαν-", "kind": "OCR misread (χ for κ, and ἀ for ἐ as the Philokalia prints it)"},
{"file": "cic/texts/palamas_opera-omnia-pg150-grc-lat_migne1865.txt", "lines": "67530", "scan": "μεθεχτὴν, νόει μοι τὴν φυσιχῶς", "reads": "μεθεκτὴν, νόει μοι τὴν φυσικῶς", "kind": "OCR misread (χ for κ)"},
{"file": "cic/texts/palamas_opera-omnia-pg150-grc-lat_migne1865.txt", "lines": "67531", "scan": "προποῦσαν τῷ Θεῷ πρόοδον, xat τὴν ἔχφανσιδ, xal", "reads": "προσοῦσαν τῷ Θεῷ πρόοδον, καὶ τὴν ἔκφανσιν, καὶ", "kind": "OCR misread, as the Philokalia prints it (χ for κ; Latin letters for καὶ)"},
{"file": "cic/texts/palamas_opera-omnia-pg150-grc-lat_migne1865.txt", "lines": "67532", "scan": "χαὶ οὕτως", "reads": "καὶ οὕτως", "kind": "OCR misread (χ for κ)"},
{"file": "cic/texts/palamas_opera-omnia-pg150-grc-lat_migne1865.txt", "lines": "67533", "scan": "Àoyo;", "reads": "λογος", "kind": "OCR misread, as the Philokalia prints it"}
```

- **(b) If the rule stands,** remove `quotationOriginals[1]` (modern `Those who call them navel-souls are, ...`) and `quotationOriginals[2]` (modern `So when you hear the Fathers say ...`) entirely. The brief must then lose the quotation marks on both spans. That is a story change after recheck and the coordinator's to order, not the card's. Nothing in between will do: a partial print, or Migne's damaged Latin, would misstate the wording.
