# Card check 2: Syriac Christianity (`syriac-edessa-nisibis`, tradition)

Checked `syriac-edessa-nisibis.card.json`, `Card_Edits.md` (with its "Changes after the grade fixes"), the entry fields in it, and `Entry_Texts.md`. I checked them against the final brief (`syriac-edessa-nisibis.brief.txt`, after `Grade2_Fixes_Applied.md` and `Grade3_Fixes_Applied.md`), `Outline.md`, `Source_Sheet.md`, `Review.md`, `Card.existing.json` and the first `Card_Check.md`. There is no `Fresh_Read.md`. I re-opened every line the card cites in `cic/texts/`. Nothing else was edited. Nothing was committed.

## Verdict: FIX

There are two card fixes (both in `briefReferences`) and six entry-text fixes. Everything else passes.

## What passes

- **The first check's corrections are all applied.** Fix 1 (`voices[6]`, the 341/344 sentence removed), fix 2 (`legacy` paragraph 2 ends at "with the change."), fix 3 (the Diatessaron note), fix 4 (the Pearl note, `npnf213` 21795, "mysteries pertaining to the Kingdom") and fix 5 (Brock `year` "1992" in edit 14) are all in place. Rabbula's years are off Not found.
- **Nothing else moved.** A key-by-key diff against `Card.existing.json` shows only the fields `Card_Edits.md` lists: `voices[2]`, `[4]`, `[5]` and `[6]`, `legacy`, the source notes and `file` keys, the nine added and three removed sources, and the three new keys. Key order is kept.
- **The card matches the final brief.** The grade fixes changed no quoted span. All five `quotationOriginals` `modern` texts match the final brief exactly. Each `printed` stands verbatim at its lines: `npnf213` 25950-25953 and 13733-13734, Mitchell 1205 (twice), and Chabot 16165-16166. "prays with Satan." (`"checked at card"`) matches Mitchell's "he who prays with the Manichaeans prays with Satan". The four spans of six words or more carry no `secondReading`.
- **The envoy additions hold.** The brief's "a bishop who made peace between East and West" stands on Chabot 16229-16230 ("médiateur de la paix et de la concorde entre l'Orient et l'Occident"). The Socrates VII.8 source, the synod `briefReferences` line (16168-16169, 16227-16230, 16236-16237; 16226 is blank) and the new last `uncertain` item all stand at their lines (19135-19141, 19174-19176).
- **Every other cited line was re-read and holds.** These include Chronicle 53, 59, 77, 103, 145, 161, 251-253, 272 and 368; Theodoret 11065-11067 and 11124-11177; Ephrem's hymns at 13710-13715, 13746-13751, 13839-13840 and 14774-14787; Aphrahat at 25803-25808, 25835-25846, 27416-27419, 27988-27991, 28517-28519 and 28554-28561; Parisot at 3291-3293, 18124-18134 and 21939-21942; and Mitchell at 431, 584, 606-608, 640, 917 and 1605-1609. Also re-read: Sozomen 28873-28877, 28889-28899, 29190-29196, 32050-32054 and 32085-32103; Socrates 11679-11697; Addai 65 and 219; Eusebius 26368, 26424-26433 and 26479; `anf02` 7460; Palladius 471; Barhadbeshabba 20435-20438; Chabot 16155-16166, 16179-16180, 16410-16417, 16422, 16499-16500, 16519-16534, 17714-17746 and 17856-17861; and John of Ephesus 14152.
  - One range in `Card_Edits.md` (not on the card) is off. The king's own words in Braun stand at 1575-1578, not 1571-1575. The card's `uncertain` item gives no line, so the card needs no change.
- **Census.** I made a scratch copy outside the repository. It has the card fields, `why`, `relationsSummary`, `modernWorks` (Brock 1992) and the final brief as `longDescription`. `node tools/validate-census.mjs <copy>` gives 0 errors and 4 warnings, the same shortName warnings as before.
- **Entry fields.** `why`, `relationsSummary` and `modernWorks` (edits 13-15) pass.

## Fixes: the card

**1. `briefReferences[6]`: remove a reference the brief no longer tells.** Sozomen's account of the hymns written in Bardaisan's son's meters went to Leave out (outline Cut first 5). The brief tells only that "the Syrians went on singing his hymns", and `briefReferences[7]` already cites that (32101-32103).
- Old: " Sozomen III.16 (lines 32085-32103): Bardaisan's son's songs and Ephrem's hymns in the same meters."
- New: "" (delete, with its leading space).

**2. `briefReferences[8]`: an item the outline sends to the card is missing.** Cut first 15 sends the envoy's place at the synod to the card ("Only his place at the synod goes to the card"). The card gives his part in the grant, but not his part at the synod. The acts have the king order Isaac and his brother Marutha to gather the bishops in the great church (16413-16417; "église" falls on 16417). They also have Marutha sign second, before Hosea (17859).
- Old: "the bishops gathered in the great church of the capital (lines 16410-16416)"
- New: "the bishops gathered in the great church of the capital, where the king ordered Mar Isaac and the bishop Marutha to bring them together (lines 16410-16417)"
- Old: "Hosea of Nisibis, second metropolitan (line 17746) and third to sign (lines 17856-17861)"
- New: "Hosea of Nisibis, second metropolitan (line 17746) and third to sign, after Isaac and Marutha (lines 17856-17861)"

## Fixes: `Entry_Texts.md`

I checked every claim against the brief, the outline and the sheet. Every claim is held by the brief. The fixes below are for Part 1 of the kit and for one date clash. The representative frame ("Mar Yausep is a representative voice for the Christian tradition of Edessa and Nisibis") is kept. I re-scored my new texts with `python -m engine.m1.profile_readability` on scratch copies: the tile is grade 9.7, ease 70.4, a pass; the summary is grade 8.7, ease 71.4, a pass.

**3. `tile`: give the witness by role.** Sozomen is named bare. He does not act in the story and gets no gloss here. The brief glosses him as a Greek church historian of the next century (Part 1: give anyone else by role; name the witness who wrote long after).
- Old: "There, Sozomen says, the king believed"
- New: "There, a later Greek church historian says, the king believed"

**4. `tile`: give the reason for 363.** The handover is an act of the war, and the brief gives its reason. The outline also lists "363, with why" under Never cut.
- Old: "In 363 Rome handed Nisibis to Persia, and Ephrem moved to Edessa."
- New: "In 363, to save its starving army inside Persia, Rome handed Nisibis to Persia, and Ephrem moved to Edessa."

**5. `tile`: say it was prose.** The answer to the rivals comes right after Ephrem's hymns, so a reader takes it to be in hymns. Do not say bars "Ephrem answered all three in hymns". The brief has "In prose".
- Old: "He answered three rival teachers by name,"
- New: "In prose, he answered three rival teachers by name,"

**6. `summary`.** Four problems:
- "Ephrem" stands with no word of who he was.
- The answer to the rivals reads as hymns (as fix 5).
- Sozomen is named bare (as fix 3).
- `recordHolds` names the daughters of the covenant, but the summary never gives that name.

The new text also stays under grade 10. A first try that kept everything in one sentence scored 10.4.
- Old: "From the flood of 201 to 410, Syriac-speaking Christians lived at Edessa and Nisibis, between the Roman and Persian empires. They sang their teaching in hymns, and some men and women vowed to live unmarried and holy for God. Ephrem answered rival teachers whose followers fasted as his people did but held another faith. In Persia, Sozomen says, the king believed a charge that their bishop was a friend of the Roman emperor, and had their priests killed. In 410, forty bishops of the Persian church met to set its rules."
- New: "From the flood of 201 to 410, Syriac-speaking Christians lived at Edessa and Nisibis, between the Roman and Persian empires. They sang their teaching in hymns, and some men and women vowed to live unmarried and holy for God: the sons and daughters of the covenant. Ephrem taught in hymns at Nisibis. In prose, he answered rival teachers whose followers fasted as his people did but held another faith. In Persia, a later Greek church historian says, the king believed a charge that their bishop was a friend of the Roman emperor, and had their priests killed. In 410, forty bishops of the Persian church met to set its rules."

**7. `recordHolds`: keep to what the sheet holds.** The sheet (E2) says that no word written by a daughter of the covenant "survives in the Library". The new text says that no word survives anywhere, which is wider than the sheet. This field is about what the record holds, so it should say so.
- Old: "Rich in hymns and letters. Thin on ordinary believers, and no word written by a daughter of the covenant survives."
- New: "Rich in hymns and letters. Thin on ordinary believers, and it holds no word written by a daughter of the covenant."

**8. `intro`: the date must match the entry.** The entry's own `dates` and `start` stay "200–410 CE" and 200. Neither the card nor the entry-field list changes them. With "201–410 CE", the same entry would show two different start years. The flood of 201 is still told in the tile and the summary.
- Old: "Mar Yausep is a representative voice for the Christian tradition of Edessa and Nisibis (201–410 CE). They sang their teaching in hymns."
- New: "Mar Yausep is a representative voice for the Christian tradition of Edessa and Nisibis (200–410 CE). They sang their teaching in hymns."

## Not found, and left in

The not-found list in `Card_Edits.md` is accurate. Three unsourced items are still on the card as not found: the Peshitta clause, "from about 309", and "between 336 and 345". None is clearly contradicted by a held line, so under the role each stays in place as not found.
