# Card edits: Mesrop Mashtots

Card written to `mesrop-mashtots.card.json`. T2 = `cic/texts/langlois_collection-historiens-armenie-tome2-fra_1869.txt`; T12 = `cic/texts/langlois_collection-historiens-armenie-tomes1-2-fra_1867-1869.txt`.

## Corrections (clearly wrong)

1. `legacy.traces[0]`
   - Old: "...to Edessa and Constantinople."
   - New: "...to Edessa, and from there to Constantinople."
   - Evidence: T2 3805-3830 (sent to Edessa; "Puis ils passèrent dans le pays des Grecs, à Byzance"); the brief ("sent pupils to Edessa... from there they went to Constantinople").
2. `legacy.remembered[0]`
   - Old: "whom Langlois takes for Mesrop's nephew and pupil"
   - New: "whom the editor of the Armenian text, as Langlois reports, takes for Mesrop's nephew and pupil"
   - Evidence: T2 4455-4465 ("Le savant éditeur du texte... Il ajoute que, parmi les disciples de Mesrob, il n'y a guère que Moïse de Khorène, son neveu"). The view is the Armenian editor's, which Langlois reports; no Langlois line takes it as his own (grep of T2 for neveu/disciple de Mesrob).
3. `uncertain[6]` (the Georgian and Aghouank letters)
   - Old: "...rests on Koriun here."
   - New: "...rests on Koriun here and, later, on Moses of Khoren."
   - Evidence: T2 23913-23933 (Moses: Mesrob composed an alphabet for the Iberians; created the Aghouank letters). The card holds Moses, so "Koriun" alone is contradicted by a held source.

## New: quotations (`quotationOriginals`, three entries, one per quoted span in the brief)

All three print from T12, the cleaner scan of the same print. T2 has scan faults in each ("Anssitât", "c'eÀt été"). Original Armenian not held. No `secondReading` on any entry (all are six words or more).

- Vision: lines 55853-55883. T2 3590-3594, 3620-3621 agrees.
- Tablets: lines 55910-55912. T2 3647-3648 agrees.
- Children: lines 55914-55916. T2 3651-3653 agrees.

## New: sources (`sources.about`, four entries added)

T12 (second scan of Koriun's Life, the file the quotations print from); Armenian Synaxary of Ter Israel, Navasard (the chronicle-of-seert file, PO 5); the same Synaxary, Tré (PO 16); Georgian chronicle with Brosset's notes (KART).

## New: from the outline's "to the card" and "for the card" lists, and from the brief

- `legacy.traces`
  - Lazar: Syriac services the people could not follow (T2 36232-36240); translating given to Sahak; schools, copyists, crowded churches (T2 36473-36496).
  - Moses: Sahak and Mesrop sent him to Alexandria (T2 24738-24740).
  - Koriun: Hemayak and Vahan carry the body to Oshakan, and Vahan builds a church three months later (T2 4262-4312).
- `legacy.remembered`
  - Koriun: learned in civil and military affairs, liked by great and small (T2 3446-3450); lived in caves on herbs, coming down when needed (T2 3954-4011).
  - Synaxary: feast of the Armenian Translators, 25 November (PO 16 file line 6239); Isaac (Sahak) made the letters with the vardapet Mesrob (PO 5 file lines 28862-28866).
- `uncertain`
  - Moses's harder welcome on the Roman side, and his date disputed (T2 24206-24213, 24315-24323; census note on Moses's date).
  - The Borborite punishments in the passive, Armenian not held, and Moses's order for punishment (T2 3779-3787, 24418-24424).
  - The Georgian chronicle's rival claim for Pharnavaz and Brosset's notes (KART 2224-2230, 2263, 7036-7040; the file's header warns the scan is a poor second witness, so nothing is quoted).
  - Who translated: Koriun, Lazar, the Synaxary (T2 3634-3641, 3865-3877, 36473-36488; PO 16 file lines 6297-6301).
  - Mesrop and the see after Sahak (T2 4272-4276 editor's note; T2 25374-25392 Moses).
  - The three-way quarrel over his burial (T2 25356-25370).
- `briefReferences`: fourteen entries, no quotation marks.

## Not added

The two Julian equivalents of the death day (already covered by the two death dates in the card), the full texts of Moses's letters, the demons of Koghten, and Moses's Edessa journey were left out.

## Claims not found

None. Every existing claim was checked and found supported except the three corrected above.

## Open item

The validator reports `secondReading` missing on all three entries, as expected (release sets it). The vision quotation's French is broken by a page of footnotes at T12 55858-55882; the validator fails on `printed` until `tools/quote_scan_readings.json` lists that range as a footnote drop. Tested on a scratch copy: with the drop listed, only the `secondReading` errors remain.

## Second pass (2026-11-23)

T2 = `cic/texts/langlois_collection-historiens-armenie-tome2-fra_1869.txt`.

### The checker's changes

All seven applied word for word, each old text found once: `briefReferences[0]`, `[2]`, `[9]`, `[10]`, `[11]`, `[12]`; `uncertain[6]`; `legacy.remembered[2]`.

### Scan readings to add

None listed by the checker.

### Items added

- `uncertain` (new last item): "Moses of Khoren gives the full texts of four letters: Sahak to the emperor Theodosius, Sahak to Atticus, the bishop of the capital, Sahak to the general Anatole, and Theodosius's answer to Sahak. Mesrop and Sahak's nephew Vartan carry them."
  - Evidence: T2 24200-24225 (to Theodosius), 24250-24262 (to Atticus), 24266-24280 (to Anatole), 24294-24325 (Theodosius). Outline, Leave out: "for the card".
- `uncertain` (new last item): "Koriun's French gives the death on the eighteenth of méhégan, and Moses of Khoren and Lazar of Pharp the thirteenth. The notes in Langlois's edition turn the thirteenth into 19 February 441 in one place and 12 February 441 in another."
  - Evidence: T2 4213-4216; 25335; 25380-25381 (19 February 441); 37889-37890 (12 February 441). Outline, Leave out: the editors' equivalents "for the card".

### Skipped

- French translation only: `uncertain[0]` holds it.
- The punishment "justly inflicted on the body": `uncertain[10]` holds it.
- The burial dispute and Vahan's church at Oshakan: `uncertain[14]` and `legacy.traces[5]` hold them.
- The two dates of death: `uncertain[2]` holds them.
- Hermit years, "learned in civil and military affairs": `legacy.remembered[2]` holds them.
- Samos and Samosata: `uncertain[4]` holds it.
- "Mesrobian letters" and the feast of the Translators: `legacy.traces[2]` and `legacy.remembered[3]` hold them.
- Daron (fresh read): `placeNote` already names Daron. The held scan prints the canton as "Baron" (T2 3440), so no further line was added.
- Who asked Koriun to write (D11): the outline sends it to the Koriun story. Mesrop's term at the head of the see: `uncertain[13]` holds it.
- Validator, scratch census, `--skip-quotes`: four errors for this entry. Three are `secondReading` missing (set at release); one is `printed` of quotationOriginals[0] not standing at T12 55853-55883 (footnote page, the open item above).

## Third pass: what it was about (2026-11-23)

T2 = `cic/texts/langlois_collection-historiens-armenie-tome2-fra_1869.txt`. Starting card kept unchanged as `Card.pass2.json`. Validator (scratch census, `--skip-quotes`): 0 errors for this entry.

### New explanations (`briefReferences`)

- New entry after the Moses refusal entry: "Moses of Khoren: in the emperor's letter he gives, Sahak is blamed for serving a pagan king and for turning to Syrians, not to Constantinople's scholars." Evidence: T2 24310-24319 (the emperor's reproach); brief sentence "In the emperor's letter Moses gives, Sahak is blamed ...".
- New entry after the Borborites entry: "Koriun: he does not say what the Borborites taught." Evidence: T2 3779-3787 (no teaching given); brief sentence "Koriun never says what they taught."
- New entry after the Ephesus entry: "Koriun, Cyril of Alexandria and Nestorius: the man the council of Ephesus shut out had books that, by Koriun's word, followed Nestorius; that council's quarrel turned on whether Mary could be called Mother of God, by Cyril's account, and Nestorius urged Mother of Christ instead." Evidence: T2 4098-4101; CYR 5241-5244; NES 6953-6958; brief's last two sentences of that paragraph.
- `sources.about`, four files added: Augustine (`cic/texts/augustine_arian-sermon-collatio-maximinum-pl42-lat_migne1886.txt`), Marutha (`cic/texts/maruta-of-maipherqat_de-sancta-nicaena-synodo-syrische-texte-deu_braun1898.txt`), Cyril (`cic/texts/cyril-alexandria_three-epistles-grc-eng_pusey1872.txt`), Nestorius (`cic/texts/nestorius_bazaar-of-heracleides_driver-hodgson1925.txt`).

### Items sent to the card

- `uncertain`, new: the Borborites. Koriun does not say what they taught; Augustine's charge (some call the Gnostics Borborites, for foulness in their mysteries; AUG 1257-1259), Marutha's (immorality and licentiousness, he refuses to say more; MAR 3563-3567), credited as those writers' charges; link to Koriun's sect on the name only, Inferential-Thin; Langlois's note (T2 3814-3816) credited as the editor's. The translator's brackets in MAR are not used.
- `uncertain`, new: Koriun's French names the man shut out "Théodore", books after the heresies of Paul of Samosata and of Nestorius. Evidence: T2 4098-4101.
- `legacy.traces`, new last: the canons of Nicaea and Ephesus brought home by the pupils. Evidence: T2 3855-3860.
- `legacy.remembered`, new: the patriarch gives Mesrop the title of preacher and ranks him among the most illustrious vartapets. Evidence: T2 3716-3722.
- `legacy.remembered`, new: Koriun calls Sahak and Mesrop defenders of the true faith. Evidence: T2 4105-4106.

### Removed from `briefReferences` (no longer told)

- [0] "Greek learned as a boy, the king's decrees, " removed.
- [1] ", and Sahak found even more eager" removed.
- [5] "the bishop names Mesrop a preacher, " removed.
- [7] " and the canons of Nicaea and Ephesus," → ",".
- [8] "illness and death in the New City" → "illness and death".

### Quotations

Unchanged: the brief still quotes the same three spans with the same renderings; `quotationOriginals` kept, three entries, each `secondReading` as it stood.

### Skipped

- Mesrop going to Sahak about letters (outline item 13): marked leave out, no card home.
- Place of death (New City): already in `placeNote` and `uncertain[2]`.
- Samos/Samosata, "Mesrobian letters", the Synaxary feast: already on the card.
- Fresh read applied file: no card corrections listed.
