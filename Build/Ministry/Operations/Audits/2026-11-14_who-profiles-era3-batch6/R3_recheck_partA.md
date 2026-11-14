# R3 recheck, part A: era 3 batch 6

Scope: Columbanus, Isidore of Seville and John of Biclaro, with their cards, audio scripts and `records.json` entries; the clauses of Open-Gaps entry 251 and the batch README that concern them. Round 3 of at most 3, a targeted recheck.

## Method

I am a fresh Opus reviewer; I did not draft, review or fix these files in rounds 1 or 2. I read `CLAUDE.md` in full, the part A sections of `R2_recheck.md` and `R2_changes.md`, and the heading shape of batch 5's `R3_recheck.md`. The R2 recheck files were committed at `ca5d9ccf` (part A) and `1304da0b` (parts B and C). I read every change since then as a word diff, `git diff --word-diff 1304da0b..HEAD`, over the three briefs, cards and audio scripts and `records.json`. No brief or audio script for these three ids changed. The changes are the R2 fixes (`cb17e725`), the removal of empty `"date": null` keys (`cfccbe04`) and the American-spelling pass (`a1ed5f15`). For each changed string I opened the cited lines in the vendored file myself. Line numbers point to files under `cic/texts/` unless another path is given. I edited no file but this report, and made no git write, web or paid call.

## 1. The R2 findings

| Finding | Status | Evidence |
|---|---|---|
| R2-A-M1 (Columbanus `keyWorks` 3: 35-word sentence) | RESOLVED | Now "six letters under his name. Two went to Pope Boniface IV, and one each to Pope Gregory the Great, a council of Gallic bishops and a disciple. Another went to his monks as he waited to be shipped home. In several he names himself Columba, a dove". The longest sentence is 23 words. The count still makes six (2 + 1 + 1 + 1 + 1). |
| R2-A-M2 (Isidore `uncertain` 5: Pagi's condition dropped) | RESOLVED | Now "He follows later Spanish chroniclers, who give Sisebut's seventh year. That sets it in 618, he says, if it met in November or December, which is not clear." mansi10 l.59531-59534: "Horum crium Hiftoricoram fententia preferenda, & hac fynodus ad an. 648. retrahenda, fi tamen menfe-Novembri ) aur Decembri celebrata fity qua de re non fatis liquet" (OCR for "trium", "618", "sit"). The note is Pagi's: "ApvpnoTraTio Pacey." (OCR for "Annotatio Pagii"), l.59503, with the heading "Ad An. Ch, 619. n. 2." at l.59506. The records side already kept the condition (l.59506-59536). |
| R2-A-M3 (Isidore: the Breviarium preface is Lorenzana's; two sources missing) | RESOLVED | Card `uncertain` 4: "Francisco Antonio Lorenzana, in his preface to the Breviarium Gothicum, says he did." PL 86 l.385-390: "FRANCISCUS ANTONIUS LORENZANA, ARCHIEPISCOPUS TOLETANUS, HISPANIARUM PRIHAS, LECTORI SALUTEM"; l.474: "fere scopus concil. iv Tolet., praeside sancto Isidoro". Both `sources.about` entries are added, and their files exist. The records claim names Lorenzana, with witness l.385-390 and 474. The presiding contested claim names him, "reprinted in PL 86". |
| R2-A-M4 (all three cards: `"date": null`) | RESOLVED | The lead ruled for the README rule ("A field with no content is left out", README l.14) and removed every `"date": null`: Columbanus 3, Isidore 4, John 5, as R2 counted. `grep null` finds none in the three cards. Only null lines were removed; no real date was lost. |

R1 point found only partly resolved by R2: A-B3 (Seville II "in 619" told as settled). R2 found the brief resolved and the new card item partly right, for want of Pagi's condition. With R2-A-M2 applied, the card now keeps the condition, so A-B3 is now RESOLVED in full.

### The added date: Lorenzana's preface, "1775"

The card entry gives `"date": "1775"`. In the vendored PL 86 file the year stands only in the Library header: "Francisco Antonio Lorenzana (editor, 1775)" (l.2). Migne's own title page (l.287-325) names "FR. ANT. LORENZANA, TOLETANAE ECCLESIAE ARCHIEPISCOPI" but prints only Migne's year, 1862, and the preface carries no date that I could find. So I looked for an independent witness. Two held files confirm the year:

- Férotin, Liber mozarabicus sacramentorum (1912), l.5233-5235: "Le Bréviaire mozarabe imprimé en 1502 … et réimprimé en 1775 par l'archevêque Lorenzana (l'édition de la Patrologia latina de Migne, 1862, est la simple reproduction de l'édition de 1775)". Also l.54635-54636: "Il a été imprimé en 1775 par Lorenzana, archevêque de Tolède".
- Warren, Antiphonary of Bangor part 2 (1895), l.9920-9921: "Lorenzana's reprint of Cardinal Ximenes' Breviarium. Gothicum, Matrit. 1775".

Férotin also confirms that the PL 86 text reproduces Lorenzana's 1775 edition, so dating the preface by that edition is right. The card's other `date` values follow the same rule, the year of the printing the text comes from. The date is sound, and no change is needed. The records claim's "(ed. 1775, reprinted in PL 86)" is equally sound.

## 2. New findings in changed text

None. There is no blocking point and no minor point in the changed text of the three profiles.

What I checked:

- **The R2 fix strings** (above): each is true to its source line, names the right witness, and keeps the source's conditions. The two new `sources.about` entries match the files they name. "Pagi" without a forename follows what Mansi prints (R2 accepted it in `uncertain` 5); the new entry is consistent with it.
- **The records changes** (only `isidore-of-seville` among these ids, beyond spelling): the claim "Francisco Antonio Lorenzana, in his preface to the Breviarium Gothicum (ed. 1775, reprinted in PL 86): 'concil. iv Tolet., praeside sancto Isidoro'" quotes l.474 verbatim, OCR spacing apart. Its formation_confidence stays Contested, which is right, since the acts give only the first signature (Hispana l.40882-40884).
- **The American-spelling pass**, for these ids: Columbanus `legacy.traces` 3, "behaviour" to "behavior", and the Columbanus records note "catalogue date" to "catalog date". The Bede line is reported speech, with no quotation marks; it renders Giles's "the Scots in no way differ from the Britons in their behaviour" (l.3856-3857) as "the Irish", so it is our prose and takes American spelling. The records note is our own prose. No verbatim quotation in the three cards or their records was changed. `tools/check_spelling.py` over the three briefs, cards, audio scripts and `records.json` reports 0.
- **Writing** (CLAUDE.md, "No AI tells"; `Who_Profile_Pattern.md` item 4): the changed strings are plain and short. They have no contrast frame, colon reveal, tail, triad or unearned adjective. "That sets it in 618, he says, if it met in November or December, which is not clear" keeps Pagi's doubt in his own terms, not as a narrator's hedge.

## 3. Open-Gaps 251 and the README

Every clause on these three ids was checked against the cards, the records, the census (`cic-website/data/world-census.json`) and the vendored files.

Clauses that hold:

- **List lines.** Columbanus has a people row (`insular-irish-monastic-christianity`, people[1]), and so does Isidore (`nicene-visigothic-iberia`, people[2]). John of Biclaro has none. He is named in the text of Nicene Visigothic Iberia (documentedStories[0]) and Nubian Christianity (sources[0] note; documentedStories[0] caveat and sources[1]), as "John of Biclarum".
- **Census text, Nubian entry.** The entry says John "records the rival Makurian conversion" and makes the "rival Chalcedonian claim on Makuria". John writes "Maccurritarum gens his temporibus Christi fidem recepit" (mommsen1894 l.19834). Mommsen's apparatus reads "videntur intellegi Μακκουραι Mauretaniae Caesariensis (Ptolem. 4, 2, 19)" (l.19879-19880, OCR rough). The Library header reads Makuria (l.27-28). The card's `uncertain` 8 agrees.
- **Not held.** Hodgkin's work on Italy, which Foulke cites (only Hodgkin's Cassiodorus is held). Columbanus's book against the Arians. Redemptus's account (Mommsen l.21960-21962, Brehaut and Poschmann report it). Braulio's Praenotatio in Latin: PL 83 says only that it is printed in the Isidoriana (l.123152-123165), and Mommsen quotes pieces of it (l.21950-21953). John's rule. The Lives by Lucas Tudensis and Rodericus Cerratensis. Each matches the cards and records.
- **Years.** Columbanus "c.543-615": scan row (`Who_Scan_Era3.md` l.94); Foulke "born in Leinster, Ireland about 543" (paul-the-deacon foulke1907 l.15761). John "c.540-after 621": the PL 72 header (l.3, "c. 540-621"), and Gallandi's "post annum 621" (l.64492). Isidore "c.560-636": the headers of Lindsay, Brehaut and PL 83 (l.3). Nicolás Antonio, PL 80 l.49008-49011 and 49106-49107, names Higuera as the one "quem multiplicis ac multicipitis hujus fabulae auctorem vulgaris fama fert" and "primus inventor Chronicorum Dextri et Maximi". So "which Nicolás Antonio treats as Higuera's forgery" holds.
- **Wrong or loose leads.** PL 80 holds the Rule, Penitential, sermons, six letters and poems. On Fredegar IV.36, Krusch writes "Hoc caput plerumque ad verbum ex Vita Columbani auctore Iona … fluxit" (krusch1888 l.10072-10074), and later that Fredegar condenses the Life (l.10344). Seville II: era 657 and the ninth year (Hispana l.59339-59343); Pagi argues for 618. Toledo IV: first signature only. John as John of Gerona: Mommsen, "nec dubium est ipsum esse episcopum Gerundensem Iohannem, quem repperimus subscripsisse tam Bar[cinonensi]…" (l.19441-19442).
- **README.** The scan order and years are as the scan gives them: Columbanus 615, John of Biclaro after 621, Isidore 636 (`Who_Scan_Era3.md` l.89, 90, 94). Columbanus and Isidore are marked major, and John is a recorder at standard length. Each matches the cards' `briefLength`.

Findings on the entry:

- **R3-A-M1 MINOR (Open-Gaps 251, "List lines" and "Census text"; the same reading in a second census place, not logged).** The edge `nubian-christianity--makurian-nubian-christianity` also names John and reads his Maccurritae as Makuria. It gives confidence "Widely Accepted" and verification_state "verified-direct": "John of Biclarum says the Makurians took up the Christian faith in the third year of Justin II, about 569" (`edges[177].note`, quoting mommsen1894 l.19834). The entry logs only the Nubian Christianity entry, so whoever fixes that entry would leave the edge note unfixed. The list-line clause "named only in entry text" also misses this edge.
  - Fix, "List lines": "John of Biclaro is named only in entry text (Nicene Visigothic Iberia; Nubian Christianity, as "John of Biclarum") and in the note of the edge from Nubian Christianity to Makurian Nubian Christianity."
  - Fix, "Census text": after "…the Library file header reads them as Makuria.", add: "The edge `nubian-christianity--makurian-nubian-christianity` reads him the same way ("John of Biclarum says the Makurians took up the Christian faith in the third year of Justin II, about 569"), with confidence Widely Accepted."

- **R3-A-M2 MINOR (Open-Gaps 251, "Census text"; a contested claim told as settled in the census, not logged).** The Nicene Visigothic Iberia entry says three times that Isidore presided at the Fourth Council of Toledo. `voices[2]`: "…and who presided at the fourth council of Toledo in 633". `documentedStories[1].teaser`: "Isidore of Seville presides over a council that declares forced baptism wrong". `documentedStories[1].text`: "In 633 the bishops of Spain met at Toledo in the fourth of the great councils, with Isidore of Seville presiding". The card (`uncertain` 4) and the records (contested claim "Whether he presided at Toledo IV", confidence Contested) hold that the acts give him only the first signature (Hispana l.40882-40884). Brehaut says "probably" (brehaut1912 l.702-703); only Lorenzana's 1775 preface says he presided (PL 86 l.474). The entry's scan-corrections bullet logs this for the scan row only, not for the census text. Open-Gaps has no earlier entry on it (searched for "presid" with Isidore or Toledo).
  - Fix, "Census text": add: "The Nicene Visigothic Iberia entry has Isidore of Seville preside at the Fourth Council of Toledo (voices[2]; documentedStories[1], teaser and text). The acts give him only the first signature (Hispana l.40882-40884); Ernest Brehaut says he probably presided, and Francisco Antonio Lorenzana's 1775 preface to the Breviarium Gothicum says he did (PL 86 l.474). The card and records keep it contested."

A note for the lead, outside these three ids: the entry cites "Decision-Log, 'Who profiles, era 3 batch 6' (2026-11-14)", and it says the ten profiles "are approved to proceed". `Build/Ministry/Features/Church-Family-Tree/Decision-Log.md` has no such entry yet (its last Who entry is batch 5, l.2673). That fits a draft written ahead of the round 3 result. The Decision-Log entry needs to exist before 251 is merged as it stands.

## 4. Mechanical checks

| Profile | Words | Cap | FK | Flesch | Audio = brief | Tags |
|---|---|---|---|---|---|---|
| Columbanus (major) | 403 | ~405 | 7.6 | 67.1 | yes | one `[calmly]`, one `[warmly]` |
| Isidore of Seville (major) | 405 | ~405 | 7.8 | 64.0 | yes | one `[calmly]`, one `[warmly]` |
| John of Biclaro (recorder) | 325 | ~325 | 7.9 | 64.6 | yes | one `[calmly]`, one `[warmly]` |

`grade_text` was run from the repo root on each brief; all pass (FK ≤ 10, Flesch ≥ 60). Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed. The three cards and `records.json` parse as JSON. Every `file` named in the three cards' `sources` exists. `tools/check_spelling.py` reports 0 across the part A files and `records.json`.

## Verdict per profile

- `columbanus`: CLEAR.
- `isidore-of-seville`: CLEAR.
- `john-of-biclaro`: CLEAR.

The two minor points, R3-A-M1 and R3-A-M2, are on Open-Gaps 251, not on any profile file. Each has an exact fix ready, and neither changes a card, brief or record.

## Totals

R2 findings: 4 of 4 resolved; R1 A-B3, which R2 found partly resolved, is now resolved. New findings on the three profiles: none. New findings on Open-Gaps 251: 2 minor. Blocking: none.
