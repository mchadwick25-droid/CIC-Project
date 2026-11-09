# Era 10, IX.50 the Christian Right: adversarial review, Round 1

Reviewer: independent Opus 5.5 review · 2026-11-09 · Round 1 (full)

**Object.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_Step0_Era10_IX50_Proposed.json` and `CiC_Step0_Era10_IX50_Trace.md`, branch `claude/era10-p2e10c` (pulled; up to date).
**Ruling checked against.** Decision-Log, "Era 10 follow-up rulings" (2026-11-09), item 1: G-15 option (i). Prior drafts: D-E6 (`CiC_Step0_Era10_V2_0_Proposed_Edits.json`, `newEntries`) and V2.0 §3, §2d, G-15.
**Method.** Every item the trace calls verified was re-checked with WebSearch (mode "standard"). Where a page could be fetched, it was read directly with `curl`, and the text was searched for the quoted strings. No model was used to read pages. No repo file was edited. No metered model call was made.

## Verdict

**Not yet approved to proceed. One SUBSTANTIAL finding (the id) and nine MINOR findings. All are fixable in one revision, then a targeted Round 2 recheck.**

The row is careful work. No fabrication was found. Every quotation in the row matches its source word for word. Every date and name checks out. The tone is even: the row tells dated acts and texts and lets the movement speak for itself through Falwell's own 1980 words. It says nothing about motives. The findings below are about scope (claims a little wider than their evidence), one framing that implies a link the record does not show, and the id.

## 1. Re-verification of the trace's verified items

| # | Item | Result | How checked |
|---|---|---|---|
| E1 | Liberty University Archive, MOR Record Group 2 finding aid | **Confirmed.** PDF (4 pp.) downloaded. The historical note matches the trace's quotation word for word: founded 6 June 1979 by Falwell, LaHaye, Stanley, Kennedy, Dixon; "four principles; being pro-life, pro-family, pro-morals, and pro-American"; headquarters in Washington D.C.; "disbanded in 1989". "Last updated on March 24, 2014." | curl + pdftotext |
| E2 | MacNeil/Lehrer Report, 22 Aug 1980, AAPB cpb-aacip-507-0v89g5gw13 | **Confirmed.** Page gives "The MacNeil/Lehrer Report \| NewsHour Productions \| August 22, 1980", clip 06:22–10:45, record link `/catalog/cpb-aacip-507-0v89g5gw13`. Transcript reads: "Moral Majority of which I am the head- it's not a religious organization. It is totally political"; "72,000 pastors, Roman Catholic priests, Jewish rabbis, Mormon elders, fundamentalist, you name it, in Moral Majority". **Also on the page, verbatim:** "there is a coalition in this country of moralists. They're not all evangelical by any means; moralists who share similar moral values" and "though we theologically have great differences, we we very much share those premises and are willing to fight together" (see M2). | curl, string search |
| E3 | Reagan, National Affairs Briefing, 22 Aug 1980 | **Confirmed, and more than the trace saw.** The American Rhetoric page returned 200 with a browser user-agent. Header: "delivered 22 August 1980, Dallas Reunion Arena, Dallas, Texas [AUTHENTICITY CERTIFIED: Text version below transcribed directly from audio]" (marked abridged). Full sentence read: "Now, I know this is a non-partisan gathering, and so I know that you can't endorse me, but I only brought that up because I want you to know that I endorse you and what you're doing." The row's short quotation and paraphrase are exact. Search also confirms the briefing was organized by the Religious Roundtable (Ed McAteer) and James Robison (Miller Center, "Building a Movement Party"). The Miller Center quotes a looser variant; the row's form is the audio-transcribed one. | curl; WebSearch |
| E4 | Christian Coalition 1989; Reed executive director | **Confirmed.** EBSCO: "In 1989, following his unsuccessful bid for the Republican presidential nomination, Pat Robertson founded the Christian Coalition"; "Ralph Reed (b. 1961), executive director of the Christian Coalition, 1989-1997". Encyclopedia.com: "launched in 1989 with the assistance of its first executive director, Ralph Reed." | curl; WebSearch |
| E5 | Faith & Freedom Coalition, About page | **Confirmed.** "Ralph Reed is the founder and chairman of the Faith & Freedom Coalition, which he formed in 2009". The page is undated and carries a timeline to 2020. It also carries a values statement ("We believe that the greatness of America lies ... in the character of our people") and a "Five-Fold Mission" ("people of faith and like-minded individuals"; "on behalf of Christian values"). No creed. | curl; WebSearch |
| E6 | Williams, *God's Own Party* (OUP, 2010) | **Confirmed.** OUP 2010, viii + 372 pp.; *Church History* review (Trollinger); also reviewed in *EJAS* (Krabbendam). | WebSearch |
| E7 | Martin, *With God on Our Side* (Broadway, 1996) | **Confirmed.** *Christianity Today* (1997): Broadway Books, 418 pp., fall 1996; PBS companion. | WebSearch |
| E8 | Wilcox, *Onward Christian Soldiers?* (Westview, 1996; 4th ed. 2010 with Carin Robinson) | **Confirmed.** 1st ed. Westview 1996 (Dilemmas in American Politics, xii + 180 pp.); 2nd 2000; 3rd 2006 with Carin Larson; 4th with Carin Robinson, catalogued as 2010 in some records and 2011 in others. Larson and Robinson are the same co-author under two surnames. | WebSearch |
| E9 | Lewis, *The Rights Turn* (CUP, 2017) | **Confirmed.** CUP, October 2017, Cambridge Studies in Social Theory, Religion and Politics; reviewed in *Perspectives on Politics*; 2018 APSA Hubert Morken award. Its subject is current evangelical rights-based advocacy and opinion. | WebSearch |
| E10 | *Washington Examiner*, 2025 Road to Majority | **Confirmed.** Article exists at the cited URL. The search result gives its date as 26 June 2025. The coalition's own pages give 26–28 June, Washington Hilton. | WebSearch |

**Sentence check.** Every sentence in the row was checked against its traced item (trace §3). All are supported, with the exceptions listed as findings M1, M3, M4, M5 and M6.

## 2. Findings

### S1 — SUBSTANTIAL. The id must not be published as `christian-right-and-christian-nationalism`

- **Location.** `newRows[0].id`; `_meta.id`; trace §5 "id"; trace §5 "Validator" (the expected missing tree page).
- **Evidence.** The census rule (`meta.identifiers`): "Movement IDs ... are permanent. Once published, an ID is never changed or reused." V2.0 §3 dropped "Christian Nationalism" as the name because its naming wave (2019–2022) is after the era. The row's own name, sources and living evidence all avoid that label. Publishing the id would fix in a permanent public address a post-era label that the row itself declines to use, and that is a contested label in current debate. That breaks the window and the even tone at the one place that can never be corrected. The ruling took option (i) "drafted from D-E6", and D-E6 carries the name (n1) "The Christian Right". The census derives ids from names (`the-christian-homeschool-movement`, `the-rescue-mission-movement`, `the-liturgical-movement`).
- **Availability.** `the-christian-right` is free. It occurs nowhere in the release 22 census (movements, edges, `retiredMovements`, `retiredLinks`), nowhere in `origin/main` or `origin/live` census, and there is no `cft-website/tree/` page for it. The old id also appears in no published census or tree page; it lives only in Design files.
- **Fix.** Set `id` to `the-christian-right`. Rewrite `_meta.id` to: "The id follows the name (G-15 naming sub-option n1, as drafted in D-E6). The earlier draft id, which carried 'christian-nationalism', was never published." Update trace §5 (id note and validator line) to the new id. Name the change to Mark in one line when the row goes up, since n1 was not ruled separately; if he picks n2 instead, the id becomes `the-new-christian-right`. Either way, the old id must not ship.

### M1 — MINOR. floorNote: the first sentence claims more than the dated statement shows

- **Location.** `floorNote`, sentence 1: "There is no confession of its own to test."
- **Evidence.** The dated statement (E2) is one founder's 1980 account of one group. It shows that Falwell called the Moral Majority "not a religious organization". It does not show that no statement of faith existed, and it does not speak for the Christian Coalition or the Faith and Freedom Coalition. The trace §4 says so itself ("None was looked for beyond these searches"; "One 1980 interview ... cannot speak for the Christian Coalition"). The closing sentence hedges, but the opening one is stated flat, as settled, for the whole movement.
- **Fix.** Replace sentence 1 and move the conclusion after the evidence: "In August 1980 Jerry Falwell said the Moral Majority was not a religious group. 'It is totally political,' he said. He counted pastors, Catholic priests, Jewish rabbis and Mormon elders among its members. On his account, it had no confession of its own to test. No statement of faith has been found for it or the later groups. The churches its members came from are not tested through it. This reading is not settled until the later groups' own statements are checked." (This also takes C3's "members".)

### M2 — MINOR. The trace understates what is verified, and the wanted list is out of date

- **Location.** Trace §1 "Still [S]" (items 3 and 4); §4 "What it cannot read" (last bullet) and "Status"; §7 wanted items 2 and 3.
- **Evidence.** The AAPB clip transcript at the cited URL carries V1.0's "coalition of moralists" string word for word (see E2 above). The American Rhetoric page can be read: it returned 200 with a browser user-agent, gives the full Reagan sentence, and says it was "transcribed directly from audio". These are no longer [S].
- **Fix.** Move both items to "Verified in this run", with the URLs and the exact wording above. Note that the AAPB text is a transcript of a clip (06:22–10:45), not the full record. Lift wanted item 3. Narrow wanted item 2 to "the full record beyond the 06:22–10:45 clip". In §4, change the last "cannot read" bullet so that it rests only on the founders' circle, and add that Falwell said "though we theologically have great differences, we ... share those premises" (an own-voice, dated statement that supports the coalition reading). The row's text need not change for this, but the floorNote may use that quotation if wanted.

### M3 — MINOR. The Dallas framing implies Reagan endorsed the Moral Majority

- **Location.** `longDescription`, sentences 4–6; `why`, sentences 2–4.
- **Evidence.** The National Affairs Briefing was held by the Religious Roundtable (Ed McAteer), with James Robison, not by the Moral Majority (Miller Center, "Building a Movement Party"; V2.0 §3 already carries it as "the Religious Roundtable's National Affairs Briefing", verified). In `longDescription` the quotation follows two sentences about the Moral Majority and opens "That month", so "you" reads as the Moral Majority. Reagan's "you" was the audience in the arena.
- **Fix.** `why`: "In August 1980 Ronald Reagan, then running for president, spoke at a briefing in Dallas run by another group, the Religious Roundtable." `longDescription`: "That month, at a Religious Roundtable briefing in Dallas, Ronald Reagan told the crowd, 'I endorse you and what you're doing.'" Add a `sources` entry for the organizer, for example Miller Center, "Building a Movement Party" (millercenter.org/node/48826), type "reference", after reading it; add it to trace §1 and §3.

### M4 — MINOR. The four principles are given in the narrator's voice

- **Location.** `longDescription`, sentence 2: "It stood for four aims: pro-life, pro-family, pro-morals and pro-American."
- **Evidence.** These are the movement's own labels (E1, "four principles"). "Pro-life" and "pro-family" are self-names that the other side of the debate does not accept. Stated without attribution, they read as the map's own description. A scholar of either view would ask for them to be marked as the movement's words.
- **Fix.** "It named four principles of its own: 'pro-life, pro-family, pro-morals, and pro-American'." (E1 wording, quoted.)

### M5 — MINOR. sourcing: "Three studies trace the whole movement"

- **Location.** `sourcing`, sentence 4.
- **Evidence.** Martin (1996) and Wilcox's first edition (1996) end in 1996. They cannot trace a movement whose window runs to 2010 and whose third group dates from 2009. Only Wilcox's 4th edition and Williams (2010) reach the end of the window.
- **Fix.** "Three studies trace its history: William Martin (1996), Clyde Wilcox (1996, revised to 2010) and Daniel K. Williams (2010)."

### M6 — MINOR. relationsSummary: "It grew out of the fundamentalist and evangelical churches, which have their own entries"

- **Location.** `relationsSummary`, sentence 1.
- **Evidence.** The traced items do not show "grew out of" for evangelical churches. E1 shows that the founders were ministers, and E2 that its backers were "not all evangelical". Only repo-IX.33 (census text) supports a link, and only for Fundamentalism. There is no entry for American evangelical churches of 1940–1979; IX.24 is a global network from 1974. Fundamentalism is entered as a movement, not as churches.
- **Fix.** "The entry on Fundamentalism traces this movement back to it. Its founders were ministers. Its groups drew support from several churches and faiths, and none became a church." (Keep sentence 3 as is.)

### M7 — MINOR. IX.24 disclosure line: a non sequitur, and outside option (i) as written

- **Location.** `registerEdits[2]` (IX.24 `relationsSummary`).
- **Evidence.** The line is appended after "Graham's evangelistic association was incorporated in 1950." It does not say how the Moral Majority relates to Lausanne-era global evangelicalism. Placed after Graham, it reads as a lineage that the record does not show. V1.0 drew the IX.24 line as a distinction ("disclosure, not identity"; IX.24 is framed globally, not as an American partisan formation). Also, G-15 lists the IX.24 line under option (ii), not (i). Under (i) a pointer is reasonable, but the trace should say why it is kept.
- **Fix.** Replace `new` with: "Graham's evangelistic association was incorporated in 1950. The Christian Right, a political movement that American ministers began with the Moral Majority in 1979, has a separate entry." In the `ruling` field and trace §2, state that the line is carried over from option (ii) as a cross-reference and marks a separate entry, not a lineage. (Or drop the IX.24 edit, since the ruling under (i) does not require it.)

### M8 — MINOR. livingEvidence: Lewis is not recorded as describing the present

- **Location.** `livingEvidence.evidence`.
- **Evidence.** §2d: "A later study of earlier history does not count unless the repo records that it describes the present." The row's evidence line gives only the title and "independent scholarship; verified". Lewis does study present-day evangelical rights-based advocacy and opinion (to 2016), so the CD grade holds, but the row must say so. The search result also gives the *Examiner* article's date, 26 June 2025.
- **Fix.** "Andrew R. Lewis, The Rights Turn in Conservative Christian Politics (Cambridge University Press, 2017), a study of its present-day advocacy and opinion: independent scholarship; verified. Washington Examiner, on the Faith & Freedom Coalition's Road to Majority conference (26 June 2025; the conference met 26-28 June): independent news; verified." Update the `sources` note for E10 to match. The grade (CD; newest 2025) and group L-3 stand; L-3 (uncertain) is right, since the entry names a current, not a body.

### M9 — MINOR. voices: Reagan is listed as a voice of the movement

- **Location.** `voices[1]`.
- **Evidence.** The other voices founded or led its groups, or wrote its history. Reagan was a candidate who addressed the movement's audience once. Listing him among its voices places a person inside the movement on one quotation, which is a classification of a person, not a dated act. It also repeats M3's implied endorsement.
- **Fix.** Remove `voices[1]`. Reagan stays in `why` and `longDescription`, where the act is dated and placed.

### C1 — COSMETIC. "Its public record is strong"

- **Location.** `statusDescription`, sentence 3.
- **Evidence.** `sourcing` says "Moderate to rich" (B1). The trace cites B1 and B4, but B4 is user need, not record.
- **Fix.** "Its public record is moderate to rich."

### C2 — COSMETIC. "run by groups"

- **Location.** `statusDescription`, sentence 2.
- **Fix.** "It was a political movement carried by organizations, not a church or a confession." (D-E6's own word, and the census's for IX.54–IX.58.)

### C3 — COSMETIC. Source notes

- **Location.** `sources`.
- **Fix.** Add Encyclopedia.com, "Christian Coalition", type "reference", note "Names Ralph Reed as its first executive director", since `why` and `voices` say "first" and EBSCO does not. Wilcox: "4th ed., with Carin Robinson, 2010" is fine, but the note may add "catalogued 2010 or 2011". In `floorNote`, "backers" becomes "members" (Falwell: "in Moral Majority"); taken into M1.

### C4 — COSMETIC. IX.33 now points to the new entry twice

- **Location.** `registerEdits[0]` and `[1]`.
- **Evidence.** Both edits read well and do not damage IX.33. Each old string occurs exactly once in release 22 (re-checked). After both, IX.33's `legacy` and `relationsSummary` each say the entry exists. That is acceptable, and the `legacy` edit is required (its old sentence becomes untrue). No change needed. Optionally drop the `relationsSummary` pointer.

## 3. The asked checks

1. **Fabrication.** None. All ten items confirmed (§1). Every quotation is exact. Three phrasings claim more than their items show (M1, M5, M6), and one juxtaposition implies a link (M3).
2. **Fairness and tone.** Even. No motive claims. Reed, who is living, appears only through dated acts and offices. The movement speaks in its own 1980 words. Fix the narrator-voice self-labels (M4), the Dallas framing (M3) and Reagan as a voice (M9).
3. **Section A.** The floorNote rests correctly on the dated statement and says plainly that the reading is not settled. Its first sentence widens one founder's 1980 account into an absence claim for the whole movement (M1). The dated statement, read further, gives better own-voice support than the trace knew (M2).
4. **Window.** Nothing after 2010 in the history. Lewis (2017) and the *Examiner* (2025) are used only for the living mark and are labelled so. The FFC About page is undated and current, and is used only for the 2009 founding, which is acceptable. livingEvidence is graded right under R3 (CD on a verified independent study after 2010; L-3, uncertain), once M8 records that Lewis describes the present.
5. **Fit.** The key list and order are identical to IX.55. `kind`, `statusWord` and the Tier 3 wording match IX.25, IX.28 and IX.49. `livingEvidence` has the same four fields as IX.54–IX.58. `modernCountries` and `regions` match IX.55. Meta counts are right: 307 + 1 = 308 rows, and Pre-Survey Candidate 225 + 1 = 226 (recounted from release 22). `liveCount` is unchanged, correctly. The IX.24 edit needs M7.
6. **Readability** (`engine/m7/readability.py` `measure`, initials joined as the trace did). All row prose: 440 words, 35 sentences, FRE 60.25, FK 7.98. That matches the trace (60.0 / 8.0). By field: statusDescription 67.3 / 6.5; sourcing 52.5 / 8.3; floorNote 66.2 / 6.8; relationsSummary 59.3 / 8.6; why 54.3 / 9.6; longDescription 60.4 / 8.3; legacy 74.5 / 5.6. No sentence runs past 25 words (the two 22–25 word "sentences" the splitter reports are a quotation ending in `.'` joined to the next sentence). The grade sits right at the floor of 8; that is acceptable, since the low fields are held down by proper names. Re-score after the fixes; M3 and M4 add a few long names and will move FRE down slightly.

## 4. For Round 2 (targeted recheck)

Check only: the id and `_meta.id` (S1); the floorNote (M1); the trace's verified list, §4 and §7 (M2); `why` and `longDescription` on Dallas, plus the new source (M3); the quoted principles (M4); `sourcing` (M5); `relationsSummary` (M6); the IX.24 edit and its stated reason (M7); `livingEvidence` and the E10 note (M8); `voices` (M9); and a re-score of readability.
