# R2 recheck: era 4 batch 3

Round 2 is a targeted recheck by a fresh Opus agent that had not seen the drafting or round 1, at full effort. It covers all eight profiles and the README.

## Method

Reviewer: independent Opus, first sight of these files. I edited no profile file. I made no git commit and no web, paid or model call, and used local scripts only. Inputs: `R1_review.md` parts A and B, `R1_changes.md`, the review brief, era 4 batch 1's `R2_recheck.md` for form, and `git diff 00bc3cd4 4f7aa7ad` over `Who-Profiles/era4/batch3/` (word diff for briefs, cards and README; a per-claim diff of `records.json`, with `wilfrid-of-york` mapped to `wilfrid-of-ripon`). The working tree matches 4f7aa7ad for this folder.

I opened each cited line again in its vendored file under `cic/texts/` and read it in context, folding OCR noise, double spaces, hyphen breaks and Migne's and Raine's interleaved columns. Short names: GILES (Giles/Jane 1903), RAINE (Raine 1879), PLUMMER (Plummer 1896), WASS (Wasserschleben 1851), ALC (Alcuin PL 100-101), KYLIE, BUTE, WHITE (White 1920), STOKES (Stokes 1887), DUCH3 (Duchesne, Histoire ancienne III), WARREN, PL72, AASS3 (Acta Sanctorum March 3), ROBINSON (Eugippius 1914).

**Mechanical checks (all eight).** A script confirmed that each `audio/<id>.audio.txt` equals its brief with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, with one tag of each kind. No tag is in a brief or card. Every card is in Mark's order with no empty or null field. No brief or card sentence runs past 25 words. No "Wilfrid of York" or `wilfrid-of-york` is left in the batch outside the README's note on the scan's name. The approved Hild of Whitby texts use "Wilfrid of Ripon" for this man (hild-of-whitby brief P5, card `uncertain`), so the rename agrees with them.

| Profile | Words | Time @162 | FK | Flesch | Longest brief sentence |
|---|---|---|---|---|---|
| theodore-of-tarsus | 329 | 2:01 | 6.1 | 72.2 | 22 |
| willibrord | 332 | 2:02 | 6.4 | 74.4 | 25 |
| leoba | 337 | 2:04 | 6.8 | 71.4 | 25 (unchanged since R1) |
| wilfrid-of-ripon | 341 | 2:06 | 5.8 | 77.8 | 23 |
| muirchu | 336 | 2:04 | 6.3 | 74.6 | 23 |
| tirechan | 336 | 2:04 | 7.5 | 67.9 | 25 |
| cogitosus | 327 | 2:01 | 7.8 | 65.2 | 21 |
| cuthbert-of-lindisfarne | 335 | 2:04 | 5.8 | 79.1 | 21 |

All pass `grade_text` (FK 10 or below, Flesch 60 or above). The figures match `R1_changes.md`.

**Reading as a listener.** I read each brief whole once more. Each still reads as a story that opens on a scene, and the length cuts left no pronoun without its antecedent. Each card `uncertain` still opens on the brief's own caveat, though two say it in a stock form (R2-M7, R2-M8). The cuts did cost context in two places: Wilfrid's return to England (R2-M3) and the Ripon line on Cuthbert's card, whose new wording makes a false absence (R2-B1).

---

## 1. R1 findings

### Part A: Theodore of Tarsus, Willibrord, Leoba, Wilfrid of Ripon, README

| Finding | Verdict | Evidence |
|---|---|---|
| A-B1 (Stephen "alone" on the confession) | RESOLVED | "Alone" is gone from card `uncertain` 2 and from the records. Fridegod's heading "Quomodo a Theodoro archiepiscopo revocatus", with "Poenitet en, fili", is at RAINE l.13902-13945. Eadmer's "qui delictum quod jam olim in famulum Dei commiserat" is at l.17912-17917. Raine on their dependence: "Excerptis de libro Vite ejus flosculis" (l.2134) and "occasionally quotes from it" (l.2367). The brief P6 says "In Stephen's telling", which is still true. |
| A-B2 (Plummer on the wrong side) | RESOLVED | Plummer: "never even alludes to his penitential"; "extracts from earlier works including Theodore's"; "when Theodore's work was in existence" (PLUMMER l.11097-11106). Wasserschleben: "ebenso wenig Beda" (WASS l.1668). The card's two sentences are faithful, and the records move Plummer to "For". |
| A-M1 ("covered") | RESOLVED in the brief | "Among them were Easter …" is true to the ten chapters (GILES l.9301-9356). The card `keyWorks` 1 keeps the same fault (R2-M1). |
| A-M2 (Egfrid) | RESOLVED | Brief P6 and card `uncertain` 1 read "Egfrid, king of the Northumbrians" (GILES l.15365). l.15351-15353 is added to the records. |
| A-M3 (Hadrian on the card) | RESOLVED | "an abbat, called Hadrian, by nation an African"; "not far from the city of Naples" (GILES l.8736-8740). 23 words. |
| A-M4 (Chad cut short) | RESOLVED | "per omnes gradus ecclesiasticos ad sedem predictam plene eum ordinaverunt", the see being "Licitfelda" (RAINE l.5658-5665). |
| A-M5 (records) | RESOLVED | There is now a `contested_claim` "Who waited four months for the Roman tonsure", and l.15351-15353 is added. |
| A-M6 (cattle and spring) | RESOLVED | "ut nihil in ea vel animalium ibi pascentium … contingere auderet, nec … nisi tacens" (ALC l.55171-55185). The new sentence keeps the rule. |
| A-M7 (Radbod; Charles) | RESOLVED | "regem Frisonum Radbodum" (ALC l.55188-55199). "filium ejus Carolum regno patris potiri", Pippin's son (l.55346-55347). |
| A-M8 (picked triad; "his own people") | RESOLVED (wording varied, accepted) | Alcuin lists Rome, Milan, Agaunum, Poitiers, Tours, Paris and Reims, then says God gave each people "quo speciali gauderent patrono" (ALC l.56075-56108). So "the patron saints of many cities" is fair, and it names no picked list. "Nobis … qui nos in hoc sacratissimum ovile congregavit" (l.56110-56119) backs "the monks Willibrord gathered". |
| A-M9 (Mabillon's variant) | RESOLVED | "[Mab., die sexto Nov. id est viii Idus]" (ALC l.55794-55795). |
| A-M10 (records) | RESOLVED | Jane is added as a third side, and "His age when given to Ripon" is added. "statim ablactatum" is at ALC l.54877-54878, and "before he was seven" at BUTE l.93838-93841. |
| A-M11 (double stop) | RESOLVED | It is one full stop now. |
| A-M12 (Lul) | RESOLVED | "Lul was to follow him in Mainz" (KYLIE l.1753-1754). |
| A-M13 ("in a bracket") | RESOLVED | "In Germany, [in the eighth century,] the holy Virgin Lioba" (BUTE l.71414-71416). The new wording is plain. |
| A-B3 (Stephen "alone" on Iurmenburg, prison, Austerfield) | RESOLVED | Fridegod: "Quomodo Ermenburgis regine insidias passus est" (RAINE l.12983); "Quomodo in carcere lucem promeruit" (l.13626); "Qualiter dolose ad concilium episcoporum vocatus sit" (l.14067). Eadmer: l.16806, l.17385, and "in campo qui dicitur Eastre-" (l.18189-18190). Card `uncertain` 1 now puts the weight on Bede's silence, and the records mark the later Lives as drawing on Stephen. |
| A-B4 (namesake collision) | RESOLVED | The name, id and files are now `wilfrid-of-ripon`. The rename is carried into the Theodore brief P2, card `legacy.traces` 4 and `uncertain` 1, the Willibrord card `legacy.traces` 4, the records and the README. Ripon: GILES l.13995-13996, 14189-14191. |
| A-M14 (Stephen's churches and decree) | RESOLVED | "As bishop of York, Stephen says, …" (RAINE l.5827-5830, 6428-6444), and "Stephen says Agatho's synod ordered him restored" (l.7273-7280). |
| A-M15 ("asked to die") | RESOLVED | "wished": "being very desirous, though the bishop opposed it, to die with him" (GILES l.13983-13985). |
| A-M16 (Oswy, Egfrid) | RESOLVED | P3 now has "son of Oswy, king of the Northumbrians", and P5 "Oswy's son King Egfrid". The cut of "At home" in the same sentence made a new fault (R2-M3). |
| A-M17 (Theodore on the card; John VI) | RESOLVED | The card has "Archbishop Theodore of Canterbury". The records cite "Jean VI (701-706)" at LP1 l.4384. |
| A-M18 (Whitby contrast; Hild "host") | RESOLVED | "Haec ratio disciplinae Apostolicae sedis est, et pene totius mundi" (RAINE l.5143-5149); "presente … matre piissima Hilde" (l.5074-5075). |
| A-M19 (relics hedge) | RESOLVED | "Invenit autem presulis beata membra" (RAINE l.33985-33987), and Raine's "in the opinion of the writer the bones were those of Wilfrid senior" (l.2442-2443). It is split into two sentences. |
| A-M20 (otherNames) | RESOLVED | "Wilfred" (BUTE l.2420, 77642), "Wilfrithus" (RAINE, 29 lines), "Wilfridus" (AASS March 3 and others). |
| A-M21 (records) | RESOLVED | There is a `contested_claim` for Ripon's size, with "terra triginta mansionum" (RAINE l.4943-4944) and GILES l.13995, against l.7938-7940. Prison and Austerfield are retagged Documented as Stephen's, Eadmer's 634 Inferential-Thin, and l.15351-15353 is added. |
| A-M22 (README reason; log the call) | PARTLY | The README now reads "called none of the eight major (2026-11-14) … Medieval Irish Christianity has Adomnán of Iona", which is right. But `R1_changes.md` says "The call is logged in the batch's Decision-Log entry", and `Decision-Log.md` has no era 4 batch 3 entry yet (grep for "era 4" batch 3 and "none of the eight" finds nothing). Fix: put the call in the batch's entry when it is written. Until then, change "is logged" in `R1_changes.md` to "is to be logged". |
| A-M23 (README `date`) | RESOLVED | The README now reads "… a date, a language and its file under `cic/texts/`". |
| A-M24 (README datings) | RESOLVED | White: "not earlier than a.d. 664, possibly about a.d. 670" (WHITE l.1389-1390). Bury's 664-668 as White reports it (l.3596-3599). Stokes: "A.D. 683, apparently" (STOKES l.3224). |
| A-M25 (README names paragraph) | RESOLVED | It is true to the Hild texts and to the records' namesake note: "Wilfrid II, Hild's pupil and later bishop of York (GILES l.10973-10982, 12539-12541)". |

### Part B: Muirchu, Tirechan, Cogitosus, Cuthbert of Lindisfarne

| Finding | Verdict | Evidence |
|---|---|---|
| B-M1 (inner state; "track") | RESOLVED | "one sure track of history" (WHITE l.3794-3795); the apology closes "yet the feeling of my love is most pious" (l.3812). |
| B-M2 (hedge; Duchesne's 698) | RESOLVED | "The first book, at least, must have been published before A.D. 699; for Bishop Aedh … died in that year" (WHITE l.3592-3594). Duchesne: "dédiée à un évêque qui mourut en 698" (DUCH3 l.22836-22837). |
| B-M3 (stock opener; Sletty; Birr) | RESOLVED in the brief | "Sleibte (Sletty), on the borders of Co. Carlow"; "the Synod held at Birr, by Adamnan, a.d. 695-697" (WHITE l.3766-3770). The card keeps the stock opener (R2-M7). |
| B-M4 (Loiguire; festivals; Temoria) | RESOLVED | Tirechan's "he was unable to believe" is in White's note (WHITE l.6915-6921), and "Temoria = Tara." is at l.6548. The `contested_claim` is added. The Bury and Macalister sentences now sit on the card only, with "(or his source)" and Macalister's study of Tara (l.6550-6553). The joined Armagh sentence is nested (R2-M4), and the card's Muirchu side is short (R2-M6). |
| B-M5 (Aedh) | RESOLVED | It is "Aedh" throughout the brief and card. The records keep Stokes's "Aed" in one quotation, which is right, and in one `contested_claim` label, which is internal. |
| B-M6 (knownFor; keyWorks) | PARTLY | (a) is done. In (b), "lit before" and the comma are done, but the double stop is still there: "and his death and burial.. White says" (`muirchu.card.json` line 15). See R2-M5. |
| B-M7 (name note) | RESOLVED | "note appended to the Table of Contents of Book i. (printed here at the end of that book)" (WHITE l.3738-3740). Card and README match. |
| B-M8 (place of fire) | RESOLVED | The item is removed, and the record is retagged Dominant Modern Reconstruction. |
| B-M9 (Colgan) | RESOLVED | "A collection of seven ancient Lives of St. Patrick was published at Louvain in 1647 by John Colgan"; "Vita II, IV and V are largely based on Muirchu" (WHITE l.1478-1479, 1527). |
| B-M10 (Sechnall; Birr) | RESOLVED | "This is generally accepted as referring to the Hymn of St. Secundinus"; "probably had the fourth stanza of St. Sechnal's Hymn" (WARREN l.10589-10597). |
| B-M11 (pronoun; groups) | RESOLVED | "desertores et archiclocos et milites Hiberniae"; "si quaereret heres Patricii paruchiam illius" (STOKES l.2974-3015). "archrobbers" is in Stokes's index (l.20664). |
| B-M12 (Duchesne's reasoning) | RESOLVED | "déjà très embellies par deux siècles de conservation orale … il s'agissait de l'apôtre national, et aussi des intérêts de l'église d'Armagh" (DUCH3 l.22847-22852). The brief's "with Armagh's interests at stake" is a fair short form. |
| B-M13 (stock opener) | RESOLVED in the brief | The card keeps the stock opener (R2-M8). |
| B-M14 (plagues plural) | RESOLVED | "post mortalitates nouissimas" (STOKES l.3188-3189). One card item still says "most recent" (R2-M9). |
| B-M15 (hedges; page number) | RESOLVED ((c) in part, accepted) | "would be the earliest attempt" (WHITE l.1396-1398); "was probably due to the scribe" (l.7417-7418). Duchesne's "ce qui dépasse la p. 331, l. 9" (DUCH3 l.22844-22845) is now "the last part of the text". Stokes's Tirechan ends at about p.332, so that holds. The new sentence in (b) has a grammar fault (R2-M10). |
| B-M16 (Clono) | RESOLVED on the card | "sed quaerit familia Clono … per uim tenent locos Patricii multos post mortalitates nouissimas"; note "of Cluain (maccu Nois?)" (STOKES l.3187-3189, 3219). The records' witness for the spelling is wrong (R2-M11). |
| B-M17 (records) | RESOLVED | "The year Ultan died" is added: White 657 (WHITE l.1393-1394), Duchesne 656 (DUCH3 l.22835). Clono is retagged Inferential-Thin. |
| B-M18 (README) | RESOLVED | See A-M24. |
| B-B1 (Stokes's index) | RESOLVED | Both entries are on p.269 (STOKES l.21226, 22198), and "Muirchu Maccumachtheni, notes by, 269" is at l.21487. The second `contested_claim` is dropped, and the card no longer says "separately". The new card sentence gives the wrong reason (R2-M14). |
| B-M19 ("main source") | RESOLVED | Removed from the brief and `knownFor`. |
| B-M20 ("He") | RESOLVED | |
| B-M21 (Jacques Basnage; Canisius) | RESOLVED | "Henricus Canisius … This is found in the second edition of Canisius, by Jacques Basnage (Thesaurus Monumentorum …)" (ROBINSON l.4381-4385). Robinson is in the card's `sources.about`. |
| B-M22 (miracles in the monastery) | RESOLVED | "in suo monasterio ubi ejus venerabile requiescit corpus … oculis nostris vidimus" (PL72 l.59334-59337). `uncertain` 3's "in her church" is Basnage's own reading, "portenta quaedam in ejus templo operari solita" (l.58466-58468), so it stands. |
| B-M23 (jurisdiction; nepos) | RESOLVED | "cujus parochia per totam Hiberniensem terram diffusa" (PL72 l.58508); Stokes "Jurisdiction of Patrick (paruchia Patricii)" (STOKES l.20166). |
| B-M24 (inference; Basnage's placing; "stupendum") | RESOLVED | "Cogitosum hic reponimus, aliorum vestigiis insistentes potius quam nostrae sententiae addicti"; "Stupendum etiam … Haec enim legibus adversantur" (PL72 l.58442-58468). The records flag the approved Brigid card's reading for Open-Gaps, and the entry is due when the batch closes. |
| B-M25 (README Cogitosus) | RESOLVED | |
| B-B2 (Aidan timing) | RESOLVED | "post paucas dies" (AASS3 l.38829-38831) is in the brief P2, the card `uncertain` 4 and a `contested_claim` named as on the approved Aidan profile. |
| B-B3 (Bede's year) | RESOLVED | "The same year that King Egfrid departed this life, he … promoted to the bishopric of the church of Lindisfarne … Cuthbert" (GILES l.11559-11566); "In the year 685, Egfrid, king of the Northumbrians, was slain." (l.15365-15366). The edition's bracketed years are not cited. |
| B-M26 (Egfrid) | RESOLVED | "King Egfrid of Northumbria". |
| B-M27 (Whitby context) | DECLINED-OK | It was optional at the drafter's weight. P6's "keep Easter at the wrong time" is plain on its own. |
| B-M28 (last words narrowed) | DECLINED-OK | It was optional, as R1 allowed. |
| B-M29 (Ripon not used) | PARTLY | The item is added. But "Bede does not say so of him" is false (R2-B1). The History's `sources` title still lacks V.19, which R1 asked for (GILES l.13990-14001 is V.19), and `place` gives "Ripon" with no reason. |
| B-M30 (Eata; verse-Life item) | RESOLVED | "Eata, abbot of Melrose", and the item is deleted. |
| B-M31 (no-city tag) | RESOLVED | Retagged Documented, and the `contested_claim` is dropped. |

---

## 2. New findings

### Blocking

- **R2-B1 BLOCKING (Cuthbert card `uncertain` 7; records "Ripon in Bede's prose Life"; a false absence, made by the B-M29 fix).** The item reads: "Ripon. Bede says Eata took Cuthbert to found a monastery at Ripon. His History says the founders left rather than take the Roman Easter. The Bollandists count Cuthbert among them; Bede does not say so of him."
  - Bede's prose Life does say so. Two paragraphs after the founding, chapter 8 (AASS3 §14, l.34679-34684) reads: "praefatus Abbas Eata cum Cuthberto et ceteris, quos secum adduxerat, Fratribus domum repulsus est, et locus monasterii, quod condiderat, aliis ad incolendum monachis datus". So Eata, with Cuthbert and the other brothers, was driven home, and the place was given to other monks.
  - What Bede does not do is join the two accounts. The Life names Cuthbert but gives no reason. The History gives the reason, "would rather quit the place than adopt the catholic Easter" (GILES l.13996-14001), but names no one. The Bollandists join them: "SS. Eata, Cuthbertus aliique propter Pascha Catholicum … reliquerunt Riponense monasterium" (AASS3 l.33599-33601).
  - Fix, card: "Ripon. Bede says Eata took Cuthbert to found a monastery at Ripon. His History says the founders left rather than take the Roman Easter. The Bollandists count Cuthbert among them; Bede does not say so of him." -> "Ripon. Bede's prose Life says Eata took Cuthbert to found a monastery at Ripon, and that both were later sent home. His History says the founders left rather than take the Roman Easter. The Bollandists join the two accounts." (17, 13 and 6 words.)
  - Fix, records: in the claim "Ripon in Bede's prose Life", add "\"Abbas Eata cum Cuthberto et ceteris, quos secum adduxerat, Fratribus domum repulsus est\"" and the witness l.34679-34684. Keep Inferential-Thin for the Bollandists' joining.
  - Also, to finish B-M29: in `sources.about`, change "Ecclesiastical History, preface, III.26, IV.27-32 and V.24" to "Ecclesiastical History, preface, III.26, IV.27-32, V.19 and V.24". In `place`, either give the reason ("Ripon, where Eata took him to found a monastery") or leave the bare name, since `uncertain` now carries the reason.

### Minor

- **R2-M1 MINOR (Theodore card `keyWorks` 1; item 1; the A-M1 fault left on the card).** "They cover Easter, bishops keeping to their own dioceses, monks, wandering clergy, a yearly synod and marriage". These are six of the ten chapters. Chapter III (monasteries not to be troubled), VI (travelling clergy) and VIII (order of consecration) are left out (GILES l.9311-9351). Fix: "They cover Easter" -> "Among them are Easter".

- **R2-M2 MINOR (Wilfrid brief P2 and audio; item 4; a beat line made by a length cut).** "Bede is briefer." These three words end the paragraph as a beat, and they can be heard as describing Bede the man. Fix: "Bede is briefer." -> "Bede tells it more briefly." (+2 words.)

- **R2-M3 MINOR (Wilfrid brief P3 and audio; items 10 and 8; context lost in a cut, and an apposition that reads two ways).** "The executioners spared him … of the English nation. Alfrid, son of Oswy, king of the Northumbrians, gave him the monastery of Ripon."
  - Cutting "At home" means the brief no longer says that Wilfrid came back from Gaul. Bede: "Returning to England, he was admitted to the friendship of King Alfrid" (GILES l.13990-13991).
  - "Alfrid, son of Oswy, king of the Northumbrians" can be heard as making Alfrid the king.
  - Fix: "Alfrid, son of Oswy, king of the Northumbrians, gave him the monastery of Ripon." -> "Back in England, Alfrid, son of King Oswy of the Northumbrians, gave him the monastery of Ripon." (17 words.)
  - P4's "King Oswy" and P5's "Oswy's son King Egfrid" then read as later mentions.

- **R2-M4 MINOR (Muirchu brief P5 and audio; item 4; a nested sentence made by joining two).** "White thinks the Life was probably a tribute from Leinster to Armagh, whose bishop's claim to head the Irish church Aedh had accepted." The object comes before the verb inside a relative clause, which a listener cannot parse in one pass. "Accepted" is also softer than White's "made a formal submission to the primatial claims of its bishop" (WHITE l.3772-3773). Fix: -> "Aedh had submitted to Armagh's claim to head the Irish church, White says. He thinks the Life was probably a tribute from Leinster to Armagh." (13 and 13 words; it matches the card's `uncertain` 5.)

- **R2-M5 MINOR (Muirchu card `keyWorks` 1; B-M6 (b) left).** Fix: "and his death and burial.. White says" -> "and his death and burial. White says".

- **R2-M6 MINOR (Muirchu card `uncertain` 7; item 7; one side told by implication).** "Whether Loiguire believed. Muirchu has him say it is better to believe than to die." Muirchu goes on to say that "he believed on that day, by the advice of his friends" (WHITE l.4741-4744), and the records' side reads "and he believed". Fix: "Muirchu has him say it is better to believe than to die." -> "Muirchu says he believed that day, after telling his elders it was better to believe than to die." (19 words.)

- **R2-M7 MINOR (Muirchu card `uncertain` 1; items 12 and 4).** "Little is told of his own life." This is the witnessless stock opener that B-M3 took out of the brief, and Tirechan's card opens the same way (R2-M8). Fix: -> "Muirchu says almost nothing about himself.", which is the brief's own caveat word for word.

- **R2-M8 MINOR (Tirechan card `uncertain` 1; items 12 and 4; as R2-M7).** Fix: "Of his own life little is told." -> "Tirechan tells little of himself."

- **R2-M9 MINOR (Tirechan card `uncertain` 2; item 9).** "Stokes reads the most recent plagues Tirechan mentions". `dates` and `uncertain` 6 say "the latest plagues" for the same "mortalitates nouissimas". Fix: "the most recent plagues" -> "the latest plagues".

- **R2-M10 MINOR (Tirechan card `uncertain` 4; a grammar fault in the B-M15 (b) fix).** "White thinks the note on Patrick's burial at Saul probably Ferdomnach's too." The sentence has no verb. Fix: -> "White thinks the note on Patrick's burial at Saul is probably Ferdomnach's too."

- **R2-M11 MINOR (Tirechan records, claim "Clonmacnois spelled so by White"; item 5; wrong witness).** WHITE l.8554, "St. Ciaran of Clonmacnois. By R. A. S. Macalister.", is a book title in a publisher's list at the back of White's volume. It is Macalister's spelling, not White's. Fix: rename the claim "Clonmacnois, the spelling of R. A. S. Macalister's title as listed in White's volume". The card's spelling can stand, since a vendored file spells it so.

- **R2-M12 MINOR (Cogitosus brief P1 and audio; item 1; a length cut widened the source).** "Painted boards and pictures lined its walls." Cogitosus has the church "decorata pictis tabulatis", and then "unus paries decoratus, et imaginibus depictus": one wall painted with images (PL72 l.59429-59432). Fix: -> "Painted boards adorned it, and one wall bore pictures." (+2 words; the card's `legacy.traces` 2 already says "It had painted boards".)

- **R2-M13 MINOR (Cogitosus brief P2 and audio; item 4; "writer … wrote").** "The writer was Cogitosus, who wrote a Latin Life of Brigid of Kildare. It is a saint's Life, mostly miracles." Fix: -> "The writer was Cogitosus. His Latin Life of Brigid of Kildare is a saint's Life, mostly miracles." (-2 words; the card's `uncertain` 1 still matches.)

- **R2-M14 MINOR (Cogitosus card `uncertain` 5; item 1; the B-B1 fix gives the wrong reason).** "Both his index entries … point to the page of Muirchu's preface, so his reasoning cannot be read here." Pointing to that page is not what hides his reasoning. The page is missing from the held file (records `absent_details`). R1's wording said so. Fix: "point to the page of Muirchu's preface, so his reasoning cannot be read here." -> "point to the page of Muirchu's preface. That page is missing from the copy used here, so his reasoning cannot be read." (13 and 12 words.)

Brief fixes scored on scratch copies (`/tmp/claude-0/-home-user-CIC-Project/39eb9bee-a8ba-523c-9dfe-f5ca37666176/scratchpad/fixR2/`):

| Profile | Fixes | Words | Time | FK | Flesch |
|---|---|---|---|---|---|
| muirchu | R2-M4 | 338 | 2:05 | 6.1 | 75.2 |
| cogitosus | R2-M12, R2-M13 | 326 | 2:00 | 7.9 | 64.8 |
| wilfrid-of-ripon | R2-M2, R2-M3 | 346 | 2:08 | 5.8 | 77.8 |

Every brief fix has to be carried into the audio file.

---

## 3. Verdicts

| Profile | R1 findings | New blocking | New minor | Verdict |
|---|---|---|---|---|
| Theodore of Tarsus | 7 of 7 resolved (A-B1, A-B2, A-M1 to A-M5) | 0 | 1 (R2-M1) | NOT CLEAR |
| Willibrord | 5 of 5 resolved (A-M6 to A-M10) | 0 | 0 | CLEAR |
| Leoba | 3 of 3 resolved (A-M11 to A-M13) | 0 | 0 | CLEAR |
| Wilfrid of Ripon | 10 of 10 resolved (A-B3, A-B4, A-M14 to A-M21) | 0 | 2 (R2-M2, R2-M3) | NOT CLEAR |
| README.md | 3 of 4 resolved; A-M22 partly (Decision-Log step) | 0 | 0 | CLEAR for its text; the Decision-Log step is for the coordinator |
| Muirchu maccu Machtheni | 9 of 10 resolved; B-M6 partly | 0 | 4 (R2-M4 to R2-M7) | NOT CLEAR |
| Tirechan | 8 of 8 resolved (B-M11 to B-M18) | 0 | 4 (R2-M8 to R2-M11) | NOT CLEAR |
| Cogitosus | 8 of 8 resolved (B-B1, B-M19 to B-M25) | 0 | 3 (R2-M12 to R2-M14) | NOT CLEAR |
| Cuthbert of Lindisfarne | 5 of 8 resolved (B-B2, B-B3, B-M26, B-M30, B-M31); B-M27 and B-M28 declined-OK; B-M29 partly | 1 (R2-B1) | 0 | NOT CLEAR |

**Totals.** R1 had 63 findings: 58 resolved, 2 declined-OK (B-M27, B-M28) and 3 partly (A-M22, B-M6, B-M29). Round 2 found 1 new blocking finding (R2-B1) and 14 new minor ones (R2-M1 to R2-M14). Willibrord and Leoba are clear. Every quotation in the eight briefs still matches its vendored file. All eight briefs pass `grade_text` before and after the fixes, and every audio file equals its brief plus tags.

Round 2 is the second of the three review rounds the cap allows on each profile. R2-B1 came from a fix wording that R1 itself supplied and that was taken as worded. One fix reaches the cards and records only (R2-B1). Two reach the briefs and audio, and those are small changes (R2-M2 to R2-M4, R2-M12, R2-M13). A targeted round 3 on the changed strings should be enough.
