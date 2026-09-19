# Representative Portraits — drop folder

One subfolder per world (named by the same `world_id` the flat icons in
`../World-Icons/` already use), plus one `group/` folder for images with more than
one Representative together. This lets the web-building thread look things up by
`world_id` the same way it already does elsewhere, while filenames stay
human-readable.

## Per-world folders

| Folder | Representative | World |
|---|---|---|
| `house-churches/` | Chloe | House-Churches |
| `alexandria/` | Theon | Alexandria Catechetical School |
| `syriac/` | Yausep | Syriac Christianity |
| `donatism/` | Fidelis | Donatism |
| `empire/` | Marius | Church and Empire |
| `desert/` | Papnoute | Desert Monasticism |
| `bethlehem/` | Albina | Bethlehem Circle (Hieronymian) |
| `witt/` | Nikolaus | Lutheran Wittenberg & Its Congregations |

Inside each, files are named `Name_Portrait.png` (e.g. `Chloe_Portrait.png`) for the
standalone profile portrait — the actual convention in place as of 2026-07-24, not
the `name-profile.png` scheme originally proposed here. Follow this same
`Name_<Type>.png` pattern for anything added later — e.g. `Chloe_Table.png` for a
version meant to seat at the Living Table, or `Chloe_Photostock.png`.

## `group/` — more than one Representative together

Filename lists everyone in the image, **in this fixed order** (the same
chronological order the app already sorts worlds by, so a given trio always
produces the same filename regardless of who was thought of first):

**Chloe → Theon → Yausep → Fidelis → Marius → Papnoute → Albina → Nikolaus**

(Donatism's own time window, 311-439, opens one year before Church and Empire's
312 — `records/worlds/don.yaml`'s and `records/worlds/ijc.yaml`'s own `time_window.start`
values — so Fidelis slots in ahead of Marius in this chronological ordering, not at the
end. Nikolaus's own window, 1517-1580 — `records/worlds/witt.yaml` — opens more than a
thousand years after any other world's, so he takes the final slot.)

Example: an image with Chloe, Marius, and Albina together is always
`Chloe_Marius_Albina.png`, never `Marius_Chloe_Albina.png` — drop whichever aren't
present, keep the rest in this order.

## Status as of 2026-09-19

All eight profile portraits are in place and approved (full reasoning for the first
six: `Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`; Fidelis's own research
brief and generation prompt: `donatism/Fidelis_Portrait_Prompt.md`; Nikolaus's own:
`witt/Nikolaus_Portrait_Prompt.md`): `house-churches/Chloe_Portrait.png`,
`alexandria/Theon_Portrait.png`, `syriac/Yausep_Portrait.png`,
`donatism/Fidelis_Portrait.png`, `empire/Marius_Portrait.png`,
`desert/Papnoute_Portrait.png`, `bethlehem/Albina_Portrait.png`,
`witt/Nikolaus_Portrait.png`. No `_Table` or `group/` images have been built yet —
those come after the Living Table scene gets rebuilt around these portraits.
