# R2 recheck: era 3 batch 1

Scope: only what changed, checked against `R1_review.md` and `R1_changes.md`. Text that did not change was not reviewed again. I read the changes as a word diff from `d68a0ae3` (parts A and B as R1 saw them) and `1ce276f4` (part C, `lazar-parpetsi`) to `0e61224d`, limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch1/`. The branch has one later commit, `2d11789d`, which changes one README sentence (the coordinator's confirmation of Lazar Parpetsi's mark); I read that too. `vakhtang-i-gorgasali` left on purpose (rescored STORY by the coordinator) and was not reviewed. I opened every new or changed sentence, quotation, identifier and records.json entry at its line in the vendored file. XML tags were stripped and whitespace collapsed, and I checked who is speaking at each line: the ancient writer, a document he quotes, the translator, an editor's note or apparatus. The OCR files (Langlois t2, Halm, Mesnage, Chabot's Synodicon and Michael, Gismondi, Labourt, Nau PO 9, Scher PO 4, Gelzer and Burckhardt, the Mekhitarist Italian) were read by line and searched tolerantly. I did not edit the drafts, and I made no paid calls, model-API calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given.

Mechanical checks, all ten:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, placed before the closing line. No tag appears in a brief or card.
- `grade_text` passes for all ten (FK at most 10, Flesch at least 60). Barsauma (61.7) and Timothy (61.9) sit nearest the floor.
- Sentences: no new or changed narrator sentence runs past about 25 words. The longest is Dioscorus l.11, "In it Dioscorus tells the empress Pulcheria she may take his throne of wood, but not the one the Messiah has prepared for him in heaven." (26 words). It is R1's own fix wording and within "about".
- `briefLength` matches on all ten ("about 2 minutes 30 seconds" on the five majors, "about 2 minutes" on the rest). All ten cards and `records.json` parse as JSON, and `records.json` has exactly the ten ids. Every `file` named in a card's sources exists under `cic/texts/`.

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Vardan Mamikonian (MAJOR) | 391 | 2:24 | 6.8 | 71.4 | 405, within |
| Dioscorus of Alexandria (MAJOR) | 398 | 2:27 | 7.2 | 68.0 | 405, within |
| Euthymius the Great | 321 | 1:58 | 7.2 | 68.2 | within |
| Timothy Aelurus (MAJOR) | 404 | 2:29 | 8.1 | 61.9 | 405, within |
| Elishe | 324 | 2:00 | 8.1 | 63.2 | within (unchanged) |
| Victor of Vita | 320 | 1:58 | 7.5 | 68.8 | within |
| Moses of Khoren | 323 | 1:59 | 7.1 | 68.9 | within |
| Barsauma of Nisibis (MAJOR) | 400 | 2:28 | 8.1 | 61.7 | 405, within |
| Narsai (MAJOR) | 403 | 2:29 | 7.1 | 66.3 | 405, within |
| Lazar Parpetsi | 325 | 2:00 | 8.0 | 66.4 | within "about" |

## 1. The 6 R1 blocking findings

| Finding | Status | Evidence |
|---|---|---|
| Vardan B1 (451 given to Lazar and Elishe) | RESOLVED | Brief l.9: "Lazar says the armies met near the village of Avarayr, on the plain of the Deghmut." Lazar: "près du village appelé Avaraïr, au centre de la plaine de Deghmoud" and "Le vendredi de la fête solennelle de la Pentecôte" (Langlois t2 l.40207–40214); no year. Brief l.13 now carries the year on the modern witnesses only: Ormanian "26th of May, 451" (l.2256), Neumann's margin "June 2." (l.4147), the note "(2 Juin) 451" (Langlois t2 l.40450–40451). Card `dates`: "Fell at Avarayr, by Elishe and Lazar of Pharp, who give no year." The records claim drops "In 451", and the contested claim on the day names all three modern dates and says "These are modern dates". |
| Euthymius B2 (who baptized Aspebetus told as settled) | RESOLVED | Brief l.7: "Cyril says Euthymius baptized the father as Peter. Louis Duchesne, in his history of the early church, says Juvenal of Jerusalem baptized him. Euthymius asked Juvenal for a bishop for the converts, Cyril says, and Peter became the first bishop of the Camps in Palestine." Duchesne: "Le patriarche de Jérusalem, Juvénal, le baptisa sous le nom de Pierre et le sacra évêque des Sarrasins" (tome 3 l.21192–21194). Cyril's side as R1 read it (Cotelier l.29081–29083, 30637–30645, 30777–30779). Card `knownFor` "by Cyril of Scythopolis's account". The records keep the claim Contested with both sides. |
| Victor B1 (the see on unanimous manuscripts; the 484 Notitia and Mesnage left out) | RESOLVED | Brief l.3: "Most manuscripts of his book call him a bishop of Vita; one reads Utica." Halm's apparatus: "uitensi (uitensis LR, vticensis p)" (Halm l.370); Petschenig's apparatus has no Utica reading (l.995–1068). Mesnage's "Certains manuscrits portent la variante Uticensis" cites "Edit. Halm, p. 1" (l.4246–4247), so "one" follows the apparatus both rest on. The Notitia: "Uictor uitensis non occurrit" (Halm l.5750), the bishops "qui Carthaginem ad reddendam fidei rationem a. 484 convenerant" (Halm preface l.89–91). Mesnage: "VICTOR Vitensis n'assista pas à la Conférence, mais s'enfuit en exil, où il écrivit son histoire en 488" (l.4244–4245). Card `dates`, `uncertain` 2 and 5, the Mesnage source entry and the new records claim (Dominant Modern Reconstruction) all give the identification and the exile as Mesnage's. |
| Narsai B1 (the History and the Cause given to one Barhadbeshabba) | RESOLVED | Brief l.7: "In Connolly's English of a chronicle of the school". Connolly: "a fragment of a chronicle by Barhadhbeshabba… of first-rate importance for the history of the Nestorian School of Nisibis. It deals with the foundation of the School" (l.270–274). Card `uncertain` 1: Nau "gives the History to Barhadbeshabba 'Arbaia, and the Cause… to Barhadbeshabba, bishop of Halwan in 605; he thinks it not impossible that they are one man." Nau: "Bar Hadbesabba Arbaia, qui etait eveque de Halwan en 605" (PO 9 l.31579–31580), the same bishop of Halwan "a ecrit la Cause de la fondation des ecoles" (l.31598, badly garbled OCR), "Il n'est pas impossible que notre auteur… soit encore identique a l'eveque de Halwan" (l.31601–31603). `uncertain` 3 and `legacy.traces` 1 now name the Cause; records claim 2 is Inferential-Thin. The two spellings of the epithet in the source authors are N4. |
| Lazar B1 (Neumann's "from 428 to 485" contradicts the absence claim) | RESOLVED | Neumann: "the history of Lazarus Barbezi, which includes the period… till the Margravate of Vahan, the Mamigonian, from 428 to 485" (eghishe_neumann1830 l.1017–1021), Neumann speaking in his preface. Card `dates`: "which a note in the French edition dates to 486 and Charles Neumann, in the preface to his English Elishe, to 485"; `uncertain` 2: "Charles Neumann has the History run from 428 to 485." Both give the year to the editor, not to Lazar. The Neumann source entry is added. The records `absent_details` note and the new claim ("an editor's date", Dominant Modern Reconstruction) match. |
| Vardan B2 (the dating given to Ghesarian) | PARTLY | The witness swap is gone. The Vardan brief no longer dates Lazar; the card has no dating sentence; the records claim reads "Victor Langlois places Lazar at the end of the fifth century or the start of the sixth", witness "Langlois's introduction to Lazar, signed V. L. (langlois t2 l.35079-35081, 35357)". The introduction is signed "V. L." (l.35357). The tag R1 asked for, Dominant Modern Reconstruction "as the Lazar record has it", was not applied: the Vardan record still has Widely Accepted for the same editor's date the Lazar record tags Dominant Modern Reconstruction (N1). |

## 2. R1 minor findings

**Batch and README**
- G1: RESOLVED. `records.json` has exactly the ten ids the README lists (checked by script).
- README-M1: RESOLVED, all three parts. (1) "Elishe, Euthymius the Great, Victor of Vita and Moses of Khoren are not. Lazar Parpetsi, who took Vakhtang I Gorgasali's place on 2026-11-14, is not major"; `2d11789d` adds "the coordinator confirmed that on 2026-11-14", which names who made the call. (2) "Vahan Mamikonian (about 505) is the next row by year and goes to batch 2" matches the scan's row 55, "c.430s-c.505", WHO (`Who_Scan_Era3.md` l.55). (3) "The ninth by that order, Vakhtang I Gorgasali (499)".

**Vardan Mamikonian**
- M1: RESOLVED. "Both historians write for the Armenian side, and his words come to us only as they wrote them."
- M2: RESOLVED. "the Persian king Yazdegerd" (Lazar "Iezdedjerd, roi de Perse", Langlois t2 l.40476, rough OCR).
- M3: RESOLVED. `uncertain` 4: "rests on Lazar of Pharp and on Charles Neumann's preface to Elishe."
- M4: RESOLVED on the attribution, which is now Langlois's (see B2). The cut brief sentence ("His translator, Samuel Ghesarian, places Lazar…") leaves l.1 ending "The Armenian historian Lazar of Pharp tells the scene." with no dangling reference.

**Dioscorus of Alexandria**
- M5: RESOLVED. "gives the charges from the council's own acts. By that record, Chalcedon convicted Dioscorus…". Evagrius: "a cursory statement of the more important points" of the acts (Walford l.3077–3093, as R1 read it).
- M6: RESOLVED. "In it Dioscorus tells the empress Pulcheria…" (26 words; see the mechanical note).
- M7: RESOLVED. Card `knownFor`: "by the council's letter for disobedience and for refusing its summons three times". The letter: "on account of your disregard of the divine canons, and of your disobedience… for even when called to answer your accusers three times… you did not come" (npnf214 l.20084–20092).
- The cut Leo quotation ("you and we ought to be at one in thought and act") leaves "Feltoe… says Leo wrote to him in 445 to lay down church rules", which still stands on Feltoe (npnf212 l.490–494, as R1 read it). The records keep the quotation.

**Euthymius the Great**
- M8: RESOLVED. "Sabas, a monk whose Life Cyril also wrote". Cyril: "in alio opere gesta praestantissimi Sabae" (Cotelier l.45698–45702, rough OCR "gefta preftantiflimi Sa-be").
- M9: RESOLVED. `uncertain` 2: "Cyril wrote in Greek. Every detail on this card follows Jean-Baptiste Cotelier's Latin translation of 1681." `uncertain` 4: "Cotelier's Latin gives his death in his ninety-ninth year, though…". No scan narration is left on the card.
- The cuts (the parents and the vision; the charge of the monasteries) leave no dangling reference. Both stay in the records claims (Cyril l.26817–26904, 27504–27508).

**Timothy Aelurus**
- M10: RESOLVED in brief, card `remembered` 2, `uncertain` 2 and records. Brief: "Evagrius, from that report, says some Alexandrians killed Proterius in the baptistery 'at the instigation of Timotheus.'" Evagrius's own narration: "some of the Alexandrians, at the instigation of Timotheus, according to the written report made to Leo, despatch Proterius" (Walford l.3641–3644). Card: the petition's own words, "Of all these transactions Timotheus was the guilty cause, and the skilful builder of the scheme of mischief." (l.3752–3754, inside the petition's closing quote mark). Exact.
- M11: RESOLVED in brief, card `dates`, `uncertain` 3, records claim and contested claim. Evagrius: "in the eighteenth year of his banishment" (Walford l.5394–5396); Zachariah: "When Timothy had completed eighteen years in banishment" (l.5219–5220).
- M12: RESOLVED. "the bishop of Alexandria whom Chalcedon had deposed"; "Evagrius of Epiphania calls him Aelurus, which E. Walford's English gives as 'the Cat.'" Evagrius: "Timotheus, surnamed Ælurus" (Walford l.3620–3621).
- M13: RESOLVED. `traces` 1 "after Dioscorus of Alexandria"; `traces` 2 "Peter, whom Evagrius calls Peter Mongus" ("Peter, surnamed Moneus", Walford l.5844, OCR; "Mongus", l.6793, as R1 read it).
- M14: RESOLVED. "Birth and the year of his death"; the note names the brother Anatolius at Evetts l.35202 ("lie and his brother Anatolius were banished", OCR). R1's l.35199–35200 was off by two lines; the records cite the right one.
- The cut Life of Peter sentence stays in card `uncertain` 2 and the contested claim.

**Elishe**
- M15: RESOLVED. "grandson of Sahak" has left the Elishe claim.
- M16: RESOLVED. "not in Neumann's or Langlois's translation".

**Victor of Vita**
- M1: RESOLVED in card `uncertain` 3 ("who names no town but says such people were still in Byzantium in his own day") and the records.
- M2: RESOLVED by the B1 deletion. The card keeps "Huneric's edict, which he copies" in `dates`, which names only the dated edict of 484 (Petschenig l.5428).
- M3: RESOLVED. The Tipasa claim is now "Victor reports that…", tagged Documented; the empty `contested_claims` and the new `absent_detail` "A test of the Tipasa report" match.

**Moses of Khoren**
- M1: PARTLY. Brief l.9, card `dates` and `uncertain` 1 read "Modern work argues for a later date, but the Library holds none of it", and the records `contested_claim` now says "No held line itself says the date is disputed; the Contested tag is the coordinator's call under the era 3 ruling." That part is done. The log R1 asked for ("README or Open-Gaps: log that the dispute rests on no held line") is not in the README, and `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` has no entry for it. `R1_changes.md` passes it on ("For the README or Open-Gaps"). It needs an Open-Gaps entry from whoever owns that file.
- M2: RESOLVED. "the Mekhitarist preface, citing the same writer, gives him a hundred and twenty years". Preface: "E cen- vcnl anni viss'egli" (ita l.163–164, OCR), footnote "Tommaso Arzcrunio lib. I" (l.181).
- M3: RESOLVED. "Victor Langlois places him at the head \"des historiens de sa nation\"." (Langlois t2 l.7938, exact).

**Barsauma of Nisibis**
- M1: RESOLVED. Card `uncertain` 3. Michael the Syrian, Chabot's note: "Le récit de Marouta, rapporté par Bar Hebraeus (loc. cit.) sans indication de l'origine, perd une grande partie de son autorité… par l'aveu sincère de l'auteur qui déclare l'avoir rédigé uniquement d'après des traditions orales, et plus d'un siècle et demi après les événements" (l.33472–33478). The note is Chabot's, and the oral tradition is Maruta's own avowal as Chabot reports it, which "written from oral tradition" tells fairly. The text it annotates is Maruta's letter on Barsauma and Babai (l.33433–33466; "Marouta, métropolitain de Tagrit", l.51652–51653). 'Amr: Babai's letter "ad Barsumam delata est, ut erat sigillo munita: hic autem, quin aperiret, eam ad Pherozem transmisit… Gabrieli medico suo interpretandam tradidit. At ille aliquid in interpretatione mutavit" (Gismondi 1896–1897 l.14049–14054, OCR). Labourt: "Barsauma ordonna de lui couper la langue… puis lui fit couper la tête" (l.8081–8090). The three source entries exist.
- M2: RESOLVED in the records. Labourt: "Nous ignorons la date de sa naissance. On doit sans doute la placer vers 415-420" (l.7738–7740); "Barsauma mourut entre 492 et 495" (l.8875).
- M3: RESOLVED. Chabot's "DEUXIÈME LETTRE, — Au vénérable ami de Dieu Mar Acacius" (l.35269) confirms the letters to Acacius; the first is to five bishops (l.35203–35205, as R1 read it).
- M4: RESOLVED. "Acacius of Seleucia-Ctesiphon" (brief l.1, card `knownFor`); "Narsai of Nisibis, then a teacher at the school of Edessa".
- M5: RESOLVED. "In his second letter, he told Acacius why he could not come." The second letter is addressed to Acacius (l.35269) and gives the drought and raids (l.35275–35334, as R1 read it). "The Romans blamed Barsauma." closes the paragraph and carries a fact.
- M6: PARTLY. Brief l.9 and the card text name "Barhadbeshabba 'Arbaia" for the History and "Barhadbeshabba, bishop of Halwan" for the Cause. That part is right. The source author fields, though, spell the epithet two ways (N4).
- M7: RESOLVED. "He passes on a report that Barsauma soon regretted it." Mari: "Ferunt Barsaumam mox factum doluisse" (Gismondi l.14363, as R1 read it). The hedge holds.
- M8: RESOLVED. The marriage claim is tagged Contested.
- The length change "Chabot dates his death only to after 491": Chabot "La date de sa mort est inconnue. Elle est postérieure à [4]91" (l.20210–20211, OCR "41"). It is faithful, and the records keep Labourt's 492 to 495 beside it.

**Narsai**
- M1: RESOLVED. "Theodulus, a disciple of Mar Diodore, blessed him and called him the tongue of the East and the poet of the Christian religion." Mari: "is quondam Theodulo Mar Diodori discipulo obvius fuerat a quo benedictus fuit appellatusque orientis lingua ac christianae religionis poeta" (Gismondi l.14346–14347). The one who met Theodulus is Narsai ("Mar Narses Ma'allaia oriundus: is").
- M2: RESOLVED. `name` "Narsai of Nisibis", `otherNames` "Narsai", "Narses"; brief l.1 "Barhadbeshabba 'Arbaia"; the README matches.
- M3: RESOLVED. Ma'alta is tagged Widely Accepted, with Mari ("Ma'allaia oriundus", l.14346); the wife's jealousy is Contested.
- M4: RESOLVED. Scher: "Il est donc inexact que Narsai et ses compagnons aient été tous ensemble expulsés d'Édesse en 457, comme le racontait Siméon de Beth-Arscham" (PO 4 l.20622–20623); "Si l'expulsion de Narsaï a lieu en 457" (l.20750). The card's "doubts that Narsai and his companions were expelled together in 457, as Simeon of Beth Arsham told it" keeps Scher's own scope, and the records side gives both lines.

**Lazar Parpetsi**
- M1: PARTLY. The schools are no longer put in the camp, and records claim 1 is right. The new brief wording moves "even in the camp" onto the psalms said while taking up arms (N2).
- M2: RESOLVED. "with leave from the patriarch Sahak the Great and from Mesrop Mashtots" ("auprès du patriarche saint Sahag", Langlois t2 l.35144).
- M3: RESOLVED. "Langlois says jealous clergy accused his teaching of going against the true faith, and Vahan listened to them." Langlois: "Ils dénoncèrent Lazare au marzban qui prêta l'oreille à la calomnie" (l.35222–35223). Dropping "Then," loses no fact.
- M4: RESOLVED. "suspecting that another writer had added them or a poor copyist had altered the text". Lazar: "un autre écrivain aura interpolé… ou bien un [copiste], incapable de transcrire exactement, aura altéré l'ouvrage" (l.35715–35720).
- M5: RESOLVED. "after the histories of Agathangelos and Faustus. In his own phrase, it was the work of his weakness." Lazar: Agathangelos "entreprit le premier d'écrire l'histoire d'Arménie" (l.35389–35390, OCR). The closing sentence carries Lazar's own phrase, so it is not a bare beat line.
- M6: PARTLY. Card `role` "by Langlois's account", the source entry and both records claims are right. Stephen: "gab ihnen zum Oberhaupt den Redner und Geschichtsschreiber Lazar Pharbeci" (gelzer1907 l.2933–2936); "Stephanus, fl. ca. 1000" (l.22). The new `uncertain` item says "instead", but nothing in the `uncertain` list says what it replaces (N3).
- M7: RESOLVED. "one of the two full Armenian accounts of the war of 451 that the Library holds".
- The length changes: "Lazar says Vahan ordered him to write the History, which ends on the day Vahan took the government of Armenia." Lazar: "Je consignerai tout ceci jusqu'au jour où Vahan… prit le gouvernement de l'Arménie; et là, je terminerai" (l.35445–35448). The end point is Lazar's own, so "Lazar says" holds for both clauses. The cut list of contents stays in the card's `knownFor` and `keyWorks`.

**Applied across the batch**
- "held" removed from the Victor, Narsai and Lazar cards: done. On the Lazar card, "The held French is a rough scan." became "The copy used here is a rough scan.", which keeps the build narration R1 removed from the Vardan and Euthymius cards (N5).

## 3. New findings

- **N1 MINOR (records.json, `vardan-mamikonian`; item 1; one claim tagged two ways).** The claim "Victor Langlois places Lazar at the end of the fifth century or the start of the sixth" is tagged Widely Accepted. The Lazar record tags the same editor's date Dominant Modern Reconstruction ("Lived at the end of the fifth century or the start of the sixth", witness "an editor's date"), and R1's B2 fix asked for that tag in the Vardan record too. Source: "Il vécut à la fin du cinquième siècle ou au commencement du sixième" (Langlois t2 l.35079–35081), in the introduction signed "V. L." (l.35357). Fix: `formation_confidence` "Dominant Modern Reconstruction" on that Vardan claim.

- **N2 MINOR (`lazar-parpetsi.brief.txt` l.1, audio l.1; item 1; a detail moved, carried by R1's own fix wording).** "Even in the camp, they said the psalms in their minds as they took up their weapons." Lazar puts the spiritual exercises in the camp and the psalms in the moment of arming, in two separate clauses: "ils suivaient les exercices spirituels même dans le camp… En prenant les armes, ils récitaient mentalement des psaumes" (Langlois t2 l.43192–43198). The records claim keeps them apart correctly. Fix, brief and audio: "They said the psalms in their minds as they took up their weapons." The camp detail stays in the records. Scored: 321 words (1:59), FK 8.0, Flesch 66.4 (`grade_text`).

- **N3 MINOR (`lazar-parpetsi.card.json` `uncertain` 4; items 4, 7; "instead" with nothing to point to).** "Stephen of Taron, an Armenian historian of about the year 1000, says instead that Vahan made him head of the monks of Surenay-Anapat." The item before it is about the childhood companion, Greece and Siunik; no `uncertain` item gives the Etchmiadzin post, so a reader does not see the two sides together. Fix: "Langlois says Vahan put him in charge of the mother church at Etchmiadzin. Stephen of Taron, an Armenian historian of about the year 1000, says instead that Vahan made him head of the monks of Surenay-Anapat." Langlois: Vahan "lui confia l'administration de la métropole" (l.35202); Stephen as above (gelzer1907 l.2933–2936).

- **N4 MINOR (`barsauma-of-nisibis.card.json` and `narsai.card.json`, `sources.about`; item 9; one epithet spelled two ways).** The History's author is "Barhadbeshabba 'Arbaia" and the Cause's is "Barhadbeshabba 'Arbaya, bishop of Halwan". These are two spellings of one epithet, and Nau gives it to both men: "Rarbadbesabba' 'Arbaia" for the History (PO 9 l.31560) and "Bar Hadbesabba Arbaia, qui etait eveque de Halwan en 605" (l.31579–31580). Scher's own title has "Mar Hadb$abba 'Arbaia, évèque de Halwan" (PO 4 l.656, OCR "$" for "š"); "BARHADBESABBA 'ARBAYA" is the series list (l.575). The card text keeps the two men apart by their works and the see, but the two spellings suggest they are also kept apart by the epithet, which the sources do not do (R1_changes, Barsauma M6). Fix, on both cards: the Cause entry's author becomes "Barhadbeshabba 'Arbaia, bishop of Halwan".

- **N5 MINOR (`lazar-parpetsi.card.json` `uncertain` 7; items 4, 12; status-announcement register on a participant card).** "The copy used here is a rough scan." is the same build narration R1 removed from the Vardan card ("in a rough French scan", M3) and the Euthymius card ("The scan is rough", M9). Fix: delete the sentence, leaving "Langlois says Samuel Ghesarian translated from the only printed text, the Venice edition, and that this text is faulty." (Langlois t2 l.35282–35287, 35346–35348, as R1 read it). The records already note the OCR faults (for example "OCR 'fiiiblesse', l.35413").

No new or changed quotation is misquoted. I found no new absence claim that a held file contradicts, no editor's date given to an ancient text, and no dropped hedge. Card, brief and records otherwise agree after the changes.

## Totals

R1 findings: of 6 blocking, 5 are RESOLVED and 1 is PARTLY (Vardan B2: the witness swap is fixed, the tag is not, N1). Of 43 minor, 39 are RESOLVED and 4 are PARTLY (Moses M1, the Open-Gaps log; Barsauma M6, N4; Lazar M1, N2; Lazar M6, N3). None is NOT resolved.

New: 0 blocking, 5 minor (N1 `records.json` Vardan; N2, N3 and N5 `lazar-parpetsi`; N4 `barsauma-of-nisibis` and `narsai`). Every fix above was checked against the line it cites, and the one brief fix (N2) was scored with `grade_text`.
