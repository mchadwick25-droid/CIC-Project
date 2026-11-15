# Round 3 code recheck: Church Family Tree map, direction B

**What I reviewed.**
- Each round 2 finding in `r2-code.md`, and its two partly resolved round 1 items (8 and 9), rechecked.
- New faults only in `r3.diff` (`git diff b2585784 c49b38bf`). Unchanged code was not re-reviewed.
- Not counted, as instructed: the era card's data-only lists, the census `major` values held for Mark, and wording Mark picked.

**HEAD moved five times while I worked.**
- `618d3ab5`: switch panels (a `z-index` and a left shift). Not in `r3.diff`. See note 1.
- `878dc40d` and `56c1bb2a`: merges of release 43, plus `major` and `activeYear` for its 60 era 4 people. Data only.
- `fce4306b`: round 3 text fixes, with two small code edits (a `plainDates` rule and the river card's era line). I checked both. All 15 river cards render, and their era lines match their spans.
- `ea0e8fd6` and `62f68adf`: records and notes.

The code behind every finding below is the same at `c49b38bf` and at `62f68adf`. Every finding was reproduced on builds of `618d3ab5` (port 8775), `878dc40d` (8776) and `62f68adf` (8777). Line numbers refer to `cft-website/index.html` at `62f68adf`. The round 2 build `b2585784` (port 8771) was the baseline.

**How I tested.** Playwright with Chromium on these screens:
- a 1440×900 desktop, an iPhone 13 and an iPad Mini;
- widths from 320 to 1280px;
- browser text sizes of 16 to 24px.

**Checks that pass at `62f68adf`.**
- `node tools/validate-census.mjs`: 0 errors, 4 warnings. The `878dc40d` merge alone had 120 errors; `56c1bb2a` cleared them.
- `node --test Build/tools/generate_tree_pages.test.mjs`: 35 of 35 pass.
- `tools/check_live_commentary.py --surface cft-website --base origin/main --enforce`: exit 0, with 0 REWRITE and 0 ROUTE.
- 1,500 random actions (500 each on desktop, phone and tablet): 0 runtime errors, and 0 steps with the list stuck open.
- Every new `plainDates` use, the river spans and every river and era card: no `NaN`, `undefined` or `Infinity`.

Scripts are in `scratchpad/r3/scripts/` and screenshots in `scratchpad/r3/shots/`.

## Round 2 findings, and round 1 items 8 and 9

| # | Sev. | Status | Evidence |
|---|---|---|---|
| 1 | B | **Resolved** | `setWho` now decides the toggle before it changes state (120231). On desktop, iPhone and iPad, a second click or tap on a bubble closes the list. "Show on the map" then "On the map ×" also closes it: the button and the status line reset, and the status reads "Who list closed." After reopening, the list's ×, Escape and the chip each close the list and return focus to the bubble. Random actions reach the stuck state in 0 of 1,500 steps (round 2: 66, 20 and 77 of 300). Keyboard users still cannot make the second press, because focus leaves the control on the first press (new finding 1) |
| 2 | B | **Partly resolved** | Fixed: focus is no longer pulled in from the body. In the round 2 sweep, focus stays on the body in 57 of 57 positions, with no ring or tooltip (round 2: 57 moved, 18 with a ring or tooltip). ArrowDown still pans after Ctrl+scroll. Still open: the `:focus-visible` condition from the round 2 fix was not added, so a tap or click on an era title in the overview always moves focus into the map. **Touch:** 16 of 16 runs (round 2: 2 of 16). Over all ten eras on iPhone and iPad, focus moves every time. In 5 of 10 per device a gold ring shows (eras 1 and 2), or a tooltip floats over the map: "Non-Nicene, 31 traditions · 120–2010" (era 7) or the Georgian Church "continued as" tip (eras 9 and 10). **Desktop click at zoom 0.4:** focus moves in 5 of 5 (round 2 build: 3 of 5), with a ring or tooltip in 3 of 5. **Cause:** `goIntoEra` (121445) zooms to 0.9. `strip-on` then hides `#era-labels` (CSS 306). `keepMapFocus` (121833) sees the tapped title hidden and focuses the item nearest the centre. Its focus handler shows a tooltip or ring on any focus (120649, 120782, 120800, 120839, 120898). **Fix:** in `labelFitRun` and `applyTransform`, record `held.matches(':focus-visible')` together with `held`. `keepMapFocus` acts only when that is true. Depth changes already re-pick the tab stop, so Tab still reaches the map. Tried in the page while it ran (no repo edit): era-title taps on iPad left focus on the body with no tooltip in 4 of 4 and a shown tab stop, and the keyboard case (era 5 title, then "+" twice) still recovered |
| 3 | B | **Resolved** | The new `.who-focus` rect (CSS 262-263; `setWhoMark` 120339) is a 2px gold stroke that does not scale, shown only on `:focus-visible`. Measured at zoom 0.31, 0.35, 0.9, 1.5, 3, 6 and 9: 2px at every zoom, 4.1-5.4px outside the capsule. The capsule's own stroke is unchanged (1.54-1.98px). It does not show after a mouse click |
| 4 | M | **Resolved, with a regression** | The ticks fit: nothing spills past a chip at 641-900px with the Who list open (round 2: 4-9px at 641-720px). But no chip except Who can shrink now, and the bar still cannot wrap. The Key can be pushed off screen (new finding 3) |
| 5 | M | **Resolved** | `content:" \2713";` now comes before the alt-text form (388). The tick renders as before in Chromium |
| 6 | M | **Resolved** | `connOpener`, `openPanel`'s `opts` and the blank lines in `RIVER_LORE` are gone. This change left one new unused variable (new finding 4) |
| R1-8 | B | **Partly resolved** | The named cases now keep focus on a shown item. **Cistercians, then "−" four times:** 0 of 10 runs lost (round 2: body in 6 of 10). **Era 5 title, then "+" twice:** 0 of 10 (round 2: 10 of 10). **Bubble at 0.36, then "−" (0.288):** focus moves to Bethlehem Circle, the only tab stop, which is shown, and Tab from the page start reaches the map. Still open, and worse than round 2: focus on a name in the Who layer drops to the body on every zoom step (new finding 2) |
| R1-9 | B | **Resolved** | A pressed bubble has a gold capsule. Focus adds a separate outer ring, so "pressed" and "pressed with focus" now look different (`shots/bubble-states.png`). The figure's ring is unchanged (`shots/figure-states.png`) |

**Count:** 5 resolved (1, 3, 5, 6 and R1-9), 1 resolved with a regression (4, see new finding 3), and 2 partly resolved (2 and R1-8, both BLOCKING; the rest of R1-8 is new finding 2).

## New findings

### BLOCKING

**1. Pressing a Who control moves focus off it, by keyboard, mouse or touch. A second Enter then opens a different tradition's card.**

Where: `renderWho` (120212-120220). Inside it, `labelFitRun()` (120215) runs before `syncWhoControls()` (120217). `labelFitRun` now ends with `keepMapFocus(held)` (121827). While `who-on` is set, CSS 265 hides every Who control whose `aria-pressed` is not "true".

What is wrong: at the moment `keepMapFocus` checks, the pressed control still has `aria-pressed="false"`, so it is `display:none`. `keepMapFocus` treats it as hidden and focuses the item nearest the window centre. Then `syncWhoControls` sets `aria-pressed="true"`, and the control shows again, without focus.

Instrumented during an Enter on the bubble:
- inside the press, the bubble reads `display:none`, `aria-pressed` "false", `who-on` true;
- afterwards it reads `inline`, pressed, but focus is on Anglo-Saxon England.

How it fails:
- **Every press moves focus.** Test cases: the Latin West era 4 bubble and the Alexandria figure, pressed by Enter and by click or tap, on desktop, iPhone 13 and iPad Mini. Focus left the control in 12 of 12 (round 2 build: 0 of 12). It lands on a nearby tradition: Anglo-Saxon England for the bubble, the Alexandria house for the figure.
- **A mouse or touch user sees a stray ring.** The tradition that takes focus shows its gold ring and the browser's white focus outline, even after a click or a tap (`shots/click-bubble-node-compare.png`).
- **Keyboard:** a second Enter does not close the list. It opens the card of the tradition that took focus: Anglo-Saxon England, or Alexandria (6 of 6). For keyboard users this undoes the toggle that round 2 finding 1 fixed.

Fix: set the pressed state before the layout pass. In `renderWho`, call `syncWhoControls()` before `labelFitRun()`. It reads only `whoScope` and the DOM.

I tried this fix in the page while it ran, without editing the repo (`scripts/r3-fixcheck.js`). Focus stayed on the bubble after Enter and after a click, and a second Enter closed the list.

**2. Zooming while a Who name has focus drops focus to the page body. This is a regression from round 2.**

Where:
- `syncMapStop` (121976): this change removed its recovery (the `hadFocus` and `lost` lines).
- `keepMapFocus` now runs only at the end of `labelFitRun` and `applyTransform`.
- The names are rebuilt later in the same frame: `drawWhoNames` clears `#who` (120148) from the `whoRaf` callback (121847), and `autoWho` clears `#who-auto` (120391, 120399).

How it fails:
- **River list names.** Open a river's Who list, focus a name on the map, and press "+" or "−". Focus goes to the body in 12 of 12 steps over four lists. In the round 2 build it was 0 of 12: focus moved to a nearby story.
- **Automatic names from zoom 2.2:** 6 of 6 steps (round 2 build: 0 of 6).
- **Enter on an automatic "+N more"** (for example "5 more people of Alexandria"): the list opens and focus goes to the body (round 2 build: the Alexandria figure). Opening the list makes `autoWho` clear `#who-auto`.
- Tab reaches the map again afterwards, since the tab stop is re-picked. But the user loses their place, and nothing is announced.

Fix: carry focus across the rebuild.
- In `drawWhoNames` and `autoWho`, note the focused name's `data-key` before clearing.
- After rebuilding, focus the new name that has the same key (`preventScroll`).
- If there is none, call `keepMapFocus` with the old element. A detached element reads as hidden, so the nearest shown item takes focus.
- For the automatic "+N more", move focus to the list's first row once it opens, as the river list's "+N more" already does.

**3. Tablet bar: with a larger browser text size, the Key runs off screen.**

Where: CSS 389, `.feature-bar .chip{flex-shrink:0;white-space:nowrap}`, together with 394, `flex-wrap:nowrap` (641-900px). Only the Who chip (399) can give way now.

How it fails (round 2 build in brackets):
- **20px text, 641px wide:** the Key chip is entirely off screen and cannot be tapped [56 of 75px showing, tappable].
- **24px text, 768px wide, Who list open:** the Key is entirely off screen [59 of 85px showing].
- **24px text, 768px wide, list closed:** 14 of 85px showing [nothing cut].
- **700px with 20px text, 768px with 22px, 820px with 24px:** the Key loses 13-49px [nothing cut].
- **Side effect, MINOR:** at the default text size with the Who list open, the Who chip's label shrinks to 0px at 641px, leaving only "×" [45px], and to 15px at 660px [64px]. The tray's own title still names the list.

Screenshots: `shots/bar-compare.png` (round 2 build above, HEAD below).

This is the half of round 2's fix for finding 4 that was not done: "let the bar wrap only when it still cannot fit".

Fix:
- Keep the layer chips at their content width, as now.
- Add a measured fallback wherever the bar's content can change: `positionFeatureBar` (it already runs on resize and from the ResizeObserver) and `syncWhoControls`.
- In that check, remove a class such as `is-tight`, then add it back only if `bar.scrollWidth > bar.clientWidth + 1`. Measuring with the class off keeps it from flipping on and off.
- Style it with `.feature-bar.is-tight{flex-wrap:wrap}`.

At the default text size the bar stays one row, so A20 holds. At larger sizes the Key moves to a second row instead of off screen.

### MINOR

**4. New dead code.** `const years=members.map(m=>m.start);` (120635) is no longer read, because `tipForRiver` now takes `riverSpan(members)` (120636). Fix: remove it.

**Count:** 3 BLOCKING and 1 MINOR, all new. Round 2 finding 2 and round 1 item 8 are still partly open (both BLOCKING). New finding 2 is the open part of R1-8.

## Notes outside this round's scope (not counted)

1. **`618d3ab5` does not lift the switch panels above the Who list.**
   - The panel's `z-index:27` applies inside `.feature-bar`, which is `position:fixed; z-index:20`. That makes the bar its own stacking context, so the whole bar, panel included, stays under the tray (`z-index:26`).
   - Desktop, with the Who list open: 1 of 9 visible river switches is on top, as in round 2. A click on the third switch lands on the tray and closes the panel (`shots/rivers-panel-under-tray.png`).
   - Fix: raise `.feature-bar` above the tray (check what else sits between 20 and 27).
   - The commit's other fix works: at 641px the Connections panel now ends at 633px (round 2: 657px).
2. At 901px, with a river's Who chip showing, the bar wraps to two rows. The round 2 build does the same.
