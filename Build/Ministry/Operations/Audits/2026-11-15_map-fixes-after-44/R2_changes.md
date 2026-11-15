# Round 2 changes: map fixes after release 44

All three round 2 findings (all MINOR) are handled.

1. **One layout per caption pass.** `pinEraCaptions` now runs three loops: it writes every title and date, then reads every title's box into an array, then writes every mark. A run now forces one layout, not one per era. Round 1's changes said this before it was true; it is true from this commit.
2. **The era strip test now catches the old order.** It zooms and measures in the same `evaluate`, before any frame and so before the observer can re-pin. Chromium still gives a hidden title its real box, where WebKit is expected to give an empty one, so the test models WebKit: a `getBBox` with no rendered box returns zero width. With the old order (captions measured before the strip is turned off) it fails, with the mark 211 px inside the title. With the fix it passes.
3. **The Key panel keeps page zoom.** `ownPinch` leaves the pinch alone when it starts inside a `.chip-panel`. The bar's chips and buttons still own the pinch, and the panels' text can still be enlarged. The tap test checks that a gesture on a bar panel is not cancelled.

**Checks.** 17 of 17 in `Build/tools/tree_map_view.test.mjs`. Round 2 is the last review round needed: no blocking point is open, and this round's three minor points are fixed as the reviewer asked.
