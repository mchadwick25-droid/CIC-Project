# R1 review: ten Who profiles, era 3 batch 1

Three independent Opus reviewers, each at first sight of its drafts, reviewed the batch in three parts: part A (Vardan Mamikonian, Dioscorus of Alexandria, Euthymius the Great, Timothy Aelurus, Elishe, and the README), part B (Victor of Vita, Moses of Khoren, Barsauma of Nisibis, Narsai) and part C (Lazar Parpetsi and the README, with a cross-check against the Vardan and Elishe profiles). Part B was asked to review Vakhtang I Gorgasali too; he was rescored STORY by the coordinator while the review ran and left the batch, so part B did not review him, and part C reviewed Lazar Parpetsi, who took his place. Totals: 6 blocking, 43 minor (part A 2 and 17, part B 2 and 18, part C 2 and 8). Each part follows as written.

## R1 review: era 3 batch 1, part A (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's rulings in the Decision-Log (2026-11-12: majors capped at 2:30, about 405 words, a cap and not a target; non-majors 1 to 2 minutes, at most about 324 words). I hunted hardest for the recurring faults of earlier batches: witness swaps, a modern date told as resting on an ancient text, an identification told as settled, absence claims a held file contradicts, common names without a place, partisan witnesses not marked, invented detail, and AI tells. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `vardan-mamikonian` (major), `dioscorus-of-alexandria` (major), `euthymius-the-great`, `timothy-aelurus` (major), `elishe`, and the batch `README.md`, with their entries in `records.json`. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch1/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13, 15). Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation in the five briefs and cards in the vendored file the card or records cite. The match stripped XML tags, collapsed whitespace, joined hyphenated line breaks and normalised quote marks. For the OCR files (Langlois's Armenian historians, Neumann's Elishe, Cotelier's Latin Cyril, Nau's Theopistus, Hamilton and Brooks's Zachariah, Evetts's History of the Patriarchs, Duchesne) I read each passage by line number and searched tolerantly. I read each hit in context to see who is speaking: the ancient author, a document he quotes, a translator's introduction or margin, a footnote (`<note>` in the npnf XML), or a bracket the translator supplied. I checked every factual sentence of each brief against its passage, searched before accepting each absence claim, and compared each `records.json` entry with its brief and card. Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute. Every suggested brief fix below was applied to a scratch copy and re-scored; the post-fix word count and scores are given with each profile.

## Applies to all five

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, placed before the closing paragraph or line. No tag appears in any brief or card.
- **Readability.** All five pass (FK at most 10, Flesch at least 60). Timothy Aelurus sits nearest the floor (Flesch 61.9). Narrator sentences past 25 words: Dioscorus l.11 (26 words; see M6). The other long sentences are mostly quotation (Vardan l.9, Dioscorus l.1, 9, 13, Elishe l.1).
- **Length.** The three majors run 402 to 405 words (2:29 to 2:30), under the cap. The two non-majors run 323 and 324 words (2:00). Every `briefLength` matches.
- **Card order.** All five follow Mark's order. Missing fields are left out: Vardan and Euthymius have no keyWorks, and only Dioscorus, Timothy and Elishe have "Their own words". keyWorks never goes past three. Each `uncertain` list opens with the brief's main caveat. The `"date": null` in source entries is the schema the earlier batches used.
- **Sources lists.** Each card lists the works its brief and card rest on (Eudocia's "widow of Theodosius II" rests on Duchesne, who is listed; Timothy's Feltoe dates rest on npnf212, which is listed).
- **Who test (item 14).** Vardan is known through Elishe and Lazar of Pharp and kept as a saint (Ormanian). Dioscorus is the founding figure of a following ("Jacobite" schism, Feltoe). Euthymius is known through Cyril's Life and founded a laura. Timothy has his own petition and letters and an Armenian-held refutation. Elishe is a recorder. The drafts carry no list lines; those belong to the map build and were not checked here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Vardan Mamikonian (major) | 402 | 2:29 | 6.8 | 71.3 |
| Dioscorus of Alexandria (major) | 405 | 2:30 | 6.9 | 69.8 |
| Euthymius the Great | 323 | 2:00 | 6.9 | 69.5 |
| Timothy Aelurus (major) | 404 | 2:30 | 8.1 | 61.9 |
| Elishe | 324 | 2:00 | 8.1 | 63.2 |

**Batch finding**
- **G1 MINOR (README; records).** The README's table says `records.json` holds "For each id" the claims, contested claims and absent details, and lists ten ids. `records.json` has nine keys; `vakhtang-i-gorgasali` has no entry. That profile is in part B, so the gap is reported here only against the README's claim. Fix: add the `vakhtang-i-gorgasali` entry to `records.json` (part B's reviewer may give its content), or, until it exists, the README must not say every id has one.

---

## 1. Vardan Mamikonian

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B1); records minor (M4) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | card minor (M3) |
| 5 | No role for a witness | PASS (Lazar, Ghesarian, Elishe, Neumann, Ormanian named; "a note in Lazar's French edition" is unsigned) |
| 6 | Partisan witness named and marked | FAIL in the brief, minor (M1); card PASS (`uncertain` 1) |
| 7 | Contested both sides | PASS (the day of Avarayr) |
| 8 | Common names placed | FAIL, minor (M2) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:29) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- The court scene (l.1, 3), Lazar of Pharp tr. Ghesarian (`langlois_collection-historiens-armenie-tome2-fra_1869.txt`): "Si tu acceptes seulement pour un temps, et en apparence, ce que le roi a dit" (l.38990–38992); "Loin de moi cette pensée de mentir jamais à mon Créateur, soit en apparence, soit réellement" (l.38871–38873); the oath on the Gospel and "en versant notre sang pour la délivrance de notre pays" (l.38990–38997); "fondit en larmes, et consentit à succomber pour un temps, en apparence, pour sauver les trois nations" (l.39024–39026); in the "adrouschan (temple du feu)… quelques-uns d'entre eux, mais non tous, eurent l'air d'incliner la tête" (l.39030–39032). Faithful. The princes are "arméniens, ibériens et des Aghouank" (l.38858–38860), so "Albania" is right.
- Ghesarian's introduction: "Il vécut à la fin du cinquième siècle ou au commencement du sixième" (l.35079–35081). Ghesarian is named as translator on the title page (l.35063–35067). Faithful.
- Sahak (l.5): "instruit par le saint patriarche Sahag, son meul [aïeul]" (l.38943–38945, OCR "son meul"); Neumann's preface, "Vartan, of the house of the Mamigonians, a grandson of Sahag the Great" (`eghishe_…neumann1830.txt` l.574–575). Faithful.
- Elishe (l.7), tr. Neumann: the Mogbed and the Magi "wished to have the doors of the church broken open", and the people "hurled them at the heads of the Magi" (l.2648–2660); Vasag, "prince of Siunik", "had not disengaged himself from the alliance with the heathens" and "the apostate Vasag having abandoned the faith" (l.3137–3139, 3286–3287). Faithful.
- "Should the object of our lives be completed by a holy death in battle, let us meet it with a joyful heart." (l.9): Neumann l.3910–3912, split by a blank line and Neumann's running quote mark. Vartan is speaking (l.3881 "The Sparabed began to speak"; l.3904–3906, "elected me your leader"). Exact.
- "found worthy of martyrdom on the spot" (l.11): Neumann l.4166–4167. The right wing "together with the elephants" (l.4150–4151). Exact.
- One thousand and thirty-six: Neumann "In the whole, there fell one thousand and thirty-six" (l.4227); Lazar "qui tous ensemble font mille trente-six hommes" (l.40465–40466, rough OCR). Yazdegerd, "en apprenant… la mort du brave Vartan, éprouva un très-vif chagrin" (l.40480–40483). Faithful.
- The promise and the title of martyr (l.15; card `remembered` 1): "une action dont la renommée retentira éternellement" (l.39121–39122); "Mais Dieu leur déroba la promesse… puisque Dieu lui accorda le titre de martyr, qui devait durer éternellement parmi toutes les nations" (l.39133–39137). Exact.
- Ormanian (l.13; card): "on the 26th of May, 451, at the battle of Avarair"; "commemorated in the Armenian calendar on Shrove-Thursday" (`ormanian_church-of-armenia_gregory1912.txt` l.2256–2265); "Vardan and his thousand and thirty-five companions" (l.8564–8565); "FORMERLY ARMENIAN PATRIARCH OF CONSTANTINOPLE" on the title page (l.90). Exact.
- The 2 June date: Neumann's margin "June 2." (l.4147) and the note in Lazar's French edition, "le samedi 20 du mois de maréri (2 Juin) 451" (l.40449–40451). Card `otherNames` "Vartan le Grand": the note at l.37081–37082. Card `traces` 1: the dedication "TO THE PRIEST DAVID, OF THE HOUSE OF THE MAMIGONIANS" (Neumann l.1031). All exact.

**Findings**
- **B1 BLOCKING (items 1, 5; recurring fault 2, a modern date told as resting on an ancient text).** Brief l.9: "In 451, Lazar says, the armies met near the village of Avarayr, on the plain of the Deghmut." Lazar gives no year. His text has the place, "près du village appelé Avaraïr, au centre de la plaine de Deghmoud", and the feast, "Le vendredi de la fête solennelle de la Pentecôte" (l.40207–40214). The year 451 in that part of the file is only the editor's note, "Elle fut livrée le samedi 20 du mois de maréri (2 Juin) 451" (l.40450–40451). Elishe gives no year either; 451 in Neumann's file is his margin ("a.d. 451", l.3572–4567) and his preface ("in June 451 of our era", l.758). The card `dates` repeats the fault: "Fell at Avarayr in 451, by Elishe and Lazar of Pharp." So does the records claim "In 451 the armies met…", witness "Lazar of Pharp (langlois t2 l.40208-40209)". Fix, brief l.9: "Lazar says the armies met near the village of Avarayr, on the plain of the Deghmut." Brief l.13: "…gives 26 May 451. Neumann's margin, and a note in Lazar's French edition, give 2 June 451." Card `dates`: "Fell at Avarayr, by Elishe and Lazar of Pharp, who give no year. Malachia Ormanian gives the day as 26 May 451; Charles Neumann's margin and a note in Lazar's French edition give 2 June 451. No source used here gives his birth". Records: the claim becomes "The armies met near the village of Avarayr on the plain of the Deghmut", and the year moves to the contested claim on the day, which already names Ormanian, Neumann and the note.
- **M1 MINOR (item 6; the partisan witness not marked in the brief).** Both ancient witnesses write for the Armenian side and tell the fallen as martyrs, as the card's `uncertain` 1 says. The brief places them as "the two historians" (l.9) and never says so. Fix, brief l.9: replace "His words come to us only as the two historians wrote them." with "Both historians write for the Armenian side, and his words come to us only as they wrote them."
- **M2 MINOR (item 8).** Brief l.11: "Lazar says King Yazdegerd grieved…". Three Persian kings bore the name, and this is its only mention in the brief. Neumann's preface names him "Yasgerd II." (l.753), and Lazar "Iezdedjerd, roi de Perse" (l.40476, OCR "lezdedjerd, roi dePent"). Fix: "Lazar says the Persian king Yazdegerd grieved…". (Neumann's "the Second" may be added too; it is his number, not Lazar's.)
- **M3 MINOR (items 4, 12; status-announcement register on a participant card).** Card `uncertain` 4: "rests on Lazar of Pharp, in a rough French scan, and on Charles Neumann's preface to Elishe." "In a rough French scan" is build-process narration on a participant-facing card (Style Guide 1.11; batch 6 Marcellus M4). Fix: "That Sahak the Great was his grandfather and teacher rests on Lazar of Pharp and on Charles Neumann's preface to Elishe." The OCR note ("son meul") stays in the record.
- **M4 MINOR (records; item 1).** The records claim reads "Lazar places himself at the end of the fifth century or the start of the sixth". Lazar does not; the date is Ghesarian's, as the brief and the witness column say (l.35079–35081; the witness column's l.35066–35069 should read so too). Fix: "Ghesarian places Lazar at the end of the fifth century or the start of the sixth".
- Length with B1, M1 and M2: 412 words. Suggested cut, which also gives Elishe context at his first mention in this brief: delete l.5's "Charles Neumann, who put Elishe's history of the war into English, also calls him Sahak's grandson." (the card's `uncertain` 4 holds it), and change l.7's opening to "Back in Armenia, says Elishe, another Armenian historian of the war,". Scored: 400 words (2:28), FK 6.9, Flesch 71.0.

---

## 2. Dioscorus of Alexandria

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M6) |
| 5 | No role for a witness | PASS (the acts, Feltoe, Perry, Leo, Evagrius, Zachariah, Nau, the History of the Patriarchs named) |
| 6 | Partisan witness named and marked | FAIL, minor (M5) |
| 7 | Contested both sides | brief PASS (the trial, Theopistus); card minor (M7) |
| 8 | Common names placed | PASS (Cyril of Alexandria, Leo of Rome, Flavian bishop of Constantinople, Eusebius of Dorylaeum, Evagrius of Epiphania, Zachariah of Mitylene, Anatolius of Constantinople) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact; speaker confirmed)
- "I receive 'the of two;' 'the two' I do not receive." and "I am forced to be impudent, but the matter is one which touches my soul." (l.1): the acts of Chalcedon, Session I, Dioscorus speaking "at this point of the reading" of the acts of Constantinople against Eutyches (`npnf214` l.19251–19260). Percival's bracket supplies the context (l.19248–19250), and the brief's "the minutes of Eutyches's trial were read" is fair to it.
- "you and we ought to be at one in thought and act" (l.3): Leo, Letter 9 to Dioscorus (`npnf212` l.1934–1935). The year is Feltoe's: "in 445 dictating church regulations to S. Cyril's new successor at Alexandria, Dioscorus" (l.490–494), and the brief gives it to him.
- "alien from all the Honor of the Priesthood and of the Episcopate" and "I repudiate you. I protest." (l.5): Perry's acts of 449, Dioscorus giving sentence and Flavian answering (`council-of-ephesus-449_…perry1881.txt` l.24089–24137, across the running head at l.24124). Exact.
- "not of judges but of robbers" (l.5; card): Leo, Letter 95 to Pulcheria (`npnf212` l.8586–8640). Exact.
- "Sooner would Dioscorus see his own hand cut off, and the blood falling on the paper, than do such a thing as that." (l.9): Zachariah III.1 (`zachariah-rhetor_chronicle_hamiltonbrooks1899.txt` l.2344–2346). Exact.
- "He preserved the orthodox faith, which persists in the see of the evangelist Saint Mark to this day and for ever" (l.13; card): Evetts (`severus-al-muqaffa_…evetts1904.txt` l.35108–35109). Exact.
- Card: Feltoe's "still surviving 'Jacobite' schism originated with the deposition of Dioscorus" (`npnf212` l.772–774); Letter 98's "purposed excommunication" (l.8784–8785); Zachariah's "wrote his name in the book of life" (l.2543–2544) and "in a silver coffin" (l.5610–5613). All exact.

**Narrative checks**
- Feltoe: "By the Emperor's order Dioscorus, patriarch of Alexandria, was president" (`npnf212` l.641–643); the third session of 13 October, Gangra, "there three years later (in 454) died" (l.762–766). Evagrius II.4: "Dioscorus was convicted of having suppressed the epistle of Leo… and procured the subscriptions of the assembled prelates to a blank paper" (`evagrius-scholasticus_…walford1846.txt` l.3089–3098); II.5: "sentenced to reside at Gangra in Paphlagonia" (l.3366–3368). Walford's account fixes Evagrius's birth "about A.D. 536" (l.327–328), so "some eighty years later" is fair. The council's letter: "on the thirteenth day of the month of October you were deposed… for even when called to answer your accusers three times… you did not come" (`npnf214` l.20084–20092). All faithful.
- Zachariah III.1: "because he said, 'It is right for us to believe that Christ became incarnate from two matures [natures]; and we should not confess two natures after the union'"; Anatolius, "Not for the faith is Dioscorus deposed" (l.2315–2322). III.2: "the priests, and the monks, and many of the people… severed themselves from his communion" (l.2537–2544). "Dioscorus the Confessor" (card `otherNames`): l.4988. "Eight years and three months" (l.1352–1353). Faithful.
- Nau: "Nous sommes loin de nous porter garants de l'authenticité de bien des détails" (`theopistus_…nau1903.txt` l.415–417); "Théopiste ne fabrique pas de toutes pièces les discours" (l.428–429); after 512 (l.483–485); Assemani, "Fabulosa narratio a jacobitis recentioribus excogitata" (l.493–500); "succéda à S. Cyrille en 446… mourut le 4 septembre 454" (l.176–180). The throne of wood: "Quand bien même vous m'enlèveriez ce trône de bois, vous ne pourrez pas m'enlever le trône que le Messie m'a préparé dans le ciel" (l.15191–15194). Evetts: "no biography of the holy patriarch Dioscorus after his banishment has been found" (l.35106–35107); heading "A. D. 444-458" (l.34864). All faithful.
- records.json matches brief and card, and carries both `contested_claim` records.

**Findings**
- **M5 MINOR (item 6; a partisan record not marked).** Brief l.7 tells the charges, and the conviction, from Evagrius and the council's letter with no mark on either. The next paragraph marks Zachariah as "from the side that rejected Chalcedon". The charges are the council's own: Evagrius says he gives "a cursory statement of the more important points" of the acts, which he subjoined in full (Walford l.3077–3093). As written, the accusers' record stands as the narrator's fact while the defence is marked as partisan. Fix, l.7: "Evagrius of Epiphania, a historian born some eighty years later, gives the charges from the council's own acts. By that record, Chalcedon convicted Dioscorus of hiding Leo's letter…". (The records claim already says "a charge by his opponents".)
- **M6 MINOR (item 4).** Brief l.11: "Its editor, François Nau, does not vouch for many details. In it he tells the empress Pulcheria…". The nearest "he" is Nau, so a listener hears Nau speaking to Pulcheria. The sentence is also 26 words. Fix: "In it Dioscorus tells the empress Pulcheria she may take his throne of wood, but not the one the Messiah has prepared for him in heaven."
- **M7 MINOR (item 7, card).** Card `knownFor`: "was himself deposed at Chalcedon in 451 for refusing to answer its summons". The brief and the card's `uncertain` 1 tell the reason two ways, and the council's own letter gives more than the summons ("your disregard of the divine canons… your disobedience… the other crimes", `npnf214` l.20085–20089). Fix: "…and was himself deposed at Chalcedon in 451, by the council's letter for disobedience and for refusing its summons three times; the churches that rejected Chalcedon kept his name."
- Length with M5 and M6: 413 words. Suggested cut: delete l.11's "Nau and Feltoe date his death in exile to 454." (the card's `dates` holds it). Scored: 403 words (2:29), FK 7.1, Flesch 68.8.

---

## 3. Euthymius the Great

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS |
| 2 | Quotes verbatim | PASS (no quote marks; Latin tellings checked) |
| 3 | No invention | PASS |
| 4 | Reading aids | card minor (M9) |
| 5 | No role for a witness | PASS (Cyril, Cyriacus, Duchesne, Cotelier named) |
| 6 | Partisan witness named and marked | PASS (hagiography marked at l.3; Cyril's "deceiver" placed as his at l.9; card `uncertain` 5) |
| 7 | Contested both sides | FAIL, blocking (B2) |
| 8 | Common names placed | FAIL, minor (M8) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | FAIL, blocking (B2: a dispute not told in place); 2:00 |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Close tellings** (`cyril-scythopolis_vita-euthymii-cotelier-monumenta-v2-grc-lat_1681.txt`, Latin column; rough OCR)
- The dream (l.1): Cyril "nondum potuit orationi ne principium quidem imponere"; "magnus Euthymius divinusque Sabas mihi apparent"; "manuque in sinum immissa, argenteum quemdam… alabastrum illinc sumit; in quo cum specillum intinxisset, ter meum in os immisit. Illius autem species quidem erat similis oleo… eumque omnino cum melle conferre, ingens esset rei contumelia"; "mihi expergefacto… ejus adhuc in ore remanserunt reliquiae… praesens opus inchoavi" (l.45575–45693). Faithful. Cyril says the spoon went in "ter", three times; the brief's "put it in Cyril's mouth" leaves that out and adds nothing.
- Cyriacus: "Haec mihi Anachoreta Cyriacus narravit" (l.31776–31777). The prologue: "aptissima ad laetificandos… eos qui eam legerint, & ad rerum similium studium excitandos" (l.26601–26605). Faithful.
- Birth (l.5): "Erat autem Melitene, quae est urbs Armeniae ad Euphratem; quidam nomine Paulus… conjux, vocata Dionysia"; the vision; "natus esset puer, quarto Gratiani consulatu" (l.26817–26904). Otreius "puerum vero adoptavit, nec solum ei fuit nutritor & paedagogus" after making Dionysia a deaconess (l.27066–27153); "Presbyter ordinatur… ejusque fidei committitur cura Monasteriorum" (l.27504–27508). Faithful.
- l.7: "Post annos autem quinque in Pharan transactos, illinc recedit cum Theoctisto… ad torrentem quemdam praecipitem… magnam speluncam offendunt" (l.27729–27738); "venit Hierosolymam circa annum vitae suae vigesimum nonum" (l.40199–40201). Aspebetus and the boy Terebon, "partem corporis ex dimidio" stricken (l.28522–28560). "Aspebetum baptizat, Petrum transnominans" (l.29081–29083); "mittit divinus Euthymius ad Juvenalem Hierosolymorum Patriarcham, postulans ut eis ordinaretur Episcopus" (l.30637–30645); "Sic itaque Petrus Episcopus Castrorum in Palaestina primus ordinatur" (l.30777–30779). Faithful to Cyril.
- l.9: "septuagesimo & quinto anno aetatis magni Euthymii, congregata fuit Synodus Chalcedonensis" (l.35956–35960); "invenisset recte se habere" (l.36060–36062); "Theodosius quidam, habitu quidem Monachus, moribus vero praestigiator exitiosissimus… cepisset Eudociam Augustam" (l.36071–36087); "solus communionem ejus… aversabatur magnus Euthymius cum suis" (l.36138–36143); "admittere etiam decretum quod edidit Chalcedonensis… Juvenali… communicare" and "Juvenali & Catholicae communicat Ecclesiae; simulque ingentem Monachorum Laicorumque multitudinem… inducit" (l.37480–37640). Eudocia as "la veuve de Théodose II" is Duchesne's (`duchesne_…tome3-fra_2e-ed1910.txt` l.17335–17336), and he is listed. Faithful.
- l.11: "nonagesimo quidem & nono anno suae aetatis, decimo autem sexto Imperii Leonis, excedit e vita" (l.40203–40206). Faithful. Card `traces` 3, Sabas "octogesimo & secundo anno aetatis Euthymii", given to Domitian and then sent to Theoctistus (l.37700–37722). Card `remembered` 2, Duchesne: "Marcien et Pulchérie écrivirent aux moines; le pape Léon en fit autant; Euthyme s'employa de son mieux" (l.17480–17483) and "Les efforts de saint Euthyme pour discipliner les solitudes n'avaient abouti que dans un cercle assez restreint" (l.17324–17326). Faithful.
- Absence check: card `dates` "The sources used here give no year in our reckoning." Neither Cotelier's Life (no year in the margins of l.26790–45800) nor Duchesne gives one. Holds as scoped.

**Findings**
- **B2 BLOCKING (items 7, 10; a contested claim told as settled).** Brief l.7: "Euthymius baptized the father as Peter and asked Juvenal of Jerusalem for a bishop for the converts." The profile's own record files this claim as Contested, with a `contested_claim` record, and the card's `uncertain` 3 gives the other side: Duchesne, "Le patriarche de Jérusalem, Juvénal, le baptisa sous le nom de Pierre et le sacra évêque des Sarrasins" (l.21192–21194). The brief tells only Cyril's side, in the narrator's voice, and the card's `knownFor` ("baptized a Saracen chief and his people") does the same. The pattern requires a contested point to be told where it arises with its witnesses named (batch 2, Suetonius: a contested point told as settled was blocking). Fix, l.7: "Cyril says Euthymius baptized the father as Peter, but Louis Duchesne, in his history of the early church, says Juvenal of Jerusalem baptized him. Euthymius asked Juvenal for a bishop for the converts, and Peter became the first bishop of the Camps in Palestine." Card `knownFor`: "A monk from Melitene who settled in the desert near Jerusalem, baptized a Saracen chief and his people by Cyril of Scythopolis's account, and held to the Council of Chalcedon when most Palestinian monks turned against it."
- **M8 MINOR (item 8; "no statements that have no context").** Brief l.1: "Euthymius and Sabas appeared to him." This is Sabas's first mention in the brief, and a listener is not told who he is. Cyril gives the link in the same passage: he was hurrying on to write "in alio opere gesta praestantissimi Sabae" (l.45701–45702). Fix: "Then he fell asleep, and Euthymius and Sabas, a monk whose Life Cyril also wrote, appeared to him."
- **M9 MINOR (items 4, 12; status-announcement register on a participant card).** Card `uncertain` 2: "The Library holds the Life only in Jean-Baptiste Cotelier's Latin translation of 1681, in a rough scan; the Greek in that scan cannot be read. Every detail here was read in the Latin column." `uncertain` 4: "The held Latin scan gives… The scan is rough." This is build-process narration ("The Library holds", "the held… scan") on a participant-facing card (Style Guide 1.11; batch 6 Marcellus M4). Fix, `uncertain` 2: "Cyril wrote in Greek. Every detail on this card follows Jean-Baptiste Cotelier's Latin translation of 1681." `uncertain` 4: "Cotelier's Latin gives his death in his ninety-ninth year, though Cyril also says he came to Jerusalem in about his twenty-ninth year and spent sixty years in the desert." The scan's quality stays in the record.
- Length with B2 and M8: 346 words. Suggested cuts: delete l.3's "Cyril names the anchorite Cyriacus as the source of some of its stories." (the card's `uncertain` 1 holds it; l.3 keeps the hagiography mark) and l.5's "Later, as a priest, he was put in charge of the monasteries." Scored: 322 words (1:59), FK 7.5, Flesch 67.7.

---

## 4. Timothy Aelurus

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M10, M11); records minor (M14) |
| 2 | Quotes verbatim | PASS on wording; speaker minor (M10) |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Zachariah, Evagrius, Walford, the petition, the Life of Peter, the History of the Patriarchs, Feltoe, Evetts named) |
| 6 | Partisan witness named and marked | PASS (Zachariah marked l.3; the petition is his opponents', card `uncertain` 1) |
| 7 | Contested both sides | PASS (who killed Proterius; the length of exile) |
| 8 | Common names placed | FAIL, minor (M12, M13) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes and close tellings**
- The consecration (l.1, 3), Zachariah IV.1: "suddenly the report of the death of Marcian reached them"; "Timothy, a man expert in business and of ascetic life; who had been brought from the wilderness, by force, to Cyril, and ordained as presbyter by him. Moreover, he was of the same faith as Dioscorus"; "brought to the great Church which is called Cesarian"; "they sought for three bishops, according to the canonical statute… since two Egyptian bishops were present"; Peter the Iberian "carried… on their shoulders, not letting him touch the ground" (l.3276–3302); "on account of his emaciation, the Proterian party used jestingly to style him the 'Weasel'" (l.3314–3315). Exact where quoted.
- "the Cat": Walford's chapter heading "ELECTION OF TIMOTHY, SURNAMED ÆLURUS (THE CAT)" (l.3582–3584) and Feltoe "Timothy Ælurus (or the Cat)" (`npnf212` l.888). The heading is the translator's, and the brief gives it to "E. Walford's English". Faithful.
- "I do not agree with the transactions of Chalcedon, because I find in them divisions and cleavage of the dispensation." (l.7): Zachariah IV.6, Timothy's petition to the emperor Leo (l.3670–3672; heading l.3570–3572). "neither does the definition of the faith which the fathers proclaimed require addition" (l.13): l.3608–3609, of "the three hundred and eighteen blessed fathers" (l.3603–3604), so "the faith of Nicaea" is fair. Exact.
- l.9: "they snatched the chief priest from the very font, and dragged him away" (l.3858–3861); Gangra to Cherson (l.4002–4006); "wrote not alone against the Nestorians, but also against the Eutychianists" (l.4092–4093). The Armenian refutation: the edition's title in the file (`timothy-aelurus_widerlegung-…1908.txt` l.1). Faithful.
- l.11: Evagrius III.4, "Basiliscus summons Timotheus Ælurus from his exile, in the eighteenth year of his banishment" (Walford l.5394–5396); III.11, Zeno "on being informed… that he was already aged… abandoned his purpose. And, in fact, Timotheus shortly after paid the debt of nature" (l.5832–5838). Evetts: "for seven full years" (l.35199–35201). Zachariah: "the bones of Dioscorus… in a silver coffin" (l.5610–5612). Faithful, apart from M11.
- Card: "Timothy the Great" (Zachariah l.3151, 3275); "the friend of the poor" (l.4016); the censures "In the first place, by Dioscorus; and after him, by this Timothy; and after him by Peter" (l.3702–3704); Peter "canonically consecrated as his successor by the bishops of the country" (l.5695–5697); Evetts "twenty-two years" (l.35206) and heading "A. D. 458-480" (l.35194); Feltoe "In 457 Marcian died" and "effected in 460" (`npnf212` l.881, 897). Exact.

**Findings**
- **M10 MINOR (items 1, 2, 5; recurring fault 1, a narrator's words given to the document he cites).** Brief l.5: "A petition… which Evagrius quotes, blames Timothy. By that report, some Alexandrians killed Proterius in the baptistery "at the instigation of Timotheus."" The quoted words are Evagrius's own narration: "some of the Alexandrians, at the instigation of Timotheus, according to the written report made to Leo, despatch Proterius" (Walford l.3641–3644). The petition he then quotes begins at l.3657 and blames Timothy in other words: "Of all these transactions Timotheus was the guilty cause, and the skilful builder of the scheme of mischief" (l.3752–3754). The card's `remembered` 2 makes the swap explicit: "The petition…, quoted by Evagrius: Proterius was killed "at the instigation of Timotheus"." The records claim has the same reading. Fix, brief l.5: "Evagrius, from that report, says some Alexandrians killed Proterius in the baptistery "at the instigation of Timotheus."" Card `remembered` 2: "The petition of the Egyptian bishops and clergy of Alexandria to the emperor Leo, quoted by Evagrius of Epiphania: "Of all these transactions Timotheus was the guilty cause, and the skilful builder of the scheme of mischief"." Records: the witness reads "Evagrius II.8, following the petition (Walford l.3641-3644); the petition's own words at l.3752-3754".
- **M11 MINOR (item 1).** Brief l.11: "Evagrius and Zachariah both say he was recalled in the eighteenth year of his exile". Zachariah says "When Timothy had completed eighteen years in banishment" (l.5219–5220), which is not the same count as Evagrius's "in the eighteenth year". The card's `dates`, its `uncertain` 3 and the contested claim repeat "both". Fix, brief: "The emperor Basiliscus called him back. Evagrius says it was in the eighteenth year of his exile, and Zachariah after eighteen years." Card `dates`: "recalled in the eighteenth year of his exile by Evagrius of Epiphania, after eighteen years by Zachariah of Mitylene,". Card `uncertain` 3: "Evagrius says he was recalled in its eighteenth year, and Zachariah after eighteen years; the History of the Patriarchs…". Records: the same in the claim and the contested claim.
- **M12 MINOR (item 8).** (a) The brief never gives the subject's name with its identifier. It calls him "a priest named Timothy" (l.1) and gives the nicknames, but "Aelurus" is never said, though the held file has a second Timothy in the same see (Timothy Solophaciolus, Feltoe `npnf212` l.895–897; Timothy Salophaciolus, Zachariah l.3938). Evagrius gives "Timotheus, surnamed Ælurus" (Walford l.3620–3621). (b) l.3: "of the same faith as Dioscorus," is Dioscorus's first mention, with a role and no place. Fixes, l.3: ""of the same faith as Dioscorus," the bishop of Alexandria whom Chalcedon had deposed." and "Evagrius of Epiphania calls him Aelurus, which E. Walford's English gives as "the Cat."" (replacing "E. Walford's English of Evagrius of Epiphania gives "the Cat."").
- **M13 MINOR (item 8, card).** Card `legacy.traces` 1, "after Dioscorus and before Peter", is the card's first Dioscorus and gives a bare "Peter"; `traces` 2, "Peter, consecrated by the bishops of the country", is bare too, beside Peter the Iberian in the brief. Zachariah does not say which Peter the censures list means (l.3704). Evagrius names the successor "Peter, surnamed Moneus" (Walford l.5844, OCR), and elsewhere "Peter, surnamed Mongus" (l.6793). Fixes: `traces` 1 "…names him second, after Dioscorus of Alexandria, among those who wrote censures…" (drop "and before Peter"); `traces` 2 "Zachariah says Peter, whom Evagrius calls Peter Mongus, was consecrated by the bishops of the country and succeeded him at Alexandria."
- **M14 MINOR (records; recurring fault 4).** `absent_details` 1: "Birth, family and the year of his death. No ancient source used here gives them." The History of the Patriarchs, used on this card, names his brother: "He and his brother Anatolius were banished to the island of Gangra" (Evetts l.35199–35200), and the card's `uncertain` 3 says so. Fix: detail "Birth and the year of his death"; note "No ancient source used here gives them; the History of the Patriarchs names his brother Anatolius (Evetts l.35199-35200). Feltoe gives 457 and 460, and Evetts's heading gives his see as 458 to 480."
- Length with M10 to M12: about 416 words. Suggested cut: delete l.9's "A long work of his against Chalcedon and the letter of Leo of Rome comes down to us in Armenian." (the card's keyWorks 3 and `uncertain` 6 hold it). Scored: 397 words (2:27), FK 8.1, Flesch 61.1. (Other wordings of M11 and M12 that I tried pushed Flesch to 59.5 to 60.0; the wording above passes.)

---

## 5. Elishe

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | PASS; records minor (M15) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | card minor (M16) |
| 5 | No role for a witness | PASS (Neumann, Langlois, Thomas Ardsruni named) |
| 6 | Partisan witness named and marked | PASS (Thomas Ardsruni's Barsouma story placed as his, card `uncertain` 5) |
| 7 | Contested both sides | PASS (the last years; the bishop of the Amadunians; the supplement on the card) |
| 8 | Common names placed | PASS (Sahak the Great, Mesrop Mashtots, David of the Mamikonian house, Thomas Ardsruni) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (recorder) |

**Quotes** (`eghishe_history-of-vartan-and-the-armenian-war_neumann1830.txt`; all exact)
- "Truly, not of our own free will, do we describe, in lamenting tones, all the miseries of which we ourselves have been eye-witnesses." (l.1): chapter I (l.1117–1118).
- "From this belief no one can move us, neither angels nor men—neither fire nor sword, nor water" (l.7): the bishops' answer (l.2136–2137); it runs on "nor any other horrid tortures", and the cut is clean. The edict, "Mihrnerseh, Grand Vizier of Iran and Daniran" (l.1609–1611).
- "Concord is the mother of good; and Dissension, the nurse of evil" (l.13): the dedication (l.1070–1071).
- Card: Thomas Ardsruni, as a note in Langlois quotes him, "l'Histoire des saints Vartaniens rédigée par le bienheureux prêtre Elisée" (`langlois_…tome2-fra_1869.txt` l.27237–27242; the note is headed "Thomas Ardzrouni", l.27222). Exact.

**Narrative checks**
- The dedication "TO THE PRIEST DAVID, OF THE HOUSE OF THE MAMIGONIANS", "in the following seven chapters", "the valiant exploits of the brave, and the misery which followed" (l.1031–1047). Faithful.
- Neumann's preface: "a disciple of Sahag and Mesrob. He was also secretary to the Armenian General Vartan"; bishop of Arakadsoden, called "Amadunians", "among the members of the Synod of Artashad, in 450"; Thomas Ardsruni, "an… Armenian historian of the ninth century", has him withdraw "to the canton Ershedunik… on the shore of the Wan-sea, where he died at a very advanced age" (l.574–600). The list: "Ekhishe (Elisaeus), Bishop of the Amadunians" (l.1749), the bishops "assembled together at the royal seat in the city of Ardashad" (l.1766–1767); Langlois's translation "Elisée, évêque des Amadouni… réunis ensemble à Ardaschad" (l.27345–27351). Faithful.
- Langlois's introduction: "On ignore le lieu et la date de sa naissance; toutefois les biographes rapportent que, dans sa jeunesse, il fit partie des milices"; "Selon d'autres écrivains, Elisée aurait été le secrétaire de Vartan"; "quelques-uns même prétendent qu'il exerça les fonctions épiscopales dans la satrapie des Amadouni" (l.25717–25733); the caves of Mog and by the lake in the Reschdouni country, "dont la vie avait été abrégée par des fatigues de tout genre" (l.25740–25797); "fixée, par quelques écrivains, à l'an 480" (l.25816–25817); "il a su résister, plus qu'aucun autre de ses compagnons d'étude, à l'introduction de l'hellénisme"; "un des morceaux les plus brillants de leur littérature classique" (l.26086–26092); "Malheureusement, son exemple ne fut point imité" (l.26106–26107); the Barsouma story from Thomas (l.25945–25989); the supplement (l.25910–25925). Faithful. Langlois's own sentence names the list "des évêques assemblés à Aschdischad" (l.25731–25732), but his note (4) cites Elishe's own History for it (l.25760), so the brief's "Langlois says only that some writers think so" stands.
- Neumann on the supplement: "The editors have, then, joined two works entirely different" (l.738–746). Faithful.

**Findings**
- **M15 MINOR (records; item 1).** The claim "Disciple of Sahak and Mesrop, secretary to Vartan, grandson of Sahak; later bishop of the Amadunians…" gives "grandson of Sahak" to Elishe. In Neumann the grandson is Vartan: "secretary to the Armenian General Vartan, of the house of the Mamigonians, a grandson of Sahag the Great" (l.574–575). The record's own `absent_details` 2 says so, so the claim contradicts it. Fix: delete "grandson of Sahak;" from the claim.
- **M16 MINOR (items 4, 12; status-announcement register on a participant card).** Card keyWorks 2, `about`: "…; not in the held translations." "Held" is the Library's word, not a reader's (Style Guide 1.11). Fix: "…; not in Neumann's or Langlois's translation."

---

## Totals

2 blocking (B1 `vardan-mamikonian`; B2 `euthymius-the-great`) and 17 minor (G1 README; M1–M4 `vardan-mamikonian`; M5–M7 `dioscorus-of-alexandria`; M8–M9 `euthymius-the-great`; M10–M14 `timothy-aelurus`; M15–M16 `elishe`). Every fix above was checked against the line it cites, and every brief fix was scored on a scratch copy: all three majors stay under the 2:30 cap (397 to 403 words) and both non-majors at or under about 324 words, with FK at most 10 and Flesch at least 60.

## R1 review: era 3 batch 1, part B (Church Family Tree Who profiles)

Reviewer: independent, first sight of these drafts (branch `who-profiles-era3-batch1`, commit d68a0ae3). Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's rulings in the Decision-Log (2026-11-12: majors capped at 2:30, about 405 words, a cap and not a target; non-majors 1 to 2 minutes, at most about 324 words; 162 words a minute) and the era 3 scan ruling of 2026-11-11 (rulers "Story unless own voice"; Moses of Khoren a WHO as a recorder, his date Contested). I hunted hardest for the recurring faults of earlier batches: witness swaps, a modern date told as resting on an ancient text, an identification told as settled against a held doubt, absence claims a held file contradicts, unplaced common names and namesakes, unmarked hostile witnesses, invented detail, and AI tells. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Profiles: `victor-of-vita` (not major), `moses-of-khoren` (not major), `barsauma-of-nisibis` (major), `narsai` (major), and their entries in `records.json`. `vakhtang-i-gorgasali` was in the original scope; the coordinator rescored it STORY and removed it from the batch during this review, so it is not reviewed. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch1/`. Brief line numbers refer to the `.brief.txt` files, where each paragraph is one line and blank lines count (paragraphs sit on l.1, 3, 5, 7, 9, 11, 13, 15). Other line numbers point to files under `cic/texts/`.

Method. I searched every quotation in the four briefs and cards in the vendored file the card or records cite. The match stripped tags, collapsed whitespace and normalised quote marks; for the OCR files (Petschenig, Halm, Langlois, the Mekhitarist Italian, Chabot's Synodicon, Abbeloos and Lamy, Gismondi, Nau's PO 9, Scher's PO 4) I read each passage by line number and searched tolerantly. I read each hit in context to see who is speaking: the ancient author, a document he quotes, a translator's introduction, a footnote, or a bracket the translator supplied. I checked every factual sentence of each brief against its passage, and compared each `records.json` entry with its brief and card. Before accepting any absence or closed-list claim I searched `cic/texts/` for other held files on the person (this found Mesnage's Afrique chrétienne and the 484 Notitia in Halm for Victor; Labourt's Christianisme dans l'empire perse, Michael the Syrian's Chronicle in Chabot's French and 'Amr in Gismondi for Barsauma). Readability came from `engine.m1.gates.grade_text`, run from the repo root. Length assumes 162 words a minute.

## Applies to all four

- **Audio = brief.** Each audio script matches its brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, placed before the closing line. No tag appears in any brief or card.
- **Readability.** All four pass (FK at most 10, Flesch at least 60). Barsauma sits nearest the floor (Flesch 62.8). No narrator sentence runs past 25 words (the one hit, Victor l.9, is the Procopius quotation).
- **Length.** Victor and Moses are at the non-major ceiling (324 words, 2:00). Barsauma is at the major cap (405, 2:30) and Narsai just under (398, 2:27). Every fix below that adds words to Barsauma or Narsai names a cut that keeps it at or under the cap.
- **Card order.** All four follow Mark's order. Missing fields are left out. keyWorks never goes past three. Each `uncertain` list opens with the brief's main caveat. `"date": null` in source entries is the schema the earlier batches used.
- **Who test (item 14).** Victor, Moses and Narsai have held bodies of work (the History of the Persecution, the History of Armenia, four homilies in Connolly). Barsauma has his six letters in the Synodicon and founded, with Narsai, the school of Nisibis. Victor and Moses are recorders, as the README says. The drafts carry no list lines; those belong to the map build and were not checked here.
- **Victor's card tradition** ("Gothic, Vandal & Lombard Homoian Christianity", the church that persecuted his own) is logged in the README as the scan's, to be settled with the placing. Not counted here.

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Victor of Vita | 324 | 2:00 | 7.3 | 69.0 |
| Moses of Khoren | 324 | 2:00 | 7.0 | 69.0 |
| Barsauma of Nisibis (major) | 405 | 2:30 | 8.1 | 62.8 |
| Narsai (major) | 398 | 2:27 | 7.2 | 65.7 |

---

## 1. Victor of Vita

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B1); minor (M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Victor, Halm, Petschenig, Procopius named) |
| 6 | Partisan witness named and marked | PASS (l.5: "the polemic of a victim and an enemy of their church"; card `uncertain` 1) |
| 7 | Contested both sides | FAIL, blocking (B1: his see) |
| 8 | Common names placed | PASS (Felix, bishop of Abbir; Procopius of Caesarea; card: not Victor of Tunnuna) |
| 9 | One term | FAIL, minor (M2) |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; sources part of B1 |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact; speaker confirmed)
- "our city" (l.3, card): "et nostrae ciuitatis uenerabilis Panpinianus antistes" (`victor-of-vita_historia-persecutionis-africanae-provinciae-lat_petschenig1881.txt` l.1241-1242), Victor speaking. Halm's note: "nostrae ciuitatis] i. e. Vitensis" (`mgh-aa-3_victor-vitensis-corippus-halm1879.txt` l.604), after Ruinart.
- "even up to my time were going about in Byzantium having their speech uninjured." (l.9, card): Procopius, Wars III.8 (`procopius_wars-3-4-vandalic_dewing1916.txt` l.917-918), Procopius speaking of Honoric.

**Narrative checks**
- Felix of Abbir (l.1): "habens iam in episcopatu XLim annos ... nec sentiebat quicquam nec penitus loquebatur ... suggessimus ut a suis rex peteretur, ut saltem eum propere moriturum Carthagini esse iussisset ... fertur tyrannus ... 'iungantur boues indomiti, qui eum conligatis funibus trahendo perducant' ... ex trauerso super burdonem uinctum quasi quoddam ligni truncum toto itinere portabamus" (Petschenig l.2854-2863; Halm l.1772, "quadraginta quattuor"). Faithful; "the king, Victor reports" carries "fertur".
- "Sexagensimus nunc ... agitur annus ex eo, quo populus ille crudelis ac saeuus Uuandalicae gentis ... transuadans ... inter Hispaniam Africamque" (Petschenig l.1074-1077). "a persecutione heresis Arrianae" (l.6973). Faithful.
- The 4,966, Sicca and Lares, "Christiani sumus, catholici sumus", "nobis copia dabatur et introire et uerbum ammonitionis fratribus facere et diuina mysteria celebrare" (Halm l.1768-1770; Petschenig l.2865-2877). Faithful.
- Tipasa: "linguas eis et manus dextras radicitus abscidisset ... ita loquuti sunt et loquuntur ... pergat nunc Constantinopolim, et ibi reperiet unum de illis, subdiaconem Reparatum" (Petschenig l.5953-5961). Faithful.
- The edict "Data sub die vi. Kl. Mart. Carthagine", margin "a. 484" (Petschenig l.5428). The Book of Faith "a Uictore ipso operi suo insertum esse ueri simile est" (l.540-542). The prologue "obscurissimo" beside "additamentis spuriis" (l.512-517). The close, "uidete Africam totam, dudum tantarum ecclesiarum cuneis fultam ... modo sedentem uiduam et abiectam" (l.7015-7021). All faithful.

**Findings**
- **B1 BLOCKING (items 1, 7, 12; absence claim a held file contradicts).** Brief l.3: "The manuscripts of his book call him a bishop of Vita." Card `uncertain` 2: "That he was bishop of Vita rests on the titles in the manuscripts of his book." Card `uncertain` 5 and `dates`: "No source used here tells his own life beyond what his History says." Records `absent_details` 1 says the same. Three held lines contradict this. (a) The manuscripts are not unanimous: Halm's apparatus to the title gives "uitensi (uitensis LR, vticensis p)" (Halm l.370), and Mesnage notes "Certains manuscrits portent la variante Uticensis pour Vitensis" (`mesnage_afrique-chretienne-eveches-ruines-antiques-fra_1912.txt` l.4246-4247). (b) Halm prints with the History the Notitia of the Catholic bishops summoned to Carthage in 484 (Halm l.5156-5160, "qui Carthagine ex praecepto regali uenerunt pro reddenda ratione fidei"; dated to 484 in Halm's preface, l.89-91), and under Byzacena it lists "Uictor uitensis non occurrit" (l.5750). That is a second held witness to a Victor bishop of Vita. (c) Joseph Mesnage takes that Victor for the historian and adds a life beyond the History: "VICTOR Vitensis n'assista pas à la Conférence, mais s'enfuit en exil, où il écrivit son histoire en 488" (Mesnage l.4244-4245). The identification and the exile are Mesnage's, and should be told as his. Fixes, checked against those lines:
  - Brief l.3: "Most manuscripts of his book call him a bishop of Vita; one reads Utica." (+5 words). To hold 324, delete l.7's "He copies Huneric's edict into his book." (-7; the card's `keyWorks` and `legacy.traces` 1 hold it, and this also clears M2).
  - Card `uncertain` 2: "That he was bishop of Vita rests on most manuscripts of his book; one reads Utica. The list of Catholic bishops called to Carthage in 484, which Karl Halm prints with the History, names a Victor of Vita who did not come; Joseph Mesnage takes him for the historian. Victor calls Pampinianus the bishop of "our city"; Halm takes that to mean Vita."
  - Card `uncertain` 5: "Beyond his History, Joseph Mesnage says he did not come to Carthage in 484, fled into exile and wrote his History there in 488. No held source gives his birth or death. He is not Victor of Tunnuna, the later African chronicler." Card `dates`: replace "No source used here gives his birth or death" with "Joseph Mesnage dates the History to 488. No held source gives his birth or death".
  - Card `sources.about`: add "L'Afrique chrétienne: évêchés et ruines antiques", author Joseph Mesnage, French, `cic/texts/mesnage_afrique-chretienne-eveches-ruines-antiques-fra_1912.txt`. Records: add a claim for the Notitia line (Halm l.5750) and Mesnage's identification and date (Mesnage l.4244-4249), tagged Dominant Modern Reconstruction, and narrow `absent_details` 1 to "His birth, family and death".
- **M1 MINOR (items 1, 7; card and records).** Card `uncertain` 3: "That the Catholics of Tipasa still spoke after their tongues were cut out rests on Victor and on Procopius of Caesarea". Procopius names no place; he says Honoric "cut off the tongues of many" (Dewing l.916-917). He witnesses the wonder in general, not at Tipasa. Fix: "That Catholics still spoke after their tongues were cut out rests on Victor, who tells it of Tipasa and names the subdeacon Reparatus at Constantinople, and on Procopius of Caesarea, who names no town but says such people were still in Byzantium in his own day." Records `contested_claims` 1: the same correction.
- **M2 MINOR (item 9).** Brief l.7: "He copies Huneric's edict", singular; the card's `keyWorks` and `legacy.traces` 1 say "edicts". Victor copies two: the summons of 483, "Data sub die xiii Kal. Iunias anno septimo Hunirici" (Petschenig l.3131-3151), and the edict of 484 (l.5428). Fix: the deletion in B1 clears it; if the sentence stays, "He copies Huneric's edicts into his book."
- **M3 MINOR (records).** The Tipasa claim is tagged Contested, but its `contested_claim` says "No held source denies it; both witnesses report it". A Contested tag needs a named second side. Fix: tag the claim Documented as a report ("Victor and Procopius report…"), and drop the `contested_claim` or rename it as an honest limit (`absent_detail`: "No held witness tests the report").

---

## 2. Moses of Khoren

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1, M2) |
| 2 | Quotes verbatim | FAIL, minor (M3, an OCR fault quoted) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M1) |
| 5 | No role for a witness | PASS (Moses, Langlois, the Mekhitarist monks, Thomas Artsruni, Macler named) |
| 6 | Partisan witness named and marked | PASS (Langlois's "tradition" marked as tradition) |
| 7 | Contested both sides | FAIL, minor (M1) |
| 8 | Common names placed | PASS (Moses of Khoren; Sahak the Great and Sahak Bagratuni kept apart; Eznik of Kolb) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes**
- "Pio davvero Mosè: e di cuore umile" (card): the Mekhitarist preface (`moses-khoren_history-of-armenians-ita_mechitaristi1850.txt` l.239). Exact.
- "classé à la tète des historiens de sa nation" (card): Langlois's introduction (`langlois_collection-historiens-armenie-tome2-fra_1869.txt` l.7937-7938). Exact to the file; see M3.
- "sans doute" and "forse" (card): Langlois's note (3), "Moïse veut sans doute désigner ici saint Cyrille" (l.24853-24854); the preface, "un Platone novello, forse quel Cirillo Alessandrino" (ita l.136-137). Exact.

**Narrative checks**
- The lament (l.1, l.11): "nous, accourant de Byzance, en grande hâte, nous espérions très-certainement danser aux noces ... me voici sur une tombe, gémissant, me lamentant et pleurant. Pas même arriver à temps pour les voir (Sahag et Mesrob), leur fermer les yeux, entendre leurs paroles dernières" (Langlois l.25496-25503). The names are Langlois's bracket, but the chapter follows LXVII, "Mort de Sahag le Grand et du bienheureux Mesrob" (l.19907-19908), and the lament mourns "le pasteur ... et son compagnon" (l.25433-25436). The brief's naming is safe. "Qui désormais appréciera votre doctrine? Qui se réjouira de mes progrès" (l.25536-25537). Faithful.
- The patron: "Moïse de Khorène ... à Sahag Bagratide, salut!" (l.8723-8725); Langlois's note (7), "Sahag, prince des Bagratides, fut proclamé, en 481, marzban d'Arménie par ses compatriotes révoltés contre les Perses" (l.7963-7965). Faithful, with the identification given to Langlois.
- The journey: "Sahag le Grand et Mesrob nous envoyèrent à Alexandrie" (l.24737-24739); Edessa, "les abîmes des archives", the holy places (l.24758-24763); "un nouveau Platon ... ce docteur dont je ne me suis pas trouvé digne d'être le disciple" (l.24830-24832); the winds to Italy, Athens, then Byzantium (l.24836-24858). Faithful.
- Later life: ten years "dans l'isolement et la pauvreté"; Kiud; "à la mort d'Eznig de Goghp, comme évêque de Pakrévant"; "c'est du moins ce que raconte la tradition, qui s'est plu à entourer la vie de Moïse d'une foule de circonstances particulières, dont l'histoire n'a pas conservé le souvenir" (l.7856-7874). Thomas Ardzrouni for Zeno's reign and "plus d'un siècle" (l.7876-7881, 7896-7897). Faithful.
- Macler: "On ne sait pour ainsi dire rien de précis sur Lazar de Pharbi ou Moïse de Khorën" (`stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt` l.671-674). Faithful.
- I searched every held file that names Moses of Khoren (about fifty hits, among them Harnack's Chronologie, Ormanian, Issaverdens, Wardrop's Life of St Nino, Phillips's Doctrine of Addai, ANF 8, Macler's Sebeos). None argues a later date. Harnack lists Carrière's 1895 study by title only (l.9336-9337). The absence claim stands; see M1 for how it is told.

**Findings**
- **M1 MINOR (items 1, 4, 7; a dispute with one side and no witness for the dispute).** Brief l.9: "When Moses wrote is disputed. Langlois has him born in the later fourth century ... The Library holds no work that argues the other side." The brief never says what the other side is, so "the other side" has no context for a listener. Nor does any held line say the date is disputed: the records' `contested_claim` rests it on the Library file header of the Italian edition (ita l.4-5) and the era 3 scan. The Contested tag is the coordinator's call under the era 3 ruling and stands, but the brief should say plainly what is held and what is not. Fix, brief l.9: delete "When Moses wrote is disputed.", and replace "The Library holds no work that argues the other side." with "Modern work argues for a later date, but the Library holds none of it." (15 words out, 14 in; the brief stays at about 323). Card `uncertain` 1 and `dates`: the same wording. README or Open-Gaps: log that the dispute rests on no held line.
- **M2 MINOR (item 1; a closed claim a held file contradicts).** Card `uncertain` 5: "Thomas Artsruni's report that he lived past a hundred, into Zeno's reign, reaches us only through Langlois's note." The Mekhitarist preface also gives a long life on Thomas Artsruni's authority: "E centovent' anni viss'egli" (OCR "cen- vcnl anni viss'egli", ita l.163-164), with its footnote 7, "Tommaso Arzcrunio lib. I" (ita l.181). Fix: "Thomas Artsruni's report that he lived past a hundred, into Zeno's reign, comes through Langlois's note; the Mekhitarist preface, citing the same writer, gives him a hundred and twenty years. Langlois says his age cannot be fixed with exactness." Records: add the preface (ita l.163-164, 181) to the witness of the claim "Lived past a hundred, into Zeno's reign".
- **M3 MINOR (item 2; an OCR fault quoted as the source's words).** Card `legacy.remembered` 1 quotes Langlois as "classé à la tète des historiens de sa nation". "tète" is the OCR's reading of "tête"; as printed on the card it is a different French word. A card quotation cannot silently correct the file, and should not show the fault. Fix: quote only the clean words, "Victor Langlois places him at the head \"des historiens de sa nation\"." (l.7938, exact), and leave `legacy.traces` 1 as it is.

---

## 3. Barsauma of Nisibis (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1, M3, M7) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M5) |
| 5 | No role for a witness | PASS (his letters, Chabot, Scher, Bar Hebraeus, Mari, Barhadbeshabba, Connolly named) |
| 6 | Partisan witness named and marked | PASS (Bar Hebraeus "told his story against him", "hostile" on the card; Barhadbeshabba of his own church) |
| 7 | Contested both sides | PASS on the bishopric, Babai's death and the marriage; closed list M1 |
| 8 | Common names placed | FAIL, minor (M4, M6) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:30, at the cap) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; keyWorks minor (M3) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact; speaker confirmed)
- "du fougueux évêque de Nisibe" (card): Chabot's appendix (`synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt` l.34804-34806), Chabot speaking.
- "composa lui aussi beaucoup d'homélies" (card): the Cause of the Foundation of the Schools (`barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt` l.20801, "Barsauma composa lui aussi beaucoup d'homélies avec d'autres instructions"). Exact. The card gives it to "Barhadbeshabba"; see M6 on which Barhadbeshabba.
- "what is now known as the Nestorian Church" (card): Connolly's introduction (`narsai_liturgical-homilies_connolly1909.txt` l.4485-4486).

**Narrative checks**
- The third letter (l.1, l.13): "Dans le temps que Satan a suscité une querelle entre moi et Mar Baboui, je suis monté et j'ai cédé à l'instigation de tous les évêques délinquants contre lesquels il voulait porter un jugement ... nous nous réunîmes dans la ville de Beit Laphat ... statuâmes des canons par la passion humaine" (l.35395-35406); "le synode que nous avons tenu était contraire au christianisme" (l.35454-35455); "Nisibe est agitée, troublée et ballottée comme une mer tumultueuse" (l.35479-35480). Faithful.
- The second letter (l.5): two years' drought, the southern tribes, the Tou'ayé "sujets des Perses" raiding "même dans le territoire des Romains"; "nous persuadâmes au général de venir à Nisibe, près du marzban ... Tandis qu'ils étaient ensemble à boire, manger et se réjouir, les Tou'ayé ... fondre sur les villages inférieurs des Romains ... le général ... s'emportèrent contre nous ... Il ne nous est donc pas possible maintenant de nous rendre à l'invitation écrite" (l.35275-35334). Faithful. Chabot's note, "Nisibe était sur la frontière des deux empires" (l.35298-35300), supports l.3's first sentence.
- Chabot's note (l.3): "Bar Çauma, d'abord esclave de Marê de Qardou, étudia à l'École d'Édesse, où il se trouvait encore en 449. Il fut expulsé à la mort d'Ibas (457) et devint évêque de Nisibe, grâce à la faveur du roi Pérôz ... qui le fit même, semble-t-il, marzban ... Au mois d'avril 484" (l.20229-20239). Scher: "Barsauma fut nommé évêque de Nisibe en 435, ainsi que le disent Élie et Ebedjésus de Nisibe" (PO 4 l.20820). Faithful.
- Bar Hebraeus (l.7, l.9, l.11): "catholicum vero accusavit veluti exploratorem Graecorum" (`barhebraeus_chronicon-ecclesiasticum-vol3-lat_abbeloos-lamy1877.txt` l.3836-3847); "militibus Persis adductis ... multum fidelium sanguinem effudit" (l.3956-3960); "Ferunt numerum a blasphemo Barsuma Nisibeno interfectorum ad septem millia et septingentos ascendisse" (l.4073-4075); the woman "in cella ... quam sine pudore uxorem legitimam vocabat" beside bishops' "concubinas" (l.3757-3764); "Quidam referunt monachas in Turabdino ... clavibus cellarum suarum occidisse; alii vero Nisibi in ecclesia Mar Jacobi ejusdem sepulcrum ostendunt" (l.4546-4552). Chabot: "cet auteur est si inexact dans son récit de l'histoire de Bar Çauma" (l.41054-41056). Faithful.
- Mari (l.7, l.9): Barsauma "Babuaeum apud Peroz accusavit ... Ferunt Barsaumam mox factum doluisse" (`mari-ibn-sulayman_de-patriarchis-nestorianorum-commentaria-pars-prior-ara-lat_gismondi1899.txt` l.14355-14362); "Barsaumas itaque Mammaeam monialem uxorem duxit, nuptiasque episcopis ac presbyteris licitas fecit" (l.14386-14387). Faithful but for M7.
- Barhadbeshabba (l.9): "Comme Mar Barsauma était un homme (à l'esprit) pénétrant" (`po09_barhadbeshabba-ecclesiastical-history-part2-and-others-fra_1913.txt` l.36540-36542); the welcome and the school (l.36936-37081). Faithful.

**Findings**
- **M1 MINOR (items 1, 7; a closed list three held files extend).** Card `uncertain` 3: "That he caused Babai's death rests on Bar Hebraeus and on Mari ibn Sulayman ... Chabot also reports it from the writer 'Amr, whose work is not used here." 'Amr is held: he tells that Peroz gave Barsauma charge of Nisibis and its border lands, that Babai's letter to the emperor Leo was taken by Barsauma's guards and sent on by him to the king unopened, "quin aperiret", and that the physician Gabriel twisted it in translation (`amr-ibn-matta_de-patriarchis-nestorianorum-commentaria-pars-altera-ara-lat_gismondi1896-1897.txt` l.14043-14061). Michael the Syrian's Chronicle is held, with the letter of Maruta of Tagrit behind Bar Hebraeus's account; Chabot's note there says Maruta's story "perd une grande partie de son autorité ... par l'aveu sincère de l'auteur qui déclare l'avoir rédigé uniquement d'après des traditions orales, et plus d'un siècle et demi après les événements", and that Bar Hebraeus gives it "sans indication de l'origine" (`michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt` l.33474-33479). Jérôme Labourt reports Maruta's letter making Barsauma himself order Babai's tongue and head cut off, and calls the Bar Hebraeus picture "une confusion regrettable" (`labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt` l.8081-8090, 8046). "Whose work is not used here" is also build narration on a participant card. Fix, card `uncertain` 3: "That he caused Babai's death rests on later writers. Bar Hebraeus says so, and Chabot says Bar Hebraeus took the story from the letter of Maruta of Tagrit, written from oral tradition more than a century and a half later. Mari ibn Sulayman tells of the accusation and a report that Barsauma soon regretted it. 'Amr says Barsauma sent Babai's letter to the king unopened and the physician Gabriel twisted it. Barsauma's own letters say only that Satan stirred up a quarrel between them." Add `sources.about` entries for 'Amr (Gismondi 1896-1897), Michael the Syrian (Chabot, tome II) and Labourt. Records: add 'Amr and Maruta (via Michael) to the `contested_claim` "Whether he caused Babai's death". The brief needs no change: it gives the death as Bar Hebraeus's and Mari's and marks Chabot's caution.
- **M2 MINOR (records; an absence claim a held file contradicts).** `absent_details` 1: "no held line gives his birth or parents". Labourt: "Nous ignorons la date de sa naissance. On doit sans doute la placer vers 415-420" (Labourt l.7738-7740), and on Mare of Qardu, "C'est-à-dire probablement qu'il était né sur ses terres" (l.7750). Fix: "No ancient witness gives his birth; Jérôme Labourt places it about 415 to 420 (l.7738-7740). No held line names his parents." Labourt also puts his death "entre 492 et 495" (l.8875); add it beside Chabot's "after 491" in the records' death claim.
- **M3 MINOR (item 1; card keyWorks and sources).** The keyWorks title is "Letters to the catholicos Acacius" and its `about` says "six letters". The `ownWords` entry is "Letters to Acacius". The first of the six is addressed "Aux excellents Mihrnarsé, Siméon, Moïse, Yezdegerd et Daniel, évêques", from Barsauma and eleven other bishops (Chabot l.35203-35205). Fix: keyWorks title "Letters to the catholicos Acacius and to the bishops"; `about` "six letters kept in the Synodicon orientale, five to Acacius and one, from Barsauma and his bishops, to five bishops, retracting the synod of Beth Lapat …"; `ownWords` title "Letters to Acacius and to the bishops, in the Synodicon orientale (ed. and tr. J.-B. Chabot)".
- **M4 MINOR (item 8; namesakes at first mention).** (a) Brief l.9: "Barsauma welcomed Narsai, a teacher from the school of Edessa" uses a role, and the README says both briefs give "Narsai of Nisibis" at first mention. The card's `knownFor` has bare "Narsai". (b) Brief l.1 and card `knownFor`: "the catholicos Acacius", where Acacius of Constantinople is his contemporary (Labourt l.8116) and a place identifies him: Barsauma speaks of "la sainte église de Séleucie et Ctésiphon" (Chabot l.35473). Fixes: brief l.1, "wrote to the catholicos Acacius of Seleucia-Ctesiphon"; brief l.9, "welcomed Narsai of Nisibis, then a teacher at the school of Edessa"; card `knownFor`, "letters to Babai's successor Acacius of Seleucia-Ctesiphon, and who welcomed Narsai of Nisibis". Word cost and cuts under M5.
- **M5 MINOR (item 4; a thesis opener in a stock phrase).** Brief l.5 opens "His own letters show a bishop caught between two empires." The paragraph's facts carry the point without it. Fix: "In his second letter, he told Acacius why he could not come." and end the paragraph "The Romans blamed Barsauma." (net -7 words). Brief l.3: "In a note he says Barsauma" becomes "He says Barsauma" (-2). With M4 (+4), M6 (+1) and M7 (+3) the brief comes to about 404 words.
- **M6 MINOR (item 8; Barhadbeshabba as one man).** Brief l.9 and the card's `legacy.remembered` 1 and `uncertain` 6 give "Barhadbeshabba" bare. Held files name more than one: Labourt lists "un certain Barhadbešabba de Qardu" among Ibas's Persian pupils (Labourt l.7834), and Nau gives the History to Barhadbeshabba 'Arbaia, of Beth 'Arbaye (PO 9 l.31552-31556). The card also gives the "quick mind" (History, PO 9) and the "composa lui aussi beaucoup d'homélies" (Cause, PO 4) to one "Barhadbeshabba", which Nau leaves open (see Narsai B1). Fixes: brief l.9, "Barhadbeshabba 'Arbaia, a historian of Barsauma's own church"; card `legacy.remembered` 1, "Barhadbeshabba 'Arbaia, of his own church, praises his quick mind; the Cause of the Foundation of the Schools, by Barhadbeshabba, bishop of Halwan, says he \"composa lui aussi beaucoup d'homélies\"."; `sources.about` Cause entry author "Barhadbeshabba 'Arbaya, bishop of Halwan" (as Scher's title page gives it, PO 4 l.575, 656).
- **M7 MINOR (item 1; a dropped hedge).** Brief l.7: Mari "says Barsauma soon regretted it". Mari reports it: "Ferunt Barsaumam mox factum doluisse" (Gismondi l.14363). Fix: "and reports that Barsauma, it was said, soon regretted it." (+3). Card `uncertain` 3 is covered by M1's wording.
- **M8 MINOR (records; tags).** The marriage claim is tagged Widely Accepted though a `contested_claim` ("His wife") stands behind it. Fix: tag it Contested, to match the contested record and the card's "told two ways".

---

## 4. Narsai (major)

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, blocking (B1); minor (M1) |
| 2 | Quotes verbatim | PASS |
| 3 | No invention | FAIL, minor (M1: "the monk") |
| 4 | Reading aids | PASS |
| 5 | No role for a witness | PASS (Barhadbeshabba, Nau, Connolly, Mingana, Simeon, Mari, Bar Hebraeus named) |
| 6 | Partisan witness named and marked | PASS (Simeon "of the opposing side"; Bar Hebraeus "hostile" on the card; Barhadbeshabba's saint's life on the card) |
| 7 | Contested both sides | FAIL, blocking (B1); minor (M4) |
| 8 | Common names placed | FAIL, minor (M2) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:27) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS |

**Quotes** (all exact; speaker confirmed)
- "Edessa was darkened, but Nisibis shone forth" (l.7, card): Connolly's English (`narsai_liturgical-homilies_connolly1909.txt` l.4494) of the chronicle Mingana printed, which Connolly calls "a fragment of a chronicle by Barhadhbeshabba (saec. VI-VII)" (l.274-276). It is the Cause of the Foundation of the Schools: "Édesse s’obscurcit; Nisibe s’illumina" (Scher, PO 4 l.20744). See B1.
- "instead of our clay He has made us spiritual gold." (l.15): Homily XXII, On Baptism (Connolly l.6855-6856), Narsai speaking of the Creator. Exact.
- "what is now known as the Nestorian Church" (card): Connolly l.4485-4486.

**Narrative checks**
- The flight (l.1): "un de ses amis ... courut aussitôt annoncer au saint que s'il ne s'enfuyait pas cette nuit même ... on le jetterait au feu ... il y trouva des Perses, et il leur demanda ... d'emporter ses livres avec eux, car c'était là tout son trésor ... jusqu'à Nisibe" (PO 9 l.36830-36839). Nau: the History "a donc toute chance d'avoir été écrite à la fin du VIe siècle" (l.31574-31575). Faithful.
- Ma'alta, school at seven, the Psalter in nine months (PO 9 l.36179-36180, 36390-36393); twenty years at Edessa (l.36633). The charges, "Cet interprète est hérétique parce qu'il adhère à la pensée de Théodore et de Nestorius", and "sa pensée était avec les Perses ... qu'il voulait livrer la ville d'Édesse", after "Comment un homme perse a-t-il subjugué les Romains" (l.36684-36698), which supports "a Persian Christian". Faithful.
- Nau's note on the bishop: "Évêque de 471-498 ... Au lieu de Qourâ, il faudrait donc lire Nonnus, évêque de 457 à 471 ... Si l'on maintient la lecture de notre auteur, Narsès n'a pas quitté Édesse avant 472 ... Il ne serait pas mort avant 512" (l.36699-36705). Faithful.
- Nisibis: the monastery of the Persians, his plan to go into Persia; "il lui acheta, pour l'école, une écurie de chameaux (Beit-gamlê) qui était près de l'église ... des frères commencèrent à se réunir de tous côtés" (l.36931-36940, 37075-37081). The wife Mamai, the crowds, the retreat to Kefar-Mari, the mimra on "la femme de Mar Barsauma", and "l'évêque se repentit et il le fit revenir" (l.37118-37175, 37182). Jacob of Sarug "qui adhérait à l'hérésie", and "un mimrâ pour chaque jour de l'année" (l.37258-37271). "enseveli dans une bonne vieillesse" (l.37412). Faithful.
- Connolly: 457 and the 45 years to 502, after Mingana (l.257-260, 297-302); "all his proficiency in the Scriptures was derived from the study of Theodore's commentaries", from the Homily on the three Doctors (l.4536-4539). Nau, 503 or 504, and 507 for those who follow Bar Hebraeus's fifty years (PO 9 l.37421-37428). Simeon's "Narses leprosus", quoted from Assemani by Abbeloos and Lamy (Bar Hebraeus vol. III l.3690). Faithful.

**Findings**
- **B1 BLOCKING (items 1, 7; an identification told as settled where its editor doubts it).** The brief, card and records treat the author of the History (PO 9, Nau) and the author of the Cause of the Foundation of the Schools (PO 4, Scher) as one Barhadbeshabba. Card `uncertain` 3: "forty in Barhadbeshabba's history, forty-five in his other work on the schools". Card `legacy.traces` 1: "Barhadbeshabba, as R. H. Connolly translates him: \"Edessa was darkened…\"", a line from the Cause. Brief l.7: "In Connolly's English of Barhadbeshabba", after l.1 has introduced Barhadbeshabba as the author of the History. Records claim 2: "its author probably the bishop of Halwan of 605". Nau gives the History to Barhadbeshabba 'Arbaia named by Ebedjesu, says the bishop of Halwan of 605 wrote the Cause, and holds their identity only possible: "Il n'est pas impossible que notre auteur de «l'Histoire des saints Pères», identique à l'auteur cité par Ebedjésus, soit encore identique à l'évêque de Halwan" (PO 9 l.31601-31604, with l.31579-31580 and 31598). Fixes, checked against those lines:
  - Brief l.7: "In Connolly's English of a chronicle of the school, \"Edessa was darkened, but Nisibis shone forth\"." (+4 words, about 402).
  - Card `uncertain` 1, add: "François Nau gives the History to Barhadbeshabba 'Arbaia, and the Cause of the Foundation of the Schools to Barhadbeshabba, bishop of Halwan in 605; he thinks it not impossible that they are one man."
  - Card `uncertain` 3: "forty in Barhadbeshabba's History, forty-five in the Cause of the Foundation of the Schools, and fifty in Bar Hebraeus."
  - Card `legacy.traces` 1: "The Cause of the Foundation of the Schools, as R. H. Connolly translates it: \"Edessa was darkened, but Nisibis shone forth\". It names Narsai and his successors as the heads of the school of Nisibis."
  - Card `sources.about`: Cause entry author "Barhadbeshabba 'Arbaya, bishop of Halwan". Records claim 2: "its author Barhadbeshabba 'Arbaia; Nau thinks his identity with the bishop of Halwan of 605, author of the Cause, not impossible", tagged Inferential-Thin.
- **M1 MINOR (items 1, 3; card).** `legacy.remembered` 1: "the monk Theodulus called him the tongue of the East". Mari calls Theodulus a disciple of Diodore, and gives a second title: "Theodulo Mar Diodori discipulo obvius fuerat a quo benedictus fuit appellatusque orientis lingua ac christianae religionis poeta" (Gismondi l.14346-14347). No held line makes Theodulus a monk. Fix: "Mari ibn Sulayman, writing in the 1100s, reports that Theodulus, a disciple of Mar Diodore, blessed him and called him the tongue of the East and the poet of the Christian religion."
- **M2 MINOR (item 8; display name and a namesake).** (a) The card's `name` is "Narsai", with "Narsai of Nisibis" in `otherNames`. The pattern's Naming rule gives the display name "with 'of <place>' where the name alone is not enough", and only the id is never renamed. The README says the held files name other Narsais, and so the name alone is not enough. Fix: `name` "Narsai of Nisibis"; `otherNames` "Narsai", "Narses"; the id stays `narsai`. (b) "Barhadbeshabba" at first mention in brief l.1 and the card, as in Barsauma M6: Labourt names a Barhadbeshabba of Qardu (Labourt l.7834). Fix: brief l.1, "Barhadbeshabba 'Arbaia tells it" (+1); card `uncertain` 1, "Barhadbeshabba 'Arbaia".
- **M3 MINOR (records; tags).** "From the land of Ma'alta" is tagged Inferential-Thin, though Barhadbeshabba states it (PO 9 l.36179) and Mari agrees, "Ma'allaia oriundus" (Gismondi l.14346). Tag it Widely Accepted. The wife's jealousy is tagged Widely Accepted while the `contested_claim` "The cause of the break with Barsauma" stands behind it; tag it Contested.
- **M4 MINOR (item 7; a held editor's doubt on the year left out).** Card `uncertain` 2 and the records' `contested_claim` "When he left Edessa" give Connolly's 457 and Nau's note. Addai Scher, editing the Cause, writes "Il est donc inexact que Narsaï et ses compagnons aient été tous ensemble expulsés d'Édesse en 457, comme le racontait Siméon de Beth-Arscham" (PO 4 l.20622-20623), and works his own dates out only "Si l'expulsion de Narsaï a lieu en 457" (l.20750). Fix, card `uncertain` 2, add: "Addai Scher, editing Barhadbeshabba's Cause, doubts that Narsai and his companions were expelled together in 457, as Simeon of Beth Arsham told it." Records: add Scher's side (PO 4 l.20622-20623, 20750).

---

## Totals

Part B: 2 blocking, 18 minor (Victor of Vita 1 and 3, Moses of Khoren 0 and 3, Barsauma of Nisibis 0 and 8, Narsai 1 and 4). Vakhtang I Gorgasali was rescored STORY by the coordinator and left the batch during the review; it is not reviewed.

## R1 review: era 3 batch 1, part C (Lazar Parpetsi and the README)

Reviewer: independent, first sight of this draft. Branch `who-profiles-era3-batch1`, commit 1ce276f4. Bar: `Who_Profile_Pattern.md` review checklist 1 to 14 and the standards it points to; `CLAUDE.md` "Trust and source fidelity" and "Accessible and rigorous"; Mark's rulings in the Decision-Log (2026-11-12: majors capped at 2:30; non-majors 1 to 2 minutes, at most about 324 words at 162 words a minute). I hunted above all for witness swaps and for absence claims a held file contradicts. I did not edit the drafts. I made no paid or model-API calls and used no web. Readability and quote search ran on local scripts only.

Scope: `lazar-parpetsi` (not major; a Who as a recorder): `lazar-parpetsi.brief.txt`, `lazar-parpetsi.card.json`, `audio/lazar-parpetsi.audio.txt`, its entry in `records.json`, and the README paragraphs on Lazar and the batch order. Files are in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch1/`. For consistency I compared it with `vardan-mamikonian` and `elishe` in the same batch and with `era2/batch6/eznik-of-kolb`. Brief line numbers refer to the `.brief.txt` file, where each paragraph is one line and blank lines count (paragraphs on l.1, 3, 5, 7, 9, 11). Other line numbers point to files under `cic/texts/`; "Langlois t2" is `langlois_collection-historiens-armenie-tome2-fra_1869.txt`.

Method. I found every quotation and close paraphrase of the brief, card and records in Langlois t2 (raw djvu OCR: I read each passage by line number and searched tolerantly, since the OCR breaks words and swaps letters). I read each hit in context to see who speaks: Lazar's own History (from l.35370), Langlois's introduction (l.35073–35357, signed "V. L." at l.35357), Langlois's Discours préliminaire (signed "Victor Langlois", l.2689; Lazar at l.2638–2645), or a footnote. I checked every factual sentence against its passage. Before accepting any absence claim I searched the whole of `cic/texts/` for every spelling of the name (Lazar, Lazare, Lazarus, Lazzaro; Pharp, Pharbe, Parpi, Barb, Pharbeci, Farpense, Parpetsi). Readability came from `engine.m1.gates.grade_text`, run from the repo root.

## Summary

| Profile | Words | Est. length @162 | FK | Flesch |
|---|---|---|---|---|
| Lazar Parpetsi | 325 | 2:00 | 7.9 | 66.2 |

- **Audio = brief.** The audio script matches the brief exactly once `[calmly] ` and `[warmly] ` are removed (checked by script). One `[calmly]` at the start, one `[warmly]` before the closing paragraph. No tag in the brief or card.
- **Readability.** Passes (FK 7.9, Flesch 66.2). No narrator sentence runs past 25 words; l.3 has one at exactly 25.
- **Length.** 325 words, at the non-major cap. The fixes below add words; the combined fix text at the end brings the brief to 323 words (FK 7.7, Flesch 67.2), checked by script.
- **Card order.** Mark's order holds. keyWorks has two entries. `uncertain` opens with the brief's own caveat (the life rests on Langlois's introduction, which leans on a letter the Library does not hold).

| # | Item | Result |
|---|---|---|
| 1 | Source establishes each sentence | FAIL, minor (M1, M3, M4) |
| 2 | Quotes verbatim | PASS (see quotes below) |
| 3 | No invention | PASS |
| 4 | Reading aids | FAIL, minor (M2, M5) |
| 5 | No role for a witness | PASS (Langlois, Lazar, Ormanian, Conybeare, Ghesarian named; "a note in the French edition" is honest, since the hand of the notes is not certain: the title page gives them to Ghesarian, l.35063–35066, but some speak as Langlois, "notre Collection", l.35427) |
| 6 | Partisan witness named and marked | PASS (Lazar writes at Vahan's order and tells his patron's lapse, brief l.9 and card `uncertain` 4) |
| 7 | Contested both sides | FAIL, minor (M6) |
| 8 | Common names placed | PASS on places; context minor (M2, M5) |
| 9 | One term | PASS |
| 10 | Story, scene, disputes in place, length | PASS (2:00) |
| 11 | grade_text | PASS |
| 12 | Card order, caveat repeated | PASS on order and caveat; dates and legacy FAIL (B1, M7) |
| 13 | Audio tags | PASS |
| 14 | Who test | PASS (a recorder whose History is a main source for the war of 451 and Vahan's revolt). No list line is carried in the draft; that belongs to the map build and was not checked |

**Quotes and close tellings** (all found; speaker confirmed)
- l.1, the captive princes: Lazar, ch.53, "quelques-uns des satrapes prisonniers, c'est-à-dire de ceux que j'ai vus de mes propres yeux" ... "ils avaient établi des écoles à leur propre usage, où ils apprenaient la doctrine de l'Église" ... "ils suivaient les exercices spirituels même dans le camp" ... "En prenant les armes, ils récitaient mentalement des psaumes" (Langlois t2 l.43182–43198). Lazar speaking. See M1.
- l.1, Avarayr: Lazar names it, "près du village appelé Avaraïr" (l.40208).
- l.3, dates and name: Langlois's introduction, "Il vécut à la fin du cinquième siècle ou au commencement du sixième. Son surnom de Pharbetzi ne lui vient pas du lieu de sa naissance, mais ... du séjour prolongé qu'il fit au couvent du village de Pharbe ou Pharbi, petite localité de la province d'Ararat" (l.35079–35085). Signed "V. L." (l.35357). The brief rightly gives it to Langlois. See B2 for the Vardan profile, which does not.
- l.5: "le compagnon d'enfance de Lazare" (l.35133–35134); leave "de saint Sahag et de saint Mesrob" to go to Greece (l.35149–35152); Vahan made marzban "par la cour de Perse" (l.35172–35174) and "lui confia l'administration de la métropole" of Etchmiadzin (l.35195–35203). The noble family is inferred "d'un passage de sa Lettre à Vahan" (l.35099–35101), which supports "draws partly on a letter".
- l.7: "la jalousie de quelques membres du clergé" ... "ses doctrines étaient contraires à la vraie foi" (l.35216–35222); "lui refusèrent même le droit d'emporter les livres grecs qu'il avait rassemblés" (l.35244–35246); Tigranocerta and "une longue lettre", "il répondait point par point" (l.35250–35256); "Il paraît que cette lettre produisit sur Vahan l'effet que Lazare en attendait, car le marzban rappela sans retard auprès de lui son ancien ami" (l.35257–35260). Faithful. See M3.
- l.9: Vahan's order, "le marzban Vahan ... nous oblige d'écrire rapidement, dans l'ordre qu'il a adressé à moi Lazare de Pharbe" (l.35732–35735); title line "écrite à la demande du seigneur Vahan" (l.35383). End point: "jusqu'au jour où Vahan ... prit le gouvernement de l'Arménie; et là, je terminerai" (l.35445–35448); the History does close with Vahan's investiture and John Mandakuni's sermon (ch.85–86, l.48918–49225). Faustus: l.35711–35720, see M4. Vahan's lapse: ch.58, "ne pouvant plus supporter des calomnies continuelles, se rendit à la Porte, et là il faiblit dans sa foi" (l.43802–43805). Faithful.
- l.11: "Le présent ouvrage, oeuvre de notre faiblesse, va former comme la troisième partie de ces annales" (l.35413–35414; OCR "fiiiblesse"), after Agathangelos (l.35389) and "un certain Faustus de Byzance" (l.35401–35402). Lazar speaking. "His weakness" for "notre faiblesse" is a fair turn of the author's plural, told as paraphrase.
- Card `remembered` 1: Discours préliminaire, "termine la série des écrivains de l'âge d'or" and the Letter "considérée à juste titre comme un chef-d'œuvre de style" (l.2638–2645). Langlois speaking.
- Card `remembered` 2: Ormanian, "Lazarus of Parpi" among "the learning of ecclesiastics" (`ormanian_church-of-armenia_gregory1912.txt` l.8739–8742). "Formerly Armenian Patriarch of Constantinople" is the file's own title-page creator line (l.2).
- Card `otherNames`: "Lazar of Pharp" is Conybeare's glossary, in his own voice (`rituale-armenorum-lectionary_conybeare1905.txt` l.37861); "le Rhéteur" (Langlois t2 l.35075, 35154–35157).
- Card `uncertain` 3, 5, 6: Siunik and the hermit Moses, two years (l.35164–35167); the tomb, "où, dit-on, le tombeau de Lazare existe encore actuellement" (l.35094–35096); one edition, Venice (l.35282–35287), and "le seul texte qu'il avait à sa disposition est malheureusement incorrect" (l.35346–35348). Faithful.
- Card `legacy.traces` 2: Langlois's notes to Moses of Khoren (his introduction, signed "Victor Langlois" at l.8539, says "les annotations qui accompagnent la traduction nouvelle que nous publions" are his, l.8523–8526) and to Elishe ("traduction nouvelle accompagnée de notes historiques et critiques par Victor Langlois", l.25698–25703) name Lazar on more than thirty lines between them (l.7777–35060). Faithful.
- Card `dates` and `uncertain` 2, the 486 to 511 figure: notes at l.35473–35475 and l.48958–48961. See B1.

## Findings

- **B1 BLOCKING (items 1, 12; an absence claim a held file contradicts).** `records.json`, `absent_details` 1, says "the census year 485 rests on no held line", and the card's `dates` and `uncertain` 2 give only the French note's 486. Charles Neumann's preface to his English Elishe gives the span of Lazar's History: "the history of Lazarus Barbezi, which includes the period from the decline of the Arsacide kingdom in Armenia, till the Margravate of Vahan, the Mamigonian, from 428 to 485" (`eghishe_history-of-vartan-and-the-armenian-war_neumann1830.txt` l.1019–1021). Langlois's own figure for the History's end, "jusqu'à l'an 4.. de notre ère" (Langlois t2 l.35267–35268), is lost in the OCR. So two held editors date the History's end: Neumann to 485, the French note to 486. Fixes:
  - Card `dates`: "Victor Langlois places him at the end of the fifth century or the start of the sixth. His History ends with Vahan made governor of Armenia, which a note in the French edition dates to 486 and Charles Neumann, in the preface to his English Elishe, to 485. No source used here gives his birth or death".
  - Card `uncertain` 2: "Langlois's dates for him are broad: the end of the fifth century or the start of the sixth. The notes in the French edition date Vahan's rule as governor from 486 to 511. Charles Neumann has the History run from 428 to 485."
  - Card `sources.about`: add `{"title": "Preface to Elishe's History of Vartan", "author": "Charles Neumann", "date": null, "language": "English", "file": "cic/texts/eghishe_history-of-vartan-and-the-armenian-war_neumann1830.txt"}`.
  - Records: `absent_details` 1 note: "No held line gives his years. Langlois infers a noble family from the Letter to Vahan (l.35103-35106), which is not held. The census year 485 matches Charles Neumann's end date for the History, 'from 428 to 485' (eghishe_neumann1830 l.1019-1021); Langlois's own year for it (langlois t2 l.35267-35268) is lost in the OCR." Add a claim: "The History runs from 428 to 485", witness "Charles Neumann, preface to Elishe (eghishe_neumann1830 l.1019-1021); an editor's date", `Dominant Modern Reconstruction`.

- **B2 BLOCKING (cross-profile contradiction; items 1, 5; a witness swap in `vardan-mamikonian`).** The Lazar brief l.3 gives the dating "the end of the fifth century or the start of the sixth" to Victor Langlois. That is right: the introduction holding it is signed "V. L." (Langlois t2 l.35357). The Vardan brief l.1 gives the same date to "His translator, Samuel Ghesarian", and its record reads "Lazar places himself at the end of the fifth century or the start of the sixth", witness "Ghesarian's introduction to Lazar (langlois t2 l.35066-35069); a translator's date". Lines 35066–35069 are the title page, and Lazar does not place himself. The error looks carried from the era 3 scan, whose row 54 calls it "translator Ghesarian's introduction". Fixes, in the Vardan files: brief l.1, "His translator, Samuel Ghesarian, places Lazar at the end of the fifth century or the start of the sixth." → "Victor Langlois, who edited Lazar's History in French, places Lazar at the end of the fifth century or the start of the sixth." Records (vardan-mamikonian): claim "Victor Langlois places Lazar at the end of the fifth century or the start of the sixth", witness "Langlois's introduction to Lazar (langlois t2 l.35079-35080; signed V. L., l.35357); an editor's date", `Dominant Modern Reconstruction`, as the Lazar record has it. Check the Vardan card for the same attribution when this is fixed.

- **M1 MINOR (item 1; a detail moved).** Brief l.1: "He writes that they set up schools in the camp to learn church teaching." Lazar says they set up schools "à leur propre usage", and separately that "ils suivaient les exercices spirituels même dans le camp" (Langlois t2 l.43186–43194). The schools are not placed in the camp. The records claim 1 has the same joining ("set up schools to learn the church's teaching, even in the camp"). Fix, brief l.1: "He writes that they set up schools to learn church teaching. Even in the camp, they said the psalms in their minds as they took up their weapons." Records claim 1: "Saw some of the captive Armenian princes with his own eyes; they set up schools to learn the church's teaching, kept up their spiritual exercises even in the camp, and recited psalms in their minds as they took up arms".

- **M2 MINOR (items 4, 8; names with no context).** Brief l.5: "with leave from Sahak the Great and Mesrop Mashtots". A general listener is not told who they are. Langlois calls him "le patriarche saint Sahag" (l.35144). Fix: "He says Lazar studied in Greece with leave from the patriarch Sahak the Great and from Mesrop Mashtots." (The Eznik profile's "who made the Armenian letters" would add more context if length allows; the suggested text below keeps to the patriarch.)

- **M3 MINOR (items 1, 4; a step left out, so the next sentence has no context).** Brief l.7: the clergy's charge, then "From Tigranocerta he wrote Vahan a long letter answering each charge. Langlois says it seems to have worked, for Vahan called him back." The brief never says that Vahan believed the charges, so a listener does not know why Lazar had to win him back. Langlois: "Ils dénoncèrent Lazare au marzban qui prêta l'oreille à la calomnie et menaça son ancien ami de l'expulser" (l.35222–35225). Fix: "Then, Langlois says, jealous clergy accused his teaching of going against the true faith, and Vahan listened to them."

- **M4 MINOR (item 1).** Brief l.9: "suspecting that another writer or a careless copyist had added them." Lazar gives two different faults: another writer "aura interpolé dans son ouvrage des narrations absurdes", or a copyist "incapable de transcrire exactement, aura altéré l'ouvrage et détruit son ensemble" (Langlois t2 l.35715–35720). The copyist altered the work; he did not add the stories. The records claim says it rightly. Fix: "suspecting that another writer had added them or a poor copyist had altered the text."

- **M5 MINOR (items 4, 8; name with no context).** Brief l.11: "after Agathangelos and Faustus". Faustus has his context at l.9; Agathangelos has none. The closing sentence is also the brief's longest (24 words). Lazar calls Agathangelos the first to write "l'histoire d'Arménie" (l.35389–35390). Fix, l.11: "He called his History the third part of Armenia's annals, after the histories of Agathangelos and Faustus. In his own phrase, it was the work of his weakness."

- **M6 MINOR (items 7, 12; a held witness that tells Lazar's post differently).** Card `role`: "Historian; in charge of the mother church at Etchmiadzin", told plainly, and the records tag this claim Inferential-Thin, resting on Langlois alone. Stephen of Taron's Universal History, held in German, says that under Vahan "die große Hauptkirche Armeniens nochmals prächtig erneuert" was, and that he "vermehrte ... die Anzahl der Mönche von Surenay-Anapat (Wüste des Surenas) und gab ihnen zum Oberhaupt den Redner und Geschichtsschreiber Lazar Pharbeci" (`stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt` l.2930–2936; the file's catalogue line dates Stephen "fl. ca. 1000", l.22). That is an older witness, which puts Lazar over the monks of Surenay-Anapat, not over the mother church. The brief's own l.5 is attributed to Langlois and is fine. Fixes:
  - Card `role`: "Historian; by Langlois's account, in charge of the mother church at Etchmiadzin".
  - Card `uncertain`, add after item 3: "Stephen of Taron, an Armenian historian of about the year 1000, says instead that Vahan made him head of the monks of Surenay-Anapat."
  - Card `sources.about`: add `{"title": "Universal History (tr. Heinrich Gelzer and August Burckhardt)", "author": "Stephen of Taron", "date": null, "language": "German translation", "file": "cic/texts/stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt"}`. Use the form "Stephen of Taron", as the Moses of Khoren card does.
  - Records: add the claim with witness "Stephen of Taron (gelzer1907 l.2930-2936)", `Documented` (as what Stephen says), and note it beside the Etchmiadzin claim.

- **M7 MINOR (item 12; a loose absence claim).** Card `legacy.traces` 1: "With Elishe's History, it is one of the two held Armenian accounts of the war of 451". Stephen of Taron also tells the war, in a few lines that point to Elishe: Vardan "fiel in der Ebene von Averair ... im Kriege gegen Yazkert" (gelzer1907 l.2807–2819), and Malachia Ormanian writes of it too. Fix: "With Elishe's History, it is one of the two full Armenian accounts of the war of 451 that the Library holds, and it carries the story on through Vahan Mamikonian's revolt."

**README**
- **README-M1 MINOR (the order and the major mark, as they concern Lazar).**
  1. "The coordinator confirmed the major marks on 2026-11-13 ...; the other five are not." On 2026-11-13 the other five included Vakhtang I Gorgasali; Lazar joined on 2026-11-14 (commit d68a0ae3's README lists `vakhtang-i-gorgasali`, and says "Lazar of Parp ... goes to batch 2"). As written, the README says Lazar's non-major mark was confirmed a day before he joined the batch. Fix: "...; Elishe, Euthymius the Great, Victor of Vita and Moses of Khoren are not. Lazar Parpetsi, who took Vakhtang I Gorgasali's place on 2026-11-14, is not major." Add who made that call.
  2. "in order of death or last attested year as the scan gives it ... Narsai (about 503), then Lazar Parpetsi, whose row gives no year". The next WHO row of the scan by that order after Narsai is Vahan Mamikonian, "c.430s-c.505" (`Who_Scan_Era3.md` row 55, WHO). He was not removed in the dedupe (`Removed_Rows.md` has no Vahan). The README does not say why a row with no year goes before him. He is also the marzban ("governor") of Lazar's story, so Mark's "Story unless own voice" ruling for rulers may bear on him as it did on Vakhtang. Fix: add one sentence giving Vahan's place, for example "Vahan Mamikonian (about 505) is the next row by year and goes to batch 2," or the coordinator's rescoring if one is made.
  3. "The scan's ninth row, Vakhtang I Gorgasali" is ninth in the README's date order, not the scan's table (row 58 there). Fix: "The ninth by that order, Vakhtang I Gorgasali (499), ...".

## Consistency with Vardan Mamikonian, Elishe and Eznik of Kolb

- **Contradiction:** who dates Lazar (B2). Lazar's brief says Langlois; Vardan's says Ghesarian. Langlois is right.
- Agreements, checked: the tradition line "Armenian Christianity after Avarayr" (Lazar, Vardan, Elishe); "Sahak the Great" and "Mesrop Mashtots" (Lazar, Elishe, Eznik; Vardan has the patriarch Sahak the Great); "Lazar of Pharp" as the other form (Vardan and Eznik use it throughout, and the Lazar brief and card carry it); Malachia Ormanian as "a former Armenian patriarch of Constantinople" (Lazar card, Vardan brief and card); a note "in the French edition" of Lazar (Lazar card; Vardan card has "a note in Lazar's French edition" and "Victor Langlois's edition"). Eznik's card says Lazar names no place for the bishops' answer and makes King Yazdegerd the edict's author; nothing in the Lazar profile touches that. The Elishe profile says nothing of Lazar.
- Once B1 is fixed, the Lazar card gives 485 and 486 for Vahan's appointment. The Vardan and Elishe profiles do not date it, so nothing else needs to change.

## The brief with M1 to M5 applied

Checked by script against the current file: 323 words, about 2:00; FK 7.7, Flesch 67.2. To stay at the cap, it also cuts two things the card already holds: l.3's "who edited the French translation of his History" becomes "his French editor", and l.9's list of what the History covers goes (it is in the card's `knownFor`). The audio script follows with `[calmly] ` at the start and `[warmly] ` before l.11.

> After the battle of Avarayr, the Persian king held Armenian princes captive. Lazar Parpetsi, also called Lazar of Pharp, says he saw some of them with his own eyes. He writes that they set up schools to learn church teaching. Even in the camp, they said the psalms in their minds as they took up their weapons.
>
> Lazar was an Armenian historian. Victor Langlois, his French editor, places him at the end of the fifth century or the start of the sixth. Langlois says the name Parpetsi came from a long stay at the monastery of Pharp, a village in Ararat, and not from his birthplace.
>
> Most of his life story comes from Langlois's introduction, which draws partly on a letter of Lazar's that the Library does not hold. Langlois calls him a childhood companion of Vahan Mamikonian. He says Lazar studied in Greece with leave from the patriarch Sahak the Great and from Mesrop Mashtots. When Vahan governed Armenia for the Persian king, he put Lazar in charge of the mother church at Etchmiadzin.
>
> Then, Langlois says, jealous clergy accused his teaching of going against the true faith, and Vahan listened to them. His enemies drove him out and would not let him take the Greek books he had gathered. From Tigranocerta he wrote Vahan a long letter answering each charge. Langlois says it seems to have worked, for Vahan called him back.
>
> Lazar says Vahan ordered him to write. His History ends on the day Vahan took the government of Armenia. Lazar doubted some stories in Faustus of Byzantium, suspecting that another writer had added them or a poor copyist had altered the text. He also tells that Vahan, his patron, worn down by slander, weakened in his faith at the Persian court.
>
> He called his History the third part of Armenia's annals, after the histories of Agathangelos and Faustus. In his own phrase, it was the work of his weakness.

Totals, part C: 2 blocking, 8 minor (Lazar Parpetsi 1 blocking and 7 minor; README 1 minor; Vardan Mamikonian, cross-profile, 1 blocking).
