# Priscillian: card edits

Existing card kept word for word. Nothing was corrected: every existing statement was checked against its file and none is contradicted by a held source or by the brief. Checked by `node tools/validate-census.mjs --skip-quotes` on a scratch census (the full check is killed for memory in this session); the only errors are the three `secondReading` gaps, which release sets. The card's new quoted spans were checked by hand against the cited files with the validator's fold, and all stand.

Not added, by rule: `briefLength` (not an allowed key); `secondReading` (all three quotations are six words or more); connections to other entries.

## New: legacy.traces (4 added)

1. Toledo, about 400: clergy of Herenas call him catholic and a holy martyr. Evidence: Mansi3 96553-96555 (era 438), 96780-96784. The brief: "Fifteen years later, Spanish bishops at Toledo..."
2. Sulpicius on Ithacius and Ydacius. Evidence: SulpE 11713-11722. The brief: "Ithacius lost his bishopric."
3. Leo, 447, "by the sword of the public laws"; the severity line (cut from the brief). Evidence: Leo 3224, 3273-3286.
4. Law of 407. Evidence: CTh 87374-87380. Cut from the brief; sent to the card by the outline.

## New: uncertain (11 added)

1. Year: 385 (Richardson, JerVir 41626), 386 (JerEp 2970), Hydatius later (Hyd 1143, Mommsen's margin 387). The brief: "In about 385".
2. First execution, Jackson's note (JerVir file 16390-16391), Fremantle's table (JerEp 2970), Bernays as Hefele reports it (Hef2 23503-23512), "evil conduct" (SulpE 11667-11668). Batch ruling item 5.
3. Roberts against Halm: "as long as Martin survived" (SulpE 11660), "between them and our friends" (SulpE 11728-11729), Latin SulpL 5907-5908 and 6003-6004; Hydatius on Martin (Hyd 1136-1137). The brief: "While Martin was in Trier"; "the other side".
4. Date of the Chronicle: inference from "fifteen years" (SulpE 11729-11731). The brief: "writing some years after the deaths".
5. Ithacius and Ursacius cut off, 389 (Pros 53318-53319), against Sulpicius (SulpE 11713-11722). Cut from the brief.
6. Euchrotia: SulpE 11554-11555, 11691-11692; Pros 53288-53290. The brief: "a woman who had sheltered them" (see note below).
7. Marcus of Memphis, the oath, Ydacius, bribery, and Priscillian's account of the rescript (SulpE 11458-11463, 11487-11495, 11564-11575; Pr 4636-4638, 4655-4657). Cut or left out of the brief.
8. The curses with the sword in the Liber apologeticus (Pr 2797, 3746-3748, 3831-3836), with Schepss's attribution (Pr 80-93). Outline, Leave out.
9. Jerome's later letter (JerEp 27806-27807) and Augustine (AugE 39221-39225). Outline, Leave out.
10. Toledo professions and the editor's doubt (Mansi3 96692-96698, 96618-96620). Outline, Leave out.
11. Ambrose at second hand (Mansi3 83136-83141). Outline, Leave out.

## New: sources.about (9 added)

Leo (npnf212); Jackson's note to Theodoret (npnf203, already cited for Jerome); Fremantle's Jerome (npnf206); Augustine, Against Lying (npnf103); Hydatius; Prosper; Mansi, Toledo; Theodosian Code; Hefele v2.

## New: briefReferences (9)

Tractate II; Schepss's preface; Sulpicius II.46-51; Hefele on Bernays; Toledo; Leo; Braga; Jerome ch. 121; the census tradition. No quotation marks.

## New: quotationOriginals (3, one for each quoted span)

1. "No one should be forbidden..." Pr 4415-4417. Printed wording is the scan as it stands ("nee", "T)us", "aiiima"). Schepss's print is the only one held and no second print confirms it, so no `original` is given. No English print exists, so `printed` carries the scan and `uncertain` names its faults.
2. "My own view is that the accused..." printed in Roberts's English alone (SulpE 11642-11643). Halm's Latin (SulpL 5890-5891) is in a damaged scan ("senteatia", "dispUcere"), and a translation does not confirm its spelling, so it is not printed as an original.
3. "Even the rulers of the world..." Feltoe, Leo 3276-3278. The Latin is not held.

## Corrections: none

## Claims not found: none

## For the coordinator

- Quotation 1: if the page image or another print is later held, the Latin can go in as `original`.
- The brief's "a woman who had sheltered them" is a little stronger than Roberts's "lingering ... in the territory of Euchrotia" (SulpE 11554-11555). The card states the source's words.
- Not carried: Sulpicius's talk about Procula (outline: card if anywhere; it is gossip he marks as such).

## Second pass (2026-11-23)

**Checker changes.** `Card_Check.md` is PASS and lists no change; nothing to apply.

**Added (1).**
- Field `uncertain`, appended last. Text: "Orosius, in his Commonitorium, says Priscillian held that the soul is caught by evil powers and put into bodies, and that for this reason astrology (mathesis) prevailed, and that Christ loosed this bond and nailed it to the cross by his passion. Orosius then quotes a letter of Priscillian's." Outline item: Leave out, "Orosius's report of his teaching on souls and the stars ... card". The souls half was held; the stars half was not. Evidence: Pr 10247-10260 (Latin: "Unde et mathesim praevalere firmabat, adserens quia hoc chirographum soluerit Christus et adfixerit cruci per passionem suam, sicut ipse Priscillianus in quadam epistula sua dicit"), re-read.

**Already held, skipped.**
- Jerome's entry and Augustine against his followers (Links, card only): `legacy.remembered`, `sources.about`, `uncertain` (Jerome ch. 121; Against Lying).
- Law of 407; Prosper's report of Ithacius and Ursacius cut off; the oath of the two bishops (Cut first 1-3): `legacy.traces`, `uncertain`.
- First-execution claim with Bernays; Marcus of Memphis genealogy; curse with the sword; Augustine's Against Lying; Ambrose in Mansi's note: `uncertain`.
- Jerome's change of tone between 392 and 414: both texts are held (`legacy.remembered`, `uncertain`); no held source states a change of tone or dates the letter, so a contrast would be our inference. Not added.
- Procula rumor ("card if anywhere", gossip Sulpicius marks as such): not added, as in the first pass.

**Validator** (`--skip-quotes`, scratch census, real census untouched). The census entry still holds the old brief text, so its quotation checks fail against it until release: three `secondReading` gaps (set at release), three `quotationOriginals` "not a quotation in the brief", and unmatched spans in the old text. No error comes from the new `uncertain` item.

## Third pass: what it was about (2026-11-23)

Written to `Card.pass2.json`, from `priscillian.card.json`; all else word for word. Quotations: the brief still quotes the same three spans, unchanged, so `quotationOriginals` is untouched.

**`briefReferences`**
1. Tractate II entry: "his reason for going to Rome." → "the order he says was asked against false bishops and Manichaeans; his reason for going to Rome, to clear his name." Evidence: brief ("They asked for it, Priscillian wrote, against false bishops and Mani's followers"; "went to Rome to clear his name"); Pr 4636-4638, 4672-4676, re-read.
2. Sulpicius entry: "the portrait, the belief" → "the charge of heresy, the belief". The brief no longer tells the portrait; it now says "accused him of heresy" and "condemned ... as a heretic" (SulpE 11502-11508).
3. Same entry: "Ithacius's loss of his bishopric." → "Ithacius's loss of his bishopric after he was attacked for taking the case to the courts." Evidence: brief sentence on Ithacius; SulpE 11714-11719, re-read.
4. Hefele entry: "glossed as sorcery." → "glossed as sorcery; and, as his own supposition, the Saragossa canons against Sunday fasting and women's gatherings." Evidence: brief ("a modern historian thinks"); Hef2 17955-17958, 18003-18020, re-read.
5. Leo entry: "the sword of the public laws." → "the sword of the public laws; his charge that the teaching put each life under demons and stars." Evidence: brief; Leo 3254-3259, re-read.
- Braga entry: already names the souls; unchanged. No other entry names a cut event ("Two bishops made him bishop of Abila" and the oaths were never listed; Abila stays in the brief's opening).

**`uncertain`** (new item inserted after the Saragossa item)
- New text: Priscillian's book says Hydatius gave the council a memorandum setting down a rule for living and none of his group was censured under it (Pr 4389-4391); Hefele, in Oxenham's English, supposes that eight canons of a Saragossa synod of 380 belong to this council because they are plainly directed against the Priscillianists, among them all Christian women avoiding conventicles and no one fasting on Sunday, and notes Mansi dates it to 379 (Hef2 17955-17958, 18003-18020). Outline item 4 (card), credited to Hefele; his supposition, not fact.

**Skipped**
- Sulpicius's genealogy from Marcus of Memphis and Orosius's soul and stars report (outline item 11): already in `uncertain` (second and last items); nothing to add.
- `sources.about`: the Hefele v2 file is already cited; no new file.
- `legacy`: nothing in this pass sends anything there.
- Pelagius files: none exist for this story.

**Validator** (`--skip-quotes`, scratch census copy, deleted): 0 errors for this entry; 4 warnings, none on it.

## Card check applied (2026-11-23)

`Card_Check_About.md` (FIX, one change), applied word for word: briefReferences, Sulpicius entry: "Halm's Latin: the charge of heresy," → "Halm's Latin: his wealth and learning, the charge of heresy,". Its note that the memorandum Latin begins at Pr 4388, not 4389, concerns this file's third-pass section only.

## Fourth pass: no modern opinion (2026-11-23)

Written to `priscillian.card.json`, from `Card.pass3.json` (the starting card, unchanged); all else word for word. The brief now quotes the same three spans with the same words, so `quotationOriginals` is untouched.

**`uncertain`**
1. Würzburg item, added after the Schepss judgment: "This is a modern judgment, his alone. In his preface he also writes that the judgment on Priscillian had hung on his enemies, chiefly Sulpicius, until the treatises turned up. Schepss attributes the Book to Damasus to Priscillian himself; the story says only that his party wrote it." Evidence: the brief's cut lines and "Priscillian's party"; Pr 80-84, 85-93 (preface), re-read.
2. Year item: "The story says in about 385." → "The story gives 385 by Prosper's chronicle, which names the consuls Arcadius and Bauto, and 387 by Hydatius's, which names Theodosius's ninth year; the Roman year in each is an editor's margin." Evidence: the brief ("385 by one old chronicle and 387 by another"); Pros 53277, 53284-53287; Hyd 1143-1145, re-read.
- Hefele's Saragossa supposition and Bernays's gloss: already in `uncertain`, credited by name as his supposition and view; nothing to add.

**`briefReferences`**
3. Tractate II entry: "why he and his friends gave themselves" → "why his party gave themselves"; "his creed and his curse" → "their creed and their curse"; "what he says of Saragossa" → "what the book says of Saragossa"; "the order he says was asked" → "the order it says was asked"; "his reason for going to Rome, to clear his name." → "the party's reason for going to Rome; the bishop of Emerita and the council at Saragossa it names, which Sulpicius names too."; and "(a book of Priscillian's party, not shown to be his own)" after the call. Evidence: brief paragraphs 1, 4, 5, 6 and 11; Pr 4334, 4347, 4363-4365, 4382-4392, 4394, 4635-4638, 4672-4677; SulpE 11492, 11502-11508, 11546-11548, 11530-11531, re-read.
4. Schepss entry: "the eleven unsigned treatises found at Würzburg in 1885, and his judgment that they could be no one's but Priscillian's." → "the eleven unsigned treatises found at Würzburg in 1885." Evidence: brief last paragraph; Pr 80-89.
5. Sulpicius entry: "Gratian's order" → "the emperor's order won by the bishop of Emerita"; "the prefect's two hearings and their findings" → "the prefect's two hearings, the finding of sorcery (maleficium) and the court's findings". Evidence: brief ("The bishop of Emerita won an order from the emperor"; "guilty of sorcery"); SulpE 11530-11531; SulpL 5772, 5913-5914.
6. Hefele entry (Bernays's gloss; the Saragossa canons): removed. The brief tells neither now (sorcery rests on Sulpicius's maleficium). The file stays in `sources.about`, used by `uncertain`.
7. Toledo entry: added "and the council's own date, Spanish era 438, which gives 400." Evidence: brief ("In 400"); Mansi3 96555, 96780-96781.
8. Jerome entry: ", and the dating note" removed; the brief no longer tells Jerome's date.
9. New entry after Jerome: Prosper and Hydatius chronicles, for the two years and for "sixty years on" (Hydatius's 387 and Leo's writings sent to Spain in 447). Evidence: brief; Pros 53277-53287; Hyd 1143-1145, 1916-1918. Both files are already in `sources.about`.

**Not changed, listed:** `uncertain` items and `keyWorks` that say "Priscillian, in his book to Damasus", and the Tractate II title, still carry Schepss's attribution as the earlier card has it; kept word for word as outside this pass, and the new Würzburg sentence records it as his judgment.

**Validator** (`--skip-quotes`, scratch census copy with this card and brief in place, real census untouched): 0 errors; 4 warnings, none on this entry.

## Release fix (2026-11-23)

The census validator read the new Prosper and Hydatius entry's quoted "sixty years on" (the brief's own words) as a source quotation not held in its cited files. The coordinator reworded the end of that `briefReferences` entry, in the card and the census: `, for \"sixty years on\".` → `, for the interval the story gives as sixty years.` No quotation marks; the entry's claim is unchanged.
