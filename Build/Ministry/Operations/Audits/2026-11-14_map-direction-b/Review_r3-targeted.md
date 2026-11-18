# Church Family Tree map, direction B: targeted check of round 3's six text fixes

Reviewer: fresh Opus reviewer, one targeted check under Mark's standing ruling for minor round 3 fixes. Only the six strings were checked. No repo file was edited. No model calls of any kind.

## Result

**All six fixes PASS. No new findings.**

| Fix | Round 3 finding | Applied exactly | Does what was asked | New fault |
|---|---|---|---|---|
| 1 | River card era line (`openPanelRiver`) | Yes | Yes | None |
| 2 | Caucasus river note | Yes | Yes | None |
| 3 | Era 10 note, scale claim | Yes | Yes | None |
| 4 | Era 5 note, hedge restored | Yes | Yes | None (FRE 58.5, see below) |
| 5 | Africa river note, "The rest" | Yes | Yes | None |
| 6 | `plainDates`, decade before "c." | Yes | Yes | None |

## What was checked, and how

- Branch `claude/cft-map-direction-b`, HEAD **fce4306b**, parent 56c1bb2a. The commit changes only `cft-website/index.html` (8 lines in, 6 out). Line numbers below are at HEAD.
- **Exact match.** A script compared each changed string, byte for byte, with the proposal in `r3-text.md`, including the en dashes (U+2013) and the straight apostrophes. All six match. None of the old strings is left in the page. The only other copy of the old wording is the design prototype `Build/Ministry/Features/Atlas-World-Map/Design/river-prototype.html`, which is not served. No test pins any of these strings.
- **No stale narration.** `WORLD_CONTEXT` and `RIVER_LORE` each have one use: the era card and the river card. Tree narration is matched by a hash of each movement's `longDescription`, and there is no audio for era or river notes.
- **Browser.** I built the site with `node tools/build_tree_site.mjs` (1559 own files, 173 shared, 0 mismatched). Then I served `.build/tree` on two local ports: one as built (HEAD), and one with the parent commit's `index.html` swapped in. Chromium (Playwright) ran at 1440x900. Neither page had any errors.
- Claims were checked against `cic-website/data/world-census.json`, the page's own `DATA`, and for fix 4 the pre-survey (`Build/Ministry/Features/Atlas-World-Map/Design/CiC_World_Atlas_PreStep0_Survey_V0_1.md`). Scores come from `engine/m1/fk.py`, given as FK / FRE.

## Fix 1. River card era line (lines 121376-121379): PASS

- The code matches round 3's replacement. The `eraMin`/`eraMax` line was already there and is unchanged.
- I opened all 15 river cards with `openPanelRiver(f, members)` via `page.evaluate`, with the same arguments the river's click handler builds. I also opened each one by clicking its river group. The two paths gave the same text on all 15.
- The "What sets this river apart" line at HEAD. Only the first sentence changed, on exactly the four rivers round 3 predicted. The Representative and connections sentences are unchanged on all 15.

| River | Header | First sentence at HEAD | Before |
|---|---|---|---|
| Origin | 6 traditions · 70–900 | Found in 4 of the map's ten eras, from Era 1 to Era 4. | Confined to a single era (Era 1). |
| Syriac East | 22 · 200–2010 | Present in every one of the map's ten eras. | same |
| Syriac and Protestant | 2 · 1836–2010 | Found in 2 of the map's ten eras, from Era 9 to Era 10. | same |
| Caucasus | 18 · 314–2010 | Found in 9 of the map's ten eras, from Era 2 to Era 10. | same |
| Greek East | 42 · 185–2010 | Present in every one of the map's ten eras. | same |
| Church and Empire | 1 · about 312–451 | Confined to a single era (Era 2). | same |
| Greek and Latin | 10 · 1596–2010 | Found in 4 of the map's ten eras, from Era 7 to Era 10. | same |
| Africa | 28 · 150–2010 | Present in every one of the map's ten eras. | same |
| Africa and Latin | 2 · 1650–2010 | Found in 3 of the map's ten eras, from Era 8 to Era 10. | Found in 2 of the map's ten eras, from Era 8 to Era 10. |
| Latin West | 97 · 197–2010 | Present in every one of the map's ten eras. | same |
| Latin and Protestant | 2 · 1906–2010 | Confined to a single era (Era 10). | same |
| Protestant & Evangelical | 78 · 1517–2010 | Found in 4 of the map's ten eras, from Era 7 to Era 10. | same |
| Global Revival & Pentecostal | 10 · 1904–2010 | Found in 2 of the map's ten eras, from Era 9 to Era 10. | Confined to a single era (Era 10). |
| Across families | 1 · about 1990 to about 2010 | Confined to a single era (Era 10). | same |
| Non-Nicene | 31 · 120–2010 | Present in every one of the map's ten eras. | Found in 9 of the map's ten eras, from Era 1 to Era 10. |

- **The map's own data backs each newly counted era**, and each one falls inside the span in the header on the same card:
  - Origin, era 2: Ebionites, Christian Apocrypha, Montanism and Novatianism. Eras 3 and 4: Christian Apocrypha (c. 100-900) alone.
  - Africa and Latin, era 9: Kongo after 1650 (1650-1881).
  - Global Revival & Pentecostal, era 9: 1904 Revivals (1904-1910). The era 9 card lists this river under "Rivers that begin here", so the two cards now agree.
  - Non-Nicene, era 6: the Cathars (c. 1143-1321).
- Church and Empire stays "Confined to a single era (Era 2)", as round 3 intended with `m.end-1`. No tradition on any river lacks a numeric start or end, and none ends before it starts.
- The wording did not change, so there is no new tell. The four changed lines score FK 7.2 to 8.5, FRE 55 to 63.

## Fix 2. Caucasus river note (line 119863): PASS

- Rendered: "The Armenian spine supplies most of its entries. For centuries it flows outside the Caucasus altogether. The Georgian spine has long gaps: 609–780, 1245–1650 and 1811–1917."
- "Most": 11 of the 18 traditions are Armenian and 5 are Georgian. Caucasian Albania and the Paulicians make up the other 2.
- **The three gaps fall exactly between the five Georgian entries.** These are Georgia (c. 330-609), Georgian Revival (c. 780-1000), Georgian Golden Age (c. 1000-1245), Georgian Church 1650 (1650-1811) and Georgian Orthodoxy (1917-c. 2010).
- The census supports the gaps:
  - Golden Age: "No entry covers the church from 1245 to 1650."
  - Georgian Orthodoxy: "whether the Caucasus lane resumes at all after 1811".
  - Georgian Church 1650: "The window runs from 1650 to 1811."
- No Georgian church entry on any other river covers these years. The name matches elsewhere are Visigothic Iberia, Gothic Homoians, the Military Orders and "Georgian C of E".
- Reading: FK 5.9 / FRE 67, in sentences of 8, 8 and 10 words. The old sentence scored FK 13.9 / FRE 36 at 25 words. The colon introduces a list, not a reveal. No tell.
- Two small reading points are noted below for the river-note owner pass (P4). Neither is a fault in context.

## Fix 3. Era 10 note (line 119831): PASS

- Rendered: "Christianity's center of gravity moves south and east. The Pentecostal and charismatic family becomes the faith's growing edge. World War I (1914–18) breaks out early in this era."
- The size ranking is gone. The new sentence makes a claim about direction, which the census entry `global-south-pentecostal-christianity` states as settled:
  - "It was the growing edge of the century."
  - "What is not in doubt is the direction of travel."
- It makes no scale claim, so the census rule does not apply: "Scale claims about this family are self-report or definitional aggregate unless an independent count is named." "Growing edge" is the census's own phrase, used in three of its fields, so it is the map's voice, not a stock phrase.
- Reading: FK 8.5 / FRE 50, up from 10.0 / 43. The longest sentence is now 10 words, down from 15. The FRE under 60 comes from content words (Pentecostal, charismatic, Christianity's), as rounds 1 to 3 accepted for eras 3, 4, 9 and 10.

## Fix 4. Era 5 note (line 119826): PASS

- Rendered: "In the Latin West, new religious orders and new lay movements appear. Women's religious life is recorded on a scale not seen before. The Christian East comes under new pressures."
- The pre-survey reads "women's religious life at unprecedented documented scale". "Recorded" restores that hedge and adds nothing.
- **Reading: FK 7.6 / FRE 58.5, from 6.9 / 62.8.** That is just under the FRE 60 line. The cause is the hedge word itself, not the sentence's shape:
  - "Women's religious life leaves records on a scale not seen before." also scores 58.5.
  - "The sources record women's religious life on a scale not seen before." scores 59.9, but it adds an agent the source does not name.
  - Fidelity outranks a point and a half of FRE. This is the same content-word reason the earlier rounds accepted.
- The passive has no agent, and that is right here. It keeps the subject in front, and naming who recorded it would add a claim. No tell.

## Fix 5. Africa river note (line 119877): PASS

- Rendered: "... That lane is unbroken and the map's longest. Others are not continuous with it. Byzantine Carthage was ..."
- The river has 28 entries. 20 sit on the Alexandrian line and 8 sit outside it: the six groups the note names, plus the Melitians and the Sudanese Church. With "Others", the named groups read as examples, not the full list.
- It adds no claim. "It" clearly refers back to "That lane". FK 4.5 / FRE 74.

## Fix 6. `plainDates` (line 120025): PASS

- The rule matches round 3's replacement.
- **Census run.** In Node, I lifted each version's `plainDates` from its own commit. I ran both over every distinct date string in the census: 1,054 strings.
  - These are `movements[].dates` (350 traditions, 250 people, 12 councils, 7 movements across churches), `documentedStories[].when` and `eras[].dates`.
  - The census has no stories array.
- **Page run.** In Chromium, I ran each page's own function over the page's DATA: 1,112 strings. These add the 61 distinct map-story years from `DATA.stories`. The page prints those years with `String()`, not through `plainDates`, and none of them changes.
- **Every output that changed, in both runs (6 strings, 7 traditions):**

| Census string | Before | After | Tradition(s) |
|---|---|---|---|
| 1880s-c. 2010 | 1880s-about 2010 | 1880s to about 2010 | African-Initiated |
| 1920s-c. 2010 | 1920s-about 2010 | 1920s to about 2010 | Chinese Church |
| 1930s-c. 2010 | 1930s-about 2010 | 1930s to about 2010 | Catholic Renewal |
| 1940s-c. 2010 | 1940s-about 2010 | 1940s to about 2010 | Coptic Renaissance |
| 1960s-c. 2010 | 1960s-about 2010 | 1960s to about 2010 | Messianic Jews, Reverse Mission |
| c. 1990s-c. 2010 | about 1990s-about 2010 | about 1990s to about 2010 | Hebrew Roots |

- Nothing else changed. Era 10's "1906 to about 2010" and every other `-c.` date read as before.
- In the browser, the new form shows on all seven traditions' spoken labels, tooltips, card date lines and river-card lists. Examples: "African-Initiated, 1880s to about 2010, Not yet available" and "Chinese Church — 1920s to about 2010".
- No census string has an ordinal before "-c.", so the rule's st/nd/rd/th branch changes nothing in today's data.

## Noticed: not caused by these fixes, outside the brief

1. **Braulio of Zaragoza** (a person, era 4, added with the era 4 people after round 3 read the map). His census date "bishop c. twenty years; at councils 633-638" prints as "bishop c. twenty years; at councils 633–638" on his label, tooltip and card. No rule covers a "c." before a word. This is for the census owner, with P1.
2. **Hebrew Roots.** "about 1990s" lacks "the". The cause is the census string, which puts "c." on a decade ("c. 1990s-c. 2010"). For the census owner.
3. **The Family Tree's own tradition pages** print census dates raw, outside `plainDates`. Example, from `cft-website/tree/african-initiated-churches-harrist-aladura-zioni.html`: "The Global Church Era · 1880s-c. 2010 · W. & S. Africa, Congo". Round 3's finding 6 covered only the map.
4. **Round 3's item on 1904 Revivals still stands.** The river card and era 9's "Rivers that begin here" now place Global Revival & Pentecostal in era 9. But era 9's header, "62 traditions on 9 rivers", still leaves it out, because the census files 1904 Revivals under era 10. This is the census owner's call.
5. **For the P4 owner pass, in the Caucasus note:**
   - With "disclosed" gone, "The Georgian spine has long gaps" no longer says the gaps are in the map, not in the church's life.
   - "it" in "For centuries it flows" follows "most of its entries", where "its" is the river.
   - Both read correctly in context, so neither is a finding. Any rewording should name this river: "Georgian C of E" (1660-1815, on the Protestant river) would make a map-wide "no Georgian entry" claim false. The one river-scoped wording I tried also scored worse (FK 7.2 / FRE 58).

## Working files (scratch, not in the repo)

- `/tmp/claude-0/-home-user-CIC-Project/dea08a2e-974b-5238-b6f9-cce88a691a2b/scratchpad/r3t/check.js`: the browser run (river cards, era cards, page date strings).
- `/tmp/claude-0/-home-user-CIC-Project/dea08a2e-974b-5238-b6f9-cce88a691a2b/scratchpad/r3t/out.json`: its output, HEAD and parent.
- `/tmp/claude-0/-home-user-CIC-Project/dea08a2e-974b-5238-b6f9-cce88a691a2b/scratchpad/r3t/dates.js`: the census run of both `plainDates` versions.
- `/tmp/claude-0/-home-user-CIC-Project/dea08a2e-974b-5238-b6f9-cce88a691a2b/scratchpad/r3t/dates-render.js`: where the six changed dates render.
