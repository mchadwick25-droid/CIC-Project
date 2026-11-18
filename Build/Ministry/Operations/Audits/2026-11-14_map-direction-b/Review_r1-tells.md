# R1: AI-tells and voice review of the Church Family Tree map, direction B (release 44)

Reviewer: the AI-tells reviewer. I only read files. I edited no repo file and made no model calls of any kind.

**What I read.**
- The snapshot files `review/map-code.js` and `review/code.diff` (21:06 UTC).
- The full, unfiltered `git diff origin/main` for `cft-website/index.html` and `cic-website/assets/feedback.js`. The review diff leaves out lines that contain `"major"`, such as the Connections Off/Major/All row.
- The live working file `/home/user/CIC-Project/cft-website/index.html` as of 21:11:33 UTC.

The live file has moved on from the snapshot:
- `openEraCard` was rebuilt. It has new headings and lists, and it no longer shows the tag line or the academic name.
- More people are now marked major.

Findings quote the live file, and **all line numbers are in the live file**.

**Fixed since the snapshot (not numbered).** In the snapshot, era 7's card showed the tag line "The Western church remade - several ways at once", then the note "The Western church remade, several ways at once: …". The live card drops the tag line, so the repeat is gone.

## Status at HEAD `ecf2afb0` (committed 21:33 UTC, after I wrote the findings)
The build committed "Map: round 1 text-review fixes" while I was writing. I re-read that commit's changed lines, and the new strings in it are clean. Line numbers below are HEAD's.

- **Fixed in HEAD (12):** 1, 2, 3, 4, 5, 8, 17, 19, 23, 28, 42, 43. Two of my passing notes were fixed too: the "✓" in tablet switch names, and the "Major373" button names.
  - The new era card headings ("About this era", "Where the map stops", "Major people", "Stories") are fine.
  - So are the new count line ("64 traditions on 13 rivers · 7 movements across churches") and the new second Connections note.
- **Partly fixed (3):**
  - **7:** the plural is fixed, but a single connection still gets "Clear them". Line 113373 reads `${n} ${cn} of ${name} ${n===1?'is':'are'} showing. Clear them.` Replacement: `… showing. Clear ${n===1?'it':'them'}.` Now MINOR.
  - **16:** "two traditions" is fixed, but the note still ends "Hover or click a line to read the connection and its sources." (line 113238). Replacement: "Click or tap a line to read about the connection and its sources."
  - **27:** the menu tagline is now "An interactive map of Christian tradition, from the first house-churches to about 2010." (line 477). It still says "interactive", and it still differs from the phone hint. Replacement: "A map of Christian tradition, from the first house-churches to about 2010."
- **Still open in HEAD, with HEAD line numbers:**
  - 6 (113324)
  - 9 (113259)
  - 10 to 15: lines 111538, 111540, 111542, 111543, 111546, 111547
  - 18 (113312), 20 (113160), 21 (112328), 22 (113415), 24 (112152), 25 (500), 26 (112177), 29 (113137)
  - 30 (113255), 31 (113260), 32 (113250), 33 (113251, 113254), 34 (110870 to 110886)
  - 35 to 39: lines 111539, 111541, 111544, 111545, 111550
  - 40 (113079, 113106, 113112), 41 (112702, 113043)

**Severity.**
- BLOCKING means the text reads clearly as generated, or it misleads: it says something untrue, or it sends the reader to a control that is not there.
- MINOR means a slight tell, an awkward line, or wording that disagrees with the map's own words elsewhere.
- "Approved (A-number)" marks text Mark approved in `decisions.md`. I flag it as asked; whether to change it is his call.

**Overall.** The new UI strings are mostly clean. I found no hedging filler, no assistant cadence ("Let's", "Simply", "Here you can"), no em-dash asides, and no "X, not Y" or "X and never Y" pairs in them. The faults fall into four groups:
1. Labels that say something untrue.
2. Template strings that break when a count is 1 or a filter is on.
3. The old era notes, which are now the main text of a new card.
4. Word drift between the Key, the cards and the announcements, mainly "movements" against "traditions".

**Reading level.** I scored each replacement with the project's own `engine/m1/fk.py`, which is pure arithmetic. Each one scores better than the text it replaces. The scores are given as FK (Flesch-Kincaid grade) / FRE (Flesch Reading Ease). Era notes 3, 8, 9 and 10 stay under FRE 60, because they have to keep their content words (miaphysite, colonialism, paternalism and so on).

---

## BLOCKING

### 1. The connections legend chip gives the wrong names for two of the four kinds (misleads)
- **Where:** line 504, `#connChip .cc-key`.
- **Current:** `Grew out of` · `Influenced` · `Broke with` · `In contact`
- **Why:**
  - Everywhere else on the map, the four kinds are named by `LINK_FAMILY_LABEL` (line 111493): "Grew out of, continued as", "Influenced", "Argued against, broke with", "In contact with, member of". The chip cuts three of those names short.
  - On a phone this chip is the only legend, because the Connections panel is hidden (line 400). On a computer it contradicts the panel's own list.
  - The data has 174 "argued against" connections and 32 "broke with". So a reader would take most red lines to be breaks, when the record calls them arguments.
  - "Member of" lines would read as plain contact.
- **Replacement:** use the panel's four names, built in the script from `LINK_FAMILY_LABEL` so the two lists cannot drift apart again:
  `Grew out of, continued as` · `Influenced` · `Argued against, broke with` · `In contact with, member of`

### 2. In the zoomed-out overview, the era title's screen-reader label describes the wrong action (misleads)
- **Where:** line 112322 (`render`, the era label). The action is set at line 112324.
- **Current:** aria-label `${e.num}. ${e.title}, ${e.dates}. Opens a note on this era.`
- **Why:**
  - Below zoom 0.5 (`svg.simple`), a click or Enter calls `goIntoEra`, which zooms in. It does not open the note.
  - The label is set once at render and never updated. On a 1366×768 laptop the map even opens in this mode.
  - C6 requires names and states to stay accurate.
- **Replacement:** reset the label whenever `simple` changes in `labelFitRun`:
  - in the overview: `${e.num}. ${e.title}, ${e.dates}. Zooms in to this era.`
  - otherwise: `${e.num}. ${e.title}, ${e.dates}. Opens a note on this era.`

### 3. The era card counts movements across churches as traditions (misleads)
- **Where:** line 113128 (`openEraCard`). The count comes from `eraCounts`, line 110921.
- **Current:** `${esc(e.dates)} · ${eraCounts[i]} traditions on ${eraLaneCounts[i]} rivers`. Era 10 reads "71 traditions on 13 rivers".
- **Why:**
  - `eraCounts` counts every entry left in `DATA.movements`. That includes the 7 that the map itself labels "A movement across churches".
  - Era 10 has 64 traditions.
  - The old map tag used "movements" with this same count, which fitted; the new word does not.
- **Replacement:**
  - add `const eraTradCounts=eras.map(e=>churchBodies.filter(m=>m.era===e.num).length);`
  - then show `${esc(e.dates)} · ${eraTradCounts[i]} traditions on ${eraLaneCounts[i]} rivers`, so era 10 reads "64 traditions on 13 rivers".

### 4. The era card headings "How the era opens" and "How the era closes" do not match their text (live file only)
- **Where:** lines 113129 and 113141.
- **Current:** `<h3>How the era opens</h3>` above WORLD_CONTEXT, and `<h3>How the era closes</h3>` above ERA_CLOSE.
- **Why:**
  - Most notes sum up the whole era, not its start. Era 3 tells of Rome falling "partway through". Era 6 dates the Black Death to the middle of the era. Era 9 states the era's theme.
  - The only "closes" note (era 10) says where the Family Tree stops, not how the era ended.
  - The two headings are a matched pair for rhythm, which is a tell. Each one also tells the reader something untrue about the paragraph under it.
- **Replacement:**
  - `<h3>About this era</h3>` above the note. The Key ("About an era") and the info mark ("About …") already use this word.
  - ERA_CLOSE as a plain second paragraph under the same heading, with no heading of its own.

### 5. "People to meet" is stock copy, and on this page "meet" means having a conversation (live file only)
- **Where:** line 113133.
- **Current:** `<h3>People to meet</h3>`
- **Why:**
  - It is travel-guide wording, the kind of heading a generator reaches for.
  - On this page "Meet" is the word for talking with a Representative (`worldDoor`: "Meet {name} on Church in Conversation"). Above a list of historical people, it suggests you can talk with them.
  - The list holds the era's major people, and the heading above it is "Major councils".
- **Replacement:** `<h3>Major people</h3>`

### 6. The announcement for a kind of connection reads as a broken template
- **Where:** line 113320 (`buildLegend`, clicking a `[data-kind]` row).
- **Current:** `${label(b)} ${kindsOff.has(k)?'hidden':'shown'}. ${shown} of ${Object.keys(LINK_FAMILY_LABEL).length} kinds of connection showing.` This produces "Influenced hidden." and "Argued against, broke with hidden. 3 of 4 kinds of connection showing."
- **Why:**
  - The kind names are verb phrases, so adding a state word after them makes a sentence that does not parse.
  - The live site said "… links hidden", which at least read as a sentence. C6 requires the announcements to stay intact.
  - The same line uses both "shown" and "showing".
- **Replacement:** `${label(b)}: ${kindsOff.has(k)?'hidden':'showing'}. ${shown} of ${Object.keys(LINK_FAMILY_LABEL).length} kinds of connection showing.` This reads "Argued against, broke with: hidden. 3 of 4 kinds of connection showing." It matches the bar's own toast, "People: off".

### 7. "1 connections of X are showing"
- **Where:** lines 113369 and 113370 (`showConnections`).
- **Current:**
  - aria-label `${n} connections of ${name} are showing. Clear them.`
  - announcement `${n} connections of ${name} showing.`
- **Why:**
  - About 50 traditions have exactly one connection, so "1 connections … Clear them." will be common.
  - The label also breaks the pattern of the Who chip next to it: "Who: X. Clear the names from the map."
- **Replacement:**
  - aria-label `Connections: ${name}, ${n}. Clear ${n===1?'it':'them'} from the map.`
  - announcement `${n} ${n===1?'connection':'connections'} of ${name} showing.`

### 8. The new Church and Empire river shows "1 movements · 312–312"
- **Where:** line 112696 (`tipForRiver`) and line 112350 (the river's aria-label).
- **Current:** `${count} movements · ${minYear}–${maxYear}` and `${f.name} river, ${members.length} movements`
- **Why:**
  - This release gives Church and Empire a river of its own, holding one tradition. Its tooltip now reads "1 movements · 312–312" and its label reads "Church and Empire river, 1 movements".
  - "Across families" shows "1 movements · 1990–1990".
  - The river card already handles a river with one member.
  - "Movements" also disagrees with the new Key, which says a river "is wider where more traditions were active".
- **Replacement:**
  - tooltip `${count} ${count===1?'tradition':'traditions'} · ${minYear===maxYear?minYear:`${minYear}–${maxYear}`}`, which reads "1 tradition · 312"
  - aria-label `${f.name} river, ${members.length} ${members.length===1?'tradition':'traditions'}`

### 9. The Key sends phone users to a switch that is not there. Approved (A24)
- **Where:** line 113256 (`keyRows`, the row "A connection").
- **Current:** "A line between two traditions. Turn the lines on under Connections."
- **Why:**
  - On a phone the Connections group is hidden (line 400), and lines are forced off (`effectiveLinkMode`, line 113218).
  - The phone route is the card's "Connections · N, Show on the map" button (A22), which every screen has.
- **Replacement:** "A line between two traditions. Open a tradition's card to show its connections on the map."

### 10–15. Era notes with clear tells. Approved (A27: ship "the era notes the map already has")
These are old notes. This release takes them off the map and makes them the main text of the new era card.

Each replacement keeps every claim and adds none. Each also changes "band" to "era". "Band" was the word when the note sat in its horizontal band on the map; on a card titled "N. Era name" it points at nothing (Style Guide 1.10). Changing them touches A27, so it is Mark's call.

**10. Era 1** (line 111538)
- **Current:** "This band starts where the map does: the Jerusalem Temple falls in 70 CE, running to Constantine's Edict of Milan in 313 — the year the persecution these movements describe finally ends. For the Persian church east of Rome, that divide ran backwards: persecution only intensified after 312."
- **Why:**
  - It chains a colon reveal, an em-dash aside and a second colon reveal.
  - "Finally" and "ran backwards" are unearned emphasis.
  - The first sentence does not parse ("falls in 70 CE, running to …").
  - "These movements" is the old word for traditions.
  - Score now: FK 12.6 / FRE 44.
- **Replacement (FK 7.1 / FRE 65):** "This era starts where the map does, with the fall of the Jerusalem Temple in 70 CE. It runs to Constantine's Edict of Milan in 313, the year the persecution these traditions describe ends. The Persian church east of Rome had the opposite experience. Persecution there grew worse after 312."

**11. Era 3** (line 111540)
- **Current:** "The parting of the communions: Chalcedonian, miaphysite, and East Syriac Christianity become distinct, self-aware families here, while the Latin West enters the post-Roman kingdoms and monasticism becomes its formative engine everywhere. For scale: Rome itself falls to invasion in 476, partway through."
- **Why:**
  - It opens with a title and a colon reveal.
  - "Formative engine" is a stock metaphor.
  - "For scale:" is a formula repeated in eras 3, 6 and 10.
  - Score now: FK 15.0 / FRE 26.
- **Replacement (FK 9.6 / FRE 45):** "In this era the churches part into separate communions. Chalcedonian, miaphysite and East Syriac Christianity become distinct families, each with a sense of its own identity. The Latin West enters the post-Roman kingdoms. Monasticism becomes the force that shapes it everywhere. Rome itself falls to invasion in 476, partway through the era."

**12. Era 5** (line 111542)
- **Current:** "The Latin West's great creative explosion — new religious orders, new lay movements, and women's religious life at a scale not seen before — while Byzantium consolidates and the Christian East endures new pressures."
- **Why:**
  - It is a dash fragment with no main verb (Style Guide 1.3).
  - "Great creative explosion" is an unearned adjective (Style Guide 1.5).
  - There is a triad inside the dashes.
  - Score now: FK 18.3 / FRE 21.
- **Replacement (FK 8.9 / FRE 51):** "In the Latin West, new religious orders and new lay movements appear. Women's religious life grows to a scale not seen before. Byzantium consolidates, and the Christian East comes under new pressures."

**13. Era 6** (line 111543)
- **Current:** "Plague, papal schism, and institutional crisis, met by the most interior, vernacular, lay-accessible devotional writing Christianity had yet produced. For scale: the Black Death sweeps Europe (1347–51) during this band."
- **Why:**
  - It is a sentence fragment.
  - It stacks three adjectives in front of one noun.
  - It uses the "For scale:" formula.
  - Score now: FK 12.3 / FRE 34.
- **Replacement (FK 7.9 / FRE 61):** "Plague, papal schism and institutional crisis mark this era. They are met by devotional writing more inward than any before it, and more often in everyday languages for lay people to read. The Black Death sweeps Europe from 1347 to 1351."

**14. Era 9** (line 111546)
- **Current:** "Christianity globalizes under empire's shadow and against it. The era's honest theme is entanglement: mission and colonialism, revival and respectability, liberation and paternalism, held together rather than resolved."
- **Why:**
  - This is the strongest tell on the page.
  - "Honest theme" is unearned emphasis, followed by a colon reveal.
  - Three pairs are lined up for rhythm.
  - "Held together rather than resolved" is both an X-rather-than-Y pair and a wise saying placed as the closing line. Mark: "no xy no wise saying".
  - Score now: FK 17.7 / FRE −7.
- **Replacement (FK 10.7 / FRE 37):** "Christianity spreads around the world, both under empire and against it. Mission is tangled with colonialism, revival with respectability, and liberation with paternalism. None of these pairs is resolved in this era."

**15. Era 10** (line 111547)
- **Current:** "Christianity's center of gravity moves south and east, and the Pentecostal/Spirit-movement family becomes the largest new Christian reality since the Reformation. For scale: World War I (1914–18) breaks out early in this band."
- **Why:**
  - "Christian reality" is filler.
  - It uses the "For scale:" formula.
  - Score now: FK 11.9 / FRE 40.
- **Replacement (FK 9.8 / FRE 44):** "Christianity's center of gravity moves south and east. The Pentecostal and Spirit-movement family becomes the largest new form of Christianity since the Reformation. World War I (1914–18) breaks out early in this era."

---

## MINOR

### 16. Connections panel, first note: "movements", "Hover", "read the connection"
- **Where:** line 113235.
- **Current:** "… Where a connection joins two movements equally, the mark sits at both ends. Hover or click a line to read the connection and its sources."
- **Why:**
  - The note opens with "Lines join traditions", then switches to "movements" (word drift, Style Guide 1.9).
  - The panel also shows on tablets, where you cannot hover, and the Key says "Tap".
  - You read about a connection; you do not read "the connection".
  - The rest of the note is clean. It repeats "connection" on purpose, which keeps the term fixed.
- **Replacement:** "Lines join traditions where the sources record a connection. The color and the mark at the end show the kind of connection. The line's pattern shows how sure the record is. Where a connection has a direction, the mark sits at the end it points to. Where a connection joins two traditions equally, the mark sits at both ends. Click or tap a line to read about the connection and its sources."

### 17. Connections panel, second note: "movement", "Pick a movement"
- **Where:** line 113237.
- **Current:** "Major connections show one movement growing out of another, a recorded break, or an act of authority the sources record, such as a council condemning a group. Pick a movement to see all of its connections."
- **Why:**
  - It uses "movement" again.
  - "Pick" does not say how.
  - The first sentence runs to 27 words.
- **Replacement (FK 8.5 / FRE 58):** "Major connections show one tradition growing out of another, or a recorded break. They also show an act of authority the sources record, such as a council condemning a group. Open a tradition's card to see all of its connections."

### 18. "All rivers in full. 15 of 15 rivers in full."
- **Where:** line 113309.
- **Current:** `(on?'All rivers in full. ':'All rivers faint. ')+riverCount()`
- **Why:** when every river is on, it says the same thing twice and reads as a template.
- **Replacement:** on: `All ${laneButtons.length} rivers in full.` Off: `All rivers faint.`

### 19. The Connections mode announcement gives fixed totals, not what is showing
- **Where:** line 113315.
- **Current:** `${nMajor} major connections showing.` / `All ${nAll} connections showing.`
- **Why:** the numbers are fixed totals. With a kind switched off or a river faint, "All 722 connections showing" is untrue.
- **Replacement:**
  - count after `applyToggles()` with `const n=document.querySelectorAll('.edge-line:not(.is-off)').length;`
  - then announce `${n} major connections showing.` or `${n} connections showing.`
  - keep "Connections hidden." for Off.

### 20. "Names are showing." after going into an era
- **Where:** line 113157 (`goIntoEra`).
- **Current:** `${eras[i].title}. Names are showing.`
- **Why:**
  - Everywhere else on this map, "the names" means people's names ("Clear the names from the map", "5 named on the map").
  - Here it means tradition names. People's names do not appear until zoom 2.2.
- **Replacement:** `${eras[i].title}. Tradition names are showing.`

### 21. The era info mark's label breaks with a colon
- **Where:** line 112328.
- **Current:** `About ${e.title}: opens a note on this era.`
- **Why:** every other new label ends with a full stop and then "Opens …", as in "… Opens their card." and "… Opens a note on this era."
- **Replacement:** `About ${e.title}. Opens a note on this era.`

### 22. The era strip numbers the era differently
- **Where:** line 113411.
- **Current:** `${e.num} · ${e.title}`, shown as "3 · The Age of Monks and Empires".
- **Why:** the era title on the map and the era card both read "3. The Age of Monks and Empires".
- **Replacement:** `${e.num}. ${e.title}`

### 23. Era dates still show raw, next to the fixed person dates
- **Where:**
  - the era tag on the map (`tag.textContent=e.dates`)
  - the era strip (line 113412)
  - the era card's count line (line 113128)
  - the Who tray subtitle (line 112166)
  - the era aria-labels
- **Current:** for example "70-312 CE" and "1906-c. 2010". In the tray: "26 people · 451-622".
- **Why:**
  - C1 fixed the root cause for people's dates, which now read "about" and use en dashes.
  - Era dates in the same panels still show "c." and hyphens.
  - A screen reader may read "1906 minus c. 2010".
- **Replacement:** move the `personDates` rules into one shared formatter and run `e.dates` through it. That gives "70–312 CE", "451–622" and "1906 to about 2010".

### 24. The tray grip says "Open the list" when the list is already open
- **Where:** line 112152.
- **Current:** `low?'Open the list':'Make the list smaller'`
- **Why:** the list is open in both states, and the two labels do not form a pair.
- **Replacement:** `low?'Make the list bigger':'Make the list smaller'`

### 25. The tray's close label does not match the Who chip
- **Where:** line 500.
- **Current:** `Close the Who list and clear the names`
- **Why:**
  - The Who chip says "Clear the names from the map."
  - "The names" on its own is unclear.
- **Replacement:** `Close the Who list and clear the names from the map`

### 26. "Told within no tradition" against the card's "Told within no single tradition"
- **Where:** line 112177 (the tray's "By tradition" view).
- **Current:** `Told within no tradition · ${loose.length}`
- **Why:** the person card's Tradition line (line 112244) says "Told within no single tradition". That is two wordings for one fact.
- **Replacement:** `Told within no single tradition · ${loose.length}`

### 27. The site menu tagline uses the stock phrase "interactive map" and starts in lower case
- **Where:** line 477 (`#siteMenu .tag`). The header tag on line 474 has the same older wording.
- **Current:** "an interactive map of Christian tradition, from the first house-churches to about 2010"
- **Why:**
  - "Interactive map" is stock product copy.
  - In the menu it stands alone as a paragraph, but starts in lower case.
  - The phone's new opening hint already puts it plainly: "A map of Christian tradition, from the first house-churches to about 2010." A phone user sees both versions.
- **Replacement:**
  - menu: "A map of Christian tradition, from the first house-churches to about 2010."
  - header, if it is to match: "a map of Christian tradition, from the first house-churches to about 2010"

### 28. The opening hint says "to go in"
- **Where:** line 113813.
- **Current:** `(coarsePointer?'Tap':'Click')+' an era or a river to go in.'`
- **Why:**
  - "Go in" is vague. The action is a zoom to reading size (A18).
  - The thing to tap is the era's title, not the era.
- **Replacement:** `(coarsePointer?'Tap':'Click')+' an era title or a river to zoom in.'`

### 29. The era card's people line ends "74 people in all" (live file only)
- **Where:** line 113134.
- **Current:** `${majors.length>12?`And ${majors.length-12} more major people. `:''}${people.length} ${people.length===1?'person':'people'} in all.`
- **Why:**
  - The line opens with "And".
  - "In all" reads as if the era had only that many people. It is the number of people from that era who have cards on the map.
- **Replacement:** `The map has ${people.length} ${people.length===1?'person':'people'} from this era${majors.length<people.length?`, ${majors.length} of them major`:''}.` This reads "The map has 74 people from this era, 36 of them major."

### 30. Key, "People of a river": "Everyone". Approved (A24)
- **Where:** line 113252.
- **Current:** "Everyone on that river in that era, with the count."
- **Why:**
  - "Everyone" is an absolute (Style Guide 1.6). The mark covers the people the map has cards for, not everyone.
  - A single person shows no number (A3).
- **Replacement:** "The people of that river in one era. The number says how many."

### 31. Key, "A dashed river": "nothing on record". Approved (A24)
- **Where:** line 113257.
- **Current:** "Years with nothing on record."
- **Why:**
  - The dashes mean that none of that river's traditions was active in those years. They do not mean nothing at all is recorded.
  - The live site said "none on record".
- **Replacement:** "Years with none of its traditions on record."

### 32. Key, "A river": "A family of churches". Approved (A24)
- **Where:** line 113247.
- **Current:** "A family of churches. It is wider where more traditions were active."
- **Why:**
  - The map's own river notes say several rivers are not families: "This is a seam, not a tradition"; "This is not a tradition-family river"; "a thematic, doctrinal-position category, not a genealogical tradition".
  - One river is even named "Across families".
- **Replacement:** "A group of traditions. It is wider where more of them were active."

### 33. The Key says "Tap" on a computer. Approved (A24)
- **Where:** lines 113248 and 113251.
- **Current:** "Tap its name to open its card." and "Tap to see who they were."
- **Why:** the opening hint already switches between Tap and Click depending on the pointer, and the Connections note says "click".
- **Replacement:**
  - `${coarsePointer?'Tap':'Click'} its name to open its card.`
  - `${coarsePointer?'Tap':'Click'} to see who they were.`
  - `coarsePointer` is declared at line 113703, before `buildLegend()` runs at line 113807.

### 34. River names: "&" against "and", "creed", and Church and Empire against Church & Empire. Approved (A29)
- **Where:** `FAM`, lines 110870 to 110886.
- **Current:**
  - "Syriac and Protestant", "Church and Empire", "Greek and Latin", "Africa and Latin" and "Latin and Protestant" sit beside "Protestant & Evangelical" and "Global Revival & Pentecostal".
  - "Outside the Nicene creed".
- **Why:**
  - One list uses two spellings of "and".
  - The Church and Empire river holds a single tradition whose map name is "Church & Empire". So the river and its tradition differ only by "and" against "&".
  - The river notes write "Nicene Creed".
- **Replacement (Mark's call):** one spelling throughout. For example "Protestant and Evangelical" and "Global Revival and Pentecostal" with the tradition renamed "Church and Empire", or "&" everywhere. And "Outside the Nicene Creed".

### 35–39. Era notes with lighter tells. Approved (A27)
**35. Era 2** (line 111539)
- **Why:** a dash fragment, and one 43-word sentence (FK 20.7 / FRE 21).
- **Replacement (FK 8.5 / FRE 55):** "Historians call this era the 'imperial church'. Christianity moves from a persecuted minority to the empire's own religion. The creeds that define it are settled at Nicaea and then, just after this era, at Chalcedon. They are settled because an emperor now has a stake in the outcome."

**36. Era 4** (line 111541)
- **Why:** one 35-word sentence (FK 18.3 / FRE 26).
- **Replacement (FK 9.0 / FRE 53):** "Under the rise of Islam, Christianity becomes a minority faith across its old heartlands. It converts new northern peoples and fights an internal war over religious images. It sends its longest missions east along the Silk Road."

**37. Era 7** (line 111544)
- **Current:** "The Western church remade, several ways at once: this band holds the Reformation's many, often-rival movements side by side, each with its own direct descendants still living today."
- **Why:** a colon reveal, and "band".
- **Replacement (FK 6.4 / FRE 63):** "This era holds the Reformation's many movements side by side. Often they were rivals. Each has its own direct descendants still living today."

**38. Era 8** (line 111545)
- **Why:** a semicolon chain, and FRE 14.
- **Replacement (FK 10.8 / FRE 40):** "The established churches settle into place. Renewal moves into small groups, personal religious experience and revival on both sides of the Atlantic. In this era, people's own stories of their spiritual lives become a popular kind of writing."

**39. Era 10 closing note** (line 111550)
- **Current:** "The tree's history runs to 2010. Movements since then will be added as they become history."
- **Why:**
  - "As they become history" is a closing turn of phrase.
  - Elsewhere the site says "about 2010".
- **Replacement:** "The Family Tree runs to about 2010. Movements after that will be added once enough time has passed."

---

## MINOR: older lines that now disagree with the new text

### 40. The river card still says "movements"
- **Where:** `openPanelRiver`, lines 113077 and 113104 to 113110.
- **Current:**
  - "1 movement · …"
  - "Its one movement is Built & Live."
  - "None of its N movements are Built & Live yet."
  - "Movements in this river" (heading)
- **Why:** the new Key and the era card call these traditions, and this release edited the same card's title lines.
- **Replacement:**
  - change "movement" and "movements" to "tradition" and "traditions" in each line
  - heading: "Traditions in this river"

### 41. The story tooltip and story card say "not its own movement" and "a story, not a movement"
- **Where:** line 112699 (`tipForStory`) and line 113041 (`openPanelStory`).
- **Current:** "Story — not its own movement" and `${esc(s.confidence)} · a story, not a movement`
- **Why:**
  - Both are X-not-Y pairs, one with an em dash, and both use the old word "movement".
  - The contrast did carry real information, but the new Key row now carries it: "A story: Something that happened, told from the sources."
- **Replacement:** "A story" and `${esc(s.confidence)} · a story`

### 42. Built-world cards show the "coming soon" line twice
- **Where:** line 112938 (after the Representative line) and line 113000 (after "Where this tradition stands").
- **Current:** "Conversations with {name} are coming soon to Church in Conversation." appears twice on each of the 11 built-world cards, because all of them have `entry`, `why` and `publicOpen`.
- **Why:** A28 wants the line on tradition cards. Saying it twice makes the card read as stitched together.
- **Replacement:** drop the second `h+=worldDoor(m);` (line 113000).

### 43. The tradition card files every connection under "Influenced"
- **Where:** lines 112971 and 112972 (`openPanel`).
- **Current:** "Influenced / transmitted to" and "Influenced by" (headings).
- **Why:**
  - These lists hold every kind, including "argued against" and "broke with". So a break gets filed under "Influenced by".
  - The same card now has a "Connections · N" button.
  - C4 asks for "connection" throughout.
- **Replacement:** "Connections from this tradition" and "Connections to this tradition" (headings).

---

## Noticed in passing (not tells; for the coordinator)
- **Scope.**
  - The live era card (21:11) adds lists of councils, rivers, people and stories.
  - A27 says "Full era cards: NOT IN THIS RELEASE", and that the release ships "the era notes the map already has".
  - Worth confirming that this change was agreed.
- **Rigor, not wording:**
  - Era 1's card gives the dates as "70-312 CE", but its note says the era "runs to … 313".
  - Era 4 says Christianity "becomes a minority faith across its old heartlands" between 622 and 1054. That is a contested reading of when people converted, told as settled.
  - "Syriac and Protestant · Reformed churches of India" (A29): "Reformed" with a capital R names the Calvinist family. It fits the Presbyterian churches of Northeast India, but the Mar Thoma half of the river is a reformed Syriac church in communion with the Anglicans, not a Reformed one. Worth a check.
- **Data, not code:** after the C1 fix, some person dates still read oddly because of the source data: "about 368–408 to 420", "about 370–380 to after 443".
- **Accessibility:**
  - On tablets, the "✓" added by `.sw-name::after` becomes part of each switch's accessible name in Chrome and Firefox ("People check mark"), on top of aria-pressed.
  - `Major<span>373</span>` gives the button the accessible name "Major373". A space before the span fixes it.
- **Gap in the Key:** the Key has no row for movements across churches, which still show (three of them always, A21). Their column caption labels them.

---

## Counts
- **Still open at HEAD `ecf2afb0`:** 31 of the 43.
  - **BLOCKING, 8:** finding 6, which is not approved, plus 9 and 10 to 15, which are approved.
  - **MINOR, 23:** 11 not approved (7, 16, 18, 20, 21, 22, 24, 25, 26, 27, 29); 10 approved (30 to 39); 2 in older lines (40, 41).
  - The other 12 are fixed in HEAD.

**As first written, against the 21:11 file:**
- **Total:** 43 findings.
- **BLOCKING: 15.**
  - Not approved (8): 1 to 8.
  - Approved (7): 9 (A24); 10 to 15 (A27).
- **MINOR: 28.**
  - New or rewritten text (14): 16 to 29.
  - Approved (10): 30 to 33 (A24); 34 (A29); 35 to 39 (A27).
  - Older lines that disagree with the new text (4): 40 to 43.
