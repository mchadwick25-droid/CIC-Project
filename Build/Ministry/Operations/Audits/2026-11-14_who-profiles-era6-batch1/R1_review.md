# R1 review: era 6 batch 1

Round 1, the full checklist review, by four fresh Opus agents that had not seen the drafting, at full effort. Part A covers John Wyclif and the README; Part B, Thomas à Kempis and Geert Grote; Part C, Richard Rolle and Julian of Norwich; Part D, Meister Eckhart, Johannes Tauler and Henry Suso. At the coordinator's request (2026-11-14), Parts B, C and D also judged whether the briefs that score lowest on the grade scale read as flattened or choppy. Each part is given as its reviewer wrote it. In all, 8 blocking and 100 minor points.

## Era 6 Who batch 1, round 1 review: PART A

**Scope.** `john-wyclif` (brief, card, audio, its `records.json` entry) and the batch `README.md`, every claim in it checked against the batch files, the scan, the live census (`cic-website/data/world-census.json`, ids `john-wyclif`, `thomas-a-kempis`) and the sources it names. Branch `claude/who-profiles-era6-batch1` at d3b9aa04. No repo file edited; no web, paid or model call.

**Method.** I read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its 14-item checklist, lessons.md, the scan row (Who_Scan_Era6.md l.80) and the live `john-wyclif` entry. I opened every line the Wyclif records cite, with 20 or more lines around it. I re-verified every quotation by script (whitespace, case, hyphen-break and punctuation tolerant), then by eye where OCR breaks the match. I searched for false absences across all 1,771 files in `cic/texts/` with windowed, case-insensitive regexes, including OCR and variant spellings (Wyclif/Wiclif/Wicleff/Wickliff/Wyclyfe; Kempis/Gerson/Imitatione; Hampole/Rolle; Tauler/Thauler/Taulerus; Kempe/Margery). I scored the brief with `engine.m1.gates.grade_text`, compared the audio string to the brief, and checked card form and sentence lengths by script. For the README, I checked the word and score ranges against all eight briefs; the tradition reasoning against the census entries and the cards; the "beyond the scan" list against the scan row; the absence claims by corpus search; and the census-fix claim against `Open-Gaps.md` (no Wyclif or Kempis census entry for this batch).

**Files opened (cic/texts/).** VAUGHAN = `wyclif_tracts-and-treatises_vaughan1845.txt` (l.1-12, 70-115, 570-580, 648-665, 874-882, 1258-1275, 1884-1916, 1994-2005, 2112-2140, 2248-2258, 3670-3692, 3790-3880, 4024-4038, 4380-4570, 4634-4646, 4755-4768, 7250-7268); SHIRLEY = `fasciculi-zizaniorum_shirley1858.txt` (l.196-223, 648-665, 722-730, 737-805, 866-890, 970-978, 1041-1045, 1680-1740, 1825-1850, 2340-2392, 2603-2643, 2690-2760, 2845-2862, 4515-4600, 23350-23392, 27345-27420); F&M = `wycliffite-bible_forshall-madden1850.txt` (l.68-80, 930-1032, 2300-2325, 2400-2425, 3433-3437, 4069-4076); POLLARD = `pollard_fifteenth-century-prose-and-verse_1903.txt` (l.105-115, 205-226, 265-275, 820-850, 940-975, 1005-1020, 7196-7212); KNIGHTON = `knighton_chronicon-v2-lat_lumby1895.txt` (l.1-12, 1420-1432, 1630-1650, 1755-1775, 6005-6020, 16920-16975); WALSINGHAM = `walsingham_historia-anglicana-v2-lat_riley1863.txt` (l.120-128, 2178-2196, 10990-11045); TRIALOGUS = `wyclif_trialogus-lat_lechler1869.txt` (l.695-710, 1565-1575, 22395-22412, 22490-22520); MATTHEW = `wyclif_english-works-hitherto-unprinted_matthew1880.txt` (l.372-400, 2858-2870, 35735-35800); CIV = `wyclif_de-civili-dominio-liber-primus-lat_poole1885.txt` (l.1-10, 1905-1930); ARNOLD3 = `wyclif_select-english-works-v3_arnold1871.txt` (l.30700-30728); HUSLET = `hus_letters_workman-pope1904.txt` (l.40-46, 4504-4514); SCHAFF = `hus_de-ecclesia-the-church_schaff1915.txt` (l.138-145, 1500-1518); MANSI27 = `mansi_sacrorum-conciliorum-collectio-tomus-27-1409-1418-lat_welter-facsimile1902.txt` (l.64750-64792, 65525-65562); MIRBT = `mirbt_quellen-zur-geschichte-des-papsttums-3e-aufl-deu-lat_1911.txt` (l.14004-14012); FOXE3 = `foxe_acts-and-monuments-v3_cattley-townsend1837.txt` (l.1-12, 95-124, 4895-4993, 7905-8046). For the README: IGN-SCR1 = `ignatius-loyola_scripta-de-sancto-ignatio-tomus01-lat-spa-ita_1904.txt` (l.1-10, 9405-9434, 12305-12333, 24014, 24205-24347); NEALE = `neale_history-so-called-jansenist-church-of-holland_1858.txt` (l.4714-4722); `cell-of-self-knowledge_seven-early-english-mystical-treatises_gardner1910.txt` (l.505-585); `rolle_fire-of-love-and-mending-of-life_comper1914.txt` (l.1495-1515, 2120-2133, 5488-5543); `rolle_yorkshire-writers-enm_horstman1895.txt` (l.130-136, 2158-2163); `tauler_history-and-life-with-sermons_winkworth1907.txt` (l.905-925, 7171); `suso_life-of-blessed-henry-suso_knox1865.txt` (l.545-556); `ehrle-denifle_archiv-literatur-kirchengeschichte-mittelalters-bd2-deu-lat_1886.txt` (l.35586-35825); `diepenveen_het-klooster-van-diepenveen-dum_opzoomer1886.txt` (l.432-448); `kempis_opera-omnia-tractatus-lat_pohl1902.txt` (l.18858-18870, 19214-19222).

**Quotations.** All five quotations in the brief and card match their files.
- Brief: "naturally bread and wine, but sacramentally the body and blood of Christ." matches VAUGHAN l.4562-4563, with an OCR allowance ("naturalhj"). The full stop sits inside the marks in the file too.
- Brief: "substantially no evidence" matches POLLARD l.844.
- Card: "was holden of full many men, the greatest Clerk" matches POLLARD l.7204-7205. The OCR reads "Wyclipfb" just before; the quote stops before Pollard's "[Divine]".
- Card: "they could not burn" matches FOXE3 l.8044. The file runs on with a comma, so the full stop is rightly outside the marks.
- Card: "If considered only as the father of English prose, the great reformer might claim more reverential treatment at our hands." matches SHIRLEY l.2856-2858, with an OCR allowance ("tlie").

The Latin of Knighton, Walsingham, the Trialogus, the Urban letter, Mansi and Mirbt, and Matthew's Middle English, are told in modern words with no marks, as the ruling requires. Each modern telling was checked against its lines. One hedge is dropped (A-M12).

**Dates.** The brief's dates and their owners:
- 17 May 1382: VAUGHAN l.3808.
- 1845: VAUGHAN l.77.
- 1858: SHIRLEY l.223.
- April 1361: SHIRLEY l.884-886.
- February 1377: VAUGHAN l.2122-2127; SHIRLEY l.1686; F&M l.993.
- The 1377 bulls: SHIRLEY l.1728.
- Spring 1381: SHIRLEY l.2606.
- "That summer": VAUGHAN l.3796.
- 1850: F&M l.5290.
- 1903: POLLARD l.111.
- 29 December 1384 is the one problem, A-M7: the day is Shirley's, but his line reads "the same year" after a printed "1381" (SHIRLEY l.2743-2748). The year 1384 is F&M's (l.1030).

On the card, every date names its owner except the death sentence in `dates` (A-M10). No Library file header is used as a witness anywhere in the profile.

**Audio.** `audio/john-wyclif.audio.txt` is the brief exactly, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. It has two tags and nothing else changed. Pass.

---

### john-wyclif

**Verdict: two blocking findings (A-B1, A-B2). Otherwise passes with minor fixes.**

`grade_text`: FK 8.02, Flesch 64.69. 405 words, at the major cap. Audio pass.

**A-B1 (card `uncertain`, "The burning of his bones": a misread note, credited to the wrong owner).**
- Bad text: "He heads the decree A.D. 1425. Foxe's 1837 editors note that the council had not yet ordered the bones burned."
- Evidence: the note is at FOXE3 l.4990-4991: "(1) The bones of Wicklitf were not yet commanded by the council of Constance to be burned." It is not about the 1425 decree. It annotates the Oxford testimonial of 5 October 1406 (l.4902-4964), whose words "Neither was this doctor convicted of any heresy, nor burned of our prelates after his burial.^" (l.4952-4953) carry the mark. Its "not yet" means not yet in 1406.
- It is numbered with Foxe's own source notes on that page ("(2) Ex. 2. tomo operum Jo. Huss", l.4992) and carries no "— Ed.", unlike the editors' notes (l.4905-4913, 7962). So "Foxe's 1837 editors" is unsupported.
- Placed after the 1425 heading, the sentence tells the listener that the council had still not ordered a burning when Foxe dates one. The note says nothing of the kind.
- The council's decree, in Foxe's English, orders the body and bones "taken out of the ground, and thrown away far from the burial of any church" (l.7946-7948). Mansi has the same: "exhumari, & procul ab ecclesiastica sepultura" (MANSI27 l.65559-65561, OCR "provul ab ecm").
- Fix: "His heading for the decree gives A.D. 1425. In Foxe's own English, the council's decree orders the bones dug up and thrown far from any church burial. It says nothing of burning."
- Records: replace the witness FOXE3 l.4990-4991 with FOXE3 l.7946-7948 and MANSI27 l.65559-65561.

**A-B2 (records `absent_details`, "A contemporary friendly account of his life": a false absence).**
- Bad text: the note cites Shirley's "No friendly hand has left us any, even the slightest, memorial of the life and death of the great reformer" (SHIRLEY l.2753-2755) as the honest limit.
- Evidence: a held file the card already cites gives one. FOXE3 l.4902-4964 holds "The Public Testimony given by the University of Oxford, touching the great Learning and good Life of John Wickliff", dated "the fifth day of October, in the year of our Lord, 1406". It says "his conversation, even from his youth upward, unto the time of his death, was so praiseworthy and honest, that never at any time was there any note or spot of suspicion reported of him" (l.4946-4949).
- Its authenticity is disputed: the editors' note (4) begins "The enemies of Wickliff have endeavoured to overthrow the authenticity of this valuable" document, and refers the reader to Lewis's History (l.4914, 4982-4986).
- William Thorpe's 1407 words (POLLARD l.7204-7208) are a second friendly near-contemporary witness.
- Shirley's sentence is his own judgment, not an absence in the held texts.
- Fix: retitle the detail "A friendly account of his life from his own day". Note: "Shirley writes that no friendly hand left any memorial (SHIRLEY l.2753-2755). Foxe prints an Oxford testimonial of 5 October 1406 praising his learning and life, whose authenticity his enemies have disputed, his editors note (FOXE3 l.4902-4964, 4914, 4982-4986). Thorpe's 1407 tribute is in POLLARD l.7204-7208. Not told in the brief."

**A-M1 (brief para 1: "such heretics" can be heard the wrong way round).**
- Bad text: "In his Latin dialogue Trialogus, Wyclif called it the friars' earthquake council. When Christ's members fail to cry out against such heretics, he wrote, the earth cries out."
- Evidence: the sentence before is "twenty-four points drawn from Wyclif's writings were condemned". A listener can take "such heretics" for Wyclif's side. Wyclif means his judges: "isti haeretici tam expresse Christo contrarii … in ista damnatione … Quando enim membra Christi deficiunt ad reclamandum contra tales haereticos, terra clamat" (TRIALOGUS l.22511-22517).
- The records claim still says "hence 'he wrote of his judges'", which the brief no longer says.
- Fix: "In his Latin dialogue Trialogus, Wyclif called it the friars' earthquake council, and called his judges the heretics. When Christ's members fail to cry out against them, he wrote, the earth cries out." Bring the records claim into line.

**A-M2 (brief para 1: the witness came loose from "drawn from Wyclif's writings").**
- Bad text: "…and twenty-four points drawn from Wyclif's writings were condemned."
- Evidence: the sentence sits in Vaughan's account. Vaughan says only that twenty-four conclusions "were read, as those which had been preached 'generally, commonly, and publicly'" (VAUGHAN l.3836-3838). He adds that some had "received a partial colouring from the ignorance or" malice of his enemies (l.3868-3870).
- "Extracted from his writings" is Shirley's phrase (SHIRLEY l.2697-2699).
- Fix: "…and twenty-four conclusions were condemned. They were drawn from Wyclif's writings, Shirley says."

**A-M3 (brief: the who-line comes late, at sentence 8).**
- Evidence: sentences 1 to 7 never say who Wyclif was. The first word on him is "He finds Wyclif at Oxford as master of Balliol College in 1361" (para 2, sentence 2). Era4 b6 A-M27 was the same fault.
- Fix, in sentence 1: "…to judge the teaching of John Wyclif, an Oxford doctor of theology and rector of Lutterworth."
- Witnesses: KNIGHTON l.16933-16935 ("rector ecclesie de Lutturworthe … doctor in theologia"); SHIRLEY l.1043-1044.
- If "rector" is kept, see A-M20.

**A-M4 (brief para 3: "bulls" is undefined and is misheard).**
- Bad text: "Pope Gregory XI sent bulls that condemned nineteen of his conclusions and ordered his arrest."
- Evidence: a listener hears the animal. The pattern's undefined-term rule and "words a listener mishears" (era4 b4 C-M4) apply.
- Fix: "Pope Gregory XI sent letters, called bulls, that condemned nineteen of his conclusions and ordered his arrest."

**A-M5 (brief paras 4 and 5, card `remembered`: the chronicle's author is told as settled, while the card's own item contests it).**
- Bad text: "Henry Knighton, a Leicester chronicler hostile to Wyclif, calls John Ball…"; "Knighton also complains…". The card has "Henry Knighton, a Leicester chronicler hostile to him, still calls him…".
- Evidence: the card's item "Who wrote the Leicester chronicle" and records contested_claim 10 give Shirley's "pseudo-Knighton" and "the so-called Knighton" (SHIRLEY l.2369, 2722-2726) against the manuscript title (KNIGHTON l.1427-1428).
- Precedent: era4 b8 R3-M6, an identification told as settled.
- Fix for the brief: "A Leicester chronicle that bears the name of Henry Knighton, and is hostile to Wyclif, calls John Ball, a priest among that summer's rebels, Wyclif's forerunner." Then "The chronicle also complains…" and "So the gospel's pearl, it says, is trodden by swine."
- Fix for the card: "The Leicester chronicle under Henry Knighton's name, hostile to him, still calls him…"

**A-M6 (brief para 4: "Vaughan rejects the charge." names the wrong charge, and it is a beat line).**
- Evidence: Knighton's charge is that Ball was Wyclif's forerunner "veluti Christus Johannem Baptistam, qui vias suas in talibus opinionibus praeparavit" (KNIGHTON l.16944-16947), a forerunner in opinions.
- What Vaughan rejects is something else: Wyclif "was not the man to become the agent of insurrection, after the fashion of John Ball and Wat Tyler, as some of his ingenuous opponents have insinuated" (VAUGHAN l.7262-7264). He does not answer Knighton.
- Fix: "Vaughan denies that Wyclif was an agent of the rising, as some of his opponents hinted." This matches the card's own item.

**A-M7 (brief para 6: the year is told as Shirley's, and Vaughan's side of a recorded dispute is missing while the live census tells it).**
- Bad text: "On 29 December 1384, Shirley says, a stroke took his speech as he heard Mass in his parish church. He died two days later."
- Evidence: Shirley gives "On the 29th of December of the same year". His "same year" follows "The citation did not reach him till 1381" (SHIRLEY l.2712-2713, 2743-2748), a print or OCR slip. The year 1384 is F&M's: "the last day of December 1384" (F&M l.1030). The README itself says so.
- The records contested_claim "How and where he was struck" holds Vaughan's "he is said to have been employed in administering the bread of the eucharist" (VAUGHAN l.4761-4763). The live census tells exactly that as fact: "as he gave out the bread at Mass".
- Fix: "On 29 December, Shirley says, a stroke took his speech as he heard Mass in his parish church. Vaughan reports that he was said to be giving out the bread. He died on the last day of 1384, Forshall and Madden write."
- This adds about 20 words, and the brief is at the 405 cap, so the drafter must cut elsewhere. One candidate is para 2's "The crown gave him the parish of Lutterworth.", which A-M3 makes redundant.

**A-M8 (brief, closing line: a rhetorical question heard in the narrator's voice).**
- Bad text: "Christ and his apostles, he answered, taught the people in the tongue best known to them. Why should men not do so now?"
- Evidence: the question is Wyclif's ("why shulden not men do nou so?", MATTHEW l.35793-35795), but it stands alone with no attribution and closes the brief. It is heard as the narrator's flourish.
- Fix: "Why should men not do so now, he asked."

**A-M9 (brief para 5: a scholar with no role).**
- Bad text: "Alfred Pollard, in 1903, says…"
- Evidence: the rule is that every scholar gets a role and a time (era4 b8 Y-M4). POLLARD l.111 and title.
- Fix: "Alfred Pollard, who edited fifteenth-century English prose in 1903, says…"

**A-M10 (card `dates`: the death sentence has no owner).**
- Bad text: "Struck by paralysis on 29 December 1384, he died on the last day of that December."
- Evidence: every other sentence in the field names its witness, and the README promises that "the cards… say whose they are". The day is Shirley's and Vaughan's (SHIRLEY l.2748; VAUGHAN l.4764-4765); the year and "last day" are F&M's (l.1030).
- Fix: "Struck by paralysis on 29 December, Shirley and Vaughan say, he died on the last day of December 1384, as Forshall and Madden date it."

**A-M11 (card `dates` and `uncertain` "When he was born", records contested_claim "Birth year": a held witness is missing).**
- Evidence: F. D. Matthew, already on the card, writes: "The date and place of Wyclif's birth are alike uncertain. Of the date all we know is that he died in 1384, and that he was then an old man… We may place it somewhere about 1320." (MATTHEW l.380-384). He also gives Leland's Spreswell and Wycliffe-on-Tees for the place (l.384-390).
- The card gives only 1324 and Shirley's doubt.
- Fix: add to the item: "F. D. Matthew, in 1880, calls the date and place alike uncertain and places his birth about 1320." Add Matthew as a side of the contested claim, and add a claim with witness MATTHEW l.380-390.

**A-M12 (card `uncertain` "How he was struck": Walsingham's hedge is dropped).**
- Bad text: "Thomas Walsingham, hostile, says God struck him as he meant to preach against Saint Thomas of Canterbury on his feast."
- Evidence: "dum in Sanctum Thomam, ut dicitur, eodem die in sua praedicatione … vellet evomere" (WALSINGHAM l.11025-11028, OCR "codcm"). The "as is said" covers the intent to preach against Thomas.
- Precedent: era4 b2 C-M5.
- Fix: "…says God struck him as, it was said, he meant to preach against Saint Thomas of Canterbury on his feast."

**A-M13 (card `uncertain` "The hearing at St Paul's": Vaughan's qualifier is dropped).**
- Bad text: "Vaughan dates it 19 February 1377, Shirley 23 February."
- Evidence: "The nineteenth day of the same month was fixed for the hearing of his defence" (VAUGHAN l.2125-2126). That is a set day, not a reported one. Shirley: "on the 23d of February, Wyclif appeared" (SHIRLEY l.1685-1686).
- Fix: "Vaughan says the hearing was set for 19 February 1377. Shirley says he appeared on 23 February."

**A-M14 (card `remembered`, Foxe: no witness for "Protestant", and process register).**
- Bad text: "John Foxe was a Protestant historian of the martyrs; his editors cite his editions of 1559 and 1563."
- Evidence: no records claim gives a line for "Protestant historian". "His editors cite his editions" narrates the edition's apparatus (FOXE3 l.7962, "See the edition of 1563, p. 105, and the Latin edition of 1559, p. 23.— Ed.").
- Fix: "John Foxe told the story in his book of the martyrs, in Latin in 1559 and in English in 1563, his 1837 editors note." Add a records claim with witnesses FOXE3 l.7962 and the running head "MARTYRS AND EXILES FOR THE TRUTH" (l.8023, OCR "MAKTYRS"). If "Protestant" is kept, it needs a held line.

**A-M15 (card `traces`, Hus: the sentence is 33 words).**
- Bad text: "Jan Hus of Prague, in a sermon of probably 1408, hoped his soul would be where Wyclif's soul rests, Herbert Workman and R. Martin Pope report in their 1904 edition of his letters."
- Fix: "Jan Hus of Prague, in a sermon of probably 1408, hoped his soul would be where Wyclif's soul rests. Herbert Workman and R. Martin Pope report it in their 1904 edition of his letters."

**A-M16 (card: names with no identifier at first card mention).**
- "Thomas Arnold, who edited his English works" (keyWorks). The famous Thomas Arnold is the Rugby headmaster. The editor has no time on the card.
  - Fix: "Thomas Arnold, who edited his Select English Works in 1871" (ARNOLD3 title, l.73).
- "They call John Purvey's authorship of the later revision undeniable" (uncertain, item 1). Purvey is never identified.
  - Fix: "They call it undeniable that John Purvey, who lived with Wyclif in his later years, made the later revision" (F&M l.3435-3436, 4071-4075).

**A-M17 (card `remembered`, Thorpe: a quoted word whose modern sense misleads).**
- Bad text: "…the greatest Clerk" they then knew.
- Evidence: a listener hears an office clerk. Pollard glosses it "[Divine]" (POLLARD l.7205). CLAUDE.md asks for no word whose modern sense misleads. The quote stays; the narrator can gloss it.
- Fix: "He told Arundel that Wyclif "was holden of full many men, the greatest Clerk" they then knew, a word Pollard glosses as divine, a scholar of theology."

**A-M18 (card `sources`: form).**
- "English (modernised)" and "English and Middle English (modernised)" use British spelling outside a quotation (era4 b7 B-M2). Fix: "modernized".
- The Mansi entry has no author and no date, where both apply. Fix: author "Giovanni Domenico Mansi (ed.)" if a held line names him, otherwise leave author out; date "1902 (facsimile)", from the file's own imprint.

**A-M19 (card `sources.ownWords`: the brief's book on civil lordship is missing).**
- Evidence: brief para 3 rests on De civili dominio ("prima, quod nemo ut est in peccato mortali habet iusticiam simpliciter ad donum Dei", CIV l.1914-1915). The card's sources omit it.
- Fix: add `{ "title": "De Civili Dominio, book 1", "author": "John Wyclif; Reginald Lane Poole (ed.)", "date": "1885", "language": "Latin", "file": "cic/texts/wyclif_de-civili-dominio-liber-primus-lat_poole1885.txt" }`.
- Also in the brief: "God's gifts" → "God's gift" ("donum", singular).

**A-M20 (card: one term for one office).**
- Evidence: `knownFor` says "rector of Lutterworth" and `role` says "parish priest of Lutterworth". "Rector" is undefined for a listener.
- Fix: use "parish priest of Lutterworth" in both, or "rector, the parish priest, of Lutterworth" once.

**A-M21 (card `uncertain`: four labels name a topic, not the question).**
- Evidence: "The rising of 1381.", "The hearing at St Paul's.", "The papal letters." and "The burning of his bones." name a topic, not a question. Precedent: era4 b2 D-M16.
- Fix: "Whether he had a part in the rising of 1381.", "The date and aim of the St Paul's hearing.", "When the papal letters were issued.", "When and how his bones were burned."

**A-M22 (records: a range is off).**
- The Merton claim cites SHIRLEY l.870-871, which is a page head. The words "was, almost certainly, another man of the same name, who died rector of a living in Sussex in 1383" are at l.874-875.
- Fix: l.874-875.

**A-M23 (records `absent_details` "A birth year of 1330": misstates the census).**
- Bad text: "The census year c.1330 appears only in Library file headers".
- Evidence: the live entry's dates are "c. 1360-1384", start 1360. The c.1330 is the scan's (Who_Scan_Era6.md l.80), as the README rightly says.
- Fix: "The scan's year c.1330 appears only in Library file headers…"

**A-M24 (records: two card or brief words have no witness).**
- "William Courtenay": every records line gives Vaughan's "Courtney". The first name and spelling are Lumby's: "William Courtenay, Archbishop of Canterbury" (KNIGHTON l.6014-6015). Add the witness.
- Foxe's "Protestant": see A-M14.

### README.md

**Verdict: one blocking finding (A-B3). Otherwise passes with minor fixes.**

**A-B3 (Kempis bullet: a false absence).**
- Bad text: "No held line says what the census says about copies or about Ignatius's desk, so the profile does not."
- Evidence: IGN-SCR1 holds the desk. In Oliver Manare's reply to Lancicius's questions ("Responsio P. Manarei ad P. Lancicii postulata", page heads l.24014, 24289), l.24341-24347 read: "in cubiculo suo secretiori ordinarie super mensam alios libros non habebat, quam nouum Testamentum et Thomam de Kempis, quem solebat appellare perdicem librorum spiritualium."
- In modern words: in his inner room he kept on the table no other books than the New Testament and Thomas à Kempis, whom he called the partridge of spiritual books.
- On copies, NEALE l.4717-4721 adds to the "read more widely" line the census-like claim that the Imitation "has, it is said, gone through as many editions as there have been months since it first appeared".
- The same false absence sits in `records.json`, `thomas-a-kempis.absent_details`, "Ignatius keeping the Imitation on his desk" ("no line in the Ignatius volume or elsewhere was found for it"). That is Part B's profile; flagged here so it is fixed with the README.
- Fix: "Ignatius's desk is held: Oliver Manare's reply to Lancicius says Ignatius kept only the New Testament and Thomas à Kempis on his table (IGN-SCR1 l.24341-24347). No held line says 'most copied'; Neale gives 'as many editions as… months', with 'it is said' (NEALE l.4719-4721)." Then either tell the desk line on the Kempis card, with Manare named, or record why it is not told.

**A-M25 (para 2: the census-fix log the README claims does not exist).**
- Bad text: "…their profiles agree with the live entries except where the held lines differ; those points are logged in Open-Gaps for a census fix".
- Evidence: `Open-Gaps.md` has no entry for this batch, and none names the Wyclif or Kempis census text. Precedent: era3 b6 B-M13.
- Fix: log an Open-Gaps entry before the README says so. Owner: the coordinator, for a census fix. The Wyclif points it should carry:
  1. Live: "On 29 December 1384, as he gave out the bread at Mass, he was struck by paralysis." This tells Vaughan's "he is said to have been employed in administering the bread" (VAUGHAN l.4761-4763) as fact. Shirley has him hearing Mass (SHIRLEY l.2748-2749).
  2. Live: "In 1374 he went to Bruges… The crown then gave him the parish of Lutterworth." Shirley and F&M put the presentation in April 1374, before Bruges (SHIRLEY l.2376-2377; F&M l.979-983). Vaughan puts it about November 1375 (VAUGHAN l.1999-2004).
  3. Live: "In June 1377 the pope sent letters" tells Vaughan's month as settled. Shirley gives 30 May (l.1728) and F&M 11 June (l.995-996).
  4. Live: "His 1845 editor says Balliol College chose him…" uses a role for a named witness. Name Robert Vaughan (VAUGHAN l.1264-1266).
  5. Live: "From about 1360 he argued there against the friars" drops Vaughan's hedge, "The year 1360 has been mentioned as that in which Wycliffe became distinguished" (VAUGHAN l.1260-1262).
  - The Kempis points (the desk; "most copied") follow A-B3.

**A-M26 (para 3: a score range is stale).**
- Bad text: "Flesch Reading Ease 64.7 to 81.3".
- Evidence: `grade_text` gives henry-suso 81.46.
- Fix: "64.7 to 81.5". The words (395 to 405) and grade (5.3 to 8.0) hold.

**A-M27 ("Held witnesses beyond those the scan cites", Wyclif: overclaimed).**
- Evidence: the scan row (Who_Scan_Era6.md l.80) already cites most of them: WYC-TRI "(Trialogus, Lechler's prolegomena first)", WYC-MAT, WYC-ARN1/2/3, HUS-CH (Schaff), HUS-LET (Workman and Pope), MANSI27, WYCBIB (Forshall and Madden), and KNIGHT and WALS ("hostile chroniclers").
- Beyond the row are only Shirley's Fasciculi, Pollard, Mirbt and Foxe.
- Fix: "Wyclif. Shirley's introduction to the Fasciculi Zizaniorum, its Carmelite narrative and its Latin letter to Urban VI; Pollard's introduction and Thorpe's Examination; Mirbt on Inter cunctas; Foxe."

**A-M28 ("Card traditions": two reasons are untrue).**
- Grote: "his conversion and preaching fall in its years". The Grote card dates the turn to 1374, by Grube. That is before the entry's c. 1380.
  - Fix: "his preaching and the first houses fall in its years; his conversion, which Grube dates 1374, comes just before".
- Eckhart: "Eckhart's birth and Paris years fall before". The only Paris year on the card is Evans's list of 1302, inside c. 1300 to 1400.
  - Fix: "Eckhart's birth falls before; his Paris mastership of 1302 and his trial fall inside".

**A-M29 (Eckhart bullet: "as are the questions the card lists as uncertain").**
- Evidence: three of the card's uncertain items carry no Contested tag:
  - "His death": Widely Accepted.
  - "His offices before 1326": Inferential-Thin.
  - "The bull's numbers": Documented.
- Only the retraction, birth, Frankfurt and "before 1326" items have contested_claims.
- Fix: "His retraction, his birth, the Frankfurt priorate and an accusation before 1326 are tagged Contested."

**A-M30 (quotation paragraph: incomplete).**
- "Quotation marks are kept for held English: …Vaughan's and Pollard's Wyclif" omits the Wyclif card's quotations of Shirley and Foxe, and the Kempis card's quotation of Neale.
- "Lines held only in Latin, German or Dutch are told in modern words" omits Middle English. Matthew's Middle English tract is told in modern words in the Wyclif brief.
- Fix: add "Shirley's and Foxe's Wyclif, Neale's Kempis", and "Lines held only in Latin, German, Dutch or Middle English are told in modern words".

**A-M31 (Names and ids, Wyclif: misdescribes the card).**
- Bad text: "The card gives the Merton fellow and the warden of Canterbury Hall to another man of the same name, after Shirley."
- Evidence: the card sets Vaughan and F&M (all three posts his) against Shirley (another man). It does not decide.
- Fix: "The card sets Vaughan and Forshall and Madden, who give him Queen's, Merton and Canterbury Hall, against Shirley, who gives the Merton fellow and the Canterbury Hall warden to another man of the same name."

README claims checked and found true:
- Eight profiles, none written before, and the 2026-11-14 ruling (Decision-Log l.2817).
- All eight are "yes" in the scan's Major column, and the map caps hold.
- Wyclif: 1324 with Shirley's "vague conjecture"; the death year from F&M; Vaughan's OCR-garbled year (l.4765); F&M's Baruch and Pollard's Daniel.
- Rolle: COMPER 2129-2131 is the Office quoting him, and his own account is at l.5493-5541; the 29 September death day is Horstman's alone (searched); the Hampole nuns prepared the Office (COMPER l.1497).
- Julian: her text never names her (searched); Margery Kempe's visit is in no held file (Gardner's Kempe extract has no visit; searched).
- Eckhart: the bull condemns and does not excommunicate (no "excommunic" in the bull, Denifle l.35586-35825); the 22 February act shows him present.
- Tauler: the death day is Winkworth's alone (searched; WINK l.7171); her hearers' notes and the eighty-four sermons (l.905-925); three held birth years (with McCann's 1300 also held, which changes nothing).
- Suso: Stagel's writing by stealth and the burning (Knox l.545-556).
- Grote: "wonende toe GroUe" belongs to Hermen Sticke (Opzoomer l.442); Engelhusen's lay rule, by Langenberg.
- The file table, and the audio description.

### records.json (these profiles)

`john-wyclif` has 48 claims, 10 contested_claims and 4 absent_details.
- Every Contested tag has a contested_claim behind it: the Bible, Lutterworth, the bulls, the rising, birth, Walsingham, the early Oxford years, the 1382 appearance, and Knighton.
- Confidence tags fit. Lechler's dating is DMR, named as his. Schaff's is DMR. Pollard's view is Contested.
- The ranges I opened cover their quoted text except SHIRLEY l.870-871 (A-M22).
- OCR forms are flagged in parentheses, evenly. Knighton's "conculeatur" is marked "[OCR, conculcatur]".
- Faults: the stale "he wrote of his judges" (A-M1); the misread Foxe note (A-B1); the false-absence detail (A-B2); the c.1330 "census" wording (A-M23); the missing witnesses for "William Courtenay" and "Protestant" (A-M24, A-M14); the missing Matthew side of the birth claim (A-M11).
- The absent detail on the burning searched cic/texts for "1428", "Fleming" and "Swift". I re-ran it over all 341 files that name Wyclif and found nothing: a true limit.

### Checklist summary

| # | Item | john-wyclif |
|---|---|---|
| 1 | Each sentence sourced | fail (A-B1); minor (A-M2, A-M6, A-M14) |
| 2 | Quotes verbatim | pass |
| 3 | No invention | pass |
| 4 | Reading aids | minor (A-M1, A-M4, A-M8, A-M15, A-M17, A-M20) |
| 5 | Named witnesses | minor (A-M9) |
| 6 | Partisan witness marked | pass |
| 7 | Contested claims both sides | minor (A-M5, A-M7, A-M11, A-M12, A-M13) |
| 8 | Common names | minor (A-M16) |
| 9 | One term for one thing | minor (A-M20) |
| 10 | Story, scene, disputes in place, length | minor (A-M3, A-M7); 405 words, at cap |
| 11 | Readability | pass (FK 8.0, Flesch 64.7) |
| 12 | Card order, fields, caveat repeated | minor (A-M10, A-M18, A-M19, A-M21) |
| 13 | Audio tags | pass |
| 14 | Who test | pass |

Records (A-B2, A-M22 to A-M24) and README (A-B3, A-M25 to A-M31) are outside the 14 items and are counted below.

### Count

- **Blocking: 3.** A-B1 (Wyclif card: the misread Foxe note), A-B2 (Wyclif records: the false absence of a friendly account), A-B3 (README: the false absence of Ignatius's desk; the same fault sits in the Kempis records).
- **Minor: 31.** A-M1 to A-M24 (Wyclif brief, card, records), A-M25 to A-M31 (README).

| Profile | Words | FK | Flesch | Blocking | Minor |
|---|---|---|---|---|---|
| john-wyclif | 405 | 8.0 | 64.7 | 2 | 24 |
| README.md | n/a | n/a | n/a | 1 | 7 |

**Scores.** john-wyclif `grade_text`: fk 8.020, fre 64.689. The batch range by the same gate: words 395 to 405; FK 5.3 to 8.0; Flesch 64.7 to 81.5.

**Files reviewed (absolute paths)**
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/README.md
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/john-wyclif.brief.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/john-wyclif.card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/audio/john-wyclif.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/records.json
- /home/user/CIC-Project/cic-website/data/world-census.json
- /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-12_who-scan-era6/Who_Scan_Era6.md
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md


---

## Era 6 Who batch 1, round 1 review: PART B

**Scope.** `thomas-a-kempis` and `geert-grote`: brief, card, audio script and their `records.json` entries, with the README lines that speak of them, their agreement with each other (names, dates, spellings), and, for Kempis, the live census entry `thomas-a-kempis` in `cic-website/data/world-census.json`. Held to the batch rulings: the Imitation's authorship is Contested and told so; quotation marks only around held English; Latin, German and Dutch told in modern words with the source named. No repo file was edited.

**Method.** Read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), `Who_Profile_Pattern.md` and its 14-item checklist, the lessons file, and the scan rows for Kempis (l.81) and Grote (l.89). Opened every line range the records cite for every brief and card claim and read 20 to 60 lines around each. Every quotation in both briefs and every card string was checked by script against the cited file (normalized for case, whitespace, punctuation and hyphen line-breaks); punctuation at the quotation edges was then checked by eye. False-absence sweep: every "alone", "only", "never", "no line", "no year" and "not among" was searched across all of `cic/texts/` with case-insensitive, whitespace-tolerant patterns and OCR variants (Stuerman/Sturman/Stuurman, Groote/Groot/Grote/Gerijt/Gherd, Heusden/Huesden, Pohl/Iosephus, pulsum/pestil/plague, "in common"/"common life"/"common table", "desk", "most copied"). `grade_text` run on both briefs; sentence lengths counted by script on briefs and card strings. Audio diffed against the brief. The coordinator's added check (whether FK 6.7 and FK 5.7 read as flattened or choppy) was answered by reading each paragraph for lost connections; findings are raised only where the writing suffers (K-M2, K-M6, G-M2).

**Files opened (cic/texts/).** CHRON = kempis_chronicle-of-mount-st-agnes_arthur1906.txt (l.228-302, 326-450, 1040-1110, 1180-1200, 1695-1745, 1880-1926, 1975-2032, 2325-2386, 3385-3440, 3740-3900); FOUNDERS = kempis_founders-of-the-new-devotion_arthur1905.txt (l.392-400, 1020-1034, 1165-1195, 1505-1545, 1568-1578, 1600-1622, 2060-2110, 2168-2195, 2296-2312, 2745-2775, 2862-2895, 3768-3780, 3805-3835, 3878-3892, 3940-3982, 4220-4226, 4600-4610, 5088-5150, 5545-5580, 5960-6010, 6262-6296, 8940-9026, 11030-11045, 12770-12830); BUSCH = busch_chronicon-windeshemense-lat_grube1886.txt (l.306-312, 1552-1565, 4510-4518, 4800-4813, 5338-5348, 5400-5432, 14894, 15000-15030, 15234-15260, 15345-15372, 15618-15660, 15680-15770, 15800-15820, 15905-15950); BENHAM = kempis_imitation-of-christ_benham1886.txt (l.480-540, 615-668); INGRAM = kempis_earliest-english-translation-de-imitatione-christi-enm_ingram1893.txt (l.1-12 header, 150-200, 240-265, 298-325, 386-412, 1168-1192); NEALE = neale_history-so-called-jansenist-church-of-holland_1858.txt (l.366-372, 3680-3760, 3760-4040, 4655-4690, 4698-4740); IGN = ignatius-loyola_exercitia-spiritualia-et-directoria-lat-spa_1919.txt (l.1-15 header, 1900-1910, 2594-2608, 2638-2646, 3066-3076, 3098-3104, 25082-25094); WESLEY = wesley-j_journal-v1_curnock1909.txt (l.940-970); NOVICES = kempis_sermons-to-the-novices-regular_scully1907.txt (l.240-256); LYD = kempis_st-lydwine-of-schiedam_scully1912.txt (l.115-132, 244-256, 1350-1356); DUTHOIT = kempis_prayers-and-meditations-on-the-life-of-christ_duthoit1904.txt (l.1-4 header, 47, 574-606, 738-750); POHL = kempis_opera-omnia-tractatus-lat_pohl1902.txt (l.1-6 header, 110, 18000-18018); the other Pohl volumes (title lists only, for the Vita Gerardi); GROOTE = groote_epistolae-xiv-lat_acquoy1857.txt (searches); LANG = langenberg_quellen-und-forschungen-niederdeutschen-mystik-gml_1902.txt (l.156-164, 482-492, 2058-2072, 2155-2200); DIEP = diepenveen_het-klooster-van-diepenveen-dum_opzoomer1886.txt (l.436-500); RUUS (searched).

**Quotations.** All 14 quoted strings in the Kempis brief and card and all 10 in the Grote brief and card match their files verbatim under the normalization (FOUNDERS, CHRON, BENHAM, INGRAM, NEALE, WESLEY, RUUS). No quotation needs an OCR allowance: every quoted line is clean in its file. One edge-punctuation fault: K-M4. Non-English lines (Busch's Latin, the Spanish of Ignatius, the Diepenveen Dutch, Grube's German, Pohl's Latin, Acquoy's Latin, Langenberg's German) are all told in modern words without quotation marks, as the ruling requires.

**Dates.** Kempis: 1399 (CHRON l.1097-1104), 1406 (CHRON l.1189-1193), 1424 (CHRON l.1706-1709; BUSCH margin l.5345 "U24"), 1429 (CHRON l.1885), 1471 and the ninety-second year (CHRON l.3392, 3413-3416), Neale's 1400 and 1417/1459 (NEALE l.4704-4711), Benham's c.1380 and 1439 (BENHAM l.492-493, 506-510), Duthoit's 1413 (DUTHOIT l.739-740), the Dublin note's 1380 and 25 July 1471 (INGRAM l.260-261), Atkynson 1504 (INGRAM l.174-177): all as the card gives them, each with its owner, except the drift in K-M7 and the gaps in K-M8 and K-M9. Grote: 1384, St Bernard's day, the forty-fourth year (CHRON l.3783-3787; BUSCH l.15929-15936), Busch's 1464 (BUSCH l.15009-15012, in the Liber de origine, l.14894), Arthur's 1340 (FOUNDERS l.399), Opzoomer's 1340 (DIEP l.467), Grube's 1374 (BUSCH l.310): as given, each with its owner. No Library header is used for a date in either profile. One header is used for a name (K-M11).

**Audio.** Both audio scripts are the brief exactly, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and no other tags (diffed by script).

---

### thomas-a-kempis

**Verdict: passes with minor fixes. No blocking finding.** The Imitation's authorship is told as Contested in the brief (Busch, Atkynson, Benham, Ingram, each named, none settled) and on the card (three items, both sides named), with a `contested_claim` behind it.

**K-M1 (brief, para 1: the subject's common name without an identifier at first mention).**
- What is wrong. "As a schoolboy at Deventer, Thomas sang in the church choir." "Thomas" is a common name, and the identifier does not come until the next paragraph. The pattern applies the first-mention rule to the subject's own name (lessons §9, era3 b6 B-M9).
- Evidence. The full name first appears at para 2, sentence 1.
- Fix: "As a schoolboy at Deventer, Thomas à Kempis sang in the church choir." Then para 2 opens "He tells this in his Lives of the founders of the New Devotion." (See K-M2, which rewrites para 2.)

**K-M2 (brief, para 2: five unconnected facts in a row; writing suffers).**
- What is wrong. "Thomas à Kempis tells this in his Lives of the founders of the New Devotion. Geert Grote began that movement in the Low Countries before his death in 1384. Thomas's Chronicle names him Thomas Hemerken, of Kempen in the diocese of Cologne. He lived about a year in the brothers' house at Deventer. "Here indeed I learned to write," he says." Book, founder, name, lodging and writing follow each other with no link, and the paragraph breaks the one-idea rule. This is where the brief's low FK comes from and where it reads flat. The link the source gives, that Florens placed him in the house, is dropped, although it carries on the scene from para 1.
- Evidence. FOUNDERS l.12808-12812: "by the aid and counsel of Florentius, I also took up my abode in this house, and continued in the Community for about a year".
- Fix: "He tells this in his Lives of the founders of the New Devotion, the movement Geert Grote began in the Low Countries before his death in 1384. Thomas's own Chronicle names him Thomas Hemerken, of Kempen in the diocese of Cologne. With Florens's help he lived about a year in the brothers' house at Deventer. "Here indeed I learned to write," he says."

**K-M3 (brief, para 3: a word whose modern sense misleads).**
- What is wrong. "he came to Zwolle for pardons the pope had granted there." To a modern listener a "pardon" is a legal release. The Chronicle's thing is an indulgence, which is a remission of penance.
- Evidence. CHRON l.1097-1104: "Indulgences were granted to the people of Zwolle by the Apostolic See, and Pope Boniface the Ninth granted these"; "came to Zwolle to gain indulgences."
- Fix: "In 1399, he writes, he came to Zwolle to gain indulgences, remissions of penance that the pope had granted there." Card, uncertain item "Who sent him to Mount St Agnes": "for the pardons of 1399" becomes "for the indulgences of 1399".

**K-M4 (brief, para 3: comma inside the marks where the file has a full stop).**
- What is wrong. '"I was received with mercy," he says.'
- Evidence. CHRON l.1105: "and I was received with mercy.  Afterward". Lessons §4 (era4 b8 A-M21).
- Fix: '"I was received with mercy", he says.'

**K-M5 (brief para 5 and card uncertain item 2: Benham's own hedge dropped).**
- What is wrong. Brief: "Benham argues for John Gersen, an abbot of Vercelli." Card: "William Benham, who translated it in 1886, argues for John Gersen, an abbot of Vercelli." Benham states the case and then grants that it becomes uncertain. On a Contested question, dropping a witness's own hedge makes his side sound firmer than he makes it (lessons §2, hedge dropped).
- Evidence. BENHAM l.627-632: "there seems strong reason for accepting the belief that the writer of the Imitatio was John Gersen ... But when we seek to investigate further, it must be confessed that our ground becomes somewhat uncertain." The records already quote this concession (Benham claim, l.628-633).
- Fix (brief): "Benham argues for John Gersen, an abbot of Vercelli, though he grants the ground is uncertain." Fix (card): "William Benham, who translated it in 1886, argues for John Gersen, an abbot of Vercelli, though he grants that the ground grows uncertain."

**K-M6 (brief, para 6: a beat paragraph with a false sequence; writing suffers).**
- What is wrong. "Later Thomas was sent to keep his aged brother John company." It follows the paragraph on Atkynson (1504), Benham (1886) and Ingram (1893), so "Later" reads as later than those. The two-sentence paragraph also has no place (Bethany) and stands alone as a beat.
- Evidence. CHRON l.2012-2026: John died "in a good old age ... in Bethany"; "I was with him and I closed his eyes, for I had been sent by the Visitors to bear him company". The entry follows chapter XXIII, headed "1422 (1432)" (l.1981), and comes before 1433 (l.2029). The Chronicle sets it after the 1424 dream (ch. XIX).
- Fix: "Years after that dream, the Chronicle tells, Thomas was sent to Bethany to keep his aged brother John company. "I was with him and I closed his eyes," he wrote."

**K-M7 (card, dates: the witness slips onto the wrong man).**
- What is wrong. "John Mason Neale, an English historian of the Dutch church writing in the 1850s, gives 1400. He was clothed as a canon on the feast of Corpus Christi, 1406." The 1406 sentence has no owner, and the last owner named is Neale. Neale does not give it.
- Evidence. CHRON l.1189-1193 (the Chronicle's own entry); NEALE l.4704-4711 has no 1406.
- Fix: "His Chronicle records that he was clothed as a canon on the feast of Corpus Christi, 1406."

**K-M8 (card, uncertain "When he was born": an honest limit hides his own held statement of his age).**
- What is wrong. "No line in his own writings gives the year." This is literally true, but Thomas's own Chronicle gives his age in 1448, which is the nearest held line to his birth year and his own. Lessons §3 (era4 b4 C-M8).
- Evidence. CHRON l.2378-2380 (1448): "Brother Thomas of Kempen was nominated and elected ... He was one of the elders, being sixty-seven years of age". This lies within the Chronicle that Thomas wrote, before the continuator's mark at l.3405-3406.
- Fix: "When he was born. No line in his own writings gives the year, but his Chronicle makes him sixty-seven in 1448. The notice of his death puts him in his ninety-second year in 1471. ..." (the rest as it stands). The records claim on birth adds CHRON l.2379-2380.

**K-M9 (card: the death-day difference the records tag as contested is not shown as a difference).**
- What is wrong. The dates field gives "the feast of St James the Less, after Compline". The Dublin note's "25 July 1471" is tucked into the birth item. Nothing tells the listener that these are two different witnesses for one question. The records carry a `contested_claim`, "The day of his death", with both sides.
- Evidence. CHRON l.3413; INGRAM l.260-261: "Tho. e Kempis natus 1380 obyt 25 Julij 1471."
- Fix: take "and his death on 25 July 1471" out of the birth item, and add an item after it: "The day he died. The notice of his death gives the feast of St James the Less, after Compline. The seventeenth-century note in the Dublin manuscript that John Ingram reports gives 25 July."

**K-M10 (card, uncertain "His parents": British spelling outside a quotation).**
- What is wrong. "his father was a labouring man". Narrator paraphrase, not in quotation marks.
- Fix: "his father was a laboring man".

**K-M11 (card, uncertain item 3 and the sources title: the editor's name taken from a Library header, in the wrong form).**
- What is wrong. "Josef Pohl, who edited Thomas's Latin works from 1902" and "(ed. Josef Pohl)". "Josef Pohl" appears only in the Library header of the Pohl file. The volume's own title pages and Duthoit's title page call him Michael Joseph Pohl. The records witness for his editorship is "DUTHOIT l.1", which is that file's header line (lessons §8, header is never a witness).
- Evidence. POHL l.3 (header): "(Josef Pohl, Editor)"; POHL l.110: "MICHAEL lOSEPHVS POHL"; DUTHOIT l.47: "OF MICHAEL JOSEPH POHL, PH.D."; DUTHOIT l.539: "Dr. M. J. Pohl".
- Fix: card, "Michael Joseph Pohl, who edited Thomas's Latin works from 1902, is persuaded that Gersen never existed"; the sources title reads "(ed. Michael Joseph Pohl)". Records: witness "POHL l.110; DUTHOIT l.47"; drop "DUTHOIT l.1" and "the file names him Josef Pohl".

**K-M12 (card: names with no context at first mention).**
- What is wrong. Three names a general listener cannot place, each without the role its own source gives (pattern, "any name a general listener would not know"; lessons §9, every scholar gets a role and time).
  - "Rosweide saw it at Cologne". Benham gives no role. The card can say only what Benham says.
  - "Ignatius of Loyola told Consalvius de Cámara". The editors give the role: Ignatius told him his own story.
  - "asked whether Walter Hilton wrote it". Ingram gives the role.
- Evidence. BENHAM l.507-508; IGN l.2600: "res a se gestas Consalvio enarrans"; INGRAM l.316-317: "an Englishman, Walter Hilton, author of the Scale (or Ladder) of Perfection".
- Fix: "and that one Rosweide, Benham says, saw it at Cologne with a closing note dated 1439"; "Ignatius of Loyola, telling the story of his life to Consalvius de Cámara, said in Spanish that at Manresa he first saw the Gerconzito, the little Gerson."; "asked whether Walter Hilton, the English author of the Scale of Perfection, wrote it, John Ingram reports."

**K-M13 (card, legacy traces, Wesley: an undefined title, and a selection that tells half of what he says).**
- What is wrong. "he read "Kempis's Christian Pattern"". Nothing on the card ties "Christian Pattern" to the Imitation. The trace also ends on Wesley's anger and drops the next sentence, in which he says he often found comfort in the book.
- Evidence. WESLEY l.961-966: "I was, however, very angry at Kempis for being too strict; though I read him only in Dean Stanhope's translation. Yet I had frequently much sensible comfort in reading him".
- Fix: "Reviewing his life in his Journal, John Wesley wrote that at about twenty-two he read the Imitation as "Kempis's Christian Pattern". He began to see "that true religion was seated in the heart". He was "very angry at Kempis for being too strict", yet often found "much sensible comfort in reading him"."

**K-M14 (card, uncertain "The dream of 1424": the label names no question).**
- What is wrong. "The dream of 1424." names a subject, not the uncertainty. The item's point is which telling borrowed from which (lessons §10, era4 b2 D-M16).
- Evidence. BUSCH l.5426: "Die folgende Stelle hat das Chron. Montis St. Agnetis S. 50 entlehnt."
- Fix: "Which telling of the 1424 dream came first. Karl Grube, who edited Busch's Latin in 1886, notes that the Chronicle of Mount St Agnes borrowed this passage. The Chronicle's version leaves the dreamer unnamed, and Busch names him as Thomas."

Checks that pass. The Imitation is told as Contested in place, both sides named, in the brief and in all three card items, and the first uncertain item repeats the brief's caveat. Busch's naming is told in modern words with the Latin named, and it covers the qualifier ("among them one on the imitation of Christ"; BUSCH l.5413-5415). Neale's "only reason" is his, attributed (NEALE l.4732-4734). The census differences on "most copied" and Ignatius's desk are true absences. "Most copied" appears only in the Library header of the Benham file (l.14) and in the Library README, which are not witnesses. No held line has the desk. The scene, the who-line (1384, then 1399 in para 3) and the close are sourced. Every card witness is in `sources`. otherNames are all spelled in held files: "Thomas Hemerken of Kempen" is the census `informalName`, and the Chronicle has "Thomas Hemerken of the city of Kempen" (CHRON l.1191-1192). Field order is right, and briefLength fits 400 words.

### geert-grote

**Verdict: one blocking finding (G-B1). Otherwise passes with minor fixes.**

**G-B1 (brief para 7, card uncertain item 1, records: a false "alone" on how the common life began).**
- What is wrong. Brief: "Busch alone tells how the common life began." Card: "Busch alone tells how the common life began, and that Grote caught the plague from his friend Lambert Stuerman." Records: "Common life, Busch alone among primary witnesses", tagged Inferential-Thin. Kempis's own Life of Grote tells how the common life began: Grote ruled that those who wished to live together should earn their living by their hands and live in common. Kempis's Life of Florentius tells the first brothers keeping a common table. What only Busch tells is the talk with Florens. A false absence is blocking wherever it sits (lessons §1, §3).
- Evidence. FOUNDERS l.3812-3822 (Life of Gerard, ch. on his disciples): "he ordained that if any should wish to abide continually together, they should earn their own living by the labour of their hands, and, as far as might be, live in common under the discipline of the Church." FOUNDERS l.5984-5989 (Life of Florentius): "to associate themselves together in Christ after the Apostolic manner; and they rejoiced with eager hearts to keep a Common table". BUSCH l.15349-15369 holds the Florens exchange, which is Busch's alone (confirmed: FOUNDERS l.1173-1178 is Arthur citing Busch; Duthoit l.593-600 and Neale l.4655-4690 do not tell it).
- Fix (brief): "Only Busch tells the talk that began the common life." (The rest of the paragraph stands. "Busch is also alone in saying..." in para 8 stands; the plague detail was checked and is Busch's alone.) Fix (card, uncertain item 1): "Busch alone tells the talk with Florens Radewijns that began the common life, and that Grote caught the plague from his friend Lambert Stuerman. Kempis says only that Grote ruled that those who lived together should earn their living by their hands, and that he was smitten." Fix (records): reword the claim to "The Florens–Grote exchange that began the common life, Busch alone; Kempis's Life gives Grote's rule that those living together earn their living by their hands and live in common (FOUNDERS l.3812-3822) and the first brothers' common table (FOUNDERS l.5984-5989)", witness "BUSCH l.15349-15369; FOUNDERS l.3812-3822, 5984-5989", and tag the exchange Inferential-Thin and the rule Documented.

**G-M1 (brief para 2: Kempis's account of his sources told as the narrator's fact, and narrowed).**
- What is wrong. "He wrote Grote's Life from what disciples told him". This is Kempis's own claim about his sources, told with no owner. It also leaves out that his informants were "both men and women".
- Evidence. FOUNDERS l.2086-2093: "Though I did not see Gerard in the flesh, yet have I known in the body divers men who owned discipleship to him, and from these I have often heard of his good deeds; ... I have received a faithful relation thereof from trusty persons, both men and women."
- Fix: "He wrote Grote's Life, he says, from what men and women who had known Grote told him, as a tribute to the founder of his own movement, the New Devotion."

**G-M2 (brief paras 3 and 4: a choppy run of bare acts; writing suffers).**
- What is wrong. Para 3 ends "Grote resigned his posts and put on a plain habit." Para 4 is then "He gave his Deventer house to poor sisters he had gathered. He became a deacon, the order below priest, so that he could preach, but out of awe would not be ordained priest." These are three acts from one turn of his life, set down as a list of "Grote... He... He..." sentences across a paragraph break. The witness for para 4 (Kempis's Chronicle) is not named in it.
- Evidence. CHRON l.3801-3808 tells all three in one passage: resigned his benefices, bequeathed his house to the poor Sisters, took the rank of deacon to preach.
- Fix (paras 3 and 4 joined): "... Grote resigned his posts and put on a plain habit. His Deventer house, Kempis's Chronicle says, he gave to poor sisters he had gathered there. He became a deacon, the order below priest, so that he could preach, but out of awe would not be ordained priest."

**G-M3 (brief, close: "kept" claims more than the source).**
- What is wrong. "His own notes, which Kempis kept, put...". The held line says the last chapter of the Life is taken from Grote's notes. Nothing says Kempis kept the notes.
- Evidence. FOUNDERS l.1572-1575 (Arthur): "the whole is taken from notes made by Gerard himself"; FOUNDERS l.4223-4224 (Kempis's heading).
- Fix: "His own notes, which Kempis gives at the end of his Life, put "the Gospel of Christ" first among his studies, "for therein is the Life of Christ.""

**G-M4 (card, knownFor: the same phrase twice in one sentence).**
- What is wrong. "Citizen of Deventer and deacon of the diocese of Utrecht who gave up his church posts and preached against vice through the diocese of Utrecht." The sentence is 25 words with a repeated doublet.
- Fix: "Citizen of Deventer who gave up his church posts and, as a deacon, preached against vice through the diocese of Utrecht."

**G-M5 (card, keyWorks "Letters": Kempis did not write English, and "years" overreaches).**
- What is wrong. "Kempis quotes several in English in his Life". Kempis wrote Latin, and the English is Arthur's. "his letters from the years of his silence". The held lines give the ban and his silence "for a time", not years.
- Evidence. FOUNDERS l.2775-2776: "He therefore held his peace for a time"; GROOTE l.4675-4676 (Acquoy): "postquam ei interdictum erat praedicare".
- Fix: "They include his warning about the friar Bartholomew at Kampen and letters written after his preaching was stopped. Kempis quotes several in his Life, which J. P. Arthur put into English in 1905".

**G-M6 (records, birth year: Opzoomer's same note gives another death year, unrecorded).**
- What is wrong. The card and records cite Opzoomer's note for 1340. The same sentence gives his death as 1383, against Kempis's and Busch's 1384. The variant is not recorded, and the reading needs an OCR allowance ("r383").
- Evidence. DIEP l.467-468: "Hij' is ïn 1340 te Deventer geboren en aldaar in r383 overleden."
- Fix: add to records `absent_details` (or the birth-year contested side): "Opzoomer's note gives his death 'in r383' (OCR; 1383 as printed), against 1384 in Kempis (CHRON l.3783) and Busch (BUSCH l.15934-15935). Not told; the card cites Opzoomer for 1340 only." No card change.

Checks that pass. The opening scene matches CHRON l.366-447 closely. "In a time of plague" keeps Kempis's wording, and Kempis does not say plague was the cause. The plague by Lambert Stuerman's pulse is Busch's alone: searched all of `cic/texts/` for Stuerman, Sturman and Stuurman, and the hits are BUSCH l.15809, Arthur's bequest note at FOUNDERS l.1190, and unrelated files. Neale l.3895-3902 has him seized after nursing the sick, and Duthoit l.600 "(of the plague)" names no friend. Bartholomew's teaching is told in modern words from Grote's letter (GROOTE l.2141-2142; BUSCH l.15650-15652), with "Grote wrote". The heresy finding is the court's (BUSCH l.15762-15764). The ban is told with Kempis's "craftily obtained" and the townspeople's line verbatim (FOUNDERS l.2758, 2768-2771). The card's three-sided "Why his preaching was stopped" names the unnamed friend and Acquoy. The Kempen/Ghent against Kampen/Gouda item rests on held lines, and the Latin Vita Gerardi is in no held file (POHL de compunctione l.334-336 lists vol. VII as part of the series only). otherNames: Gerard Groote (FOUNDERS), Gerard the Great (FOUNDERS heading), Gerardus Magnus (BUSCH), Gerijt die Groete (DIEP l.446) and Gherd de groet (LANG l.487) are all spelled in held files. Field order and briefLength (402 words) are right.

Non-counted notes (not findings). (1) Neale is a held witness on Grote that the Grote profile does not use. He gives "the October of 1340" for the birth (NEALE l.3683-3684), and his town list has Kampen and Gouda (l.3747-3749), which agrees with Busch against Arthur's Kempen and Ghent. The README's "Held witnesses beyond those the scan cites" list for Grote could name him. (2) The census Devotio Moderna movement text says "After his death in 1384 his followers organized". Busch and Kempis both put the start of the common life in Grote's lifetime. That is a census-text point for the movement's owner, outside this batch.

### records.json (these profiles)

- **R-M1 (README l.5: a claim that is not yet true).** "those points are logged in Open-Gaps for a census fix". `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` (3459 lines, last entry 262) has no era 6 batch 1 entry and no Kempis census point. Fix: "those points are listed in each profile's `absent_details` and go to Open-Gaps for a census fix when the batch is approved to proceed", or log the entry now.
- **R-M2 (Kempis records, the Vos claim note: misstates the source).** "the brief uses 'Heusden', Busch's and the scan's form ('lohannes Huesden' in Busch's OCR at 4803; 'Vos de Huesden')". Busch prints "Huesden" (BUSCH l.2662, 3862, 4803), as the Chronicle does. No held file connected to him spells "Heusden" (searched all of `cic/texts/`). The modern place form is a fair choice, but the note must not claim Busch for it. Fix: "the brief and the Grote card use 'Heusden', the modern form of the town; the Chronicle and Busch both print 'Huesden' (CHRON l.1702, 1707; BUSCH l.2662, 4803)."
- **R-M3 (Kempis records: two differences with the live census entry are not logged).**
  - The live entry says Florentius sent him to Mount St Agnes ("When Thomas was twenty, Florentius sent him"). It also says he "stayed in that small house until he died" (why) and was "in one small house all his life" (teaser). The profile tells these differently: the sending is contested (card item "Who sent him to Mount St Agnes"), and there is the exile at Lunenkerc from 1429 (CHRON l.1885-1924, three years) and the year with John at Bethany (CHRON l.2023-2026).
  - `absent_details` logs only the desk and "most copied" points, so the README's "agree with the live entries except where the held lines differ; those points are logged" does not cover these two.
  - Fix: add two `absent_details` entries: "Census longDescription: 'Florentius sent him'. His own Chronicle has him come for the indulgences and ask to stay (CHRON l.1103-1106); the death notice says Florentius sent him (CHRON l.3419-3421). Told as contested." And: "Census why/teaser: 'stayed in that small house until he died' / 'all his life'. The Chronicle has him in exile at Lunenkerc from 1429 for about three years (CHRON l.1885-1924) and with his brother at Bethany for 'a year and two months' (CHRON l.2023-2026)."
- Witness ranges, Kempis: all cited ranges cover their quoted text (checked: CHRON l.1097-1106, 1189-1194, 1702-1731, 2012-2026, 3392, 3409-3436; FOUNDERS l.6274-6292, 9021-9024, 12808-12826, 1517-1524, 1606-1619; BUSCH l.5410-5416, 5426; BENHAM l.487-490, 492-498, 506-521, 628-633, 663-664; INGRAM l.166-177, 259-261, 304-322, 1175-1186; NEALE l.4704-4736; IGN l.2600-2605, 2643-2644, 25087-25092, 3072-3073, 3101-3102; WESLEY l.961-965; NOVICES l.244-253; LYD l.119-129, 251, 1353-1354; DUTHOIT l.577-586, 741-743), except "DUTHOIT l.1" (K-M11).
- Witness ranges, Grote: all cover (CHRON l.366-447, 3750-3751, 3783-3830, 3852-3886; FOUNDERS l.2086-2093, 2171-2193, 2252-2310, 2370-2386, 2756-2771, 2866-2891, 3772-3778, 3872-3876, 3886-3889, 3950-3958, 4223-4224, 4605-4607, 5093-5148, 5274-5286; BUSCH l.15009-15012, 15237-15259, 15282-15283, 15349-15369, 15415-15430, 15626-15652, 15686-15764, 15805-15818, 15852-15872, 15913-15936, 15943-15946, 4514-4515, 4802-4812, 310; DIEP l.440-497, 465-467; LANG l.160-162, 487-489, 2062-2071, 2159-2195). The common-life claim's tag and witness change under G-B1.
- `formation_confidence`: every Contested tag in both entries has a `contested_claim` behind it (Kempis: authorship, year of entry, who sent him, birth year, the Bible's dates, death day; Grote: plague, birth year, the ban, towns, Ruysbroek companions, last promise). The other tags fit, except the common-life tag (G-B1).

### Checklist summary

| # | Item | thomas-a-kempis | geert-grote |
|---|---|---|---|
| 1 | Each sentence sourced | minor (K-M7) | minor (G-M1, G-M3, G-M5) |
| 2 | Quotes verbatim | minor (K-M4) | pass |
| 3 | No invention | pass | pass |
| 4 | Reading aids | minor (K-M2, K-M3, K-M6, K-M10, K-M12, K-M13) | minor (G-M2, G-M4) |
| 5 | Named witnesses | pass | pass |
| 6 | Partisan witness marked | pass (the death notice is a brother of the house; Benham marked as doubter) | pass (Kempis "a canon of the movement Grote began" placed once in brief and card) |
| 7 | Contested claims both sides | minor (K-M5, K-M9) | pass |
| 8 | Common names | minor (K-M1, K-M12) | pass |
| 9 | One term for one thing | pass | pass |
| 10 | Story, scene, disputes in place, length | pass (400 words) | pass (402 words) |
| 11 | Readability | pass (FK 6.7, FRE 71.5) | pass (FK 5.7, FRE 79.0) |
| 12 | Card order, fields, caveat repeated | minor (K-M8, K-M11, K-M14) | fail (G-B1) |
| 13 | Audio tags | pass | pass |
| 14 | Who test | pass | pass |

Consistency between the two profiles. Names, dates and spellings agree: Florens Radewijns, vicar of Deventer; Geert Grote; Johannes Busch, a canon of Windesheim; John Vos of Heusden, prior of Windesheim; Mount St Agnes near Zwolle; Windesheim; Thomas à Kempis; Grote's death in 1384; Busch's account finished in 1464; Arthur's Lives (1905) and Chronicle (1906). The Kempis brief's "Geert Grote began that movement" agrees with the Grote card's "the founder, by Busch's account". No conflict was found.

### Count

- **Blocking: 1.** G-B1.
- **Minor: 23.** K-M1 to K-M14; G-M1 to G-M6; R-M1 to R-M3.

| Profile | Words | FK | Flesch | Blocking | Minor |
|---|---|---|---|---|---|
| thomas-a-kempis | 400 | 6.7 | 71.5 | 0 | 14 |
| geert-grote | 402 | 5.7 | 79.0 | 1 | 6 |
| README / records | | | | 0 | 3 (R-M1 to R-M3) |

**Scores.** `grade_text`: Kempis fk 6.66, fre 71.45; Grote fk 5.66, fre 79.05. Both are inside the gates. The low FK reads as flat in Kempis para 2 and para 6 and in Grote paras 3 and 4, and the fixes K-M2, K-M6 and G-M2 join those sentences. The rest of both briefs connects its sentences and keeps the sources' voice.

**Files reviewed (absolute paths)**
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/README.md
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/thomas-a-kempis.brief.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/thomas-a-kempis.card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/audio/thomas-a-kempis.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/geert-grote.brief.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/geert-grote.card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/audio/geert-grote.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/records.json (thomas-a-kempis, geert-grote)
- /home/user/CIC-Project/cic-website/data/world-census.json (thomas-a-kempis; devotio-moderna-brethren-of-the-common-life)
- /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-12_who-scan-era6/Who_Scan_Era6.md (l.81, 89)
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md (searched)


---

## Era 6 Who batch 1, round 1 review: PART C

**Scope.** `richard-rolle` and `julian-of-norwich`: brief, card, audio script, and their `records.json` entries, against the 14-item checklist of `Who_Profile_Pattern.md`, the lessons file, the batch README and the two rows of `Who_Scan_Era6.md` (l.82, l.83). Julian is a Who under the women ruling (she founded, taught or led), so I checked whether the profile shows that from held lines. At the coordinator's added request I also judged both briefs for flattening or choppiness at their low grades (Rolle FK 6.4, Julian FK 5.4). I edited no repo file and made no web, paid or model calls.

**Method.** I read every brief and card string against the cited lines in context, 20 or more lines around each. I checked each quotation by script against its file, tolerant of whitespace, case, hyphen line-breaks and punctuation, then checked misses by eye. I hunted false absences and implied absences with case-insensitive, whitespace-tolerant greps across all of `cic/texts/`: Kempe, Margery, Juliana, Juhana (OCR), Jelyan, Julyan, Lady and Dame Julian, anchoress near Norwich; Hampole, 29 September, Michaelmas, September 1349, Wanley; "shall be well" in the short text. I scored both briefs and test fixes with `engine.m1.gates.grade_text`, counted sentence lengths, and diffed each audio script against its brief.

**Files opened (cic/texts/).**
- COMPER = `rolle_fire-of-love-and-mending-of-life_comper1914.txt`: l.135-165 (Underhill's introduction), 1490-1570 (Comper's preface, Misyn), 1630-1660 (signature 1913, English Martyrologe), 1675-1830 (Office, Lections I-IV), 2010-2115 (Lection VIII), 5465-5545 (Fire of Love I.15), 10375-10395 (Misyn's explicit), 1115-1130.
- HORST = `rolle_yorkshire-writers-enm_horstman1895.txt`: header, l.125-160, 205-230, 284-312, 495-526, 1990-2040, 2105-2115, 2156-2170, 2204-2212.
- HODGSON = `rolle_form-of-perfect-living-and-other-prose-treatises_hodgson1910.txt`: l.1-12, 185-190, 1195-1212, 1510-1520.
- FORSHALL-M = `wycliffite-bible_forshall-madden1850.txt`: l.420-445, 620-690.
- WYC-ARN3 = `wyclif_select-english-works-v3_arnold1871.txt`: l.1885-1960.
- UNDERHILL-H = `hilton_scale-of-perfection_underhill1923.txt`: l.40-105, 250-262, 528-548, 1190-1205, 1862-1872.
- TEST-EBOR3 = `york-registry_testamenta-eboracensia-v3-enm_raine1865.txt`: l.3790-3812, 9712-9722, 11868-11886.
- SURTEES-H = `surtees-society_horae-eboracenses-prymer-of-york-use-lat-enm_wordsworth1920.txt`: header, l.75-90, 1640-1656.
- MORRIS = `pricke-of-conscience_northumbrian-poem-enm_morris1863.txt`: l.100-135, 280-300 (search for a second death day or orders; none).
- VAUGHAN = `wyclif_tracts-and-treatises_vaughan1845.txt`: l.3278-3290.
- WARRACK = `julian-of-norwich_revelations-of-divine-love_warrack1901.txt`: l.200-460, 490-525, 740-765, 2080-2240, 2300-2320, 2588-2645, 3795-3830, 5540-5562, 8555-8630.
- HARFORD = `julian-of-norwich_comfortable-words-for-christs-lovers_harford1911.txt`: header, l.170-340, 455-480, 1130-1200, 2160-2176.
- DALGAIRNS = `hilton_scale-or-ladder-of-perfection_dalgairns1908.txt`: l.110-125, 205-216, 1765-1815.
- BURY = `bury-st-edmunds_wills-and-inventories-enm_tymms1850.txt`: l.1484-1494, 2312-2320.
- GARDNER = `cell-of-self-knowledge_seven-early-english-mystical-treatises_gardner1910.txt`: l.245-262, 505-590.
- CRESSY = `julian-of-norwich_sixteen-revelations-of-divine-love_cressy1843.txt`, by grep for the quoted lines.

**Quotations.** All 11 quoted strings in the Rolle brief and card, and all 23 in the Julian brief and card, match their files. Allowances:
- Julian, the copyist's heading: the file breaks "good / ness" and "Nor / wich" with no hyphen (HARFORD l.469-471).
- Julian, "It behoved that there should be sin; but all shall be well...": Warrack's footnote mark "[1]" follows "sin;" (WARRACK l.3818-3819). The records note it.
- Julian, "I am a woman unlearned, feeble and frail": an OCR footnote mark "13" follows "unlearned," (HARFORD l.1161). The records note it.
- Rolle, "suddenly I felt within me a merry and unknown heat.": the file reads "heat, But first" (COMPER l.5517). The comma is an OCR slip for a full stop, so the stop inside the marks is acceptable.
- Rolle, "the noise as it were of readers, or rather singers.": exact (COMPER l.5532).
- The Office's "My brother is mad! My brother is mad!" runs across a page break and running head (COMPER l.1705-1717, 1734-1735). The records note it.

**Dates.** Rolle: 1349 (COMPER l.1016, 156-157; HORST l.134; Widely Accepted); 29 September is Horstman's alone, and he is named (HORST l.134, 2161). Misyn's 1435 is in his explicit (COMPER l.10388-10389). Comper's 1913 is the signature of her preface (COMPER l.1638-1642). Horstman's 1895 comes from Comper's citation (COMPER l.1082-1083), not the header. Forshall and Madden's 1850 and Hodgson's 1910 come from in-text lines. Julian: 13 May 1373 is in her own text (WARRACK l.2086-2087). 1413 is Harford's reading and 1442 Blomefield's, both named. Warrack's 1901 is from her introduction's signature (WARRACK l.1956) and 1909 from HARFORD l.198-202. "Eighteenth-century" for Blomefield is Harford's (l.186-188). No header year is used as a witness in either brief.

**Audio.** Both scripts are the brief exactly, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. They differ only by a trailing newline. Two tags each.

---

### richard-rolle

**Verdict: passes with minor fixes. No blocking finding.**

The brief opens on a real scene, names every witness, marks the Office as the Office's account, and tells the priest dispute with both sides named. On the coordinator's question: the brief is not simplified in substance, and Rolle's own words carry paragraph 4. Paragraphs 2 and 3 do flatten into a run of "X says" lines, though, and the priest dispute arrives with no event to set it off (C-M1).

**C-M1 (brief, paragraphs 2 and 3: a run of "says" lines; a dispute with no reason; a dropped qualifier).**
- What is wrong. Paragraph 2 ends with two disconnected witness lines on the birth year: "Charles Horstman, who edited Rolle's English writings in 1895, puts his birth about 1300. Evelyn Underhill, introducing Comper's book, says probably about 1290." The card already holds this dispute, and the pattern does not repeat card dates as a list. The first line also drops Horstman's "or shortly before". In paragraph 3, "Horstman says Rolle was not in holy orders" follows the Dalton clothing with no link, so a listener cannot hear why the question matters. The Office's own preaching scene is the reason, and Horstman draws that consequence himself.
- Evidence. HORST l.131-132: "was born about, or shortly before, 1300". COMPER l.1766-1768: "having first besought the blessing of the priest, he went into the preacher's pulpit and gave the people a sermon". HORST l.502-505: "was not in holy orders, was neither priest nor monk, and consequently was not allowed to preach from the pulpit".
- Fix. Delete the two birth sentences from paragraph 2; the card keeps them. Replace the first two sentences of paragraph 3 with: "The Office says he preached from a church pulpit, and that a squire, John de Dalton, then clothed him as a hermit. Charles Horstman, who edited Rolle's English writings in 1895, says Rolle was not in holy orders, so was not allowed to preach from the pulpit." With C-M2 and C-M3, the brief is then 406 words, FK 6.5, Flesch 75.0.

**C-M2 (brief, paragraph 5: "learned that Rolle had just died").**
- What is wrong. The Office does not say the rider found him just dead. Hampole was "far distant". What the rider learned, after inquiring the hour, is that the fits had come back shortly after Rolle died. The brief moves the timing from the fits to the death.
- Evidence. COMPER l.2096: "which place was far distant from her own dwelling". COMPER l.2102-2106: "he learnt that the saint was dead to this world; and after diligently inquiring the hour of his passing, he found that the aforesaid illness had returned to the recluse shortly after the hour of Richard's departure".
- Fix. "When they came back, a rider went to Hampole and learned that Rolle had died shortly before the fits came back."

**C-M3 (brief, paragraph 4: an archaic tail inside the quotation).**
- What is wrong. "but forsooth privily, because alone before my Maker" is archaic past a listener's ease. The pattern says an archaic line is told in modern words.
- Evidence. COMPER l.5540-5541.
- Fix. 'Then "I burst out singing what before I said", though only in private, alone before his Maker.'

**C-M4 (card, legacy.traces 2 and 4: Forshall and Madden's hedges dropped).**
- What is wrong. "Forshall and Madden date the verses and the copy to the reign of Henry VI" drops their "appear". "They judge it substantially Rolle's original" drops their "more likely".
- Evidence. FORSHALL-M l.628: "The verses as well as the Ms. appear to be of the time of Henry the Sixth". FORSHALL-M l.642-645: "it seems therefore more likely, that the copy ... represents substantially the original of Rolle".
- Fix. "Forshall and Madden say the verses and the copy appear to date from the reign of Henry VI." And: "They think it more likely substantially Rolle's original, and Arnold says they showed it to be his."

**C-M5 (card, uncertain: three labels name no question).**
- What is wrong. "The story of his flight.", "The Dalton church." and "The commentary on the Canticles." name a topic, not the question (lessons §10).
- Fix. "How far the story of his flight can be trusted.", "Where the Dalton church stood.", "Who wrote the commentary on the Canticles."

**C-M6 (card, keyWorks "The Form of Living": process register).**
- What is wrong. "It is read here in Geraldine Hodgson's modern English of 1910" narrates the build ("here"); see lessons §9, "kept apart here".
- Fix. "Geraldine Hodgson put it into modern English in 1910."

### julian-of-norwich

**Verdict: one blocking finding (C-B1). Otherwise passes with minor fixes.**

**C-B1 (brief, paragraph 5, and card: the women ruling is not shown; her answer is turned into an open question; items 1, 4, 14).**
- What is wrong. Julian is a Who because she taught, here through her book. The README says "the brief tells her teaching through the book". It does not. Paragraph 5 gives only her lowliness ("unlettered", "unlearned, feeble and frail") and her refusal: "She refuses to be called a teacher." It then ends, "Yet she asks whether, being a woman, she should keep quiet about God's goodness". In the source that question is rhetorical, and her answer follows at once: she will tell it, out of charity, to her fellow Christians. Told as "she asks whether", it hangs open, and a listener hears a woman who declined to teach. That is the reverse of what the held lines show and of why she is a Who. The card has no line of her teaching either. Its one "teaching" line is teaching she received (C-M13).
- Evidence.
  - HARFORD l.1158-1168: "But God forbid that ye should say, or take it so, that I am a teacher ... For I am a woman unlearned, feeble and frail; but I know well this that I say I have it of the showing of Him that is Sovereign Teacher. But truly charity stirs me to tell you it. For I would God were known, and my even-Christians sped (is), as I would be myself".
  - HARFORD l.1177-1187: "But, because I am a woman, should I therefore leave [it alone], that I should not tell you the goodness of God, since I saw in the same time that it is His will that it be known? ... behold Jesus that is Teacher of all."
  - The long version addresses its readers in the same way. WARRACK l.2603-2608: "that which I say of me, I say in the person of all mine even-Christians ... And therefore I pray you all for God's sake, and counsel you for your own profit, that ye leave the beholding of a poor creature that it was shewed to". WARRACK l.2634-2635: "I say it to you that be simple, for ease and comfort".
  - The copyist's heading frames the book as written for others. HARFORD l.473-476: "In the which vision are full many comfortable words, and greatly stirring to all that desire to be Christ's lovers."
- Fix (brief). Replace paragraph 5 after its first sentence: 'In the shorter text, in Harford's spelling, she refuses to be called a teacher, for "I am a woman unlearned, feeble and frail". "But truly charity stirs me to tell you it," she goes on. Being a woman, she says, is no reason to keep silent about God's goodness, since she saw that God wills it known.' This drops the sentence on Warrack's gloss of the Sloane "knew no letter", which the card keeps under "How learned she was". With C-M9 to C-M12, the brief is 404 words, FK 5.5, Flesch 80.9.
- Fix (card). Add to knownFor: 'She wrote it for her fellow Christians, "for I would God were known", while refusing to be called a teacher.' Add a records claim citing HARFORD l.1158-1168 and 1177-1187 and WARRACK l.2603-2608.

**C-M9 (brief, paragraph 2: a choppy run; the heading detached from its own claim).**
- What is wrong. On the coordinator's question, this is where the Julian brief flattens. Ten short sentences of manuscript history run in a row. The gloss on "recluse" splits the heading's two claims, so "The heading adds that she is still alive" comes loose. "Dundas Harford printed..." and "He reads its year as 1413" are a choppy pair.
- Fix. '... "a devout woman, and her name is Julian, that is recluse at Norwich". The heading adds that she is still alive. A recluse, or anchoress, lived shut in a cell beside a church. Dundas Harford, who printed that shorter text after the British Museum bought it in 1909, reads its year as 1413.'

**C-M10 (brief, paragraph 3: a partial list told as the list).**
- What is wrong. "she had asked God for a sickness near to death at thirty, and for three wounds" leaves out the first of her three gifts. That is the sight of the Passion, which the showings answer.
- Evidence. WARRACK l.2087-2090: "Which creature [had] afore desired three gifts of God. The First was mind of His Passion; the Second was bodily sickness in youth, at thirty years of age; the Third was to have of God's gift three wounds."
- Fix. "Before this, she had asked God for three gifts. They were a sight of His Passion, a sickness near to death at thirty, and three wounds, of contrition, compassion and longing toward God."

**C-M11 (brief, paragraph 4: "She asked what it was").**
- What is wrong. She did not ask; she thought the question (Style Guide 1.12, questions must match the source).
- Evidence. WARRACK l.2315-2316: "I looked thereupon with eye of my understanding, and thought: _What may this be?_ And it was answered generally thus".
- Fix. "She wondered what it might be, and was answered: ..."

**C-M12 (brief, paragraph 1: "showings" undefined).**
- What is wrong. "the showings began" uses her term before any gloss.
- Fix. "and the showings, as she calls her visions, began."

**C-M13 (card, keyWorks long version: received teaching read as given).**
- What is wrong. "She also writes of teaching 'twenty years after the time of the Shewing, save three months'". The line is about teaching she was given inwardly. On a Who card under the women ruling, a reader hears it as her own teaching.
- Evidence. WARRACK l.5559-5560: "For, twenty years after the time of the Shewing, save three months, I had teaching inwardly".
- Fix. 'She also writes that she was taught inwardly "twenty years after the time of the Shewing, save three months".'

**C-M14 (card, knownFor: an implied absence).**
- What is wrong. "Her book survives in a shorter and a longer version. The longer one holds the words 'all shall be well'." Singling out the longer version implies the short one lacks the words. The short text has them several times.
- Evidence. HARFORD l.2170-2172: '"But all shall be well, and all manner of things shall be well."'. Also l.2387 and l.2464.
- Fix. 'Both hold the words "all shall be well".'

**C-M15 (card, remembered 4: the wrong book for Underhill's line; a source missing).**
- What is wrong. "Evelyn Underhill, who edited Walter Hilton's Scale of Perfection in 1923, calls her book 'perhaps the finest flower of English religious literature'." The line is in her 1914 introduction to Comper's Fire of Love, not the Hilton book. The card also cites Underhill's 1923 Hilton ("When she died"), but `hilton_scale-of-perfection_underhill1923.txt` is not in `sources`.
- Evidence. COMPER l.148-151, under "By Evelyn UNDERHILL" (l.135). UNDERHILL-H l.66: "(1343-c. 1413)".
- Fix. "Evelyn Underhill, introducing Frances Comper's edition of Rolle's Fire of Love in 1914, calls her book ...". Add to sources.about: { "title": "The Scale of Perfection, introduction", "author": "Evelyn Underhill", "date": "1923", "language": "English", "file": "cic/texts/hilton_scale-of-perfection_underhill1923.txt" }.

**C-M16 (card, uncertain "Julian Lampet.": one side told as settled; a hedge dropped; the label).**
- What is wrong. "Dame Julian Lampet was a different woman" is Warrack's side in the narrator's voice. The records tag the question Contested. "Dalgairns ... took the two for one woman" drops his "most probable". The label names no question.
- Evidence. WARRACK l.343-345: "is surely an impossibility". DALGAIRNS l.1777-1780: "It appears, however, most probable that she is the Juliana Lampit".
- Fix. "Whether she was Julian Lampet. Dame Julian Lampet was an anchoress at Carrow, the Benedictine nunnery by Norwich. ... J. B. Dalgairns, a priest of the Oratory, thought it most probable that the two were one woman, who lived to a hundred. Warrack calls that surely an impossibility." Keep the wills sentences as they are.

**C-M17 (card, uncertain "When she died": a reason Dalgairns does not give).**
- What is wrong. "says she appears to have died in 1443, on his view that she was Julian Lampet". Dalgairns gives no ground for 1443 and does not tie it to Lampet.
- Evidence. DALGAIRNS l.1785-1788: "She was thirty years old and a half in May, 1373, and, as she appears to have died in 1443, she must have lived to be a hundred."
- Fix. "J. B. Dalgairns says she appears to have died in 1443, and so lived to be a hundred. He gives no ground for the year."

**C-M18 (card, remembered 1: one reading of ambiguous Latin given as Poiret's).**
- What is wrong. "and calls her taught by God, profound and ecstatic". In Poiret's entry, "Theodidactae, profundae, ecstaticae" can go with "Julianae" (genitive singular) or with "Revelationes" (plural). The card picks one reading. "Warrack says he marked her ... and calls her" also lets "calls" be heard as Warrack's.
- Evidence. WARRACK l.275-276: "_Julianae Matris Anachoretae, Revelationes de Amore Dei. Anglice. Theodidactae, profundae, ecstaticae._"
- Fix. "Warrack says he marked her name with his sign of greatness. In modern words, his Latin entry reads taught by God, profound, ecstatic."

**C-M19 (card, a scholar without a time).**
- What is wrong. "J. B. Dalgairns, a priest of the Oratory" has a role and no time.
- Evidence. DALGAIRNS l.211-214: the reprint of Cressy's text appeared in 1870 "with an introduction by Father Dalgairns", the essay printed here.
- Fix. "J. B. Dalgairns, a priest of the Oratory, writing in 1870, ..."

**C-M20 (card, keyWorks long version: process register).**
- What is wrong. "Read here in Grace Warrack's modern spelling of the Sloane manuscript".
- Fix. "Grace Warrack printed it in modern spelling from the Sloane manuscript in 1901."

### records.json (these profiles)

**C-M7 (richard-rolle, the death day's confidence tag).**
- What is wrong. "Day of death ... The day and the cause are Horstman's" is tagged Widely Accepted. The absent_details entry says no other held line gives it, and my search agrees. One editor's day is not Widely Accepted (lessons §11). The README treats Tauler's one-witness day as Inferential-Thin.
- Fix. Split the claim. "Death in 1349" keeps Widely Accepted. "29 September, probably of the pestilence (Horstman alone)" takes Inferential-Thin.

**C-M8 (richard-rolle, a range and a stale gloss).**
- What is wrong. The "Margaret of Anderby" witness, "COMPER l.2038-2045, 2088-2111", quotes "he was wont to instruct her in the art of loving God", which is at l.2047-2048. It also quotes the rider's ride at l.2049. The "Recluse gloss" claim quotes the brief as "a woman who lived shut in a cell". The brief reads "A recluse lived shut away in a cell."
- Fix. Witness "COMPER l.2038-2052, 2088-2108". Gloss claim: "The gloss 'A recluse lived shut away in a cell' is the narrator's plain definition."

**C-M21 (julian-of-norwich, an incomplete search in the Kempe absent_details note).**
- What is wrong. The note says Gardner's Kempe extract "does not mention Julian". That holds for the extract. But it lists "dame julian" and "lady julian" as the names searched, and Gardner's own introduction names her twice, as "Mother Juliana of Norwich" and the OCR "Juhana". The visit itself is still absent: Gardner calls Kempe a "precursor" and offers a thirteenth-century Margeria as a possible identification. So the absence stands, but the search note is wider than the search.
- Evidence. GARDNER l.255-256: "Mother Juliana of Norwich, whose Revelations of Divine Love professedly date from 1373". GARDNER l.576-579: "a worthy precursor of that other great woman mystic of East Anglia: Juhana of Norwich". GARDNER l.552-554: Margeria "between 1284 and 1298".
- Fix. Append to the note: "Gardner's introduction names her as 'Mother Juliana of Norwich' (l.255-256) and calls Kempe her 'precursor' (l.576-579); neither line tells a meeting. Searches added: 'juliana', 'juhana'."

Also needed, as part of C-B1: a records claim for her teaching her readers (HARFORD l.1158-1168, 1177-1187; WARRACK l.2603-2608), tagged Documented. Once the brief is fixed, the README sentence "the brief tells her teaching through the book" becomes true. Until then it is not.

Every other claim checked has a witness whose range covers its text. Each Contested tag on these two profiles has a contested_claim behind it: Rolle's birth, his orders, Margaret, the Canticles and the canonization; Julian's 1413/1442 heading, her birth, Lampet, which version came first, and "unlettered". The scan's corrections the README lists for these two (COMPER 2129-2131 as the Office quoting him; Harford's 247 as a summary; Warrack's 1342 and 1442 as her own reckoning) check out against the files.

### Checklist summary

| # | Item | richard-rolle | julian-of-norwich |
|---|---|---|---|
| 1 | Each sentence sourced | minor (C-M2, C-M4) | fail (C-B1); minor (C-M10, C-M14, C-M15, C-M17, C-M18) |
| 2 | Quotes verbatim | pass (OCR allowances noted) | pass (OCR allowances noted) |
| 3 | No invention | pass | pass |
| 4 | Reading aids | minor (C-M1, C-M3, C-M6) | fail (C-B1); minor (C-M9, C-M11, C-M12, C-M20) |
| 5 | Named witnesses | pass | pass |
| 6 | Partisan witness marked | pass (the Office's purpose is named) | n/a |
| 7 | Contested claims both sides | pass | minor (C-M16) |
| 8 | Common names | pass | pass |
| 9 | One term for one thing | pass | pass |
| 10 | Story, scene, disputes in place, length | minor (C-M1) | pass |
| 11 | Readability | pass (FK 6.4, Flesch 73.8) | pass (FK 5.4, Flesch 80.2) |
| 12 | Card order, fields, caveat repeated | minor (C-M5) | minor (C-M13, C-M15, C-M16, C-M19) |
| 13 | Audio tags | pass | pass |
| 14 | Who test | pass | fail (C-B1: the teaching that makes her a Who is not shown) |

### Count

- **Blocking: 1.** C-B1 (Julian, women ruling not shown; her answer turned into an open question).
- **Minor: 21.** Rolle: C-M1 to C-M8 (8). Julian: C-M9 to C-M21 (13).

| Profile | Words | FK | Flesch | Blocking | Minor |
|---|---|---|---|---|---|
| richard-rolle | 404 | 6.4 | 73.8 | 0 | 8 |
| julian-of-norwich | 395 | 5.4 | 80.2 | 1 | 13 |

**Scores.** With the fixes above applied as worded: Rolle 406 words, FK 6.5, Flesch 75.0; Julian 404 words, FK 5.5, Flesch 80.9. Both stay within the 2:30 cap. Neither brief reads as simplified in substance once C-M1 and C-M9 join their choppy runs. The low FK comes from short quoted lines and plain narration, not from lost content.

**Files reviewed (absolute paths)**
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/richard-rolle.brief.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/richard-rolle.card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/audio/richard-rolle.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/julian-of-norwich.brief.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/julian-of-norwich.card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/audio/julian-of-norwich.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/records.json (richard-rolle, julian-of-norwich)
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/README.md
- /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-12_who-scan-era6/Who_Scan_Era6.md (l.82-83)


---

## Era 6 Who batch 1, round 1 review: PART D

**Scope.** `meister-eckhart`, `johannes-tauler` and `henry-suso`: brief, card, audio script and their `records.json` entries, with the README lines on them, and their consistency with each other (Eckhart, Elsbeth Stagel, Henry of Nördlingen, C. de B. Evans, Heinrich Denifle, the Life, the dates). Held to the coordinator's rulings, above all that Tauler's sermons survive as his hearers' notes, said plainly with the witness named. No repo file edited; no web, paid or model call.

**Method.** Read CLAUDE.md ("Trust and source fidelity", "Accessible and rigorous"), the Who Profile Pattern and its 14-item checklist, lessons.md, the three Who_Scan_Era6 rows (l.84-86), and the README. Opened every cited line in its file with 20 or more lines around it. Quotations checked by script (lowercase, letters and digits only, hyphen line-breaks joined) against the files. False-absence hunt: every "alone", "only", "never names", "no source", "not known" searched across all of `cic/texts/` (42 files name Eckhart, 40 or more name Tauler), case-insensitive, with OCR and spelling variants (Eckart, Eckehart, Ekardus; Tauler, Taulerus, Tauleri; IHS, Jhs, ihs; Saxonia, Sachsen, Böhmen, Bohemia, Provincial; 1361, Juni). `grade_text` run on each brief; sentence lengths counted by script for briefs and every card string; audio rebuilt from the brief and compared byte for byte. Severity follows lessons §1: a false absence is blocking wherever it sits.

**Files opened (cic/texts/).** DENIFLE-II = ehrle-denifle_archiv-literatur-kirchengeschichte-mittelalters-bd2-deu-lat_1886.txt (l.1-40, 23179, 24245, 29240-29300, 34498-34512, 34600-34610, 34800-34850, 34905-34995, 35069-35190, 35260-35320, 35433-35477, 35586-35835); DENIFLE-III (bd3, 1887, l.35080-35151, search only); EVANS = eckhart_meister-eckhart-vol1_evans1924.txt (l.30-42, 330-548, 639, 1421-1433, 1519-1521); DANIELS = eckhart_lateinische-rechtfertigungsschrift-lat_daniels1923.txt (l.1-12, 43-51, 645-665, 847-855, 898-930); PFEIFFER = eckhart_deutsche-mystiker-bd2-gmh_pfeiffer1857.txt (l.355-380, 518-522); DENZ = denzinger_enchiridion-symbolorum-lat_bannwart1911.txt (l.88, 15210-15222); JOSTES = eckhart_meister-eckhart-und-seine-juenger-gmh_jostes1895.txt (l.65, 75, 800-865); LEA = lea_history-of-the-inquisition-of-the-middle-ages-v3_1888.txt (l.54, 7390-7405); WINK = tauler_history-and-life-with-sermons_winkworth1907.txt (l.825-1003, 1700-1800, 3360-3415, 3925-4000, 4100-4135, 4240-4310, 4505-4630, 4900-4912, 5055-5180, 5255-5270, 6420-6455, 7020-7060, 7080-7180, 7800-7815); SPENER = spener_pia-desideria-deu_koehler1841.txt (l.1-130, 5370-5380); LANGENBERG = langenberg_quellen-und-forschungen-niederdeutschen-mystik-gml_1902.txt (l.9275-9296); WESLEY = wesley-j_journal-v1_curnock1909.txt (l.56, 8640-8660, 8683); KNOX = suso_life-of-blessed-henry-suso_knox1865.txt (l.1-200, 300-350, 520-558, 995-1055, 1330-1345, 3470-3505, 3750-3790, 5340-5370, 5375-5385, 5500-5504, 8380-8440, 10685); BIHL = suso_deutsche-schriften-gmh_bihlmeyer1907.txt (l.166, 4970-5050, 5185-5192, 5305-5310, 6630-6675, 7370-7385, 8245-8300, 8778-8798, 8960-8995, 9165-9176, 10655-10662, 11120-11150, 18395-18400); LITTLE = suso_little-book-of-eternal-wisdom_1910.txt (l.1-12, 30, 730-746, 895-952); CRAFT = craft-of-dying_book-of-the-craft-of-dying-and-other-early-english-tracts_comper1917.txt (l.110-132, 255-265, 6545-6566); BUSCH = busch_chronicon-windeshemense-lat_grube1886.txt (l.160, 167, 20488-20526); also, by search, theologia-germanica_theologia-germanica_winkworth1893.txt (l.1230-1300), arndt_true-christianity_boehm-schaeffer1868.txt (l.1120-1140), julian-of-norwich_comfortable-words-for-christs-lovers_harford1911.txt (l.3797-3816), cloud-of-unknowing_cloud-and-other-treatises_mccann1924.txt (l.16981), luther_works-v3-selected_various1930.txt (l.6011-6025).

**Quotations.** All 24 quoted strings in the three briefs and cards match their files by script: EVANS ("the scantiest material for a biography", "never made any recantation of his teaching", "What matters is that it shall happen in me."), KNOX ("the holy Master Eckart", "by stealth, so that he knew not of it.", "this ghostly theft", "burnt all of it that was there.", "for the most part just as she had written it with her own hand.", "the Name of Jesus", "he went to the holy Master Eckart"), LEA ("aggrieved by the sentence of heresy passed upon Master Eckart"), WINK ("dark as to the light of grace", "a downright fool", "Tauler did not himself write down his discourses, but they were compiled from notes taken by his hearers", "helped me in every way he could with all fidelity", "Works of love,", "are more acceptable to God than lofty contemplation", "faithful Father Tauler", "his noble act of disobedience", "Tauler's Life"), WESLEY ("Tauler's Life"), LITTLE ("I am not what thou seekest!", "Tender loving Wisdom! And is it Thou I have so long been seeking for?"). OCR allowances: WINK l.3410-3411 "down- right" (line-break hyphen); WESLEY l.8653 "Life^" (footnote mark outside the quoted words). Punctuation sits outside the marks where the file has none ("contemplation". where WINK has ";"; "hearers". where WINK has ","). No Latin, German or Middle High German is put in quotation marks.

**Dates.** Every year in the three briefs names its owner, except those read from the dated acts and bull, which are Documented (DENIFLE-II l.35078-35080, 35287-35290, 35433-35435, 35820-35821). Tauler's 16 June 1361 is Winkworth's (WINK l.7171-7172; no other held file gives the day). Suso's 25 January 1366 is Bihlmeyer's and 1365 is Knox's (BIHL l.8964-8966; KNOX l.85-87). No Library header is used as a witness: Denifle 1886 (DENIFLE-II l.33, title page), Daniels 1923 (DANIELS l.51, title page; records cite blank l.43, see D-M24), Knox 1865 (KNOX l.191-193), Bihlmeyer 1907 (BIHL l.166), Comper 1917 (CRAFT l.130), the Little Book 1910 (LITTLE l.30, imprimatur), Lea 1888 (LEA l.54), Spener's editor 1841 (SPENER l.126; records cite blank l.116, see D-M24). Evans's "1920s" and Winkworth's "nineteenth century" are inferences from their latest cited works (EVANS l.639, 1923; WINK l.992-1003, 1855), tagged Inferential-Thin, and phrased as decades.

**Audio.** All three audio scripts are the brief exactly, with `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph, and no other tag (checked by rebuilding from the brief). Pass.

---

### meister-eckhart

**Verdict: one blocking finding (D-B1). Otherwise passes with minor fixes.**

**D-B1 (card `uncertain`, "His offices before 1326", and its records claim: false "alone").**
- What is wrong. "His offices before 1326. Evans alone gives Saxony in 1303, Bohemia in 1307, Strasbourg in 1312 and Frankfurt in 1320." Three other held witnesses give the offices or the Strasbourg years. The card's own `place` field already cites Denifle for Strasbourg 1312 to 1321. The records claim repeats the "alone" ("Card uncertain: Evans alone gives…", tagged Inferential-Thin).
- Evidence. WINK l.4251-4254: "the celebrated Master Eckart, a brother of his own Order, who, after having filled the important offices of Provincial in Saxony and Vicar-General in Bohemia, had returned to Strasburg". PFEIFFER l.368-369: "vielleicht während seines generalvicariats in Böhmen (um 1307) gehaltenen predigten" (sermons perhaps given during his vicar-generalship in Bohemia, about 1307). DENIFLE-II l.35268-35269: Johannes de Grifenstein "welcher 1312 — 21 wenigstens mehrere Jahre mit Eckehart im Convente zu Strassburg weilte".
- Fix (card): "His offices before 1326. Evans gives Saxony in 1303, Bohemia in 1307, Strasbourg in 1312 and Frankfurt in 1320." / "Winkworth also names his offices in Saxony and Bohemia. Franz Pfeiffer, his editor of 1857, places the Bohemian office about 1307." / "Denifle places him at Strasbourg between 1312 and 1321. He thinks the Frankfurt prior named Eckhart in a letter was another man, and doubts that the Master was ever at Frankfurt." Fix (records): reword the claim to "Evans gives…; Winkworth names Saxony and Bohemia (WINK l.4251-4254); Pfeiffer, Bohemia about 1307 (PFEIFFER l.368-369)" and retag Widely Accepted for the offices, keeping Frankfurt Contested.

**D-M1 (card `dates` and the contested_claim "His birth": Evans's qualifier dropped, a held side missing).**
- What is wrong. "C. de B. Evans… says neither its date nor its place is known." Evans goes on at once to report the argued birthplaces, and Pfeiffer, in Evans's own English, names Strassburg as his birthplace. The contested_claim sets Evans against Bannwart's Hochheim, when Evans himself reports Hochheim as argued.
- Evidence. EVANS l.494-496: "Of his birth neither date nor place is known. It is argued that he was born before 1200 either at Strassburg in Saxony, or at Hochheim in Thüringia." (the year reads "1200" in the OCR and is not usable). EVANS l.377-378 (Pfeiffer's preface of 1857 in Evans's English): "consistently with Eckhart's home and birthplace, Strassburg".
- Fix (card `dates`, after the Evans sentence): "He adds that some argue for Strassburg in Saxony and others for Hochheim in Thuringia. Franz Pfeiffer, his editor of 1857, calls Strassburg his home and birthplace." Fix (records): add both to the "His birth" sides, with the OCR year noted as unread.

**D-M2 (brief, paragraphs 3 and 4: pronouns that capture the wrong man).**
- What is wrong. "edited in 1923 by Augustinus Daniels, a Benedictine monk. He could be in error, he wrote, but not a heretic" is first heard as Daniels. "Evans says the first known mention of his name is on a list of Paris professors" can be heard as Evans's name.
- Evidence. DANIELS l.924-926 (Eckhart's own "Errare enim possum, hereticus esse non possum"); EVANS l.496-497.
- Fix: "In it Eckhart wrote that he could be in error but not a heretic, for error is of the mind and heresy of the will." and "Evans says the first known mention of Eckhart's name is on a list of Paris professors, in 1302."

**D-M3 (brief, paragraph 2: qualifier dropped).**
- What is wrong. "Eckhart called God to witness that he had always hated every error in faith." The declaration limits it: as far as he was able.
- Evidence. DENIFLE-II l.35309-35311: "quod omnem errorem in fide et omnem deformitatem in moribus semper, in quantum michi possibile fuit, sum detestatus".
- Fix: "In the paper, Eckhart called God to witness that he had always hated every error in faith, as far as he was able."

**D-M4 (brief, paragraph 5: the confession narrowed).**
- What is wrong. "It lists twenty-six articles he confessed he had preached". The bull says he preached, taught and wrote them, and the writing matters to the condemnation.
- Evidence. DENIFLE-II l.35637-35638: "ipse predicavit, dogmatizavit et scripsit viginti sex articulos".
- Fix: "It lists twenty-six articles he confessed he had preached, taught and written, and two more charged against him."

**D-M5 (card `uncertain`, "The bull's numbers": no uncertainty).**
- What is wrong. The item names no doubt and no doubter: twenty-six plus two is Denifle's twenty-eight, and Evans's seventeen and eleven (EVANS l.529-530) also make twenty-eight. Lessons §10: an item with no uncertainty is not a doubt.
- Evidence. DENIFLE-II l.35586-35587, 35636-35639, 35771-35772.
- Fix: delete the item. The brief already gives the bull's numbers.

**D-M6 (card `uncertain`, "His life": tail).**
- What is wrong. "That is Evans's judgment." adds no fact; the sentence before already names Evans.
- Fix: delete the sentence.

**D-M7 (card `legacy.traces`, first item: heard ambiguity).**
- What is wrong. "a vision in which Eckhart appeared to him after death" can be heard as after Suso's death.
- Evidence. KNOX l.1336-1342 (the dead appear to the Servitor, "Among others… the blessed Master Eckart").
- Fix: "It also tells of a vision in which Eckhart, after his own death, appeared to Suso in glory."

**D-M8 (card `uncertain`, "His life": scholars with no role or time).**
- What is wrong. "his outline of the career comes chiefly from the books of Preger and Lasson." Neither is placed.
- Evidence. EVANS l.450-451: "The following facts are taken chiefly from Preger's Geschichte and Lasson's Meister Eckhart."
- Fix: "He says his outline of the career comes chiefly from Preger's history of German mysticism and Lasson's book on Eckhart, both German studies he cites."

### johannes-tauler

**Verdict: one blocking finding (D-B2). Otherwise passes with minor fixes.** The coordinator's ruling holds: the brief says plainly, in Winkworth's words and with her named, that Tauler did not write down his sermons and that they were compiled from his hearers' notes (WINK l.907-910), and keeps her qualified view of the eighty-four Strasbourg sermons (WINK l.914-917). The card's knownFor, keyWorks and uncertain say the same. Pass on the ruling, with D-M13 for the ownWords entry.

**D-B2 (brief, paragraph 6: false "alone").**
- What is wrong. "His last months are told by Winkworth alone." The History tells the Master's last illness of more than twenty weeks, the friend's visit, the eleven days of talk and the death-struggle in the convent. Winkworth's own account takes the eleven days from it, as the card's uncertain item says. What rests on Winkworth alone is the year, the move to his sister's convent, the day and the burial.
- Evidence. WINK l.3930-3933: "visited him with sickness, so that the Master kept his bed for more than twenty weeks"; WINK l.3987-3988: "And for a space of eleven days the Master held much discourse with the man"; WINK l.3995-3997: "the Master had a most horrible and frightful death-struggle". WINK l.7168-7170: "For yet eleven days, it is said that they held much discourse together". No other held file gives the sister, the day or the burial (search of all cic/texts for Tauler with 1361, Juni, June, sister, Schwester).
- Fix: replace the first sentence with "Winkworth alone gives the year, the place and the day of his death, and her account of his last days follows the History." (23 words.)

**D-M9 (brief, paragraph 2: thesis opener).**
- What is wrong. "Whether any of it happened is disputed." opens the paragraph on a status line, ahead of the witnesses who carry the dispute (lessons §9, era4 b8 A-M4).
- Fix: delete it, so the paragraph opens "The History's own text never names the Master." The dispute is still told in place by Winkworth and Denifle.

**D-M10 (brief, paragraph 6: detail added).**
- What is wrong. "He had himself carried to the convent" adds the manner. Winkworth says he caused himself to be removed.
- Evidence. WINK l.7122-7125: "he caused himself to be removed to the convent where his aged sister was a nun".
- Fix: "He had himself moved to the convent where his aged sister was a nun."

**D-M11 (brief, paragraph 5: a place with no context).**
- What is wrong. "At Basel, wrote his old friend Henry of Nördlingen…" comes straight after "kept working" at Strasbourg. Nothing says why Tauler was at Basel. Winkworth does: he preached from Cologne to Basel and made a long visit there.
- Evidence. WINK l.5133-5138: "he did not confine his exertions to that city, but preached from time to time at various places, from Cologne to Basle. Before the close of 1338 he seems to have made a somewhat lengthened visit to the latter city"; WINK l.5171-5173.
- Fix: "Winkworth says he also preached from Cologne to Basel. At Basel, his old friend Henry of Nördlingen, a priest from Constance, wrote that Tauler "helped me in every way he could with all fidelity"." (9 and 25 words.)

**D-M12 (brief paragraph 3 and card `dates`: a scholar with a time but no role; drift from the Eckhart and Suso cards).**
- What is wrong. "C. de B. Evans, writing in the 1920s" says when, not who. The Eckhart profile calls him Eckhart's English translator and the Suso card "an English translator of Eckhart in the 1920s".
- Evidence. EVANS l.30-42 (title page: "TRANSLATION… BY C. DE B. EVANS").
- Fix, in both places: "C. de B. Evans, an English translator of Eckhart in the 1920s".

**D-M13 (card `sources.ownWords`: not only his own words).**
- What is wrong. The one ownWords entry is the whole book, "The History and Life… with Twenty-Five of his Sermons", authored "Johannes Tauler". The History is a book about the Master, not his words, and the sermons are his hearers' notes by the card's own account. Lessons §10: ownWords holds only the subject's own words; retitle (era3 b8 C-M10).
- Evidence. WINK l.907-910; WINK l.4114-4115 (the History is a book in which Tauler "appears as 'the Master'").
- Fix: title "Twenty-five of his sermons, compiled from his hearers' notes, in Susanna Winkworth's English"; author "Johannes Tauler, through his hearers' notes; Susanna Winkworth (tr.)". The History stays in `about`.

**D-M14 (card `keyWorks` and `uncertain`, "His sermons": the marks misowned and miscounted).**
- What is wrong. keyWorks: "marks some of her twenty-five as doubtful". Uncertain: "one of her selection is marked as Eckhart's in an older edition". Winkworth reports that the Frankfort edition marks two: No. 2 as Eckhart's and No. 4 as probably a disciple's.
- Evidence. WINK l.966-970: "The sermon No. 2, is marked as Eckart's in the Frankfort Edition, and No. 4 as most probably the production of a disciple of his, commonly called Eckart, junior."
- Fix (keyWorks): "…had his own corrections. She reports that the Frankfort edition marks two of her twenty-five as Eckhart's or a disciple's." Fix (uncertain): "She notes that the Frankfort edition marks one of her selection as Eckhart's and another as probably his disciple's."

**D-M15 (card `legacy.traces`: a partial list told as the list).**
- What is wrong. "Winkworth lists printed editions of his sermons from Basel in 1521 and Cologne in 1543." She first names the oldest, Leipzig 1498, which holds only the eighty-four.
- Evidence. WINK l.828-829: "The oldest printed edition, too, that of Leipsic, in 1498, has only these eighty-four sermons."
- Fix: "Winkworth lists printed editions of his sermons from Leipzig in 1498, Basel in 1521 and Cologne in 1543."

**D-M16 (card `uncertain`, "Whether he heard Eckhart": both witnesses' Strasbourg view left out).**
- What is wrong. The item gives only Cologne. Winkworth also holds that at Strasbourg he "must have come in contact" with Eckhart, and Evans says he probably heard him at Strasbourg too. This is the Strasbourg the Eckhart card places Eckhart in.
- Evidence. WINK l.4245-4251: "on returning from Paris to Strasburg, [he] have come in contact with several of the mystical teachers… The most eminent of these was the celebrated Master Eckart"; EVANS l.507-508: "Here Tauler, Suso and Ruysbroeck probably heard him, and Tauler also at Strassburg."
- Fix: "Whether he heard Eckhart. Winkworth thinks he must have met Eckhart's teaching at Strasbourg, and was probably among his admirers at Cologne." / "Evans says he probably heard him at both. No source used here shows them meeting."

### henry-suso

**Verdict: one blocking finding (D-B3). Otherwise passes with minor fixes.**

On the coordinator's added check (FK 5.3): the brief is not simplified in substance. It keeps the Life's own imagery ("this ghostly theft", the Name over the heart, the red-silk cloths, "I am not what thou seekest!") and tells the authorship question in place with both Knox and Bihlmeyer. The low grade comes from short, plain words more than from short sentences (the average is about 14 words). The writing does suffer in three places, where sentences sit side by side as a list of card facts with nothing joining them (paragraphs 2 and 6) or a sentence hangs with no outcome (end of paragraph 5). D-M19 gives the joins. Eckhart (FK 7.7) and Tauler (FK 7.1) flow, and no choppy-run finding is raised on them.

**D-B3 (card `uncertain`, "The Name on his breast", and records `absent_details`, "IHS cut on his breast": false "only").**
- What is wrong. "The form IHS appears in the Life only on the cloths Stagel stitched." The records note says the same. Bihlmeyer's German text of the Life, which the card lists among Suso's own words, writes the Name cut over his heart as IHS, twice, in that very chapter.
- Evidence. BIHL l.11132-11133: "und stach also hin und her und uf und ab, unz er den namen IHS eben uf sin herz gezeichent"; BIHL l.11145-11146: "do genas er, und beleib der nam IHS eben uf dem herzen stende". KNOX l.8417-8420 has IHS only on the cloths, so the "only" holds for Knox's English alone.
- Fix: delete the uncertain item; nothing about the form is in doubt. Rewrite the absent_details note: "Knox's English says 'the Name of Jesus' (KNOX l.1028, 1051); Bihlmeyer's German text of the same chapter writes it IHS (BIHL l.11133, 11145). Knox has IHS only on the cloths (KNOX l.8417-8420)." The brief is right as it stands.

**D-M17 (brief, paragraph 5: the Life's framing dropped).**
- What is wrong. "The Life calls this the sin of simony." The Life calls the scruple "an inordinate fear" and explains what simony is; it does not say his entry was simony. Told this way, a listener hears the Life convict him.
- Evidence. KNOX l.3484-3490: "This temptation fell upon him through an inordinate fear. It had been told him that his admission into the Order had been connected with the bestowal of temporal goods, and from this comes the sin called simony". (Bihlmeyer doubts any wrong was done, BIHL l.5417-5421, as records note.)
- Fix: "The Life says this woke in him an inordinate fear of the sin called simony." (15 words.)

**D-M18 (brief, paragraph 2: pronoun capture).**
- What is wrong. "Thomas Francis Knox, an Oratorian priest who put the Life into English in 1865, says he was born in 1300." The nearest "he" is Knox.
- Fix: "…says Suso was born in 1300."

**D-M19 (brief, paragraphs 2, 5 and 6: facts listed side by side; a sentence left hanging; the coordinator's check).**
- What is wrong. Paragraph 2 runs five unjoined statements, each with a new subject, and splits the woman's naming from the scene it explains with the birth years in between. Paragraph 6 gives Bihlmeyer's death and burial in two sentences that share one witness. Paragraph 5 ends on the charge at the chapter with no outcome, though the Life gives one.
- Evidence. KNOX l.3765-3771: "They said that he had written books containing false doctrine… In consequence, he was harshly and severely reprimanded, and he was threatened with heavy punishment, though God and the world knew that he was guiltless".
- Fix, paragraph 2: "The friar is Henry Suso, a Dominican of Constance, whose Life tells his story in the third person, as the Servitor of the Eternal Wisdom. A later chapter names the woman as Elsbeth Stagel, a Dominican nun at Töss. Thomas Francis Knox, an Oratorian priest who put the Life into English in 1865, says Suso was born in 1300. Karl Bihlmeyer, who edited his German works in 1907, reckons about 1295." (25, 14, 20, 12 words.)
- Fix, end of paragraph 5: add "He was harshly rebuked and threatened with heavy punishment, though the Life holds that he was guiltless." (17 words.)
- Fix, paragraph 6: "Bihlmeyer writes that Suso died at Ulm on 25 January 1366 and was buried inside the friars' church. Knox gives the same day in 1365, with burial in the cloister." (18 and 13 words.)

**D-M20 (brief, paragraph 5: Eckhart with no context).**
- What is wrong. 'Then "he went to the holy Master Eckart", who set him free.' The brief never says who Eckhart was. A general listener hears a name and a title only (Pattern: "no statements that have no context").
- Evidence. KNOX l.3498-3502; DENIFLE-II l.35292-35293 ("magister Ekardus, doctor sacre theologie, ordinis predicatorum").
- Fix: 'Then, the Life says, he went to Meister Eckhart, a Dominican master of theology, and "the holy man delivered him".' (19 words; "The holy man delivered him from it", KNOX l.3500-3501.)

**D-M21 (brief and card titles; also the Eckhart card: "Life of the Servant", and Servant/Servitor drift).**
- What is wrong. "The Life of the Servant" appears in no held text. It is in the Library content notes only (KNOX l.9; BIHL l.10). Knox calls the book "The Life of Blessed Henry Suso, by Himself" and the man "the Servitor" (238 times); Bihlmeyer calls it the "Vita". The brief then names him "the Servitor" in paragraph 2 and "the Servant" in paragraph 7, two words for one self-name (item 9).
- Fix: brief paragraph 1, "His Life says she wrote it down…". Suso card keyWorks title "The Life (Knox's Life of Blessed Henry Suso, by Himself; Bihlmeyer's Vita)", and knownFor "whose Life tells his inner life". Eckhart card traces, "Henry Suso's Life tells that…". Brief paragraph 7: "the Servant, as this book calls him, seeks rest in created things."

**D-M22 (card, names with no identifier at first card mention).**
- What is wrong. `legacy.traces`: "Henry of Nördlingen" (the Tauler card calls him "a priest from Constance"). `uncertain`, "The chapter…": "Denifle, he reports" and "Preger and Seeberg", with no role or time. In this card, Denifle's first mention is here.
- Evidence. WINK l.5171-5175; BIHL l.8294-8296 ("Freund und Gesinnungsgenosse unseres Mystikers war auch Heinrich von Nördlingen"); DENIFLE-II l.35835; BIHL l.6673-6675.
- Fix: "Henry of Nördlingen, a priest and friend of Tauler and Suso," and "Heinrich Denifle, a Dominican scholar, chose Bruges in 1336, Bihlmeyer reports. Preger and Seeberg, whom he also cites, chose 's-Hertogenbosch in 1335."

**D-M23 (card `legacy.traces`: Comper's time qualifier dropped).**
- What is wrong. "Comper writes that the Horologium became a favorite book in cloisters in Germany…". Comper dates it to the close of the Middle Ages.
- Evidence. CRAFT l.262-265: "It became a favourite book in the cloisters at the close of the Middle Ages, not only in Germany, but also in the Netherlands, France, Italy, and England."
- Fix: "Comper writes that by the close of the Middle Ages the Horologium had become a favorite book in cloisters in Germany, the Netherlands, France, Italy and England."

### records.json (these profiles)

- Every brief and card claim checked has a witness, and except as noted the line ranges cover the quoted text. Contested tags all have a contested_claim behind them (Eckhart: recantation, birth, Frankfurt, accusation before 1326; Tauler: the History, birth; Suso: birth, birthplace, death and grave, chapter, how much is Stagel's). The DMR tag on Bihlmeyer's reworking names its owner.
- The records changes for D-B1 (Eckhart offices), D-B3 (Suso IHS) and D-M1 (Eckhart birth sides) are given above.
- **D-M24 (records: three ranges point at blank lines).** DANIELS l.43 (Eckhart, for 1923) is blank; the title page "MÜNSTER i. W. 1923" is l.51. SPENER l.116 (Tauler) is blank; "Leipzig 1841" is l.126. KNOX l.5365 (Suso, Töss near Winterthur) is blank; the footnote "Thoss, near Winterthur, in Switzerland" is l.5366. Fix: cite l.51, l.126 and l.5366.
- Census: these three are not live census entries, so no live-entry check applies. The Who_Scan_Era6 rows (l.84-86) are corrected in the README as the scan's own lines show.

**README (these profiles).**
- **D-M25 (README, Eckhart bullet: two statements wider than the files).** (a) "the 1327 trial acts and the bull of 1329, which are held in full in Denifle's printing". Denifle says that only the last Cologne acts survive, and not all of those, and that he prints only the ones that concern Eckhart directly (DENIFLE-II l.34914-34916: "Von den Kölner Processacten sind uns nur die letzten, und diese nicht alle… erhalten"; l.34965-34967). (b) "His retraction is tagged Contested, as are the questions the card lists as uncertain." "His life" and "His death" carry no contested_claim (nor "The bull's numbers", which D-M5 removes). Fix: "rests on the surviving 1327 acts and the full bull of 1329, in Denifle's printing" and "His retraction is tagged Contested, as are his birth, the Frankfurt priorate and an accusation before 1326."
- If D-B1, D-B2 and D-B3 are fixed, the README's "Held witnesses beyond those the scan cites" should add Pfeiffer's preface (Eckhart) and the History's last chapters (Tauler), and Bihlmeyer's text of the IHS chapter (Suso) (lessons §12, era4 b8 R-M2). This is part of those fixes and is not counted separately.

### Checklist summary

| # | Item | meister-eckhart | johannes-tauler | henry-suso |
|---|---|---|---|---|
| 1 | Each sentence sourced | fail (D-B1); minor (D-M1, D-M3, D-M4) | fail (D-B2); minor (D-M10, D-M14, D-M15, D-M16) | fail (D-B3); minor (D-M17, D-M23) |
| 2 | Quotes verbatim | pass | pass | pass |
| 3 | No invention | pass | minor (D-M10) | pass |
| 4 | Reading aids | minor (D-M2, D-M6, D-M7) | minor (D-M9, D-M11) | minor (D-M18, D-M19, D-M20) |
| 5 | Named witnesses | minor (D-M8) | minor (D-M12) | minor (D-M22) |
| 6 | Partisan witness marked | pass | pass | pass |
| 7 | Contested claims both sides | minor (D-M1) | pass | pass |
| 8 | Common names | pass | pass | minor (D-M22) |
| 9 | One term for one thing | pass | pass | minor (D-M21) |
| 10 | Story, scene, disputes in place, length | pass | minor (D-M9) | minor (D-M19) |
| 11 | Readability | pass (FK 7.7, FRE 65.1) | pass (FK 7.1, FRE 67.7) | pass (FK 5.3, FRE 81.5) |
| 12 | Card order, fields, caveat repeated | minor (D-M5) | minor (D-M13) | fail (D-B3) |
| 13 | Audio tags | pass | pass | pass |
| 14 | Who test | pass | pass | pass |

Consistency across the three: Elsbeth Stagel is spelled and placed the same in the Eckhart and Suso texts ("a nun of Töss"; Knox's "Elizabeth Staglin" kept to records). Eckhart is "Eckhart" in narrator prose everywhere and "Master Eckart" only inside Knox's and Lea's quoted English. The dates agree: Eckhart dead by 1327, Suso freed by him about 1324 in Bihlmeyer's reckoning, Tauler dying in 1361 and Suso in 1365 or 1366 with owners named. Langenberg is "writing in 1902" in both cards that cite him. Denifle is "a Dominican scholar" in the Eckhart and Tauler texts. The drifts are Evans's role (D-M12), Henry of Nördlingen and Denifle unplaced on the Suso card (D-M22), "Life of the Servant" on both the Eckhart and Suso cards (D-M21), and Strasbourg missing from the Tauler card's Eckhart item while the Eckhart card has Eckhart there (D-M16).

### Count

- **Blocking: 3.** D-B1 (Eckhart, false "Evans alone" on his offices), D-B2 (Tauler, false "told by Winkworth alone" for his last months), D-B3 (Suso, false "IHS only on the cloths").
- **Minor: 25.** Eckhart D-M1 to D-M8; Tauler D-M9 to D-M16; Suso D-M17 to D-M23; records D-M24; README D-M25.

| Profile | Words | FK | Flesch | Blocking | Minor |
|---|---|---|---|---|---|
| meister-eckhart | 405 | 7.7 | 65.1 | 1 | 8 |
| johannes-tauler | 403 | 7.1 | 67.7 | 1 | 8 |
| henry-suso | 403 | 5.3 | 81.5 | 1 | 7 |
| records / README | | | | 0 | 2 |

**Scores.** `engine.m1.gates.grade_text`: Eckhart fk 7.713, fre 65.082; Tauler fk 7.082, fre 67.678; Suso fk 5.290, fre 81.457. All three are at the major cap of about 405 words. The fixes above add roughly ten words to Tauler and twenty-five to Suso, so the drafter should trim elsewhere in those two (Suso paragraph 3 or the Little Book lead-in) and rescore. No brief sentence runs past 24 words, and no card sentence past 25.

**Files reviewed (absolute paths)**
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/meister-eckhart.brief.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/meister-eckhart.card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/audio/meister-eckhart.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/johannes-tauler.brief.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/johannes-tauler.card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/audio/johannes-tauler.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/henry-suso.brief.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/henry-suso.card.json
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/audio/henry-suso.audio.txt
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/records.json (entries meister-eckhart, johannes-tauler, henry-suso)
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era6/batch1/README.md
- /home/user/CIC-Project/Build/Ministry/Operations/Audits/2026-11-12_who-scan-era6/Who_Scan_Era6.md (l.84-86)


---

