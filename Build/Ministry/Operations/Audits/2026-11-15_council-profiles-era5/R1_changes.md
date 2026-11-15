# Round 1 changes: era 5 council profiles (2026-11-15)

The coordinator applied the brief fixes; Opus fixers applied the entry and records fixes, each re-checking the evidence in cic/texts/ before applying it. One line per finding.

Briefs after round 1: Clermont 400 words, FK 7.02, Flesch 69.26; Lateran IV 400 words, FK 8.13, Flesch 62.84; Lyon 392 words, FK 8.02, Flesch 64.06. Each audio script equals its brief plus the two tags.

Coordinator's calls: the Clermont truce sentence keeps who the three years applied to (peasants and merchants), which the reviewer's copy dropped; 'His is the fullest account from inside the council' was cut to hold the cap. A-M16 (adding Anna Komnene, William of Tyre and Ibn al-Athir to the Who click) was not applied: writers who only report a council stay off the Who click (Decision-Log, 'Major councils, era 4').

---

## Round 1 changes, Part A — council-of-clermont-1095

Files edited: `Build/Ministry/Features/Church-Family-Tree/Council-Profiles/era5/council-of-clermont-1095.entry.json`, `records.json` key `council-of-clermont-1095` only (re-read before write). Brief and audio not touched; audio equals brief minus its two tags (checked). Both JSON files validate. Every cited line re-read in cic/texts/ before applying.

## Findings

- A-B1 — fixed. Evidence holds (LP1 l.47588-47590, 47681-47682, 47693-47697: "cccx episcoporum", "xiiii kl. decembris", "mxcvi"). Brief: applied by coordinator. Entry: `attended[1]`, `datesNote`, `uncertain[2]`, `uncertain[3]`, `uncertain[4]` rewritten as the review gives; Lambert added to `record` (after William of Tyre); LP1 added to `sources.writtenLater`. Records: claim for Lambert's count, day and year (indiction "vi" as printed), Documented; claim for Duchesne's "vers l'an 1120" and "de main contemporaine", Dominant Modern Reconstruction; the two absent_details rewritten to "A list of names" and "The day of Urban's speech"; Lambert (LP1 l.47694) added to the 1096 side of "The year".
- A-B2 — fixed. Evidence holds (M21 l.11886-11887, 11936-11938, 11944; canon headings at l.12045-12049, 12064-12072, 12071-12077, 12080-12083; the list sits under "Inter caetera Belvacensis concilii decreta"). Brief: applied by coordinator. Entry: `decided[0]` and `uncertain[0]` rewritten; new `decided[3]` with the four canons the review names (investiture, inheritance and penance, sons of concubines and clergy, prebends in two cities); "regulares" rendered "regular clergy", not "canons regular", since the Latin says only regulares. The further items at l.12084-12122 ("Item ejusdem" etc.) were not counted, as the review advises, because their heading to Clermont is not certain in the two-column OCR. Beauvais added to `record` (kind acts) and to `sources.fromTheCouncil`; the Mansi `writtenLater` entry kept. Records: absent_details[0] rewritten; one claim for the Beauvais excerpts' own heading and one claim per canon kept, each witness_kind acts, Documented as headed.
- A-S1 — brief: applied by coordinator. Entry `outcome[5]` brought into line ("daughter of the emperor Alexios"; "In Constantinople" dropped, since no line says where Alexios heard).
- A-S2 — fixed. Quotation marks dropped from "like rivers flowing together from everywhere" in `outcome[5]` (no English Alexiad held; confirmed the Greek at ANNA l.15675-15676).
- A-S3 — fixed. Evidence holds (PL152 l.26613-26614 Ruinart "Ferunt"; l.26632-26636 the editor's "imo reipsa, ut apparet ... fuerit injunctum", Labbe tom. X col. 517; doubt of the apparition l.26582-26604; Petreius "nullo plane argumento probat" l.26653). `uncertain[8]` second sentence and the records contested sides rewritten as the review gives; confidence stays Inferential-Thin.
- A-S4 — fixed. Evidence holds (AASS l.26404-26405 "109S [1095] quo Concilio Claromontano"; l.148148-148149 "mxcvi"). `uncertain[4]` and the modern-reconstruction `record` note rewritten; AASS l.26403-26405 added to the 1095 side of "The year". The Pamplona claim's witness lines corrected to l.26403-26405.
- A-M1 — brief: applied by coordinator. Entry `issue[0]`, `uncertain[0]` and Baldric's `record` note now say he gives "the pope's words, or words like them"; records claim added for "His vel hujuscemodi aliis" (PL166 l.77696-77697).
- A-M2 — brief: applied by coordinator. Records claim "seated in a raised pulpit" changed to "seated in the pulpit ('residens in pulpito')" (PL166 l.77477-77478); records claim added for the call to fight (PL166 l.77629-77631, 77639-77640), which the new brief sentence needs; `issue[0]` adds it too.
- A-M3 — brief: applied by coordinator.
- A-M4 — brief: applied by coordinator.
- A-M5 — brief: applied by coordinator (the truce sentence no longer names pilgrims). Entry keeps the fuller canon 9 detail (Thursday to Sunday, clerics and monks, pilgrims) and its `decided[2]` now reads "above all for pilgrims"; records claim the same, with "ac primum".
- A-M6 — not applied in the brief: the new brief does not mark Anna's "greed" and "broken promises" as her own charges (the review made it conditional on the cap; the brief is at 400 words). Entry `outcome[5]` now says they are her own charges against the Franks. Update: applied to the brief by the coordinator: "her father feared what she called their greed and broken promises"; "to come too" cut to hold the cap (400 words, FK 7.02, Flesch 69.26).
- A-M7 — fixed. Evidence holds (M21 l.27334 "STEPHANI BALUZII", l.27397 "Lemovices meos"). `outcome[7]`, the modern-reconstruction `record` entry, the Mansi `writtenLater` title and author, and the records claim now name Étienne Baluze.
- A-M8 — fixed. Evidence holds (PL166 l.27615 Fabricius, l.27619). Albert's `record` note rewritten; records claim added for the notice.
- A-M9 — fixed. Evidence holds (MIRBT l.11222 one citation, l.11228 "(Codex Cencii)"). `record[0]` note rewritten; records claim on the acts brought into the same wording.
- A-M10 — fixed. Evidence holds (CART l.13313-13315). `decided[8]` (Grenoble) and the records claim now add "or the case was settled before the pope".
- A-M11 — fixed. Evidence holds (PL166 l.65369-65380, "superioris Roberti Frisonis filius" l.65370). `outcome[3]` and the people line "Robert of Flanders" rewritten; records claim adds "son of Robert the Frisian".
- A-M12 — fixed. `calledBy` now ends "where the Latin says only that he planned the first two"; the records contested claim on Vézelay and Le Puy no longer says "a translator's change".
- A-M13 — fixed. Evidence holds (MATT l.15578-15581 Bernard of Valence; l.15582-15584 Daimbert). `traditions[2].note` rewritten as the review gives; the records census-edge claim now says the census generalizes and the held cases are two.
- A-M14 — fixed. Latin dropped from `decided[1]` (canon 2) and `calledBy` (the Grenoble letter); English kept. Records claim for canon 2 now gives "pecuniae" with the OCR "pecmiiae" noted.
- A-M15 — fixed. `modernCountries` now `{"country": "France", "countryId": "Q142", "place": "Clermont"}` (Whitby form confirmed in era4).
- A-M16 — not applied — writers who only report the council stay off the Who click (era 4 rule).

## Census/scan items for Open-Gaps

- Census edge `latin-papal-church-gregorian--latin-church-of-outremer` note says "Latin clergy filled the new sees in the East", generalizing from two held cases (Bernard of Valence at Antioch, Daimbert at Jerusalem; MATT l.15578-15584). Not edited.
- Anna Komnene, William of Tyre and Ibn al-Athir are WHO in the 2026-11-14 rescore (Rescore.md l.50, 197, 203, 216) with no census id; they are left off this council's Who click by the era 4 rule (A-M16).
- No census row gives Clermont as a place; `place` set by name only (A-M15).

## Library header items

- Mansi tomus 20 (Clermont's acts, per Mirbt's "Mansi XX 816. 902") is not in cic/texts/.
- M21 OCR misreads the Clermont heading as "Clavomontano" (l.12045) and is two-column interleaved through l.12040-12122; the headings of the items at l.12084-12122 cannot be assigned to Clermont with confidence from this scan.
- MIRBT l.11226 OCR "pecmiiae" for "pecuniae"; CART l.13307 "Arverniz" for "Arverniae"; AASS l.26404 "109S" for "1095".
- LP1 l.47694 Lambert's indiction prints "vi", which fits neither 1095 nor 1096; left as printed.

---

## R1 changes, part B: fourth-lateran-council-1215 (entry.json and records.json)

Brief and audio: the brief now equals the review's proposed text word for word (blank-line-insensitive diff), and the audio equals the brief plus the two tags. Both JSON files validate. The entry still reads "about 2 minutes 30 seconds" (400 words).

Note: another agent's Clermont commit (b294e985) picked up my records.json changes under this key, because it staged the whole file. Only the later Cathar-note edit and the entry are uncommitted.

## Findings

- B-B1: fixed. The entry's `attended[5]`, `uncertain[4]`, the Francis `people` part and Glassberger's `record` note now use the review's text. Added a Frachet `record` row and two `writtenLater` rows (Reichert's Latin, Conway's English). In records: `contested_claims` on Francis now reads "at Rome during the council", with the review's sides. Added a Frachet claim (Inferential-Thin) and a claim for the c. 1260 date (Conway's introduction, l.160-179, 211). Checked: Reichert l.1743, 1748-1777; Conway l.996-1050.
- B-B2: fixed. The claim is now about the Psalterium decem chordarum as Buonaiuti quotes it, cited l.17741-17856, with the siglum at l.3009. The `record` witness and the `sources` row were renamed as the review gives them. `absent_details` (Joachim's tract) now names the Psalterium in place of the Tractatus. Checked.
- B-B3: fixed. The source row is split into Jordan's Libellus and Bartholomew of Trent's Vita altera. `outcome[0]` now names Bartholomew. Added a Bartholomew `record` row. The records claim (Honorius confirmed) names Bartholomew and cites l.94619-94624. Checked.
- B-B4: fixed. The brief part was applied by the coordinator. The Bollandists' `record` note now gives the review's text. Added a `fromTheCouncil` row for Glassberger's editors' note. Records: added a claim for the Salimbene quotation (l.7319-7323), and the extracts claim now says "Most canons". One addition beyond the review: `uncertain[0]` and `absent_details[0]` also name the canon 1 phrases quoted in Cajetan's commentary in the Leonine Summa (l.30506-30512, 33675-33677; the file header names Cajetan). That avoids a new false "only". A claim was added for it.
- B-B5: fixed. Vitry's note now reads "later bishop of Acre; no source among ours puts him at the council". Added a claim for letter I's "Acconensis ecclesie minister humilis" (l.5860-5861).
- B-B6: fixed, with changed wording. The review's "a dualist scripture the Cathars used" has no held line behind it: Döllinger's Vienna text carries no attribution. Döllinger does print it in a volume of documents "zur Geschichte der Valdesier und Katharer", and notes a second text in the Carcassonne inquisition records (l.132-140). The note now says exactly that. "Waldensian poems" became "the Waldensian poem the Nobla Leiczon".
- B-S1: brief, applied by the coordinator. `decided[5]` and the claim were already right.
- B-S2: fixed. `decided[2]` uses the review's wording. The records claim was brought into line with it (Mirbt l.12365-12384). Checked.
- B-S3: fixed. `uncertain[5]` uses the review's text. `contested_claims` on canon 13 was removed and folded into the Salimbene claim, which now cites both Coulton l.13489-13492 and Glassberger l.7319-7323.
- B-S4: fixed. Joachim's `record` row is now "later narrative", with the review's note. Both Joachim claims are now "later narrative". Added a claim that Joachim died in 1202 (Ehrle-Denifle l.3350). The cite of the era 4 pattern-gap entry is for the coordinator's Open-Gaps entry.
- B-S5: brief, applied by the coordinator.
- B-S6: census items, not edited. Listed below.
- B-M1: brief, applied by the coordinator.
- B-M2: brief parts (Dominic as a Spanish preacher, the abbot Joachim) applied by the coordinator. In the entry, `people` "Almaric" is now "Almaric of Paris", with the review's part. Records: added claims for the Mansi notice on Dominic "Hispanus" (l.1048-1050) and on Almaric at Paris (l.1056-1058). "Augustine's" was left as is, per the review.
- B-M3: brief, applied by the coordinator. `decided[1]` was already right.
- B-M4: brief, applied by the coordinator.
- B-M5: fixed. `outcome[1]` now gives Innocent's death with its witnesses, and "In a letter Röhricht dates to October 1216". `outcome[3]` now says "by Denifle's dating". `outcome[6]` now says "In a letter Röhricht dates to the end of March 1217". Added claims for Denifle's 1255 (l.5148-5151) and for Röhricht's heading to letter II. That heading is at l.6116, not l.6112 as the review says.
- B-M6: fixed. `issue[4]`, Denzinger's `record` note and two records claims now read "the headings in Denzinger's Enchiridion, in Clemens Bannwart's edition of 1911". The brief keeps "two modern editors" (the optional change was not taken).
- B-M7: fixed. The Pedalion's `record` row and both Pedalion claims are now "later narrative".
- B-M8: fixed. The `teaser` is now the review's three sentences. `knownFor` is the 25-word version, and Joachim stays in the brief.
- B-M9: fixed. Added `record` rows for the Assisi catalogue (Ehrle identifies it as Richard of Poitiers's), the Pulkava variant, the Anagni protocol, Covel (the review's note) and Alishan (a Mekhitarist, per his file header). Added a `writtenLater` row for Denifle's article and the Anagni protocol. Added a claim for Ehrle's identification (l.26363-26366).
- B-M10: brief, an optional close; not taken. The proposed brief keeps the Vitry close, and the choice is Mark's.
- B-M11: fixed. `issue[2]` and the canon 2 claim now carry "and which neither begets nor is begotten nor proceeds" (Denzinger l.13947-13949).
- B-M12: fixed. `attended[4]` uses the review's wording.
- B-M13: fixed in records. `claims[0]` is split into two claims: the two men of Toulouse (l.93023-93026), and Dominic joining Fulk (l.93039-93050), with a note that the brief's first sentence joins the two. The brief was left as is, per the review.

## Census/scan items for Open-Gaps

1. `latin-papal-church-gregorian` `documentedStories[1]`: "more than four hundred bishops and eight hundred abbots ... seventy-one constitutions". No held line gives 800 abbots or 70 or 71 constitutions. The held counts are Hethum's 422 bishops and 72 archbishops, and al-Duwayhi's 411 bishops.
2. `maronite-christianity` (`why`, `documentedStories[0]`):
   - "to settle its terms" has no held line behind it;
   - the pallium rests on al-Duwayhi alone, a second witness;
   - the bull Quia divinae sapientiae is not held.
3. Parties with no census tradition at the date:
   - the Irish bishops: `medieval-irish-christianity` ends in 1169, and there is no era 5 Irish entry;
   - Dominic's preachers are "Gathered" in 1215, but the census start of `the-dominican-order` is 1216;
   - Covel's two Latin patriarchs of Constantinople and Jerusalem: there is no row for the Latin church of Constantinople, and `latin-church-of-outremer` is not in `traditions`.
4. Pattern gap: no witness kind fits a writer earlier than the meeting (Joachim). Cite era 4's entry, "Pattern gap: no witness kind fits a writer earlier than the meeting" (2026-11-14).

Owner: the coordinator (census text and map build).

## Library header items

- None blocking. For a later header pass:
  - Reichert's Frachet header says to add 11 to its cited OCR lines;
  - Conway's header says to add 10.
- The Döllinger II header's content note gives only "the contents (Inhalt) at about OCR line 76". A note naming the Interrogatio Iohannis and the inquisitors' Cathar documents would help later searches.

---

## R1 changes: second-council-of-lyon-1274 (part C)

The brief and audio were not touched. The brief on disk is byte-identical to R1C/second-council-of-lyon-1274.fixed.txt (392 words). Its audio line 15 carries "flogged, ill-treated and exiled". I re-checked all evidence lines in cic/texts/ before applying each finding.

- C-B1: fixed. The brief part was applied by the coordinator. Entry `uncertain[0]` now says "from later writers, the earliest the patriarch list of Nikephoros Kallistos from about 1300". `issue[3]`, `traditions` (byzantine) and the `record` witness now name Nikephoros Kallistos. The record note reads "written about 1300, under Andronikos II; ...". The `sources` author is "Nikephoros Kallistos, in Migne, PG 147". In records, the `absent_details` Greek-account note uses the review's wording. A new claim gives the list's date markers (ends with John XII and Athanasios's return under Andronikos II, "most pious emperor", year 6800 = 1292 in Migne's bracket; PG 147 l.283-284, 21320-21336, 21339, 21374-21377). The Joseph contested claim and the claim at l.21368-21378 name the author. Palamas's Antepigraphai (PG 150 l.52640-52649) was not cited: those lines are a catalogue title for the work, not its text, so I make no claim that the text is held.
- C-B2: fixed. Records `contested_claims` "Michael VIII's motive" now has the Recueil editors' side (l.54168-54172), with the census sentence reworded as the review asked, and is raised to Contested. A matching claim was added (modern reconstruction, Contested). Entry `uncertain[6]` was replaced with the review's text.
- C-S1: fixed. Entry `decided[3]` was replaced with the review's text. A new `uncertain` item covers what the mendicant decree did. A new contested claim "What the mendicant decree did" (Contested) covers Glassberger, Salimbene, Clement XIV and Lea. Salimbene was added to `record` (later narrative) and to `sources.writtenLater` (English, Coulton 1907). The `absent_details` note now lists Salimbene, Glassberger, Eubel, Clement XIV and Lea. Five claims were added: Salimbene l.16092-16094, l.15763-15766 and l.13617-13619; Glassberger's editors' Latin l.7323-7328; Eubel l.14488-14489. The Carmelites tradition note now records Glassberger's disagreement with Lea.
- C-S2: fixed. Tocco and the canonization depositions moved to `sources.writtenLater`, and `fromThoseThere` was removed.
- C-S3: not applied here, by design (census items are logged by the coordinator). The records motive point keeps C-B2's wording. All four points are listed below.
- C-S4: brief: applied by coordinator (Bannwart is named; "The chronicle printed under Sphrantzes's name").
- C-M1: fixed. Brief: applied by coordinator. Entry `outcome[1]` and the records claim at l.1255-1260 now say "flogged, ill-treated and exiled". The records claim notes the Greek ἐκάκωσε and Bekker's Latin "mutilavit" (l.1290).
- C-M2: fixed. `attended[1]` now reads "Germanos, who had been patriarch some years before, between Arsenios and Joseph".
- C-M3: fixed. `uncertain[8]` was replaced with the review's text ("acts were corrupted"). In the records contested claim, Doukas now sits on a separate side ("a union sworn under oaths and anathemas, set beside Florence", l.14310-14316).
- C-M4: brief: applied by coordinator.
- C-M5: brief: applied by coordinator.
- C-M6: brief: applied by coordinator (Kalekas now starts paragraph 4).
- C-M7: fixed. `attended[5]` was replaced with the review's text. The records claim at l.116095-116100 was reworded: Thomas was on his way in Lent, and the witness did not remember the month or day.
- C-M8: fixed. `decided[1]` now reads "that the Roman church makes the eucharist from unleavened bread". A records claim was added for purgatory, seven sacraments and azymes (Denzinger l.14506-14612). `outcome[7]` and the Oxford records claim were reworded to the bull's "expected soon to fall to the apostolic see" (Bullarium V l.14399-14409).
- C-M9: fixed. In the Kalekas contested claim, "per the dossier," and ", not rechecked" were deleted; both lines held when re-checked. The Dominican Order is now "Affected", with the review's note. `informalName` was removed.

Other consistency: `briefLength` stays "about 2 minutes 30 seconds" (392 words, about 2:27 at 160 wpm). The teaser and knownFor still agree with the new brief. Records claims cover every factual sentence of the new brief, including the "about 1300" sentence (new claim). Both JSON files validate. records.json differs from HEAD only under this key.

## Census/scan items for Open-Gaps

Proposed entry: "Census: byzantine-church-after-1054 and the Second Council of Lyon (2026-11-15)".
1. `why`/`longDescription`: "In 1274 Emperor Michael VIII needed help from the West". This is a held modern editor's view (Recueil, rhc-armeniens l.54168-54172), not a medieval witness's.
2. `sourcing`: "Rich: ... Lyons 1274 acta". The acts are not held; only three texts survive, in modern extracts (Denzinger; Mirbt no. 306).
3. `documentedStories`, "Michael VIII Punishes the Anti-Unionists": it rests on Pachymeres and Michael's autobiography, neither held. It says "the Byzantine church refused the emperor a Christian burial", but the held witnesses differ and none says the church refused it. Boulliau: no funeral pomp (doukas l.32499-32501). Creyghton: cast out unburied (syropoulos l.3090-3094). Guillaume Adam: the monks' oath (rhc-armeniens l.63744-63748).
4. The same story's "with the exception of a compliant patriarch" conflicts with the Recueil note that Bekkos at first resisted and was imprisoned (rhc-armeniens l.63805-63812).

Scan/coverage notes (from the review's coordinator notes):
- `Councils_Scan.md` l.77 lists `the-waldensians` for Lyon 1274. No held line ties them to Lyon II, and the entry rightly omits them.
- Option, not a defect: `latin-church-of-outremer` could be "Gathered" (Paul, bishop of Tripoli, presided by the Franciscan account).
- The Augustinian Hermits, the Sack friars and the Apostles have no census tradition.
- Pachymeres (the Bonn edition, Bekker 1835, is public domain) would change the profile's "from the time" absence if acquired.

## Library header items

None found. The headers of the Salimbene (Coulton 1907) and Denzinger (Bannwart) files were read and match the citations used. The PG 147 catalogue's attribution to Nikephoros Kallistos follows Migne's heading (l.283-284, l.21339). If the Library header for that file does not record that the patriarch catalogue is attributed to him, it could say so.
