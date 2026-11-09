# Era 10, IX.50 the Christian Right: trace of every new sentence

## Revision log (after Round 1)

Revised 2026-11-09 against `CiC_Step0_Era10_IX50_Review_Round1.md`. Each finding, and what was done:

| Finding | Done |
|---|---|
| S1, the id | Done as the review gives it. The id is now `the-christian-right`, in the row, `_meta.id` and §5. The old draft id was never published. Mark should be told in one line that the id follows n1, which he has not ruled on separately; if he picks n2, the id becomes `the-new-christian-right` before this release reaches `live`. |
| M1, floorNote | Done, in the review's words. The absence claim now follows the evidence and is framed as Falwell's account ("On his account"). |
| M2, the verified list | Done. The AAPB "coalition of moralists" string and the full Reagan sentence move to "Verified in this run" (E2, E3), both re-read with `curl` this run. §4 and §7 are updated. Wanted item 3 is lifted, and item 2 is narrowed to the full record beyond the clip. |
| M3, the Dallas framing | Changed in form. The review's wording is kept in substance, but each long sentence is split in two for readability: `why` "spoke at a briefing in Dallas. Another group, the Religious Roundtable, ran it."; `longDescription` "That month Ronald Reagan spoke in Dallas, at a briefing run by another group, the Religious Roundtable. He told the crowd, ...". The organizer source differs: the Miller Center page could not be read this run (`curl` failed on its certificate chain; WebFetch returned 503), so the review's condition "after reading it" could not be met. In its place the row cites a source that was read in full: the Reagan Library's Morton Blackwell Files, "Roundtable (2 of 2)", Box 40 (E11). |
| M4, the four principles | Done, in the review's words, quoted from E1. |
| M5, sourcing | Done, in the review's words. |
| M6, relationsSummary | Done, in the review's words. |
| M7, the IX.24 line | Done, in the review's words. The edit's `ruling` and §2 say that the line comes from option (ii) and is kept as a cross-reference, not a lineage. |
| M8, livingEvidence | Done, in the review's words; the E10 source note is updated to match. |
| M9, Reagan as a voice | Done. `voices[1]` is removed. |
| C1, C2 | Done, in the review's words. |
| C3, source notes | Done. Encyclopedia.com is added (its "first executive director" sentence re-read this run). The Wilcox note records the 2010/2011 cataloging and the co-author's two surnames. "backers" became "members" through M1. |
| C4, IX.33's two pointers | Left as it was, as the review allows. The `legacy` edit is required; the `relationsSummary` pointer does no harm. |

Readability after the fixes (§6): all row prose 479 words, Reading Ease 59.6, FK grade 8.0. No sentence runs past 25 words.

Applied to the census as data release 23 (2026-11-09) on branch `claude/era10-p2e10c`. The Round 2 targeted recheck is still due.

Companion to `CiC_Step0_Era10_IX50_Proposed.json`. Drafted 2026-11-09 under the Decision-Log entry "Era 10 follow-up rulings" (2026-11-09), item 1: G-15 option (i). The row is drafted from D-E6 (`CiC_Step0_Era10_V2_0_Proposed_Edits.json`, `newEntries`) and V2.0 §3, as revised after the V2.0 reviews (R1-M4, R1-C3). It went to review (Round 1) and was revised; see the log above.

Evidence follows the change order "evidence for recent movements" (2026-11-08): the movement's own dated texts for its beginning, carriers and name, plus a scholarly study for its recognition as a movement. An item is "verified" only where this run confirmed it and a URL is given below. Everything else stays [S].

## 1. Evidence items

### Verified in this run (WebSearch, mode "standard"; two pages read with WebFetch; after Round 1, five pages re-read with `curl`)

| # | Item | What it shows | URL |
|---|---|---|---|
| E1 | Liberty University Archive, *Projects and Programs of the Moral Majority*, Record Group 2, finding aid (last updated 24 March 2014) | Historical note: "The Moral Majority was founded on June 6, 1979 by Dr. Jerry Falwell, Dr. Tim LaHaye, Dr. Charles Stanley, Dr. D. James Kennedy, and Dr. Greg Dixon. It was founded on four principles; being pro-life, pro-family, pro-morals, and pro-American. Their headquarters were in Washington D.C. and they campaigned in the political arena on behalf of their principles. The Moral Majority disbanded in 1989." Read in full from the PDF text. | https://pimcore.liberty.edu/imports/coldfusion/1420/documents/archivefindingaids/MOR_RG-02.pdf |
| E1a | JSTOR Daily, "The Moral Majority Collection" (The Editors, 1 July 2022) | The same date and the same five ministers; the collection is curated by Liberty University. Corroborates E1. | https://daily.jstor.org/the-moral-majority-collection/ |
| E2 | Jerry Falwell, interview, *The MacNeil/Lehrer Report* (22 August 1980); American Archive of Public Broadcasting, record cpb-aacip-507-0v89g5gw13 | The Moral Majority is "not a religious organization. It is totally political." Its supporters include "72,000 pastors, Roman Catholic priests, Jewish rabbis, Mormon elders, fundamentalist, you name it." The coalition is "not all evangelical by any means." After Round 1 the page was re-read with `curl`. It gives "The MacNeil/Lehrer Report \| NewsHour Productions \| August 22, 1980" and says the clip and transcript run "from 06:22 - 10:45 in the full record". The transcript reads, word for word: "there is a coalition in this country of moralists. They're not all evangelical by any means; moralists who share similar moral values" and "though we theologically have great differences, we we very much share those premises and are willing to fight together". It is a transcript of the clip, not of the full record. | https://americanarchive.org/primary_source_sets/conservatism/10-507-0v89g5gw13 |
| E3 | Ronald Reagan, address to the National Affairs Briefing, Reunion Arena, Dallas (22 August 1980) | The transcript is dated 22 August 1980. The briefing ran 21 and 22 August, so the address is on the 22nd (this settles R1-C3). After Round 1 the American Rhetoric page was re-read with `curl` (200). Its header: "delivered 22 August 1980, Dallas Reunion Arena, Dallas, Texas [AUTHENTICITY CERTIFIED: Text version below transcribed directly from audio]" (abridged). The full sentence reads: "Now, I know this is a non-partisan gathering, and so I know that you can't endorse me, but I only brought that up because I want you to know that I endorse you and what you're doing." | https://americanrhetoric.com/speeches/ronaldreaganreligiousliberty.htm ; https://www.christiancentury.org/article/2004-06/reagan-political-years-paralleled-rights-rise ; https://baptistnews.com/article/ronald-reagans-ascent-to-office-paralleled-rise-of-religious-right/ |
| E4 | EBSCO Research Starters, "Robertson Founds Christian Coalition"; Encyclopedia.com, "Christian Coalition" | Pat Robertson founded the Christian Coalition in 1989, after his 1988 presidential run, and chose Ralph Reed as executive director (1989–1997). Encyclopedia.com, re-read with `curl` after Round 1: "launched in 1989 with the assistance of its first executive director, Ralph Reed." | https://www.ebsco.com/research-starters/history/robertson-founds-christian-coalition ; https://encyclopedia.com/religion/legal-and-political-magazines/christian-coalition |
| E5 | Faith & Freedom Coalition, "About" page (undated) | The coalition's own account: Ralph Reed formed it in 2009. | https://ffcoalition.com/about |
| E6 | Daniel K. Williams, *God's Own Party: The Making of the Christian Right* (Oxford University Press, 2010), viii + 372 pp. | A scholarly history of the movement by name. Reviewed in *Church History* (W. V. Trollinger Jr.) and by Mark Noll in *The New Republic*. | https://www.cambridge.org/core/journals/church-history/article/gods-own-party-the-making-of-the-christian-right-by-williams-daniel-k-new-york-oxford-university-press-2010-viii-372-pp-2995-cloth/C50412D661DCDC63A61FBDF3732E60E4 ; https://newrepublic.com/article/88644/review-daniel-williams-darren-dochuk-christian-right |
| E7 | William Martin, *With God on Our Side: The Rise of the Religious Right in America* (Broadway Books, 1996) | A history of the movement, drawn from interviews; the companion to the PBS series. Reviewed in *Christianity Today* (1997). | https://christianitytoday.com/ct/1997/april28/7t5022.html ; https://www.kirkusreviews.com/book-reviews/william-martin/with-god-on-our-side/print |
| E8 | Clyde Wilcox, *Onward Christian Soldiers? The Religious Right in American Politics* (Westview Press, 1996; 2nd ed. 2000; 3rd ed. 2006 with Carin Larson; 4th ed. 2010 with Carin Robinson) | A political-science study of the movement. The later editions cover the 2006 and 2008 elections. | https://openlibrary.org/books/OL2993781W ; https://hachettebookgroup.com/titles/clyde-wilcox/onward-christian-soldiers/9780813391977 |
| E9 | Andrew R. Lewis, *The Rights Turn in Conservative Christian Politics: How Abortion Transformed the Culture Wars* (Cambridge University Press, 19 October 2017) | Independent scholarship on present-day evangelical rights-based advocacy and opinion (to 2016). For the living mark only. | https://www.cambridge.org/core/product/DE0EC83FEB5166F5E1C3FE91CE0D460A |
| E10 | *Washington Examiner*, "What to know about the Faith & Freedom Coalition's 2025 Road to Majority Conference" | The conference met at the Washington Hilton, 26–28 June 2025. Independent news. For the living mark only. Round 1 found the article's date in the search result: 26 June 2025. | https://www.washingtonexaminer.com/?p=3455623 |
| E11 | Ronald Reagan Presidential Library, Morton Blackwell Files, "Roundtable (2 of 2)", Box 40 (digitized folder) | Read in full from the PDF text after Round 1. A 1982 scheduling request from Elizabeth H. Dole: "Address the Memphis National Affairs Briefing of the Religious Roundtable"; "The Roundtable is headed by Ed McAteer who organized major rallies across the country for the President in 1980"; "President Reagan addressed a major, highly successful religious/political briefing in August 1980 in Dallas". A press release for the public-television program *Crisis to Crisis* in the same folder: "McAteer sponsored a gathering in Dallas, Texas, called 'The National Affairs Briefing,' where 10,000 ministers came to hear then-candidate Ronald Reagan and several evangelists speak." Shows that the Religious Roundtable, not the Moral Majority, held the Dallas briefing. Used in place of the Miller Center page the review named, which could not be read this run. | https://www.reaganlibrary.gov/public/digitallibrary/smof/publicliaison/blackwell/box-040/40_047_7007844_040_015_2017.pdf |

### Carried from the repo, not re-checked here

- **repo-IX.33.** IX.33's census text (release 22): "The political mobilization that began with the Moral Majority in 1979 also traces back to this movement". Census text, counted apart from verified items.
- **V2.0 §3** B-judgments: B1 moderate to rich, B2 thin ("the crux"), B3 real, B4 strong, Tier 3. These are the record's own judgments, not evidence items.

### Still [S]: not used in participant text

- The founders' circle as "three Catholics, a Jew and two fundamentalist Baptists" (Weyrich, Viguerie, Dolan, Phillips, Falwell, Billings). The search found the Lynchburg meeting attendees only in secondary and mirror pages, and one result names the framing as disputed. E1, the archive, names five ministers as founders.
- Later LDS support (beyond E2's "Mormon elders").
- The Miller Center essay "Building a Movement Party" (millercenter.org/node/48826), named by Round 1 for the Dallas organizer. It could not be read this run (`curl`: certificate chain failure; WebFetch: 503). E11 is used instead.
- The Faith and Freedom Coalition's founding day (14 May 2009). It was seen only on Wikipedia-derived pages. The row says "2009".
- Whitehead & Perry's definition of Christian nationalism, and their finding that its scores move apart from personal religiosity.

## 2. What changed from D-E6, and why

- **Kind and tier.** `kind: "cross-church movement"`, as the ruling sets. Tier 3 is written the way the era's other Tier 3 movement rows write it (IX.25, IX.28, IX.49): `statusWord` "Researched — deferred, smaller frame", and "Tiered deferred on a smaller frame (Tier 3)". D-E6's "Held — for Mark's direct ruling" is gone, since Mark has ruled.
- **Thin on lived ecology (B2).** This is said in `statusDescription` and in `legacy`.
- **Scholarly leg.** D-E6's `sourcing` named Du Mez, Whitehead and Perry, Stewart and Gorski (2019–2020). Those works study "Christian nationalism", and V2.0 §3 calls it a judgment whether that is the same current. The row now cites three studies of the Christian Right by name, from inside the era: Martin (1996), Wilcox (1996; 4th ed. 2010) and Williams (2010). The later works are not cited.
- **Living evidence.** D-E6 graded CD on the 2020 works and on the BJC/FFRF report (2022), which study Christian nationalism. It is regraded on E9, a verified university-press study (CD), and E10, verified news (CR). The grade stays CD, newest 2025. Group L-3 is kept.
- **floorNote.** D-E6's "Its first leaders included Catholics, a Jew and fundamentalist Baptists" rested on the [S] founders' circle. The archive (E1) names five ministers as founders. The note now rests on Falwell's own dated statement (E2) instead, and stays marked as not settled.
- **Media carriers dropped.** D-E6's `relationsSummary` said Rush Limbaugh's program (1988) and Fox News (1996) "carried its shared story". Only their launch dates were verified (V1.0). The claim about what they carried rests on no verified item, and it describes a living institution. It is left out. If it is wanted, it needs a scholarly source.
- **The Reagan quotation** is shortened to "I endorse you and what you're doing". The rest of his sentence is paraphrased. That removes the only sentence over 25 words, and quotes only what was seen in several sources.
- **The 1979 start** now rests on a verified date (E1). V2.0 §3 had flagged it as [S].
- **IX.24's disclosure clause.** G-15 lists the IX.24 line under option (ii), not (i). It is carried over under (i) as a cross-reference only: it marks a separate entry, not a lineage from Lausanne-era evangelicalism (Round 1, M7). V1.0's drafted wording ("global-congress-shaped — disclosure, not identity") is internal language and is not used. The new line names the founding year, not "(1979– )" or "(1979–2010)".
- **After Round 1.** The Dallas sentences name the Religious Roundtable as the organizer (E11), the four principles are quoted as the movement's own words, Reagan is no longer listed as a voice, and the scope of three claims is narrowed (floorNote, sourcing, relationsSummary). See the revision log.
- **IX.33's legacy** said the map gives the movement no entry of its own ("rather than giving it a world of its own"). Option (i) makes that untrue, so the clause is replaced.

## 3. Sentence → evidence

| field | sentence | evidence |
|---|---|---|
| statusDescription | Tiered deferred on a smaller frame (Tier 3). | V2.0 §3 Tier 3; the era's Tier 3 wording (IX.25, IX.28) |
| statusDescription | It was a political movement carried by organizations, not a church or a confession. | E1 ("campaigned in the political arena"); E2 ("not a religious organization"); E4; E5 |
| statusDescription | Its public record is moderate to rich. | V2.0 §3 B1; E1–E8 |
| statusDescription | What it formed in people's lives beyond politics is thinly recorded, and this entry says so. | V2.0 §3 B2 "Thin ... the crux"; the ruling's "thin on lived ecology (B2)" |
| sourcing | Moderate to rich. | V2.0 §3 B1 |
| sourcing | The Moral Majority's papers are kept at Liberty University. | E1, E1a |
| sourcing | In a 1980 interview Jerry Falwell gave his own account of it. | E2 |
| sourcing | Three studies trace its history: William Martin (1996), Clyde Wilcox (1996, revised to 2010) and Daniel K. Williams (2010). | E7, E8 (4th ed. 2010), E6 |
| floorNote | In August 1980 Jerry Falwell said the Moral Majority was not a religious group. | E2 (paraphrase of "not a religious organization") |
| floorNote | 'It is totally political,' he said. | E2, verbatim |
| floorNote | He counted pastors, Catholic priests, Jewish rabbis and Mormon elders among its members. | E2 ("72,000 pastors, Roman Catholic priests, Jewish rabbis, Mormon elders ... in Moral Majority") |
| floorNote | On his account, it had no confession of its own to test. | E2; Section A note (§4) |
| floorNote | No statement of faith has been found for it or the later groups. | Section A note (§4): none found in this run's searches |
| floorNote | The churches its members came from are not tested through it. | Section A note (§4); method |
| floorNote | This reading is not settled until the later groups' own statements are checked. | Section A note (§4); ruling ("rests on unverified items") |
| relationsSummary | The entry on Fundamentalism traces this movement back to it. | repo-IX.33 |
| relationsSummary | Its founders were ministers. | E1 |
| relationsSummary | Its groups drew support from several churches and faiths, and none became a church. | E2; E1, E4, E5 (political organizations) |
| relationsSummary | They were the Moral Majority (1979–1989), the Christian Coalition (from 1989) and the Faith and Freedom Coalition (from 2009). | E1; E4; E5 |
| why | In June 1979 Jerry Falwell and four other ministers founded the Moral Majority. | E1, E1a |
| why | In August 1980 Ronald Reagan, then running for president, spoke at a briefing in Dallas. | E3 |
| why | Another group, the Religious Roundtable, ran it. | E11 |
| why | He said the gathering was nonpartisan, so it could not endorse him. | E3 (paraphrase) |
| why | Then he added, 'I endorse you and what you're doing.' | E3 (short form, seen in several sources) |
| why | The Moral Majority closed in 1989, and Pat Robertson founded the Christian Coalition that year. | E1; E4 |
| why | In 2009 Ralph Reed, the Christian Coalition's first executive director, founded the Faith and Freedom Coalition. | E4 (Encyclopedia.com: "first executive director"); E5 |
| longDescription | Jerry Falwell, Tim LaHaye, Charles Stanley, D. James Kennedy and Greg Dixon founded the Moral Majority on 6 June 1979. | E1, E1a |
| longDescription | It named four principles of its own: 'pro-life, pro-family, pro-morals, and pro-American'. | E1, verbatim |
| longDescription | From its base in Washington, it worked in politics for those aims. | E1 |
| longDescription | In August 1980 Falwell called it 'totally political', not a religious group. | E2 |
| longDescription | Its backers, he said, were not all evangelicals. | E2 ("not all evangelical by any means") |
| longDescription | That month Ronald Reagan spoke in Dallas, at a briefing run by another group, the Religious Roundtable. | E3; E11 |
| longDescription | He told the crowd, 'I endorse you and what you're doing.' | E3, verbatim |
| longDescription | The Moral Majority closed in 1989. | E1 |
| longDescription | That same year Pat Robertson founded the Christian Coalition, with Ralph Reed as its executive director. | E4 |
| longDescription | Reed went on to found the Faith and Freedom Coalition in 2009. | E5 |
| teaser | In 1979 five ministers founded the Moral Majority, a political organization that drew support from several faiths. | E1; E2 |
| legacy | Its groups changed over thirty years, but the movement carried on. | E1, E4, E5 (1979, 1989, 2009); E8 (4th ed. 2010 covers the 2008 election) |
| legacy | In 2010 the historian Daniel K. Williams told its story in God's Own Party. | E6 |
| legacy | The record shows its political work well. | V2.0 §3 B1, B4 |
| legacy | It shows much less of what the movement meant for its members' faith. | V2.0 §3 B2 |
| voices | Jerry Falwell — who founded the Moral Majority with four other ministers in 1979, and called it 'totally political' in 1980 | E1; E2 |
| voices | Pat Robertson — who founded the Christian Coalition in 1989 | E4 |
| voices | Ralph Reed — the Christian Coalition's first executive director, who founded the Faith and Freedom Coalition in 2009 | E4; E5 |
| voices | William Martin — whose With God on Our Side (1996) told the story of the movement's rise | E7 |
| livingEvidence | (basis, evidence, grade, group) | E9 (CD; a study of the present, as §2d requires); E10 (CR, dated 26 June 2025); L-3 basis wording from V2.0 §2d |
| IX.33 legacy | ... sits one step past this window. It has its own entry, the Christian Right. | repo-IX.33; the ruling |
| IX.33 relationsSummary | The Christian Right has its own entry. | the ruling |
| IX.24 relationsSummary | The Christian Right, a political movement that American ministers began with the Moral Majority in 1979, has a separate entry. | E1; the ruling (cross-reference carried from option (ii)) |

The copy rules of V2.0 §3 hold. Every claim is a dated, published act or text. No sentence characterizes a person or a motive. Reed is living and appears only through founding dates and offices. Nothing is said about Fox News.

## 4. The Section A note

**What the carriers' own dated statements show.** One carrier statement was read this run: Falwell's, on 22 August 1980 (E2). He said the Moral Majority was "not a religious organization. It is totally political." He named its supporters as pastors, Catholic priests, Jewish rabbis and Mormon elders. He also said: "though we theologically have great differences, we we very much share those premises and are willing to fight together" (E2, verbatim). That is an own-voice, dated statement for the coalition reading. The archive's note (E1) gives its basis as four political principles, not a creed. No statement of faith was found for the Moral Majority, the Christian Coalition or the Faith and Freedom Coalition. None was looked for beyond these searches.

**What the floor test can read from that.**
- The movement made no claim of its own on Article 4's content. Its spokesman disclaimed any religious basis, so there is no confession of its own to test. This is the coalition reading in V1.0 and V2.0 §3, now resting on a dated own-voice statement rather than on [S] items.
- It was not built on one church's confession. By its own account, it drew in people from churches on both sides of the floor (Catholic priests and Mormon elders), and from outside Christianity (Jewish rabbis).

**What it cannot read.**
- It cannot test any member church through the coalition. Each church is assessed in its own entry, where it has one.
- It cannot say what any individual supporter believed.
- One 1980 interview by one founder cannot speak for the Christian Coalition (1989) or the Faith and Freedom Coalition (2009). Neither group's own statement was read.
- It cannot say who besides the five ministers built the movement, or that its founders set out to cross the floor. That claim would rest on the founders' circle, which stays [S] (above). Falwell's own words on shared premises across "great differences" (E2) show the coalition, not who designed it.

**Status.** The note is provisional and stays marked as unverified. The ruling's reading rests on unverified items. One leg (E2) is now verified, including V1.0's coalition-of-moralists string (after Round 1). The other two V1.0 legs are still [S]: the founders' circle, and Whitehead & Perry, which this row no longer uses. The floorNote says plainly that the reading is not settled.

## 5. Notes for review

- **id.** `the-christian-right`. It follows the name (G-15 naming sub-option n1, as drafted in D-E6). The earlier draft id carried "christian-nationalism", a name the record dates after the era (V2.0 §3); it was never published. The new id occurs nowhere in the release 22 census, `origin/main`, `origin/live` or `cft-website/tree/` (Round 1). Mark has not ruled n1 separately; if he picks n2, the id becomes `the-new-christian-right` before release.
- **Edit checks.** Each `registerEdits` old string occurs exactly once in its field in release 22.
- **Applied to a scratch copy** (`apply.py`, in the scratch folder for this run). The key order matches IX.55. `meta.totalEntries` becomes 308 and `statusCounts["Pre-Survey Candidate"]` becomes 226; both recount correctly.
- **Validator.** `node tools/validate-census.mjs <scratch> --atlas cft-website/index.html`: 308 movements, 579 edges, 10 eras, 0 errors, 2 warnings (both old shortName warnings, also on release 22). With `--tree cft-website/tree` added, the only error was the expected missing tree page for the new row. After Round 1 the row is applied to the census itself (release 23) with the id `the-christian-right`, and its tree page is generated, so that error clears.
- **No edges** are proposed. P2-L10 handles links.
- **`documentedStories`** is `[]`. No story is drafted.
- **Region.** "United States", with the IDs IX.55 uses (Q30).

## 6. Readability

Scored with `engine/m7/readability.py`'s `measure`. Initials ("Daniel K.", "D. James") were joined for scoring so that they do not count as sentence breaks.

| field | words | Reading Ease | FK grade |
|---|---|---|---|
After Round 1:

| field | words | Reading Ease | FK grade |
|---|---|---|---|
| statusDescription | 44 | 55.3 | 8.3 |
| sourcing | 38 | 50.3 | 8.6 |
| floorNote | 82 | 70.1 | 6.4 |
| relationsSummary | 44 | 61.1 | 7.5 |
| why | 85 | 54.1 | 9.2 |
| longDescription | 126 | 59.7 | 8.4 |
| legacy | 44 | 74.5 | 5.6 |
| **all row prose** (teaser included) | 479 | **59.6** | **8.0** |

Before Round 1 the row scored 60.0 / 8.0 on 437 words. The fixes add longer names and words (Religious Roundtable, organizations, the quoted principles), which lowers Reading Ease by 0.4. The two Dallas sentences were split to hold it there. All new prose, with the IX.33 and IX.24 lines added and initials not joined (`apply.py`), scores 59.4 / 7.8. The row averages about 11 words a sentence. The longest has 19 words, and none is over 25. The fields below 60 are held down by names: Moral Majority, Christian Coalition, Faith and Freedom Coalition, and the names of persons. The new disclosure sentences on IX.33 and IX.24 run 7 to 20 words each.

## 7. Wanted list (W20, revised)

Lifted by this run:
- The Moral Majority's 1979 founding date, now verified (E1). The founding text itself is still wanted (below).
- The source of Falwell's "coalition of moralists" words, found: *The MacNeil/Lehrer Report*, 22 August 1980 (E2).
- The Dallas date (R1-C3): the address is dated 22 August 1980 (E3).
- Reagan's 22 August 1980 address, read word for word from the audio-transcribed text (E3, after Round 1).
- V1.0's "coalition of moralists" string, read word for word in the clip transcript (E2, after Round 1).

Still wanted, for the source-research thread:
1. **The Moral Majority's own founding text**: its articles of incorporation or first statement of purpose (1979), and the first issue of the *Moral Majority Report*. Liberty University Archive, Moral Majority Record Groups 1 to 3.
2. **The full record** of Falwell's 22 August 1980 interview (AAPB, cpb-aacip-507-0v89g5gw13), beyond the 06:22–10:45 clip.
3. (Lifted after Round 1: Reagan's address, now read word for word, E3.)
4. **The founders' circle**: a scholarly account of the Lynchburg meeting of 1979 and the roles of Weyrich, Viguerie, Phillips, Billings, McAteer and Dolan (Martin 1996 or Williams 2010, with page numbers). Needed before any copy says who besides the five ministers founded it.
5. **The Christian Coalition's own founding statement** (1989) and any statement of its basis.
6. **The Faith and Freedom Coalition's own dated founding document** (2009), and the 14 May 2009 date from a dated source.
7. **A statement of faith from any of the three carriers**, if one exists. If none does, record that it was searched for and not found. This would settle Section A on the carriers' own texts.
8. **Whitehead & Perry's definition**, verified, if the later Christian-nationalism works are ever cited. This row no longer uses it.
9. **A scholarly source** for any claim that the media carriers (Limbaugh, 1988; Fox News, 1996) carried the movement's story, if that line is ever restored.
10. **A dated item after 2010** from the movement's own carriers (for example the Faith and Freedom Coalition's 2025 conference program), to add own-voice evidence to the living mark.
