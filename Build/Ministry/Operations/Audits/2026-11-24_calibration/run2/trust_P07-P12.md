# Trust gate: P07 to P12

Reader: a historian of Christianity, with the vendored sources open (`cic/texts/`) and the census cards (`cic-website/data/world-census.json`).

| Piece | Subject | Sentences checked | HELD | SUMMARY HOLDS | SOFTENED | ASSUMPTION | MODERN ONLY | NOT FOUND | Gate |
|---|---|---|---|---|---|---|---|---|---|
| P07 | Ulfila | 38 | 24 | 6 | 1 | 1 | 6 | 0 | **FAIL** |
| P08 | Epiphanius of Salamis | 44 | 30 | 10 | 1 | 0 | 3 | 0 | **FAIL** |
| P09 | Catholic Church of the Ancien Régime | 24 | 12 | 7 | 1 | 0 | 2 | 2 | **FAIL** |
| P10 | Priscillian | 43 | 30 | 8 | 0 | 0 | 5 | 0 | **FAIL** |
| P11 | Jerome | 38 | 23 | 7 | 1 | 0 | 7 | 0 | **FAIL** |
| P12 | Tacitus | 29 | 18 | 2 | 0 | 0 | 9 | 0 | **FAIL** |

How I counted. A quoted block counts as one unit. Questions and pure transitions with no claim are left out. A sentence that holds except for one modern-only element, such as an editor's date, is marked for that element. The whole sentence counts as non-HELD.

Three patterns recur across the six pieces. The caller may want to rule on each as a class.

- **(a) Statements about the source base,** such as "nearly all we know of him comes from X" or "almost everything rests on this chapter". No old source makes these claims. They are judgments a modern editor makes about the record, so I mark them MODERN ONLY. Several also contradict the piece itself, which then quotes other old sources.
- **(b) Dates that come only from a modern editor,** such as the Benedictine or Fremantle date of a letter, or Kauffmann's 383. I mark these MODERN ONLY. A date the old text itself gives is HELD. Examples: Prosper's consular year, Epiphanius's regnal year, Sulpicius's "to the consulship of Stilicho", the Braga era date.
- **(c) Modern reception history,** meaning what 19th- and 20th-century editors and historians concluded. These are MODERN ONLY even when the piece names them as modern and reports them accurately. The rule bars telling them.

---

## P07: Ulfila

Census card: `ulfila` (movements[432]). Old texts used:
- Auxentius, *Epistula de fide, vita et obitu Wulfilae*, in `auxentius-durostorum_epistula-de-fide-vita-obitu-wulfilae_kauffmann1899.txt` (critical text from about line 15100; §§42–63)
- Philostorgius 2.5, in `philostorgius_ecclesiastical-history_walford1855.txt`
- Socrates 1.5, 2.41, 4.33, and Sozomen 6.37, in `npnf202_socrates-sozomen-ecclesiastical-histories.xml`
- Theodoret 4.33, in `npnf203_theodoret-jerome-gennadius-rufinus.xml`
- Streitberg 1908, in `wulfila_gothic-bible-v1-got_streitberg1908.txt`

The HELD sentences, in brief:
- The seven years, the martyrs, the crossing, and the reception under Constantius: Auxentius §59, "post multorum seruorum et ancillarum Cristi gloriosum martyrium … conpletis septem annis … cum grandi populo confessorum … in solo Romanie, athuc beate memorie Constantio principe, honorifice est susceptus".
- The Exodus quote: Auxentius §59, "sicuti deus per Moysem de potentia et uiolentia Faraonis … ita et per sepe dictum deus confessores sancti fili sui unigeniti de uarbarico liberauit et per Danubium transire fecit et in montibus secundum sanctorum imitationem sibi seruire". The rendering is faithful.
- Bishop at thirty: §56.
- The creed. The Father is "solum esse ingenitum, sine principio" (§42). The Son is "maiorem habentem deum et patrem suum" (§45) and "similem secundum scribturas" (§§48, 63). The homoousian profession is "ut diabolicam adinuentionem … spreuit et calcauit" (§45).
- The testament and the deathbed words, "Ego Ulfila episkopus et confessor semper sic credidi et in hac fide sola et uera transitum facio ad dominum meum … filium subditum et oboedientem suo in omnibus deo patri" (§63).
- The illness on entering Constantinople, "statim coepit infirmari" (§61).
- Philostorgius: ordained "by Eusebius and the other prelates that were with him", and "translated … all the books of holy Scripture, with the exception of the Books of Kings … the Gothic tribes were especially fond of war".
- Socrates 4.33: "invented the Gothic letters, and translating the Sacred Scriptures". Sozomen 6.37: "He taught them the use of letters, and translated the Sacred Scriptures".
- Socrates 4.33 on Fritigern and Valens, on Athanaric, and on the martyrs.
- Sozomen 6.37: "it is said, entered into disputations … they promised to lay his requests before the emperor … Compelled by the urgency of the occasion, or, possibly, thinking that it was better to hold such views".
- Theodoret 4.33: "Partly by the fascination of his eloquence and partly by the bribes … Eudoxius succeeded in inducing him".
- Arius: Socrates 1.5, "that which was begotten had a beginning of existence".

### Non-HELD sentences

1. **"His pupil Auxentius, who wrote in his praise and on whom nearly all of this life rests, told it as a new Exodus." MODERN ONLY (pattern a).** The pupil, the praise and the Exodus framing are HELD (§§55, 59). "On whom nearly all of this life rests" is the editor's verdict on the sources. Kauffmann makes it, and so does the census's Auxentius card ("the main record"). The piece itself goes on to rest half its account on Philostorgius, Socrates, Sozomen and Theodoret.

2. **"Those who confessed had held to the faith under persecution, and the barbarians' land was the Goths' country." SUMMARY HOLDS.** §58: "in uarbarico … ab inreligioso et sacrilogo iudice Gothorum … persecutio est excitata, ut … fierent martyres et confessores".

3. **"A modern historian takes this Eusebius for the bishop of Nicomedia." MODERN ONLY (pattern c).** Philostorgius says only "by Eusebius and the other prelates that were with him". Walford's notes do not name the see. Identifying the see is a modern act, which the piece admits.

4. **"Among the Goths, Auxentius says, Ulfila taught a people starved of preaching and made Christians into true Christians." SUMMARY HOLDS.** §57: "in fame et penuria predicationis indifferenter agentem ipsam gentem Gothorum … emendauit et uibere docuit et cristianos uere cristianos esse manifestauit et multiplicauit". "Made … into" slightly sharpens "manifestauit" ("showed to be"), but the force survives. The piece drops "indifferenter agentem" (living carelessly).

5. **"Fragments of a Gothic Bible survive without a translator's name, but their editor in 1908 had no doubt they were Ulfila's." MODERN ONLY (pattern c).** The report of the editor is accurate. Streitberg, p. [intro]: "Obwohl die Bruchstücke der gotischen Bibel ohne den Namen des Übersetzers auf uns gekommen sind, so kann es doch nicht zweifelhaft sein, daß wir in ihnen die Trümmer der Bibelübersetzung zu erkennen haben, die … Wulfila … unternommen hat." Even so, this is an identification only a modern editor makes.

6. **"The Greek for like, homoios, gives these churches the name Homoian." MODERN ONLY.** No old source calls Ulfila's church "Homoian". Auxentius names his opponents "Omousiani" and "Omoeusiani" (§§47, 49). For his own side he uses only "cristiani". The label is a modern scholarly classification, also used on the census card.

7. **"In 360, by the usual date, he joined the bishops at Constantinople in confirming a creed that banned the word 'substance' for God, saying Scripture never uses it." MODERN ONLY (pattern b, the date).** The creed's content and Ulfila's assent are HELD. Socrates 2.41 reads: "we have thought proper to reject it, as it is not contained even in the sacred writings … To this creed Ulfilas bishop of the Goths gave his assent". Socrates gives no year. "By the usual date" admits that the date is modern. Kauffmann supplies it: "was im jähre 360 zu Constantinopel geschehen ist".

8. **"It matters because the Goths still held that faith in the historians' day." SUMMARY HOLDS.** The "because" is the narrator's framing. It matches the historians' own reason for asking. Socrates 4.33 says "so many of the Goths are even to the present time infected with the errors of Arianism". Sozomen 6.37 speaks of "the Goths having retained, even to the present day, the tenets of Arianism".

9. **"But Sozomen says Ulfila was why the barbarians on the Danube followed Arius." SOFTENED OR CHANGED.** The piece sets this against Socrates ("Socrates puts it down to the emperor Valens … But Sozomen says…"), as if Sozomen gave a rival answer. Sozomen first tells the same Fritigern–Valens story, then adds: "It does not, however, appear to me that this is *the only reason* that can be advanced … For Ulphilas …" (6.37). He supplements Socrates and does not contradict him. The "But" changes what the source claims.

10. **"Socrates says Ulfila took the creed only in 360, holding Nicaea's faith before." ASSUMPTION ADDED (a date put in Socrates's mouth).** Socrates 2.41: "To this creed Ulfilas … gave his assent, although he had previously adhered to that of Nicæa; for he was a disciple of Theophilus". Socrates gives no year. "Only in 360" attributes a modern date to him.

11. **"Sozomen says he signed from thoughtlessness, and changed sides years later, under Valens, on an embassy seeking land for the Goths." SUMMARY HOLDS.** Sozomen 6.37: "though he took part, as I am convinced, from thoughtlessness, at the council of Constantinople … yet he did not swerve from the doctrines of the Nicæan council. He afterwards, it appears, returned to Constantinople". The embassy was for land in Thrace, under Valens. "Signed" compresses "took part". "Years later" is a fair reading of "afterwards", since the council was under Constantius and the embassy came after the Huns.

12. **"The chief took this as an attack on his ancestors' religion and punished the Christians, so that many died as martyrs." SUMMARY HOLDS.** Socrates 4.33: "regarding this as a violation of the privileges of the religion of his ancestors, subjected those who professed Christianity to severe punishments; so that many of the *Arian* Goths of that period became martyrs". The piece drops "Arian", a detail of some interest given the piece's subject.

13. **"Later the emperor ordered Ulfila to Constantinople for a debate, to stop his opponents teaching in his churches." SUMMARY HOLDS.** §61: "cum precepto inperiali … ad Constantinopolitanam urbem ad disputationem quidem contra Pneumatomacos perrexit … ne Cristi eclesias sibi a Cristo deditas docerent et infestarent". The purpose clause belongs to Ulfila's going, not to the emperor's order. The piece's syntax lets it read either way.

14. **"He died there, about 383." MODERN ONLY (pattern b).** Auxentius and Maximinus give no year. The census's own datesNote reads: "died at Constantinople in 383 (Kauffmann's dates, worked from Auxentius's numbers)".

**Heart.** The heart is right. It is Auxentius's own frame: a new Exodus over the Danube, a creed held to the deathbed, and the disputed question of when he became Homoian. It is the record's heart, not an imported one. The faults lie at the edges: the source-base claim, the modern dates and labels, and the way Sozomen is set against Socrates.

---

## P08: Epiphanius of Salamis

Census card: `epiphanius-of-salamis` (movements[431]). Old texts used:
- Panarion, in `epiphanius_ancoratus-panarion-haer-1-33-gcs-bd1-grc_holl1915.txt` (proem from about line 12372; ch. 1–2 about line 13368; haer. 33.3 about line 34004) and `epiphanius_panarion-haer-65-80-pg42-grc-lat_migne1863.txt` (haer. 77, line 48852)
- Letter 51 and *Against John of Jerusalem* 11, in `npnf206_jerome-principal-works.xml`, with Letter 66 for "my brother Paulinian"
- Socrates 6.7–12, and Sozomen 6.32, 8.14 and 8.15, in `npnf202_socrates-sozomen-ecclesiastical-histories.xml`
- Augustine, *De haeresibus*, praef., in `augustine_arian-sermon-collatio-maximinum-pl42-lat_migne1886.txt`
- Nicaea II, Session 6, with the Caroline Books notes, in `mendham_seventh-general-council-second-of-nicaea_1850.txt`

The HELD sentences, in brief:
- The proem quote: "μέλλομεν ὑμῖν τά τε ὀνόματα τῶν αἱρέσεων δηλοῦν τάς τε παρ᾽ αὐτοῖς ἀθεμίτους πράξεις ἀνακαλύπτειν, ὥσπερ ἰοὺς καὶ δηλητήρια ὄντα, σὺν αὐτοῖς δὲ ἅμα καὶ ἀντιδότους ἐφαρμόσαι, ἀλεξητήρια τῶν δεδηγμένων καὶ προκαταληπτικὰ τῶν μελλόντων εἰς τοῦτο ἐμπίπτειν". The book is "Πανάριον εἴτ᾽ οὖν κιβώτιον ἰατρικὸν", holding "αἱρέσεις ὀγδοήκοντα", and after the eighty comes "Χριστοῦ νύμφη ἁγία ἐκκλησία, οὖσα μὲν ἀπ᾽ αἰῶνος". The rendering is faithful.
- Sources from books, hearsay and his own eyes and ears: Pan. 2, "τὰ μὲν ἐκ φιλομαθίας ἴσμεν, τὰ δὲ ἐξ ἀκοῆς κατειλήφαμεν, τοῖς δέ τισιν ἰδίοις ὠσὶ καὶ ὀφθαλμοῖς παρετύχομεν".
- Ptolemy's letter: "ἵνα μή τις νομίσειεν ἡμᾶς ἐξ ἀκοῆς μόνον τὸν ἀπατεῶνα ἐλέγχειν" (33.2).
- Apollinaris: "ὁ ἀεὶ ἡμῖν ἀγαπητὸς" (77.2).
- Sozomen 6.32 on Besanduc near Eleutheropolis, "chosen by the inhabitants of Cyprus", "metropolis … a seaport".
- *Against John* 11: "the 'silly old man'", and "kissing his feet".
- Letter 51: the souls as angels; the denial of the resurrection of this flesh; the allegorised paradise; "I have drunk also from the great river Euphrates, not spiritual but actual water"; Paulinian "had several times fled from you"; "I gave orders to a number of deacons to seize him and to stop his mouth"; "crying out that he was unworthy"; the curtain "bore an image either of Christ or of one of the saints … I tore it asunder … that curtains of the other sort … shall not be hung up".
- Sozomen 8.14–15: the Theophilus letter, "formerly blamed him for asserting that God possessed a human form", the Cyprus synod, "nor pray with him publicly, unless…", the Long Brothers' question, "formed his judgment by the reports he had heard", and "he died while on his voyage back to Cyprus".
- Augustine: "ordinem sum secutus … separatis viginti, quas ante Domini adventum … reliquas … sexaginta".
- Nicaea II: "a passage attributed to Saint Epiphanius which is none of his: for the same divine father, having made a treatise of eighty chapters … had he therefore considered the making of images to have been against the mind of Christ, he no doubt would have placed that also in his catalogue of heresies". The Caroline Books then cite the Anablatha curtain letter.

### Non-HELD sentences

1. **"A heresy, in his book, is a teaching the church judged false." SOFTENED OR CHANGED.** The gloss does not fit Epiphanius's own category. His eighty "heresies" begin with Barbarism, Scythism, Hellenism and Judaism, and include the Greek philosophical schools. Augustine reports twenty "quas ante Domini adventum exstitisse … computavit". Epiphanius frames the list as "πίστιν τε καὶ ἀπιστίαν, εὐδοξίαν τε καὶ ἑτεροδοξίαν … ἐξότε ἄνθρωπος ἐπὶ γῆς πέπλασται" (Pan. 1–2). The judging is also his, not "the church's".

2. **"Later writers, from Augustine to a council at Nicaea four centuries on, took his book as their list." SUMMARY HOLDS.** Augustine follows his order. Nicaea II argues from his catalogue.

3. **"In old age he carried the same fight to Jerusalem and Constantinople, against the followers of Origen, a Christian teacher who had died long before." SUMMARY HOLDS.** "Silly old man" comes from *Against John* 11. Socrates 6.10 says Origen "had been dead nearly two hundred years". Letter 51 itself ties Origen to "the other eighty heresies".

4. **"He wrote the Panarion about 375, by his own dating." SUMMARY HOLDS.** Pan. 2: "βασιλείας Οὐαλεντινιανοῦ καὶ Οὐάλεντος ἑνδεκάτου ἔτους καὶ Γρατιανοῦ ἑβδόμου". The conversion to a year is arithmetic on his own date.

5. **"Each chapter names a heresy, tells its teaching and answers it." SUMMARY HOLDS** against the proem, which promises names, deeds and antidotes. One note for the record: Augustine read Epiphanius (or his summary) differently, as "historica narratione memorans omnia, nulla disputatione adversus falsitatem pro veritate decertans" (*De haer.* praef.). The piece's claim stands on Epiphanius's own text.

6. **"In the 390s he preached against Origen in the church at Jerusalem." MODERN ONLY (pattern b, the date).** *Against John* 11 ("We were present … when the bishop Epiphanius spoke against Origen in your church") and Letter 51 give no year. The decade comes from Fremantle's chronology. The rest of the sentence is HELD.

7. **"In a letter to that bishop Epiphanius says why." SUMMARY HOLDS.** Letter 51 §§3–5 sets out his case against Origen.

8. **"Epiphanius held to the plain sense." SUMMARY HOLDS.** Letter 51 §5: "He does not say 'went down from Eden' … I myself have seen the waters of Gihon".

9. **"If the rivers were real, so was Eden." SUMMARY HOLDS.** Letter 51: "if the water is visible and real, then the fig-tree and the rest of the timber must be real also".

10. **"The same letter defends two acts of force." SUMMARY HOLDS.** These are the ordination of Paulinian (§§1–2) and the torn curtain (§9).

11. **"The historian Socrates says Theophilus wanted revenge on monks he had driven out of Egypt, the Long Brothers, and used a man of simple mind and manners." SUMMARY HOLDS.** Socrates 6.10: "not having this as his first object, but rather his purpose of revenge on Dioscorus and his brethren … Epiphanius being on account of his extraordinary piety a man of simple mind and manners". Socrates 6.7 has "the Tall Monks", who "made their escape with great difficulty". "Long Brothers" is Sozomen's name for them.

12. **"There he ordained a deacon in the territory of its bishop, John Chrysostom, against church rules." MODERN ONLY.** Socrates 6.12 reads only: "after having ordained a deacon, he again entered the city". The phrase "against church rules" comes from the NPNF editor's note: "It was contrary to the canons of the church for a bishop to ordain … in another's diocese. Cf. Apostol. Can. 35". Socrates's chapter heading says "without John's Permission". It does not say the act was against the canons.

13. **"Four centuries on, both sides in the quarrel over holy images claimed him." SUMMARY HOLDS.** The iconoclast florilegium cites "the far-famed Epiphanius", and Hadrian cites his "exposition" of the Canticles (Mendham, Session 6 and p. ~118 note).

14. **"A reply written at Charlemagne's order answered with his own curtain letter." MODERN ONLY (in part).** The curtain-letter reply is HELD: the Caroline Books, lib. iv c. 25, as given in Mendham's note, quote Letter 51. "At Charlemagne's order" rests in this corpus only on Mendham's 1850 title page: "compiled by order of Charlemagne for its confutation". The Caroline Books' own preface is not vendored.

**Heart.** The heart is right. It is the medicine chest of antidotes, carried in old age into a campaign against a long-dead teacher, and it closes on the church as the cure. The piece's spine is Epiphanius's own image, and the anti-Origen campaign is what the record most fully attests. The gloss on "heresy" (item 1) cuts against that heart, because the list is Epiphanius's own world-history of error, not a church register.

---

## P09: The Catholic Church of the Ancien Régime (movement)

Census card: `catholic-church-ancien-regime` (movements[189]). The first paragraph of the piece is almost word for word the card's `longDescription`. Old texts used:
- `clement-xiv_bulls-suppression-and-restoration-of-the-jesuits-lat-eng_1814.txt`
- `clement-xi_unigenitus-lat-eng_1713.txt`
- `pius-vi_bref-sur-la-constitution-civile-du-clerge-fra_1791.txt`
- `baldassari_enlevement-et-captivite-de-pie-vi-fra_1839.txt` and `merck_captivite-et-mort-de-pie-vi-fra_1814.txt`
- `wiseman_recollections-of-the-last-four-popes_1858.txt` (a near-contemporary witness of Pius VII)
- `mercati_raccolta-di-concordati-ita-fra-lat_1919.txt` (the 1801 concordat text)
- `propaganda-fide_collectanea-decreta-instructiones-rescripta-v1-lat_1907.txt`

The HELD sentences, in brief:
- The bull: "the Kings of France, Spain, Portugal, and Sicily, found themselves reduced to the necessity of expelling and driving from their states … these very companions of Jesus".
- The suppression dated 1773; the 1801 concordat, "Concordato fra Pio VII e la Repubblica francese, 15 luglio 1801"; the 1814 restoration in *Sollicitudo*.
- Pius VI's death as a prisoner at Valence in 1799 (Baldassari; Merck, governor of the citadel).
- Captivity to 1814: Wiseman, "The decree of Napoleon of Feb. 10, 1814, which released the Pope from captivity".
- Collectanea no. 126 (23 March 1656): "proposita fuerunt, anno 1645, Sacrae Congregationi de Propaganda Fide … quaesita". On the Confucius hall: "censuit permittendas sinensibus christianis praenomatas caeremonias, quia videtur cultus esse mere civilis et politicus".
- The 1659 Instruction: "Quid enim absurdius quam Galliam, Hispaniam, aut Italiam … in Sinas invehere?"
- No. 307 (4 Oct. 1726): "Omnes etiam presbyteros indigenas, sinenses, cocincinenses, tunquinenses etc. teneri emittere iuramentum praescriptum in Const. Ex illa die". The oath formula is quoted in *Ex quo singulari*: "Praecepto ac Mandato Apostolico super ritibus et caeremoniis sinensibus … plene ac fideliter parebo … et absque ulla tergiversatione adimplebo".

### Non-HELD sentences

1. **"This was the Catholic Church at the height of its establishment and on the edge of its worst crisis: enormously wealthy, woven into the monarchies of Europe, and increasingly unable to control them." MODERN ONLY.** This is a historian's overview judgment, taken from the census card. No vendored old text makes it.

2. **"Rome's condemnation of Jansenism in the bull Unigenitus (1713) turned into a fifty-year political crisis in France." MODERN ONLY (the second half).** "Condemnation of Jansenism" is a fair summary of the bull: "notoriously reviving several Heresies, and chiefly those which are contained in the infamous Propositions of Jansenius". The "fifty-year political crisis" rests only on the census card and the vendoring content note ("the act that set off the half-century crisis"). No parlement record or Jansenist source in the corpus is used to support it.

3. **"His bull names quarrels, riots, charges against Jesuit teaching, and greed for property." SUMMARY HOLDS.** The bull: "very violent disputes arose on all sides, concerning the doctrine of the society … that insatiable avidity of temporal possessions"; "dangerous seditions arose, tumults, discords". "Riots" is fair for "seditions … tumults".

4. **"The kings, it says, wished to stop Christians rising against one another." SUMMARY HOLDS.** The bull: "persuaded that there remained no other remedy … and that this step was necessary in order to prevent the Christians from rising one against another, and from massacreing each other".

5. **"Then came the Revolution: church property nationalized, thousands killed or driven abroad, and Pope Pius VI carried off to die a French prisoner in 1799." SUMMARY HOLDS.** Pius VI's brief: "l'invasion des biens ecclésiastiques". Baldassari: "les massacres de l'Abbaye et des Carmes … plus de deux mille ecclésiastiques français … obligés de se réfugier dans les Etats pontificaux". Wiseman: priesthood and religion "annulled by death, confiscation". Merck and Baldassari cover the captivity and the death at Valence.

6. **"In 1809 Napoleon annexed the Papal States, saying that spiritual power joined to rule over land had bred quarrels." NOT FOUND.** I searched for the Schönbrunn/Vienna decree of 17 May 1809 ("17 mai 1809", "Schœnbrunn", "Charlemagne … prédécesseur", "pouvoir temporel", "puissance temporelle") across `cic/texts/`. Launay (t. 2, about line 37806) has only a September 1809 Schönbrunn decree dissolving the Missions-Étrangères. Wiseman mentions the "Departments of Rome and of Thrasymene" but not Napoleon's reasoning. The decree's wording is not vendored.

7. **"The pope outlived him and restored the Jesuits that year." NOT FOUND (the first half).** The restoration of 1814 is HELD (*Sollicitudo*). Nothing in the corpus says that Pius VII outlived Napoleon. It is true (1823 against 1821), but I found no vendored source for it.

8. **"Rome ran its missions through Propaganda, the congregation for spreading the faith." SUMMARY HOLDS.** The Collectanea opens with Gregory XV's *Inscrutabili* (1622) and is the Congregation's own record.

9. **"Its collected decrees show three acts in these years." SUMMARY HOLDS** (framing).

10. **"Converts could also keep rites for their dead, once anything superstitious was removed." SUMMARY HOLDS.** "censuit, posse tolerari sinenses conversos adhibere dictas caeremonias erga suos defunctos etiam cum gentilibus, sublatis tamen superstitiosis". "Could keep" is a little stronger than "could be tolerated", but the meaning holds.

11. **"They were not to urge any people to change its rites, customs and ways." SOFTENED OR CHANGED.** The Instruction makes the ban conditional: "nullaque ratione suadete illis populis ut ritus suos, consuetudines et mores mutent, *modo non sint apertissime Religioni et bonis moribus contraria*", that is, unless they are plainly contrary to religion and good morals. The piece drops the condition and makes the rule absolute. That changes what Rome ordered.

12. **"That text seemed to name only Europeans." SUMMARY HOLDS.** It is the question's stated reason: "La ragione di muovere questo dubbio si è che in detta Costituzione pare non vengano indicati che i soli missionari europei."

**Heart.** The heart is doubtful. The census voices are Clement XI, Clement XIV, Pius VI, Pius VII and Liguori. The card's "why" is Unigenitus, the suppression, the Revolution and the concordat. The piece gives that whole arc a single paragraph, which is copied from the census and only partly sourced. Two thirds of the piece then go to three Propaganda decrees on Chinese rites. Those decrees are well sourced, but they sit at the edge of this subject. The first and best-documented decree, from 1656, is also earlier than the movement's own anchor (Unigenitus). And the 1659 ban is quoted without its condition.

---

## P10: Priscillian

Census card: `priscillian` (movements[458]). Old texts used:
- Tractate II (*Liber ad Damasum*), in `priscillian_quae-supersunt-lat_schepss1889-csel18.txt` (from line 4326)
- Sulpicius, *Chronicle* 2.46–51, in English (`npnf211_sulpitius-severus-vincent-lerins-cassian.xml`) and Latin (`sulpicius-severus_libri-qui-supersunt-chronica-vita-martini-lat_halm1866-csel1.txt`)
- Prosper, *Chronicle*, nos. 1187 and 1193, in `prosper_chronica-minora-1-lat_mommsen1892.txt`
- Hydatius, nos. 13 and 16, in `chronica-minora-2_…mommsen1894.txt`
- Toledo I, in `mansi_sacrorum-conciliorum-collectio-tomus-3-…txt` (about line 96778)
- Leo, Letter 15, in `npnf212_leo-great-gregory-great.xml`
- Braga I, in `bruns_canones-…-pars-altera-lat_1839.txt`

The HELD sentences, in brief:
- The book handed in: "qui libellum tradidimus".
- The quote: "semper hoc in eclesiis et admonuimus et admonemus … nec prohibere si quis contemptis parentibus liberis facultatibus dignitate et adhuc et anima sua deum malluerit amare quam saeculum". The rendering is faithful.
- Saragossa, in his own words: "nemo e nostris reus factus tenetur, nemo accusatus … nemo damnatus est … tua potissimum epistula … ne quid in absentes et inauditos decerneretur".
- "in causa fidei sanctorum iudicium malle quam saeculi".
- Sulpicius: noble birth and riches, the vigils, the fasting, "little desire for amassing wealth", "believed that he had practised magical arts from his boyhood", "infamous heresy of the Gnostics … arcanis occultata secretis", "Ydacius … harassing … without measure … applied … a torch", condemned in absence as a layman at Saragossa, made bishop "in Abilensi oppido", Gratian's rescript, Damasus and Ambrose, Maximus from Britain at Trier, the appeal at Bordeaux "ut … ab episcopis audiri", Ithacius on reading and fasting, Martin's plea, "quoad usque Martinus Treveris fuit, dilata cognitio est", "gemino iudicio auditum conuictumque maleficii", the emperor's sentence, the martyr cult, the funerals and oaths, and Ithacius "solus … omnium episcopatu detrusus".
- "My own view is that the accused displease me as much as the accusers."
- Prosper: "a. 385 … Maximi gladio addictus est". This supports "about 385" and "by the sword".
- Toledo I: "Priscillianum catholicum, sanctumque martyrem clamassent".
- Leo: "the leaders of the world so abhorred this profane folly that they laid low its originator, with most of his disciples, by the sword of the public laws".
- Braga: "habitum aera DXCIX" (AD 561), "Priscilliani erroris figmenta damnentur".

### Non-HELD sentences

1. **"A rich and learned layman of Spain, Priscillian called men and women to that strict life, and became bishop of Abila." SUMMARY HOLDS.** Sulpicius 2.46–47, with the strict life from Tract. II.

2. **"Nearly all we know of him comes from Sulpicius Severus, a writer from Gaul, writing some years after the deaths." MODERN ONLY (pattern a).** This is Schepss's judgment in his preface: "totum de eo iudicium ab eius inimicis penderet, in quibus maximam Sulpicio Seuero concedebant auctoritatem". The piece contradicts it at once by quoting Priscillian's own book and by citing Prosper, Toledo, Leo and Braga.

3. **"In his own account, Priscillian and his friends gave themselves wholly to God after baptism, because Scripture says that whoever loves anyone more than God cannot be his disciple." SUMMARY HOLDS.** "totos nos dedissemus deo, legentes quod qui quemquam amplius quam deum diligeret discipulus eius esse non posset". "Because" stands for "legentes" (reading that). That is fair.

4. **"The same book gives his creed and curses every heresy, the followers of the Persian teacher Mani above all." SUMMARY HOLDS.** "omnes hereses … catholico ore damnamus … inter quae tamen omnia Manicaeos, iam non hereticos, sed idololatras et maleficos … damnamus". "Persian teacher" is the narrator's gloss and is not in Priscillian. Read as a clarification it holds, but it is not sourced here.

5. **"Sulpicius says Priscillian did not deny studying obscene teachings, holding night meetings of women, and praying naked." SUMMARY HOLDS, slightly softened.** Sulpicius has "nocturnos etiam *turpium* feminarum egisse conuentus", gatherings of shameful women. The piece drops "turpium". The softening runs in Priscillian's favour, but the charge as reported is muted.

6. **"These are the court's findings; no account from his side survives." SUMMARY HOLDS** as an honest limit. Sulpicius frames these as what the prefect found, and no record of the trial from Priscillian's side exists in the corpus.

7. **"Priscillian was killed by the sword with several companions, among them a woman who had sheltered them." SUMMARY HOLDS.** Sulpicius 2.51: "Latronianus quoque et Euchrotia gladio perempti". Sulpicius 2.48: "lingering for a little while in the territory of Euchrotia" (in agro Euchrotiae). "Sheltered" is a fair reading.

8. **"The deaths split the other side." / "Its bishops above all quarreled for fifteen years…".** The second sentence is HELD against the Latin. The first I mark **SUMMARY HOLDS**. Halm's Latin reads "at inter nostros perpetuum discordiarum bellum exarserat, quod iam per quindecim annos foedis dissensionibus agitatum … cum maxime discordiis episcoporum omnia turbari". NPNF mistranslates this as "between them and our friends". The piece follows the Latin correctly.

9. **"Yet sixty years on, Leo, bishop of Rome, wrote to Spain against the Priscillianists, and praised the killing." SUMMARY HOLDS.** The letter is dated "in the consulship of the illustrious Calipius and Ardaburis (447)". Leo: "this rigourous treatment was for long a help to the Church's law of gentleness".

10. **"For centuries Priscillian was known only through his enemies." MODERN ONLY (pattern a).** This is Schepss's preface, quoted in item 2.

11. **"In 1885, a scholar opened an old manuscript at Würzburg and found eleven unsigned treatises." MODERN ONLY (pattern c).** Schepss, praef.: "autumno anni 1885 in codicem saec. V uel VI inciderem, qui … undecim tractatus continet. Nam etsi Priscilliani nomen in codice … nusquam apparet".

12. **"He judged they could be no one's but Priscillian's." MODERN ONLY.** This is an identification made only by the modern editor: "mox mihi et aliis persuasi fieri non posse, quin alii auctori quam Priscilliano illi tractatus tribuerentur".

13. **"Among them was the book Priscillian had carried to Damasus, with his call in his own words again." MODERN ONLY.** It rests on the identification in item 12.

**Caveat for the caller.** Every "Priscillian wrote" sentence in the body depends on Schepss's attribution. The census lists the tractates as `ownWords`. The internal evidence is strong: Tract. II names Damasus, Hydatius, Saragossa, Hyginus, Symposius and Ambrose, and speaks for the group that handed in the *libellus*. So I have marked those sentences HELD as the text of the *Liber ad Damasum*. Read strictly, the rule would make all of them MODERN ONLY. That needs a ruling.

**Heart.** The heart is right, and the piece is strong. It opens and closes on his own call to choose God over family, wealth and rank. It then tells the case through the hostile record and the fact that Sulpicius disapproved of both sides. This is the right heart for a man known almost only through his judges. The trouble is that the piece says so itself, in modern-only sentences.

---

## P11: Jerome

Census card: `jerome` (movements[337]). Old texts used:
- From `npnf206_jerome-principal-works.xml`: Letter 125 §12; Letters 39, 45, 51 and 108; the preface to the Gospels
- From `npnf203_theodoret-jerome-gennadius-rufinus.xml`: *Apology against Rufinus* 3.22, and Rufinus, *Apology* 2.32
- From `npnf101_augustine-confessions-letters.xml`: Letters 28, 71, 75, 82 and 195
- `palladius_lausiac-history_clarke1918.txt`
- `prosper_chronica-minora-1-lat_mommsen1892.txt` (no. 1274)
- `isidore-seville_etymologiae-origines-lat_lindsay1911.txt` (6.4.5)
- `denzinger_enchiridion-symbolorum-lat_bannwart1911.txt` (no. 785)

The HELD sentences, in brief:
- Letter 125: "I betook myself to a brother who before his conversion had been a Jew and asked him to teach me Hebrew … I began to learn my letters anew and to study to pronounce words both harsh and guttural … from this seed of learning sown in bitterness I now cull sweet fruits".
- Augustine 71: "the Latin one taken from it".
- The Gospel preface: "almost as many forms of texts as there are copies".
- Letter 45: "I found myself surrounded with virgins, and to some of these I expounded the divine books … They believed my accuser when he lied; why do they not believe him when he retracts?"
- Letter 39: "She weeps for her daughter, killed with fasting … hurl them into the Tiber".
- *Against Rufinus* 3.22: "In the month of August … I went on board ship … choosing my own time".
- Letter 108: "a monastery for men … three companies and monasteries" of virgins; "would force me by fresh questions"; Paula learned Hebrew.
- Rufinus 2.32: "making a new translation under the influence of the Jews … Who but you would have laid hands upon the divine gift and the inheritance of the Apostles?"
- Augustine 71 on Oea, and the "ignorance or … spite" of the Jews.
- Letter 75: "the Hebrew Ms. has 'ciceion' … I therefore put down 'ivy'".
- Letter 82: "my only reason for objecting to the public reading of your translation from the Hebrew in our churches"; "neither 'gourd' nor 'ivy'".
- Letter 195: "Catholics revere and look up to you as the restorer of the ancient faith".
- Prosper, under 420: "Hieronimus presbyter moritur anno aetatis suae XCI prid. kal. Octobris".
- Isidore: "Cuius interpretatio merito ceteris antefertur".
- Trent: "haec ipsa vetus et vulgata editio … pro authentica habeatur, et ut nemo illam reicere … audeat".

### Non-HELD sentences

1. **"Jerome was a young man in the desert when fasting failed to quiet his restless mind." SOFTENED OR CHANGED.** Letter 125 §12: "I was still unable to endure the promptings of sin and the natural heat of my blood; and, although I tried by frequent fasts to break the force of both, my mind still surged with [evil] thoughts". "Restless mind" removes what the source names, sin and the heat of the blood. That is the reason Jerome gives for taking up Hebrew at all.

2. **"Years later he wrote of what it cost a scholar fresh from Rome's great Latin writers." SUMMARY HOLDS.** The letter names "Quintilian … Cicero … Fronto … Pliny".

3. **"In time it became the Western church's standard text." SUMMARY HOLDS** via Isidore ("merito ceteris antefertur") and Trent.

4. **"In the 380s Damasus, the bishop of Rome, urged him to correct the Latin Gospels the churches already had against the Greek." SUMMARY HOLDS.** The preface reads "You urge me to revise the old Latin version … which of them agree with the Greek original". The decade is anchored by Damasus's pontificate, which ended in 384. It is not a free modern date.

5. **"Most of what we know of Jerome, and of the women around him, comes from his own letters." MODERN ONLY (pattern a).** It is a judgment about the source base.

6. **"Then Rome turned on him." SUMMARY HOLDS.** Letter 45 §§2–3: "Before I became acquainted with the family of the saintly Paula, all Rome resounded with my praises…"

7. **"Palladius, a monk on his opponents' side, charged instead that Jerome held her back by his jealousy." SUMMARY HOLDS.** Lausiac History 41.2: "She was hindered by a certain Jerome from Dalmatia … he hindered her by his jealousy". Palladius's hostility shows in his own text (36.6–7). The phrase "on his opponents' side" is Clarke's note (292.4), but the text bears it out.

8. **"From about 391 he addressed many prefaces to Paula and her daughter." MODERN ONLY (pattern b).** The date comes from Fremantle's chronology. The prefaces carry no year.

9. **"Augustine, a bishop in Africa, begged him not to translate the Scriptures afresh unless he marked where he differed from the old Greek, which Augustine held in the highest esteem." SUMMARY HOLDS.** Letter 28: "I beseech you not to devote your labour to the work of translating into Latin the sacred canonical books, unless you follow the method in which you have translated Job … that of the LXX., whose authority is worthy of highest esteem." A small note: in Letter 28 Augustine was still a priest; he speaks of Alypius as "now invested with the office of bishop".

10. **"Rufinus of Aquileia, once Jerome's close friend, had fallen out with him over Origen, a Greek scholar whose ideas were under attack." SUMMARY HOLDS.**

11. **"In 400 Rufinus wrote against him." MODERN ONLY (pattern b).** The *Apology*'s year comes from the editor, Fremantle.

12. **"In 403 Augustine told Jerome how a bishop at Oea had Jerome's Jonah read in church." MODERN ONLY (pattern b, the year).** The content is HELD (Letter 71 §5). The year 403 is the editors' date for the letter.

13. **"Yet in 418 Jerome wrote that Catholics revered Augustine as the restorer of the ancient faith." MODERN ONLY (pattern b, the year).** The content is HELD (Letter 195). "418" is the NPNF heading, "(a.d. 418.)", an editor's date.

14. **"The decree does not name Jerome, but the version the council chose was his." MODERN ONLY.** The first clause is correct (Denzinger 785). Equating the "vetus et vulgata editio" with Jerome's version is not in the decree or in any vendored old text. Isidore attests only that Jerome's version was preferred. The flat "was his" also overstates. Parts of the Vulgate are not Jerome's, and an honest phrasing would need to say so.

15. **"About 411 he wrote of that first hard lesson in Hebrew: 'But I thank the Lord…'" MODERN ONLY (pattern b, the year).** The quote is HELD (Letter 125 §12). "About 411" is the editor's date for the letter.

**Heart.** The heart is right. It is the bitter seed and the sweet fruit: a man who learned Hebrew against his own training, a version fought over by Rufinus and Augustine, and a version that won. This matches the census card's "knownFor". The one change of substance is item 1. Without the struggle with sin, the opening loses the force Jerome himself gives his reason for learning Hebrew. The rest of the failures are editors' dates.

---

## P12: Tacitus

Census card: `tacitus` (movements[408]). Old texts used:
- Annals 15.44, in `tacitus_annals-15-44_church-brodribb1876.txt` (one chapter only)
- Tertullian, *Apology* 16 and *To the Nations* 1.11, in `anf03_tertullian.xml`
- Sulpicius, *Sacred History* 2.29, in `npnf211_…xml`

The HELD sentences, in brief:
- Tacitus: the nightly illumination, the skins, dogs and crosses, Nero in the dress of a charioteer, "criminals who deserved extreme and exemplary punishment", "Christus … suffered the extreme penalty during the reign of Tiberius at the hands of one of our procurators, Pontius Pilatus", "a most mischievous superstition", "hated for their abominations", "did not banish the sinister belief that the conflagration was the result of an order", "an arrest was first made of all who pleaded guilty; then, upon their information, an immense multitude was convicted, not so much of the crime of firing the city, as of hatred against mankind", "exhibiting a show in the circus", and the closing judgment of pity.
- Tertullian: "Cornelius Tacitus first put this notion into people's minds … as Christianity is nearly allied to Judaism, from this, I suppose, it was taken for granted that we too are devoted to the worship of the same image … the very opposite of tacit in telling lies … Cneius Pompeius … found no image there"; also "most loquacious in falsehood" (*Ad Nat.*).
- Sulpicius 2.29: "the most cruel tortures were accordingly inflicted upon the innocent … covered in the skins of wild beasts … devoured by dogs, while many were crucified or slain by fire … to serve for light during the night". Sulpicius dates his own work by counting "down to the time of Stilico" (2.9). This supports "about 400".

### Non-HELD sentences

1. **"Writing about fifty years after the great fire of Rome in 64, Tacitus gives the fullest account outside the church of what Nero did to the Christians." MODERN ONLY.** The year 64 is not in the vendored chapter. The file warns that "the rest of Tacitus is NOT in this corpus", and the date of the fire is in Annals 15.38. The year appears only in modern notes: McGiffert, and the vendoring header's "Written c. 116 CE". "The fullest account outside the church" is a modern comparative judgment.

2. **"Yet his one chapter became what later historians built on." MODERN ONLY (pattern c).**

3. **"Tacitus stops to explain the name, and gives Christ in its Latin form." SUMMARY HOLDS.**

4. **"Historians a century ago read that to mean the inquiry proved them Christians, not that they set the fire." MODERN ONLY (pattern c).** This is an explicitly modern reading, taken from Schanz–Hosius–Krüger or Duchesne.

5. **"Almost everything known of these deaths rests on this one chapter, and Tacitus never says where he learned of Christus." MODERN ONLY (pattern a, the first clause).** The second clause is true of the chapter. The first is a judgment about the source base, and the piece's own Sulpicius paragraph partly undercuts it.

6. **"About the year 200, Tertullian, defending the Christians, answered him by name over another of his histories." MODERN ONLY (pattern b, the date).** The rest is HELD (*Apology* 16). "About 200" is a modern dating of the *Apology*.

7. **"Later historians made the chapter their main outside record of these deaths, and a Roman's witness that Christus was put to death under Pilate." MODERN ONLY (pattern c).**

8. **"In an 1876 debate, a speaker arguing that the Bible was not divine said the passage was open to challenge." MODERN ONLY (pattern c).** It accurately reports Bradlaugh 1876: "the quotation from Tacitus is liable to impeachment". It is still 19th-century reception.

9. **"The historians who weighed it treated it as Tacitus's own." MODERN ONLY (pattern c).**

10. **"In 1890, a translator of Eusebius's history of the early church rejected the view of some historians that the victims were Jews, not Christians." MODERN ONLY (pattern c).** McGiffert's note.

11. **"Back in the gardens at night, Tacitus ends with his own judgment." SUMMARY HOLDS** (framing).

**Heart.** The heart is right, but the telling breaks the rule. Tacitus suits this subject well: a contemptuous Roman witness who names Christus under Pilate and ends in pity despite himself. Tertullian and Sulpicius answer him, and those two sources carry the piece well. Four of its eleven paragraphs, though, are modern reception (the 1876 debate, "the historians who weighed it", McGiffert in 1890, and "historians a century ago"). The rule bars telling these, however accurately they are reported. With the reception paragraphs and the modern dates cut, the piece would come close to passing.
