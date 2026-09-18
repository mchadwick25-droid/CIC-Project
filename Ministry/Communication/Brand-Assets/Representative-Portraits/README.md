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
| `rzg/` | Theophilus | The Reformed Cities: Zurich & Geneva |

Inside each, files are named `Name_Portrait.png` (e.g. `Chloe_Portrait.png`) for the
standalone profile portrait — the actual convention in place as of 2026-07-24, not
the `name-profile.png` scheme originally proposed here. Follow this same
`Name_<Type>.png` pattern for anything added later — e.g. `Chloe_Table.png` for a
version meant to seat at the Living Table, or `Chloe_Photostock.png`.

## `group/` — more than one Representative together

Filename lists everyone in the image, **in this fixed order** (the same
chronological order the app already sorts worlds by, so a given trio always
produces the same filename regardless of who was thought of first):

**Chloe → Theon → Yausep → Fidelis → Marius → Papnoute → Albina → Theophilus**

(Donatism's own time window, 311-439, opens one year before Church and Empire's
312 — `records/worlds.yaml`'s own `don`/`ijc` `time_window.start` values — so Fidelis
slots in ahead of Marius in this chronological ordering, not at the end. The
Reformed Cities' own window, 1519-1650, opens over a millennium after every other
world listed here, so Theophilus slots in last, not merely appended by convenience.)

Example: an image with Chloe, Marius, and Albina together is always
`Chloe_Marius_Albina.png`, never `Marius_Chloe_Albina.png` — drop whichever aren't
present, keep the rest in this order.

## Status as of 2026-09-18

All seven original profile portraits remain in place and approved (full reasoning
for the first six: `Ministry/Features/In-App-Icons-Graphics/Decision-Log.md`;
Fidelis's own research brief and generation prompt:
`donatism/Fidelis_Portrait_Prompt.md`):
`house-churches/Chloe_Portrait.png`, `alexandria/Theon_Portrait.png`,
`syriac/Yausep_Portrait.png`, `donatism/Fidelis_Portrait.png`,
`empire/Marius_Portrait.png`, `desert/Papnoute_Portrait.png`,
`bethlehem/Albina_Portrait.png`.

An eighth profile portrait, `rzg/Theophilus_Portrait.jpg` (note: `.jpg`, not `.png`
— the file as generated and approved, not re-encoded to match the others' format),
was approved 2026-09-18. Grounding and generation-prompt reasoning: not yet
committed as a standalone brief (2026-09-18 finding while promoting to `live` —
this citation pointed at a file that was never added; owning thread to supply
the actual brief and restore the citation).

No `_Table` or `group/` images have been built yet — those come after the Living
Table scene gets rebuilt around these portraits.
