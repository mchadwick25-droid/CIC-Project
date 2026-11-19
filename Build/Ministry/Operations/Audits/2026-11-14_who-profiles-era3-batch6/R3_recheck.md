# R3 recheck: era 3 batch 6

Round 3, the third and last under the cap, was a targeted recheck in three parts, each by a fresh Opus agent that had not seen the drafting or the earlier rounds, at full effort. The parts follow, unchanged.

## R3 recheck, part A: era 3 batch 6

Scope: Columbanus, Isidore of Seville and John of Biclaro, with their cards, audio scripts and `records.json` entries; the clauses of Open-Gaps entry 251 and the batch README that concern them. Round 3 of at most 3, a targeted recheck.

### Method

I am a fresh Opus reviewer; I did not draft, review or fix these files in rounds 1 or 2. I read `CLAUDE.md` in full, the part A sections of `R2_recheck.md` and `R2_changes.md`, and the heading shape of batch 5's `R3_recheck.md`. The R2 recheck files were committed at `ca5d9ccf` (part A) and `1304da0b` (parts B and C). I read every change since then as a word diff, `git diff --word-diff 1304da0b..HEAD`, over the three briefs, cards and audio scripts and `records.json`. No brief or audio script for these three ids changed. The changes are the R2 fixes (`cb17e725`), the removal of empty `"date": null` keys (`cfccbe04`) and the American-spelling pass (`a1ed5f15`). For each changed string I opened the cited lines in the vendored file myself. Line numbers point to files under `cic/texts/` unless another path is given. I edited no file but this report, and made no git write, web or paid call.

### 1. The R2 findings

| Finding | Status | Evidence |
|---|---|---|
| R2-A-M1 (Columbanus `keyWorks` 3: 35-word sentence) | RESOLVED | Now "six letters under his name. Two went to Pope Boniface IV, and one each to Pope Gregory the Great, a council of Gallic bishops and a disciple. Another went to his monks as he waited to be shipped home. In several he names himself Columba, a dove". The longest sentence is 23 words. The count still makes six (2 + 1 + 1 + 1 + 1). |
| R2-A-M2 (Isidore `uncertain` 5: Pagi's condition dropped) | RESOLVED | Now "He follows later Spanish chroniclers, who give Sisebut's seventh year. That sets it in 618, he says, if it met in November or December, which is not clear." mansi10 l.59531-59534: "Horum crium Hiftoricoram fententia preferenda, & hac fynodus ad an. 648. retrahenda, fi tamen menfe-Novembri ) aur Decembri celebrata fity qua de re non fatis liquet" (OCR for "trium", "618", "sit"). The note is Pagi's: "ApvpnoTraTio Pacey." (OCR for "Annotatio Pagii"), l.59503, with the heading "Ad An. Ch, 619. n. 2." at l.59506. The records side already kept the condition (l.59506-59536). |
| R2-A-M3 (Isidore: the Breviarium preface is Lorenzana's; two sources missing) | RESOLVED | Card `uncertain` 4: "Francisco Antonio Lorenzana, in his preface to the Breviarium Gothicum, says he did." PL 86 l.385-390: "FRANCISCUS ANTONIUS LORENZANA, ARCHIEPISCOPUS TOLETANUS, HISPANIARUM PRIHAS, LECTORI SALUTEM"; l.474: "fere scopus concil. iv Tolet., praeside sancto Isidoro". Both `sources.about` entries are added, and their files exist. The records claim names Lorenzana, with witness l.385-390 and 474. The presiding contested claim names him, "reprinted in PL 86". |
| R2-A-M4 (all three cards: `"date": null`) | RESOLVED | The lead ruled for the README rule ("A field with no content is left out", README l.14) and removed every `"date": null`: Columbanus 3, Isidore 4, John 5, as R2 counted. `grep null` finds none in the three cards. Only null lines were removed; no real date was lost. |

R1 point found only partly resolved by R2: A-B3 (Seville II "in 619" told as settled). R2 found the brief resolved and the new card item partly right, for want of Pagi's condition. With R2-A-M2 applied, the card now keeps the condition, so A-B3 is now RESOLVED in full.

#### The added date: Lorenzana's preface, "1775"

The card entry gives `"date": "1775"`. In the vendored PL 86 file the year stands only in the Library header: "Francisco Antonio Lorenzana (editor, 1775)" (l.2). Migne's own title page (l.287-325) names "FR. ANT. LORENZANA, TOLETANAE ECCLESIAE ARCHIEPISCOPI" but prints only Migne's year, 1862, and the preface carries no date that I could find. So I looked for an independent witness. Two held files confirm the year:

- Férotin, Liber mozarabicus sacramentorum (1912), l.5233-5235: "Le Bréviaire mozarabe imprimé en 1502 … et réimprimé en 1775 par l'archevêque Lorenzana (l'édition de la Patrologia latina de Migne, 1862, est la simple reproduction de l'édition de 1775)". Also l.54635-54636: "Il a été imprimé en 1775 par Lorenzana, archevêque de Tolède".
- Warren, Antiphonary of Bangor part 2 (1895), l.9920-9921: "Lorenzana's reprint of Cardinal Ximenes' Breviarium. Gothicum, Matrit. 1775".

Férotin also confirms that the PL 86 text reproduces Lorenzana's 1775 edition, so dating the preface by that edition is right. The card's other `date` values follow the same rule, the year of the printing the text comes from. The date is sound, and no change is needed. The records claim's "(ed. 1775, reprinted in PL 86)" is equally sound.

### 2. New findings in changed text

None. There is no blocking point and no minor point in the changed text of the three profiles.

What I checked:

- **The R2 fix strings** (above): each is true to its source line, names the right witness, and keeps the source's conditions. The two new `sources.about` entries match the files they name. "Pagi" without a forename follows what Mansi prints (R2 accepted it in `uncertain` 5); the new entry is consistent with it.
- **The records changes** (only `isidore-of-seville` among these ids, beyond spelling): the claim "Francisco Antonio Lorenzana, in his preface to the Breviarium Gothicum (ed. 1775, reprinted in PL 86): 'concil. iv Tolet., praeside sancto Isidoro'" quotes l.474 verbatim, OCR spacing apart. Its formation_confidence stays Contested, which is right, since the acts give only the first signature (Hispana l.40882-40884).
- **The American-spelling pass**, for these ids: Columbanus `legacy.traces` 3, "behaviour" to "behavior", and the Columbanus records note "catalogue date" to "catalog date". The Bede line is reported speech, with no quotation marks; it renders Giles's "the Scots in no way differ from the Britons in their behaviour" (l.3856-3857) as "the Irish", so it is our prose and takes American spelling. The records note is our own prose. No verbatim quotation in the three cards or their records was changed. `tools/check_spelling.py` over the three briefs, cards, audio scripts and `records.json` reports 0.
- **Writing** (CLAUDE.md, "No AI tells"; `Who_Profile_Pattern.md` item 4): the changed strings are plain and short. They have no contrast frame, colon reveal, tail, triad or unearned adjective. "That sets it in 618, he says, if it met in November or December, which is not clear" keeps Pagi's doubt in his own terms, not as a narrator's hedge.

### 3. Open-Gaps 251 and the README

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

### 4. Mechanical checks

| Profile | Words | Cap | FK | Flesch | Audio = brief | Tags |
|---|---|---|---|---|---|---|
| Columbanus (major) | 403 | ~405 | 7.6 | 67.1 | yes | one `[calmly]`, one `[warmly]` |
| Isidore of Seville (major) | 405 | ~405 | 7.8 | 64.0 | yes | one `[calmly]`, one `[warmly]` |
| John of Biclaro (recorder) | 325 | ~325 | 7.9 | 64.6 | yes | one `[calmly]`, one `[warmly]` |

`grade_text` was run from the repo root on each brief; all pass (FK ≤ 10, Flesch ≥ 60). Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed. The three cards and `records.json` parse as JSON. Every `file` named in the three cards' `sources` exists. `tools/check_spelling.py` reports 0 across the part A files and `records.json`.

### Verdict per profile

- `columbanus`: CLEAR.
- `isidore-of-seville`: CLEAR.
- `john-of-biclaro`: CLEAR.

The two minor points, R3-A-M1 and R3-A-M2, are on Open-Gaps 251, not on any profile file. Each has an exact fix ready, and neither changes a card, brief or record.

### Totals

R2 findings: 4 of 4 resolved; R1 A-B3, which R2 found partly resolved, is now resolved. New findings on the three profiles: none. New findings on Open-Gaps 251: 2 minor. Blocking: none.

## R3 recheck, part B: era 3 batch 6

Scope: round 3, the last allowed. Part B covers `john-moschus` (recorder, standard length), `babai-the-great` (major) and `severinus-of-noricum` (standard), with their briefs, cards, audio scripts and `records.json` entries. It also covers the one change to `era3/batch5/records.json`, the batch README's sentences on these three, and Open-Gaps 251's clauses on them, with the "Correction to batch 5" and "Card tradition" clauses in full.

### Method

I am a fresh Opus reviewer. I did not draft or fix these files and had not seen earlier rounds. I read `R2_recheck.md` part B and `R2_changes.md` part B. I read every change since R2 as a word diff from `1304da0b` ("R2 recheck, parts B and C") to HEAD (`c7b84b31`), limited to the batch 6 folder and `era3/batch5/`. Under part B, these changed:
- the Babai card (R2-B-B1, R2-B-M1 to M3) and records entry (R2-B-B1, R2-B-M1)
- the Moschus card (American spelling: "traveled" twice, "defense"; two `"date": null` keys removed)
- the Severinus card (one `"date": null` key removed)
- the batch 5 `henana-of-adiabene` note (R2-B-B1)

No brief or audio script of the three changed. I opened each changed string at its line in the vendored file and checked who speaks there. Because R2-B-B1 turns on how much of the Life of George Braun leaves out, I read every footnote of Braun's in the Life (braun1915 l.12419 to the closing "Amen" at l.15452), not only the four R2 cited. Line numbers point to files under `cic/texts/` unless another path is given. I edited no file but this report, and made no git writes, model calls or web requests.

### 1. The R2 findings

| Finding | Status | Evidence |
|---|---|---|
| R2-B-B1 (Braun's Life of George called "whole") | PARTLY | "Whole" is gone from the card, both records entries and the batch 5 note. But the replacement wording counts the omissions, and the count is wrong. Braun passes over four passages, not three, and gives two more only as a summary note. See R3-B-B1. The card's new wording also gives Braun a judgment he makes on only two of them. See R3-B-M1. |
| R2-B-M1 (Guidi: the quarrel between the two men; line ranges) | RESOLVED | Card `uncertain` 1: "It tells of a quarrel between him and Babai the Little that lasted to the end of their lives." Guidi: "Salanas vero rixae amator iurgia multa magnasque contentiones / excitavit inter duas illas firmissimas religionis turres, duo Babhay, / nec conquievit aut desiit usque ad finem agonis , vitae asceticae, eorum" (chronica-minora-pars-prior-versio-lat_guidi1903 l.2050-2052). The records quotation matches the file, OCR space before the comma included. "cognominaverunt" stands on l.2064, "Seripsit autem" on l.2069. The witness now reads l.2032-2037, 2050-2064, 2069-2070. The contested claim and the Book III absent detail cite l.2036-2064. The Mari witness cites l.13517-13520, and "nobio Mar Abraliam" is on l.13520 (mari gismondi1899). |
| R2-B-M2 (long card sentences; "which" after Khosrau) | RESOLVED, one sentence still long | `legacy.traces` 4 now reads "...but helped them with his pen. Addai Scher dates the debate to 612." Seert: "Mar Babai '", qui n'avait pas pu se / rendre k cctte reunion k cause de sa faiblesse et de son kge avance, leur / avait ete dun grand secours par sa plume" (scher1919 l.29556-29558); "1. En 612" is Scher's note (l.29565). `uncertain` 6 is split as worded. In `uncertain` 5, the split R2 gave still leaves the first sentence at 29 words. See R3-B-M2. |
| R2-B-M3 (Labourt's word "lost in the scan") | RESOLVED | "a word before the dates cannot be read in the Library's text of his page." OCR: "Il mourut âgé de soixante-quinze ans, phone / 'entre 615 et 620." (labourt1904 l.17771-17772). |
| R1 B-B3 (Life of George held), carried by R2-B-B1 | PARTLY | As R2-B-B1 above. |
| R1 B-H1 (batch 5 note), carried by R2-B-B1 | PARTLY | As R2-B-B1 above. The rest of the note is true. See section 3. |
| R1 B-M13 (README: "logged in Open-Gaps") | RESOLVED | Open-Gaps 251, "Card tradition", now logs the Severinus change. See section 4. |

### 2. New findings in changed text

**R3-B-B1 BLOCKING (`records.json` `babai-the-great`, the claim opening "Babai's Life of George, in Braun's German" and `absent_details` "A Syriac or English text of his own books"; `era3/batch5/records.json` `henana-of-adiabene` `absent_details` "A second witness to Babai's doctrinal charges"; Open-Gaps 251, "Not held"; carried from R2-B-B1).**

The R2 fix replaced "whole" with a count. The records claim says "the introduction shortened and three passages passed over". The absent detail says Braun "passes over two encomia and one passage he calls empty of content". The batch 5 note says he "passes over three passages but keeps the charges". Open-Gaps 251 says he "leaves out three passages".

Braun's own footnotes inside the Life say more than that:
- The introduction: "Von der sehr langen Einteilung gebe ich nur die wichtig- / sten Gedanken." (braun1915 l.12442-12443)
- An encomium: "Das folgende, sachlich belanglose Enkomion auf die Heilige / übergehe ich." (l.13161-13162)
- A reflection, missed by R2: "Eine hier folgende Betrachtung habe ich übergangen." (l.13270)
- A long encomium: "Ein langes Enlromion, worin die Beiden mit den die / Bundeslade aus dem Philisterlande ziehenden Kühen ... verglichen / werden, übergehe ich." (l.13319-13322)
- A reflection given only as a note: "Es folgt zunächst im Anschluß an 1 Kor. 7, 29 — 81 eine / Betrachtung über die Schlechtigkeit der Zeit." (l.13362-13363). The text goes from "was der selige Paulus voraussagte1)" (l.13349) straight to section 30 (l.13351).
- Passages "of no content": "Die folgenden, sachlich inhaltslosen Ausführungen über- / gehe ich." (l.13806-13807)
- George's prayer cut short: "Das Gebet setzt sich, noch lange fort in einem Dank für / die Berufung zum Christentum ... zum Mönchtum und Mar- / tyrium." (l.14944-14947). The translation picks up at section 62 (l.14928).

So Braun passes over four passages and gives two more only as a summary note, besides shortening the introduction. (The note "Es folgt im Text eine Lücke", l.14728, marks a gap in the Syriac text, not an omission of Braun's.) All three record texts and the Open-Gaps clause state a count that the translator's own notes contradict. That is a false claim about what a held source contains. It is the same kind of defect R2-B-B1 was raised for, and the batch 5 note, which this round was asked to confirm as true, still carries it. The note's other point stands: none of the omissions falls in the charges. The reflection noted at l.13362 comes before section 30, where the charges begin (l.13351 ff.).

Fixes, each replacing only the words quoted:
- Records claim opening: replace "(the introduction shortened and three passages passed over, braun1915 l.12442-12443, 13161-13162, 13319-13322, 13806-13807)" with "(the introduction shortened, four passages passed over and two given only as a note, braun1915 l.12442-12443, 13161-13162, 13270, 13319-13322, 13362-13363, 13806-13807, 14944-14947)".
- Records `absent_details` "A Syriac or English text of his own books": replace "and passes over two encomia and one passage he calls empty of content (l.13161-13162, 13319-13322, 13806-13807)" with "passes over two encomia, a reflection and one passage he calls empty of content (l.13161-13162, 13270, 13319-13322, 13806-13807), and gives a reflection on the times and the rest of George's prayer only as notes (l.13362-13363, 14944-14947)".
- Batch 5 note: replace "which shortens the introduction and passes over three passages but keeps the charges (persian-martyr-acts bkv22 braun1915 l.12419 ff.; omissions noted at l.12442-12443, 13161-13162, 13319-13322, 13806-13807; the charges at l.13355-13400)" with "which shortens the introduction, passes over four passages and gives two more only as notes, but keeps the charges (persian-martyr-acts bkv22 braun1915 l.12419 ff.; omissions noted at l.12442-12443, 13161-13162, 13270, 13319-13322, 13362-13363, 13806-13807, 14944-14947; the charges at l.13355-13400)". Nothing else in the note changes.
- Open-Gaps 251, "Not held": replace "which shortens the introduction and leaves out three passages" with "which shortens the introduction, leaves out four passages and gives two more only as notes".

**R3-B-M1 MINOR (`babai-the-great.card.json` `keyWorks` 2 `about`; checklist item 1; the R2-B-B1 card wording).**
- The card says "Oskar Braun translates the Life into German, shortening its long introduction and leaving out a few passages he judged of no substance."
- Braun calls two of the omitted passages of no substance: "sachlich belanglose" (l.13161) and "sachlich inhaltslosen" (l.13806). He gives no such judgment for the long encomium (l.13319-13322), the reflection (l.13270), the reflection on the times (l.13362-13363) or the prayer (l.14944-14947). The card gives him a reason he states for only two of six.
- "A few" is fair, and the card no longer says the Life is complete. So this is a loose attribution, not a false account of the source.
- Fix: "a monk of Izla, once a Magian named Mihramgushnasp, put to death under Khosrau. Oskar Braun translates the Life into German. He shortens its long introduction and leaves out or sums up several passages, two of which he calls of no substance. J.-B. Chabot gives two passages in French, among them the charges against Henana of Adiabene; Scher says Paul Bedjan published the Syriac"

**R3-B-M2 MINOR (`babai-the-great.card.json` `uncertain` 5; checklist item 4; R2-B-M2's split).**
- "The Arabic histories of Mari and 'Amr, in Enrico Gismondi's Latin, say the archdeacon Mar Aba and Mar Babai the Great governed the church while it had no head." This is 29 words. The writing standard asks for nothing past about 25.
- The content is right: Mari, "oius intoroa guberna- / tionom gorontibus Mar Aba arcliidiacono alquo Mar Babaoo Magno" (gismondi1899 l.13518-13519); 'Amr, "administravit ... Mar A!ia archidiaconus / una cum Mar iJabae-) ^lngno" (gismondi1896-1897 l.13425-13426).
- Fix: "His part in the vacancy. Thomas says three metropolitans asked him to visit the monasteries; the angel in Thomas's story calls him the vicar of the catholicos. The Arabic histories of Mari and 'Amr survive here in Enrico Gismondi's Latin. They say the archdeacon Mar Aba and Mar Babai the Great governed the church while it had no head. Mari counts seventeen years. J.-B. Chabot follows them."

**R3-B-M3 MINOR (Open-Gaps 251, "Correction to batch 5"; a line citation).**
- The clause cites "labourt1904 l.15763-15866". The batch 5 note it reports cites l.15764-15866. L.15763 ends the previous sentence of Labourt's note 4 ("de la foi faite au roi Chosrau en 612. Syn. ortent., p. 580-598 et 625-634."). The De Unione sentence starts on l.15764 ("Grâce à l'obligeance de M. Chabot...").
- Fix: "(labourt1904 l.15764-15866)".

The other changed strings check:
- Moschus: "traveled" (`knownFor`, `uncertain` 4) and "defense" (`legacy.remembered` 1) are our prose, not quotations. The two removed `"date": null` keys left `title`, `author`, `language` and `file` as they were.
- Severinus: only the `date` key on the Gregory the Great source went; nothing else changed.
- Babai: `legacy.traces` 1 "held in honor" is our paraphrase of Thomas, not a quotation. `uncertain` 1, 4 and 6 read cleanly at their new splits, with no beat lines or AI tells.

`tools/check_spelling.py` on the three briefs, cards, audio scripts and `records.json` finds no British spelling.

### 3. The batch 5 change

`git diff origin/main -- Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch5/` is one line in `records.json`: the `note` of `henana-of-adiabene` `absent_details` 3, "A second witness to Babai's doctrinal charges". No other batch 5 file differs. The batch 5 brief and card are untouched.

The note checked clause by clause:
- "Both held texts that state the charges are Babai's own" is true.
- The De Unione part is true: "Grâce à l'obligeance de M. Chabot, nous sommes en mesure d'adjoindre / à ces textes un traité inédit de Babaï sur l'Incarnation (De unione)" (labourt1904 l.15764-15765), and the Henana footnote at l.15816-15820.
- The Braun part is true except the count (R3-B-B1). The charge "Er leugnet die Auferstehung der Leiber" falls inside the cited l.13355-13400.
- The Hoffmann extracts (hoffmann1880 l.5596-5612), Chabot's passages (chabot1902 l.42080-42240), the Evagrius commentary not held, and Seert's unnamed "doctrines heretiques" all stand as R2 found them.

Verdict on the note: NOT YET TRUE, until R3-B-B1's count is fixed.

### 4. Open-Gaps 251 and the README

**"Correction to batch 5".**
- The old note did say the De Unione was "not held": "Babai's De Unione and Evagrius commentary are cited by Braun and Labourt but not held".
- "held in part, as Labourt quotes it in French": true, but the line cited should be 15764 (R3-B-M3).
- "held in Chabot's two French passages and in Braun's abridged German": true. It leaves out Hoffmann's extracts, which the note names, but that is incomplete, not false.
- "Only that absent_details note was changed": true by the diff. The note sits at `absent_details/3`.
- "by the coordinator's call of 2026-11-14": the R1 changes, part B, record the change. I found no separate record of the call to check against.
- "the brief and card of batch 5 are unchanged, and the point that the charges rest on Babai alone still holds": true. The batch 5 card `uncertain` 2 and brief l.9 still say the charges "rest on Babai the Great alone", and both held texts that state them are his.

**"Card tradition" (Severinus).**
- The supplement scan's row: "Early Benedictine Italian Monasticism; Gothic Homoian Christianity" (`Build/Ministry/Operations/Audits/2026-11-12_who-scan-supplement/Who_Scan_Supplement.md` l.138). The clause gives the census names, which are "Early Benedictine / Italian Monasticism" and "Gothic, Vandal & Lombard Homoian Christianity" (`cic-website/data/world-census.json` l.39201, 40509).
- "He was Catholic": Eugippius, "in the confession of the Catholic faith" (robinson1914 l.796).
- "the second placing comes only from the Rugians he lived among, by George W. Robinson's reading of Eugippius": Robinson's note, "makes it / evident that the Rugii, or at least their sovereigns, were ... Christians / of the Arian sect" (l.1305-1308). Both corpus-map rows give the same reason: "for the Homoian entry (the Rugian court). One provisional row for both" (`cic/corpus-map/early-benedictine-italian-monasticism.yaml` l.110; `gothic-and-vandal-homoian-christianity.yaml` l.58).
- "His card reads 'Early Benedictine / Italian Monasticism'": true (card l.9).

The clause is true.

**Other 251 clauses on these three.**
- "List lines": Moschus has a people row (`movements/47/people/4`). Babai appears only as a voice (`movements/44/voices/3`). Severinus is not in the census (no "Severinus" in `world-census.json`). All true.
- "Not held": Photius's codex 199 matches the records absent detail and Lipomanus's "Photius, cod. 199" (pg87-3 l.3440). The Babai clause carries the count fixed under R3-B-B1.
- "Scan corrections": the Moschus "c.550-619" is the file header's ("John Moschus (c. 550-619)"). Budge's "flourished about A. D. 569 — 628" is at budge1893 l.2068. The Severinus "about 482" is Robinson's table. All match the cards.
- The entry's Source line cites a Decision-Log entry "Who profiles, era 3 batch 6", which `Decision-Log.md` does not yet hold. That belongs to the lead before merge and is not a part B finding.

**README.**
- l.5 lists Moschus (619) and Babai (628) in the scan's order, and Severinus among the supplement rows. True.
- l.7: Babai is major; Moschus is a recorder at standard length. True.
- l.9: the Severinus sentence matches the scan and the card, and "The correction is logged in Open-Gaps" is now true (251).

### 5. Mechanical checks

- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each has one of each tag.
- `grade_text`, run from the repo root:

| Profile | Words | FK | Flesch | Cap |
|---|---|---|---|---|
| John Moschus | 325 | 7.1 | 68.0 | 325 |
| Babai the Great | 404 | 6.8 | 73.0 | 405 |
| Severinus of Noricum | 324 | 7.0 | 69.0 | 325 |

- All three cards and both `records.json` files parse as JSON.

### Verdict per profile

- John Moschus: **CLEAR**. Only spelling and empty `date` keys changed, and both are right.
- Babai the Great: **NOT CLEAR** on R3-B-B1. The fault is in the records entry, not the card or brief. The brief is unchanged and clear. The card's minors are R3-B-M1 and R3-B-M2.
- Severinus of Noricum: **CLEAR**. B-M13 is resolved by Open-Gaps 251.
- Batch 5 `henana-of-adiabene` note: the only batch 5 change. **NOT YET TRUE** until R3-B-B1 is applied.

### Totals

R2 part B findings: R2-B-M1 and R2-B-M3 resolved. R2-B-M2 resolved, with one sentence still long (R3-B-M2). R2-B-B1 partly resolved (R3-B-B1, R3-B-M1). B-M13 resolved. New: 1 blocking (R3-B-B1) and 3 minor (R3-B-M1 to M3).

## R3 recheck, part C: era 3 batch 6

Scope: `constantius-of-lyon`, `faustus-of-riez`, `gennadius-of-marseilles` and `ruricius-of-limoges`, with their briefs, cards, audio scripts and `records.json` entries in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`; the clauses of Open-Gaps 251 and the batch README on these ids. Round 3 of 3, a targeted recheck.

### Method

I am a fresh Opus reviewer. I did not draft, review or fix these files in rounds 1 or 2. I read `CLAUDE.md` in full, part C of `R2_recheck.md` and `R2_changes.md`, and the brief for this round. I read every change since R2 began as a word diff from `1304da0b` ("R2 recheck, parts B and C") to HEAD (`c7b84b31`). The four `records.json` entries were diffed one by one by script. The diff holds the R2 fixes, the lead's removal of empty `"date": null` keys, and the American-spelling pass. For every R2 finding, and for every changed string, I opened the cited lines in the vendored file myself and asked who speaks there: the ancient writer, an editor, a note or an apparatus. I read the Open-Gaps and README clauses against the cards, the records, `cic-website/data/world-census.json` and `cic/corpus-map/`. I edited no profile file, and made no git write, model, web or paid call. Line numbers point to files under `cic/texts/` unless another path is given.

Mechanical checks, all four:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each has one of each tag, and no tag appears in a brief.
- All four cards and `records.json` parse.
- `tools/check_spelling.py` on the four briefs, four cards and `records.json`: 0 British spellings. The spelling changes are all in our own prose or in modern renderings: "labor" (Faustus brief, inside Opus's modern rendering, so American spelling is right), "favored" (Faustus card and records paraphrase), "harbor" (Ruricius brief), "catalog" (Gennadius card and records paraphrase). No verbatim quotation from an edition was respelled.
- The removed `"date": null` keys leave every entry with title, author, language and file. No other field moved.

| Profile | Words | Est. @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Constantius of Lyon (recorder) | 323 | 2:00 | 8.0 | 66.1 | within 325 |
| Faustus of Riez | 324 | 2:00 | 8.1 | 63.1 | within 325 |
| Gennadius of Marseilles (recorder) | 325 | 2:00 | 8.2 | 64.0 | 325, at the cap |
| Ruricius of Limoges | 324 | 2:00 | 7.3 | 66.8 | within 325 |

### 1. R2 findings

| Finding | Status | Evidence |
|---|---|---|
| R2-C-M1 (Constantius card `uncertain` 6) | RESOLVED | The item now reads "…he reverses this, and holds that the writer of that Life… drew on Gregory." and "Levison also says the text in common use was a much-interpolated second Life, and Duru's edition reprints that second Life." Levison: "Vita altera admodum interpolata" (levison1920 l.659-661); "Textum vulgatum interpolationibus refertum esse" (l.703); "Vitae Germani secundae (§ 18 — 37, AA. SS. Iulii VII, 206 — 210; Duru l. l I, 57— 66)" (l.599); Duru "editionem Boschianam iteravit" (l.1619-1621). The colon-reveal is gone and no sentence runs past 25 words. Records side 2 carries the Duru clause with l.599, 1620-1621. |
| R2-C-M2 (Constantius records, citation lines) | RESOLVED | Krusch's note 2, "Hoc caput Gregorius fere ad verbum cum Vita S. Germani Autisiod. a Constantio composita convenit; lib. I, c. 7, Duru" stands at arndt-krusch1885 l.44307-44310 (OCR "llnc capnt Grcgnrins"). "lam jiuUus dubito" is at l.66258, and the page head "ADDENDA ET EMENDANDA. 883" at l.66231. |
| R2-C-M3 (PL 48: a dissertation, not a note) | PARTLY | The card `uncertain` 2, the records claim and its witness, and the first mention in `absent_details` now say "dissertation". Heading confirmed: "APPENDIX SECUNDA … DISSERTATIONES SEPTEM" (pl48 l.18388-18399). The same `absent_details` note still closes "Rees and the PL 48 note call him priest" (R3-C-M1). |
| R2-C-M4 (Constantius sources) | RESOLVED | Both entries are in `sources.about` and both files exist. The PL 48 entry has no `date` key, under the lead's ruling. Rees's words "the life of Saint Germanus, written by Constantius, a priest of Lyons" (rees 1853 l.17717-17718) stand in his note to the Life of Cadoc, so "notes" in the title is right. |
| R2-C-M5 (Ruricius brief: "he held nothing against him") | RESOLVED | Brief l.1: "Yet Caesarius held nothing against him." Engelbrecht l.24713-24716, "nihil pietati vestrae vel potuimus vel debuimus inputare". The audio script matches. |
| R2-C-M6 (Ruricius records: era 644) | PARTLY | The era figure is now explained, and the card no longer says the acts give 506. But the new parenthesis says "Bruns gives the variants 643 and 543" and cites l.13760 as a print of the Agde heading. Line 13760 is in Bruns's apparatus to the Council of Vaison II, not Agde (R3-C-B1). The card's new sentence also runs 34 words (R3-C-M2). |
| R2-C-M7 (review history inside records claims) | RESOLVED | All six parentheses and asides are gone. A search of the four entries for "R1", "R2", "brief now", "first search", "review" and "coordinator" finds nothing. The epilogue claim keeps "the brief gives this in Opus's modern English", as the finding allowed. |

R1 C-M7 (logging the truncated Levison file) is now Open-Gaps 251's Library clause; see section 3.

### 2. The "in 506" question

**The question.** In R2 the era printed with the Agde acts, 644, gives AD 606. So the records retagged 506 as Engelbrecht's reckoning, and the card dropped "whose acts date it to 506". The Ruricius brief still says "in 506" with no source named. Is that fine?

**Judgment: it is fine as told. No change to the brief.** The year is not one editor's guess. Three held witnesses give 506, and none of the held sources gives a different year:

- **Bruns's own dating apparatus.** Bruns heads the council "CONCILIUM AGATHENSE" with no year (l.10481). His note 3 gives the codices' datings (l.10498-10501): "Conc. Agath. viginti quinque episcoporum habitum era 644 [643 JE.], Anno vicesimo secundo Alarici regis sub die tertio Idus Septembris … Messala v. c. consule habet Corbej., Jes. A, B, Reg. B; in aliis deest nota consularis" (OCR "tertiq", "Septenibris", "CQnsvlm"). "JE." is one of his Spanish codex sigla (compare "JE. BR. E. 3. T. 1. 2.", l.882). So the era and its variant come from the Spanish codices, and the consul from the Corbie, Jesuit and Reg. B copies. Bruns's own year is in his table of contents: "LXXI(XLVII) Can. Conc. Agathensis . . a.506 145" (l.22833), and again in his index, "…gattieiise «. 506 n. 145" (l.22953, OCR).
- **Engelbrecht:** "anno enim 506 (sub d. III Idus Septembris Messala u. c. consule…)" (engelbrecht1891 l.2933-2934).
- **The unsigned PL 67 prolegomenon**, already among the Ruricius card's sources: "Anno 506 Caesarius ad concilium convocavit episcopos" and "sub die III idus Septembres, Messala V. C. consule, id est anno Christi 506, Alarici Gothorum in Gallia regis 22" (pl67 l.96489-96496; OCR "Ciesarius", "Chiisti", "Alariei").

The consul Messala fixes the year. The era figure is a scribal fault in the Spanish copies, not a rival dating. A brief may give an agreed year as a plain date, as other briefs in this series do. The card's "which August Engelbrecht reckons as 506" names one witness of three. That is true and not misleading, so I raise no finding on it. The records retag to Dominant Modern Reconstruction is cautious but defensible. A change of tag now would be churn, so I do not ask for one. The records should name all three witnesses, though, and they should drop the wrong "543" (R3-C-B1).

### 3. New findings

One blocking point in the records and one in Open-Gaps 251; three minor, and one note that is not a finding. None touches a brief, an audio script or a card fact.

**R3-C-B1 BLOCKING (Ruricius records, claim "Agde 506": a variant cited from the wrong council's apparatus).**
Evidence: the R2 parenthesis reads "Bruns gives the variants 643 and 543", and the witness cites "bruns … l.10498-10500, 13760". Line 13760 is not a second print of the Agde heading. It is note 1 to "CONCILIUM VASENSE SECUNDUM" (heading l.13728, running head "CONCILIUM VASENSE II." at l.13711), on the canon "Ut presbyteri per parochias juniores lectores domi nutriant" (l.13739): "decem et septem episcoporum add. solus Reg. F; viginti quinque episcoporum habitum era 644. [543. JE.] Codd. Hisp." That is Bruns's apparatus to Vaison II (529). For Agde, Bruns gives only 644 and "[643 JE.]" (l.10499). R2's own evidence for this finding called l.13760 "Bruns's second print of the heading". This is the slip, and the change copied it forward. A checker who follows the citation lands on another council. The brief and card do not depend on it.
Fix, in the claim, replace the parenthesis "(the era figure as printed, 644, gives 606, not 506, and Bruns gives the variants 643 and 543; the year rests on the twenty-second year of Alaric and the consul Messala, which Engelbrecht reckons as 506, l.2933-2934)" with:
"(the era figure of the Spanish codices, 644, gives 606, not 506, and Bruns's codex JE. reads 643; the year rests on the twenty-second year of Alaric and the consul Messala, which Engelbrecht reckons as 506, l.2933-2934, as do Bruns's own table, 'Can. Conc. Agathensis . . a.506', and the PL 67 prolegomenon, 'Messala V. C. consule, id est anno Christi 506' (OCR 'Chiisti'))".
Witness, replace with: "Bruns, Canones II (bruns_canones-apostolorum-et-conciliorum-pars-altera-lat_1839 l.10498-10501; table of contents l.22833); Engelbrecht (faustus-riez engelbrecht1891 l.2933-2942); prolegomenon, PL 67 (facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865 l.96489-96496)". Keep the tag as it is.

**R3-C-B2 BLOCKING (Open-Gaps 251, "List lines": a false absence for Constantius of Lyon).**
Evidence: "Constantius of Lyon, Severinus of Noricum and Ruricius of Limoges are named nowhere in the census." The census names Constantius of Lyon in two person entries. In Germanus of Auxerre (`movements[463]`, id `germanus-of-auxerre`), the long description has "Now, Constantius of Lyon writes, Germanus…". The card has "Constantius of Lyon wrote his Life, by Levison's date about 480 or a little after" (`legacy.remembered` 1), "Bede took the British chapters of Constantius of Lyon's Life…" (`legacy.traces` 1) and "Most of his story comes from Constantius of Lyon's Life…" (`uncertain` 0). It also lists him as the author of a source. In Hilary of Arles (`movements[464]`), `legacy.remembered` 0 reads "Constantius of Lyon, in his Life of Germanus of Auxerre, calls him…". He has no people row and no voice. A search of the census for Ruricius and for Severinus finds nothing, so those two halves stand. The map Who build slice is told to place him as if he were new to the census, when two entries already cite him.
Fix: "Constantius of Lyon has no people row, but the Germanus of Auxerre entry and the Hilary of Arles card name him as the writer of the Life of Germanus. Severinus of Noricum and Ruricius of Limoges are named nowhere in the census."

**R3-C-M1 MINOR (Constantius records, `absent_details` "His family, birth, death, orders"; R2-C-M3 left half-done).**
Evidence: the note now says "Marius Mercator PL 48, an unsigned dissertation calling him 'Constantius presbyter'", but closes "Rees and the PL 48 note call him priest, Isidore bishop."
Fix: "Rees and the PL 48 dissertation call him priest, Isidore bishop."

**R3-C-M2 MINOR (Ruricius card `uncertain` 2; the new sentence runs 34 words, with a loose "which").**
Evidence: "Its acts date the council to the twenty-second year of King Alaric, with the consul Messala in some copies, which August Engelbrecht reckons as 506; the Spanish era printed with them, 644, does not fit that year." "Which" can attach to "some copies" as easily as to the date, and the semicolon joins two thoughts (`Who_Profile_Pattern.md` item 4; CLAUDE.md, nothing past about 25 words). The facts are right: Bruns has the consul only in "Corbej., Jes. A, B, Reg. B; in aliis deest nota consularis" (l.10500-10501).
Fix: "Its acts date the council to the twenty-second year of King Alaric, and some copies add the consul Messala. August Engelbrecht reckons this as 506. The Spanish era printed with the acts, 644, does not fit that year." The rest of the item is unchanged.

**R3-C-M3 MINOR (Open-Gaps 251, "List lines" on Faustus: an unchecked "only", and a census error it should log).**
Evidence: "Faustus of Riez is named only in the text of the Gallic monastic entry". He is also named in the note on the link `gallic-monastic-ascetic-christianity--merovingian-gallic-christianity` (`edges[26]`): "Gennadius tells of Faustus, the first abbot of Lérins, who became bishop of Riez." That note misreads Richardson's English. Richardson has "Faustus, first abbot of the monastery at Lerins, and then made bishop of Riez" (npnf203 l.43682-43686), meaning first abbot and then bishop, and his own note reads "Abbot of Lerins 433–4". Engelbrecht's index has "Honoratus primus abbas Lirinensis" (engelbrecht1891 l.28706), and the census's own Gallic monastic entry says Honoratus founded the house.
Fix, in "List lines": "Faustus of Riez is named in the text of the Gallic monastic entry ("Faustus, later became bishop of Riez") and in the note on the link from it to Merovingian Gallic Christianity; the Faustus people row is Faustus of Milevis." In "Census text", add: "The note on the link from Gallic Monastic-Ascetic to Merovingian Gallic Christianity calls Faustus "the first abbot of Lérins". It reads Richardson's "first abbot of the monastery at Lerins, and then made bishop" (npnf203 l.43684-43685) as an order of abbots. Honoratus was the first abbot ("Honoratus primus abbas Lirinensis", Engelbrecht's index, engelbrecht1891 l.28706), as the Gallic monastic entry itself says. Owner: the coordinator, for the census text."

**Note, not a finding (Bruns on the Alaric year).** I record one point so a later reader does not re-raise it. Bruns's note may mean that the Alaric year, like the era, stands only in the Spanish heading ("cum in nonn. Codd. Hisp.", OCR "noni."). The OCR does not settle this, and the PL 67 prolegomenon gives Labbe's title with both the consul and "Alarici … regis 22". The card's "Its acts date the council to the twenty-second year of King Alaric" is therefore supported as worded.

### 4. Open-Gaps 251 and the README

Clauses on part C ids, each checked against the files:

- **List lines.** Faustus: see R3-C-M3. The Faustus people row is Faustus of Milevis (`movements[10]`, Manichaeism) ✓. Gennadius: no people row or voice, and he is named only in text ✓. Constantius: false absence (R3-C-B2). Ruricius: named nowhere ✓.
- **Card tradition.** Constantius's card reads "British and Welsh Christianity". The Germanus of Auxerre entry is `toldWithin: british-welsh-christianity` ✓. Constantius is called "a man of Lyon" ✓ (card `place`, "Lyon, in Gaul"). Ruricius's corpus-map row `faustus-riez_de-gratia-and-collected-works_engelbrecht1891--ruricius-limoges-letters` has `confidence: needs-ruling`, and its note says "Which Gaul entry holds him is a needs-ruling" (`cic/corpus-map/merovingian-gallic-christianity.yaml` l.67-74) ✓. His card reads "Merovingian Gallic Christianity" ✓.
- **Library (the truncated Levison file): correct.** I checked the truncation two independent ways.
  - Bytes: `od -c` on the last 300 bytes ends "E t   i d e o   i n   s c r i b e n d o   s u c c i n c t u m ^ \n". The file has 4580 lines, and l.4580 is the last.
  - Structure: the page head "… AUCTORE CONSTANTIO. 283" is at l.4571, and the epilogue starts at l.4574 and breaks off mid-sentence. The only "Explicit" in the body after the header is a variant reading in the p.282 apparatus, "Explicit vita sancti Germani episcopi A 6" (l.4550). No EXPLICIT line and no p.283 apparatus follow.
  - The header promises the text "through 'EXPLICIT VITA SANCTI GERMANI EPISCOPI' (p. 283)", pp. 225-283, from archive.org `passionesvitaequesanctorum5` (header l.3, 7, 9) ✓.
  - "No profile claim rests on the missing text" ✓. The epilogue claim cites l.4574-4579, which is held, and the brief's rendering covers only "Deum testor … tacuisse" (l.4577-4579).
- **Not held.** The Library has no Sidonius file; the only Sidonius hits are in other works. His letters to Constantius and Ruricius come through Levison and Engelbrecht ✓. No English of Faustus, Ruricius or Constantius is held; Levison's header says no public-domain English exists ✓. Gennadius's works against the heresies and his letter to Gelasius are named as not held, consistent with the card.
- **Scan corrections.**
  - Faustus "c.405/410-c.490/495" is the header (engelbrecht1891 l.2). Engelbrecht: "Faustum non multo ante annum 410 natum esse statuam" (l.163); "Quo anno mortuus sit Faustus, prorsus incertum est" (l.365) ✓.
  - Gennadius "died 496": Richardson's note "Died 496." (npnf203 l.43968) and Jackson ✓. "Richardson thinks a later hand added it": "This compels the rejection of the paragraph on Gennadius himself as by a later hand" (l.38478-38479) ✓.
  - Constantius "fl. c.480" is Levison's date ✓.
  - Ruricius "c.440 to c.507" is the header (engelbrecht1891 l.2) ✓, and 485 is Engelbrecht's reckoning ✓.
  - "The Ruricius who signs councils in 535 and 541 is his grandson, by Leo's index to Fortunatus" ✓. Leo has "Ruricii episcopi Lemovicini. Eorum epitaphium IV, 5. [Ad alterum c. a. 507 mortuum … alter nepos illius interfuit concilio Arverno I. a. 535, Aurelianensi IV. a. 541, V. a. 549 per Bantaredum archidiaconum subscripsit]" (leo-krusch1881 l.53125-53130; OCR "Huricii", "51)7", ",541"). The card's `uncertain` 5 says the same and adds 549 through the archdeacon.
  - Faustus's "the semi-Pelagian reply" told as fact, against Engelbrecht ✓ (card `uncertain` 1; engelbrecht1891 l.652-670 per records). Constantius's "only near-contemporary Life" as an unchecked "only" is a description of the scan and is fair.
  - Caesarius is not named in the scan-corrections clause, so there is nothing to check there.
- **README.** Line 5 names Constantius, Severinus, Faustus and Gennadius as the first era 3 WHO rows of the supplement scan "by best held date", then Ruricius in Benjamin's place. That order matches the dates the cards give: c.480, about 482, c.490/495, 496, then c.507. The supplement scan rows (Who_Scan_Supplement.md l.136, 147, and the follow-up pass at l.38 for Ruricius) agree ✓. Line 7 makes Constantius and Gennadius recorders at standard length, and Faustus and Ruricius standard ✓. "None is a live person entry" holds for all four.

### 5. Verdicts

- **Constantius of Lyon: CLEAR.** One minor records wording (R3-C-M1). The Open-Gaps false absence (R3-C-B2) is in the tracking entry, not the profile.
- **Faustus of Riez: CLEAR.** The census point (R3-C-M3) belongs to Open-Gaps, not the profile.
- **Gennadius of Marseilles: CLEAR.**
- **Ruricius of Limoges: NOT CLEAR on one records point (R3-C-B1).** The brief, audio script and card are sound, and "in 506" stands. The records claim cites a Vaison II apparatus line as an Agde variant. The fix is a one-clause, ready-to-apply replacement. Since this is round 3, it goes to the cap ruling as a records-only correction. R3-C-M2 is a card sentence split with no change of fact.

Open-Gaps 251 needs R3-C-B2 and R3-C-M3 applied before it is committed as final.
