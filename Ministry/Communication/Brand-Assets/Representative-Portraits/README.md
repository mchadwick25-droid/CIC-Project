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
| `empire/` | Marius | Church and Empire |
| `desert/` | Papnoute | Desert Monasticism |
| `bethlehem/` | Albina | Bethlehem Circle (Hieronymian) |

Inside each, files are named `Name_Portrait.png` (e.g. `Chloe_Portrait.png`) for the
standalone profile portrait — the actual convention in place as of 2026-07-24, not
the `name-profile.png` scheme originally proposed here. Follow this same
`Name_<Type>.png` pattern for anything added later — e.g. `Chloe_Table.png` for a
version meant to seat at the Living Table, or `Chloe_Photostock.png`.

## `group/` — more than one Representative together

Filename lists everyone in the image, **in this fixed order** (the same
chronological order the app already sorts worlds by, so a given trio always
produces the same filename regardless of who was thought of first):

**Chloe → Theon → Yausep → Marius → Papnoute → Albina**

Example: an image with Chloe, Marius, and Albina together is always
`Chloe_Marius_Albina.png`, never `Marius_Chloe_Albina.png` — drop whichever aren't
present, keep the rest in this order.

## Status as of 2026-07-24

All six profile portraits are in place and approved (full reasoning:
`Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`):
`house-churches/Chloe_Portrait.png`, `alexandria/Theon_Portrait.png`,
`syriac/Yausep_Portrait.png`, `empire/Marius_Portrait.png`,
`desert/Papnoute_Portrait.png`, `bethlehem/Albina_Portrait.png`. No `_Table` or
`group/` images have been built yet — those come after the Living Table scene gets
rebuilt around these portraits.
