# Round 2 code recheck: Church Family Tree map, direction B

**What I reviewed.**
- Each round 1 finding in `r1-code.md`, rechecked at HEAD.
- The round 2 diff, `git diff 8a54246d HEAD` on `cft-website/index.html` and `cic-website/assets/feedback.js`. `feedback.js` did not change.
- Not counted as findings, as instructed: the era card's lists (a coordinator call) and the proposed census `major` values (held for the preview). I did run every link in the era card for faults.

**HEAD moved four times while I worked.**
- `b2585784`: a census value.
- `bba0637c` and `6712638f`: text fixes.
- `07cb4bd1`: Mark's wording picks.

None of these touches the code behind the findings below. I tested builds of `b2585784` (port 8771) and `6712638f` (port 8772), and re-ran every new finding on `6712638f`. Line numbers refer to `cft-website/index.html` at `07cb4bd1`. Its line numbers match `6712638f`.

**How I tested.** Playwright with Chromium on these screens:
- a 1440×900 desktop, an iPhone 13 and an iPad Mini;
- widths from 641 to 1280px;
- a larger browser text size.

The round 1 build (port 8766) served as the baseline where a comparison was needed.

**Checks that pass.**
- `node tools/validate-census.mjs`: 0 errors, 4 warnings.
- `node --test Build/tools/generate_tree_pages.test.mjs`: 35 of 35 pass.
- `tools/check_live_commentary.py --surface cft-website --base origin/main --enforce`: exit 0, with no REWRITE or ROUTE lines.
- The overlap check at the 12 zoom levels in A16: 0 overlaps at each.
- 2,100 random actions across desktop, phone and tablet, on both builds: 0 runtime errors.

Scripts are in `scratchpad/r2/scripts/` and screenshots in `scratchpad/r2/shots/`.

## Round 1 findings

| # | Sev. | Status | Evidence |
|---|---|---|---|
| 1 | B | **Resolved** | `sizeMarks` 113449-113465: council names 113451; cross-church names, heading, dot and ring; halos and rings from `markU()`. The rings also gained `vector-effect`. Measured at zoom 1.5 to 9: council names and heading at most 16px; cross-church names and heading at most 16px; dot radius 4.1px; tradition ring 13px with a 2px stroke; story ring 25.7px with a 2px stroke. River bubbles' new focus outline breaks the same rule (new finding 3) |
| 2 | B | **Resolved** | Rect hit area that extends away from the house only (112027, 112052-112057). Clicks on a house centre that opened Who: Alexandria at 0.9, 1.5 and 3: 0 of 9, 0 of 5 and 0 of 1. The Desert at 0.9: 0 of 21 (round 1 build: 17 of 21). Wittenberg: 0 of 22 (round 1 build: 4 of 22). Phone: 0 throughout. No other mark's centre (story, council, bubble, cross-church dot, era mark) lands on a figure |
| 3 | B | **Resolved** | `openDeepLink` runs on DOMContentLoaded (113847-113852). `?world=` `desert-monasticism`, `augustine-of-hippo`, `council-of-nicaea-325` and `cistercian-monasticism` all show "This helped" and "Report a problem" on desktop, iPhone and iPad |
| 4 | B | **Resolved** | `returnFocus` (111931) and the announcements. The list's Escape, its × and the chip return focus to the bubble and say "Who list closed." The × and Escape on connections return focus to The Desert and say "Connections cleared." A second press on the opening control is broken (new finding 1) |
| 5 | B | **Resolved** | iPhone: "Show on the map" closes the card and puts focus on the list title (`#trayTitle`, 111949). The list's × then moves focus to a map item |
| 6 | B | **Resolved** | No refit while a card is open (113833), and `zoomToWho` no longer closes the card. With a card open I typed into "Report a problem", then went 390×420, then 844×390, then back. The card stayed open, the text was kept, and focus stayed in the box |
| 7 | B | **Resolved** | `cramped` (111945-111949). At iPad Mini, 700, 820, 900 and 1024px the card closes, focus goes to the list title, and 5 of 5 names show. At 1100 and 1280px the card stays and 5 of 5 names show |
| 8 | B | **Partly resolved** | The tab stop is now re-picked when depth classes change (113466-113470), so Tab reaches the map again in both round 1 cases. But focus still drops to the page body. Cistercians, then "−" four times: body in 6 of 10 runs. Era 5 title, then "+" twice: body in 10 of 10. The recovery (113681) waits a frame and then looks for focus on the body. In Chromium the hidden item still holds focus at that point (instrumented), so the check usually misses. River bubbles hide at 0.30, which is not in the depth key: focus a bubble at 0.36 and press "−" (0.288). Focus goes to the body, the tab stop stays on the hidden bubble, and Shift+Tab from Zoom out skips the map. See also new finding 2 |
| 9 | B | **Partly resolved** | Figures: a gold ring on `:focus-visible` only (260-261, 112050), 10-13px radius, 2px stroke. Good. Bubbles: focus turns the outline gold (262), but its width scales with zoom (new finding 3). A pressed bubble also looks the same with or without focus: gold 1.54px against gold 1.8px at zoom 0.9 (`shots/bubble-states.png`). A pressed bubble with focus is exactly the state after Enter opens the list, since focus stays on the bubble |
| 10 | B | **Resolved** | 391-399. One row at 641, 660, 690, 700, 720, 768, 800, 820, 850, 880 and 900px, with and without the Who chip, for touch and mouse. Nothing is cut off. The Who label shortens with an ellipsis below 744px. Side effect: new finding 4 |
| 11 | B | **Resolved** | "Connections from this tradition" and "Connections to this tradition" (112969-112970) |
| 12 | B | **Resolved** | `statusLabel` (112666): hover tip and spoken label read "The Desert, about 320–430 CE, Conversations coming soon" |
| 13 | B | **Resolved** | The spoken label follows the overview (113479-113482): "Zooms in to this era." at 0.4 and "Opens this era's card." at 0.6 |
| 14 | M | **Resolved** | Place-line boxes join the grid (113522-113526). Bubble over a place line, in 1,213 views at zoom 1.8-4: 0 (round 1 build: 9, including the Non-Nicene era 1 / Apologists case). A16 overlap check: 0 at all 12 zooms |
| 15 | M | **Resolved** | 113381 checks `defaultPrevented`, and the card's Escape calls `preventDefault` (113192). Escape in a card closes only the card |
| 16 | M | **Resolved** | 113303. Switching Latin West off clears its river Who. Switching Alexandria's river off clears that tradition's Who. See note 1 at the end |
| 17 | M | **Resolved** | `focusWorld` goes to 0.8 (113184). `?world=cistercian-monasticism` opens with the name showing on all three devices |
| 18 | M | **Resolved** | Every listed item is gone: `PORTRAIT_DATA`, `laneHidden`, both RIVER_LORE entries, `opts.people`, `{zoom:true}`, `.across.is-off.is-lit`, the touch-screen `.who-hit` rule, `widthAt`, `PLACE_FONT` and `who-btn:disabled`. The change left new dead code (new finding 6) |
| 19 | M | **Resolved** | Reopening resets to "By date" and full size (111942) |
| 20 | M | **Resolved** | Escape inside the Rivers, Connections or Key panel returns focus to that panel's chip (113334-113339) |
| 21 | M | **Resolved** | "Coming soon" shows once on The Desert and Wittenberg cards, and not at all on Cistercians |
| 22 | M | **Resolved** | Chrome reads the tablet switches as "People", "Stories" and "Councils". The rule has no fallback (new finding 5) |

**Count:** 20 resolved, 2 partly resolved (8 and 9, both BLOCKING), 0 open.

## New findings

### BLOCKING

**1. A second press on the same Who control leaves the list stuck open. After that, the list's ×, Escape and the chip do nothing.**

Where: `setWho` at 111940-111941, and `clearWho` at 111952-111953.

What is wrong: when the scope is the same, `setWho` sets `whoScope=null` first, then calls `clearWho()`. `clearWho` starts with `if(!whoScope)return;`, so nothing is rendered.

```js
whoScope=whoScopeKey(scope)===whoScopeKey(whoScope)&&!(opts&&opts.on)?null:scope;
if(!whoScope){clearWho();return;}        // clearWho: if(!whoScope)return;
```

How it fails:
- Click a river's Who bubble, then click it again. Or press "Show on the map" in a card, then "On the map ×". Or press Enter twice on a figure.
- Every time, the list stays open, the names stay on the map and the bubble stays pressed. The card button still reads "On the map ×", and the status line still says "Who list open…".
- From there the list's ×, Escape in the list and the chip all do nothing, because each calls `clearWho()`, which now returns at once.
- Reproduced on desktop and iPhone at `b2585784` and `6712638f`.
- Random actions reached this state on every device: 66, 20 and 77 of 300 steps on desktop, phone and tablet.

This is a regression from the round 1 fix. Before it, `setWho` called `renderWho()` on toggle-off.

Fix: decide the toggle before changing state.

```js
if(whoScopeKey(scope)===whoScopeKey(whoScope)&&!(opts&&opts.on)){clearWho();return;}
const wasOpen=!!whoScope; whoScope=scope;
```

**2. Focus is pulled into the map from the page body, and the item that receives it shows a gold ring or a tooltip.**

Where: `syncMapStop` 113672, 113681 and 113683, which now runs on every depth change (113468-113469). The focus handlers it triggers are at 112355 (river tooltip), 112506 ("continued as" tooltip) and 112488, 112545 and 112604 (rings). None of them checks `:focus-visible`.

What is wrong:
- `hadFocus` is true whenever focus is on the page body. So when zoom hides the tab-stop item, focus moves into the map even though the user never put it there.
- The check runs a frame late. So it usually misses the case it was written for (finding 8), yet catches a body that was never in the map.

How it fails:
- **Mouse, desktop.** Click Cistercians, close its card, then click the page title. Focus is now on the body, and ArrowDown pans the map. Ctrl+scroll out to the overview. Focus jumps to "Who: Latin West, era 5". ArrowDown now moves focus between bubbles and no longer pans.
- **All positions.** The same set-up at 57 traditions spread over the map: focus moved into the map in 57 of 57. In 18 of them a gold ring showed on a tradition, or a river or "continued as" tooltip appeared.
- **Touch, iPad.** Tap an era title in the overview. In 2 of 16 runs, focus jumped to Last Christian Nubia (gold ring) or to the Non-Nicene river. The river's tooltip "Non-Nicene, 31 traditions · 120–2010" was left floating over empty map (`shots/tap-era-tooltip-tablet.png`).

Fix, which also completes finding 8:
- Recover focus synchronously, at the point where the depth classes and Who marks change: in `labelFitRun`, after `syncDepth()` and `placeWhoMarks()`.
- Recover only if `document.activeElement` is a map item inside the SVG that `mapItemShown` now reports hidden. Then focus the nearest shown item. Chromium has not yet blurred the item at that point, so the race goes away.
- Never move focus when it is on the body or outside the map.
- Recover only if the lost item matched `:focus-visible`, so a tap that happened to focus a title does not cause a tooltip.
- Add `Z_RIVER_WHO` to the depth key.

**3. The river bubble's focus outline grows and shrinks with zoom (A17).**

Where: CSS 262, `.who-pill:focus-visible .who-cap{…stroke-width:2px!important}`. `.who-cap` has no `vector-effect`. At rest its width comes from `U*.11` (112044) and stays near 1.5-2px.

What is wrong: the focus width is 2 map units. On screen it is 0.7px at 0.35, 1.8px at 0.9, 6px at 3 and 18px at 9. Measured with `:focus-visible` on.

How it fails:
- At zoom 9, the 18px gold stroke fills a 25px bubble, and the count is barely legible (`shots/bubble-focus-z9.png`).
- In the overview (0.35), the focus outline is 0.7px, half as wide as the 1.5px outline at rest.

Round 1 counted growing focus rings as BLOCKING under A17 (finding 1).

Fix: draw the bubble's focus mark like the figure's: a separate outline about 2-3px outside the capsule, with `vector-effect:non-scaling-stroke`, a 2px stroke, shown only on `:focus-visible`. It then looks the same at every zoom, and it also separates focus from the pressed state (the rest of finding 9).

### MINOR

**4. Tablet bar: the ticks spill past their chip outlines.**

Where: 391-399. `flex-wrap:nowrap` lets the layer chips shrink below their content.

How it fails: with the Who list open, the ticks of People, Stories and Councils sit 9px past the chip border at 641-700px and 4-5px past at 720px. With a 20-24px browser text size, they sit 11-13px past at 768-820px (`shots/bar-641-who.png`, `bar-768-font20-who.png`). The round 1 build wrapped instead.

Fix:
- Keep the layer chips at their content width (`.feature-bar .chip:not(.who-chip){flex-shrink:0}`), so only the Who chip gives way.
- Let the bar wrap only when it still cannot fit, as with a large text size.

**5. The tick declaration has no fallback.**

Where: 387, `content:" \2713" / ""`.

What is wrong: a browser that does not support alternative text in `content` drops the whole declaration. Firefox added support only in version 128. Such a browser shows no tick at all, so "on" is shown by colour alone (A20 asks for a tick and gold).

Fix: put `content:" \2713";` on the line before it.

**6. New dead code.**
- `let connOpener=null;` (113350) is never read.
- `openPanel`'s `opts` parameter (112922) is no longer used, and no caller passes it.
- Blank lines are left inside `RIVER_LORE` (111578-111579, 111594) where entries were removed.

Fix: remove them.

**Count:** 3 BLOCKING and 3 MINOR, all new. Of the round 1 findings, 2 BLOCKING are still partly open (8 and 9).

## Notes outside this round's scope (already in the round 1 build; not counted)

1. On desktop, with the Who list open, the Rivers panel opens under the list. 15 of 16 river switches cannot be clicked (z-index 26 against 25). This matters for finding 16's fix, which acts on those switches.
2. On a phone, a river Who whose name column lies far to the right of its traditions leaves most names off screen. Latin West, era 1: 1 of 4 names in view (round 1 build: 1 of 2). The fit stops at 0.85. The list holds every name.
3. At 641px the Connections panel runs 16px past the right edge (round 1 build: 58px).
