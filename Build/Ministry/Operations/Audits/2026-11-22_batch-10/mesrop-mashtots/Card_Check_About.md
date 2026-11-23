# Card check, third pass (what it was about): Mesrop Mashtots

**PASS.**

Checked `mesrop-mashtots.card.json` against `Card.pass2.json`, the section "Third pass: what it was about (2026-11-23)" of `Card_Edits.md`, and `mesrop-mashtots.brief.txt` as it now stands. T2 = `cic/texts/langlois_collection-historiens-armenie-tome2-fra_1869.txt`.

## 1. Each edit against its evidence (every cited line opened)

- `briefReferences`, Moses entry (emperor's letter): T2 24310-24325 reads the reproach for devotion "à un roi païen" and for turning "à certains Syriens", "dédaignant les savants qui sont dans notre ville". Brief paragraph 7, last sentence, tells it. Justified.
- `briefReferences`, "he does not say what the Borborites taught": T2 3779-3787 gives no teaching. Brief: "Koriun never says what they taught." Justified.
- `briefReferences`, Koriun/Cyril/Nestorius entry: T2 4098-4101 ("des livres conformes aux hérésies de Paul de Samosate et de Nestorius"); CYR 5241-5244 ("nearly the whole contest ... on our affirming that the holy Virgin is Mother of God"); NES 6953-6958 ("When you call her the Mother of Christ ... a word which is useful toward agreement", Nestorius telling his own counsel, context 6927-6947). Brief paragraph 9, last two sentences. Justified; no quotation marks used.
- `sources.about`, four files added (Augustine, Marutha, Cyril, Nestorius): each file exists and is the one cited by a new field. Justified.
- `uncertain[17]`, Borborites: AUG 1257-1259 ("nonnulli eos etiam Borboritas vocant, quasi coenosos, propter nimiam turpitudinem quam in suis mysteriis exercere dicuntur") matches the card's English; MAR 3563-3567 matches "immorality and great licentiousness ... refuses to report", with the translator's bracketed "[Obscönitäten]" and "Blut [von Kindern]" not used; T2 3814-3816 is Langlois's note ("Secte gnostique qui parut au deuxième siècle et qui niait le Jugement dernier"), credited as his. Link rated Inferential-Thin, charges credited to their writers. Justified, and matches Outline item 8's instruction to the card.
- `uncertain[18]`, "Théodore", Paul of Samosata and Nestorius: T2 4098-4101. The bracket "[de Mopsueste]" stays only in `uncertain[5]`, where it is credited as the bracket's. Justified, per Outline item 9.
- `legacy.traces`, new last (canons of Nicaea and Ephesus): T2 3855-3860 ("copies authentiques des Saintes-Écritures, des écrits ... des patriarches (c'est-à-dire des pères de l'Église), et des canons des saints conciles de Nicée et d'Éphèse"). Justified.
- `legacy.remembered`, preacher and vartapets: T2 3722-3726 ("le patriarche qui conféra à Mesrob [le titre de] prédicateur (égégbésigdîgos) ... le fit ranger parmi les plus illustres et bienheureux vartahed"). The cited range 3716-3722 stops one line short of the rank (3725-3726); the claim is supported. Justified.
- `legacy.remembered`, defenders of the true faith: T2 4105-4106 ("Sahag et Mesrob, défenseurs de la vraie foi"). Justified.
- `briefReferences` removals and trims ([0], [1], [5], [7], [8] of the starting card): none of the removed words is told in the brief now (no Greek as a boy, no king's decrees, no "even more eager", no preacher title, no canons, no New City). Justified.

## 2. Nothing else moved

Field by field against `Card.pass2.json`: only `legacy`, `uncertain`, `sources` and `briefReferences` differ, and every difference is one listed in `Card_Edits.md`. `otherNames`, `knownFor`, `datesNote`, `placeNote`, `role` and `quotationOriginals` are word for word.

## 3. `briefReferences` against the brief

Every remaining entry names something the brief still tells.

## 4. Census rules

- Keys: the same ten as the starting card. A scratch census with this card in place passes `node tools/validate-census.mjs` with full quotation checking: 0 errors.
- `quotationOriginals`: the brief quotes three spans ("At once he saw them ... writing on stone.", "They rejoiced over them as if they were the divine Tablets,", "Mesrop gathered children ... long breath,"). There are three entries, each `modern` matching the brief and each `printed` verbatim at its lines in the tomes 1-2 file (55853-55883, 55910-55912, 55914-55916). None is under six words.
- Every cited file is in `sources`. No audit file, review or ruling is named. Spelling is American outside the printed French.

## 5. "checked at card"

None.

## 6. Not found / clearly wrong

Nothing is listed as not found. Nothing clearly wrong was left in.

## 7. Census entry

None for this pass.
