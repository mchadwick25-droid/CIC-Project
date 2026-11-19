# Era 3 on the live tree (data release 42): review round 1

Reviewer: fresh Opus agent, full effort, independent of the drafting. Branch `claude/cft-era3-live` at `477c7d3b`, against `origin/main`.

**Verdict: not yet approved to proceed. 2 blocking, 8 substantial, 10 minor.**

The validator run named in the brief passes: `cic-website/data/world-census.json: 559 movements, 736 edges, 10 eras — 0 errors, 4 warnings` (the four are shortName length warnings, one of them `council-of-dvin-609`). `tools/check_spelling.py` on the census finds 0 British spellings. The 76 people and 3 councils in the census match their profile files: every brief, knownFor and card field is the same. Every place id was copied from an existing census row.

How this was checked. `Census_Text_Changes.md`, the file the brief names, is not on the branch (see S8). The older-text changes were reviewed from an independent diff of release 41 (`census41.json`) against the branch census. That diff matches the 19 changes in the worker's scratchpad `fixlog.json`. Every rendering, scan reading and fix below was checked against the vendored file at the line given.

---

## BLOCKING

### B1. Fulgentius of Ruspe and Victor of Vita sit in the "Non-Nicene Traditions" lane (`fulgentius-of-ruspe`, `victor-of-vita`)

The census text: `"toldWithin": "gothic-and-vandal-homoian-christianity"`, `"lane": "8 Beyond the Floor (researched & explained)"`, `"laneLabel": "Non-Nicene Traditions"`. The build script takes the lane from the home tradition (`if home: lane = home['lane']`). The tree page for Fulgentius now reads: "A person. The tradition that tells their story: Gothic, Vandal & Lombard Homoian Christianity."

The census's own card says the opposite. Fulgentius's knownFor reads: "Catholic bishop of Ruspe in Africa under the Arian Vandal kings ... who answered King Thrasamund's case against the Catholic faith in writing." In release 41, every person in lane 8 belonged to the non-Nicene tradition that holds them: Valentinus, Marcion, Bardaisan, Ulfila, Arius, Eusebius of Nicomedia, Apollinaris, Aetius, Eunomius, Philostorgius and Auxentius. These two would be the first Nicene opponents placed in that river. A participant scanning the map would read them as Homoians. That is misleading.

The placing is also inconsistent with this build's own call for Boethius. He is "named only in the text of the Gothic, Vandal & Lombard Homoian Christianity entry (his execution)" (Open-Gaps 252), yet he is told within none, in the Latin West river.

Fix. Tell Fulgentius within none, in the Africa river (`4 Africa`, where Latin African Christianity under Byzantium sits), as Boethius is in Latin West. Do the same for Victor of Vita, or put both to Mark together as one choice. If Mark keeps the Homoian placing, the person's lane must not read "Non-Nicene Traditions". The defensibility of each placing is set out under item 4 at the end.

### B2. The Nisibis story now cites the Chronicle of Seert for a sequence the Chronicle does not tell (`the-church-of-the-east-under-persia`, documentedStories[1].text)

The new text: "The church's synods of 585, 596 and 605, and the Chronicle of Seert, record the sequence: the catholicos Ishoyahb condemned Henana's teaching without naming him; Henana kept his post under the protection of the Persian governor; and finally, by the Chronicle of Seert's count, about three hundred students walked out in a body rather than sit under him."

The Chronicle (ch. LXXIV) tells a different sequence.
- Henana found help from the king's physicians, not from a governor: "jusqu'à ce qu'il eût trouvé occasion d'implorer le secours des médecins du roi, auxquels le métropolitain Grégoire avait défendu d'épouser deux femmes" (`chronicle-of-seert_histoire-nestorienne-seconde-partie-po13-ara-fra_scher1919.txt` l.28658-28660, OCR normalized).
- The catholicos in the Chronicle is Sabrisho, and he sided with Henana: "le catholicos, bien loin de confirmer leur sentence, accueillit favorablement la lettre de Hnana" (l.28666-28667).
- The students left because of Sabrisho's decision and Gregory's departure: "Les étudiants furent fortement affectés de cette décision de Sabriso'" (l.28671).

No held line gives a governor's protection. Labourt has the notables of Nisibis and the king acting against Gregory (`labourt_le-christianisme-dans-l-empire-perse-sassanide-fra_1904.txt` l.12268-12270), and Sabrisho helping the Henanians (l.12274-12275). Scher's note to the Cause says the same: "La plupart des notables de Nisibe ayant pris parti pour ce dernier, le roi Chosrau II ordonna à l'évêque de se rendre à Caëcar" (`barhadbeshabba_cause-de-la-fondation-des-ecoles-po4-syr-fra_scher1908.txt` l.16969-16971).

The governor clause predates this branch. The branch's fix to Open-Gaps 253, though, now names a held witness for it. The fix moved the misattribution instead of removing it.

Fix. Rewrite the sentence so each witness carries only what it holds. For example: "The church's synods of 585 and 596 condemned teaching that later writers took for his, without naming him. The Chronicle of Seert tells how Gregory, metropolitan of Nisibis, condemned Henana's books, how Henana found help at the king's court and the catholicos Sabrisho took his side, and how, when Gregory left the city, about three hundred students walked out." Drop "under the protection of the Persian governor". Check the story's `when` ("c. 596–602") against the result.

---

## SUBSTANTIAL

### S1. Liberatus is made to "tell of African bishops" (`latin-africa-under-byzantium`, documentedStories[0].caveat)

The new text: "Liberatus of Carthage tells of African bishops deposed and exiled for refusing to condemn the Three Chapters, without naming Reparatus."

Liberatus names no region, and he declines to tell: "quomodo consentientes episcopi in trium damnationem capitulorum muneribus ditabantur, vel non consentientes depositi in exsilium missi sunt, vel aliqui fuga latitantes ... quoniam nota sunt omnibus, puto nunc a me silenda" (`liberatus-victor-tunnunensis-primasius-junillus-pl68-lat_migne1866.txt` l.82406-82413, OCR normalized). "African" comes from Jean Garnier's note, not from Liberatus: "Muneribus ditabantur.] De suis Africanis loquitur, Reparato Carthaginensis, Firmo Numidiae, Primasio ..." (l.82524-82525). The new source note, "An African account of the bishops deposed, exiled or in hiding; it does not name Reparatus", is accurate.

Fix: "Liberatus of Carthage mentions bishops rewarded, deposed, exiled or in hiding over the Three Chapters, but passes over the details as well known. His editor Jean Garnier takes him to mean the Africans, Reparatus among them."

### S2. Philoxenus's dates line gives a death year the profile withholds (`philoxenus-of-mabbug`, `dates`)

The text: "bishop from 485; died c. 523". The brief says: "No early source used here gives the year he died. The editor François Nau puts the end of his time as bishop in 523." The card's dates note says the same. The held line is a term of office: "Philoxène (Xénaïas), évêque de Mabboug, de 485 à 523" (batch7 `records.json` l.493). The short line turns it into a death year.

Fix: "bishop 485-523, by Nau" or "bishop from 485; exiled 519". Keep `end` 523 as the map year.

### S3. Julian and Longinus are placed only at Constantinople (`julian-missionary-to-the-nobadae`, `longinus-bishop-of-the-nobadae`)

The text for both: `"region": "Constantinople"`, `"placeLabel": "Constantinople"`. The card place notes read: "Constantinople; the land of the Nobadae, beyond the Thebais" (Julian), and "...among the Nobadae on the eastern borders of the Thebais beyond Egypt; ... among the Alodaei, beyond the Nobadae" (Longinus). Their whole significance lies in Nubia, but the map line names only the city they set out from.

Fix: add the mission field to `region` and `placeLabel` ("Constantinople, the land of the Nobadae"; for Longinus also "the Alodaei"), with no id, as was done for "the Judean desert". The census already holds a "Nile Sudan" row (Q135028, Egypt and Sudan) on `nubian-christianity`. If the map slice judges "the land of the Nobadae" to fall within it, that row can be copied, and no id needs to be invented.

### S4. Tradition voices now contradict the new person cards beside them on the map panel (`nubian-christianity` voices[0]; `early-benedictine-italian-monasticism` voices[0])

- Nubian voices[0]: "Julian — the Miaphysite missionary who reached Nobadia in 543". The new Julian card's dates note says: "John of Ephesus gives no year." Julian's `start` 543 is marked SCAN in the build table. Open-Gaps 247 put this line on the coordinator ("the Julian line's 'Nobadia' is in no held file"), but the fix answered only the David and Gildas items of that bullet.
- Benedict voices[0]: "author of the Rule ... died around 547". The new Benedict entry says "c. 480-543", and its card says: "died, by the tradition of his order, in 543, as both give it."

The map's Voices list renders these lines (`cft-website/index.html` holds "died around 547" and "reached Nobadia in 543"). A reader sees two different years on one panel.

Fix: align the voices lines with the cards. For example: "Julian — the Miaphysite missionary to the Nobadae under Justinian and Theodora; his mission is known only through John of Ephesus's account". And: "Benedict of Nursia — author of the Rule and founder of Subiaco and Monte Cassino; his order's tradition gives his death as 543". Either finish the other 247 items (Theodosius "patriarch from 535"; Longinus "around 580"; "Nobadia") or carry them in Open-Gaps by name.

### S5. Isidore at Toledo IV: the fix leaves a dangling phrase and a stilted teaser (`nicene-visigothic-iberia` documentedStories[1])

The text: "In 633 the bishops of Spain met at Toledo in the fourth of the great councils, with Isidore of Seville's name first among the signatures, to legislate for church and kingdom together." The bishops did not meet "with his name first among the signatures": the signatures came at the end. The teaser has the same problem: "A council whose acts Isidore of Seville signs first declares forced baptism wrong". The fix is true to the acts: "I. Ego Isidorus in Christi nomine ecclesiae Hispalensis metropolitanus episcopus haec statuta subscripsi" (`collectio-canonum-ecclesiae-hispanae-toledo-iii-lat_1808.txt` l.40882-40884). But the writing now reads as a workaround, which the writing standard rules out.

Fix. Story: "In 633 the bishops of Spain met at Toledo in the fourth of the great councils, to legislate for church and kingdom together. Isidore of Seville's name stands first among their signatures." Teaser: "The bishops of Spain, with Isidore of Seville's name first on their acts, declare forced baptism wrong — and rule that ...". Brehaut's "probably also at the fourth of Toledo in 633" (`isidore-seville_encyclopedist-of-the-dark-ages-extracts_brehaut1912.txt` l.701-703) may be added as his view if wanted.

### S6. The Ladder sentence no longer says anything about legacy, and it hedges twice (`chalcedonian-monasticism-judean-desert-and-gaza`, `legacy`)

The text: "John Climacus wrote the Ladder of Divine Ascent at Sinai, in the later 500s or about 600, though his years are disputed." The "or" already states the uncertainty, so "though his years are disputed" hedges it a second time. The sentence also sits in the legacy paragraph without a legacy point. The new John Climacus card holds one: "Philippe Labbe says the Greeks held him in great value ... Elias of Crete, he says, wrote explanations of the Ladder."

Fix: "John Climacus wrote the Ladder of Divine Ascent at Sinai, in the later 500s or about 600. The Greeks held it in great value, Philippe Labbe says, and Elias of Crete wrote explanations of it."

### S7. The validator's rendering rule is looser than it needs to be (`tools/validate-census.mjs`, `declaredRendering`)

The rule skips any quotation that has "in modern words" within 120 characters on either side, in the same paragraph. It does not let anything through today: in the whole census it skips exactly 14 spans, and every one is a real rendering that I checked against its original (Faustus x3, Ruricius x3, Columbanus x2, Constantius, Isidore, Babai, Moschus x3). But a genuine English quotation in the sentence before or after a rendering would also be skipped. Columbanus's "Error is manifestly ancient" stands in a different paragraph only by chance. A meta sentence such as Isidore's "Their Latin is told here in modern words" exempts everything within its reach, and the rule applies to every prose field, cards included.

The older comment, about 15 lines above the new code, now contradicts the rule: "A narrator's retelling in modern words carries no quotation marks and is not checked here."

Fix at the root: list the renderings, as the scan readings are listed. Add a `tools/quote_renderings.json` that names each entry id, the rendered span and the original's file and lines. The check skips only a listed span and fails when a listed span no longer stands in the prose. A rendering then cannot enter unreviewed, and the review's check against the original is on record. At the least, narrow the reach to the quotation's own sentence. Update the old comment either way.

### S8. The audit file and the release records are not on the branch

`Build/Ministry/Operations/Audits/2026-11-14_cft-era3-live/Census_Text_Changes.md` does not exist; the folder did not exist until this review was filed. There is no Decision-Log entry for release 42 and no Open-Gaps entry carrying its items. Release 41's entry and Open-Gaps 249 set the pattern. Items that need a home include:
- The SCAN map years: Julian 543-545, Romanos 490-556, John of Beth Aphthonia 538.
- The unlinked 247 census-text items (S4).
- The 248 Reccared rows that call his subscription a profession of faith.
- No audio for the 79 entries.
- The tree-page 404 check after deploy.

Fix: write the changes file, with each old and new text and the Open-Gaps entry it answers, then the Decision-Log entry and the Open-Gaps carry, before the PR is marked ready.

---

## MINOR

### M1. The Maccurritae fix: one strong verb, one unbalanced summary, heavy repetition (`nubian-christianity` and its edge)

Mommsen writes "videntur intellegi Μακκοῦραι Mauretaniae Caesariensis (Ptolem. 4, 2, 19)" (`chronica-minora-2_...mommsen1894.txt` l.19879-19880, OCR "mdentur inlelleyi MuxxovQcti"). That means "they seem to be meant". "took them for" is a little firmer.

The relationsSummary gives only Mommsen's side: "Theodor Mommsen, its editor, took them for a people of Mauretania, not the Makurians of Nubia." The caveat and the edge rightly say "not settled".

The Mommsen clause appears five times across one entry and its edge, which reads mechanically. "John of Biclarum" survives in five source titles and loci, including the source list of the same Nubian story whose caveat now says "John of Biclaro".

Fix. relationsSummary: "...became Christian around 569. Whether these are the Makurians of Nubia is not settled; Theodor Mommsen, its editor, thought them a people of Mauretania." Shorten the source notes to "the Chalcedonian notice of the Maccurritae (see the caveat)". Make the spelling of John's name the same throughout.

### M2. Caesaria card: "heading" names the greeting (`caesaria-of-arles-the-elder`, card.uncertain)

The text: "Two letters of Caesarius are written to an abbess Caesaria. The heading of the second calls her a holy sister, and the first calls her a venerable sister in its opening words." The second letter's heading is "EPISTOLA II. AD EASDEM." The words "Caesariae sanctae sorori abbatissae" are its greeting (`facundus-ferrandus-caesarius-dionysius-pl67-lat_migne1865.txt` l.86729-86733). The first letter's "venerabilis in Christo soror" is right (l.86510-86511). The fix is otherwise true to the lines and answers the triage point.

Fix: "Two letters of Caesarius are written to an abbess, Caesaria. The second greets her as a holy sister, and the first calls her a venerable sister in its opening words."

### M3. Victor of Tunnuna card: one added source is misnamed (`victor-of-tunnuna`, sources)

"Endnote to the Life of Antony, in Nicene and Post-Nicene Fathers, second series, volume 4". The line is a footnote (`<note>`) inside section 91, "Of his sickness and his last will" (`npnf204_athanasius-select-works-letters.xml` l.33483, l.33519). Both additions are the right root fix, since the card already names "English notes in the Ante-Nicene and Nicene Fathers". The ANF item is the "Introductory Note" of Part I (`anf03_tertullian.xml` l.465).

Fix: "Note to section 91 of the Life of Antony, in ...".

### M4. Short dates lines that state flatly what the card hedges

None is wrong, but each drops the card's "probably", or picks one of several years without saying so:
- Benedict "c. 480-543": the year is his order's tradition.
- Cassiodorus "c. 480-575": Trithemius, through Hodgkin.
- Columbanus "c. 543-615": Munro's "probably 615".
- John of Ephesus "c. 507-586": Brooks's "probably died in 586".
- Marius "bishop 574-594": Mommsen's reckoning against Conon's 581 and Chifflet's 596.
- Theodosius "patriarch 535-566": Evetts gives 567.

Wording points:
- Ferrandus "6th c.; praised in 546" turns Victor's floruit notice into an event; "noted by Victor, 546" is closer.
- John of Biclaro "signs in 610": "A John of Gerona" is Mommsen's identification.
- Dionysius "c. 500-525; dead by 556" can be read as a life span followed by a contradiction; "at work c. 500-525; dead by 556" says what the card says.

Fix: add "c." to the end year where the card says "probably" or "about". Use "at work" or "signs as" where a line could be read as a life span or a settled identification.

### M5. Places and regions

- Severinus "Noricum · Naples": he never lived at Naples; the card says he was "buried at last in the Lucullan castle at Naples".
- John Rufus "Antioch · Jerusalem": this leaves out Maiuma, the see in his role line.
- `regions` is copied from the home tradition, so Vigilius (Rome) has only "Asia Minor", John Rufus (Antioch, Jerusalem) "Africa", and Constantius (Lyon) "North Europe". A region filter will miss them where they lived.

Fix: "Noricum" alone for Severinus; add Maiuma for John Rufus; derive `regions` from the person's own places where these disagree, or carry it with the map slice.

### M6. Placings outside the brief's list

- Constantius of Lyon in British and Welsh Christianity is weak. He was a man of Lyon who wrote of Germanus's British mission. Merovingian Gallic Christianity holds Avitus of Vienne and Ruricius, both of the same years and of non-Frankish kingdoms.
- Gennadius of Marseilles (wrote c. 480, died c. 496) sits in Gallic Monastic-Ascetic Christianity, whose census span ends at 450.

Both are defensible as the Lérins and Marseilles line. Each should be named in the release's Decision-Log entry, as Faustus is.

### M7. Two de-quotings could read better

- Victor of Vita brief: 'He calls Pampinianus the bishop "nostrae civitatis", of our city, and Karl Halm...'. The Latin is right (`mgh-aa-3_victor-vitensis-corippus-halm1879.txt` l.564; Halm's note "nostrae ciuitatis] i. e. Vitensis", l.604). Fix: 'the bishop "nostrae civitatis" (of our city)'.
- Moses of Khoren card: "The new Plato he says taught at Alexandria is Cyril..." loses the sense of a title. Langlois's French is "d'un nouveau Platon" (`langlois_collection-historiens-armenie-tome2-fra_1869.txt` l.24830). Fix: 'The "nouveau Platon", new Plato, he says taught...'.

### M8. Scan readings: all thirteen hold, but the "drop" entries check too little

Each reading was checked against its file and line:
- Every "scan" string is there as given.
- Each "reads" is the evident printed word (Procopio, culpabili, Caesariae matris, his, KINGS, dragon, of that, the, banishment, perform).
- Each drop range holds only a running head, signature or section marks, footnotes or a page number: Perry l.24124-24128; McCrindle l.7193-7206; Payne Smith l.13034-13042.

A drop, though, blanks the whole range after checking only that the named head is present. Text added to that range later would vanish unseen.

Fix: for a drop, also require that the range holds nothing but blank lines and the declared lines.

### M9. The Nisibis story carries two claims the new Henana card does not support (pre-existing; for Open-Gaps)

- "Henana died in his post around 610". The Henana card says Scher's notes "put his death under the catholicos Sabrisho, who died in 604, and elsewhere say he was still alive in 610". Nothing held says "in his post".
- The story's source "Statutes of the School of Nisibis (496 and 602)" sits beside the card's "Ignazio Guidi dates new school rules made while he was master to 590".

Fix: with B2, tell the death as the card does, and check the statutes' year.

### M10. Renderings: all fourteen checked, three small points

Each "in modern words" span was checked against its original:
- Faustus: Engelbrecht l.11049-11051, l.13403-13404 (letters to Lucidus and to Ruricius, headed l.10968, l.13393).
- Ruricius: l.23186, l.20044, l.23199-23201 (ep. II.33 to Caesarius, headed l.23175-23178; first letter to Faustus, headed l.20022-20027).
- Columbanus: PL 80 l.20763-20765.
- Isidore: PL 80 l.52558.
- Constantius: Levison l.4577-4579.
- Babai: Labourt l.15853-15854.
- Moschus: PG 87/3 l.10094-10095, l.3785.

All are faithful, clause by clause. The earlier helper's triage is confirmed on each point.

The Babai edit is a correct root fix: it drops the "and" the French lacks ("le Fils est mort, par le Fils tout a été créé et fait").

Three small points stand. Constantius's "Et tamen" ("and yet") is lost, and "Then he writes" does not carry the turn from his plea for pardon. Faustus loses "ergo". The Moschus speaker is Sophronius ("Et dixit mihi"), and "he said" after "Sophronius nodded" carries that.

Optional fix for Constantius: "Yet, he writes, in modern words, ...".

---

## Item 4: the build's placings

- **Boethius, told within none, Latin West: defensible.** He died in 524, before Justinian's reign. No census tradition holds him, and the only census line naming him is in the Homoian entry.
- **Procopius and Agathias, told within none, Greek East: defensible.** Both cards say "Outside the church" and carry the "Outside witness" label. They match the Sozomen precedent of release 41.
- **Columbanus, Insular / Irish Monastic Christianity: defensible.** He was an Irish peregrinus from Bangor, and that tradition already named him as a voice. Merovingian Gallic Christianity is the stated alternative.
- **Faustus of Riez, Gallic Monastic-Ascetic Christianity: defensible.** He was abbot of Lérins from 433, within the tradition's span. The Gallic monastic link note already uses him.
- **Samson of Dol, British and Welsh Christianity: defensible.** He was of Dyfed and trained at Llantwit, and the Breton church he served was British-founded.
- **Fulgentius of Ruspe, kept in Gothic, Vandal & Lombard Homoian Christianity: not defensible as built.** See B1.

## Item 6: AI tells and generic voice

The new dates lines are plain, and so are the new places and the David and Gildas voices. The David fix is good: "the British bishop whose Lives make him the preacher at the synod of Brefi; the annals put his death in 588 or 601" rests on the card's annals note. So is the Gildas fix ("written in the 540s"; Williams: "a few years after 540 and before 547"). The writing defects are the double hedge in S6, the dangling phrase in S5 and the five-fold Mommsen clause in M1. "In modern words" now stands 14 times across seven briefs, three times in Ruricius's five paragraphs. It is honest, and it is needed for fidelity, but it is close to a formula. Where a paragraph holds two renderings of one letter, one marker covering both is enough.

## Checked and found sound

- British-to-American spelling in every changed profile line. No quotation and no title changed; "colors", "skeptic", "councilor" and the rest are all in the profiles' own prose.
- The Barhadbeshabba title "with the Catalogue of Abdisho of Nisibis", and the checker's two names. The pattern is case-sensitive, and its new test proves the lowercase "catalogue" is still flagged.
- The Constantinople 553 tradition name now equals the census name "Antiochene Exegetical Christianity (Chrysostom-centered)".
- The Dioscorus `records.json` note. Basset l.14421-14437 tells the exile to Gangra with "Macaire ... évêque d'Edkou"; Budge v1 l.7430-7433 tells the banishment "to the island of GAGRA" with "Abba MACARIUS, bishop of the city of KAw".
- The Gildas, David, Faustus-abbot (Gennadius) and Henana-praise ("homme orné d'humilité", Cause l.21006) fixes, each against its held line.
- The council people lists.
- The people lists and voice links: only own-tradition rows were linked, as in release 41, and no older list was reordered.
