# Round 3 fix check: `a602e437` to `1e3d37c8`, `cft-website/index.html`

**How I tested.**
- I built both commits in my own worktrees.
- Playwright Chromium: a 1440×900 desktop, `iPad Mini` (both orientations), `iPhone 13`, and every bar width from 641 to 1440px.
- Text sizes of 16, 20 and 24px, set with the CDP call `Page.setFontSizes`. That is the browser's own default font size.
- Real mouse, touch and key input. Web fonts load.
- Scripts are in `/tmp/claude-0/fc/` and shots in `/tmp/claude-0/fc/shots/`.
- The branch moved on to `aea7d944` while I worked. Its `index.html` changes touch none of this code, so every finding below still applies.

## The six fixes

**1. Fixed.**
- Tested on the Latin West era 4 bubble and the Alexandria figure, by Enter, Space and click or tap, on three devices.
- Focus stays on the control in 18 of 18 presses (base: 0 of 18).
- A second press closes the list in 17 of 18. A click or tap leaves no ring.
- The miss: on the iPhone the pressed bubble ends up under the tray. Base does the same.

**2. Fixed.**
- **River names** under "=" and "−": the same name keeps focus in 24 of 24 steps (base: the body each time). The "+N more" keeps it in 30 of 30.
- **Automatic names:** the same name keeps focus in 30 of 33 steps. In the other 3, another shown name took focus. Base: the body, 33 of 33.
- **Zooming below 2.2:** a nearby tradition takes focus, 7 of 7.
- **Enter on an automatic "+N more"** focuses the first tray row. Escape then returns focus to the figure (base: the body).

**3. Partly fixed.**
- **What works.** Where the bar is measured, it fits or wraps, and only the Who chip shrinks. Examples:
  - 20px at 641px: Key 75 of 75px (base: 0).
  - 24px at 768px, list open: 85 of 85px (base: 0).
  - iPad Mini at 24px: two rows, Key whole (base: 0–14 of 85px).
- **Still BLOCKING.** Nothing re-measures when the chips change width but the bar's box does not.
  - Below 1181px, switching a layer on adds a "✓". If the last measure had that layer off, the Key is pushed off.
  - With People and Stories saved as hidden, at 20px and 700px, turning both on leaves 53 of 75px.
  - Layers off, resize, layers on:
    - 20px: 62 widths fail; worst 12 of 75px.
    - 24px: 150 fail; worst 10 of 85px.
    - 16px: none.
- **Fix:** observe the bar's children, or call `fitFeatureBar` from `applyToggles`.

**4. Fixed.**
- With a Who list open, every visible switch is on top in all 10 panel checks.
- Desktop 11 of 11 (base: 1 of 9). iPad 13 of 13 (base: 1 of 11). iPhone 8 of 8 (base: 2 of 8).
- With panels closed, the bar covers nothing new: 0 sampled points on other overlays land on it.

**5. Fixed.** At 16px the bar is one row at every width, with or without a Who chip. Base had two rows at 901–1009px. At 901px the long river label shows 121 of 230px.

**6. Fixed.** Nothing reads `years`. All 15 rivers keep base's labels and tooltips.

**#1628–#1631 unchanged.**
- Tab reaches the map in base's number of presses.
- Escape, the tray's ×, the Who chip and a second press each close the list and return focus. The status text matches base.
- Names, pressed states and expanded states match base exactly.

**Known trade-off holds.** At 16px the Who label is 0px at 641–645px and 15px at 660px.

## New faults

**BLOCKING 1. Switch panels no longer wrap.**
- `.feature-bar>*{white-space:nowrap}` matches `.chip-group`. `white-space` is inherited, so every `.chip-panel` is now `nowrap` (base: `normal`).
- **Desktop and iPad:**
  - The Connections notes stop mid-sentence (1992px of text in 350px).
  - The Key panel cuts its descriptions, and 3 of 11 terms and 3 of 9 links fall outside it.
- **iPhone:**
  - The Key panel is 619px wide and starts at −229px. 0 of 11 terms are whole, and 5 of 9 links can't be reached.
  - At 24px, river descriptions run under the switches.
- **Fix:** set `nowrap` on the chips only.
- Shots: `/tmp/claude-0/fc/shots/panel-key-head-iphone.png` (base: `panel-key-base-iphone.png`) and `/tmp/claude-0/fc/shots/panel-links-head-desktop-16.png`.

**MINOR 2. ResizeObserver loop errors.**
- "ResizeObserver loop completed with undelivered notifications." fires as a window `error`.
- It fired on live text-size changes (7 of 10 sequences) and on some page loads: 4 of 210 (at 24px, at 848 and 1216px), and 4 of 4 at 729px with 20px text and late fonts. Base fired none.
- **Cause:** `fitFeatureBar` changes the observed bar's height inside the observer's own callback.
- Nothing shows, but an error monitor would log it.

**MINOR 3. The overflow check ignores the bar's right padding.**
- `scrollWidth > clientWidth + 1` lets chips run into the padding, while wrapping breaks at the content box.
- Just above each wrap point, the Key sits in the padding, up to 0.9px past the edge. That's 11 widths at 20px and 58 at 24px.
- If `is-tight` was set earlier, those widths show two rows instead: 7 of 114 late-font loads at 24px.

**MINOR 4. At larger text the Who label vanishes on wide screens.**
- The label is 0px, so only "×" shows: 746–941px at 20px, 868–1305px at 24px.
- Above 900px this is new, since base wrapped. The `aria-label` still names the list.

**No fault found.**
- 2,000 random actions (500 per device, plus 500 on desktop at 20px): 0 runtime errors, and the list never stuck open.
- `is-tight` never flipped while idle at 27 boundary widths.
- Focus is restored only if it fell to the body from the layer being rebuilt.

**Count:** 1, 2, 4, 5 and 6 fixed; 3 partly. New: 1 BLOCKING, 3 MINOR.
