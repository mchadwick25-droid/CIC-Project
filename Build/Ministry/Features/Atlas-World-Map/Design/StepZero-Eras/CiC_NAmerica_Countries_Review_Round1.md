# N. America countries: adversarial review, Round 1

Reviewer: independent Opus 5.5 review · 2026-11-10 · Round 1 (full)

**Object.** `Build/Ministry/Features/Atlas-World-Map/Design/StepZero-Eras/CiC_NAmerica_Countries_Proposed.json` (30 edits with evidence quotes, 1 `noChange`, 7 `doubtful`), against `cic-website/data/world-census.json` (release 25). Branch `claude/n-america-countries`, head `4f7212547`.

**Rules applied.** Atlas Decision-Log, 2026-11-10, "Change order: modern countries for rows labeled 'N. America'" (Mark: option c):
- A row whose `placeLabel` has a part "N. America" (a trailing " and beyond" ignored) gets a modern country only when the row's own text names that country or a place inside it.
- Only United States (Q30), Canada (Q16) and Mexico (Q96), each with place "N. America", placeId Q49.
- "American" as an adjective counts only when it plainly means the United States.
- Publisher cities in source titles do not count.
- Places named only for a later or other body do not count.
- Rows that name nothing stay empty.

Also CLAUDE.md, "Trust and source fidelity": evidence is a claim to re-check, not a fact to trust.

**Method.**
- Listed every census row by its label parts. Exactly 31 rows qualify. All 31 are in the proposal (30 edits, IX.32 as `noChange`). Out-of-scope labels seen: VII.13 "England · America", VIII.2/VIII.3 "American frontier", VIII.48 "Spanish America", IX.8 "Central America", IX.48 "North America".
- For each edit: checked `id`, checked `old` deep-equals the census, checked `new` = `old` plus only the allowed entry shapes, checked one evidence item per added country in the same order. Resolved each evidence `field` path and counted the quote. Every quote occurs exactly once in its named field.
- Read each quote in context. Then scanned every text field of all 31 rows with a gazetteer of US states and cities, Canadian provinces and cities, and Mexican places, plus "America(n)", "United States", "Canad-", "Mexic-". Read each hit for misses and for wrongly placed names.
- Applied the proposal with my own script (`apply.py`, scratch dir): only `modernCountries` of the 30 rows changes; meta and every other field are untouched; the census round-trips byte for byte before the edit. Ran `node tools/validate-census.mjs <applied> --atlas cft-website/index.html`: **322 movements, 578 edges, 10 eras — 0 errors, 2 warnings** (the two existing `shortName` warnings, same as the base file).
- Rendered every row's place line with `cic-website/assets/place-line.js` (the code `cft-website/index.html` calls through `placeLine()`), to see the order question.
- No repo file edited. No metered model call.

**Result in one line.** The country lists are right for all 31 rows: every added country is supported by the row's own text, and nothing is missed. Three evidence quotes do not meet the rule, though the country they support is shown elsewhere in the same row. Those must be swapped before the trace can stand.

## SUBSTANTIAL findings

### S-1 — IX.15 United States: the quote names another body's event

- **What.** Evidence is `relationsSummary` "Azusa Street", in "grew directly out of the wider Pentecostal movement that followed the Azusa Street revival". Azusa Street is the parent movement's revival (1906), not Oneness Pentecostalism's own story. That is a place named for another body, which the rule excludes. The drafter's own `doubtful` note points to better text.
- **Outcome.** United States stays. The row's own story is in the US: the Pentecostal Assemblies of the World, the Oneness body, was led from Indianapolis.
- **Fix.** Replace the evidence item with `{"country": "United States", "field": "documentedStories[1].text", "quote": "The Pentecostal Assemblies of the World was led from Indianapolis"}`. Update the IX.15 `doubtful` entry to match (or drop it, since the order point moves to M-3).

### S-2 — IX.28 United States: the quote belongs to the new monasticism, a separate current

- **What.** Evidence is `relationsSummary` "Durham, North Carolina". The sentence is "The new monasticism began in the same years. In 2004 more than sixty people in Durham, North Carolina, drafted its twelve marks." The same field calls the new monasticism something the row "overlaps", not the row itself. That is a place named for another body.
- **Outcome.** United States stays. The row's own text puts the emerging-church conversation in the US: "reprinted in the United States in 2003, by which time an American conversation had begun to use the same vocabulary". Here "American" plainly means the United States, as the clause before it says.
- **Fix.** Replace the evidence item with `{"country": "United States", "field": "documentedStories[0].text", "quote": "by which time an American conversation had begun to use the same vocabulary"}`.

### S-3 — IX.29 United States: the quote is only an organization's name

- **What.** Evidence is `relationsSummary` "Dallas Theological Seminary". The text never says where the seminary is. The draft rightly leaves Canada out of IX.29 and IX.33 because "Niagara Bible Conference" is a name that states no place. "Dallas Theological Seminary" is the same case. Keeping one and dropping the other is an inconsistent use of the rule.
- **Outcome.** United States stays. Scofield's work on the Reference Bible, the row's own "mass formation text", is placed in the US in plain words.
- **Fix.** Replace the evidence item with `{"country": "United States", "field": "documentedStories[1].text", "quote": "He worked in Dallas, in Northfield, Massachusetts"}`.

## MINOR findings

### M-1 — Five quotes lean on a person's description when the row says it outright

The country is right in each case and the quote is not false, but each quote describes a person rather than placing the movement. A stronger quote sits in the same row. All replacements below are exact, single-occurrence substrings.

| Row | Current quote | Replace with |
|---|---|---|
| VIII.4 US | `why` "New York doctor's wife" | `teaser` "a movement launched from a New York parlor" |
| VIII.16 US | `longDescription` "New England" (in "a New England woman") | `teaser` "New England and outward" |
| VIII.17 US | `why` "American Civil War" (adjective only) | `documentedStories[0].text` "The brethren of Ogle County, Illinois" |
| VIII.34 US | `documentedStories[0].text` "James Osgood Andrew of Georgia" | `documentedStories[0].text` "The General Conference met in New York on 1 May" |
| VIII.36 US | `longDescription` "Long Island" (Hicks's home) | `documentedStories[0].text` "In April 1827 Philadelphia Yearly Meeting" |

Optional, same kind: IX.33 "Los Angeles campaign" (Billy Graham, 1949, on the edge of the row's story) could be `documentedStories[0].text` "John Scopes, a young teacher in Dayton, Tennessee".

### M-2 — VIII.34 Canada: the quote stops before the church

- **What.** "emigrated to Ontario" says only that five men moved. The row's story (Methodism) reaches Canada in the next words.
- **Fix.** Extend the quote to `"emigrated to Ontario, where Loveless helped found a Methodist chapel"` (same field, occurs once). Canada stays.

### M-3 — IX.15 and IX.16: order puts Mexico before the United States, and the order shows

- **Does the order matter?** Yes, for display. In `cft-website/index.html`, `modernCountries` is used only through `placeLine()` → `CFTPlace.formatPlace` (`cic-website/assets/place-line.js`). That function lists the countries under each place in array order. The cards and tree would read "N. America, Mexico and United States and beyond" (IX.15) and "N. America, Mexico and United States · Korea, South Korea and beyond" (IX.16). No map code in that page reads the order: no other code path uses `modernCountries` or `countryId`. The validator does not check order either.
- **Why it is a finding.** "First appearance across fields in file order" is a mechanical rule that no Decision-Log entry sets. Where existing rows list more than one country under one place, the census puts the core country first (Aksum: Ethiopia, Eritrea; Makuria: Sudan, Egypt; al-Andalus: Spain, Portugal). Both rows' own texts open in the US: IX.15's teaser is "North America and then worldwide, 1913", with Arroyo Seco in 1913 before Mexico in 1914. IX.16's teaser reads "North America, Korea and Mexico". So Mexico first reads as if the movement began there.
- **Fix.** In IX.15 and IX.16 `new`, put the United States entry before the Mexico entry, and the evidence items in the same order. Optionally, for IX.15's Mexico evidence, the row's own story is clearer in `longDescription` "In Mexico the Apostolic revival began in 1914" than in the `region` word alone (both are valid).

### M-4 — IX.48 "North America" is outside this change order, but has the same gap

- **What.** IX.48 (American Orthodoxy) has the label "North America", not "N. America", so the ruled rule does not reach it. Its `modernCountries` is empty, as the 31 were. The draft is right not to touch it.
- **Fix.** Do not change it here. Register it in the Atlas Open-Gaps as a possible follow-on for Mark to rule on (same rule, or a label change to "N. America"), so it does not go quiet.

## Points checked and found right (no finding)

- **IX.57 Canada (Toronto Blessing, 1994).** Kept. The row runs 1982 to c. 2010, so 1994 is inside its window. The row says the revival "grew inside one of its churches" (`relationsSummary`), and the Vineyard cut ties only in December 1995. So at the time named, the Toronto Airport Vineyard was this row's own body, not a later or other one. The current quote is valid; `relationsSummary` "The Toronto Blessing of 1994 grew inside one of its churches" is the clearest backing, and the `doubtful` note can say so.
- **VIII.34 Canada (Tolpuddle).** Kept, with M-2's longer quote. The founding of a Methodist chapel in Ontario is Methodism's own story in Canada.
- **VIII.4 Canada (Hamilton, Canada West).** Kept. The Hamilton meetings of 1857 are the Holiness movement's own story. "Canada West" is the earlier name of a place inside modern Canada, not a later or other body. "Hamilton, Canada West" would also do as the quote.
- **Wrongly placed names, none used.** "Georgia" in VIII.34/VIII.35 is the US state (Georgia law, Augusta). "Presbytery of New Brunswick" (IX.33) is in New Jersey, and the draft rightly did not read it as Canada. Birmingham in IX.32 and VIII.17 is in England; the Birmingham in IX.41 (Alabama) is not used. "Washington" in IX.35 and IX.44 and "Washington Gladden" (IX.34, a person) are not used. Toronto in VIII.15 is a publisher city in source titles, rightly excluded.
- **Doubtful list.** The Niagara Bible Conference (IX.29, IX.33), "Dallas Willard" (IX.32), "North American Christian Convention" (IX.42) and "Latin America" (VIII.25; the 1916 conference met at Panama, outside the three countries) are all rightly left out.
- **IX.32 noChange.** Right. I read every text field. The row names only Newbigin, Willard, Wright, Madras, Birmingham, Selly Oak and Winson Green. "Dallas" is part of a name. It stays United Kingdom only.
- **Misses.** None. Every one of the 30 edited rows names a US place in its own story, and all 30 get the United States. The only Canadian places in the 31 rows' own stories are in VIII.4, VIII.34 and IX.57. The only Mexican places are in IX.15 and IX.16. All five are taken.
- **Release note.** `cft-website/index.html` embeds the movement data (`const DATA`, 322 rows), and `engine/m6/census_atlas_sync.py` mirrors `modernCountries`. The data release must rebuild both for the change to show.

## Verdict

**Not yet approved to proceed.** S-1, S-2 and S-3 are evidence-record defects. Each cites a quote that the rule itself excludes. No country in the census output changes: all 31 rows' country lists are correct as drafted, and the applied file validates with 0 errors. The fixes are three quote swaps, given exactly above. M-1 to M-3 should be made in the same pass. M-4 is a gap to register, not a change to make here. A Round 2 targeted recheck of the changed evidence and order then suffices.
