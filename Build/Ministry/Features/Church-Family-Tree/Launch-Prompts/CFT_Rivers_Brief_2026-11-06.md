# Brief — rivers that swell, thin and drift (decided by Mark, 2026-11-06)

For the Church Family Tree build thread. Recorded here as Mark gave it.

## Decision

Mark chose Option 1, and asked to "keep the river feel, not the harshness". The map's
existing, honest signals become visible:
- **Width** shows how many documented movements in a family are active in a given year.
- **Rivers drift** toward or away from each other only along documented census links.

Log this in `Build/Ministry/Features/Atlas-World-Map/Decision-Log.md` as a new 2026-11-06
entry before building.

## The feel (the main constraint)

- **Water, not a chart.** Every change of width or position eases in and out over decades.
  - No kinks, corners or sudden jumps.
  - No line bends sharply toward a link point.
- **Swelling.** Rivers swell and thin gradually, the way a real river widens below a confluence.
- **Leaning.** Rivers lean toward or away from each other; they don't snap. A pull or push
  builds slowly, holds, then relaxes.
- **No crossing.** Rivers never cross or touch a neighbor's water. Keep a clear gap even at
  the strongest pull.
- **Keep what's there.** Keep the seeded winding wave (`seededWave`), the smooth path building
  (`smoothPath`) and the organic phase at close zoom. The new motion rides on top of the
  river's own meander; it doesn't replace it.
- **Compare before shipping.** Take screenshots at full-map zoom and close zoom and compare
  them with the current map. If anything looks mechanical or zig-zag, smooth it further.
- **Mark judges the feel** by eye on the preview before merge.

## Honesty rules (non-negotiable; `CLAUDE.md`, "never invent")

- **Width means documented activity:** the count of census movements in that family active
  in that year.
  - It does not mean membership or size. No population numbers exist.
  - The legend says exactly this, for example: "Width: how many documented movements were
    active."
- **Drift uses only census edges** (`cic-website/data/world-census.json`, `edges`), and only
  over the years both movements overlap. No hand-placed bends and no narrative nudges.
- **Each link's pull is weighted by its confidence grade.** Starting values:

  | Grade | Weight |
  |---|---|
  | Documented | 1 |
  | Widely Accepted | about 0.7 |
  | Dominant Modern Reconstruction | about 0.7 |
  | Contested | about 0.4 |
  | Inferential-Thin | about 0.25 |

  Record the final values in the decision log.

## What to change (in the map file)

1. **Width.**
   - `widthAt()` now returns `10 + 46*(cnt/maxCnt)^0.55`, which is 10 to 56 px. Widen the
     range so growth and decline read clearly: a thin trickle at one active movement, several
     times thicker at the peak. Tune the exponent and range by eye.
   - Smooth the per-lane count samples (`laneSamples`) along time, for example with a moving
     average over a few decades, so the count swells rather than stepping each time a
     movement starts or ends.
   - Keep "no floor": a lane with nothing active has zero width.
2. **Drift** (`driftEdges`, `driftInfluence`, `driftOffset`, `DRIFT_MAX = 32`).
   - **Pull together:** "gave rise to", "continued as" and "influenced" (green and brown),
     plus "in contact with" (gray) at reduced strength.
   - **Push apart:** "argued against" and "broke with" (red).
   - **Genesis convergence:** lineage types currently drive only the genesis/parent
     convergence. Adding them as attraction is intended now, but check that this doesn't
     double-draw the parent convergence at a lane's genesis.
   - **Weights:** multiply each link's strength by its confidence weight.
   - **Strength:** raise `DRIFT_MAX` well above 32, and keep the `tanh` saturation, so many
     overlapping links ease toward the cap.
   - **Gap:** add a hard minimum gap between neighboring lanes' edges, computed from both
     widths, so no river crosses another.
   - **Fade:** lengthen the smoothstep fade in `driftInfluence`, which is now the first and
     last fifth of the overlap, so pulls build and relax gently.
3. **Link endpoints.** Links are drawn from node positions (`m._x`, `m._y`). If nodes ride the
   drifted, widened river, check that the links still attach to their dots.
4. **Legend.** Under Tradition families, add two short notes in plain words:
   - "Width: how many documented movements were active."
   - "Rivers lean together or apart along documented links."
5. **River switches.** The legend switches from mchadwick25-droid/CIC-Project#1521
   (`data-lane`, the `is-off` class) must keep working. A hidden river must not leave its pull
   on other rivers. Either recompute the drift without the hidden lanes, or document plainly
   that the geometry doesn't change when a river is hidden.

## Process

- **Branch.** Start from current `main`. mchadwick25-droid/CIC-Project#1517, #1521 and #1524
  are merged: the colors, the switches and the thicker lines are already there.
- **One pull request.** Run `tools/check_live_commentary.py --base origin/main --enforce` and
  `tools/check_spelling.py` on the edited files.
- **Browser check in Chromium:**
  - full-map zoom and close zoom, in both dark and light themes
  - a phone width
  - no page errors
- **Mark's review.** Post the screenshots or the Cloudflare branch preview link for Mark to
  judge the feel before merging.
- **Census untouched.** The census data does not change, so `tools/validate-census.mjs` and
  the atlas edge-sync check should stay green without edits.

## What exists (for orientation)

- **Rivers per family:** lanes are keyed by `laneOrder`, with colors in `FAM` / `famColor`.
- **Width:** `laneSamples` and `widthAt`.
- **Drift:** `ATTRACT_TYPES` / `REPEL_TYPES`, `driftEdges` and `driftOffset`.
- **Link colors:** the `--link-*` tokens. Link families: `LINK_FAMILY`.
- **Where drift shows:** the census has 86 links, so drift appears only where links exist.
  That is expected, not a bug.
