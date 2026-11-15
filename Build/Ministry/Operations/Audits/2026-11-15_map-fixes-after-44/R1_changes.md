# Round 1 changes: map fixes after release 44

All eight round 1 findings (all MINOR) are handled. Line numbers are in `cft-website/index.html` after the change.

1. **Rotation and detail level.** `clampView` now reports when it changed the scale, and `applyTransform` then calls `applyDetail()`. That covers resize and rotation, and any other path where the clamp, not the caller, moves the zoom across the detail threshold. Test: "turning the phone re-applies the floor, the clamp and the detail level".
2. **Mark after leaving the era strip.** `applyTransform` now runs `syncEraStrip()` before `pinEraCaptions()`, so the titles are drawn again before they are measured. Test: "the era mark is right after zooming in past the era strip and back out", on both screens.
3. **Measuring work.** `pinEraCaptions` now writes every title and date first, then reads every title's box, then places the marks, so it forces one layout per run instead of one per era. The ResizeObserver re-places only when a title's size differs by more than half a screen pixel from the size last measured. It no longer runs a second time on every zoom frame.
4. **Who list closing.** `renderTray` calls `applyTransform()` instead of `pinEraCaptions()`, so the clamp follows the map area as the list opens and closes. Test: "closing a Who list re-applies the clamp" (it fails with the old line: 700 px empty of 1440).
5. **The iPhone floor.** No code change. The floor is the lower of 0.9 × the opening zoom and the zoom where the tree's width fits the screen. That gives 0.454 on desktop (0.9 × 0.504) and 0.183 on iPhone 13, where the width fit is lower than the opening zoom (0.391). On a phone the brief's two parts cannot both hold, because the opening zoom is raised to 0.391 and the tree is wider than the screen there. The choice goes to Mark in the report and the pull request. The test now checks the rule itself instead of a loose bound.
6. **Hover effects on touch.** The gate is now `hoverInput()`. It covers the hover effects as well as the tip: the house halo and lit river, the story halo, the edge highlight, the person and council lights. A touch tap now changes nothing on hover, so WebKit has no hover content change to hold the click for. That is not checked on a device.
7. **Pinch over the map's controls.** One function, `ownPinch`, cancels a two-finger touch start and Safari's gesture events. It is applied to the stage, the era strip, the connections chip, the zoom controls, the zoom hint, the top bar and the bottom bar. Page zoom still works on cards, the Who list and the text pages. The stage's own touchstart is passive again, as on main. `touch-action:none` on the stage was already on main; the second commit's message was wrong to imply it was added.
8. **Tests.** Added: rotation, closing the Who list, zooming across the era strip, and keyboard focus still showing a tip. The test box now comes from the map's own transform (`getScreenCTM`) at 2 px slack. The test stays local-only: CI has no browser job (Playwright in CI is the open P1-8 item). This is logged in Open-Gaps with the WebKit gap. The late-font test needs `fonts.gstatic.com`, as the live page does.

**Checks after the changes.**
- **Tests:** 17 of 17 in `Build/tools/tree_map_view.test.mjs`.
- **Release 44 checks:**
  - Overlaps are 0 at the A16 zooms.
  - With a Who open, all 29 river-eras show 0 overlaps on desktop and iPhone 13, with the same off-screen counts as main.
  - Keyboard focus-stepping and the zoom-to actions match main.
