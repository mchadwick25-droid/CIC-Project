# Church Family Tree map, direction B: participant-facing text, round 3 (targeted recheck, last round)

Reviewer: fresh round 3 reviewer, reading bar, fidelity and the AI-tells check together. No repo file edited. No model calls of any kind.

## What was checked, and how

- Branch `claude/cft-map-direction-b`. The brief's diff (`git diff b2585784 HEAD`) ends at **c49b38bf**. Line numbers below are `cft-website/index.html` at c49b38bf.
- I read runtime text in Chromium (Playwright) from a private copy of 618d3ab5. That commit is c49b38bf plus a panel-position fix with no text in it. Sizes: 1440x900, 820x1180 and 390x844 (touch). I read all 15 river cards and tooltips, all ten era cards (story lists opened), the Key, the era labels, info marks and strip, 350 tradition labels and tooltips, the movement and council labels, 62 map-story and 504 documented-story tooltips, and the date lines of every tradition card. There were no page errors.
- HEAD moved during the review to **56c1bb2a**. That is a merge of origin/main (era 4 live, 878dc40d), then a commit adding `major` and `activeYear` to 60 era 4 people. I checked both against my findings. All 350 traditions keep their river, years and era. The census entries I cite are unchanged, except "Coptic Christianity under Early Islam", whose new text keeps "a shift historians place mostly later, and argue about still". So nothing below changes.
- Claims were checked against `cic-website/data/world-census.json`, the page's own `DATA`, and, for the era notes' origin, `Build/Ministry/Features/Atlas-World-Map/Design/CiC_World_Atlas_PreStep0_Survey_V0_1.md`. Scores come from `engine/m1/fk.py`, given as FK / FRE.
- Mark's eight round 2 picks (findings 1, 2, 6, 7, 8, 9, 10 and 11) match round 2's proposals exactly. I checked this by script, on the map and on the method page. "Mark-approved" below marks a fault found in his picked wording; those need his ruling.

## Counts

- **Round 2 findings (15):** 13 resolved, 1 partly (5), 1 applied ahead of the ruling it depends on (15). Two of the fixes exposed new faults (3 led to new finding 1; 13 led to new finding 6).
- **Round 2 process items (3):** all 3 still open.
- **Round 1 items round 2 carried:** r1-tells 27 and 28 are still open (not applied). r1-tells 34 is still Mark's call. The census deferrals are still not logged (P1).
- **New findings: 6. 2 BLOCKING, 4 MINOR.**
  - BLOCKING: 1 (river card era line) and 2 (Caucasus river note).
  - MINOR: 3 and 4 are Mark-approved era notes. 5 and 6 are not approved wording.
- **New process item: 1 (P4, the river notes).**

---

## Round 2 status

### New findings of round 2

| # | Subject | Status at c49b38bf |
|---|---|---|
| 1 | Era 4: minority claim told as settled | **Resolved** (Mark's pick). The merged Coptic entry still says the shift is placed "mostly later", so "starts to become" agrees with it. |
| 2 | Era 5: "Byzantium consolidates" | **Resolved** (Mark's pick). The rest of the note: see new finding 4. |
| 3 | River card span | **Resolved.** Card and tooltip now share `riverSpan`: Latin West reads "97 traditions · 197–2010" in both, and Church and Empire "1 tradition · about 312–451". The new header shows a fault in the line below it; see new finding 1. |
| 4 | River card "Built & Live", "movements" | **Resolved.** "Its one tradition has a Representative.", "2 of its 28 traditions have a Representative.", "None of its 2 traditions has a Representative yet.", "Traditions in this river" and the new note all read correctly. The counts match the 11 built worlds. The era line's logic is new finding 1. |
| 5 | River notes give counts the card contradicts | **Partly.** Africa, Latin West, Protestant & Evangelical and Non-Nicene no longer give counts, and the Latin and Protestant note is hidden. The Caucasus note was missed (new finding 2). The Africa rewording now hides two entries (new finding 5). The root cause is wider than counts (P4). |
| 6 | Era 1 note | **Resolved** (Mark's pick). |
| 7 | Era 3 note | **Resolved** (Mark's pick). The pre-survey says "monasticism becomes the era's formative engine everywhere", so "the churches everywhere" is faithful. |
| 8 | Era 9 note | **Resolved** (Mark's pick). No summary closer is left. FK 10.2 / FRE 34. |
| 9 | Era 10 "Spirit-movement" | **Resolved** (Mark's pick). The note's scale claim is new finding 3. |
| 10 | Era 10 closing note | **Resolved** (Mark's pick). It is on the map, the method page and `Build/tools/tree_site_pages.json`, and the test checks both pages. |
| 11 | Key, "People of a river" | **Resolved** (Mark's pick). |
| 12 | Era card story years printed twice | **Resolved.** "The Great Alleluia of 1233", "The Bianchi of 1399" and "Nil Sorsky Stands Up at the Council of 1503" now print once. 24 lines still pair a year in the title with a fuller date, such as "Lausanne, 1927 3–21 August 1927". The date adds the day or month, so these are not repeats. |
| 13 | "c." in tradition and story dates | **Resolved for "c."** No date shows "c." on any label, tooltip, card date line, river list or era card. The widened rule missed one form; see new finding 6. The only "c." left is inside census short names, where it means "century" ("Uniate 18th c.", "Methodism 19th c."); see "Noticed". |
| 14 | "Major people" shows 12 of N silently | **Resolved.** "The map has 74 people from this era, 36 of them major. This list shows 12 of the major people." |
| 15 | "Opens a note on this era" | **Applied ahead of P2.** All four places now say "Opens this era's card." / "Opens that era's card." No ruling on the card's scope is logged. If Mark returns the card to A27, these four go back. |

### Process items of round 2

| # | Subject | Status |
|---|---|---|
| P1 | The census deferrals are not in Open-Gaps | **Open.** There are no entries on the branch or on main. Main's Open-Gaps now ends at 265 (era 4 live), so the new entries start at 266 once main is merged. |
| P2 | The era card's scope has no change order | **Open.** There is none in either Decision-Log, and finding 15 now assumes the larger card. |
| P3 | Proposed major calls shown as settled | **Open.** Nothing new is logged for the 38 entries of ab836b12. Decision-Log line 2026 states the rule. Line 2369 records Mark confirming the era 6 to 10 coordinator calls, not these. |

### Round 1 items that round 2 left partly or open

| Item | Status |
|---|---|
| r1-text 8, 9, 18 | **Resolved** through round 2's findings 3 and 4. The river notes still say "movements" in places; see P4. |
| r1-text 12 | Carried as P2. |
| r1-text 4 (root cause), 14, 27, 30 | **Deferred** to the census owner. Not yet logged (P1). |
| r1-tells 14, 39, 40 | **Resolved** through round 2's findings 8, 10 and 4. |
| r1-tells 41 | **Resolved.** The story tooltip reads "A story from the sources", where round 1 proposed "A story". All 62 map stories carry sources, so the line holds. The story card reads "Documented · a story". |
| r1-tells 27 | **Open, not applied.** Line 487: "An interactive map of Christian tradition, from the first house-churches to about 2010." Line 484 has the lower-case header version. Replacement as in round 1: "A map of Christian tradition, from the first house-churches to about 2010." (FK 5.8 / FRE 75). |
| r1-tells 28 | **Open, not applied.** Line 113850 still says "Tap an era or a river to zoom in." Only the era title zooms (the only caller of `goIntoEra` is the title label). Replacement as in round 2: `(coarsePointer?'Tap':'Click')+' an era title or a river to zoom in.'` (FK 3.7). |
| r1-tells 34 | **Still Mark's call** ("&" against "and" in river names). It has not been put to him. |

---

## New findings

### BLOCKING

**1. River card: the era line contradicts the span directly above it**
- Where: `openPanelRiver`, lines 113083–113084 (`eraNums`), used by `spanText` at 113097–113099. The line sits under "What sets this river apart".
- Current, as rendered:
  - Origin: "6 traditions · 70–900", then "Confined to a single era (Era 1)." Era 1 ends in 312. The river is drawn to 900, because Christian Apocrypha runs to 900.
  - Africa and Latin: "Found in 2 of the map's ten eras, from Era 8 to Era 10." That is three eras. Kongo after 1650 runs to 1881, inside era 9.
  - Global Revival & Pentecostal: "10 traditions · 1904–2010", then "Confined to a single era (Era 10)." Era 10 starts in 1906. The era 9 card lists this river under "Rivers that begin here".
  - Non-Nicene: "Found in 9 of the map's ten eras, from Era 1 to Era 10." The Cathars (about 1143–1321) run into era 6, and the river is drawn there.
- Code now: `const eraNums=[...new Set(members.map(m=>m.era))];`
- Why:
  - `eraNums` counts the eras in which traditions *begin*. The header, since round 2's finding 3, uses the years they are *active*. So do the drawn river (`concurrentCount`, `laneEndY`) and the Key ("A dashed river: Years when the map has no tradition on that river."). The two measures now meet on one card and disagree.
  - The wording ("Confined to", "Found in", "Present in") claims presence, so it is wrong on these four rivers.
  - Fix the measure once, rather than rewording the line.
- Replacement (lines 113083–113084):
  ```
  const eraIdx=new Set();
  members.forEach(m=>{const a=eraOfYear(m.start), b=Math.max(a,eraOfYear(m.end-1)); for(let i=a;i<=b;i++)eraIdx.add(i);});
  const eraNums=[...eraIdx].map(i=>eras[i].num);
  const eraMin=Math.min(...eraNums), eraMax=Math.max(...eraNums);
  ```
  - `m.end-1` stops a tradition that ends on an era's first year from counting in that era. Church & Empire ends in 451, so it stays "Confined to a single era (Era 2)."
  - I ran this in the page. It changes exactly these four rivers and leaves the other 11 as they are:
    - Origin: "Found in 4 of the map's ten eras, from Era 1 to Era 4."
    - Africa and Latin: "Found in 3 of the map's ten eras, from Era 8 to Era 10."
    - Global Revival & Pentecostal: "Found in 2 of the map's ten eras, from Era 9 to Era 10."
    - Non-Nicene: "Present in every one of the map's ten eras."
  - Origin's full line then scores FK 7.2 / FRE 64.

**2. Caucasus river note: a count and a gap that the card and the census contradict (round 2's finding 5 missed it)**
- Where: `RIVER_LORE["Caucasus"].riverCoherence`, line 111570, under "What makes it one river".
- Current: "The Armenian spine supplies ten of fifteen entries and for centuries flows outside the Caucasus altogether; the Georgian spine carries long disclosed gaps (609-780, 1245-1917)."
- Why:
  - The card's header, directly above, reads "18 traditions · 314–2010". Of the 18, 11 are Armenian and 5 Georgian; Caucasian Albania and the Paulicians make up the rest.
  - The map holds "Georgian Church 1650" (1650–1811), inside the stated 1245–1917 gap. The census's Georgian Golden Age entry now says: "No entry covers the church from 1245 to 1650."
  - Round 2 rated this fault BLOCKING for five other rivers. Its fix covered those five and missed this one.
  - The sentence is a long semicolon chain (FK 13.9).
- Replacement (FK 5.9 / FRE 67; it corrects two claims to the map's own entries and adds none):
  "The Armenian spine supplies most of its entries. For centuries it flows outside the Caucasus altogether. The Georgian spine has long gaps: 609–780, 1245–1650 and 1811–1917."
  - All three gaps come from the river's own entries. The census names the second one, and the Georgian 1650 and 1917 entries name the third. I found no census line naming 609–780, so the word "disclosed" is dropped.
  - If Mark wants no years at all: "The Georgian spine has long gaps."

### MINOR

**3. Era 10 note: a scale claim the census says needs a named count (Mark-approved)**
- Where: `WORLD_CONTEXT[10]`, line 111538. It is the main text of the era 10 card.
- Current: "… The Pentecostal and charismatic family becomes the largest new form of Christianity since the Reformation. …"
- Why:
  - The census's entry for this family (`global-south-pentecostal-christianity`) sets a rule: "Scale claims about this family are self-report or definitional aggregate unless an independent count is named." Its legacy says: "Counts of it need care … What is not in doubt is the direction of travel."
  - "The largest new form … since the Reformation" ranks the family by size. No count is named, and the census itself makes no such claim. The ranking comes from the pre-survey ("the largest new Christian reality since the Reformation").
  - Most scholars would accept the ranking, which is why this is MINOR. It still states as settled a size the map's own data treats with care. CLAUDE.md: "Never present a disputed claim as settled."
- Replacement (FK 8.5 / FRE 50, against 10.0 / 43 now; "growing edge" is the census's own phrase, "It was the growing edge of the century"):
  "Christianity's center of gravity moves south and east. The Pentecostal and charismatic family becomes the faith's growing edge. World War I (1914–18) breaks out early in this era."
  - The ranking can stay only if it names an independent count, as the census rule asks. That would add a claim, so it is Mark's call.

**4. Era 5 note: claims more than its source (Mark-approved)**
- Where: `WORLD_CONTEXT[5]`, line 111533.
- Current: "… Women's religious life grows to a scale not seen before. …"
- Why:
  - The pre-survey, the source of this note, says "women's religious life at unprecedented documented scale". "Documented" was a deliberate hedge: the same paragraph says "Sourcing turns abundant".
  - The map note dropped it when it was first written, so it now claims the scale itself was new. The census has no claim about this scale either way.
- Replacement (restores the source's hedge, adds nothing; FK 7.6 / FRE 59):
  "In the Latin West, new religious orders and new lay movements appear. Women's religious life is recorded on a scale not seen before. The Christian East comes under new pressures."

**5. Africa river note: "The rest" now hides two entries that sit outside the Alexandrian line**
- Where: `RIVER_LORE["Africa"].riverCoherence`, line 111584 (round 2's finding 5 wording).
- Current: "Most of its entries share one institutional line: the Church of Alexandria … That lane is unbroken and the map's longest. The rest are not continuous with it." Six groups are then named: Byzantine Carthage, Kongo's Antonians, Madagascar, Buganda, the African-initiated churches and the reverse-mission congregations.
- Why:
  - "The remaining six" matched the six names. "The rest" now reads as if those six are all of them.
  - Two more of the river's 28 entries sit outside the line, and their own entries say so. The Sudanese Church: "The ancient Christian kingdoms of Nubia stood on the same land, but no line runs from them to this story." The Melitians: "A rival church to the bishops of Alexandria from about 306. It broke with them."
  - "Most" is still true: 20 of 28.
- Replacement (adds nothing; the six names then read as examples): "Others are not continuous with it."
  - Naming the two would add census-backed claims. That belongs in the owner pass (P4).

**6. Decade dates before "c." now print "1880s-about 2010" (introduced by round 2's finding 13)**
- Where: `plainDates`, line 111732. It shows on seven traditions' spoken labels, tooltips, card date lines and river card lists.
- Current output:
  - "African-Initiated, 1880s-about 2010, Not yet available" (spoken label)
  - "Chinese Church — 1920s-about 2010" (river card list)
  - Also Catholic Renewal (1930s), Coptic Renaissance (1940s), Messianic Jews and Reverse Mission (1960s), and Hebrew Roots ("about 1990s-about 2010").
- Why:
  - Round 2 widened only the last rule to allow a decade's "s". The "-c." rule still needs a digit right before the hyphen, so "1880s-c. 2010" falls through to "1880s-about 2010".
  - These dates showed raw before, so the formatter's new reach exposed the gap.
- Replacement (line 111732): `.replace(/(\d(?:s|st|nd|rd|th)?)-c\.\s*/g,'$1 to about ')`
  - I ran it over all 1,053 distinct tradition, story and council date strings. Only these six strings change, to "1880s to about 2010" and "about 1990s to about 2010". "1906 to about 2010", "393 to about 458", "about 312–451" and "about 1990 to about 2010" are unchanged.

---

## New process item (not a text fix; it needs Mark's call before closure)

**P4. The river notes are stale against the current members, and far over the reading bar.**
- **Where:** `RIVER_LORE`, eleven rivers with five sections each. They are the longest participant-facing text on the map.
- **Root cause:** the notes were "researched by the Fable model against this exact set of member movements" (`Code-Notes_2026-11-06.md`, line 249). The member sets have grown since: Africa from 25 to 28, Caucasus 15 to 18, Latin West 76 to 97, Protestant & Evangelical 65 to 78, Non-Nicene 28 to 31. Round 2 dropped the counts, which treats a symptom. The staleness goes beyond counts:
  - the Caucasus gap (finding 2);
  - Africa's two unnamed entries (finding 5);
  - the two notes already hidden for the same reason (Greek and Latin; Latin and Protestant).
- **Reading level:** every note is well over the bar. Scored per river: FK 12.9 to 17.6, FRE 24 to 40, and 8 to 13 sentences over 25 words each. The longest sentence is 93 words (Africa). Africa has 11 em dashes and Latin West 15.
  - The four sentences round 2 edited kept their length: Africa 42 words, Latin West 43, Protestant & Evangelical 39.
  - Protestant & Evangelical also keeps the old noun ("the river's movements") on a card that now says "traditions" everywhere else, and an X-but-Y colon reveal ("is narrow but real:").
  - Other old tells: "does not pretend otherwise" (Latin West and Protestant & Evangelical), and the closers "a true theme, but not a lineage" (Africa) and "Rome is the river's pole, not its whole:" (Latin West).
- **Why it is a process item:** by this round's scale it would be BLOCKING. But a review round cannot fix it by patching sentences; that would be a fix on a fix. It needs one owner pass: re-check each note against the current members, then rewrite to the bar.
- **Options for Mark:**
  - (a) Run the owner pass before this release.
  - (b) Hide the notes until the pass is done, as already done for two rivers. The cards stay complete without them.
  - (c) Ship the notes as background research, with the gap logged.
  - Recommendation: (b). The notes fail on accuracy and on the bar, and the map works without them. Whatever he picks, the pass needs an Open-Gaps entry.

---

## Checked, no finding

- **The eight Mark-approved strings**, against the census and the map's data:
  - Era 1: "It ends in 312" matches the card's "70–312 CE". The Persian claim matches the census ("Constantine's conversion of Rome made its position worse") and the pre-survey.
  - Era 3: as in the status table.
  - Era 4: matches the merged Coptic entry.
  - Era 9: every claim is in the pre-survey's era 9 summary.
  - Era 10 close: nothing on the map ends after 2010. It reads well on the method page, which also uses "the map" and "traditions".
  - Key line: the bubble's count is the length of the Who list it opens.
- **New river card lines.** "Background research on the river as a whole. Each tradition below has its own sourced entry." (FK 6.0) is true: 334 of the 335 tradition cards on those rivers show sources. The 335th, Gallic Monasticism, is a built world whose fuller record loads separately, and it did not load in my private copy.
- **New labels.** "About The Early Church Era. Opens this era's card.", "1. The Early Church Era, 70–312 CE. Opens this era's card." and "You are in era 1, The Early Church Era, 70–312 CE. Opens this era's card." are intact. On a phone the era title still says "Zooms in to this era." Their status depends on P2.
- **Tablet ticks.** The changed `::after` rule still leaves the tick silent in Chromium. At 820 the accessibility tree reads "People [pressed]", "Stories [pressed]" and "Councils [pressed]".
- **AI tells in the strings added or changed since round 2.** The new card lines, labels, Key line, tooltips, era notes and closing note have no X-not-Y or X-and-never-Y pairs, no summary closers, no colon reveals, no em-dash asides and no stock phrases. Both old X-not-Y story labels are gone. Era 9's three pairs carry its content, as round 2 accepted. The old tells inside the river notes are in P4.
- **Reading level of the changed era notes:** FK 5.3 to 10.6, longest sentence 17 words. FRE is under 60 for eras 3, 4, 9 and 10, held down by content words (miaphysite, colonialism, Pentecostal), as rounds 1 and 2 accepted.

## Noticed, for the census owner or outside the brief

- Census names still carry "c." for "century" and hyphenated years ("Uniate 18th c.", "Kievan Rus' Christianity, 1054-1240"). Two short names also carry their own dates, so the map says them twice: "Jesuits 1650-1814, 1650–1814" (spoken label) and "Maronites 1815-1906 — 1815–1906" (river card list). These belong with P1's census entries.
- The census files "1904 Revivals" (1904–1910) under era 10, which starts in 1906. After finding 1's fix, its river card will say the river is found from Era 9. That matches the era 9 card, but era 9's tradition count will still leave this tradition out. This is the census owner's call.
- The method page's "What is still to come" still prints "(1906-c. 2010)". It was not changed this round.
- The Key still has no row for movements across churches; round 2 noted this.
- During the review, several stray untracked files appeared at the repo root, with names beginning `+       "note": …`. They were gone by the end. Worth a check that none were committed.
