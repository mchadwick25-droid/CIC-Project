> **SUPERSEDED — 2026-07-04.** This draft was sent back for substantial rework by an Opus deep review (see `reference/L2C-System-Status/CiC_Pipeline_Decision_Log.md`), which found its central justifying claim inaccurate and its Boundary/Shared-status design broken on real content. Rather than patch it, the project lead directed a complete rework of the Step 2 process that combines Source Ecology and source-tagging into one step, per-world only (cross-world checking deferred as separate follow-up work). See `Source_Registry_Template.md` for the current, live design. Kept here, unmarked-as-deleted, as the historical record of what was tried and why it didn't hold up — per this project's own Record Integrity Principle.

---

# Cross-World Source Registry

**Version 1.0. New in the Doc_02B V2.0 design pass. Companion to every world's Doc_02B — filed in reference/L3B-World-Build-Methodology as a project-level, cross-world living document, not a per-world artifact. Living, append-only: entries are added as each world's Doc_02B is finalized, never renumbered or removed.**

## What this is, and why it exists

At five worlds, a builder could plausibly recognize when a source belonged to a different world's inheritance — that is roughly how Theon's Gregory-of-Nyssa defect was eventually caught, by someone noticing the resemblance. At forty worlds, that recognition cannot be relied on to happen by chance. This Registry is the mechanical substitute: a single index of every source any world's Doc_02B has claimed as Native, so a new world's build can check a candidate source's prior claims by lookup rather than by memory.

This Registry does not replace Doc_02A's or Doc_02B's own evidentiary judgment for any single world. It only answers one question, for one source, at a time: **has this already been claimed as Native by another world, and if so, is that an exclusive claim or a recorded Shared one?**

## How this is used (see Doc_02B Approved Source Database Template V2.0, "Cross-World Registry Check")

1. Before finalizing any Doc_02B entry as Native, look the source up here by author/work.
2. Not present: proceed with the normal Boundary Check against Doc_01; if it passes, claim it as Native and add it here in the same build pass that finalizes that world's Doc_02B.
3. Present, claimed by a different world, no Shared justification recorded: the source defaults to Comparandum–Excluded in the new world's Doc_02B. A Shared claim may still be established, but it must be argued and recorded, not assumed.
4. Present and already marked Shared: both worlds may license it as Native/Shared in their own Doc_02B, and the new world's builder adds their own world to the "Claimed By" column rather than creating a duplicate entry.

## Registry Table

| # | Source (author/work) | Era | Region/Tradition | Claimed By (World) | Shared? | Notes | Added |
|---|---|---|---|---|---|---|---|
| 1 | Scripture (Old and New Testament, all books) | Pre-dates every world's horizon | Universal | All five worlds (Alexandria, Early Latin, Early Communal, Desert Christianity, Nicene-Cappadocian) | Yes | Foundational shared inheritance across all worlds by nature, not by oversight — the paradigm case of a legitimate Shared entry. Individual books/verses are cited per-world in each world's own Doc_02B; this Registry entry exists so no future builder mistakes a Scripture citation for a cross-world contamination risk. | 2026-07-04, by: Doc_02B V2.0 design pass |
| 2 | Origen (biography, catechetical-school career, general allegorical/exegetical method) | c. 185–254 CE | Alexandria | Alexandria (Theon) | No | Native to Alexandria. Not claimed by any other current world; no Shared justification recorded. | 2026-07-04, by: Doc_02B V2.0 design pass |
| 3 | Clement of Alexandria (*Paedagogus*, *Stromata*) | c. 150–215 CE | Alexandria | Alexandria (Theon) | No | Native to Alexandria, specifically the burning-bush-as-Logos-theophany reading (Paedagogus II.8) — see Alexandria's own Doc_02B NOT-approved-for flag distinguishing this from Gregory of Nyssa's reading of the same passage. | 2026-07-04, by: Doc_02B V2.0 design pass |
| 4 | Athanasius (*On the Incarnation*) | c. 296–373 CE | Alexandria | Alexandria (Theon) | No | Native to Alexandria; the ch. 54 theosis formula is this world's own most explicit citable anchor. | 2026-07-04, by: Doc_02B V2.0 design pass |
| 5 | Gregory of Nyssa (*Life of Moses*, epektasis doctrine, *Life of Macrina*, Fourth Homily on Ecclesiastes, etc.) | c. 335–395 CE | Cappadocia | Nicene-Cappadocian (Eumathios) | No | **The paradigm entry this Registry exists to protect.** Explicitly confirmed Native to Cappadocia only; explicitly NOT Shared with Alexandria (Theon) — the original defect this whole mechanism was built to prevent from recurring. Any future world's builder considering citing Gregory of Nyssa should stop here first. | 2026-07-04, by: Doc_02B V2.0 design pass |
| 6 | Basil of Caesarea, Gregory of Nazianzus (Cappadocian corpus generally) | 4th c. CE | Cappadocia | Nicene-Cappadocian (Eumathios) | No | Native to Cappadocia. | 2026-07-04, by: Doc_02B V2.0 design pass |
| 7 | Augustine of Hippo, Possidius, the Donatist controversy corpus | Early 4th–mid 5th c. CE | North Africa | Early Latin (Cordus) | No | Native to Early Latin. | 2026-07-04, by: Doc_02B V2.0 design pass |
| 8 | The Didache, Polycarp (*To the Philippians*), 1 Clement, Ignatius of Antioch's letters | c. 70–150 CE | House-church / ekklesia, broadly Eastern Mediterranean | Early Communal (Chloe) | No | Native to Early Communal. The Novatian schism (251 CE) and its own characteristic sources are explicitly NOT native here — see Early Communal's own Doc_02B boundary finding; this is a temporal exclusion, not a cross-world one, and is recorded in that world's Doc_02B rather than here. | 2026-07-04, by: Doc_02B V2.0 design pass |
| 9 | The Apophthegmata Patrum, Evagrius Ponticus, Athanasius's *Life of Antony*, the Anthropomorphite/Origenist controversy corpus (Theophilus's letters, c. 399–402 CE) | c. 270s–early 5th c. CE | Egyptian desert | Desert Christianity (Kimon) | No | Native to Desert Christianity. Explicitly NOT to be confused with the later, unrelated Byzantine Iconoclasm controversy (8th–9th c.) — a temporal/topical distinction recorded in that world's own Doc_02B. | 2026-07-04, by: Doc_02B V2.0 design pass |

## Notes on seeding this Registry

Entries 1–9 above are seeded retroactively from the five existing worlds' already-built Doc_02B files (`CiC-Fable-Experiment` branch), so the Registry starts populated rather than empty when the next (sixth, and eventually fortieth) world is built. This seeding is a summary of each world's own Doc_02B, not a re-audit — the authoritative detail for any entry remains that world's own Doc_02B file. Entry 5 is deliberately the most detailed because it is the load-bearing example: every future builder who reaches for Gregory of Nyssa should be stopped by this table before they need to be stopped by adversarial testing.

## Living-document protocol

Identical discipline to Doc_02B itself: append with the next sequential #, never renumber or remove an existing entry. If a Shared claim is later found to be a mistake (a source assumed universal that turns out to be exclusive to one world after all), correct the Shared column and record why in Notes — do not delete the row.
