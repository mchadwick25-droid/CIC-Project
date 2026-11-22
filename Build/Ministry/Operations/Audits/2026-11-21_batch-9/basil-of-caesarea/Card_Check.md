# Card check: Basil of Caesarea (`basil-of-caesarea`)

**FIX** (two changes). New card; no starting card and no new census entry.

## Checked

- Validator, on a scratch census with the card and brief set in: no errors for this entry except the two the release step clears (no `secondReading` on the three quotations, each six words or more; the three modern quotations not yet in `tools/quote_renderings.json`). Keys allowed; no `briefLength`; no audit named.
- Quotations, one entry for each of the brief's three quoted spans, none for a dropped span. Each `printed` stands at its lines: 1, Jackson, `npnf208` 39133-39135; 2, the Greek of PG 31, 72547-72549, checked by hand (Τίνα οὖν ἀπονίψεις ; τίνα θεραπεύσεις ; τίνος ἔσχατος ἔσῃ, αὐτὸς καθ᾽ ἑαυτὸν διάγων ;), with Clarke's English at 13460-13464; 3, Jackson, `npnf208` 33483-33485. The renderings hold: 2 follows the Greek (no word for feet), and the card says so. 1 and 3 are English alone because the Greek of the Letters is not held. Every quoted file is in `sources`.
- Fields against their lines (spot-checked): Jackson's chronology (`npnf208` 556, 600-605, 648-652, 685-689, 740-744, 776-777); Jerome 116 and its note (`npnf203` 41555-41560); Gennadius and Fremantle (42466-42471, 44607-44609); Theodoret (14086-14087, 14166-14168, 20714); Photius (1957-1972); Palladius (457); Sozomen 3.14 and 6.34 (`npnf202` 31861-31863, 39955-39961); Socrates (13929-13931); Oration 43.15, 25, 29, 34, 37, 63, 78-79 (`npnf207`); Gwynn (`npnf213` 11423); Hefele (17893-17895); Morison (370-382); Clarke (13154); the Greek-calendar note (`npnf208` 3314). All hold.
- No claim was listed as not found that should be wrong, and nothing found clearly wrong.

## Changes

1. **American spelling** (not quoted printed wording, so the rule applies), four places:
   - `legacy.traces[6]`: old "in defence of St. Basil, and an attack on Eunomius by Sophronius, also in defence of St. Basil." new "in defense of St. Basil, and an attack on Eunomius by Sophronius, also in defense of St. Basil."
   - `uncertain[0]`: old "written in self-defence against Eustathius of Sebaste" new "written in self-defense against Eustathius of Sebaste"
   - `briefReferences[0]`: old "written in self-defence against Eustathius of Sebaste." new "written in self-defense against Eustathius of Sebaste."
2. **`briefReferences[9]` names what the brief does not tell.** The brief never mentions Sozomen or the name Basileias (nor did v1). Old: "Sozomen 6.34: the Basileias still bore his name. World census, Cappadocian Christianity: his tradition." New: "World census, Cappadocian Christianity: his tradition." (The same fact stays in `legacy.traces[3]`, where it belongs.)

## Conflicts with the census entry's other fields

The card and the brief do not change the census. Each conflict and what settles it:

1. **Death date.** Census `longDescription` gives "Basil died on 1 January 379" as fact; `dates` "c. 329-379", `end` 379 and the `teaser` "c. 329 to 379 CE" give 379. The card and brief say "378 or 379". **No held source settles the day or the year.** For 1 January 379: Jackson's chronology (`npnf208` 776-777), Clarke (Life of Macrina, line 52) and the note on Jerome 116 (`npnf203` 41555, "died 379"). For 378: Gwynn (`npnf213` 11423, "at the end of 378") and Hefele (v2, 17893-17895, the Antioch synod of September 378 "in the ninth month after the death"). The ancient witnesses fix no year: Gregory of Nyssa says eight years after (Life of Macrina 178-180), and Jerome says "in the reign of Gratianus" (`npnf203` 41560). So the card's contested form is right. The census `longDescription` sentence is wrong to state the day as settled; the brief replaces it at release. The `c.` on `dates` and the teaser leave 379 as a stated upper bound, which no held source contradicts.
2. **The predecessor who died in 370.** Census `longDescription`: "In 370 Eusebius of Caesarea died". The card names him by role. This is **not a factual conflict**. The name is held: Jackson's chronology, "370. Death of Eusebius of Cæsarea" (`npnf208` 685); Gregory's own pun, "the prelate whose name betokened his godliness" (`npnf207` 42047-42048, with the endnote "Eusebius, i.e., 'pious'"). The defect is that the census wording collides with the historian **Eusebius of Caesarea** (census `eusebius-of-caesarea`, Caesarea Maritima, c. 260-339), whom Jackson also calls "Eusebius of Cæsarea, the historian" (`npnf208` 14461). The role form avoids that. One correction to `Card_Edits.md`, conflict 3: its evidence calls the name "an editor's insertion in `npnf207` 41776 and 42048". The endnotes there are the editor's, but the chronology at `npnf208` 685 gives the name, and Gregory points to it by the pun.
3. **On the Holy Spirit.** Census `longDescription` says "Not long after 373". The card gives Jackson's 374 (`npnf208` 740-744) and the tree's "about 375". These agree in substance, so there is no conflict.
4. The census `why` ("from about 370"), `relationsSummary`, `voices`, `legacy` and `sourcing` are not contradicted.
