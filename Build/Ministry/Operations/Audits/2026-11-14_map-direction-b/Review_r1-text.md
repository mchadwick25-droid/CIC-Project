# Church Family Tree map, direction B: participant-facing text review, round 1

Reviewer: adversarial text review (reading bar and fidelity), 2026-11-14. No repo file edited.

## What was reviewed, and how

- The snapshot I was given (`map-code.js`, `code.diff`, served on :8765 = commit 8a54246d).
- The branch has since moved. HEAD now also has b5599cff (a larger era card) and ab836b12 (major flags). I served HEAD from a scratch copy on :8766 and checked the era card there. Line numbers below are `cft-website/index.html` at HEAD.
- Runtime text was read in Chromium (Playwright) at 1440x900, 820x1180 and 390x844 (touch). The census checks were scripted against `cic-website/data/world-census.json` and the page's own `DATA`. No model calls.
- "Approved" marks wording Mark already approved (A24 Key, A29 river names). Those findings need his ruling. They are not mine to overrule.

Counts: **14 BLOCKING, 17 MINOR.** Four of the BLOCKING items are in approved wording (2, 3, 4, 5). Three are in text this change did not write but now shows in new places (9, 13, 14). Three are in the era card added after the snapshot (10, 11, 12).

---

## BLOCKING

### 1. The Connections chip calls 84% of the red lines "Broke with"
- Where: `index.html:504` (`#connChip .cc-key`), shown by `showConnections()` on every screen.
- Current: `Grew out of` / `Influenced` / `Broke with` / `In contact`
- What is wrong: red is the whole conflict family, "argued against" (174 connections) and "broke with" (32). For Church & Empire, 17 of the 18 red lines are "argued against". The chip still tells the reader that the imperial church "broke with" Donatism, the Anomoeans and others. On a phone this chip is the only legend. The other labels also drop half their kind: "continued as" and "member of".
- Replacement (use the panel's own labels, `LINK_FAMILY_LABEL`, so the two can't drift):
  `Grew out of, continued as` / `Influenced` / `Argued against, broke with` / `In contact with, member of`

### 2. The Key tells phone users to use a control phones don't have (approved, A24)
- Where: `index.html:113256`, `buildLegend()` keyRows, "A connection".
- Current: `A line between two traditions. Turn the lines on under Connections.`
- What is wrong: at 640px and below, the Connections group is hidden (`.chip-group.grp-links{display:none}`) and `effectiveLinkMode()` is forced to off. The Key is shown on phones. The only route there is the card button (A22).
- Replacement (true on every screen, because A22 puts the card button everywhere):
  `A line between two traditions. To see a tradition's lines, open its card and choose Connections.`

### 3. "Years with nothing on record" is false about history (approved, A24)
- Where: `index.html:113257`, keyRows, "A dashed river".
- Current: `Years with nothing on record.`
- What is wrong: `threadPath()` draws a dash where no tradition of that river is on this map (`cnt===0`). It says nothing about the historical record. The dashes it draws today include Greek East 313–325 (the years before Nicaea), Africa and Latin 1881–1905, and Caucasus 1448–1515. All of these are well documented. The old Key said something narrower: "years with none on record", meaning movements.
- Replacement: `Years when the map has no tradition on that river.`

### 4. "Eastern Catholic" names a river that holds a Baptist and Orthodox record (approved, A29)
- Where: `index.html:110878` (`FAM` k:3.5). The root cause is in the census: `world-census.json:71390-71392`.
- Current: `common:"Eastern Catholic"`
- What is wrong: the river's 10 members include "Persecuted Church", the Initsiativniki Baptists and Romania's Lord's Army. Neither is Eastern Catholic. That record's own `lane` field says `3<->6 span (Greek East / Protestant)`, but its `laneOrder` is 3.5. The map's own note for it says: "It sits in its own lane because it doesn't belong in either Greek East or Protestant & Evangelical outright, and forcing it into one would misstate the other half." The new common name turns that old misfiling into a false label in the switch list and on the river card.
- Replacement: until the record moves, `common:""`. That gives no common name, as with Latin and Protestant. The real fix is a census and design call for Mark: give the record its own river (laneOrder 3.6, with its existing `Greek East/Prot. bridge` notes). After that, "Eastern Catholic" is true of the nine that remain.

### 5. "Reformed churches of India" is the wrong family name (approved, A29)
- Where: `index.html:110874` (`FAM` k:1.5).
- Current: `common:"Reformed churches of India"`
- What is wrong: capital-R "Reformed" names the Calvinist family. The map's own notes for this river describe two other things. One is the Mar Thoma Church, a Syriac-rite church reformed along Anglican-evangelical lines and in communion with Anglicans. The other is the hill churches of northeast India, "Presbyterian among the Khasis and northern Mizos" and Baptist elsewhere. "Of India" also suggests all such churches in India.
- Replacement: `common:"Mar Thoma and churches of northeast India"`

### 6. The era 10 card counts movements across churches as traditions on rivers
- Where: `index.html:113128` (`openEraCard`). The count comes from `eraCounts` (`index.html:110921`).
- Current: `${esc(e.dates)} · ${eraCounts[i]} traditions on ${eraLaneCounts[i]} rivers`. Era 10 shows "71 traditions on 13 rivers".
- What is wrong: `eraCounts` still includes the 7 movements across churches, so era 10 has 64 traditions, not 71. The map keeps those 7 apart ("Movements across churches") and draws none of them on a river. The old era tag said "movements across … lanes", which fit that count. "Traditions on rivers" does not. Don't change `eraCounts` itself, because it sizes the bands.
- Replacement:
  `const nTrad=churchBodies.filter(m=>m.era===e.num).length, nAcross=acrossMovements.filter(m=>m.era===e.num).length;`
  `` `${esc(e.dates)} · ${nTrad} traditions on ${eraLaneCounts[i]} rivers${nAcross?` · ${nAcross} movements across churches`:''}` ``
  Era 10 then reads "64 traditions on 13 rivers · 7 movements across churches".

### 7. The era title's spoken label is wrong in the overview
- Where: `index.html:112322` (era label in `render()`).
- Current: `` `${e.num}. ${e.title}, ${e.dates}. Opens a note on this era.` ``
- What is wrong: in the simple overview, activating the title calls `goIntoEra()`. That zooms in and announces "… Names are showing." No note opens. The overview is the default on phones (scale 0.39) and on short laptop screens, for example 1280x720. I confirmed this at 390x844.
- Replacement: in `labelFitRun()`, right after `svg.classList.toggle('simple',simple)` (`index.html:113461`), add:
  `` if(simple!==labelFit.simple){labelFit.simple=simple;gLabels.querySelectorAll('.era-label').forEach((t,j)=>t.setAttribute('aria-label',`${eras[j].num}. ${eras[j].title}, ${eras[j].dates}. ${simple?'Zooms in to this era.':'Opens a note on this era.'}`));} ``

### 8. River tooltip and label: "1 movements · 312–312"
- Where: `index.html:112350` (river `aria-label`), `112348` (`riverTip`), `112696` (`tipForRiver`).
- Current: `` `${f.name} river, ${members.length} movements` `` and `` `${count} movements · ${minYear}–${maxYear}` `` (called with the first and last *start* year).
- What is wrong: the new Church and Empire river, and Across families, show "1 movements". Church and Empire's tooltip shows "312–312". Every river's range also stops at its last start year, for example Latin and Protestant "1906–1938", though it runs to 2010. The Key and the era card call these "traditions".
- Replacement:
  - `` 'aria-label':`${f.name} river, ${members.length} ${members.length===1?'tradition':'traditions'}` ``
  - `` const riverTip=tipForRiver(f,members.length,Math.min(...years),Math.max(...members.map(m=>m.end))); ``
  - `` return `<div class="n">${esc(f.name)}</div><div class="m">${count} ${count===1?'tradition':'traditions'} · ${minYear}–${maxYear}</div>`; ``
  - Church and Empire then reads "1 tradition · 312–451".

### 9. Built worlds say "Open for conversation". The Key and the cards say "coming soon"
- Where: `index.html:112672` (`statusLabel`), used in every tradition `aria-label` and tooltip. The source is census `statusMeta["Built & Live"].shortWord` (`world-census.json:222`). This is old text, outside the diff.
- Current: hovering Donatism shows "Open for conversation". A screen reader hears "Donatism, c. 311-439 CE, Open for conversation".
- What is wrong: `CONVERSATIONS_LIVE=false`. The new Key line says "Conversations with its Representative are coming soon", and every card says the same. The tooltip now contradicts both on the same screen. The river card's "Its one movement is Built & Live." uses the internal status name too.
- Replacement:
  `` function statusLabel(m){if(m.status==='Built & Live'&&!CONVERSATIONS_LIVE)return 'Conversations coming soon';const sm=DATA.statusMeta&&DATA.statusMeta[m.status];return (sm&&sm.shortWord)||m.status;} ``

### 10. Era card (HEAD b5599cff): "Stories from this era" lists stories from other eras
- Where: `index.html:113137-113139`.
- Current: `<h3>Stories from this era</h3>`, `On the map · N`, `In the traditions' cards · N stories in M traditions`
- What is wrong: the second list takes every story in each of the era's traditions, whatever its date. The era 1 card (70–312) lists "Nine Years Waiting for Faustus, 383", "Palladius Asks Where the Other Bishops Are, 381" and "The Psalms on the Wall of Augustine's Room, August 430". The era 3 card (451–622) lists Hypatia (415), Ephesus (431), "Toledo IV, Canon 57, 633" and "Colmán Takes the Bones Home, 664".
- Replacement (no claim about the stories' dates):
  - `h+='<h3>Stories</h3>';`
  - `<p class="meta">On the map, from this era · ${mapStories.length}</p>`
  - `<summary>In the cards of this era's traditions · ${nTrad} ${nTrad===1?'story':'stories'} in ${tradStories.length} ${tradStories.length===1?'tradition':'traditions'}</summary>`

### 11. Era card (HEAD): council years printed twice
- Where: `index.html:113130`.
- Current output: "Chalcedon 451 451", "Arles, 314 314", "Councils of 251 251", "Carthage, 411 411", "Ephesus 431 431", "Constantinople 553 553", "Toledo 589 589", "Dvin, between 596 and 609 c. 596–609".
- Replacement for the list item:
  `` `<li><button type="button" class="panel-link" data-id="${esc(c.id)}">${esc(c.shortName||c.name)}</button>${/\d{3}/.test(c.shortName||c.name)?'':` <span class="meta">${esc(c.dates||'')}</span>`}</li>` ``

### 12. Era card (HEAD): beyond A27, and two headings misname their paragraphs
- Where: `openEraCard` at HEAD, `index.html:113128-113141`.
- What is wrong:
  - A27 says: "Full era cards: NOT IN THIS RELEASE … ships the information mark, which opens the era notes the map already has". The build default listed title, academic name, dates, tag line and the two notes. HEAD drops the academic name and the tag line, and adds councils, rivers, people and stories. That is a change to a converged plan, so it needs a named change order from Mark or a revert. I can't tell whether he approved it after the decision list.
  - The headings mislabel their text. `How the era opens` sits over notes that sum up the whole era. Era 9's note is "The era's honest theme is entanglement…". `How the era closes` sits over "The tree's history runs to 2010. Movements since then will be added as they become history." That sentence is about where the map stops, not about how 1906–2010 ended.
- Replacement: revert to the A27 default, or get Mark's change order. If the sections stay, change the headings: `<h3>About this era</h3>` and `<h3>Where the map stops</h3>`.

### 13. The era notes now shown in the card fail the reading bar, and three conflict with the map's own data (old text, Mark's call under A27)
- Where: `WORLD_CONTEXT`, `index.html:111538-111547`, shown by `openEraCard`. They used to sit on the map under each era title.
- What is wrong:
  - Measured Flesch-Kincaid grade is 11.6 to 19.6, and Reading Ease is 2 to 53. Five notes have a sentence of 28 to 43 words. The bar is grade 8–10, ease 60 or more, and nothing past about 25 words.
  - Conflicts with the map:
    - Era 1 says persecution "finally ends" in 313. The map's own story "The Forty Martyrs of Sebaste" is dated 320.
    - Era 2 says Chalcedon is "just after this band". The same card lists Chalcedon 451 among the era's councils, and the era runs 312–451.
    - Era 7 says "each with its own direct descendants still living today". Family of Love has `living:false`.
  - Era 3's "Rome itself falls to invasion in 476" is a popular simplification. In 476 the last Western emperor was deposed. The city was not invaded that year.
  - Rewriting these is Mark's call (A27, "Don't write any era history"). The rewrites below only split sentences and swap in plainer words. They add no claim. They narrow or drop only the three claims the map's data contradicts, and they drop the 476 sentence.
- Replacements:
  1. `This era starts where the map does, when the Jerusalem Temple falls in 70 CE. It runs to Constantine's Edict of Milan in 313, which officially ends the persecution these movements describe. For the Persian church east of Rome, it went the other way. Persecution there only grew worse after 312.`
  2. `Historians call this the era of the 'imperial church'. Christianity moves from a persecuted minority to the empire's own religion. Its defining creeds, from Nicaea to Chalcedon, are settled because an emperor now has a stake in the outcome.`
  3. `The communions part ways. Chalcedonian, miaphysite and East Syriac Christianity become separate families, each aware of itself. The Latin West enters the post-Roman kingdoms. Everywhere, monasticism becomes the engine that shapes the church.` (The 476 sentence is dropped. Bringing back a corrected one is for Mark.)
  4. `Christianity becomes a minority faith across its old heartlands as Islam rises. It converts new peoples in the north and fights an internal war over religious images. It sends its longest missions east along the Silk Road.`
  5. `The Latin West has a great creative explosion. New religious orders and lay movements appear, and women's religious life reaches a scale not seen before. Meanwhile Byzantium consolidates, and the Christian East endures new pressures.`
  6. `This era brings plague, a split papacy and crisis in the church's institutions. They are met by the most inward devotional writing Christianity had yet produced, in everyday languages and open to lay people. For scale: the Black Death sweeps Europe in 1347–51, during this era.`
  7. `The Western church is remade, several ways at once. This era holds the Reformation's many movements, often rivals, side by side. Most have direct descendants still living today.`
  8. `Established churches settle into place. Renewal moves into small groups, personal religious experience and revivals on both sides of the Atlantic. In this era, the spiritual life story told in the first person becomes a mass genre.`
  9. `Christianity spreads around the world, both under the shadow of empire and against it. The era's honest theme is entanglement. Mission is tangled with colonialism, revival with respectability, and liberation with paternalism. They are held together rather than resolved.`
  10. `Christianity's center of gravity moves south and east. The Pentecostal and Spirit-movement family becomes the largest new Christian reality since the Reformation. For scale: World War I (1914–18) breaks out early in this era.`
  - After the rewrite, no sentence is over 21 words and grade is 6–12. Ease stays below 60 where the names carry it, as in 3 and 9.

### 14. People's dates read as lifespans when many are not (census data, now in many more places)
- Where: census `dates`, via `personDates()` (`index.html:111759`). It feeds the Who list rows, names on the map from zoom 3.4, tooltips, `aria-label`s, and the card's "Dates" fact when there is no `datesNote`.
- Current examples: "Martin Luther / 1517–1546", "John Calvin / 1536–1564", "Augustine of Hippo / 386–430", "Ambrose / 374–397", "Constantine the Great / 312–337", "Gregory VII / 1073–1085".
- What is wrong: a bare range after a name reads as birth to death. Luther was born in 1483, Calvin in 1509 and Augustine in 354. These ranges are active years, office or reign. 69 of the 190 people have a bare range. 38 of those have no `datesNote` to correct it, including most of the major names. "By date" also sorts by a hidden `activeYear`, so the list looks out of order against the dates it shows. For example, Hilary "about 300–367" comes after Lucifer "bishop by 353".
- Replacement: this is a census fix, and each entry has to be checked against its sources. Write the kind of span into any `dates` string that is not a lifespan, as the census already does for others ("bishop 412-444", "king 586-601"). Examples: `"active 1517-1546"` renders "active 1517–1546". `"pope 1073-1085"` renders "pope 1073–1085". `"emperor 312-337"` renders "emperor 312–337". `personDates()` needs no change.

---

## MINOR

### 15. Key: "A family of churches" (approved, A24)
- Where: `index.html:113247`. Current: `A family of churches. It is wider where more traditions were active.`
- Wrong: by the map's own river notes, several rivers are not families. Across families is a label. Non-Nicene is "a thematic, doctrinal-position category". Syriac East is "a language family, not a communion".
- Replacement: `A family of churches, or a group the map keeps together. It is wider where more traditions were active.`

### 16. Key: "Everyone on that river" (approved, A24)
- Where: `index.html:113252`. Current: `Everyone on that river in that era, with the count.`
- Wrong: the count is the people the map names. Read alone, it sounds like everyone in that church.
- Replacement: `Everyone the map names on that river in that era, with the count.`

### 17. Key says "Tap" on computers (approved, A24)
- Where: `index.html:113248`, `113251`. Current: `Tap its name to open its card.` and `Tap to see who they were.`
- Wrong: the opening hint already switches between Tap and Click (`coarsePointer`). The Key doesn't.
- Replacement: `` `${coarsePointer?'Tap':'Click'} its name to open its card.` `` and `` `${coarsePointer?'Tap':'Click'} to see who they were.` ``. `coarsePointer` is declared before `buildLegend()` runs.

### 18. Connections panel mixes "movement" and "tradition", and doesn't say how to "pick"
- Where: `index.html:113235`, `113237`.
- Wrong: the panel calls the same mark a "tradition" in one sentence and a "movement" in the next. "Movement" is also the name of a different mark, the movement across churches. The second note has a 27-word sentence. "Pick a movement" doesn't say how.
- Replacements:
  - In 113235, `Where a connection joins two movements equally, the mark sits at both ends.` becomes `Where a connection joins two traditions equally, the mark sits at both ends.`
  - 113237 becomes `Major connections show one tradition growing out of another, or a recorded break. They also show acts of authority the sources record, such as a council condemning a group. To see all of one tradition's connections, open its card and choose Connections.`
  - The river card's "N movement(s)" and "Movements in this river" (`113077`, `113110`) are old text. Align them with "traditions" when they are next touched.

### 19. Connection counts: singular, filters, spoken names
- Where: `index.html:113369-113370`, `113315`, `113236`.
- Wrong:
  - 51 traditions have one connection, and the chip then says "1 connections of Medieval Ireland are showing".
  - The mode announcement always says "All 722" or "373 major", even when some kinds are switched off or some rivers are faint.
  - The buttons' accessible names are "Major373" and "All722".
- Replacements:
  - `` const cn=n===1?'connection':'connections'; `` then `` `${n} ${cn} of ${name} ${n===1?'is':'are'} showing. Clear them.` `` and `` announce(`${n} ${cn} of ${name} showing.`) ``.
  - `` const vis=gEdges.querySelectorAll('.edge-line:not(.is-off)').length; announce(linkMode==='off'?'Connections hidden.':`${vis} ${linkMode==='major'?'major ':''}${vis===1?'connection':'connections'} showing.`); ``
  - `Major <span>${nMajor}</span>` and `All <span>${nAll}</span>`, with a space before each span.

### 20. "▾" and "✓" are read aloud in switch names
- Where: `index.html:113262` (`group()`), CSS `index.html:385`.
- Wrong: the accessibility tree reads "Rivers ▾", "Connections ▾", and on tablets "People ✓" [pressed]. The state is announced twice, once as a symbol.
- Replacement: `<span class="dn" aria-hidden="true"> &#9662;</span>`. For the CSS: `.feature-bar .chip[aria-pressed="true"] .sw-name::after{content:" \2713" / ""}`, which gives the tick an empty spoken name.

### 21. Card Who button state "On the map ×" is read as "times"
- Where: `index.html:112016`.
- Replacement: `btn.querySelector('.who-state').innerHTML=on?'On the map <span aria-hidden="true">×</span>':'Show on the map';`

### 22. River "+N more" says it opens a list that is already open
- Where: `index.html:111938`. Current: `` `${rest} more ${rest===1?'person':'people'}. Opens the full list.` ``
- Wrong: on tablet and desktop the list is already open, and the link only moves focus into it. On a phone it expands the list.
- Replacement: `` `${rest} more ${rest===1?'person':'people'}. Shows the full list.` ``

### 23. Opening hint: "to go in"
- Where: `index.html:113813`. Current: `… an era or a river to go in.`
- Replacement: `` (coarsePointer?'Tap':'Click')+' an era or a river to zoom in.' ``

### 24. Phone menu tagline starts in lower case
- Where: `index.html:477`. Current: `an interactive map of Christian tradition, from the first house-churches to about 2010`
- Wrong: in the header it reads as a subtitle. In the menu it stands alone as a sentence.
- Replacement: `An interactive map of Christian tradition, from the first house-churches to about 2010.`

### 25. River common names: capitals, and two that set a church apart from its own family (approved, A29)
- Where: `index.html:110873`, `110877`, `110879`, `110886`.
- Wrong: "Outside the Nicene creed" and "The church of the Roman empire" should take capitals: Nicene Creed, Roman Empire. "Coptic, Ethiopian and African churches" reads as if Coptic and Ethiopian were not African. "Church of the East and Syriac churches" reads as if the Church of the East were not Syriac.
- Replacements: `Outside the Nicene Creed`; `The church of the Roman Empire`; `Coptic, Ethiopian and other African churches`; `Church of the East and other Syriac churches`.

### 26. Era dates still show "c." and hyphens; people's dates no longer do
- Where: era tag `index.html:112337`, era strip `113412` and its `aria-label` `113413`, era card `113128`, Who list subtitle `112166`.
- Current: "70-312 CE", "1906-c. 2010".
- Replacement: move `personDates()`'s replace chain into `function plainDates(s){return String(s||'').replace(/\b(\d+(?:st|nd|rd|th))\s+c\./g,'$1 century').replace(/(\d)-c\.\s*/g,'$1 to about ').replace(/\bc\.\s*(?=\d)/g,'about ').replace(/(\d)-(?=[a-z])/g,'$1 to ').replace(/(\d(?:st|nd|rd|th)?)-(?=\d)/g,'$1–');}`. `personDates()` then returns `plainDates(P.entry.dates)`, and `e.dates` is replaced by `plainDates(e.dates)` at those five places. That gives "70–312 CE" and "1906 to about 2010".

### 27. Four census date lines don't read as dates in the Who list
- Where: census `dates` (as shown in Who list rows, tooltips and `aria-label`s).
- Current output and replacement census string (each based on the entry's own `datesNote` or teaser):
  - Olympias: "about 368–408 to 420" becomes `born c. 368; died between 408 and 420`
  - Sozomen: "about 370–380 to after 443" becomes `born c. 370-380; wrote after 443`
  - Marius Mercator: "Commonitorium 429" becomes `warned Constantinople in 429`
  - Valentinus: "at Rome, from Hyginus to Anicetus" becomes `at Rome in the time of bishops Hyginus to Anicetus`

### 28. Era card (HEAD): "People to meet"
- Where: `index.html:113133`.
- Wrong: on the sister site of a product built on conversations, "meet" can read as an offer to talk with these people.
- Replacement: `<h3>Major people</h3>`. This also matches the card's own "And N more major people".

### 29. "Conversations with … are coming soon" appears twice on every built-world card
- Where: `index.html:113000` (second `worldDoor(m)`, inside `if(m.why)`). This is old code. A28 names this line.
- Wrong: all 11 built worlds have `why`, so the sentence shows twice.
- Replacement: delete `h+=worldDoor(m);` at 113000. The line still shows once, after the Representative line.

### 30. Council cards never name the new Church and Empire river
- Where: census `council.rivers`.
- Wrong: Arles 314, Nicaea, Sardica, Constantinople I and Chalcedon all tie to the imperial church (A30). Their cards' "Rivers" line still lists Greek East and Latin West only.
- Replacement: add `"Church and Empire"` to those five councils' `rivers` lists. This is a census change, so it is for the census owner.

### 31. Card headings "Influenced / transmitted to" and "Influenced by" sit over every kind of connection
- Where: `index.html:112971-112972`. This is old text. C4 asks for "connection" everywhere.
- Wrong: the rows under them include "argued against" and "broke with". Church & Empire's card lists 17 "argued against" rows under "Influenced / transmitted to".
- Replacement: `<h3>Connections from this tradition</h3>` and `<h3>Connections to this tradition</h3>`.

---

## Checked, no finding

- **`personDates()` (C1).** I ran all 186 distinct census strings through it. "c." for century and "c." for circa are both handled: "37 to early 2nd century", "late 4th century", "5th–6th century", "mid-2nd century", "about 480 to about 575", "393 to about 458", "about 460 to before 533". No "c." is left in any output.
- **Connection counts.** "Major 373" and "All 722" match the lines drawn. A card's "Connections · N" matches the lines it lights. Lit lines show even when their kind is filtered out.
- **Who counts.** The pill count, the list total, "+N more" and the announcement agree. For Latin West era 2, "26 people, 5 named on the map" and "+21 more" all line up.
- **Key marks.**
  - The house, gold house, dot, figure, capsule, book, council ring and era "i" match what is drawn.
  - All 12 councils touch 3 or more traditions.
  - All 62 map stories are Documented or Widely Accepted.
  - All 11 gold-house worlds are public-open with a Representative and say "coming soon".
- **No "link" left in participant text (C4).** Edge card: "Major connection". Person card: "Connections on the map". Note: "checked connection".
- **Switch, toolbar, tray, menu and zoom labels.** These are short and plain, and have names and states.

## Outside the text brief (for the design worker)

- The bar's "Key" button and the era information mark use the same "i" glyph. The Key row "About an era: Opens a note on that era" describes the glyph the Key button itself wears.
- The Key's "A connection" icon combines the green of "grew out of" with the round dots that mark "in contact" lines.
