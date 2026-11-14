# R3 recheck, part B: era 3 batch 6

Scope: round 3, the last allowed. Part B covers `john-moschus` (recorder, standard length), `babai-the-great` (major) and `severinus-of-noricum` (standard), with their briefs, cards, audio scripts and `records.json` entries. It also covers the one change to `era3/batch5/records.json`, the batch README's sentences on these three, and Open-Gaps 251's clauses on them, with the "Correction to batch 5" and "Card tradition" clauses in full.

## Method

I am a fresh Opus reviewer. I did not draft or fix these files and had not seen earlier rounds. I read `R2_recheck.md` part B and `R2_changes.md` part B. I read every change since R2 as a word diff from `1304da0b` ("R2 recheck, parts B and C") to HEAD (`c7b84b31`), limited to the batch 6 folder and `era3/batch5/`. Under part B, these changed:
- the Babai card (R2-B-B1, R2-B-M1 to M3) and records entry (R2-B-B1, R2-B-M1)
- the Moschus card (American spelling: "traveled" twice, "defense"; two `"date": null` keys removed)
- the Severinus card (one `"date": null` key removed)
- the batch 5 `henana-of-adiabene` note (R2-B-B1)

No brief or audio script of the three changed. I opened each changed string at its line in the vendored file and checked who speaks there. Because R2-B-B1 turns on how much of the Life of George Braun leaves out, I read every footnote of Braun's in the Life (braun1915 l.12419 to the closing "Amen" at l.15452), not only the four R2 cited. Line numbers point to files under `cic/texts/` unless another path is given. I edited no file but this report, and made no git writes, model calls or web requests.

## 1. The R2 findings

| Finding | Status | Evidence |
|---|---|---|
| R2-B-B1 (Braun's Life of George called "whole") | PARTLY | "Whole" is gone from the card, both records entries and the batch 5 note. But the replacement wording counts the omissions, and the count is wrong. Braun passes over four passages, not three, and gives two more only as a summary note. See R3-B-B1. The card's new wording also gives Braun a judgment he makes on only two of them. See R3-B-M1. |
| R2-B-M1 (Guidi: the quarrel between the two men; line ranges) | RESOLVED | Card `uncertain` 1: "It tells of a quarrel between him and Babai the Little that lasted to the end of their lives." Guidi: "Salanas vero rixae amator iurgia multa magnasque contentiones / excitavit inter duas illas firmissimas religionis turres, duo Babhay, / nec conquievit aut desiit usque ad finem agonis , vitae asceticae, eorum" (chronica-minora-pars-prior-versio-lat_guidi1903 l.2050-2052). The records quotation matches the file, OCR space before the comma included. "cognominaverunt" stands on l.2064, "Seripsit autem" on l.2069. The witness now reads l.2032-2037, 2050-2064, 2069-2070. The contested claim and the Book III absent detail cite l.2036-2064. The Mari witness cites l.13517-13520, and "nobio Mar Abraliam" is on l.13520 (mari gismondi1899). |
| R2-B-M2 (long card sentences; "which" after Khosrau) | RESOLVED, one sentence still long | `legacy.traces` 4 now reads "...but helped them with his pen. Addai Scher dates the debate to 612." Seert: "Mar Babai '", qui n'avait pas pu se / rendre k cctte reunion k cause de sa faiblesse et de son kge avance, leur / avait ete dun grand secours par sa plume" (scher1919 l.29556-29558); "1. En 612" is Scher's note (l.29565). `uncertain` 6 is split as worded. In `uncertain` 5, the split R2 gave still leaves the first sentence at 29 words. See R3-B-M2. |
| R2-B-M3 (Labourt's word "lost in the scan") | RESOLVED | "a word before the dates cannot be read in the Library's text of his page." OCR: "Il mourut âgé de soixante-quinze ans, phone / 'entre 615 et 620." (labourt1904 l.17771-17772). |
| R1 B-B3 (Life of George held), carried by R2-B-B1 | PARTLY | As R2-B-B1 above. |
| R1 B-H1 (batch 5 note), carried by R2-B-B1 | PARTLY | As R2-B-B1 above. The rest of the note is true. See section 3. |
| R1 B-M13 (README: "logged in Open-Gaps") | RESOLVED | Open-Gaps 251, "Card tradition", now logs the Severinus change. See section 4. |

## 2. New findings in changed text

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

## 3. The batch 5 change

`git diff origin/main -- Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch5/` is one line in `records.json`: the `note` of `henana-of-adiabene` `absent_details` 3, "A second witness to Babai's doctrinal charges". No other batch 5 file differs. The batch 5 brief and card are untouched.

The note checked clause by clause:
- "Both held texts that state the charges are Babai's own" is true.
- The De Unione part is true: "Grâce à l'obligeance de M. Chabot, nous sommes en mesure d'adjoindre / à ces textes un traité inédit de Babaï sur l'Incarnation (De unione)" (labourt1904 l.15764-15765), and the Henana footnote at l.15816-15820.
- The Braun part is true except the count (R3-B-B1). The charge "Er leugnet die Auferstehung der Leiber" falls inside the cited l.13355-13400.
- The Hoffmann extracts (hoffmann1880 l.5596-5612), Chabot's passages (chabot1902 l.42080-42240), the Evagrius commentary not held, and Seert's unnamed "doctrines heretiques" all stand as R2 found them.

Verdict on the note: NOT YET TRUE, until R3-B-B1's count is fixed.

## 4. Open-Gaps 251 and the README

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

## 5. Mechanical checks

- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each has one of each tag.
- `grade_text`, run from the repo root:

| Profile | Words | FK | Flesch | Cap |
|---|---|---|---|---|
| John Moschus | 325 | 7.1 | 68.0 | 325 |
| Babai the Great | 404 | 6.8 | 73.0 | 405 |
| Severinus of Noricum | 324 | 7.0 | 69.0 | 325 |

- All three cards and both `records.json` files parse as JSON.

## Verdict per profile

- John Moschus: **CLEAR**. Only spelling and empty `date` keys changed, and both are right.
- Babai the Great: **NOT CLEAR** on R3-B-B1. The fault is in the records entry, not the card or brief. The brief is unchanged and clear. The card's minors are R3-B-M1 and R3-B-M2.
- Severinus of Noricum: **CLEAR**. B-M13 is resolved by Open-Gaps 251.
- Batch 5 `henana-of-adiabene` note: the only batch 5 change. **NOT YET TRUE** until R3-B-B1 is applied.

## Totals

R2 part B findings: R2-B-M1 and R2-B-M3 resolved. R2-B-M2 resolved, with one sentence still long (R3-B-M2). R2-B-B1 partly resolved (R3-B-B1, R3-B-M1). B-M13 resolved. New: 1 blocking (R3-B-B1) and 3 minor (R3-B-M1 to M3).
