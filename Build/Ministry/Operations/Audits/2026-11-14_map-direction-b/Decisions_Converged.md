# Church Family Tree map redesign, direction B, data release 44: the converged decision list

Mark said "Converged, auto mode" on 2026-11-14. This is the design worker's decision list, verbatim, plus Mark's two rulings for the brief.

WHAT WAS WRONG ON LIVE (measured)
1. Below zoom 1.1 the map hid 339 of 350 tradition names but kept all 88 Who pills; each label was tested against its own dot in labelFitRun.
2. Pills were placed for the name's base size, then the name was enlarged, so pills sat on names.
3. The 11 Nov ruling (Open-Gaps 217) was unbuilt: live caps 6 and 4, stacks on both sides.

A. DECISIONS
A1. Direction: "B: Quiet map + list".
A2. Who control is a mark, not the word. A tradition's Who is a single cream figure with no ring. The word "Who" stays in the list title, the chip and the card button.
A3. River Who and tradition Who are told apart. River: a group figure with a count in a capsule outlined in the river's colour. One person: a single figure, no number.
A4. River Who placement. One per river per era, on the river just under the era's top line; touching bubbles stagger one row. A river that begins mid-era has its bubble at the start of its stream, nudged clear of names.
A5. Tradition Who sits tight against its house, on the river side (figure, house, name). It shows wherever the tradition's name shows.
A6. Names tie to traditions. River Who: each shown name sits in one column to the right, joined by a dotted line to its tradition, whose name is forced visible. People told within no tradition sit beside the river near their active year.
A7. Who belongs to a river-era by the person's own active year.
A8. On the map: majors only, up to 5 per river-era spread across the era, up to 4 per tradition; if a river-era has no major, the earliest few.
A9. The Who list: bottom sheet on phone, left panel on tablet and desktop; opens by date with a "By tradition" view; names on the map are bold with "On the map". On a phone its height fits its content.
A10. Map names are about 21px to tap; the list rows (48px) are the 44px route.
A11. Who by zoom: the toggle works at every zoom; from zoom 2.2 each tradition in view shows as many of its major people as fit before the next row, then "+N more"; from 3.4 each name carries its dates.
A12. Tradition mark is a house. Cream; gold for the 11 built worlds. A tradition whose name is hidden falls back to a small dot.
A13. All marks one size (about 14px, capped at 18px): house, figure, book, council ring.
A14. Representative pictures hidden.
A15. Stretch the busy years: inside each era every tradition and story on a river gets at least one row (30 map units) before the next, the same warp for every river; quiet years are not squeezed. Layout rects reserve a full row for house, figure, name and story.
A16. Overlaps: Prototype at rest: 0 overlaps at zooms 0.2, 0.32, 0.39, 0.58, 0.7, 0.9, 1.4, 1.8, 2.6, 4, 7; 1 at 0.47. Map height 12,744 against 11,000 live.
A17. Zoom: continuous, max raised from 3.2 to 9; text and marks stop growing past a set size. Depths: rivers and era titles always; river Who 0.30; built worlds 0.34; council marks 0.45; major traditions 0.50 (others as dots); council names 0.55; stories and cross-church movements 0.65; every tradition and its Who figure 0.80; story titles 1.3; place lines 1.6; people beside traditions 2.2; their dates 3.4.
A18. Small screens open on a simple overview: rivers, era titles, river Who, built worlds only. Tapping a river or an era title goes to reading size there.
A19. Core layers "Eras, rivers, traditions" never switch off. "Tied; others dim": rivers not in focus stay as faint lines with faint dots.
A20. Bar per screen. Every layer has a visible switch carrying the map's own mark. Computer: one row, mark, word and sliding switch. Tablet: one row, mark and word, tick and gold for on. Phone: title on one line, switches in a bottom bar, mark over word. People and Councils gain switches.
A21. Movements switch removed; movements show when rivers they influence are on. Three of the seven (Rescue Missions, Promise Keepers, Church Struggle) have no river link, so they always show.
A22. Connections panel: "Off, Major, All" (373 major lines, 722 all), four kinds as filters, the word "connections" throughout. On a phone: "One tradition at a time": each tradition card has a "Connections · N, Show on the map" button that lights that tradition's lines, names the other ends, fades the rest and shows a four-colour legend chip. That button is on every screen.
A23. Phone header: title and Menu on one line; Reset view under the zoom buttons. The phone's opening hint carries the tagline.
A24. The Key: rewritten to match the icons and keep it simple (the prototype's wording).
A25. An information mark beside each era title opens the era's notes.
A26. Era strip: zoomed in past 0.8, a slim strip under the header names the era in view and opens its card.
A27. Full era cards: NOT IN THIS RELEASE. Mark's ruling: "Map now, cards later". Release 44 ships the information mark, which opens the era notes the map already has. Don't write any era history.
A28. Card title: the map's short name first, formal name beneath. Feedback bar at the foot of each card. "Conversations with [Name] are coming soon" on tradition cards only.
A29. River names, historical then common: Origin · The first churches; Syriac East · Church of the East and Syriac churches; Syriac and Protestant · Reformed churches of India; Caucasus · Armenian and Georgian; Greek East · Orthodox; Church and Empire · The church of the Roman empire; Greek and Latin · Eastern Catholic; Africa · Coptic, Ethiopian and African churches; Africa and Latin · Catholics in Africa; Latin West · Catholic; Latin and Protestant (no common name); Protestant & Evangelical; Global Revival & Pentecostal; Across families; Non-Nicene · Outside the Nicene creed.
A30. Church & Empire on its own river.
A31. Councils: one straight column for all eras, each mark on its own row (38 units apart), name level with it, heading level above, names at 12px or more, none over another.
A32. No search in this release.
A33. Dark is the default.

B. DATA WORK
B1. Major mark for people: a yes/no field on each person entry in the census; the validator requires the field; the site build mirrors it.
B2. Active year per person: one year for each person.
B3. Major traditions (the 0.50 layer): a tradition counts as major if it is a built world or has a major person. No new field.
B4. Church & Empire's river is a census change: a new river; the existing origin record for the Greek/Latin bridge was written about the empire's church and moves with it; the Eastern Catholic river (from 1596, Union of Brest) needs its own origin record resting on a held source.
B5. The three movements with no river link always show (A21).

C. FAULTS TO FIX
C1. personDates() turns every "c." into "about": Josephus prints "37 to early 2nd about", Tyconius "late 4th about". Fix the root cause.
C3. The unused light palette still switches on under a light host theme. Dark is the default. Remove the light palette or finish it.
C4. Tradition cards still say "Major link" and similar; use "connection" everywhere.
C5. Don't build the Representative-picture switch yet. Pictures are hidden.
C6. Build the tablet and phone switches as prototyped, and keep the accessibility of PRs #1628-#1631: names, states, keyboard, announcements.

Defaults the build worker took where the list was silent (asked of the design worker, no answer yet):
- River names (A29): the historical name everywhere a river is named (switch list, river card title, tooltip, Who titles); the common name in the switch list and under the river card title.
- Era card (A25/A27): title, academic name, dates, the era's tag line, and the two era notes the map already carried (WORLD_CONTEXT, ERA_CLOSE). No placeholders.
- The Greek/Latin bridge river lore covered both the imperial church and the Eastern Catholics; with the river split it is wrong for each, so neither river card shows lore until it is rewritten.
- Feedback at the foot of each card records the card's entry as the page "tree/<id>", the same key its own tree page uses; cards with no entry use "atlas-v3".
