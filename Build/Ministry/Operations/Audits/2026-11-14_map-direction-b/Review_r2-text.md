# Church Family Tree map, direction B: participant-facing text, round 2 (targeted recheck)

Reviewer: fresh round 2 reviewer, reading bar and fidelity together with the AI-tells check. No repo file edited. No model calls of any kind.

## What was checked, and how

- Branch `claude/cft-map-direction-b`. HEAD moved during the review from 5f087815 to **b2585784**. That commit only sets Thomas à Kempis `major: true`. Everything below is checked at b2585784. Line numbers are `cft-website/index.html` at b2585784.
- `review/r2.diff` leaves out the `"major"` lines and cuts long lines. I re-ran `git diff 8a54246d HEAD`. Nothing else differs.
- Runtime text was read in Chromium (Playwright) from a private copy of HEAD, at 1440x900, 820x1180 and 390x844 (touch). I read all ten era cards, all fifteen river cards and tooltips, the Key, the Connections panel, the Who list, the chips and the spoken labels and announcements. There were no page errors.
- Claims were checked against `cic-website/data/world-census.json` and the page's own `DATA` (eras, stories, councils, movements). Scores come from `engine/m1/fk.py`, given as FK (Flesch-Kincaid grade) / FRE (Flesch Reading Ease).
- Mark's picks were applied exactly as proposed on `mark-wording-picks.html`. I checked this by script: all ten notes, the five Key lines and the river names match.
- "Mark-approved" marks wording Mark approved, either in the picks or under A24/A27. Those findings need his ruling.

## Counts

- **Round 1, r1-text (31):** 24 resolved (one of them with its root cause deferred), 4 partly, 3 deferred to Open-Gaps.
- **Round 1, r1-tells (43):** 36 resolved, 4 partly, 3 open.
- **New findings: 15. 5 BLOCKING, 10 MINOR.**
  - BLOCKING: 1 and 2 are in Mark-approved era notes. 3 and 4 are on the river card, where round 1's fixes stopped short. 5 is old text outside this round's diff.
  - MINOR: 6, 7, 8, 9 and 11 are Mark-approved. 10 and 15 are approved under A27/A24. 12, 13 and 14 are not approved wording.
- **Process items: 3.** These are not text faults, but they stand in the way of closure.

---

## Round 1 status

### r1-text.md

| # | Subject | Status at b2585784 |
|---|---|---|
| 1 | Connections chip labels | **Resolved** (line 512). The chip is still hard-coded, not built from `LINK_FAMILY_LABEL`, so it can drift again. That is optional. |
| 2 | Key, "A connection" (A24) | **Resolved** (Mark's pick). True on every screen. |
| 3 | Key, "A dashed river" (A24) | **Resolved** (Mark's pick). Checked against `threadPath()`: a dash is drawn only where `cnt===0` between the river's first and last tradition. |
| 4 | "Eastern Catholic" | **Resolved in the map** (common name blank). The root cause, the Persecuted Church record filed at `laneOrder` 3.5, is **deferred to the census**. The picks page told Mark this is "logged in Open-Gaps". No entry exists; see process item P1. |
| 5 | "Reformed churches of India" | **Resolved** (Mark's pick). The river's two members are both "Northeast India … & the Mar Thoma …". |
| 6 | Era card count | **Resolved.** Era 10 reads "64 traditions on 13 rivers · 7 movements across churches". |
| 7 | Era title spoken label in the overview | **Resolved.** At 390x844: "1. The Early Church Era, 70–312 CE. Zooms in to this era." |
| 8 | River "1 movements · 312–312" | **Partly.** The tooltip and label are fixed ("1 tradition · 312–451"). The river card still ends every river at its last start year, and it now disagrees with the tooltip. See new finding 3. |
| 9 | "Open for conversation" | **Partly.** `statusLabel()` is fixed: tooltips and labels read "Conversations coming soon". The river card's "Its one movement is Built & Live.", which this finding also named, is unchanged. See new finding 4. |
| 10 | Era card stories heading | **Resolved.** |
| 11 | Council years twice | **Resolved for councils.** The same fault appears in the era card's story lists. See new finding 12. |
| 12 | Era card beyond A27; headings | **Partly.** The headings are fixed ("About this era", "Where the map stops"). The scope question is still open; see process item P2. |
| 13 | Era notes: reading bar and three data conflicts | **Resolved for what it named.** Era 1 is narrowed, era 2's Chalcedon slip is fixed, era 7 now says "Most" (35 of 36 era 7 traditions are living), and the 476 sentence is gone. All ten notes now score FK 7.0–10.7, and the longest sentence is 23 words. FRE is 37–68; eight notes are under 60, held down by names and content words. The data check found new conflicts, in new findings 1, 2 and 6. |
| 14 | People's dates read as lifespans | **Deferred** to the census owner. Not in Open-Gaps (P1). The Who list still shows "Hilary of Poitiers, about 300–367" and "Augustine of Hippo, 386–430". |
| 15 | Key, "A family of churches" (A24) | **Resolved** (Mark's pick). |
| 16 | Key, "Everyone on that river" (A24) | **Resolved** (Mark's pick). The new wording clashes with "named on the map". See new finding 11. |
| 17 | Key "Tap" on computers | **Resolved.** |
| 18 | Connections panel "movement" / "pick" | **Partly.** Both panel notes are fixed. The river card's "movement(s)" and "Movements in this river" are unchanged. Round 1 allowed "when next touched"; new finding 4 touches that card. |
| 19 | Connection counts | **Resolved** (singular, filtered counts, "Major 373"). |
| 20 | "▾" and "✓" read aloud | **Resolved.** The accessibility tree at 820 and 1440 reads "Rivers", "People [pressed]", "Connections". |
| 21 | "On the map ×" | **Resolved.** |
| 22 | "+N more" | **Resolved** ("Shows the full list."). |
| 23 | "to go in" | **Resolved** ("to zoom in"). See r1-tells 28. |
| 24 | Menu tagline lower case | **Resolved.** See r1-tells 27. |
| 25 | River name capitals and "other" | **Resolved** (Mark's pick). Checked against the members: Syriac East holds Syriac Orthodox, Maronites, St Thomas, Malankara and Sayfo; Africa's 28 are all African or African-diaspora churches. |
| 26 | Era dates "c." and hyphens | **Resolved.** The tag, strip, strip label, era card, Who subtitle and era-title label all use `plainDates()`. The same fault remains in tradition and story dates; see new finding 13. |
| 27 | Four census date lines | **Deferred** to the census owner. Not in Open-Gaps (P1). The tray still shows "Marius Mercator, Commonitorium 429". |
| 28 | "People to meet" | **Resolved** ("Major people"). |
| 29 | "Coming soon" twice | **Resolved.** The Donatism card shows it once. |
| 30 | Council cards and the Church and Empire river | **Deferred** to the census owner. Not in Open-Gaps (P1). |
| 31 | "Influenced / transmitted to" headings | **Resolved.** |

### r1-tells.md

| # | Subject | Status at b2585784 |
|---|---|---|
| 1–8 | Legend chip, era label, era count, era headings, "People to meet", kind announcement, "1 connections", "1 movements" | **Resolved.** For 7: "Connections: Medieval Ireland, 1. Clear it from the map." For 8: "1 tradition · 312–451". |
| 9 | Key phone route (A24) | **Resolved** (Mark's pick, r1-text's wording). |
| 10 | Era 1 note (A27) | **Resolved** as proposed. A new data point came up; see new finding 6. |
| 11 | Era 3 note | **Resolved** as proposed. Its "it" is now ambiguous; see new finding 7. |
| 12 | Era 5 note | **Resolved** as proposed. A claim conflicts with the map's data; see new finding 2. |
| 13 | Era 6 note | **Resolved.** |
| 14 | Era 9 note | **Partly.** "Honest theme" and the colon reveal are gone. The closing idea survives as "None of these pairs is resolved in this era."; see new finding 8. |
| 15 | Era 10 note | **Resolved.** "Spirit-movement" is still unexplained; see new finding 9. |
| 16–26 | Panel notes, river and connection announcements, "Names are showing", info-mark label, strip numbering, era dates, tray grip, tray close, "no single tradition" | **Resolved.** |
| 27 | Menu tagline "interactive map" | **Partly.** The capital is fixed. "An interactive map of Christian tradition…" (line 485) still differs from the phone hint, "A map of Christian tradition…". Replacement as in round 1. |
| 28 | Opening hint | **Partly.** "zoom in" is fixed. Only the era *title* zooms (the only caller of `goIntoEra` is the label), but the hint says "Tap an era". Replacement: `(coarsePointer?'Tap':'Click')+' an era title or a river to zoom in.'` (line 113848). |
| 29 | "74 people in all" | **Resolved.** The fix dropped the cue that the list is partial; see new finding 14. |
| 30–33 | Key lines (A24) | **Resolved** (Mark's picks). For 30, see new finding 11. |
| 34 | "&" against "and"; "creed" (A29) | **Partly.** "Nicene Creed" is fixed. "Protestant & Evangelical" and "Global Revival & Pentecostal" still sit beside "Syriac and Protestant". The Church and Empire river still holds the "Church & Empire" tradition. This was not on the picks page, so it is still Mark's call. |
| 35–38 | Eras 2, 4, 7, 8 (A27) | **Resolved** as proposed. Era 4's claim conflicts with the map's data; see new finding 1. |
| 39 | Era 10 closing note (A27) | **Open.** This note was not on the picks page; see new finding 10. |
| 40 | River card "movements" | **Open.** See new finding 4. |
| 41 | "Story — not its own movement" / "a story, not a movement" | **Open** (lines 112702, 113042). Replacement as in round 1. |
| 42, 43 | "Coming soon" twice; "Influenced" headings | **Resolved.** |

---

## Process items (not text faults; they block closure)

**P1. The deferrals are not in Open-Gaps.** The brief says r1-text 14, 27 and 30 are logged for the census owner. The picks page says the Greek and Latin record's placement is "logged in Open-Gaps". At b2585784, `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` has no such entries; its last entry is 264, era 6 Who batch 1. CLAUDE.md requires every known gap to be in Open-Gaps, "never left to live only in a conversation thread". Those four entries need writing before this closes.

**P2. The era card scope still has no change order.** A27 says: "Full era cards: NOT IN THIS RELEASE … ships the information mark, which opens the era notes the map already has." The card at HEAD also lists councils, new rivers, up to 12 major people, a people count, and two story lists (commit b5599cff). I found no change order for this in either Decision-Log. The picks page describes the card only as showing the era notes, so Mark may not have seen the lists. He needs to rule: name a change order, or revert to A27. New finding 15 depends on his ruling.

**P3. Proposed major calls are shown as settled.** Commit ab836b12 says "proposed major calls for the 38 first person entries, pending Mark's confirmation". The Family Tree Decision-Log says each major mark is "confirmed by Mark". These calls feed the era card's "Major people" list and its "N of them major" line, and which names show on the map (A8). If Mark has confirmed them, the confirmation should be logged.

---

## New findings

### BLOCKING

**1. Era 4 note tells a disputed claim as settled, and the map's own data disputes it (Mark-approved)**
- Where: `WORLD_CONTEXT[4]`, line 111531. It is the main text of the era 4 card.
- Current: "Christianity becomes a minority faith across its old heartlands as Islam rises. It converts new peoples in the north and fights an internal war over religious images. It sends its longest missions east along the Silk Road."
- Why:
  - The note puts the change to minority status inside 622–1054, as settled.
  - The era 4 entry "Coptic Christianity under Early Islam" (642–1013) says the Coptic church "began the long slide from being the country's uncontested majority toward the minority it is now — a shift historians place mostly later, and argue about still". Its long description says: "beginning the long, centuries-long drift toward minority status that conversions would eventually bring".
  - One documented story in that entry does put a turning point in 832. So the map's data is itself split, and the note should not settle the question.
  - CLAUDE.md: "Never present a disputed claim as settled." Round 1 raised this only in passing. The picks page told Mark "No claim changes."
- Replacement (narrows one claim, adds none; FK 8.2 / FRE 59, against 8.7 / 55 now):
  "As Islam rises, Christianity starts to become a minority faith across its old heartlands. It converts new peoples in the north and fights an internal war over religious images. It sends its longest missions east along the Silk Road."

**2. Era 5 note: "Byzantium consolidates" is contradicted by the map's own data (Mark-approved)**
- Where: `WORLD_CONTEXT[5]`, line 111532.
- Current: "In the Latin West, new religious orders and new lay movements appear. Women's religious life grows to a scale not seen before. Byzantium consolidates, and the Christian East comes under new pressures."
- Why:
  - Era 5's own key events include "Sack of Constantinople (1204)".
  - The era 5 entry "The Byzantine Church after the Schism" (1054–1300) says: "in 1204 it turned to disaster. A crusading army sacked Constantinople and set up a Latin patriarch. The church of the empire was driven out to Nicaea for nearly sixty years."
  - The same card lists that entry's story "Niketas Choniates Watches the Latins in Hagia Sophia", dated April 1204.
  - The picks page told Mark "No claim changes."
- Replacement (drops one claim, adds none; FK 6.9 / FRE 63):
  "In the Latin West, new religious orders and new lay movements appear. Women's religious life grows to a scale not seen before. The Christian East comes under new pressures."

**3. River card: each river's span still ends at its last start year, and now disagrees with the tooltip (r1-text 8, second place)**
- Where: `openPanelRiver`, lines 113077–113078. The tooltip is built at 112348 and in `tipForRiver` at 112698.
- Current: `const yearSpan=members.length===1?esc(members[0].dates):`${members[0].start}–${members[members.length-1].start}`;` then `${members.length} movement${members.length===1?'':'s'} · ${yearSpan}`.
  - What shows on the card: "Latin West / Catholic / 97 movements · 197–1962"; "Origin · 6 movements · 70–251"; "Latin and Protestant · 2 movements · 1906–1938"; "Protestant & Evangelical · 78 movements · 1517–1998".
  - The tooltips for the same rivers read "97 traditions · 197–2010", "6 traditions · 70–900" and "2 traditions · 1906–2010".
- Why:
  - The card's spans are wrong. Both Latin and Protestant traditions run to 2010, and the Catholic river does not end in 1962.
  - The same river now shows two spans and two nouns.
  - r1-text 8 named this fault, but the fix went only into the tooltip. The root cause is that two places compute the span. Fix it once, rather than patching the second copy.
- Replacement:
  - Add: `function riverSpan(members){return members.length===1?plainDates(members[0].dates):`${Math.min(...members.map(m=>m.start))}–${Math.max(...members.map(m=>m.end))}`;}`
  - Line 112348: `const riverTip=tipForRiver(f,members.length,riverSpan(members));`
  - Line 112698: `function tipForRiver(f,count,span){return `<div class="n">${esc(f.name)}</div><div class="m">${count} ${count===1?'tradition':'traditions'} · ${esc(span)}</div>`;}`
  - Lines 113077–113078: delete `const yearSpan=…` and write `h+=`<p class="meta">${members.length} ${members.length===1?'tradition':'traditions'} · ${esc(riverSpan(members))}</p>`;`
  - The card and tooltip then both read "97 traditions · 197–2010". Church and Empire reads "1 tradition · about 312–451".

**4. River card: "Built & Live" says the conversations are live (r1-text 9 and 18, r1-tells 40)**
- Where: `openPanelRiver`, lines 113086, 113104–113107 and 113111.
- Current:
  - "Its one movement is Built & Live." (Church and Empire)
  - `${built} of its ${n} movements ${built===1?'is':'are'} Built & Live.`
  - "None of its 10 movements are Built & Live yet."
  - "Spans Era 7 to Era 10 — 4 of the map's ten eras."
  - The heading "Movements in this river"
  - "Background research on the tradition as a whole, not one of the sourced per-movement entries below."
- Why:
  - "Built & Live" is the census's internal status name, and to a reader it means the conversations are live. Elsewhere the same screen says "Conversations coming soon" (in tooltips, since r1-text 9). The Key says "A tradition with a Representative: Conversations with its Representative are coming soon."
  - "Movement" is the old word for a tradition, and also the name of a different mark: the movements across churches.
  - The em-dash aside is the last dash left in the card's own sentences.
- Replacement:
  ```
  const spanText=eraNums.length===10?`Present in every one of the map's ten eras.`
    :eraMin===eraMax?`Confined to a single era (Era ${eraMin}).`
    :`Found in ${eraNums.length} of the map's ten eras, from Era ${eraMin} to Era ${eraMax}.`;
  const builtText=members.length===1?`Its one tradition ${built?'has':'does not yet have'} a Representative.`
    :built>0?`${built} of its ${members.length} traditions ${built===1?'has':'have'} a Representative.`
    :`None of its ${members.length} traditions has a Representative yet.`;
  ```
  - Heading: `<h3>Traditions in this river</h3>`
  - Note: `<i>Background research on the river as a whole. Each tradition below has its own sourced entry.</i>`

**5. River notes give counts the card above them contradicts (old text, outside this round's diff)**
- Where: `RIVER_LORE`, lines 111585 (Africa), 111592 (Latin West), 111595 and its `riverCoherence` (Latin/Prot. bridge), 111603 (Protestant & Evangelical) and 111623 (Non-Nicene). Shown under the river card's header.
- Current, against the map:
  - Africa: "Nineteen of its twenty-five entries share one institutional line" and "The remaining six are not continuous with it". The river holds 28.
  - Latin West: "Seventy-six entries across eighteen centuries share no single institution". The river holds 97.
  - Protestant & Evangelical: "What unites the river's sixty-five movements doctrinally". The river holds 78.
  - Non-Nicene: "Its twenty-eight entries fall into roughly six historical clusters." The river holds 31.
  - Latin and Protestant: "This lane holds one census record, not a tradition: the ecumenical communities of Iona (1938) and Taizé (1940)." and "It is a single documented case…". The river holds two traditions: Taizé & Iona, and the Philippine Independent Church (1906–2010), which the note never mentions.
- Why:
  - Each card prints the real count in its header, directly above the note. A reader then sees two numbers and cannot tell which is right.
  - The note was written against an earlier census. The build already hid the Greek and Latin note for the same reason ("neither river card shows lore until it is rewritten").
  - This is old text, but it sits on the card that findings 3 and 4 touch.
- Replacement (drops the counts, adds nothing):
  - Africa: "Most of its entries share one institutional line: …" and "The rest are not continuous with it."
  - Latin West: "Its entries, across eighteen centuries, share no single institution, and this river does not pretend otherwise: …"
  - Protestant & Evangelical: "What unites the river's movements doctrinally is narrow but real: …"
  - Non-Nicene: "Its entries fall into roughly six historical clusters." All 31 fall in the six clusters it lists.
  - Latin and Protestant: hide the note until its owner rewrites it to cover the IFI, as already done for Greek and Latin: `{k:5.5,lore:null, name:"Latin and Protestant", common:"", col:"#7d43a7"}`.

### MINOR

**6. Era 1 note: "runs to … 313" under a card dated 70–312, and the edict credited to Constantine alone (Mark-approved)**
- Where: `WORLD_CONTEXT[1]`, line 111528.
- Current: "This era starts where the map does, with the fall of the Jerusalem Temple in 70 CE. It runs to Constantine's Edict of Milan in 313, which gave Christians, and all others, freedom to follow the religion they chose. The Persian church east of Rome had the opposite experience. Persecution there grew worse after 312."
- Why:
  - The card's own date line reads "70–312 CE". The map's data ends era 1 in 312 and lists "Edict of Milan (313)" among era 2's key events. Round 1 noted this in passing, but it never reached Mark.
  - The picks page says the new clause uses "the words of the Constantine entry". That entry says "With Licinius he gave Christians, and all others, freedom to follow the religion they chose", and lists "Edict of Milan, with Licinius". The note drops Licinius.
- Replacement (drops the attribution, adds nothing; FK 5.3 / FRE 75):
  "This era starts where the map does, with the fall of the Jerusalem Temple in 70 CE. It ends in 312. In 313 the Edict of Milan gave Christians, and all others, freedom to follow the religion they chose. The Persian church east of Rome had the opposite experience. Persecution there grew worse after 312."
  - Naming "Constantine and Licinius" would follow the census, but it adds a claim, so that is Mark's call.

**7. Era 3 note: "it" now reads as "the Latin West" (Mark-approved)**
- Where: `WORLD_CONTEXT[3]`, line 111530.
- Current: "… The Latin West enters the post-Roman kingdoms. Monasticism becomes the force that shapes it everywhere."
- Why:
  - The nearest noun is "The Latin West", so "shapes it everywhere" narrows the claim to the West.
  - The era is "The Age of Monks and Empires". Its card lists the Judean Desert, the Syriac Orthodox, Ireland & Iona and the Benedictines. The old note's "everywhere" meant across the communions.
- Replacement (FK 10.3): "… The Latin West enters the post-Roman kingdoms. Monasticism becomes the force that shapes the churches everywhere."

**8. Era 9 note: the closing line survives in new words (Mark-approved; written in round 1)**
- Where: `WORLD_CONTEXT[9]`, line 111536.
- Current: "Christianity spreads around the world, both under empire and against it. Mission is tangled with colonialism, revival with respectability, and liberation with paternalism. None of these pairs is resolved in this era."
- Why:
  - The picks page told Mark the closing "held together rather than resolved" was dropped. Its idea is still the last line, as a step-back summary. That is the wise-saying cadence Mark ruled out.
  - The line is also hard to check: a pair cannot be "resolved".
  - Simply dropping it raises FK to 13.5, so the replacement also splits the sentences.
- Replacement (adds nothing; FK 10.2 / FRE 34, against 10.7 / 37 now; FRE stays low because of the content words, as round 1 accepted):
  "Christianity spreads around the world. It grows both under empire and against it. Mission is tangled with colonialism. Revival is tangled with respectability, and liberation with paternalism."

**9. Era 10 note: "Spirit-movement" is a term the map never explains (Mark-approved)**
- Where: `WORLD_CONTEXT[10]`, line 111537.
- Current: "… The Pentecostal and Spirit-movement family becomes the largest new form of Christianity since the Reformation. …"
- Why:
  - The term comes from the 2026 pre-survey (`Build/Ministry/Features/Atlas-World-Map/Design/CiC_World_Atlas_PreStep0_Survey_V0_1.md`, era 10). It appears nowhere in the census or anywhere else on the map. The river is "Global Revival & Pentecostal".
  - The bar asks for terms to be introduced before they are used.
  - The census's own name for this family is in the Global Pentecostal legacy: "Pentecostal and charismatic Christianity".
- Replacement (FK 10.0 / FRE 43): "Christianity's center of gravity moves south and east. The Pentecostal and charismatic family becomes the largest new form of Christianity since the Reformation. World War I (1914–18) breaks out early in this era."

**10. Era 10 closing note: "runs to 2010" against Mark's "about 2010" (approved under A27; never on the picks page)**
- Where: `ERA_CLOSE[10]`, line 111540, under the heading "Where the map stops".
- Current: "The tree's history runs to 2010. Movements since then will be added as they become history."
- Why:
  - Mark's 2026-11-08 ruling (Atlas Decision-Log, "era 10 becomes history"): "Era 10 is historical, 1906 to about 2010 … not a hard boundary". The card's own date line reads "1906 to about 2010".
  - The heading says "map" but the note says "tree".
  - "Movements" is the old word.
  - "As they become history" is a closing turn of phrase (r1-tells 39).
- Replacement (adds nothing; FK 5.0): "The map runs to about 2010. Traditions that began after that will be added once enough time has passed."

**11. Key, "People of a river": "the map names" clashes with "named on the map" (Mark-approved)**
- Where: `buildLegend` keyRows, line 113254.
- Current: "Everyone the map names on that river in that era, with the count."
- Why:
  - On this map, "named on the map" means a name shown on the map. Opening Latin West era 2 announces "Who list open: 26 people, 5 named on the map", and the list marks those 5 "On the map".
  - The Key says the count, 26, is everyone "the map names", which by that sense is 5.
- Replacement (FK 4.2): "The people the map lists for that river in that era, with the count."

**12. Era card: story years printed twice**
- Where: `openEraCard`, lines 113140 and 113141. This is new text since round 1.
- Current output:
  - "The Great Alleluia of 1233 1233"
  - "The Flagellants of 1260 1260"
  - "The Bianchi of 1399 1399"
  - "John the Almsgiver and the Refugees of 614 614"
  - In the cards list: "Nil Sorsky Stands Up at the Council of 1503 1503"
- Why: this is the fault r1-text 11 fixed for councils.
- Replacement:
  - Line 113140: replace `</button> <span class="meta">${esc(String(s.year))}</span></li>` with `</button>${String(s.title).includes(String(s.year))?'':` <span class="meta">${esc(String(s.year))}</span>`}</li>`
  - Line 113141: replace `${s.when?` <span class="meta">${esc(String(s.when))}</span>`:''}` with `${s.when&&!String(s.title).includes(String(s.when).trim())?` <span class="meta">${esc(plainDates(String(s.when)))}</span>`:''}`

**13. "c." is left in tradition and story dates, next to "about" for people and eras**
- Where: the node `aria-label` (112453), the movement-across `aria-label` (112596), `tipFor` (112677–112678), `tipForDocStory` (112705), the tradition card's date line (112942), the documented-story meta (112957), the story card's related list (113049), the river card list (113112) and the era card's story list (113141).
- Current examples:
  - A screen reader hears "Donatism, c. 311-439 CE, Conversations coming soon".
  - The era 1 card lists "Serapion Reads the Gospel of Peter Properly c. 200".
  - The river card lists "Church & Empire — c. 312-451".
  - 77 documented-story dates carry "c.".
- Why: C1 set "about" and en dashes for people. Round 1 extended them to eras. The map now mixes "about 300–367" and "c. 311-439" on one screen. The bar asks for no needless Latin.
- Replacement: wrap each of these in the shared formatter, for example `${plainDates(m.dates)}`, `${esc(plainDates(m.dates))}` and `${esc(plainDates(String(s.when)))}`. The output then reads "about 311–439 CE" and "about 200".
  - I ran `plainDates` over all 807 distinct tradition and story date strings. It turns every "c." into "about".
  - 14 decade forms keep their hyphen, for example "1530s-1650" and "c. 240s-430". Widen its last rule to `.replace(/(\d(?:s|st|nd|rd|th)?)-(?=\d)/g,'$1–')` to cover them. That gives "1530s–1650" and "about 240s–430". I tested this, and the existing outputs do not change ("1906 to about 2010", "5th–6th century", "393 to about 458").

**14. Era card: the "Major people" list shows 12 of N without saying so (introduced by round 1's fix)**
- Where: `openEraCard`, line 113136.
- Current: up to 12 names, then "The map has 74 people from this era, 36 of them major." (era 2; era 3 has 28 major people, era 1 has 14).
- Why: the old line said "And 24 more major people". The round 1 rewrite dropped that, so 24 of the 36 major people are now missing from the list without notice.
- Replacement: `${majors.length>12?` This list shows 12 of the major people.`:''}`, appended after the existing sentence. Era 2 then reads: "The map has 74 people from this era, 36 of them major. This list shows 12 of the major people."

**15. "Opens a note on this era" now opens a full card (A24/A25 wording; depends on P2)**
- Where:
  - The Key row "About an era: Opens a note on that era." (113257)
  - The era information mark label (112328)
  - The era-title label (113487)
  - The era strip label (113426)
- Why: if Mark keeps the larger era card (P2), "a note" undersells it. The card lists councils, rivers, people and stories, and the Key's tradition row already says "open its card".
- Replacement, only if the larger card stays:
  - "Opens that era's card." (Key)
  - "Opens this era's card." (the three labels)
  - If the card goes back to A27, leave all four as they are.

---

## Checked, no finding

- **Key lines (Mark's picks).**
  - "A connection" is true on every screen: the card button "Connections · N, Show on the map" is everywhere.
  - "A dashed river" matches `threadPath()`.
  - "A river" and the Tap/Click lines are correct.
  - The four reworded Key lines score FK 3.7–6.0.
- **River names (Mark's picks).** Each name was checked against its members:
  - "Church of the East and other Syriac churches": 22, all Syriac.
  - "Mar Thoma and churches of northeast India": 2.
  - "Coptic, Ethiopian and other African churches": 28.
  - "The church of the Roman Empire": 1.
  - "Outside the Nicene Creed": 31.
  - Greek and Latin is left blank, and no stray separator shows.
- **Era notes with no data conflict.**
  - Era 2: Chalcedon 451 now sits inside its own era and its own council list.
  - Era 6: Black Death 1347–51 matches the era's key event.
  - Era 7: "Most" is true; 14 of 15 era 7 Protestant & Evangelical traditions are living, and only Family of Love is not.
  - Era 8: no conflict.
  - Era 10: the World War I dates are right.
  - Era 1's new clause matches the census apart from Licinius (finding 6).
- **New spoken labels and announcements.** All of these read as intact sentences, with singulars handled:
  - "Who list closed.", "Connections cleared."
  - "All 15 rivers in full."
  - "Influenced: hidden. 3 of 4 kinds of connection showing."
  - "Connections: Medieval Ireland, 1. Clear it from the map."
  - "You are in era 1, The Early Church Era, 70–312 CE. Opens a note on this era."
  - "Tradition names are showing."
- **AI tells in this round's new strings.** I found no hedging filler, no assistant cadence, no em-dash asides, no colon reveals and no scare quotes. Era 2's 'imperial church' is a term attributed to historians, not a scare quote. The X-not-Y pairs that remain are old (r1-tells 41; the river card note in finding 4). The lists of three in eras 6, 8 and 9 carry the notes' content, and Mark kept them.
- **Era card headings and counts.**
  - "About this era", "Major councils", "Major people", "Stories" and "Where the map stops" are correct.
  - "Rivers that begin here" lists only rivers whose first tradition falls in that era.
  - Counts match the data.

## Noticed, outside the text brief

- The Key still has no row for the movements across churches. The era 10 card now counts them, as "7 movements across churches".
