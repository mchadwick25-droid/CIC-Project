# Era 10, P2-E10b: adversarial review, Round 1

Reviewer: independent Opus 5.5 review · 2026-11-08 · Round 1 (full)

**Object.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_P2E10b_Proposed.json` (7 new rows IX.52 to IX.58, 50 register edits, 2 meta edits) and `CiC_Step0_Era10_P2E10b_Trace.md`, on branch `claude/era10-step0-history` at 41003b08, against `cic-website/data/world-census.json` release 21.

**Rules applied.** Decision-Log 2026-11-08 "ERA 10 GATE: Mark takes every recommendation" and the two change orders below it. Evidence: `CiC_Step0_Era10_Movements_V1_0.md` (§1 to §4, G-56 to G-79) and `CiC_Step0_Era10_V2_0.md` (§2d, G-14, G-34). R3 from `Design/CiC_Step0_LivingEra_Protocol_Addendum_V1_0.md`.

**Method.**
- Applied the proposal with my own applier (`scratchpad/e10b-rev1/myapply.py`), not the drafter's. Every `replace` and `removeItem` matched exactly once; `set` olds matched release 21; meta olds matched.
- Ran `node tools/validate-census.mjs` on the result, with and without `--tree cft-website/tree`.
- Read every new sentence (all fields of the 7 rows, every register edit, every IX.16 field after the edit) against its traced item. 62 sentences were checked against the item text in the Movements record.
- Re-verified 12 cited works and 1 historical claim by WebSearch (standard mode).
- Measured readability with `engine/m7/readability.py`'s syllable counter, per field, with the Flesch formula applied to short fields too (the module itself leaves fields under 30 words unscored).
- No repo file was edited. No metered model call was made.

---

## SUBSTANTIAL findings

**S-1. IX.33: Billy Graham's crusades did not begin in Los Angeles in 1949.**
- *Location:* registerEdits[9], IX.33 `relationsSummary`, new sentence 3: "Billy Graham's crusades began with a Los Angeles campaign in 1949, extended from three weeks to more than eight."
- *Evidence:* M4 E1 (the BGEA timeline) supports the 1949 Los Angeles campaign and its extension. It does not say the crusades began there. The BGEA's own Billy Graham Library dates "Billy Graham's first city-wide campaign" to Grand Rapids, 13 to 21 September 1947 (billygrahamlibrary.org/billy-grahams-first-city-wide-campaign-begins/). The sentence states something false and adds a claim no item supports.
- *Fix:* "Billy Graham's Los Angeles campaign of 1949 ran for more than eight weeks instead of the three planned." The source note at registerEdits[12] can stay as it is.

**S-2. Three living marks are graded CD on journalism alone.**
- *Location:* the `livingEvidence.grade` of IX.52 (Vatican News, 2022), IX.53 (Christianity Today and RNS obituaries, 2023) and IX.58 (K-LOVE News, 2021).
- *Evidence:* the ruled §2d (G-5) gives "Contemporary-Reported (CR) when it rests on the body's own word, on journalism, or on an independent source not yet verified". R3 defines CR as "resting on self-report, a single stream, or journalism alone", and its rule (iii) forbids promotion. Each of these three marks rests on one news report. The grades come over unchanged from the Movements record's drafts. Only IX.57 (Bialecki, university-press fieldwork) earns CD. IX.54 and IX.55 are correctly CR.
- *Fix:*
  - Set all three to "CR (Contemporary-Reported); newest dated item …, newest verified …".
  - IX.52 stays "settled", because §2d's settled test does not turn on the grade.
  - IX.53's mark also rests on an agency that no item ties to the movement. Add Movements §1 M5 E4 to its evidence. That is the Christian Post report, verified, of the 2012 merger of CrossGlobal Link (the former IFMA, 1917) into Missio Nexus. It names the movement's own successor body. Keep the grade CR.

**S-3. IX.55 is built against the condition in G-64's recommendation.**
- *Location:* newRows IX.55. Its `floorNote` begins "Not yet assessed on a dated text". The trace's own note says "that condition is carried, not met."
- *Evidence:* Mark took every recommendation as the ruling. G-64's recommendation is "(a) … Section A must still be settled on a carrier's dated statement before the entry is built." That condition is part of the ruling.
- *Fix:* hold IX.55 out of this release. That makes 6 new rows, `totalEntries` 301→307 and Pre-Survey Candidate 219→225. Send to the source-research thread for HSLDA's dated statement of faith, or another carrier's. Build the row once that statement is staged and Section A is settled on it.
- *Alternative:* if the thread reads "built" as the world build (the row's `entry` field) rather than the census row, that reading belongs to Mark. It needs one question to him, not a self-certified reading. See the Section A answer below.

**S-4. IX.55: a quotation is attributed to Mitchell Stevens without a verified source in his words.**
- *Location:* IX.55 `legacy`: "By 2001 Mitchell Stevens could describe homeschooling as 'an elaborate social movement'."
- *Evidence:* the only source is Movements §2 M13 item 1, which is the *publisher's description* on press.princeton.edu ("Publisher's description: homeschooling 'is not a random collection of individuals but an elaborate social movement'"). A WebSearch this run found the same phrasing in review copy, not attributed to Stevens's text. CLAUDE.md requires every quote to be re-verified verbatim against its source. This one is attributed to someone whose words were not seen.
- *Fix:* either drop the quotation marks and the attribution ("By 2001 a university-press study could treat homeschooling as an organized social movement"), or cite the book's own page once it is opened. (S-3 holds the row in any case. The fix must still land before the row is built.)

**S-5. IX.24: the inserted sentences turn the existing "It" toward the wrong subject.**
- *Location:* registerEdits[0], IX.24 `relationsSummary`. The two new sentences (the Winters' paper; the IMB and CPM in 1997) sit straight before the existing sentence "It worked as a network rather than a denomination, restating itself through … the Lausanne Covenant (1974) …".
- *Evidence:* after the edit, "It" reads as the Southern Baptist International Mission Board or the Church Planting Movement approach, a denominational agency. The field now misleads, and the sentence order also jumps from 1974 to 1997 and back to 1974. The task brief asks whether the edits damage other bodies' text. This edit does.
- *Fix:* keep registerEdits[0]'s `old` unchanged, with `new` = `old`, or drop the edit. Move the two sentences into registerEdits[1], after "…how separated churches should act together." Read in order there: the Winters' paper ("At the 1974 congress, Ralph and Roberta Winter prepared…"), then the IMB and CPM, then the Tearfund sentence, then the Stanley and Graham sentence. "At the same congress" must become "At the 1974 congress", because its referent moves.

---

## MINOR findings

**M-1. IX.51 `longDescription` brings back a present-tense claim.**
- "its own history presents him as God's messenger". Release 21 deliberately reads "presented". Ruling 4 (change order, era 10 becomes history) says no present-tense claim enters an entry except the living mark.
- *Fix:* "presented".
- Also: "From February 1939 its magazine Pasugo … set out that teaching". The item supports Pasugo carrying "its teaching" in general, not this doctrine in particular. *Fix:* "set out its teaching".

**M-2. IX.16 pointer lines.**
- "Iglesia ni Cristo, once carried here, now has its own entry" (`statusDescription`) and "…once grouped with them, now has its own entry" (`relationsSummary`) narrate the file's change history in live text (CLAUDE.md, live surfaces). They also say the same thing twice.
- *Fix:* delete the `statusDescription` sentence. In `relationsSummary`, write "Iglesia ni Cristo, in the same lane, has its own entry."
- The IX.16 `legacy` edit leaves a dangling "one": "La Luz del Mundo had passed through one, in 1964, and The Way through two changes of leadership after its founder." *Fix:* "La Luz del Mundo had one change of leader, in 1964. The Way had two after its founder."
- **De-duplication otherwise clean.** Every IX.16 field was checked after the edit. No "Iglesia", "Philippin", "Manalo", "Pasugo", "1914", "1963", "2009", "four", "messenger" or "Q928" is left anywhere in the row. The `id` stays, which is right, because ids are permanent. The Way, Unification and La Luz del Mundo text is intact: their dates, founders, scriptures, court records, the documented story and the living evidence are unchanged. Start 1926 is right (La Luz del Mundo, 6 April 1926). No edge touches IX.16 or IX.51.

**M-3. The edited IX.16 fields keep pre-existing defects that the edit now owns.**
- CLAUDE.md: a PR that edits a live field removes the commentary already in it.
- The edited `teaser` is one 43-word sentence (FRE 5) with internal jargon ("packed on one register row for roster economy"). The edited `why` has a 54-word sentence. The `longDescription` keeps sentences of 31, 44, 34 and 29 words and "for the map's economy". The `relationsSummary` keeps a 35-word sentence.
- *Fix* (plainer wording, all facts kept):
  - **teaser:** "North America, Korea and Mexico, from 1926. Three separately founded bodies share this row, but not a confession. Each is assessed on its own published texts."
  - **why:** "Three separately founded movements share this entry. The Way International grew out of Victor Paul Wierwille's radio ministry in the 1940s. Sun Myung Moon founded the Unification Church in Seoul in 1954. La Luz del Mundo was founded in Guadalajara in 1926, and from 1964 a second apostle led it in succession from its founder. Each has its own scripture, founder claim and history, told here on its own terms."
  - **longDescription** sentence 1: "These three bodies share a row, but not a confession. Each is described from its own published texts." Split the other three long sentences at their semicolons and "and"s.
  - **relationsSummary** sentence 1: "Three separately founded bodies share this row because none is large or well studied enough for its own entry. They do not share a confession, and each body's own texts carry its own finding."

**M-4. `modernCountries` does not match the carriers.**
- IX.53 lists only United Kingdom/Britain. Every verified in-window carrier is North American: the IFMA "of North America", Wheaton, and Camp Wycliffe in Arkansas. No verified item places a British carrier in the window, which is the same reason the drafter dropped the UK from IX.57.
- IX.56 omits the United States (Saint John's Abbey, Minnesota).
- IX.57 is empty, though the United States ID (Q30, as on IX.55 and IX.58) exists and Fuller is in Pasadena.
- *Fix:*
  - IX.53: `[United States Q30/Q30]`. Drop "Britain" from `region` and `placeLabel` ("N. America, then global") unless an item is cited for it.
  - IX.56: add `{United States, Q30, United States, Q30}`.
  - IX.57: `[{United States, Q30, United States, Q30}]`.

**M-5. Present-tense claims in two `floorNote`s.**
- IX.54: "Its network keeps a statement of faith". IX.55: "Its legal defense association calls itself a Christian organization". The latter is an undated page, date [S].
- *Fix:*
  - IX.54: "Its network has a statement of faith on record, but the text and its first date are not cited here."
  - IX.55: "Its legal defense association describes itself as Christian on an undated page. No dated statement of faith is cited here."

**M-6. IX.57: "whose entry closes where this one begins, in 1982".**
- IX.45's census `end` is 1980 and its `dates` are "1960-1980s". Its text names the Vineyard (1982) as "the start of the third wave".
- *Fix* (`relationsSummary`): "It follows the charismatic renewal and the Jesus movement, whose entry names the Vineyard of 1982 as the start of the third wave." Make the matching change in `statusDescription`.

**M-7. IX.52: the 1930 abstention count is disputed.**
- "with 47 not voting" rests on the ECU report (E9). A WebSearch this run found 46 in Hollinger (JETS 56/4, 2013) and in an EBSCO summary. The 193 to 67 figure agrees across every source seen.
- *Fix:* drop "with 47 not voting" from `longDescription`, or tag the count Contested and say "about 46 or 47".

**M-8. IX.58 `relationsSummary`: "of the same decade" is not in the evidence.**
- The record says only that Mathisen distinguishes it from "the wider 'men's movement'".
- *Fix:* end the sentence at "men's movement".

**M-9. IX.53 `sourcing`: "Klaus Fiedler (1994) and William Svelmoe (2008) study it".**
- Svelmoe studies Townsend and Wycliffe and places them inside the faith-mission culture (M5 §0 reading). He does not study the movement itself.
- *Fix:* "Klaus Fiedler (1994) tells it as one story. William Svelmoe (2008) places Wycliffe inside it. Wider histories by Joel Carpenter and Wilbert Shenk (1990) and Dana Robert (2009) also cover it."

**M-10. The `kind` field arrives before P2-E10c defines it.**
- The ruling's order of work gives "the `kind` field and its drawing" to P2-E10c.
- IX.57's unit also includes the Association of Vineyard Churches, a church body. G-28 gives the kind to "a movement outside church bodies".
- *Fix:* either drop `kind` from b and let c add it, or keep it and have c rule on it, IX.57 explicitly included. Do not let c inherit an unratified value. Log it in Open-Gaps.

**M-11. Readability: most new fields fall below Reading Ease 60.**
- No new sentence exceeds 25 words. The mean is 13.8 words, and the maximum in new text is 23. But the FRE of the new text is low. FRE is computed per field with the module's formula; "name" marks a field where proper names drag the score (I re-scored it with names replaced by a one-syllable stand-in).

| row | field (FRE) |
|---|---|
| IX.52 | statusDescription 41.6 (name) · sourcing 44.0 (name) · relationsSummary 54.0 · why 53.5 · longDescription 51.6 (name; 71 without names) |
| IX.53 | statusDescription 50.6 · sourcing 41.6 (name) · relationsSummary 45.2 · why 29.2 (name: "Interdenominational Foreign Mission Association"; 61 without) · teaser 38.5 · longDescription 47.9 (name) · legacy 33.7 (name) |
| IX.54 | sourcing 32.5 (name: "Salvation in the Slums", "Christianity Today") · relationsSummary 58.4 · why 49.3 · longDescription 46.4 (name; 68 without) · legacy 47.8 (name) |
| IX.55 | sourcing 38.2 (the word "university-press") · floorNote 48.6 · relationsSummary 42.8 · why 45.8 · teaser 40.6 · legacy 18.8 |
| IX.56 | statusDescription 52.9 · floorNote 42.6 · relationsSummary 50.9 · why 37.5 (name: "Orate Fratres", "Collegeville"; 76 without) · teaser 28.8 · longDescription 47.3 (name; 74 without) · legacy 46.1 (name) |
| IX.57 | statusDescription 49.5 · sourcing 49.5 · relationsSummary 55.3 · why 56.9 · teaser 46.9 · longDescription 46.5 (name; 69 without) · legacy 42.7 |
| IX.58 | statusDescription 55.6 · sourcing 4.6 · relationsSummary 33.3 · why 47.8 · teaser 47.8 · longDescription 51.9 · legacy 0.5 (a verbatim quote: keep it) |
| edited old rows | IX.16 floorNote 53.4, relationsSummary 49.5, statusDescription 58.5, why 37.5, teaser 5.1, longDescription 37.0 (see M-3) · IX.24 relationsSummary 23.5 (pre-existing 37- and 31-word sentences) · IX.28 relationsSummary 26.8 · IX.33 relationsSummary 21.4 (pre-existing 30- and 41-word sentences) · IX.45 relationsSummary 26.3 (pre-existing 73-word sentence), legacy 49.2 (pre-existing 29- and 28-word sentences) |

At or above 60: IX.52 floorNote, teaser and legacy; IX.53 floorNote; IX.54 statusDescription, floorNote and teaser; IX.55 statusDescription and longDescription (60.2); IX.56 sourcing; IX.57 floorNote; IX.58 floorNote; IX.16 legacy; IX.30 legacy; IX.51 longDescription (63.4).

Proposed rewrites. Facts and names are kept; the score shown is for the rewrite.
- **IX.52 why** (69): "By 2006, Kevin Ward found, most Anglicans lived outside the West. Their bishops met at Lambeth. There they spoke on Christian unity, on birth control and on sexuality."
- **IX.52 relationsSummary** (64): "It carries on from the Victorian Church of England and the Oxford Movement. Both of those entries end in 1906. In this era Anglicans also appear inside other stories, such as the East African Revival and the Church of South India."
- **IX.53 teaser** (76): "In 1917, mission groups with no tie to any one church formed a fellowship. People called them faith missions."
- **IX.53 why** (57; the long name sets the ceiling): "In 1917 mission groups with no church of their own formed a fellowship. They called it the Interdenominational Foreign Mission Association. People knew its members as 'faith missions'. Klaus Fiedler tells their story as one movement, from Hudson Taylor to the Africa of his day."
- **IX.53 legacy** (64): "In 1994 Klaus Fiedler told the whole story as one movement, from Hudson Taylor to the Africa of his own day."
- **IX.54 why** (56): "In 1872 Jerry McAuley opened a mission on Water Street in New York. Others followed. In 1906 mission leaders in New York joined in a federation. A historian counts these missions among the revival-based welfare movements of 1865 to 1920."
- **IX.54 legacy** (74): "The union took a new name in 2000, the Association of Gospel Rescue Missions. In 2010 it was still the movement's network."
- **IX.55 teaser** (69): "In 1983 two fathers who taught their own children, both lawyers, set up a legal defense group for families who schooled at home."
- **IX.55 why** (56): "Sociologist Mitchell Stevens found that homeschooling was an organized movement, not a scatter of private choices. He traced one of its two roots to the Christian day schools of the 1960s and 1970s. In 1983 a legal defense group for homeschool families followed."
- **IX.56 teaser** (53; "liturgical" was already removed): "A movement to renew worship began with a talk in Malines in 1909. It spread to Catholic abbeys and Anglican parishes."
- **IX.56 legacy** (55; names): "John Fenwick and Bryan Spinks tell its story across many churches: Catholic, Anglican, Eastern and North American. They close the Catholic part in 1962."
- **IX.56 why** (44): the score is set by "liturgical", "Benedictine" and "Orate Fratres". Splitting the second sentence at "where" is the most that can be gained without losing a fact.
- **IX.57 teaser** (55): "It began with a seminary course called 'Signs and Wonders'. Its churches sought the gifts of the Spirit without becoming Pentecostal."
- **IX.57 legacy** (57): "In 1997 Donald Miller studied the Vineyard beside two other new church networks. Jon Bialecki's study of its churches followed in 2017."
- **IX.58 why** (77): "In 1990 a college football coach and a friend started a ministry for men. Its first members called themselves Promise Keepers. By 1996 its rallies had filled 22 stadiums with nearly 1.2 million men. Each man made seven promises. Among them, he would stand by other men, stay pure and keep his marriage strong. He would also reach across lines of race and church."
- **IX.58 sourcing** (58): "Moderate. A study by John Bartkowski (2004) comes from a university press. An encyclopedia entry, the movement's own book of 1994 and news reports of the time add to it."
- **IX.52 statusDescription** (57): "Tier 2: viable, secondary. It rests on the records of Lambeth and of the Anglican Consultative Council, and on two standard histories. Its window opens in 1906, where the Victorian Church of England entry ends." The tier wording should follow the house form ("Tiered Viable, secondary (Tier 2)") if that form is kept fleet-wide.

**M-12. IX.30 `legacy` uses "later" twice and turns a subtitle into a claim.**
- "Lester Ruth and Lim Swee Hong later wrote a history … and of the ideas that reshaped the Protestant church."
- *Fix:* "In 2021 Lester Ruth and Lim Swee Hong published a history of contemporary praise and worship." The full subtitle stays in `sources`.

---

## COSMETIC findings

- **C-1.** The new rows' key order differs from the 49 era 10 rows. The existing order runs `…why, entry, sources, longDescription, teaser, voices, legacy, [streams], documentedStories, livingEvidence`. The new rows place `livingEvidence` after `living` and put `kind` mid-row. Reorder them to match, so diffs and readers stay uniform.
- **C-2.** IX.53 tells the Fiedler sentence three times (`why`, `longDescription`, `legacy`). Keep it in one or two of them. "Present-day Africa" reads as a claim about today; "the Africa of his day" or the book's title in italics avoids that.
- **C-3.** IX.56 `statusDescription`: "where historians close the Catholic movement" rests on one book. Write "where Fenwick and Spinks close the Catholic movement".
- **C-4.** IX.52 `why`: "on limiting families" → "on birth control" or "on limiting parenthood" (see M-11 rewrite).
- **C-5.** Trace: IX.58's Pueblo, Boulder and basketball-arena details trace to "Round 1 review M-12", not to an evidence item. E2's item text in the Movements record should record them, so that the trace points at evidence and not at a review.
- **C-6.** The drafter's applier recomputes the meta counts instead of applying `metaEdits`, and its sentence check reads `trace.json`, not the fields, so untraced edited fields (M-3) escape it. Both counts happen to be right: 308 and 226.

---

## Section A (task item 3)

**IX.53, IX.54 and IX.57 honor the rulings. IX.55 does not.**
- G-57(a), G-60(a) and G-73(b) were each recommended without a Section A precondition. G-73's text even notes that "Section A still waits on a verified text of the 1994 statement of faith" and still recommends the entry. Entering those rows with an honest "not yet assessed" `floorNote` follows the ruling. It also follows the never-invent rule, since none of the three claims a floor result.
- G-64's recommendation alone attaches the condition "before the entry is built" (S-3).

**A note for the method page.** No other census row carries a "not yet assessed" `floorNote`. P2-E10c's method-page line should explain the state, and Open-Gaps should list the four rows (or three, if IX.55 is held) with the dated statement each still needs.

## Rulings (task item 2)

Clean, apart from S-3 and M-10.
- Nothing is placed for G-15 or IX.50.
- No row is placed for the student movement (G-62(c)), frontier missions as an entry (G-58, held at (d)), the healing revival (G-71/G-72), the Oxford Group (G-69(d)) or Keswick (G-70(a)).
- Each named line sits where its question recommended:
  - Wycliffe in IX.53 (G-56(a));
  - the frontier line in IX.24 (G-58(b)), with CPM beside it (G-59(a));
  - relief in IX.24 with its reach-back disclosed (G-61(a)). World Vision is rightly left out: its item is [S];
  - broadcasting in IX.33 (G-65(a));
  - mass evangelism in IX.24 and IX.33 (G-34(a));
  - Word of Faith in IX.45 (G-75(a));
  - Jesus music in IX.45 and praise and worship in IX.30 (G-76(a));
  - Toronto in IX.57 (G-74(a));
  - the new monasticism in IX.28 (G-67(b)).
- The new rows follow G-68(a) (1909 to 1962, living false), G-77(a), G-78(a) and G-60(a) (the 1872 reach-back disclosed).

## Census integrity (task item 4)

Clean.
- All edits applied without a miss.
- `validate-census.mjs`: 0 errors and 2 pre-existing warnings without `--tree`. With `--tree cft-website/tree` the only errors are the 7 expected missing tree pages.
- Ids and atlasIds are unique. IX.50 stays unused.
- Every `modernCountries` country and place ID already exists in the census.
- Lanes, labels and orders, including "5<->6 bridge", match existing values. Status, chip, glyph and statusWord match the 27 existing Tier 2 rows.
- Every field shape matches. `livingEvidence` has the same four keys. Source `type` values are among primary, secondary and reference.
- Meta: 308 rows and 226 Pre-Survey Candidates are correct. Every status count matches the rows.
- G-51(a): each living item is mirrored in `sources[]` with the "living mark only" note.

## Window (task item 6)

Clean, apart from S-2's grades and the present-tense items in M-1 and M-5.
- No history claim falls after 2010. Post-2010 dates appear only in `livingEvidence`, its mirrored source, or as publication years of scholarship (Bialecki 2015 and 2017, Ruth and Lim 2021, Markofski 2015), which follows the existing practice (Bowler 2013 on IX.30).
- IX.54's "in 2010" and IX.52's 2008 GAFCON sentence are inside the window.
- The IX.58 crowd figure is given as an estimate, with Contested noted in the trace.

## Other clean checks

- **Re-verified by WebSearch this run** (bibliographic details match the citation):
  - Fiedler 1994 (Regnum; place varies by record, as disclosed);
  - Magnuson 1977 (Scarecrow, ATLA 10; lists "the rescue mission movement");
  - Stevens 2001 (Princeton);
  - Peshkin 1986 (Chicago; 18 months, a Baptist school in Illinois);
  - Pecklers 1998 (Liturgical Press; liturgy and social justice in the 1930s and 1940s);
  - Fenwick and Spinks 1995 (Continuum; chapter "Roman Catholic Liturgical Movement 1900-62");
  - Bartkowski 2004 (Rutgers; chapter 1 "The Rise and Fall of the Christian Men's Movement");
  - Bialecki 2017 (UC Press; an ethnography of the Vineyard);
  - Hangen 2002 (UNC; Rader, McPherson, Fuller; paid airtime);
  - Ward 2006 (CUP; non-Western churches "now make up most of the communion");
  - Mathisen 2001 (CT and Books & Culture, September 2001);
  - Lambeth 1930 Resolution 15 (193 to 67; the abstentions disputed, M-7).
- **Spot-checked sentences, all supported apart from the findings above:**
  - the Lambeth 1920 Appeal and Nicene wording;
  - ACC Limuru 1971; GAFCON June 2008;
  - IFMA's March and September 1917 meetings, "fellowship of missions without denominational affiliation", forty-six missions in 1965, Camp Wycliffe 1934;
  - McAuley 1872; Pacific Garden Mission 1877 and its "harbor" quote; the 1906 federation; the IUGM on 17 September 1913 with about fifty missions; 350 members in 1972; AGRM in 2000;
  - the Moores 1975; Dobson c. 1982; HSLDA in March 1983; "a handful of states"; Hill's quote;
  - Beauduin and Malines 1909; Michel, Orate Fratres and the Liturgical Press in 1926; Hebert 1935 and 1937; the Church Times quote;
  - MC510 1982 to 1985; dropped 1986; Smedes 1987; Power Evangelism 1985; the CT 1986 definition of the Third Wave; Toronto 1994; the December 1995 split; Poloma 1997;
  - PK: the 20 March 1990 drive, about seventy men, 4,200 in 1991, 22 rallies and about 1.2 million men in 1996, the 1994 book, 4 October 1997, the 345 staff from March 1998, Mathisen's quote, the CSM statement of faith;
  - the Hangen, NRB 1944, Tearfund 1968, Stanley, BGEA 1950, Rhema 1974, Maranatha 1971, Eskridge and Durham 2004 lines;
  - IX.51's 27 July 1914, Pasugo from February 1939, the 1963 and 2009 successions, and the "own counts" claims, all in release 21's own text.
- **Spelling:** American throughout. "Mobilisation" and "Globalisation" are proper names and titles.
- **No AI tells** found in the new copy.

---

## Verdict

**REVISE.** Five substantial findings: S-1 to S-5. All are mechanical to fix except S-3, which either holds IX.55 back or needs Mark's reading of G-64. From Round 2, a targeted recheck should cover S-1 to S-5, M-1 to M-10 and the M-11 rewrites that are taken.
