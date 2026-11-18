# Source sheet: Moses the Black

All paths are under `cic/texts/`. Line numbers are the file's own. Quotes are verbatim from the file, OCR errors included where the file has them. In NIK quotes, the file's runs of two spaces are shown as one, and line-end hyphen breaks are joined. Confidence uses the project's five levels. Where a claim is "the source says X", the level grades the report; a second level, where given, grades the event itself.

Short names used below:
- **LH** = `palladius_lausiac-history_clarke1918.txt` (Palladius, Lausiac History, English of W. K. Lowther Clarke, 1918, from Butler's Greek).
- **PAR1** = `palladius_paradise-v1-syriac_budge1907.txt` (Budge, Syriac Paradise vol. I; Book I only).
- **PAR2** = `anan-isho_paradise-v2-sayings_budge1907.txt` (Budge, Syriac Paradise vol. II, the sayings, 'Anan-Isho's Syriac recension).
- **SOZ** = `npnf202_socrates-sozomen-ecclesiastical-histories.xml` (Sozomen, Church History, NPNF).
- **CAS** = `npnf211_sulpitius-severus-vincent-lerins-cassian.xml` (Cassian, NPNF, tr. Gibson).
- **ESX-M** = `ethiopian-synaxarium_book-of-saints-ethiopian-church-v2-v4-microform_budge1928.txt`; **ESX-1** = `...-v1-maskaram-khedar_budge1928.txt`; **ESX-2** = `...-v2-takhshash-yakatit_budge1928.txt`.
- **NIK** = `nikodemos-hagiorite_synaxaristes-vol2-mar-aug-grc_1900.txt` (Greek Synaxaristes, Nikodemos the Hagiorite; OCR heavily garbled).
- **TOM** = `thomas-of-marga_book-of-governors-v2-english_budge1893.txt` (Budge's 1893 description of a Syriac Paradise manuscript).

## Witnesses and their kind

| Witness | Kind | Gap |
|---|---|---|
| Palladius, LH 19 | Later, near-contemporary. Palladius lived among the Egyptian monks from 388 and spent fifteen days at Scete; he does not say he met Moses. Much of the robber past is report ("they used to say"). | Written 419–420 (LH 657, editor's note 13: "I.e. 419-420", on LH 185). Moses's own dates are not given. |
| Sozomen VI.29 | Later; retells the same story in the same order, so likely dependent, not independent. | Begun about 443 (SOZ 22477, editor's introduction). |
| Syriac sayings, PAR2 | Later collection. 7th-century Syriac compiler ('Anan-Isho', file header lines 5–6) of older material. Wording and numbering differ from the Greek. | Two to three centuries to the compiler; the oral sayings are older. |
| Ethiopian Synaxarium | Late legend. Ge'ez calendar of saints, "translated into Ethiopic from Arabic" (ESX-1 header, Creator line). File content note: "Late medieval memory; retrospection flags required" (ESX-M header). | Roughly a thousand years. |
| Nikodemos, Synaxaristes | Late; Greek calendar, 1868 edition reprinted 1900; Nikodemos died 1809 (NIK header). Follows Palladius closely. | About fourteen centuries. |

The Greek text of the Lausiac History is not held (only Clarke's English). The Syriac Palladius chapter on Moses is **not held**: PAR1 prints Book I only (PAR1 header lines 23–29, "only BOOK I's text is printed here"), and Moses is in Book II. The Greek alphabetical sayings are not held. The Coptic (Arabic Jacobite) Synaxary entry for his day is not held: the Patrologia Orientalis volumes in the Library cover Thout–Babeh, Toubeh–Amshir and Barmahat–Bashons, not Ba'unah.

## Setting

| # | Claim | Source | Conf. | Verbatim |
|---|---|---|---|---|
| S1 | He lived and died at Scete, in the Egyptian desert. | LH 337 | Documented | "So he died in Scete seventy-five years old, having become a priest; and he left seventy disciples." |
| S2 | His robber life was by the Nile. | LH 333 | Documented (as report) | "he was informed that it was on the opposite bank of the Nile. And, since the river was in flood and about a mile in extent" |
| S3 | Palladius first came to Alexandria in 388. | LH 197; note LH 713 | Documented | "THE first time that I set foot in the city of the Alexandrians, in the second consulate of the great Emperor Theodosius" / note: "I. e. 388." |
| S4 | Palladius himself visited the old men of Scete. | LH 361 | Documented | "I journeyed secretly into the great desert and spent fifteen days in meeting the fathers who had grown old in the desert at Scete." |
| S5 | No year of birth or death is held. A spoken "around 400" or "the late 300s" is the researcher's inference from S3 and the 419–420 date. | — | Inferential-Thin | — |
| S6 | Tradition (census `toldWithin` desert-monasticism): spoken name "the desert", informal "Desert Fathers and Mothers"; "Abba" is the honoured address for a proven elder, not an office. | `cic-website/data/world-census.json`, entry desert-monasticism | — | "'Abba and Amma', kind own: 'Honored address for proven elders, men and women; not an office.'" |

## Who he was

| # | Claim | Source | Conf. | Verbatim |
|---|---|---|---|---|
| W1 | An Ethiopian by race, black, a house-servant (slave) of an official. | LH 333 | Documented | "A CERTAIN Moses----this was his name----an Ethiopian by race and black, was house-servant to a government official." |
| W2 | Sozomen calls him "an Egyptian" and "a slave". | SOZ 39461; 39499 | Documented (disagreement) | "Moses, an Egyptian, dwelt at Scetis." / "Moses was originally a slave, but was driven from his master's house on account of his immorality." |
| W3 | The Syriac chapter list names him "the Indian". | PAR1 299; TOM 8939 | Documented (as a title only) | "10.MOSES the Indian (Greek text, chap. 19)." / "10 Of Abba Moses, thejudian, the servant of" (OCR; next line TOM 8941 "Ptolemy. See fol. 120^"). The TOM line may name a master "Ptolemy"; the OCR and layout are too unclear to rely on, and the chapter text is not held. |
| W4 | The sayings call him "the Black" and "the Ethiopian". | PAR2 88; 2766; 2850; 2874 | Documented | "Abbâ Moses, the Black"; "Abbâ Moses the Ethiopian" |

## Events

| # | Claim | Source | Conf. | Verbatim |
|---|---|---|---|---|
| E1 | His master drove him out for immorality and brigandage; he was said to have murdered. | LH 333 | Documented as report; the murders themselves Contested (Palladius: "he was said to") | "His own master drove him out because of his immorality and brigandage. For he was said to go even the length of murder." |
| E2 | Palladius tells the crimes to show the repentance. | LH 333 | Documented | "I am compelled to tell his wicked acts in order to show the virtue of his repentance." |
| E3 | Said to have led a robber band; swam the flooded Nile, sword in mouth, to kill a shepherd; the shepherd hid; Moses killed four rams, ate, sold the skins for wine. | LH 333 | Documented as report ("they used to say") | "Anyhow they used to say that he was leader of a robber-band" ... "he grasped his sword in his mouth and put his shirt on his head and so got over, swimming the river." |
| E4 | Struck in conscience, he gave himself to a monastery. No cause is named. | LH 335 | Documented | "In the end this abandoned man, conscience-stricken as a result of one of his adventures, gave himself up to a monastery" |
| E5 | Sozomen calls the turn sudden. | SOZ 39502–39503 | Documented | "by some sudden conversion he embraced the monastic life" |
| E6 | Four robbers attacked him in his cell; he tied them, carried them to the church and asked the brothers what to do, since he might not hurt anyone. They confessed and left the world because of him. | LH 335 | Documented as Palladius's tale ("Among other tales this is told of him") | "He tied them all together and, putting them on his back like a truss of straw, brought them to the church of the brethren, saying: \"Since I am not allowed to hurt anyone, what do you bid me do with these?\" Then these robbers, having confessed their \|88 sins and recognized that it was Moses the erstwhile renowned and far-famed robber, themselves also glorified God and renounced the world because of his conversion, saying to themselves: \"If he who was so great and powerful in brigandage has feared God, why should we defer our salvation?\"" |
| E7 | He fought his old habit of sexual incontinence, as he himself testified, and nearly gave up. He went to Isidore, priest of Scete. | LH 337 | Documented | "This Moses was attacked by demons, who tried to plunge him into his old habit of sexual incontinence. He was tempted so greatly, as he himself testified, that he almost relinquished his purpose." |
| E8 | Isidore's image: a dog at a butcher's shop stops coming when the shop is closed. | LH 337 | Documented | "For just as a dog in a butcher's shop owing to his habits cannot tear himself away, but if the shop is closed and no one gives him anything, he no longer comes near it." |
| E9 | Twelve ounces of dry bread, much work, fifty prayers a day; then six years standing all night without sleep; still troubled by dreams. | LH 337 | Documented | "taking nothing except dry bread to the extent of twelve ounces, accomplishing a great deal of work and completing fifty prayers (a day)" / "So he remained in his cell for six years and every night he stood in the middle of the cell praying and not closing his eyes. And he could not master the thing." |
| E10 | By night he secretly filled the older monks' water-pots, from wells up to five miles off. | LH 337 | Documented | "going out by night he would visit the cells of the older and more ascetic (monks), and taking their water-pots secretly would fill them with water. For they fetch their water from a distance, some from two miles off, some five miles, others half a mile." |
| E11 | Struck at the well, in Palladius's telling by the demon; found next day; ill for a year. | LH 337 | Documented as Palladius's wonder-telling | "So one night the demon watched for him, having lost his patience, and as he stooped down at the well gave him a blow with a cudgel across the loins and left him (apparently) dead" ... "for a year he was so ill that with difficulty did his body and soul recover strength." |
| E12 | Isidore told him to stop fighting the demons; Moses refused; Isidore said his dreams had ceased and told him to come to Communion; two months later he suffered nothing. | LH 337 | Documented | "So the great Isidore said to him: \"Moses, stop struggling with the demons, and do not provoke them.\" But he said to him: \"I will never cease until the appearance of the demons ceases.\" So he said to him: \"In the name of Jesus Christ your dreams have ceased. Come to Communion then with confidence, for, that you should not boast of having overcome passion, this is why you have been oppressed, for your good.\"" |
| E13 | Became a priest; died at Scete aged 75; left seventy disciples. | LH 337 | Documented | see S1 |
| E14 | Sozomen: ordained presbyter over the monks at Scetis; numerous eminent disciples. | SOZ 39522–39525 | Documented (dependent) | "he was ordained presbyter over the monks at Scetis. After a life spent in this manner, he died at the age of seventy-five, leaving behind him numerous eminent disciples." |

## Sayings (PAR2; Syriac recension, 7th-century compilation)

Each is Documented as what the collection says; whether the event happened is Inferential-Thin. Only sayings that name him "the Black" or "the Ethiopian", or tie him to his story, are used.

| # | Claim | Line | Verbatim |
|---|---|---|---|
| Y1 | Fathers at Scete insulted him as "this Ethiopian"; he kept silent. | 164 | "On one occasion the Fathers in Scete were gathered together, and because certain folk were wishing to see Abbâ Moses, they treated him with contumely, saying, \"Why doth this Ethiopian come and go in our midst?\" But Moses hearing this held his peace. And when the congregation was dismissed, they said unto him, \"Abbâ Moses, wast thou not afraid?\" And he said unto them, \"Although I was afraid I uttered not a word.\"" |
| Y2 | A second telling of the same, in the question-and-answer part: "troubled" in place of "afraid", taught as a lesson on holding back anger. | 2874 | "Abbâ. Moses the Ethiopian was on one occasion reviled by certain men, and the brethren asked him, saying, 'Wast not thou troubled in thy heart, O father, when thou wast reviled?' And he said unto them, 'Although I was troubled, yet I said nothing.'" |
| Y3 | As one of the clergy, he was tested by the bishop; the clergy drove him out of the sanctuary as "Ethiopian"; he rebuked himself in racial terms. | 1028 | "Now when he went into the sacrarium they rebuked him and drove him out, saying, \"Get outside, O Ethiopian\"; and having gone forth he began to say to himself, \"They have treated thee rightly, O thou whose skin is dark and black; thou shalt not go back as if thou wert a [white] man.\"" (The bracket is Budge's supply.) Earlier in the same saying: "Behold, thou art wholly white, O Abbâ Moses." The old man said unto him, "Is the Pâpâ within or without?" |
| Y4 | He guided a brother: release from harvest work, keep the cell. | 88 | "he went to Abbâ Moses, the Black, and said unto him, \"Father, tell me what I shall do; shall I go to the harvest?\"" |
| Y5 | Remembered as "Abbâ Moses who was a thief", who welcomed visitors warmly; a vision sets him beside Arsenius. | 96 | "\"Take me also to Abbâ Moses who was a thief,\" and when they went to him, the old man received them with joy, and having refreshed them greatly he dismissed them in peace." |
| Y6 | Later teaching on Isidore's restraint of him: labour alone does not heal without the Spirit and Communion. | 2766–2768 | "Abbâ Isidore restrained Abbâ Moses the Ethiopian from works, and from contests with devils, saying, 'Rest thee, Moses, and quarrel not with the devils...'" / "thereupon Abbâ Moses learned these things, and his thoughts were humbled, and he partook of the Holy Mysteries, and the devils were conquered" / "Many monks have imagined that their passions would be healed, and that they would acquire soundness of soul merely by their labours and strenuousness, and therefore they were abandoned by grace, and fell from the truth." |
| Y7 | Later teaching: grace sometimes calls a man suddenly, as it moved Moses the Ethiopian. | 2850 | "Sometimes Divine Grace moveth a man suddenly, even as it moved Abbâ Moses, the Ethiopian, and sometimes by the hearing of the Scriptures, as in the cases of the blessed Mâr Anthony" |

Sayings naming only "Abba Moses" (not used as his, identity not shown in this edition): the basket of sand, refusing to judge a brother (1160); "sit in thy cell, and thy cell shall teach thee everything" (178); the barbarians who killed Abba Moses and seven brothers at Scete (1464); the Passover fast broken for guests (952); "Moses of Scete" praying for rain (1326); "Moses of Pâtârâ" shown the angels by Isidore (1202).

## Impact, heaviest first

1. **His story was told, from the first, as proof of what repentance does.** Palladius says so (E2, LH 333). Nikodemos repeats the purpose (NIK 41915–41919, OCR: "διηγήθην περί τοΰ όσιου τούτου, διά νά δείξω, ότι είναι δυνατόν νά σωΟώσι διά της μετανοίας όσοι θέλουσι, καΐ μυρίας πρότερον άν πράξωσιν αμαρτίας" — "I have told about this saint to show that those who wish can be saved through repentance, even if they have first done countless sins"). The Ethiopian Synaxarium closes on it (ESX-M 37189–37192): "Observe, O our brethren, the power of repentance and what it doth. It changed a man who was [OCR garbled] murderer, and a fornicator, and a thief, and made him a father and a teacher". Documented.
2. **People followed him into the monk's life.** The four robbers (E6) and seventy disciples (E13; NIK 41955–41957 also gives seventy, "μαθητάς καί μιμητάς", disciples and imitators). Documented as report.
3. **The Syriac teaching tradition used his case to teach.** Y6, Y7, Y2: Isidore's counsel became a lesson that effort alone does not heal, and his conversion an example of grace calling suddenly. Documented (7th-century compilation).
4. **Churches kept his feast.** Ethiopian: 24 Sane (ESX-M 37092–37094: "XXIV. Sane ... On this day Saint Abba moses the Black became a martyr."); hymn of salutation (ESX-1 2297–2318). Greek: 28 August (NIK 41888–41889, OCR: "μνήμη τοΰ ύσίου ... ΜΩΤΣΕΩΣ τοΰ Αΐθίο.•το<:", memory of the holy father Moses the Ethiopian). An Ethiopian saint's death-vision names him beside Antony, Macarius and Pachomius (ESX-2 2392–2394). The Ethiopian entry says his body lies "in dabra BADRfeMOS (baramus ?) in the desert of scete" (ESX-M 37195–37196; Budge's query). Documented that the calendars keep him; the grave claim is late legend.

## Links to other people

- **Isidore, priest of Scete:** guided him (E7, E8, E12). Met. Clarke notes Palladius names three Isidores (LH 711); this one is "the priest of Scete" (LH 337).
- **Palladius of Helenopolis:** wrote his life (LH 19). On the tree (census `palladius-of-helenopolis`).
- **Sozomen:** retold Palladius's account (SOZ VI.29).
- **Arsenius:** set beside him in a vision in saying 21 (PAR2 96). Not on the tree as far as checked.
- **Macarius:** in the Ethiopian Synaxarium only, baptizes him and foresees his martyrdom (ESX-M 37112–37114; 37157–37162). Late legend.
- **Not linked: the Abba Moses of Cassian's Conferences.** Gibson's introduction says Cassian's Moses had "formerly dwelt in the Thebaid near S. Antony" (CAS 15325–15326; editor's). Gibson's note takes him as possibly "the second of this name (Moses the Libyan) mentioned by Sozomen" (CAS 24272–24276; editor's). Palladius gives Moses the Libyan a separate entry (LH 467). Do not merge.

## Disagreements and late material

- **Ethiopian, Egyptian or Indian:** Palladius "an Ethiopian by race and black" (LH 333); Sozomen "an Egyptian" (SOZ 39461); Syriac chapter list "the Indian" (PAR1 299). Contested.
- **Age at death:** Palladius and Sozomen 75 (LH 337; SOZ 39524); Nikodemos 70 (NIK 41955, "έβδομήχοντα χρόνων γέρων"). Palladius is the earlier witness.
- **How he died:** Palladius and Sozomen say only that he died. A saying tells of barbarians killing an "Abba Moses" and seven brothers at Scete, without naming him the Ethiopian (PAR2 1464). The Ethiopian Synaxarium makes him a martyr killed by barbarians (ESX-M 37094; 37184–37188). Nikodemos sends readers elsewhere for "his martyrdom" (NIK 41935, OCR: "Το μα|>τΰριθ(< αύτοΰ βρα εις το νίον Λειμωνάριον", see his martyrdom in the New Leimonarion). Contested; the martyrdom rests on late witnesses and an unnamed saying. Nikodemos's own text, against his footnote, says he "fell asleep" in the ascetic life as an old man of seventy and calls him a holy father (ὁσίου), not a martyr (NIK 41953–41955, OCR: "θεαρέστως 7>οιπόν διανΰσας τήν ζωήν του ό όσιος ούτος, έκοιμήΟη έν ττ] άσχήσει, υπάρχων έβδομήχοντα χρόνων γέρων"; NIK 41888 "ύσίου").
- **Conversion:** Palladius names no cause (E4). The Ethiopian Synaxarium adds a sun-worshipping master, prayers to the sun, baptism by Macarius, five hundred brothers (ESX-M 37101–37114; 37137–37138). Late legend; not used.
- **The sanctuary test, retold late:** the Ethiopian Synaxarium retells PAR2 1028 with changes: the archbishop himself says "Why have ye brought this black man here? Take him away."; Moses says "They have treated thee rightly, O black man, O thou whose face is horrible"; then the archbishop ordains him and says "Behold, thou hast become white, all of thee, within and without." (ESX-M 37139–37148). The ordination after the test and "white within and without" are in this late witness only. In PAR2 1028, "thou art wholly white" is the bishop's remark when Moses wore "a long outer garment".
- **Sozomen's source:** the NPNF editor thinks the chapter's stories are "probably also borrowed" from Timothy of Alexandria, "at least in part" (SOZ 39403–39406; editor's).
- **The robber stories and the murder** come as report ("they used to say", "he was said to"), LH 333.
- **Wonders:** the demon's blow at the well and the power over demons are Palladius's telling (LH 337).

## Heart of his life: census check (added 2026-11-18)

Census `moses-the-black`, knownFor: "A house-servant driven out for robbery who became a monk at Scete in Egypt, a priest and a teacher of seventy disciples." Role: "Monk and priest". Each claim against the held texts:

| # | Census claim | What the sources hold | Source | Conf. | Verbatim |
|---|---|---|---|---|---|
| H1 | House-servant | Held. | LH 333 | Documented | "was house-servant to a government official" |
| H2 | Driven out for robbery | Held, but not robbery alone: "immorality and brigandage". | LH 333 | Documented | "His own master drove him out because of his immorality and brigandage." |
| H3 | A monk at Scete | Held. He gave himself to a monastery (LH 335); Isidore "the one who lived in Scete" guided him (LH 337); he died at Scete (LH 337). Palladius does not say the monastery he first entered was at Scete. | LH 335; 337 | Documented | "gave himself up to a monastery" / "So he died in Scete" |
| H4 | A priest | Held. | LH 337; SOZ 39522 | Documented | "having become a priest" / "he was ordained presbyter over the monks at Scetis" |
| H5 | Seventy disciples | Held. | LH 337 | Documented | "and he left seventy disciples" |
| H6 | A teacher | Not in Palladius's words; held by the sayings, which show a brother coming to "Abba Moses, the Black" for a rule of life. | PAR2 88 | Documented as what the saying says; the event Inferential-Thin | "he went to Abbâ Moses, the Black, and said unto him, \"Father, tell me what I shall do; shall I go to the harvest?\"" |
| H7 | (Not in census) Counted among the great fathers by the time Palladius wrote | Held. | LH 337 | Documented | "This was the manner of life of Moses the Ethiopian; he too was numbered \|90 among the great ones of the fathers." |

## The barbarian saying (PAR2 1464): decision (added 2026-11-18)

| # | Claim | Source | Conf. | Verbatim |
|---|---|---|---|---|
| B1 | A saying tells of barbarians at Scete killing "Abbâ Moses" and seven brothers; he quotes "Those who take the sword shall perish by the sword". It does not name him the Black or the Ethiopian. | PAR2 1464 | Documented as what the saying says; that it is this Moses, Inferential-Thin | "On one occasion when the brethren were sitting with Abbâ Moses, he said unto them, “Behold, this day have the barbarians come to Scete; rise up and flee.”" ... "‘Those who take the sword shall perish by the sword’ ”" |
| B2 | Only the late Ethiopian Synaxarium ties this death, and the sword word, to Moses the Black. | ESX-M 37160–37163; 37185 | Late legend | "And Abba moses answered and said unto \| him, \" Peradventure I am he, O my father. For it is written. \| He who hath slain with the knife shall die by the knife\" (Mat- \| thew xxvi, 52). And when the Barbarians came" / "came and killed him. And with him were seven brethren who" |

Decision: the saying is not told and not quoted. In the held texts its Moses is made the Ethiopian only by a witness about a thousand years late; the earlier witnesses, Palladius and Sozomen, say only that he died at Scete at seventy-five. Telling it with that limit audible would spend a large share of a two-minute story on a doubtful identity, and its sword line invites a link to the robber's sword that no source draws. The late Ethiopian memory of a violent death keeps one clause in the death beat, credited.

## Library sweep

- **Card sources** (starting list): LH, SOZ, PAR2, CAS. All opened and read at the lines cited.
- **Corpus map:** `cic/corpus-map/desert-monasticism.yaml` (source files listed; line 531 mentions "Abba Moses arriving at the council with a leaking jug", the PAR2 basket saying). No other bucket names him. `WORKS.yaml`, `AUTHOR-IDS.yaml` and `RETRIEVAL-HINTS.md` have no entry for him (grep "moses" found none relevant).
- **Text search:** `cic/texts/` grepped for "Moses the Black/Ethiopian/Robber/Indian", "Abba/Abbâ/Abbot Moses", "Moses who was a thief", "Moïse le noir", "Moyses Aethiops", Greek "Μωϋσῆς/Μωσῆς ... Αἰθίοψ", and Greek synaxaria and Coptic synaxary volumes by hand. The broad Latin/Greek name forms hit some 330 files, almost all on the biblical Moses. **Eleven files mention this Moses:** LH, PAR1 (title only), PAR2, SOZ, CAS (only to tell another Moses apart), ESX-M, ESX-1, ESX-2, NIK, TOM (manuscript list and index only), and the corpus map row.
- **Used:** LH (main witness), PAR2, SOZ, ESX-M, ESX-1, ESX-2, NIK, PAR1 and TOM for name forms.
- **Set aside:** CAS, because its Abba Moses is a different monk; the Syriac Palladius chapter, Greek Lausiac and Greek alphabetical sayings, because they are not held; the Coptic Synaxary, because the Ba'unah volume is not held; the Ethiopian Synaxarium's conversion and martyrdom details, because they are late legend in conflict with or beyond Palladius; the TOM "Ptolemy" reading, because the OCR is unclear.
- **Later witnesses read and set aside (added 2026-11-18, from Outline_Check_2):** Dorotheus of Gaza, Doctrina XIV (`dorotheus-gaza_doctrinae-barsanuphius-climacus-agathias-grc-lat_migne-pg88.txt` 136342–136344, Latin): "Ut se ipsum accusabat abbas Moyses dicens : « Sterqui- linium cum sis et cinis, non homo ; cur ad homines ingrederis? »" ("you are dung and ash, not a man; why do you go in among men?"). Close to the sanctuary saying (Y3), but names only "abbas Moyses". Theodore the Studite, PG 99 (`theodore-studite_opera-omnia-pg99-grc-lat_migne1860.txt` 72550–72561, Latin), retells the two-boats vision of Arsenius and "abbas Moyses" (Y5). Neither names him the Ethiopian; neither is used.
- **Correction:** the corpus-map row on the leaking jug is `desert-monasticism.yaml` line 620, not 531.
- **Not opened, per run rules:** any `*.brief.txt`, and the census `longDescription` and `teaser`.
