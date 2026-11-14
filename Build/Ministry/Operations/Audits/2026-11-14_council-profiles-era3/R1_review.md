# Council profiles, era 3: review round 1 (2026-11-14)

**Scope.** Three major-council profiles in `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era3/`: `second-council-of-constantinople-553`, `third-council-of-toledo-589`, `council-of-dvin-609`. For each: the brief, the entry, the audio script and that id's part of `records.json`. The scope matches `Build/Ministry/Operations/Audits/2026-11-12_major-events-scan/Councils_Scan.md`, "Era 3", which lists exactly these three. Open-Gaps 246 corrects only era 1 and 2 rows, so it changes nothing here.

**Standard.** `Council_Profile_Pattern.md` (C1 to C8) with `Who_Profile_Pattern.md` checklist items 1 to 9, 11 and 13. The approved era 1 and 2 profiles in `Council-Profiles/era2/` are the form to match.

**Method.**
- Every quotation in the three briefs and entries was searched in its vendored file under `cic/texts/` with a whitespace-, hyphen- and tag-tolerant search, and read in context for speaker, side and meaning. The file:line cited in `records.json` was opened for every claim the briefs rest on.
- Every factual sentence of each brief was checked against the held lines: dates, counts, who did what, and every "only", "no held source" and "not held". `cic/texts/` was searched for counter-evidence: all spellings of Kyrion (Kiurion, Kurion, Gurion, Gourion, Cyrion, Quiricus), Michael the Syrian, Labourt, Wigram, Chamich, Langlois, Serpos, both Brosset Georgian volumes, the second Stephen of Taron volume, Liberatus, John of Ephesus and the Collectio Avellana.
- People verdicts were checked against every Who scan (`2026-11-1*_who-scan-*/Who_Scan_*.md`, the supplement and the dedupe list). Person ids were checked against the Who-profile cards and `cic-website/data/world-census.json`. Tradition ids, names and dates were checked against the census, and the census edges for each council were read.
- Readability was scored with `engine.m1.gates.grade_text`. Sentences were split and counted. Each audio script was compared with its brief plus `[calmly] ` at the start and `[warmly] ` before the last paragraph.
- No model calls, no network calls, no paid services. No draft was edited.

**Result in one line.** All three pass the gates (readability, length, audio), and every quotation is in its file word for word; no finding is blocking, but five substantial findings, two at Constantinople and three at Dvin, need a fix before those two profiles are approved to proceed; Toledo has minor findings only.

## Per-council table

| Council | Words | FK | FRE | Audio = brief | Verdict |
|---|---|---|---|---|---|
| second-council-of-constantinople-553 | 400 | 7.87 | 60.66 | yes | PASS WITH FIXES |
| third-council-of-toledo-589 | 398 | 6.93 | 69.22 | yes | PASS |
| council-of-dvin-609 | 353 | 8.11 | 60.66 | yes | PASS WITH FIXES |

Each audio script equals its brief with the two tags and no others; the only difference is the brief file's trailing newline. Constantinople and Dvin sit just over the reading-ease floor, and Constantinople is at the 400-word ceiling. Any fix that adds words there needs a cut elsewhere and a rescore. No brief sentence runs past 25 words; the longest is Constantinople's 24-word "In a session given in full only in the Paris copy …".

## Quotations

Every quoted string in the three briefs is verbatim in its file, and its speaker is right:
- Constantinople: Evagrius IV.38 (`evagrius-scholasticus_ecclesiastical-history_walford1846.txt` l.9545-9546); the emperor's letter (`npnf214_seven-ecumenical-councils.xml` l.23129-23130, but see CON-3); the sentence (l.23669); Gregory to Constantius (`npnf212_leo-great-gregory-great.xml` l.40147-40150).
- Toledo: Agilan's words in Gregory of Tours V.43 (`gregory-tours_history-of-the-franks-v2_dalton1927.txt` l.10199-10201); Gregory to Leander (`npnf212` l.32576-32577).
- Dvin: Kyrion's reply (`issaverdens_armenia-and-the-armenians-v2-ecclesiastical-history_1875.txt` l.3695-3697); "and all those who accepted it" (l.3705-3706, across the page break); Ormanian's "became part of the Greek Church" (`ormanian_church-of-armenia_gregory1912.txt` l.2737-2738).

The entries' quotations are verbatim too, with the exceptions named in TOL-1 (English renderings of Latin in quotation marks) and CON-3.

---

## second-council-of-constantinople-553

**CON-1. Substantial (item 1; C5; C1).** The Persian synod of 585 is presented as the Church of the East's answer to the council.
- Entry `traditions`, `the-church-of-the-east-under-persia`, part "Refused": "A synod of the Church of the East, dated to 585 … gave a canon to the defence of the books and teaching of 'saint Théodore', the Interpreter." Entry `record`, Synodicon: "Not an account of the council, but a later synod's answer to it." Entry `outcome[4]` says the same. In the brief the synod is placed in the aftermath, between Victor's exiles and Gregory: "In Persia, a synod of the Church of the East defended Theodore as the Interpreter of Scripture."
- The canon names neither the council nor Justinian. It answers men "dans le temps actuel … qui s'intitulent orthodoxes" inside the Persian church (`synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt` l.26570-26600, 26646-26660). Jérôme Labourt, a held historian, reads that canon as aimed at the party of Henana of Adiabene: "C'étaient les partisans de Henana d'Adiabène" (`labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt` l.15699-15719). The census row and Open-Gaps 248 say the same ("the synods of 585, 596 and 605 never name Henana, and Chabot, Braun and Labourt infer it").
- The one held link between the 585 synod and the fifth council is Labourt's reading of Ishoyahb's creed, not the canon: "Le patriarche argumente contre tous les partisans byzantins ou persans du cinquième concile œcuménique" (l.15587-15589). Labourt also says the synod of 554 makes no allusion to the controversy (l.15542-15543).
- Fix: in the entry, credit the link to Labourt by name as his reading of the creed. Say the Theodore canon names no council and that Labourt takes it as aimed at Henana's followers. Change the part to Affected unless a held witness says the church refused the council. Add Labourt to `record` (modern reconstruction) and `sources.writtenLater`, and a claim to `records.json`. In the brief, either drop the Persia paragraph or make it Labourt's reading, for example: "In Persia, Jérôme Labourt, a French historian of that church, reads the creed of a synod of 585 as an answer to the council." Rescore; the brief is at the 400-word cap.

**CON-2. Substantial (false absence; C1; item 7).** `records.json`, `absent_details[4]`: "A Miaphysite response to the council: None found in John of Ephesus, the Syriac chronicle known as Zachariah's, or Procopius." The Library holds one. Michael the Syrian's chronicle, in Chabot's French, has a chapter on "the synod that Justinian gathered at Constantinople, which is called the Fifth Synod" (`michael-the-syrian_chronique-tome2-livres-viii-xi-fra_chabot1901.txt` l.18680-18681, 19002-19006). It says:
- the year is "l'an 26 de Justinianus, qui est l'an 864 des Grecs" (l.19002-19004);
- three patriarchs were there, Eutychius, Apollinaris and Domninus, and Vigilius "se trouvait bien dans la ville impériale … mais il ne vint point à l'assemblée" (l.19066-19075);
- "le synode confirma l'anathème d'Origène, qu'avait porté Justinianus lui-même" (l.19089-19091).

A second passage, which speaks of the synod as held "de nos jours", says Vigilius "fut invité à venir au synode : il n'y vint pas" (l.6757-6768). This bears on two of the entry's contested claims. On the Origen question it is a witness on Evagrius's side. On Vigilius's attendance it is a third witness, with the acts and Evagrius, against Victor of Tunnuna. Neither claim lists it.

Fix: remove the absent detail. Add Michael the Syrian to `record` (later narrative, Syriac Orthodox, twelfth century, copying earlier writers) and to `sources.writtenLater`. Add him to the `contested_claims` on Origen and on whether Vigilius was present, and to `uncertain`. Weigh whether `syriac-orthodox-west-syriac-christianity` belongs under Affected. The brief need not change.

**CON-3. Minor (item 2).** Brief: "'In vain we sent several commands to him,' the emperor's letter says." The line sits inside Percival's note "[The following is the letter condensed, including Hefele's digest …]" (`npnf214` l.23069-23071), in a stretch marked "From here to the next asterisk the text varies. Hefele says he follows the Paris codex with 'abridgments'" (l.23124-23127). These are Hefele's condensed English, not a translation of the emperor's whole sentence. The same applies to the paraphrase in paragraph 3. Fix: "the emperor's letter says, in the digest Hefele gives", or drop the quotation marks and tell it in modern words.

**CON-4. Minor (item 7).** Brief: "Vigilius was in the city but would not come." This is told flat, while `contested_claims[1]` holds it as Contested (Victor of Tunnuna: "cui praesules sedium aderant Vigilius", `chronica-minora-2_…mommsen1894.txt` l.19130-19131). The emperor's letter is named and the weight of witnesses is heavily one way (with Michael, CON-2), so this is not misleading. Fix: none needed in the brief. In the records, once Michael is added, tag the claim Widely Accepted with Victor's listing as the dissent, so the brief and the records agree.

**CON-5. Minor (ambiguous antecedent).** Brief: "Percival says most scholars accept it as his. He died in Sicily, going home." Heard aloud, "He" falls on Percival. Fix: "Vigilius died in Sicily, going home."

**CON-6. Minor (items 4, 9).** Brief: "The sentence reads, 'We therefore anathematize the Three Chapters.'" Heard aloud, "The sentence" can mean the grammatical sentence. "Anathematize" is new to the listener, since the brief has said "curse" so far. Paragraph 4 says "one Paris manuscript" and paragraph 6 says "the Paris copy". Fix: "The council's final sentence reads, 'We therefore anathematize,' or curse, 'the Three Chapters.'" Use one word, "manuscript", in both places.

**CON-7. Minor (item 1; close).** Brief close: "Gregory the Great of Rome later wrote of the synod 'called by many the fifth.' Nothing was done in it, he said, 'with respect to the faith, but only with respect to persons.'" Heard alone, this sounds like Rome's verdict on the council. Gregory wrote it to Constantius of Milan, who had held back a letter to Queen Theodelinda because it named the fifth synod (`npnf212` l.40141-40144). In Letter I.25 he writes, "The fifth council also I equally venerate" (l.31921-31922). The entry's `outcome` carries both. Fix: "Writing to Milan, where the Lombard queen took offence at the council, Gregory the Great …", or add that he also said he venerated it. Mind the word cap.

**CON-8. Minor (pattern 3; C2; item 4).** Brief: "The Library holds only extracts of the acts, in English." "The Library" is the project's own word, and the era 2 briefs do not use it. The sentence can also be heard as saying that only extracts survive, but the full acts are in Mansi, tomus 9. The brief also never says that the acts are the record of the side that won. The entry's `uncertain[0]` and `record` both say so. Fix: "The council's acts survive in full in Latin. We draw on English extracts, the record of the side that won."

**CON-9. Minor (item 7).** Entry `calledBy`: "Pope Vigilius did not consent (Hefele)." Evagrius says the opposite: "Vigilius gave his assent in writing to the assembling of the synod but declined attendance" (`evagrius…walford1846.txt` l.9556-9557). The point is credited to Hefele, so it is not told as settled, but Evagrius is not named. Fix: add "Evagrius says he assented in writing to the meeting but would not attend", and a `contested_claim`.

**CON-10. Minor (C7; entry fields).**
- `informalName`: "the council of the Three Chapters" is in no held file (searched). The pattern asks for "another name the held sources use". "The Fifth Council" is held (Gregory, Percival, Michael). Fix: keep "The Fifth Council" and drop the other.
- `people`: Gregory the Great (WHO; census id `gregory-the-great`) and Pelagius II (LISTED in the era 3 scan) are named in `outcome`, and Gregory in the brief's close, but neither is in `people`. Toledo lists Gregory as "Not present; wrote …". Fix: list both, as Toledo does.
- `uncertain[3]`: "Justinian did not sit in it" cites no witness. The held lines show his letter read in Session I and his quaestor speaking in Session VII (`npnf214` l.23194-23196, 23271-23276). Fix: "Justinian wrote to the council and sent his quaestor Constantine to speak for him in Session VII."

## third-council-of-toledo-589

**TOL-1. Minor (item 2).** The entry puts English renderings of Latin in quotation marks, as if they were the source's words:
- `issue[1]`: "our catholic faith" (`nostram catholicam fidem`, John of Biclaro, `john-biclaro-leander-pl72-lat_migne1878.txt` l.64851) and "Glory to the Father through the Son in the Holy Spirit" (acts, `collectio-canonum-ecclesiae-hispanae-toledo-iii-lat_1808.txt` l.36969);
- `issue[2]` and `uncertain[4]`: "not many days" (`non multos … dies`, l.36621-36622);
- `traditions`, homoian row: 'the faith and communion coming from Arius' (l.36900-36901);
- `attended[4]`: "all the seniors of the Goths" (`omnes seniores Gothorum`, l.37214).

This is the ARI-5 fault from the era 2 round. Fix: drop the marks and tell them in modern words, or quote the Latin with an English gloss outside the marks.

**TOL-2. Minor (item 1).** Entry `decided[0]` says "O. M. Dalton … says the speech was composed by Leander", next to the book of faith. `record` says "Dalton says Leander composed it". `uncertain[3]` and `contested_claims[3]` say "Whose words the king's book of faith is … Dalton … says Leander composed it." Dalton's note reads "His speech on that occasion was composed by Leander" (`dalton1927.txt` l.29212-29214). That is Reccared's speech to the council, and Dalton does not say it means the tomus. Fix: "Dalton says Leander composed the king's speech", and frame the contested claim as whether the king's words at the council were Leander's.

**TOL-3. Minor (item 8).** Brief: "Leander of Seville and Eutropius, an abbot." Eutropius is a common name (Eutropius the historian, and others) and has no place. John of Biclaro gives "Eutropium monasterii Servitani abbatem" (`mommsen1894.txt` l.20398-20399). Fix: "Eutropius, abbot of Servitanum". Optionally, "Masona, bishop of Mérida" at first mention, as the entry's `people` gives his role.

**TOL-4. Minor (register).** Entry `attended[1]`: "In the held list, as counted for this profile, … The scan is damaged in two places." This is process narration in a participant-facing field. Fix: "The signed list has sixty-two bishops in person and five who signed through deputies. Two places in the printed text are damaged."

**TOL-5. Minor (sources).** Reccared's own letter to Gregory the Great is held in English (`npnf213_gregory-great-ephraim-syrus-aphrahat.xml` l.2251-2262), with Barmby's note that "the genuineness of this letter is considered doubtful". It is not in `sources` or `record`. Fix: add it under `fromThoseThere`, with the doubt, or note in `records.json` why it is left out.

**TOL-6. Minor (C7).** `people` lists Gregory the Great as "Not present". It leaves out the brief's other named witnesses who have Who verdicts: John of Biclaro (WHO), Isidore of Seville (WHO) and Gregory of Tours (WHO, card `gregory-of-tours`). It also leaves out Euphemius of Toledo, who signed second. Fix: settle one rule for all three councils on whether non-attending witnesses go on the Who click (see CON-10), and apply it.

**TOL-7. Minor (item 1; optional).** Brief and entry: "in twenty-three anathemas". Articles I to XXII are anathemas. Article XXIII is the closing subscription: "Proinde damnationem hanc … cum anathemate eorum propria manu subscripsimus" (acts l.37017-37024). Twenty-three is the usual count, so this is not wrong. Fix (optional): "in twenty-three articles of condemnation".

## council-of-dvin-609

**DVN-1. Substantial (C1, C3, item 6).** Brief: "His side reaches us only through his foes." Entry `uncertain[0]`: "the Georgian side reaches us only through its opponents." Kyrion's own words reach us only through James Issaverdens. The file header calls his book "A Mechitarist's English sketch … written for visitors to San Lazzaro". Issaverdens calls Kyrion "a most learned and pious man" (`issaverdens…1875.txt` l.3653-3654). That is not a foe's account. Brosset, the other main modern witness, is a French historian of Georgia, on neither side. The entry's `record` gives Issaverdens no side at all, so C1 is not met for him. This puts the brief's key witness on the wrong side, the fault ARI-1 found in era 2. Fix: brief, "His own words reach us only in Issaverdens, who calls him 'a most learned and pious man.' Every other witness is Armenian or modern." Entry: give Issaverdens's side in `record` (a Mekhitarist of San Lazzaro, writing in 1875, favourable to Kyrion), and reword `uncertain[0]`. Read with DVN-3, which may add a friendly witness. Rescore; FRE is 60.66.

**DVN-2. Substantial (C2; item 1).** The brief opens on Stephen of Taron's anathema as the council's scene: "When he failed, he drew the spiritual sword and cursed them, with the assent of all the Armenians." It later joins it to Issaverdens: "Issaverdens says Abraham then called a synod of bishops at Dvin." Stephen names no council and gives no date (`stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt` l.3101-3105). The entry's own `decided[1]` says so: "Stephen of Taron, who names no council and gives no date". Every held account of a synod at Dvin is modern: Issaverdens in 1875 (l.3700-3706), Brosset in 1876 (`zakaria_memoires-historiques-sur-les-sofis-fra_brosset1876.txt` l.22668-22672, citing Kirakos and Ukhtanes, neither held) and Ormanian in 1912 (l.2737-2738). The brief says "Our witnesses are Armenian writers and modern historians". It does not tell the listener that the council itself is known only from the modern writers. Fix: add after paragraph 1, "Stephen names no council and gives no year. The synod at Dvin is told only by writers of the 1870s and after." Change "then called" to "called". Rescore.

**DVN-3. Substantial (items 1, 7).** Entry `uncertain[4]`: "Whether a letter of Gregory the Great to Quiricus, a bishop in Hiberia, concerns Kyrion: its editors do not say so, and incline to Pontic Iberia." `records.json` `contested_claims[2]` sets the editors against the census on the same ground. This misreads the editors. Ewald and Hartmann weigh three places, "in Hiberniam an in Hiberiam Ponticam an in Hispaniam, quae etiam Hiberia appellatur", and choose the Pontic one: "Equidem puto de Hiberia Pontica agi" (`gregory-great_registrum-epistolarum-t2-pars2-libri-10-14-lat_ewald-hartmann1895.txt` l.12165-12170). Against Ireland and Spain, the Pontic Iberia is the Caucasian one, Kyrion's own country. The editors do not name Kyrion. But their reading supports the census's identification rather than standing against it. They date the letter 601 (l.12142), while Maurice was still emperor, and it is addressed to "Quirico episcopo et ceteris in Hiberia catholicae ecclesiae episcopis" (l.12179-12180). Fix: "Its editors do not name Kyrion, but place the letter in the eastern, Pontic Iberia and date it 601." Re-tag the contested claim, and say whether the letter bears on DVN-1 (a friendly witness) and DVN-4 (the date). If it is used, add it to `sources`.

**DVN-4. Minor (C4; item 7).** Brief: "Ormanian has Abraham elected on 30 April 607 and the council at Dvin in 609. Brosset, in a note of 1876, puts it in 596." `contested_claims[0]`: "Issaverdens and Stephen of Taron: no year." Neither gives a year for the synod, but both place Abraham's break in the reign of the emperor Maurice. Stephen goes straight on from the anathema: "Der Kaiser Maurikios aber setzte einen gewissen Yöhan zum Katholikos … ein; und Abraham residierte in Duin" (gelzer-burckhardt l.3103-3105). Issaverdens dates Abraham's accession "A. D. 59?" (the last digit is lost in the OCR, l.3690), and has Kyrion appeal to Maurice (l.3714-3717). Phocas took the throne in November 602 (Barmby, `npnf212` l.23781), so both accounts sit badly with 607 and 609. The teaser and `shortName` ("Dvin, about 609") lead with Ormanian's side. Stephen's "shortly before Movses died" is also told without Issaverdens's 580, "immediately after his elevation" (l.3644-3660). Fix: in the records and `uncertain`, add that Stephen and Issaverdens set Abraham under Maurice, and Issaverdens's year for Abraham. Consider "Dvin, between 596 and 609" for the teaser and short name.

**DVN-5. Minor (item 4).** Brief: "Shortly before Movses died, Stephen says, Kyrion came to doubt the orthodox faith." Heard aloud, "the orthodox faith" is the narrator's word, and it takes the Armenian side. Fix: "came to doubt what Stephen calls the orthodox faith".

**DVN-6. Minor (register).** Brief: "No record of the council is held in the Library"; "No held source names the bishops or counts them"; "No other held source tells of that meeting." These use the project's own vocabulary, which the era 2 briefs avoid. Fix: "No record of the council survives in the books we draw on"; "No writer names the bishops or counts them"; "No other writer tells of that meeting."

**DVN-7. Minor (close; item 1).** Brief close: "Brosset, the French historian of Georgia, wrote in 1849 that the Georgians parted from the Armenians in religion for ever." In the held note Brosset dates this "vers l'an 580", before either date for the council. He also says "Tous ces témoignages sont tirés de Tchamitch" (`kartlis-tskhovreba_histoire-de-la-georgie-pt1-histoire-ancienne-fra_brosset1849.txt` l.9695-9697). Told as the close of a Dvin profile, it reads as the result of the council, and it drops his date and his source. Fix: "Brosset, drawing on the Armenian historian Chamich, wrote in 1849 that from about 580 the Georgians parted from the Armenians in religion for ever." Or close on Ormanian's "became part of the Greek Church", moved from paragraph 7.

**DVN-8. Minor (entry field).** `informalName`: "The council of the Armenian–Georgian break" is in no held file (searched). The census uses "Dvin III" and "the third council of Dvin". Ormanian writes "the synod of Douine". Fix: "The Third Council of Dvin", or leave the field out.

**DVN-9. Minor (record).** Samuel of Ani's own table, as Brosset's note quotes it, says: "Les Ibériens, ayant adopté l'hérésie de Chalcédoine, se séparèrent" (`zakaria…brosset1876.txt` l.22668). This is a held medieval Armenian witness, and the census edge already cites "Samuel of Ani, an Armenian chronicler of the 1100s". The entry's `record` lists only Brosset's note on it. Fix: add Samuel to `record` (later narrative, Armenian side), with Brosset's judgment that the table's chronology there is "entièrement fausse".

---

## Checks that passed across all three

- **C1.** Every `record` entry has a kind. Partisan witnesses are marked (Justinian, Victor of Tunnuna, Evagrius, the Toledo acts, John of Biclaro, Gregory of Tours, Stephen of Taron, Ormanian), except Issaverdens (DVN-1).
- **C2.** Toledo names the held acts first and says they are the winners' record ("Every witness here writes from the Catholic side"). Dvin says early that no record is held. Constantinople says early what of the acts is held, with the gap in CON-8.
- **C3.** Constantinople gives the defenders in their own words: Vigilius's Constitutum (`collectio-avellana_…v1-lat_guenther1895.txt` l.22362-22364) and Facundus (`facundus…pl67-lat_migne1865.txt` l.41872-41882). Toledo gives the Homoian view through two witnesses: Agilan in Gregory of Tours, and Leovigild's synod and booklet through John of Biclaro and the acts. Dvin gives Kyrion's reply, with the side error in DVN-1.
- **C4.** Every count has its witness. The Toledo sixty-two and seventy-two (acts l.36593; PL72 l.65083; Mommsen l.20392) and the Constantinople 145 and 165 (Hefele, `npnf214` l.22879-22883; the Vienna manuscript, l.24008) are kept apart. Modern dates are credited by name: Hefele for 5 May 553, Chabot for 585, Percival for 589, Ormanian for 607 and 609, Brosset for 596. Two dates convert an ancient date and need no modern name. The 14 May of the Constitutum is "prid. Iduum Maiarum" (Avellana l.24223). The 8 May at Toledo is "die octavo iduum majarum" (acts l.36612).
- **C5.** `issue`, `decided` and `outcome` are separate in all three entries. Refusals are told as such: Africa, Milan and Istria for Constantinople; Vertanes and Gregory at Issaverdens's Constantinople meeting for Dvin. The exception is CON-1.
- **C6.** Toledo tells the king's book of faith as read by a notary and signed by the king and Queen Baddo (acts l.36631-36632, 36771-36782). The Gothic profession is told as signed by eight former Arian bishops (l.37118-37170). The Constantinople anathemas are told as the council's sentence.
- **C7.** All three entries have `kind` `major-council` and `kindLabel` "Major council". The verdicts match the scans. Justinian I, Vigilius, Theodoret, Origen, Victor of Tunnuna, Primasius, Reccared, Leander and Gregory the Great are WHO. Facundus and Reparatus are STORY. Theodore of Mopsuestia and Kyrion I are LISTED. Eutychius, Ibas, Pelagius I, Masona, Eutropius, Baddo, Leovigild, Abraham, Movses II and Vertanes are NOT SCORED. The era 3 scan names Abraham and Vertanes as "not in my list", and Movses II and Pelagius I appear only in its namesake notes, so NOT SCORED is right for them. Every id resolves to a Who card (`vigilius-of-rome`, `victor-of-tunnuna`, `theodoret-of-cyrrhus`, `reccared`, `leander-of-seville`) or to a census entry (`justinian-i`, `origen`, `gregory-the-great`). Every tradition id is in the census, with dates that fit. The Antiochene row (350-430) is used with the census edge that records the 553 condemnation. The scan's `aquileian-christianity` (340-410) is rightly left out, as Sardica's era 1 row was.
- **C8 and item 11.** All three briefs are within 400 words and pass `grade_text`. Each opens on a sourced moment: Evagrius's question of cursing the dead, the fast and the king's entry in the Toledo acts, and Stephen's anathema (see DVN-2).
- **Item 3.** No invented scene, feeling or speech. The Toledo scene is checked against the acts (l.36598-36622), Argimund's punishment against John of Biclaro (PL72 l.65064-65080; Mommsen l.20429-20436), and the Eutychius scene against Evagrius.
- **Item 4.** No "not X but Y" contrasts in the narrator's voice; Gregory's "not … faith, but only … persons" is a quotation. No rhetorical questions, no tail lines, no colon-reveals. Every close ends on a sourced statement.
- **Item 5.** No role stands in for a witness. Every modern editor is named: Percival, Hefele, Chabot, Brosset, Ormanian, Issaverdens, Dalton, Barmby, Mommsen, Günther, Duchesne.
- **Item 13.** The tags are only in the audio scripts, in the two right places.

## Notes for the coordinator (no fix to these profiles)

- Scan correction: the Who scan row "Stepanos of Taron (Asoghik) … WANTED … Not held" is wrong. His Universal History is held in German (`stepanos-taron_armenische-geschichte-deu_gelzer-burckhardt1907.txt`) and, for Book III, in French (`stepanos-taron_histoire-universelle-deuxieme-partie-fra_macler1917.txt`).
- The Constantinople entry leaves out the scan's `aquileian-christianity` and adds `antiochene-exegetical-christianity-chrysostom-ce`, `the-church-of-the-east-under-persia` and `roman-church-gregorian`. These belong in an Open-Gaps entry like 246 when the era is approved.

## Counts

| Council | Blocking | Substantial | Minor |
|---|---|---|---|
| second-council-of-constantinople-553 | 0 | 2 | 8 |
| third-council-of-toledo-589 | 0 | 0 | 7 |
| council-of-dvin-609 | 0 | 3 | 6 |
| **Total** | **0** | **5** | **21** |

Round 2 should be a targeted recheck of the five substantial findings, and of any minor fix taken. Constantinople and Dvin must be rescored after their fixes, since both sit at FRE 60.66 and Constantinople is at 400 words.
