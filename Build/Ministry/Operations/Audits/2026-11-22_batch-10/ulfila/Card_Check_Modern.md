# Ulfila: card check, the modern pass

Checked: `ulfila.card.json` against `Card.pass3.json`, `Card_Edits.md` ("Fourth pass: no modern opinion (2026-11-23)") and `ulfila.brief.txt` as it now stands. Every cited line opened in `cic/texts/`.

**Verdict: FIX** (seven changes, below).

## What holds

- Nothing moved outside the edit list: the only differences from `Card.pass3.json` are edits 1-9 (datesNote; `uncertain` entries 1, 3, 6 and 17; three `briefReferences` entries removed; the Sozomen reference trimmed).
- Edits 1, 2, 3, 5, 6, 7, 8 and 9 stand on their evidence: DUC 20991-20995, PHI 120 ("Eusebius and the other prelates that were with him"), STR 603-607, NP2 9484-9490 and 9606-9612 (Socrates 2.41, the emperor's return, no year), SOC-G1 27461-27466 ("τότε πρῶτον"), NP2 40160-40162 (Sozomen, "during the reign of Constantius"), AUX 3684, 3735 (Kauffmann's June 383), AUX 15283-15292 (no year).
- `briefReferences`: every remaining entry names only what the brief still tells. None names Eusebius of Nicomedia, a year, or the fragments' translator.
- `quotationOriginals`: unchanged, four entries for the brief's four quoted spans.
- No audit named; American spelling.

## Changes

Edit 4's evidence, "No held modern writer is named for the council's year", is wrong: Kauffmann (AUX 2531, 2590, 2641: "concil des jahres 360"), Duchesne (DUC 11505-11507: "dans les premiers jours de janvier 360") and Streitberg (STR 1091: "Konstantinopeler Synode vom J. 360") all give 360. The modern date can be credited by name, so it must be.

1. `uncertain`, Sozomen council entry.
   Old: "360 is the usual modern date, a modern judgment that no held old source gives."
   New: "360 is the date Kauffmann, Duchesne and Streitberg give, a modern judgment that no held old source gives."

The pass marked Duchesne and Streitberg as modern judgments but left Kauffmann's own reconstructions, and the doubt he reports, unmarked. Each `uncertain` entry stands alone on the page, so each needs its own mark.

2. `uncertain`, consecration entry.
   Old: "and thinks Ulfila was made a country bishop at first."
   New: "and thinks Ulfila was made a country bishop at first, each a modern judgment."
   Evidence: AUX 3752-3755, 3798-3805.

3. `uncertain`, crossing entry.
   Old: "Kauffmann dates the crossing to 348 or 349."
   New: "Kauffmann dates the crossing to 348 or 349, a modern judgment."
   Evidence: AUX 3751-3752 ("ins jahr 348—349 setzt").

4. `uncertain`, numbers entry.
   Old: "Kauffmann notes that the age often treated numbers this way, but counts them as real years."
   New: "Kauffmann notes that the age often treated numbers this way, but counts them as real years, a modern judgment."
   Evidence: AUX 3755-3757.

5. `uncertain`, creed's language entry.
   Old: "Kauffmann reports Georg Waitz's doubt whether the deathbed creed was left in Latin in the form that survives."
   New: "Kauffmann reports Georg Waitz's doubt whether the deathbed creed was left in Latin in the form that survives, a modern judgment."
   Evidence: AUX 3736-3738 ("Waitz s. 56").

The brief now says only that fragments of a Gothic Bible survive without a translator's name. Two card fields still hand the surviving fragments to Ulfila as settled, and the codex's date is Streitberg's, uncredited.

6. `keyWorks[0].about`.
   Old: "the Scriptures in Gothic; the Gospels survive in part in the Codex Argenteus at Uppsala, written in the fifth or sixth century in silver and gold on purple parchment, and Paul's letters in palimpsests from Bobbio, now at Milan"
   New: "the Scriptures in Gothic, which Philostorgius, Socrates and Sozomen say he made; Gothic Gospels survive in part in the Codex Argenteus at Uppsala, written in silver and gold on purple parchment, in the fifth or sixth century by Streitberg's dating, and Paul's letters in palimpsests from Bobbio, now at Milan, all without a translator's name; Streitberg takes them for his, a modern judgment"
   Evidence: PHI 120; NP2 14448-14459, 40178-40179; STR 603-607, 1348-1353, 1402-1404.

7. `legacy.traces[2]`.
   Old: "The Gothic Bible survives in fragments, edited by Ernst Bernhardt in 1884 and by Wilhelm Streitberg in 1908."
   New: "Fragments of a Gothic Bible survive without a translator's name, edited by Ernst Bernhardt in 1884 and by Wilhelm Streitberg in 1908."
   Evidence: STR 603-604; the brief, paragraph 6.

## Not found (left in place)

- `uncertain`, numbers entry: "like David, Joseph and Christ". Auxentius names David at thirty and calls Ulfila an imitator of Christ and his saints (AUX 15240-15243); Joseph is not in the file. From the existing card; not changed by this pass.
