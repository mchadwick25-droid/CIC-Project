# Card edits: Leo of Rome

Batch 8, 2026-11-21. The existing card (`Card.existing.json`, the census card) is kept word for word; every edit below is an addition at the end of a list, or a new key. No existing word is changed, moved or cut. File names: LEO is `npnf212_leo-great-gregory-great.xml` (Feltoe's English, with his Introduction), NC `npnf214_seven-ecumenical-councils.xml`, PROS the Mommsen Prosper, JOR Jordanes, CM2 the Mommsen Hydatius, Cassiodorus and Victor of Tunnuna, LP the Book of the Popes, ZAC the Syriac chronicle, NES Nestorius, GEN Gennadius in `npnf203_theodoret-jerome-gennadius-rufinus.xml`. "Sheet" is `Source_Sheet.md`, "Outline" is `Outline.md`. Every line below was re-read in its file.

## Clearly wrong

None. I checked each existing claim against the brief and the held lines it rests on (LEO 399-410, 435-478, 484-487, 545-548, 619-623, 754-778, 848-862, 902-908; NC 19996-20007; PROS 54626-54634, 54944-54972, 55120-55131), and none is contradicted by a held source or by the brief.

## New: additions

| Field | Old words | New words | Evidence |
|---|---|---|---|
| `legacy.traces` (4 added) | none | The anniversary sermon on Peter honored in his person; the break with Anatolius and how it ended; the Illyrian bishops signing the canon, Florence and 1215; his feasts and the doctor's title. | LEO 13464-13468 (Sermon III); LEO 813-821, NC 22415-22417; NC 22405-22409, 22430-22436; LEO 912-914. |
| `legacy.remembered` (4 added) | none | Nestorius's praise; the Syriac chronicle's charge, with its date problem; Cassian's words; Hydatius's record. | NES 20470-20476; ZAC 2218-2224, LEO 609-614; LEO 439-444; CM2 1916, 1974-1976. |
| `uncertain` (11 added) | none | The election (forty days, Gaul, the Book of the Popes' Tuscan); Feltoe's inference that he knew no Greek; the Manichaeans (443 or 444, the emperor's ordinance); Hilary of Arles; Gennadius on Prosper; the Tome's pair; Ephesus 449; after Ephesus; the canon; Attila in full; the Vandals in 455 with Sermon 84. | PROS 54626-54634, 54713-54723, 54811-54829, 54944-54957, 55120-55131, 42878, 42886-42888; LEO 470-478, 413-416, 528-538, 1908-1912, 496-505, 5421-5425, 6713-6716, 655-669, 685-688, 701-712, 710-731, 6779-6784, 804-813, 6793-6799, 9079-9093, 9257-9265, 9280-9281, 8686-8687, 21150-21156, 21193-21195; GEN 43673-43676; LP 7641-7642, 7959-7961; NC 22383-22390; JOR 2687-2709; CM2 2065-2067, 2104-2107, 15698, 17662-17667. |
| `sources.about` (8 added) | none | Hefele (the Tome's Latin), the canons with Percival's notes, Gennadius, Jordanes, the Hydatius, Cassiodorus and Victor chronicles, the Book of the Popes, the Syriac chronicle, Nestorius. | The same files; `date` from the Sheet's file keys, null where it names none. |
| `briefReferences` (new key, 10) | none | One line per paragraph of the brief, plus the tradition's line. No quotation marks. | The same lines as above and the Sheet's E-items. |
| `quotationOriginals` (new key, 3) | none | See below. | See below. |

The Mark ruling's pair (Nestorius and the Syriac chronicle) and the review's M4 items (the anniversary sermon, the deacon's escape, Florence, the emperor's order on the Manichaeans, Jordanes drawing on a writer of Attila's time) are all carried, in `legacy.remembered`, `legacy.traces` and `uncertain` as listed. The outline's "For the card" list is carried except where noted at the end.

## Quoted spans

| Span in the brief | Original and print | Status |
|---|---|---|
| To be hungry, to be thirsty, to grow tired and to sleep is plainly human. (14 words) | English LEO 5415-5416; Latin in Hefele 12336-12337, clean, with Mansi's damaged scan (M5 123352-123354) giving the same words | awaiting second reading |
| Nor need a letter set down everything that could be committed at Ephesus, in what was not a trial but a robbery. (22) | English LEO 8637-8640 alone; Latin only in a damaged scan of Mansi (M6 13193-13198), where the long s reads as f, and no other held print has it | awaiting second reading |
| Yet worldly things stand on one footing, and the things of God on another. No building will stand firm except on the rock the Lord laid as its foundation. (29) | English LEO 9081-9083 alone; Latin only in faulty scans (M6 18298-18310; the Acta Sanctorum, `acta-sanctorum_octobris-tomus-10-lat_bruxelles1861.txt` 34665-34666, which prints "scieeularium" and "prster"), neither clean at the word for worldly | awaiting second reading |

The census card has no `quotationOriginals`, so no second reading is copied. The outline's second Latin print for Q3 (the Acta Sanctorum) is not used because I read it by hand: "scieeularium" and "prster" are scan faults that no held print resolves, so under the Batch 6 ruling Q3's Latin is left off and the English stands alone. Q1's Hefele print has no fault. Greek: none. The brief's wording for Q2 is its own rendering of Leo's Latin, and it differs from Feltoe's English, which the existing key-works line quotes; the quotation's `uncertain` note says so.

## Where held sources differ, each credited on the card

Attila's withdrawal (Prosper, Jordanes, Hydatius, Cassiodorus, the Book of the Popes, Victor, and Feltoe's place and cause); the year of the Manichaean search (443 and 444); Flavian's end; the Syriac chronicle against the date of the Tome; why Leo rejected the canon (Quesnel and the Ballerini); how the quarrel with Anatolius ended (Feltoe and the editors); the election and the Book of the Popes' birthplace.

## Not found, so left off the card

- Leo's restoration of Theodoret and his letter to him, and Timothy Aelurus's book calling Leo a Nestorian (Gennadius's story): the Sheet names them but cites no held line.
- The brief's line that the churches of Egypt and Syria refused the Tome's faith rests, in the Outline, on the census entries for the Council of Chalcedon and the tradition, not on a held line. It is cited as the world census in `briefReferences` only.
- The existing card's `otherNames` Leo the Great and Leo Magnus are found (LEO 322, 419).
