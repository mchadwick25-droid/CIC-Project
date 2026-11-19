# Round 3 fix check 2: `aea7d944` to `58a615f4` (feature bar), plus five later commits

**How I tested.**
- Base `aea7d944` and head `58a615f4`, each built in its own worktree. Each later commit was built and checked on its own.
- Playwright Chromium: 1440×900 desktop, iPad Mini both ways, iPhone 13, and every bar width from 641 to 1440px.
- Text at 16, 20 and 24px (`Page.setFontSizes`). Web fonts loaded, except in the late-font runs.
- Scripts, logs and shots: `/tmp/claude-0/fc2/`.

## The bar fixes (58a615f4)

**A (BLOCKING): Fixed.**
- Layers off, resize, layers on: 0 of 7,200 checks leave the Key cut or the fit wrong. That covers 800 widths, three text sizes, and no Who list, a long river label or a tradition. Base: 62 widths at 20px (worst 12 of 75px), 149 at 24px (worst 10 of 85px).
- Saved hidden layers, then switched on: 0 of 420 loads wrong. Base: 7 of 60 at 20px, 16 of 60 at 24px.
- iPad both ways and desktop, by touch or click: 27 of 27 right. Base: 23 (iPad, 24px: Key 14 of 85px).
- Note: the fit now lands one frame after a chip changes.

**B (BLOCKING): Fixed.**
- 14,400 panel opens (every width, three sizes, Who list or not): all wrap, none scrolls sideways or cuts text, all sit 8px or more inside both edges. Base: every panel `nowrap`.
- 150 opens by click, tap, Enter and Space on four devices: every control reachable and on top. Base: 150 of 150 faulty.
- iPhone Key panel: 0–390px, 9 of 9 links. Base: starts at −229 to −524px; 1–4 links.

**MINOR, observer errors: Fixed.** 0 in 264 loads (fonts on time or 1.8s late), 66 live text-size changes and 2,500 random actions. Base: 4 of 4 loads at 729px, 20px, late fonts; 8 of 16 text-size sequences.

**MINOR, right padding: Fixed.** The Key never sits in the padding on one row (base: 11–30 widths at 20px, 58 at 24px). No second row without need. No idle flips at 42 edge widths.

**Also, Key panel off the left edge: Fixed when opening.** 0 of 14,400 opens. Base: 27 of 267 sampled widths at 20px, 67 at 24px.

**Not regressed.** With a Who list open, all switches are on top (75 opens). At 16px the bar is one row at all 800 widths, with or without a Who list. Focus, names, states and announcements match base on four devices.

**New fault. MINOR 1: an open panel keeps its opening shift when the bar reflows.**
- Resizing, rotating, or the Who chip coming or going can leave it partly off screen until reopened.
- Base did this more: of 580 resize pairs, head 33/85/144 at 16/20/24px, base 67/149/196. Random actions: 8 of 2,500 steps (base 37 of 1,500).
- New variant: a Key panel shifted right on two rows ends up past the right edge once the bar is one row again. On an iPad at 24px, turned from portrait to landscape, it ends 249px off screen.
- Cause: `positionFeatureBar` never re-clamps open panels.
- Otherwise, 2,500 random actions: 0 errors.

**Known, not counted.**
- 16px: the Who label is 0px at 641–645px, and the × stays whole. Same as base.
- 20px: label 0px at 35 widths (757–941). 24px: 64 widths (881–1305). At 10 and 14 of those widths, even the × is cut, worst 1.3 of 8.6px. Base: 40 and 72 widths.
- At 24px on phones under 369px wide, Rivers and Key panels are wider than the screen. Same as base.

## Card feedback footer (desktop, iPhone; POSTs mocked, 0 sent; code unchanged since 58a615f4)
- All 7 card types end with one footer. Tab reaches both buttons. Report opens the form on "Accuracy"; Escape closes it and returns focus. Names and states right. Nothing cut at 16 or 24px.
- **BLOCKING:** river, connection, story and era cards (and people with no entry) all send page `atlas-v3`. One "This helped" marks them all pressed and disabled, even after reload, and their reports can't be told apart. Cause: `showPanel(null)`.
- **MINOR:** "This helped" by keyboard drops focus to the body. Escape then fails until Tab.

## Era mark (3b4ef40c): no fault
- The ring is 14px with a 1.4px stroke at every overview zoom (0.06–0.79), on three devices. In the strip it is 14px in a 16px icon. Before: 19px, 1.6.
- The tap area is 44px. Taps and clicks open the era card: 27 of 27 at the centre, 81 of 81 at 18px off. The strip opens it 9 of 9.
- Hover and focus restyle the ring. The strip shows its hover colour and focus ring.
- The ring sits 7.9–8.4px after the title (was 5.3–5.8). It never touches the title or date line. As before, the invisible area reaches 6px over the title's end, and map marks pass under the pinned caption.

## Build-status wording (b2a072ba, 13263c1a)
- "Not yet available" is gone from 296 tips and 296 labels. The Representative sentence is gone from all 15 river cards. No label has an empty part.
- **BLOCKING:** the Latin Pastoral card still says "There's no built conversation for this tradition here yet." Source: `cic-website/data/world-census.json`, `movements[6].why`.
- River paragraphs read well. Apart from the cut sentence, they are unchanged word for word.
- ESLint finds no new unused code. 0 errors over 1,696 cards.

## Who hovers (13263c1a)
- Real mouse on all 103 Who marks: the tip names match the first tray rows 103 of 103, and "+N more" is right 34 of 34. The labels name the same people.
- 0 status words in 534 tips and 1,308 labels. Councils show the year once (it was twice on 9).
- No tip overflows. On the phone, 11 of 11 taps open the list. 0 errors.
- **MINOR:** with the tray set to "By tradition", clicking another bubble keeps that order, so its first rows differ from the tip.
- **MINOR:** labels run places together: "Rome, today in Italy, Bethlehem, West Bank".

## Card Who button (d4588fbf): no fault
- Text and label match the list on all 74 cards, on both devices at 16 and 24px.
- Long first names end in an ellipsis. "+N more" and "See the list" are never cut.
- Click, tap, Enter or Space focuses the heading and scrolls it to the top (1.5s on the longest card). Tab reaches the first name, and that card's Tradition link returns.
- Nothing uses the removed code. A Who list opened beside a card works, and the tray keeps its name.

**Count.** The bar: A, B, both minors and the left-edge fix hold, with 1 new MINOR. Later work: 2 BLOCKING (footer page key, Latin Pastoral sentence) and 3 MINOR.
