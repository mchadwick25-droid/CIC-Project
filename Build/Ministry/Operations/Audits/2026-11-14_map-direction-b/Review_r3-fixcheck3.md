# Round 3 fix check 3: `d4588fbf` to `a9302d0b`

**How I tested.** I built base and head from `git archive` copies with `node tools/build_tree_site.mjs`, served on ports 8896 and 8897. Playwright Chromium ran on desktop, iPad Mini both ways and iPhone 13, at 16, 20 and 24px. All POSTs were mocked. Scripts and logs: `/tmp/claude-0/fc3/`.

## 1 (BLOCKING), a key per card: Fixed
- All 1,696 cards, of nine kinds, use 1,696 different keys. Base: 1,077 shared `atlas-v3`.
- All 1,696 sent keys pass the route's own pydantic rule.
- I liked one card of each of eight kinds, by click and by tap. Each like carried that card's key, and so did a report. The 98 other cards I checked stayed unmarked, before and after reload. Base: one river like marked 65 others.
- No map control opens a named-voice card now. I opened those by code.
- **New, MINOR:** one connection key is 124 characters. `feedback.js` cuts it to 120. It still posts and stays unique, but no longer names its edge in full. Edge ids join two ids, so more can come.

## 2 (BLOCKING), Latin Pastoral sentence: Fixed
- Gone from the census and the map. `atlas-check` passes.
- 0 of 1,696 cards show build-status wording. Base: 1.
- Census validator, quick and full: 0 errors, 4 warnings, as in base.

## 3 (MINOR), open panels after reflow: Fixed
- 4,341 checks over three text sizes: 3,276 resizes, 180 turns, 741 Who chip arrivals and exits (351 by a real click or tap), 144 text-size changes.
- Head: 0 faults. Each panel lands where a fresh open puts it, 8px inside both edges. Base: 1,249 faults, worst 263px off screen.
- The earlier iPad case (Key panel, 24px, turned to landscape): base 249px past the edge, head 22px inside.

## 4 (MINOR), "This helped" by keyboard: Fixed
- On the map (desktop, iPad) and four tree pages, focus stays on the button after Enter or Space. It reads as pressed.
- More presses send nothing, even mid-POST.
- After a 500 or a network failure, the button works again and keeps focus.
- After reload the liked button stays in the Tab order. Escape still closes the card.
- Base: focus fell to the page body every time.

## 5 (MINOR), Who list order: Fixed
- I set a river list to "By tradition", then opened each of the 103 Who lists. All 103 opened by date, and their first rows matched the hover tip. Base: 0 reset, 12 differed.
- The same list asked for again keeps its order.
- The map hides other Who marks while a list is open, so only code reaches this path.

## 6 (MINOR), spoken places: Fixed
- 350 of 350 tradition labels read "Name, dates. Place; place". No empty parts. The other 958 labels are unchanged.

## Not regressed
- 1,800 panel opens, every 8px from 641 to 1440, land exactly where base puts them.
- The bar fits right at all 4,341 checks.
- Focus return and the form (Report, Escape, Send, failed Send) match base.

## Dead code and errors
- ESLint: no new unused code.
- 300 random actions on desktop and 300 on iPhone 13: 0 broken rules, 0 errors, no duplicate likes. No page errors in any run.

## Seen, not new
- A failed Send by keyboard drops focus to the page body, in head and base. Send still uses `disabled`, the cause item 4 fixed.

**Count.** All six fixed at the root. 1 new MINOR. No regressions.
