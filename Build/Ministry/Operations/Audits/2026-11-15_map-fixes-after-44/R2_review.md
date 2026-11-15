# Round 2 review: map fixes after release 44 (targeted recheck)

Reviewer: a fresh Opus agent that had not seen the work. It made a targeted recheck of commit f663f169 (the round 1 fixes) against `R1_review.md` and `R1_changes.md`. It ran `node --test Build/tools/tree_map_view.test.mjs` (17 of 17 pass) and wrote no files; the worker recorded its findings here as handed back. WebKit cannot run here.

**Verdict: PASS WITH MINOR.** No blocking points.

## Round 1 findings

1. Rotation and detail level: resolved. `clampView` reports a rescale and `applyTransform` then calls `applyDetail()`. There is no recursion, and no double work during a pinch or `zoomAt`, which clamp before `applyTransform`. The test fails on the old code.
2. Mark after the era strip: resolved in code (`syncEraStrip` before `pinEraCaptions`), but the new test does not catch it (finding 2).
3. Measuring work: partly resolved. The ResizeObserver guard is right; the "one layout per run" claim is not (finding 1).
4. Who list closing: resolved. `renderTray` calls `applyTransform()`. No loop through `queueAutoWho`, `autoWho` or `renderWho`, and no new focus or scroll effect. The test fails on the old line.
5. The iPhone floor: handled as asked, and going to Mark. The test's either/or bound is safe, because the next assertion rules out a floor above the width fit.
6. Hover effects on touch: resolved. `hoverInput()` gates the river, story, edge, across and council `mouseenter` effects; every other `mouseenter` only calls the gated `showTip`. Mouse users lose nothing, because `pointerover` sets the input before `mouseenter`. Pinned movements still work from the click.
7. Pinch over the map's controls: resolved, apart from the Key panel (finding 3). Only two-finger touches are cancelled. The cards and the Who list are outside all seven targets.
8. Tests: resolved, apart from finding 2.

The ResizeObserver guard holds. For SVG, `contentRect` is the bounding box in local units, the same space as `_drawnW`. A zoom frame matches and is skipped, and a font swap is far larger than half a pixel. `_drawnW` is set before the first callback, because `render()` pins the captions through `renderWho()` right after it observes the titles.

## Findings

1. **MINOR.** `pinEraCaptions` still alternates reading and writing, one era after another (`cft-website/index.html:121661–121665`). It reads one title's `getBBox()`, writes that mark's transform, then reads the next title. Drag, pinch and glide can still force up to 10 layouts a frame, so R1_changes item 3's "one layout per run" is not true. Fix: read every box first, then write every mark, and correct the wording.
2. **MINOR.** The zoom-back-out-across-the-strip test cannot catch the fault it was added for. `markGaps` waits two frames before it measures, and in that time the observer re-pins. The test would pass with the old order. Fix: measure in the same `evaluate` as the zoom, before any frame.
3. **MINOR.** A pinch on the Key panel can no longer zoom the page (`cft-website/index.html:122064`; the panel is built near 121513). Every `.chip-panel` sits inside `.feature-bar`, and on phones the Key panel is a text sheet up to 60vh tall. `ownPinch(.feature-bar)` cancels the pinch there, so a reader cannot enlarge that text, though round 1 said to leave text surfaces alone. Fix: skip the cancel inside `.chip-panel`.
