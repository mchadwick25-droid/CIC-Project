# Card check: Mesrop Mashtots

**Verdict: FIX** (seven changes, below). T2 = `cic/texts/langlois_collection-historiens-armenie-tome2-fra_1869.txt`.

## What holds

- **Nothing else moved.** A field-by-field diff of `Card.existing.json` against `mesrop-mashtots.card.json` shows exactly the three listed corrections; every other existing field is word for word. The new fields are appended.
- **Correction 1** (`legacy.traces[0]`, Edessa, then Constantinople): supported (T2 3818-3828; the brief).
- **Correction 2** (`legacy.remembered[0]`, the nephew claim): supported. The Nerses introduction at T2 4455-4465 gives the view to "le savant éditeur du texte", and the introduction is signed "V. L." (T2 4598). No other line in T2 has Langlois making Moses Mesrop's nephew.
- **Correction 3** (`uncertain[6]`): justified, because Moses is held and tells the Georgian and Aghouank letters (T2 23913-23933). The wording needs one fix (FIX 6).
- **Quotations:** three quoted spans in the brief and three entries. Each `modern` matches the brief exactly. Each `printed` stands at T12 55853-55883, 55910-55912 and 55914-55916, and agrees with T2. The Armenian is not held, so no original is carried. None is under six words, so there is no "checked at card" entry and no `secondReading`. The T12 file is in `sources`.
- **Validator:** a scratch census with this card and the brief passes `tools/validate-census.mjs` (full quote check) with no `mesrop-mashtots` error. The open item in `Card_Edits.md`, that the vision quotation would need a footnote drop listed, did not show in this run.
- **New legacy and uncertain items:** each was read at its cited lines in T2, SYN16, SYN5 and KART, and each is supported, except the one in FIX 7.
- **Keys:** allowed. No audit is named. Spelling is American.
- **Not found:** none listed, and none found.

## FIX

1. `briefReferences[0]`. The brief no longer tells Vartan, Daron or the archives. Fresh read cut them.
   - Old: "Koriun, Life of Mesrop, tr. J.-Raphaël Emine: the son of Vartan from Daron, the royal archives, his turning to the monk's life; Koriun's word that he wrote of men he saw with his own eyes."
   - New: "Koriun, Life of Mesrop, tr. J.-Raphaël Emine: Greek learned as a boy, the king's decrees, his turning to the monk's life, with herbs and the bare ground; Koriun's word that he wrote of men he saw with his own eyes."
2. `briefReferences[2]`. The brief does not name Daniel.
   - Old: "the Syrian bishop Daniel's letters fail"
   - New: "a Syrian bishop's letters fail"
3. `briefReferences[9]`. The brief does not tell Moses's letters of Sahak and the emperor. It does tell that Moses was a pupil by his own account (T2 24738-24740).
   - Old: "Moses of Khoren, History of Armenia III: the Roman-side letters of Sahak and the emperor, and the first refusal of the letters."
   - New: "Moses of Khoren, History of Armenia III: the first refusal of the letters on the Roman side; his own account of being a pupil of Sahak and Mesrop."
4. `briefReferences[10]`. The brief does not tell Lazar's Syriac services, his schools, or his pointer to Koriun's Life. It does tell that Lazar credits the translating to Sahak.
   - Old: "Lazar of Pharp, History of Armenia: the Syriac services the people could not follow; the schools, copyists and crowded churches; Koriun's Life as the place to learn how the letters were found."
   - New: "Lazar of Pharp, History of Armenia: the translating given to Sahak; the copyists and crowded churches."
5. `briefReferences[11]` and `[12]`. The brief does not name Pharnavaz, and the feast went to the card (Outline, Cut first 7).
   - Old: "Georgian chronicle, tr. Brosset: Georgia's script given to an early king, Pharnavaz."
   - New: "Georgian chronicle, tr. Brosset: Georgia's script given to an ancient king."
   - Old: "Armenian Synaxary of Ter Israel, tr. G. Bayan: Sahak with Mesrob as makers of the letters, and the feast of the Armenian Translators."
   - New: "Armenian Synaxary of Ter Israel, tr. G. Bayan: Sahak with Mesrob as makers of the letters."
6. `uncertain[6]`. Moses does not say "renewed" for the Aghouank. He says Mesrob "créa les caractères" (T2 23930-23931).
   - Old: "That Mesrop gave the Georgians an alphabet and renewed that of the Aghouank rests on Koriun here and, later, on Moses of Khoren."
   - New: "That Mesrop gave the Georgians an alphabet and renewed that of the Aghouank rests on Koriun here; Moses of Khoren later has him make letters for both."
7. `legacy.remembered[2]`. Koriun says he came down when told of something useful to do in the lands he had taught (T2 4005-4011). Koriun does not say "to teach".
   - Old: "coming down only when he was needed to teach."
   - New: "coming down only when he was needed in the lands he had taught."

## Second pass check (2026-11-23)

**Verdict: FIX** (two changes, below). T12 = `cic/texts/langlois_collection-historiens-armenie-tomes1-2-fra_1867-1869.txt`.

### What holds

- **The checker's changes.** A diff of the card at `cd102480` against the card now shows all seven changes word for word, and nothing else in those fields moved. The only other differences are the two new `uncertain` items.
- **Outline items "to the card".** Each is held: the French translation only (`uncertain[0]`); the "justly inflicted on the body" line (`uncertain[10]`); the two dates of death (`uncertain[2]`) and the Julian equivalents (the new last item); the burial dispute and Vahan's church (`uncertain[14]`, `legacy.traces[5]`); the hermit years and talks for the simplest people (`legacy.remembered[2]`, `uncertain[8]`); civil and military affairs (`legacy.remembered[2]`); Samos and Samosata (`uncertain[4]`); "Mesrobian letters" (`legacy.traces[2]`); the feast of the Translators (`legacy.remembered[3]`); Daron from the fresh read (`placeNote`); Moses's letters (the new item). The skip of D11 holds: the outline gives it to the Koriun story, not the card.
- **Scan readings to add.** None given, none listed.
- **Keys, spelling, audit.** No new key. The new items use American spelling. No audit is named.

### FIX

1. `uncertain[15]`. Moses gives five letters, not four: Atticus's answer to Sahak follows Theodosius's (T2 24338-24372). The text says Mesrop and Vartan carry Sahak's letters (T2 24196-24197, 24254-24255, 24270-24271) and come back with the emperor's (T2 24291-24292); it does not say who carried Atticus's.
   - Old: "Moses of Khoren gives the full texts of four letters: Sahak to the emperor Theodosius, Sahak to Atticus, the bishop of the capital, Sahak to the general Anatole, and Theodosius's answer to Sahak. Mesrop and Sahak's nephew Vartan carry them."
   - New: "Moses of Khoren gives the full texts of five letters: Sahak to the emperor Theodosius, Sahak to Atticus, the bishop of the capital, Sahak to the general Anatole, and the answers of Theodosius and of Atticus to Sahak. Mesrop and Sahak's nephew Vartan carry Sahak's letters and bring back the emperor's."
2. `uncertain[16]`. The "12 February" is a scan fault. T2 37889 prints "au la février"; the second scan of the same print reads "au 19 février de" 441 (T12 89832-89833), as the note to Moses does (T2 25380-25381; T12 77528-77529). Both notes give 19 February 441. The source sheet's D1 carries the same misreading.
   - Old: "The notes in Langlois's edition turn the thirteenth into 19 February 441 in one place and 12 February 441 in another."
   - New: "The notes in Langlois's edition, to Moses and to Lazar, both turn the thirteenth into 19 February 441."


Coordinator (2026-11-23): both second pass check fixes applied word for word.
