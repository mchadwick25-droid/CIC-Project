# Hosted Tour — Integration Note V0.1 (proposal for the assembly session)

**Date:** 2026-07-16
**Status:** A proposal only — the front-end thread owns integration timing and the map thread owns the map demo. Nothing here has been wired; neither demo was modified by the other thread's work.

## The handoff, as proposed

The map demo's world panel already renders the placeholder button:
`Take a tour with Chloe (coming later)` (in `CiC_World_Map_Interactive_Demo.html`, the LIVE-world panel actions). The proposal is the smallest honest change:

1. **For Chloe's world only**, the button drops "(coming later)" and opens the tour experience — in demo form, simply by opening `CiC_Chloe_Tour_Interactive_Demo.html` (same folder-relative link inside the assembled package, or the two files zipped together the way the map's email pack already works). The tour's arrival card already answers from the other side: "You chose: 'Take a tour with Chloe'" — the seam is written to read as one product.
2. **For every other world**, the button keeps its placeholder — and when tours become real, a world with no documented communal scene gets the honest refusal text as the button's own answer (per the Tours rule, 2026-07-07, and the per-world evidentiary analysis in `Ministry/Technology/CiC_Tour_Experience_Module_Strategy_V0_1_DRAFT.md` §3: House-Churches yes; Syriac qualified yes; Desert and Bethlehem Circle partial, different scenes; Nicene-Cappadocian not assessable).
3. **Return path:** the tour's ending ("The Way Out") should, in an assembled demo, offer "Back to the World Map" alongside "Walk it again" — a one-line addition best made in the assembly session where both files sit side by side.

## Shared-language conformance (verified, not assumed)

The tour demo copies the map demo's actual CSS tokens (including `--live-chloe`), inlines the identical Cinzel data-URI face, keeps captions in a docked strip below the stage (the house rule), and reuses the tour-engine contract (`?tour=1`, `?pose=N`, skippable, reduced-motion). A viewer moving from map to tour should read them as one artifact. Both recordings (GIF + twelve-frame slideshow) were produced with the same pose-mode + headless-Chrome + Pillow pipeline as the map's.

## Open items for the assembly session

- The return-path button (item 3 above) — trivial, but touches both files, so it belongs to the session, not to either thread unilaterally.
- Whether the assembled package's zip carries both demos plus both slideshows/GIFs, mirroring the map thread's email-pack pattern.
- Mark's read on Chloe's scripted lines (flagged in the design note §7) before any public showing.
