# Era 10, P2-E10h: adversarial review, Round 1

Reviewer: independent Opus 5.5 review · 2026-11-09 · Round 1 (full)

**Object.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_P2E10h_Proposed.json` (15 new rows, IX.59 to IX.73; 61 register edits: 27 replace, 23 addItem, 10 set, 1 removeItem) and `CiC_Step0_Era10_P2E10h_Trace.md`, on branch `claude/era10-p2e10h` at 0eb60f235, against `cic-website/data/world-census.json`. The brief names release 23. The file on the branch is release 24 (2026-11-09, 307 movements), and that is what I applied against.

**Rules applied.** Atlas Decision-Log 2026-11-09, "ERA 10 GLOBAL SWEEP GATE: Mark rules all 71 questions": every answer is the Rec. of its question in `CiC_Step0_Era10_GlobalSweep_V1_0.md` §7 (G-80 to G-150). The change order on evidence for recent movements (2026-11-08): an [S] or snippet-only item never carries a sentence. The era 10 change orders: history runs 1906 to c. 2010; the living mark means alive today; its evidence sits only in `livingEvidence`, graded CD/CR under `Design/CiC_Step0_LivingEra_Protocol_Addendum_V1_0.md` R3. CLAUDE.md: never invent; the five formation_confidence grades, with contested claims shown as contested; B2 participant copy (FK 8 to 10, FRE ≥ 60 as a target, no sentence past 25 words, active voice, American spelling, no AI tells, no process narration).

**Method.**
- Applied the proposal with my own applier (`scratchpad/e10h-rev1/myapply.py`), not the drafters'. Edits apply in order. Every `replace` and `removeItem` old matched exactly once. Every `set` old matched release 24. The `sources.work` and `sources[0].work` edits each matched one source once. `meta.totalEntries` 307→322, Pre-Survey Candidate 226→241.
- `node tools/validate-census.mjs applied.json --atlas cft-website/index.html`: 322 movements, 578 edges, 10 eras, **0 errors, 2 warnings**. Both warnings are pre-existing shortName warnings on era 1 rows.
- Read every field of the 15 rows and every edited field after the edit, against the trace and the record's evidence item.
- Re-verified 27 cited works and key dates by WebFetch and WebSearch. Every item the finishing pass opened was re-opened from its own URL: Awiti 2023 (full text), Guamán 2008 (full text), Teel 1989 (full text), Peyrouse 2004 (Cambridge extract), Hansard 23 March 1964, PA-X 337, Rolandsen 2011 (PRIO abstract) and Zink 2018. Also: Kim 2019 (thesis text), Ticozzi (full PDF), *Ad Apostolorum Principis* (vatican.va), both UCCJ confessions (uccj.org), Longman (Cambridge Core), Werner et al. 2000 (JAH review listing: Paulines, 2000, 688 pp.), Nikkel 2001 (Edinburgh archive and DACB), Chesnut 2003, *Christianity Today* 27 March 1964 and November 1974, the 1965 Joint Declaration, the FABC history page, Kiwanuka's dates, the 1988 Zaire missal, the 1965 Polish letter, El Shaddai's founding year, jurnalul.ro, the Vatican's biography of Cardinal Todea, Mahieu 2004 (MPI working paper 69) and Achútegui and Bernad.
- Checked each ruled option against what was drafted or withheld. Checked the atlas code (`cft-website/index.html`, `FAM` and `famOf`) for the new 4.5 lane.
- Readability with `engine/m7/readability.py`: per row (why, longDescription, legacy, relationsSummary, statusDescription, teaser, sourcing, floorNote), and per sentence for length.
- No repo file was edited. No metered model call was made.

---

## SUBSTANTIAL findings

**S-1. IX.44: the inserted Titicaca line leaves "Its" pointing at the adobe building, and makes Camacho one of Adventism's first converts.**
- *Location:* registerEdits[55], IX.44 `longDescription`.
- *Evidence:*
  - After the edit the field reads: "…The Stahls lived in an adobe building that served as a school on weekdays and a place of worship on Sabbaths. Its own internal arguments, including the long controversy that followed the book Questions on Doctrine, are on that same public record…". "Its" now reads as the building. This damages an existing sentence (the same defect as P2-E10b S-5).
  - "Camacho … was among the first Adventist converts." In an entry on the worldwide Adventist church, this reads as one of the movement's first converts, decades after the 1860s. Teel (p. 213, re-read) says "uno de los primeros conversos adventistas" in a passage about the Peruvian altiplano. The sentence drops the scope its source gives it.
- *Fix:* registerEdits[55] `new` =
  "In 1911 Ferdinand and Ana Stahl joined Manuel Camacho at Utawilaya, in Platería district, Puno province, on the Peruvian side of Lake Titicaca. Camacho, an Indigenous visionary, was one of the first Adventist converts on the altiplano. He had opened a free school in his home about 1902. The Stahls lived in an adobe building that served as a school on weekdays and a place of worship on Sabbaths. The church's own internal arguments, including"

**S-2. IX.24: "The Lausanne congress of 1974 rejected it" overstates the cited source.**
- *Location:* registerEdits[14], IX.24 `relationsSummary`, and the note on registerEdits[15].
- *Evidence:* the cited item, *Christianity Today*, "What's Behind the Idea of a Missionary Moratorium?" (November 1974), was re-read. It says only that "the idea of a broad moratorium appeared to be rejected by most leaders". It also quotes the Lausanne Covenant: "A reduction of foreign missionaries and money in an evangelized country may sometimes be necessary". The congress passed no rejection, and its covenant partly allowed what Gatu asked. The sentence presents a reported mood as a formal act, and the record's "Rejected at Lausanne 1974" condenses the same item too far.
- *Fix:*
  - registerEdits[14] `new` = "Graham's evangelistic association was incorporated in 1950. In 1971 the Kenyan theologian John Gatu called for a moratorium on missionaries. At Lausanne in 1974 most leaders appeared to reject a broad moratorium. Still, the Lausanne Covenant allowed that fewer foreign missionaries might sometimes help a national church grow."
  - registerEdits[15] `note` = "Records Gatu's call and reports that at Lausanne a broad moratorium 'appeared to be rejected by most leaders'. Quotes the Covenant's allowance for a reduction of foreign missionaries."

**S-3. IX.73: the Holy See's act is dated 12 March 1990 on a source that does not carry it, and the Holy See's own date is 14 March.**
- *Location:* IX.73 `why` (sentence 3), `longDescription` (last sentence), `sources[0].note`, `statusDescription` and `sourcing`.
- *Evidence:*
  - The cited page (jurnalul.ro, "Discordie între ortodocşi şi greco-catolici") was re-read twice. It contains no March date, and it does not mention the Holy See, the Vatican, Todea or a metropolitan. Its dates are 22 and 31 December 1989 and 24 April 1990. It quotes Decree-Law 126 of 24 April 1990, which cites Decree 358/1948 and Decree-Law 9 of 31 December 1989.
  - The Holy See Press Office's biography of Cardinal Alexandru Todea says that on 14 March 1990 he "was promoted to the Metropolitan See of Făgăraş and Alba Iulia". On that day John Paul II named bishops to all five dioceses.
  - Jurnalul does not give the day of Decree 358 either. Stéphanie Mahieu, *Legal Recognition and Recovery of Property* (Max Planck Institute for Social Anthropology Working Paper 69, Halle, 2004), re-read, gives "On December 1, 1948, Decree no. 358" and Decree-Law no. 9 of 31 December 1989.
- *Fix:*
  - `why` = "On 1 December 1948 the Romanian state dissolved the Greek Catholic Church by Decree 358. Its property passed to the state, and its churches to the Orthodox church. On 31 December 1989 a decree-law restored it. On 14 March 1990 John Paul II named Alexandru Todea its metropolitan."
  - `longDescription`, replace "On 12 March 1990 the Holy See recognized its metropolitan." with "On 14 March 1990 John Paul II named Alexandru Todea metropolitan of Făgăraș and Alba Iulia."
  - `sources[0]` = {"work": "Decree-Law 126 of 24 April 1990, as reproduced in Jurnalul Național (jurnalul.ro), citing Decree 358/1948 and Decree-Law 9 of 31 December 1989", "type": "reference", "note": "The repeal of 1989 and the restitution decree of 1990."}
  - Add {"work": "Stéphanie Mahieu, Legal Recognition and Recovery of Property: Contested Restitution of the Romanian Greek Catholic Church Patrimony, Max Planck Institute for Social Anthropology Working Paper 69 (Halle/Saale, 2004)", "type": "secondary", "note": "Decree 358 of 1 December 1948 and Decree-Law 9 of 31 December 1989."}
  - Add {"work": "Holy See Press Office, biography of Cardinal Alexandru Todea", "type": "reference", "note": "Promoted to the Metropolitan See of Făgăraș and Alba Iulia on 14 March 1990."}
  - `statusDescription`, sentence 2 = "It rests on the decrees of 1948 and 1989, read through a press account and a study of the restitution disputes, and on a study of the neighboring Czechoslovak case."
  - `sourcing`, sentence 2 = "The decree that dissolved the church in 1948 and the decree-law that restored it in 1989 are verified, with the naming of its metropolitan in March 1990."

**S-4. IX.72: the events of 1054 are described against the Joint Declaration's own words.**
- *Location:* IX.72 `why` (sentences 3 and 4) and `longDescription` (sentences 5 and 6).
- *Evidence:* the rows say "By those sentences Rome and Constantinople had cut each other off" and "Rome and Constantinople had passed them on each other in 1054". The Declaration (vatican.va, re-read) says something different. Its ¶2: the sentence was "leveled against the Patriarch Michael Cerularius and two other persons by the legate of the Roman See under the leadership of Cardinal Humbertus", and the legates were then "the object of a similar sentence pronounced by the patriarch and the Synod of Constantinople". Its ¶3: the censures concerned "the persons concerned and not the Churches". The row's main cited source contradicts the row. That is misleading on a point scholars hold settled.
- *Fix:*
  - `why` = "In 1907 a brotherhood of theologians called Zoe was founded in Greece. On 7 December 1965 Pope Paul VI and Ecumenical Patriarch Athenagoras I issued a joint declaration. They removed from memory the sentences of excommunication of 1054. In 1054 Rome's legates had excommunicated Patriarch Michael Cerularius, and his synod had condemned the legates in turn."
  - `longDescription`, replace "It lifted the sentences of excommunication. Rome and Constantinople had passed them on each other in 1054." with "It removed from memory the sentences of excommunication of 1054. Rome's legates had excommunicated Patriarch Michael Cerularius, and his synod had condemned the legates in turn. The declaration said those sentences struck persons, not the churches."

**S-5. El Shaddai: a new sentence carries the [S] date, and IX.66 cites a source entry that names no work.**
- *Location:* registerEdits[52], IX.11 `relationsSummary`. IX.66 `sources[0]` and the Velarde voice.
- *Evidence:*
  - The Asia notes record that "the record marks the date [S]; it rests on census text only".
  - registerEdits[52] is a new sentence, not a move: "El Shaddai, a Catholic movement founded in the Philippines by Mike Velarde in 1984, is told in the entry on Philippine Catholicism." It carries the [S] founder and date. Under the change order, an [S] item never carries a sentence.
  - IX.66 `sources[0]` is {"work": "El Shaddai (1984, Velarde)", "type": "primary", "note": "The movement's own record, as named before in the Global South Pentecostal entry."}. That is a fragment cut from IX.11's composite source line, not a work. No El Shaddai text was opened, so "The movement's own record" describes something not in hand.
  - My search finds 1984 widely given (20 August 1984), with 1981 given for the radio arm, so the date is probably right. It still rests on no verified item in this slice.
- *Fix:*
  - registerEdits[52] `new` = "Child of Azusa + AIC lines; the century's growing edge. El Shaddai, a Catholic movement in the Philippines, is told in the entry on Philippine Catholicism."
  - IX.66: remove `sources[0]`.
  - Either remove the voice "Mike Velarde — founder of El Shaddai in the Philippines in 1984" from IX.66 until a verified item carries it, or verify it now on Wiegele's *Investing in Miracles* (the page that dates the founding) and add the page to Wiegele's source note.
  - Add the founding date and founder to the notDrafted list and the source-research wants, so the gap does not go quiet.

---

## MINOR findings

**M-1. The 4.5 lane has no entry in the atlas's lane table.**
- The census labels ("4<->5 bridge (Africa / Latin West)" / "Africa / Latin West — bridge") follow the 3<->5 and 5<->6 precedent, and I accept them.
- But `cft-website/index.html` holds `FAM` entries for 3.5, 3.6 and 5.5, and none for 4.5. `famOf(4.5)` ties between 4 and 5 and returns Africa, so IX.59 draws in Africa's color and lane label. The lane has no `LANE_PARENT_FROM_RECORD` entry and no inbound edge either, so it starts unattached.
- *Fix* (a front-end change, outside this file): add `{k:4.5, lbl:"Africa/Latin bridge", …}` to `FAM`, and `4.5:4` to `LANE_PARENT_FROM_RECORD`, or draft the VIII.43 → IX.59 edge the Africa notes suggest.

**M-2. Four sentences run past 25 words** (the notes' "No sentence over 25 words" is wrong).
- IX.59 `teaser` (27 words) = "Africa, 1906 to 2010 — the Catholic Church from Joseph Kiwanuka's consecration in 1939 to the African Synod of 1994, with a missal for Zaire and the question of Rwanda."
- IX.61 `sourcing` (31 words) = "Moderate to rich: a 688-page history of the Sudanese church and a study of Dinka Christianity, both from Paulines Publications Africa in Nairobi. A Baylor study of Dinka Anglicanism adds to them."
- IX.62 `sourcing` (28 words) = "Rich: the bishops' own conference documents in Spanish and Portuguese, and CEHILA's history in many volumes. A Cambridge survey of 2008 and Jean Meyer's history of the Cristero War add to them."
- IX.70 `relationsSummary` sentence 2 (26 words) = "It stands beside two Rome-centered entries. One tells the Catholic Church from Pius X to the Council, and the other the parish after the Second Vatican Council."

**M-3. shortNames.**
- IX.62 "Latin America 20c" does not say Catholic and uses an abbreviation found nowhere else. *Fix:* "Latin Am. Catholic" (18 characters), to pair with IX.63's "Latin Am. Protestant".
- The others are acceptable. "Romanian United" follows the church's own name, and "IFI (Philippines)" its own initials. "Romanian Greek Cath." (20) would be clearer to most participants. That is a judgment for the coordinator, not a defect.

**M-4. IX.69 brings in a present-tense claim.** "Most belong to European minorities that came with Russian colonization…" *Fix:* "Most belonged to European minorities that came with Russian colonization in the eighteenth and nineteenth centuries."

**M-5. "In 2010 it was a living church" is repeated as filler.** It appears in the legacy of IX.69, IX.70, IX.71 ("these were living churches"), IX.72 ("both were living churches") and IX.73. No item dated 2010 stands behind it. It echoes the living mark inside the history text, and it repeats as a template phrase. *Fix:* delete the sentence in all five. In IX.73, keep its second clause as "It had been legal again since 1989."

**M-6. IX.63: an English rendering sits in quotation marks.** "aims to show how Pentecostalism there became 'quichuanized'". The abstract's words are «se "quichuaniza"». *Fix:* "Her book of 2004 sets out to show how Pentecostalism there took on a Quichua form."

**M-7. IX.65 `why` overstates the 1946 hierarchy.** "each under its own bishop". Ticozzi (re-read) counts 20 archdioceses, 79 dioceses and 38 apostolic prefectures. Prefectures are not under bishops, and only 21 of the 28 Chinese-led units had Chinese bishops. *Fix:* "Twenty years later Pius XII set up a full hierarchy of dioceses in China."

**M-8. IX.67: Achútegui and Bernad's dates.** Volume 1 is 1960 (revised 1961) and volume 2 is 1966. Two volumes of documents followed in 1971 and 1972.
- *Fix* `sourcing`, sentence 3 = "Pedro de Achútegui and Miguel Bernad, both Jesuits, wrote a two-volume study of its founder (1960, 1966)."
- *Fix* in the source and the voice: "(1960-66)" → "(vols. 1-2, 1960-66)".
- Also in `why`, "confessed the Trinity without doubt" → "plainly confessed the Trinity".

**M-9. IX.59: hedge phrasing, and Longman's year.**
- `why` sentence 2, "He is described as the first…", is a passive hedge with no named describer. *Fix:* "He was the first sub-Saharan African made a Catholic bishop in the modern mission era." This keeps the narrow claim the record requires.
- Cambridge Core gives Longman's print publication as 7 September 2009 (online 2010). *Fix:* "Timothy Longman argued that the churches had aligned with the state…" (drop "in 2010"), and give the source as "(Cambridge University Press, 2009)" in IX.59 and in registerEdits[1].
- Spelling consistency: "St Peter's" (IX.59) → "St. Peter's", or "Saint Peter's" as in IX.65.

**M-10. Order and duplication in edited rows.**
- IX.21: the Prešov sentences come after the 1989 legalization, so the story jumps back to 1950. *Fix:* attach them after "…none took part." (registerEdits[43] then uses that as `old`).
- IX.8: the Medellín pointer now sits in both `longDescription` and `relationsSummary`. *Fix:* registerEdits[17] `new` = "continued inside Latin American church life. The bishops met again at Puebla in 1979; both meetings are told in the entry on Latin American Catholicism, the parent of this one."

**M-11. IX.44: Peru becomes the global Adventist entry's only modern country.**
- G-142 (a) says "adding Peru to its countries", and the validator needs the place on the label and in the region text. So the region and placeLabel changes are forced, and I accept them as carrying out the ruling.
- But IX.44's `modernCountries` was empty before. The map will now tie a North American-born world church to Peru alone. The United States has a gazetteer ID in the census (Q30).
- Flag this to the coordinator (a cross-row call, not this slice's) rather than fixing it here.

**M-12. Trace and notes housekeeping.**
- The C7 table in the trace still says the 1955 and 2005 events, the 1964 expulsion and Zink are [S], and that "a verify pass is needed". The finishing pass superseded this. *Fix:* strike or mark the superseded rows, so a reader is not told the published text rests on [S].
- G-102 (a) asks the Korean row to carry the March First Movement and the growth decades. Both are rightly withheld (1919 is [S]), but neither is in the Asia notDrafted list. *Fix:* add them, and log them in the world's gap tracking.
- Zink 2018 is typed "reference" in IX.61. It is a monograph: "secondary".

**M-13. IX.61 and the 1964 expulsion.** "In March 1964 the government expelled foreign missionaries" agrees with its sources (Hansard of 23 March; *CT* of 27 March, "this month"). The order itself was issued on 27 February 1964 (*Fides*; *CT* in a later report), and departures ran to about 9 March. *Optional:* "In February and March 1964 the government expelled foreign missionaries", if a verified item carrying 27 February is added.

**M-14. Commentary already in edited live rows.** IX.11 ("Child of Azusa + AIC lines"; "this map does not pretend otherwise"), IX.4 ("which is why this map takes them one at a time") and IX.7 ("The map treats these as four distinct movements…") carry map commentary in participant copy. CLAUDE.md asks the PR that edits a live file to remove the commentary already in it. Run `tools/check_live_commentary.py --surface cic-website` at apply, and clear what it reports for these rows.

**M-15. Readability (judgment).**
- Whole-row FK runs 7.2 to 9.4, inside the band.
- FRE runs 46.4 (IX.63) to 67.4 (IX.70). Most rows sit at 50 to 57, and the added register text sits at 48.2.
- The shortfall comes mainly from institution and personal names (CLADE, CONELA, FEINE, Huampaní, Oaxtepec; Sremski Karlovci, Tomos). Sentence length averages 12 to 16 words.
- FRE ≥ 60 is a target principle, not a bar, so this is not substantial. IX.63 is the one row worth a pass: give one sentence to the 1977-1982 council meetings, and cut "This Latin American Council of Churches, CLAI," to "CLAI".

---

## Judgment calls ruled

- **IX.44 region and placeLabel with Peru.** Accepted. The validator ties `modernCountries` to the place label and the label to the region text, so G-142 (a)'s "adding Peru to its countries" cannot be carried out without both. See M-11 for the one consequence to raise.
- **IX.61 opening in 1955.** Accepted. 1955 is the ruled window (G-86 (a)). The text shows the dating question openly: historians usually trace the war to Torit in 1955, and Rolandsen dates civil war proper from 1963, full-scale from late 1963 (PRIO abstract, re-read). The contested point is shown as contested, not settled.
- **The 4.5 lane label.** Accepted as census text. The atlas needs a lane-table entry (M-1).
- **shortNames.** See M-3. One change.
- **Rows at FRE 47 to 55.** Not substantial. See M-15.

## Rulings carried out (checked)

- **Rows.** The 15 rows match the Decision-Log's corrected count of 14 "enter" candidates plus E3b. IX.59 is on the bridge lane (G-80 (c)), and the Catholic regional rows are in lane 5. IX.61 is its own row (G-86 (a)). The Cristero line is inside LA-1 on the G-93 fallback (b).
- **Named lines placed:**
  - Rwanda in C1, with an IX.3 relations line (G-83 (a)).
  - Spartas in IX.4 (G-87 (a)).
  - The AACC and the moratorium in IX.46 and IX.24, and the 1956 priests in C1 (G-88 (a)).
  - Medellín and Puebla moved from IX.8 to LA-1 (G-90 (a)).
  - The CCR in Brazil in IX.7 (G-95 (a), G-133 (c)).
  - IX.15 Mexico (G-98 (a)) and IX.20 Jamaica (G-99 (a)), both with "Latin America" (G-134 (a)).
  - Guatemala in LA-5 (G-101 (a)).
  - Indian Pentecostalism in IX.11 (G-113 (a)), the FABC in IX.23 (G-114 (a)) and Indonesian Catholics in IX.37 (G-115 (a)).
  - The Japanese Orthodox cross-reference in IX.48 (G-121 (a)).
  - E1's kin lines (G-122 (a)), Lithuania in E2 (G-123 (a)), and Prešov in IX.21 (G-129 (a)).
  - The MECC in IX.46 (G-141 (a)).
  - Proaño in LA-1, FEINE in LA-5 and the Titicaca Adventists in IX.44 (G-142 (a)).
  - Central Asia in E1 (G-148 (a)).
- **Overlap moves:**
  - El Shaddai is out of IX.11's longDescription, voice, source, region and teaser, and into IX.66 (G-107 (a), G-132 (b), G-133 (c)), subject to S-5.
  - IX.11's dates are corrected to 1910 (G-135 (c)).
  - The Pará story stays until LA-2 enters, and that is correct.
- **Withheld, correctly, on [S] or unverified items:**
  - From Africa: the TRC legacy (G-81), the Church of Pentecost (G-84), Shembe, Legio Maria, Chilembwe, Toko, Milingo and Sant'Egidio.
  - From Asia: minjung (G-118); Timor-Leste, Uniting Church and Hillsong; the Japanese Orthodox after 1906 told as history (G-121).
  - From the East: E9's line (G-130 (b)), E10 (G-131 (a)), E11 and Mukachevo.
  - The SIL (G-142, contested and unverified), and the deported Catholics and Lutherans (G-148).
  - The March First Movement is also withheld correctly, but it is unlisted (M-12).
- **Living marks.** Each mark's evidence sits only in `livingEvidence` and in a source flagged "for the living mark only". The CR grades on unverified journalism or own voice follow §2d and R3. IX.61's CD rests on Zink 2018, scholarship whose subject and publisher are confirmed by the JEH review. That is acceptable. Nothing in history text is dated after 2010.

## Re-verification summary

Confirmed as drafted:
- Teel, Allpanchis 21.33 (1989): 209-248, p. 213 and 214 wording.
- Awiti 2023: 29 May 1954; 29 January 1985; CEAS 1960; ERPE 19 March 1962.
- Guamán 2008: FEINE 1980; Chimborazo 1966; more than 1,500 congregations; "Indígena ecuatoriano".
- Peyrouse 2004 (NP 32.3: 651-674, extract wording).
- Hansard HC Deb 23 March 1964 vol 692 cc8-9.
- PA-X 337, 9 January 2005.
- Rolandsen 2011 abstract, including "late 1963".
- Zink 2018 (Baylor).
- Kim 2019: 17 September 1907; 78 members (38 and 40); seven pastors; probationary adoption; Kijang 1953; WCF adoption.
- Ticozzi: 137 circumscriptions in 20 regions; 28 Chinese-led; Tian 18 February 1946; 1957 assembly 17 July to 2 August; Benedict XVI 2007 wording; May 1980 conference.
- *Ad Apostolorum Principis*: "flowers and . . . latest buds"; no powers of teaching or jurisdiction; "valid … gravely illicit".
- UCCJ: 26 October 1954, 8th Assembly, "unerring standard", "triune God"; 26 March 1967, Suzuki Masahisa, "should not have aligned itself with that war effort", "once again headed in a dangerous direction", the 25th anniversary in October 1966.
- Werner, Anderson and Wheeler (Paulines, 2000, 688 pp.) and Nikkel (Faith in Sudan 11, 2001; Edinburgh thesis, dated 1993 by DACB and 1994 by the archive).
- *CT* 27 March 1964: 272 and 28.
- Kiwanuka: 25 May and 29 October 1939.
- Zaire missal: 30 April 1988.
- Polish letter: 18 November 1965, Kominek, 34 signers.
- FABC: 180 bishops, Manila 1970, Paul VI at the latter part.

Not as drafted: S-2 (*CT* November 1974), S-3 (jurnalul.ro; the Todea biography), S-4 (the Joint Declaration), M-7 (Ticozzi), M-8 (Achútegui and Bernad), M-9 (Longman).

Not confirmed: Chesnut's chapter number (the chapter title is confirmed by an essay of the same name; the number is not).

---

## Verdict

**Not approved to proceed.** Five substantial findings:
- two misstatements against the row's own cited source (S-2 Lausanne; S-4 the 1054 excommunications);
- one date the cited source does not carry and the Holy See dates otherwise (S-3);
- one dangling pronoun that damages an existing sentence, with a converts claim stripped of its scope (S-1);
- one [S] date carried by a new sentence, with a source entry that names no work (S-5).

Every fix above gives exact replacement text, and none needs new research except S-5's optional Wiegele check. The structure, the ruled options, the withholding, the living-mark discipline and the apply mechanics are sound: 0 validator errors, and every old matched once. Round 2 should be a targeted recheck of S-1 to S-5 and of any minor findings taken up, against this round's findings. This is Round 1 of the three-round cap on this document.
