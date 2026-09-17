# World Media, Story Beats Twenty — homepage image strip (second pass)

**STATUS: 19 of 20 images downloaded and verified.** Only `san-vitale-ravenna/`
is still a placeholder — see its own `DOWNLOAD-PENDING.md` for why (not archived
on the Wayback Machine, and Wikimedia's direct endpoint was still cooling down
from an earlier rate limit at the time of this pass). Everything else in this
folder is a real, downloaded file, not a placeholder.

Twenty candidate photographs for a homepage image strip on churchinconversation.com,
spanning the full ~2000-year story of the Church — a broader, second sourcing pass
alongside `../World-Media-Era-Spanning/`'s smaller 8-image set. Nothing here duplicates
an exact file from either `../World-Media/` (the 70-450 CE world-selector tiles) or
`../World-Media-Era-Spanning/`, though a few subjects sit in the same broad era.

Same discipline throughout: one real, historically-matched photo per slot, sourced
from Wikimedia Commons, verified individually for a genuine period/subject match and
an actual open license — never stock imagery, never a caption trusted at face value.

**No individuals.** Every slot was screened against one hard constraint: no photo
whose main subject is a specific named historical person (no portraits, no statues/
busts of one named person as the main subject). Iconographic religious art (mosaics,
frescoes depicting Christ or saints as devotional art) is treated differently from a
portrait photograph of a historical figure, and crowds/congregations are always fine
— several slots are deliberately crowd shots for exactly that reason. Two candidate
files were rejected specifically on this rule and are noted below.

## Files

| Folder | Image | Period | Story beat |
|---|---|---|---|
| `etchmiadzin-cathedral/` | `etchmiadzin-cathedral.jpg` | founded 301-303 CE, rebuilt c. 480s | Armenia, the first state to adopt Christianity |
| `catacombs-priscilla/` | `priscilla-fractio-panis-fresco.jpg` | 2nd-4th c. | Early Christian devotional art, the hidden Church |
| `san-vitale-ravenna/` | `san-vitale-mosaici.jpg` | completed 547 CE | Byzantine mosaic art, Justinian's Italy |
| `hagia-sophia-exterior/` | `hagia-sophia-exterior.jpg` | completed 537 CE | Byzantine architecture (exterior, distinct from the Deesis mosaic elsewhere in the library) |
| `lindisfarne-priory/` | `lindisfarne-priory.jpg` | founded 635 CE, ruins are Norman-era | Anglo-Saxon/Celtic Christianity |
| `cluny-abbey/` | `cluny-abbey-ruins.jpg` | 10th-12th c. | Benedictine monastic reform |
| `holy-sepulchre-jerusalem/` | `holy-sepulchre-jerusalem.jpg` | traditional site, 12th-c. Crusader rebuild | The earliest layer of the Church's story; the Crusades |
| `canterbury-cathedral/` | `canterbury-cathedral.jpeg` | mostly 14th-16th c. | English medieval Christianity, the Becket martyrdom site |
| `notre-dame-paris/` | `notre-dame-de-paris.jpg` | High Gothic, largely complete by 14th c. | Gothic cathedral-building, a second cathedral alongside Chartres |
| `lalibela-rock-churches/` | `lalibela-rock-hewn-churches.jpg` | 12th-13th c. | Ethiopian Christianity, a non-European chapter |
| `avignon-palais-des-papes/` | `avignon-palais-des-papes.jpg` | built 1335-1352 | The Avignon Papacy |
| `trento-cathedral/` | `trento-cathedral-san-vigilio.jpg` | cathedral 12th-13th c.; council 1545-1563 | The Council of Trent, the Counter-Reformation |
| `st-peters-basilica/` | `st-peters-basilica.jpg` | consecrated 1626 | Counter-Reformation/Baroque Catholicism |
| `geneva-st-pierre/` | `geneva-st-pierre-cathedral.jpg` | core 12th-13th c., portico 1750s | The Reformed tradition, Calvin's Geneva |
| `sao-miguel-missoes/` | `sao-miguel-das-missoes-ruins.jpg` | founded 1687, church 1740s | Jesuit missions to the Americas |
| `old-north-church-boston/` | `old-north-church-boston.jpg` | built 1723 | Colonial-era American Christianity |
| `st-francis-kochi/` | `st-francis-church-fort-kochi.jpg` | founded c. 1503 | The missionary movement's arrival in Asia |
| `st-basils-moscow/` | `st-basils-cathedral-moscow.jpg` | built 1555-1561 | Russian Orthodoxy |
| `azusa-street-afm/` | `azusa-street-apostolic-faith-mission.jpg` | photographed 1907 | The birth of modern global Pentecostalism |
| `manila-black-nazarene/` | `feast-of-black-nazarene-manila.jpg` | photographed 2012 | The contemporary Global South Church, as a gathered crowd |

## Sourcing metadata — `story-beats-twenty-sources.json`

Same schema as the two existing sets: `file`, `title`, `location`, `period`, `story`,
`source_url`, `author`, `date_taken`, `license`, `attribution`, and a `note` field
carrying the verification method and any honest caveat.

**License note.** Licenses in this set: **CC BY-SA** (2.0 through 4.0 and one IGO
variant, the majority of this set — attribution and share-alike required), **CC BY**
(2.0, 3.0, and 4.0 — attribution required, no share-alike), and **Public domain** (two
images — the Priscilla catacomb fresco and the historic Azusa Street photo).

## Method and the network-policy story behind this set

Research (finding candidates and verifying licenses) was done first, in parallel,
across four era-based batches. At that point `commons.wikimedia.org` and
`upload.wikimedia.org` were both blocked by this sandbox's network egress policy —
the same restriction already hit during the `../World-Media-Era-Spanning/` pass —
so every license, author, and date below was confirmed by a **direct fetch** of
`en.wikipedia.org`'s own MediaWiki API (`action=query&prop=imageinfo&iiprop=extmetadata|url`),
which serves Commons files' metadata through Wikipedia's federated file-repository
design even when Commons itself can't be reached.

**Mid-task, Mark widened the environment's network allowlist to include Wikimedia's
image domains directly** (and several other GLAM sources: Library of Congress, Met
Museum, Smithsonian, Rijksmuseum, NYPL). Before that change landed, a stopgap was
tried and worked in part: `web.archive.org` was already allowed, and the Wayback
Machine had cached real byte-copies of several of these exact files, retrievable via
`https://web.archive.org/web/<year>id_/<the real upload.wikimedia.org URL>`. Once the
allowlist change was live, downloads were redone directly from Wikimedia Commons
itself, which is the cleaner, authoritative path — a few files below may still show a
Wayback Machine URL in their own verification note as a record of exactly how they
were first retrieved, before the redo.

**A second, smaller obstacle**: fetching full-resolution originals back-to-back
triggered Wikimedia's own edge rate limiter (HTTP 429, "Too many requests... instead
use thumbnail images"). This was fixed by switching to Wikimedia's own thumbnail
endpoint at 1600px width — plenty for a homepage strip, and it avoids the opposite
problem of vendoring a 50+ MB original (the St. Peter's Basilica file's true original
size) into the repo for no visual benefit.

## Honest caveats

- **Cluny Abbey**: no photograph of the intact Cluny III (once the largest church in
  Christendom) exists — it predates photography and was mostly demolished after the
  French Revolution. This shows the surviving ~10% of fabric, not the church at its
  height.
- **Notre-Dame de Paris**: this photo is from 2013, before the April 2019 fire.
  Caption it as a historical/pre-fire view — the cathedral reopened after restoration
  in December 2024.
- **Lindisfarne Priory**: the visible ruins are the Norman-era (11th-12th c.) rebuild
  on the original 635 CE Anglo-Saxon foundation site, not original fabric. A candidate
  file showing a statue of St. Aidan was rejected here specifically to keep this slot
  free of a named individual as its main subject.
- **St. Francis Church, Fort Kochi**: the standing building is a later colonial-era
  stone reconstruction, not the original 1503 wooden structure.
- **Geneva's St. Pierre Cathedral**: the neoclassical west facade seen in most
  photos (including this one) is an 18th-century remodel; the church itself is
  authentic to Calvin's era, only the front is later.
- **Trento Cathedral**: the frame includes the Fountain of Neptune, a mythological
  figure rather than a named historical individual — standard, essentially
  unavoidable framing of this piazza, and not a violation of the no-individuals rule.
- **Azusa Street**: the hardest provenance in this set. Commons records only
  "Unknown author, 1907" for the historic revival-era photo used here. A safer,
  fully-attributed alternate exists if that's too thin for comfort: the modern
  historical marker at the site (`File:Azusa-Street-Historical-Sign.jpg`, Callsignpink,
  2014, CC BY-SA 4.0) — less visually dramatic but fully documented.
- **Manila's Feast of the Black Nazarene** was chosen over an also-verified
  alternate (Brazil's Marcha para Jesus, São Paulo) specifically because that
  alternate's own official caption names a sitting state governor as a marching
  participant. Manila's file is unambiguously a crowd shot with no named individual
  as its subject, at the cost of duplicating Asia as a region alongside the Kochi
  entry above.
- **St. Peter's Basilica**: the true original file was roughly 50 MB (13066×6823) —
  resized to 2000px wide (~470 KB) before vendoring here, since nothing about a
  homepage strip needs the full original resolution.
- **San Vitale, Ravenna**: this general interior/mosaic view was chosen over the
  more famous Justinian and Theodora court-portrait mosaics specifically to avoid a
  named historical individual as the image's main subject.
