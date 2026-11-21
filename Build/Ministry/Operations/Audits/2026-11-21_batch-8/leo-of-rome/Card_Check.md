# Card check: Leo of Rome

Card checker, batch 8 (2026-11-21), under `Card_Check_Prompt.md`. I wrote neither the card nor the brief. Read: `leo-of-rome.brief.txt` (and `brief.v1.txt`), `leo-of-rome.card.json`, `Card_Edits.md`, the starting card (`Card.existing.json`, which matches the census entry's `card` exactly), and each cited line in its file. The validator was not run.

**Verdict: PASS.**

## 1. Each edit is justified

`Card_Edits.md` lists no corrections and only additions. Re-read at the cited lines and confirmed:
- `legacy.traces[3]`: LEO 13464-13468 (Sermon III, Peter recognized and honored in his humble person). `[4]`-`[5]`: LEO 813-821, NC 22405-22436 (Anatolius; the Illyrian bishops; Florence; the Lateran, 1215). `[6]`: LEO 912-914 (saint, confessor, doctor since 1754, 18 February and 11 April); "writing in 1895" is the edition's year (Sheet, file key).
- `legacy.remembered[3]`: NES 20470-20476. `[4]`: ZAC 2218-2224, against Feltoe's June 449 for the Tome. `[5]`: LEO 439-444. `[6]`: CM2 1916, 1974-1976.
- `uncertain[7]`-`[17]`: PROS 42874-42888 (Gennadius in Mommsen's preface, "[consiliarius papae Leonis]" in brackets), GEN 43673-43676; PROS 54626-54634; LP 7641-7642, 7959-7961; JOR 2687-2709 (Priscus, the Mincius, Honoria) and JOR 3, 57 (551); CM2 2104-2107 (Hydatius: heaven's plagues and Marcian's forces under Aetius), 15698 (Cassiodorus: sent by Valentinian), 17662-17667 (Victor); the other LEO and NC lines as listed.
- `sources.about[3]`-`[10]`: each file is the one the new lines cite.

Nothing on the starting card is contradicted by the new brief or a held source; "Clearly wrong: none" is upheld.

## 2. Nothing else moved

Diffed field by field against `Card.existing.json`: every existing field and list item is word for word and in its place. The only differences are the items appended to `legacy.traces` (4), `legacy.remembered` (4), `uncertain` (11) and `sources.about` (8), and the new keys `briefReferences` and `quotationOriginals`, all listed in `Card_Edits.md`.

## 3. References

None names something the brief does not tell. The final brief dropped the forty days, Nestorius, the Syriac chronicle and "who had the last word"; no reference names them (Nestorius and the chronicle are on the card under `legacy.remembered`). Remaining: [0] the reading at Chalcedon, the cry, the line on what is human; [1] the Tome, the statement of faith, Peter through his successors, the canon refused, the age of Church and Empire; [2] a deacon in Gaul, chosen in 440, the Manichaeans and their books; [3] Eutyches, Flavian's synod, June 449, no Greek; [4] Ephesus 449 and the plea for Italy; [5] Letter 95, the council in the East, the envoys, the fourth session; [6] canon 28, Letters 104 and 105, the rock, the break and the peace; [7] Attila and the three accounts (Priscus names the source Jordanes draws on); [8] the faith held, Rome giving way centuries later, Egypt and Syria; [9] death in 461 and burial at St. Peter's; [10] the tradition, which the brief names. No quotation marks in any.

## 4. Census rules

Only allowed keys; no `briefLength`. Three quoted spans in the brief, three entries, each `modern` word for word; none for a dropped span. Each `printed` and `original` stands at its lines by the fold rule (LEO 5415-5416, 8637-8640, 9081-9083; Hefele 12336-12337). Every cited file is in `sources`. No audit, review or ruling named. American spelling outside printed wording; "honour" and "rumours" stand inside Feltoe's words, quoted verbatim. The three spans are all of six words or more and await the second reading; no `secondReading` was copied, since the starting card had no `quotationOriginals`.

## 5. Originals

- Q1: Hefele's Latin is clean ("Esurire, sitire, lassescere atque dormire, evidenter humanum est"), and the card carries it. Right.
- Q2: the Latin is held only in Mansi's damaged scan (M6 13193-13198, long s read as f throughout), and no other held print has it. English alone, under the batch 6 rule. Upheld.
- Q3: Mansi reads "rum ízcularium" (M6 18299-18302) and the Acta Sanctorum "scieeularium" and "prster" (34665-34666). The two scans are damaged at the same word, so neither confirms saecularium. English alone. Upheld.

No Greek used.

## 6. Not-found claims

All upheld: Leo's restoration of Theodoret and Timothy Aelurus's book (no held line cited); Egypt and Syria's refusal rests on the census entries and is credited to them in `briefReferences` only; Leo the Great and Leo Magnus found (LEO 322, 419). Nothing clearly wrong left in.
