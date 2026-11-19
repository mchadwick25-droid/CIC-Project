# Round 1 code review: Church Family Tree map, direction B (release 44)

**What I reviewed.** The working tree I was given, which the session committed during the review as `8a54246d`. It is byte-identical to `scratchpad/review/index.html`.

**Line numbers.** They refer to `cft-website/index.html` at `8a54246d`. To get the matching line in `map-code.js`, subtract 110869 from the index line.

**How I tested.**
- I served a copy of that exact version on port 8766, with feedback.js and feedback.css from the same commit.
- I tested it with Playwright on a 1440×900 desktop, an iPhone 13, an iPad Mini, and at widths of 641, 700, 768, 820, 900, 1024, 1180, 1181, 1200 and 1280px.
- HEAD moved while I worked. I re-ran every finding against HEAD `dd53c963` on port 8767 and give its status there.

**Checks that pass.**
- `node tools/validate-census.mjs`: 0 errors, 4 warnings.
- `node --test Build/tools/generate_tree_pages.test.mjs`: 34 of 34 pass.
- The prototype's own overlap check (`artifact-files/.../ref/overlap-check.js`), run on the build: 0 overlaps at all 12 zoom levels in A16, and `CANVAS_H` = 12,744.
- 600 random actions on each of desktop, phone and tablet: switches, Who, cards, connections, zoom and pan. No runtime errors.
- `personDates()` run over all 190 person date strings: no output is misplaced.

## Decisions

| # | Status | Where it is shown (index.html line) |
|---|---|---|
| A1 | Met | Quiet map by depth in `labelFitRun` (113432-113480); Who list `#whoTray` (496-502) |
| A2 | Met | `whoFigure` (112037-112050): one figure, no ring, cream (CSS 260). "Who" stays in the list title (112164), the chip (112011) and the card button (`whoCountText`, 112002-112005) |
| A3 | Met | `renderWhoPills` (112018-112036): capsule outlined in the river colour, group figure with a count, one person shows a single figure and no number |
| A4 | Met | `placeWhoMarks` (112069-112084): just under the era line; staggered by 0, 1.5, 3 or 4.5 U; a river that starts mid-era gets its bubble at the start of its stream, moved clear of names |
| A5 | Met (as prototyped) | 112086-112096: order is figure, house, name, and the figure is hidden whenever the name is hidden. Figures appear from 0.80 (A17), so major names at 0.50-0.80 have no figure. The prototype does the same (`T_ALL`) |
| A6 | Met | `drawWhoNames`: a single column (111900); dotted line from each name to its tradition (111921); that tradition's name forced visible (`lit`, 113467); people tied to no tradition are placed by active year (111904-111908) |
| A7 | Met | `riverWho` key uses `activeYear` (111826) |
| A8 | Met | `scopePeople` (111842-111854): up to 5 per river, spread across the era; up to 4 per tradition; if there are no majors, the earliest 3 |
| A9 | Met (see 19) | Left panel (CSS 313-338); bottom sheet on phone with height auto, at most 42vh (407-409); opens by date; "By tradition" view; names on the map are bold and marked "On the map" (112153-112157) |
| A10 | Met | Map names have a hit height of 1.55 × the name size, about 21px (111925); list rows are at least 48px (CSS 333) |
| A11 | Met | `autoWho` (112100-112144): from 2.2, rows fill the gap to the next tradition, then "+N more"; dates from 3.4 |
| A12 | Met | House: gold for built worlds, cream otherwise (112467-112470); a tradition whose name is hidden falls back to a dot (CSS 273-274) |
| A13 | Met | `markU` (111778). Measured: house, figure, book and council ring are about 14px, capped at 18px |
| A14 | Met | No portrait is drawn. The data is left behind as dead code (see 18) |
| A15 | Met | `eraWarp` (110939-110965); full-row layout rectangles in `markRects` (111656-111664) |
| A16 | Met | Prototype check: 0 overlaps at every listed zoom; `CANVAS_H` 12,744 (110967). A broader check found one visible overlap the prototype check does not measure (see 14) |
| A17 | **Partly met** | Zoom is continuous with `MAX_S`=9 (113356); every depth constant matches (111774-111775, 113429-113431). But council names, cross-church names and their marks, and focus rings keep growing (see 1) |
| A18 | Met | Opens at a scale of at least 0.391, which gives the simple view (113511-113518). Tapping a river (113768) or an era title (112323 → `goIntoEra`, 113130) goes to 0.9 |
| A19 | Met | No switch for eras or traditions. A river switched off stays as a faint line with faint dots (CSS 285-287); Who and connection focus dim everything else (265, 289) |
| A20 | **Partly met** | Desktop and phone are right (CSS 389-414). On tablets the bar is not always one row (see 10) |
| A21 | Met | `acrossLanes` and `across-out` (113197-113202, 113260). Checked: with all rivers off, only Rescue Missions, Promise Keepers and Church Struggle show |
| A22 | Met | Off, Major (373) and All (722) (113213); four kinds as filters (113216); on a phone the Connections group is hidden (CSS 399), connections default to off (113195), and the card button (113136-113140) leads to `showConnections` (113331-113349) with the four-colour chip (503) |
| A23 | Met | Phone header on one line (CSS 389-394); Reset view under the zoom buttons (494); opening hint with the tagline (113790) |
| A24 | Met | `keyRows` (113223-113235) match the prototype's wording word for word |
| A25 | Met | `era-info` mark (112327-112334), placed after the title (113372) |
| A26 | Met | `syncEraStrip` (113378-113391), from 0.8; opens the era card |
| A27 | Met | `openEraCard` (113117-113129) shows only what the map already had. HEAD now goes further (see the notes at the end) |
| A28 | **Partly met** | Short name first, formal name beneath (112931-112933), on tradition cards only, as in the prototype. Feedback is added at the foot of each card (113144), except on a card opened from a link (see 3). "Coming soon" appears on tradition cards only, but twice on built worlds (see 21) |
| A29 | Met | `FAM` (110870-110886); used in the switch list, river card, tooltip and Who titles |
| A30 | Met | Lane 3.4 (110876; origin record at 111072) |
| A31 | **Partly met** | One column with 38-unit rows and names level with their marks (111456-111478, 112642-112669). But the "at least 12px" rule (113421) lets names grow without limit (see 1) |
| A32 | Met | No search |
| A33 | Met | One dark palette, `color-scheme: dark` (CSS 10-16) |
| B1 | Met | Validator requires `major` as a boolean (validate-census.mjs:406); sync copies it (census_atlas_sync.py:79); 190 of 190 persons have it; page data matches the census (0 mismatches) |
| B2 | Met | `activeYear` required as a whole number (validate-census.mjs:407); 190 of 190 |
| B3 | Met | `isMajorTradition` (111816) |
| B4 | Met | The declared record moved to 3.4 unchanged (111072). The 3.5 record is a lineage record (111090) on the documented "broke with" edge, whose primary quotes are held in `cic/texts/akty-zapadnoi-rossii_t4…`. The validator's origin check passes |
| B5 | Met | As A21 |
| C1 | Met | `personDates` (111758-111766). Josephus now reads "37 to early 2nd century" and Tyconius "late 4th century"; checked across all date shapes |
| C3 | Met | No light palette, `isDark` or `data-theme` left |
| C4 | **Partly met** | The word "link" is gone. Tradition cards still head connections "Influenced / transmitted to" and "Influenced by" (see 11; fixed at HEAD) |
| C5 | Met | No picture switch |
| C6 | **Partly met** | Switches are built as prototyped, with names, pressed states and announcements. But see 4, 5, 8 and 9 for focus return, the keyboard tab stop and focus visibility, and 22 for the tick in tablet names (fixed at HEAD) |

## Findings

### BLOCKING

**1. Some text and marks keep growing past the cap (A17, A31).** Still open at HEAD.

Where:
- 113421 `sizeMarks`: `const f=Math.max(12,12/scale)`, used for council names and the "Major councils" heading.
- 112599: cross-church dot, `r:3.2`.
- 112602 and CSS 149: cross-church name, fixed at 11 units.
- 112565: "Movements across churches" heading.
- 112453-112454: tradition halo, `r:9`, and focus ring, `r:10`.
- 112536-112537: story halo, `r:19`, and focus ring, `r:20`.

What is wrong: measured at zoom 9, these are 108px council names and heading, 99px cross-church names, a 29px dot radius, and a 90px focus ring with an 18px stroke (180px on stories). Tradition names stop at 16px and marks at 18px.

How it fails:
- At zoom 3 in era 2, "Nicaea" is 36px next to 16px tradition names (`shots/council-z3.png`).
- At zoom 9, tabbing to a tradition draws a 90px gold ring round an 18px house (`shots/focus-z9.png`).

Fix: use the same capped formula as the names and marks.
- Council names: `f=Math.min(Math.max(12,12/scale),16/scale)`.
- Cross-church names, heading and dot: size them per zoom in `sizeMarks`.
- Halos and focus rings: size them from `markU()`.

The prototype has the same council rule, but the decision says text stops growing.

**2. A click or tap on a tradition's house opens its Who list instead of its card.** Still open at HEAD.

Where: 112062 (`hit.style.r=(22/scale)+'px'`), with the figure placed at 112091. `#prof-pills` (111517) is drawn above `#nodes`.

What is wrong: the figure's invisible hit circle is 44px across. It is centred about 14px from the house, so it covers the whole house. At the house centre, `elementFromPoint` returned the Who figure for 9 of 9 traditions at 0.9, 5 of 5 at 1.5 and 1 of 1 at 3, on both desktop and iPhone.

How it fails: click Alexandria's gold house. Who opens and the map zooms; the card never opens. Houses of traditions without people still open the card, so the same mark behaves two ways.

Fix: give the figure a hit area that extends away from the house only, or put the Who hit layer under the nodes. The prototype has the same hit circle.

**3. A card opened from a shared link has no feedback bar (A28).** Still open at HEAD.

Where: the deep-link open at 113795-113799 runs while the page is still parsing. `showPanel` mounts feedback only `if(window.PageFeedback)` (113144), and `feedback.js` loads with `defer` (113808).

How it fails: `/?world=desert-monasticism`, `augustine-of-hippo` and `council-of-nicaea-325` all open with no "This helped" and no "Report a problem". Any card opened afterwards has them.

Fix: open the deep-linked card after the deferred scripts have run (DOMContentLoaded), or let `PageFeedback` mount into a panel that is already open when it starts up.

**4. Closing the Who list or the connection view drops keyboard focus and announces nothing (C6).** Still open at HEAD.

Where:
- `clearWho` (111967-111971) handles only the case where the chip had focus.
- The list's × button (112185) and Escape (112188).
- `clearConnections` (113324-113330), the chip's × (113350) and Escape (113351).

How it fails:
- Tab to a river bubble, press Enter, focus a list row, press Escape: focus lands on `BODY`.
- Same with the list's ×.
- Card → "Connections · 14" → press Enter on the chip's ×: focus lands on `BODY`.
- In every case the status region still says "Who list open…" or "14 connections of The Desert showing."

Fix: remember what opened the view (bubble, figure, card button, "+N more" or the tradition's mark). On close, return focus to it, or to the nearest map item if it is gone. Announce "Who list closed" and "Connections cleared". The card already restores focus this way (`closePanel`).

**5. Phone: "Show on the map" in a card leaves focus on the page body. This is a regression.** Still open at HEAD.

Where: 111975, `lastFocused=null;closePanel();`.

What is wrong: the live code moved focus to the Who chip here. That chip is hidden on phones now, and nothing replaced it.

How it fails: on an iPhone 13, open The Desert and tap "Who · 5 people / Show on the map". The card closes, the sheet opens, and focus is on `BODY`.

Fix: move focus into the sheet, to its title, its close button or its first row.

**6. On a phone, any window resize while Who is on closes the open card, even mid-typing.** Still open at HEAD.

Where: 113781 (`resize → if(whoScope)zoomToWho()`) together with 111975 (`zoomToWho` closes the card on narrow screens).

How it fails: open Who, tap a person in the sheet, tap Report a problem and start typing. Then either rotate the phone back to portrait, or use a browser whose keyboard resizes the window, such as Firefox for Android. The card closes and focus is lost. Reproduced by shrinking the viewport to 390×420 with the card open.

Fix: close the card only when Who is switched on (in `setWho`), not inside the fit step, and do not refit while a card is open.

**7. Tablet portrait: Who opened from a card shows none of its names on the map.** Still open at HEAD.

Where: 111975 closes the card only at 640px or less; the space left for the map is computed at 111983-111985. The list is `min(330px,42vw)` wide (CSS 313-314) and the card `min(380px,90vw)` (CSS 99).

How it fails: on an iPad Mini (768px), open Alexandria and tap "Show on the map". Three people are marked "On the map", but 0 of 4 names are visible in the 65px strip left between list and card (`shots/tablet-who-card.png`). Measured:

| Width | Names visible |
|---|---|
| 700px | 0 of 4 |
| 820px | 0 of 4 |
| 900px | 1 of 4 |
| 1024px | 4 of 4 |

Fix: if the list and card leave less than about 360px of map, close the card as on phones and move focus to the list. The prototype has the same fit code.

**8. Once zooming hides the map item that holds the keyboard tab stop, Tab can no longer reach the map (C6).** Still open at HEAD.

Where: `syncMapStop` and its MutationObserver (113619-113636) re-pick the tab stop only when DOM children change. Depth hiding is done with CSS classes and `display:none`:
- CSS 275: simple mode hides non-built traditions.
- CSS 303: era titles are hidden past 0.8.
- CSS 277 and 280: stories and councils are hidden below their depth.

How it fails: arrow to Cistercians at 0.9 and press "−" four times, reaching 0.37 (simple view). Focus drops to `BODY`. The only tab stop left is the hidden Cistercians, so Tab from the map skips straight to Zoom in. The same happens when the tab stop is an era title or info mark and you zoom past 0.8.

Fix: call `queueMapSync()` whenever the depth classes change. If the focused item is hidden, move focus to the nearest item still shown.

**9. Keyboard focus on a Who bubble or figure is hard to see. This is a regression.** Still open at HEAD.

Where: CSS 246 and 258-261.

What is wrong: focus only changes the small figure from cream to gold. The bubble outline and the count do not change. Live had a 2px gold outline (`.who-pill:focus-visible rect`), which also applied in the prototype; this build removed that rule. On built worlds the focused figure is the same gold as the house next to it.

Fix:
- Bubbles: `.who-pill:focus-visible .who-cap{stroke:var(--gold-leaf);stroke-width:2px}`.
- Figures: a ring drawn only on `:focus-visible`, so there is still no ring at rest (A2).

Comparison: `shots/focus-compare.png`.

**10. The tablet bar is not always one row (A20).** Still open at HEAD.

Where: CSS 48-49 (`flex-wrap`) and 380-388.

How it fails:
- At 641-690px the bar is two rows even before anything is opened.
- At 700-850px it wraps as soon as the Who chip appears. At 768px with Who open, Key drops to a second row and the map shifts down.

Fix: tighten chip padding and gaps between 641 and 900px, or drop the ▾ marks there.

**11. Tradition cards list every connection under "Influenced / transmitted to" or "Influenced by" (C4).** Fixed at HEAD.

Where: 112970-112971.

What is wrong: "broke with", "argued against" and "in contact with" are all listed as influence. HEAD (`ecf2afb0`) now uses "Connections from this tradition" and "Connections to this tradition".

**12. Built worlds say "Open for conversation" in the hover tip and the spoken label, while the card and the Key say "coming soon".** Fixed at HEAD.

Where: `statusLabel` (112671), used at 112452 and 112674. HEAD's `statusLabel` now returns "Conversations coming soon".

**13. In the opening overview, the era title's spoken name says "Opens a note on this era" but it zooms in.** Fixed at HEAD.

Where: 112321 and 112323. HEAD switches the name with the simple view.

### MINOR

14. **A river's Who bubble sits on a place line at zoom 1.8-4.** For example, the Non-Nicene era 1 bubble covers "Athens, Greece · Rome, Italy and beyond" under The Apologists (`shots/ov-1.8-riverwho-pl.png`). The bubble placer's grid has dots and names but no place lines. The prototype check does not measure place lines. Fix: add the shown place-line boxes to the grid before `placeWhoMarks`.

15. **One Escape in a card during connection focus also clears the connections.** The listener at 113351 runs after the panel's own handler (113171-113173) has already closed the card. Fix: skip clearing when the event is already handled (`ev.defaultPrevented`).

16. **Switching a river off leaves its open Who names bright, while its bubble disappears.** The switch code (113259) no longer covers the names; live hid `.who-stack` along with its river. Fix: clear Who when its river is switched off, or dim `#who` and `#who-auto` with it.

17. **A shared link to a non-major tradition opens at 0.6 on a dot with no name.** For example, Cistercians: `focusWorld` (113164-113169) stops at 0.6, where only major names show, and the pinned tradition is not in `lit` (113467). Fix: zoom to 0.8, or force the pinned tradition's name visible.

18. **Dead code left in the live page.**
   - Left behind by this change:
     - `PORTRAIT_DATA` (111522-111534), about 91 KB of base64 that nothing uses.
     - `laneHidden()` (111812).
     - `RIVER_LORE` entries "Greek/Latin bridge" (111587) and "Greek East/Prot. bridge" (111594), about 8 KB that nothing can reach.
     - `openPanel`'s `opts.people` branch (113004): nothing passes it any more.
     - The `{zoom:true}` option passed to `setWho` (112306), which `setWho` ignores.
     - CSS `.across.is-off.is-lit` (151): cross-church movements never get `is-off` now.
     - The touch-screen CSS rule `.who-pill .who-hit{r:…}` (450), overridden by the inline `r`.
   - Already there before this change: `widthAt` (111294), `PLACE_FONT` (111653), `#panel .who-btn:disabled` (420).

19. **The list reopens in the last order chosen, and stays minimised if it was minimised.** `traySort` is global (112148) and `is-low` is never reset. A9 says the list opens by date. The prototype behaves the same way, so this needs confirming rather than fixing.

20. **Escape inside the Rivers, Connections or Key panel hides it while focus is inside, so focus drops to the body** (113313). This was already so before this change. Fix: return focus to the panel's chip.

21. **"Conversations with … are coming soon" appears twice on built-world cards** (112937 and 112999). Already so before this change; fixed at HEAD.

22. **Tablet switches read the tick in their names**, for example "People ✓" (CSS 384). Fixed at HEAD with `content:" \2713" / ""`.

**Count: 13 BLOCKING and 9 MINOR.** At HEAD `dd53c963`, 10 BLOCKING and 7 MINOR are still open.

## Notes beyond the reviewed version

- **The era card at HEAD.** `b5599cff` adds lists of councils, rivers that begin, major people and stories to the era card. A27 says release 44 ships only the information mark, opening "the era notes the map already has", and records Mark's ruling "Map now, cards later". Check this against that ruling.
- **Proposed census values at HEAD.** `ab836b12` commits "proposed major calls … pending Mark's confirmation" into the census. CLAUDE.md says nothing is committed before convergence with Mark.
- **Screenshots and test scripts** are in `scratchpad/r1/shots/` and `scratchpad/r1/scripts/`. The reviewed version is still served on port 8766 and HEAD on port 8767.
