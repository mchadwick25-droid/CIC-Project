# World Media, Era-Spanning — homepage image strip

**⚠ IMAGES NOT YET DOWNLOADED — see "The download blocker" below.** All 8
candidates are found, license-verified, and documented; the actual JPG
files could not be fetched from this sandbox. Every folder carries a
`DOWNLOAD-PENDING.md` with the exact URL to fetch instead.

Eight real historical photographs for a homepage image strip on
churchinconversation.com, spanning the full ~2000-year story of the
Church — the existing CiC source library (`cic/texts/`) and the existing
`../World-Media/` tile set both cover only 70-450 CE; this set is meant to
carry the story the rest of the way, from the early medieval manuscript
tradition through a 21st-century Global South congregation.

Same discipline as `../World-Media/`: one real, historically-matched
photo per slot, sourced from Wikimedia Commons (or, in one case, English
Wikipedia's own local file repository — see the Yamoussoukro entry below),
verified individually for a genuine period/subject match and an actual
open license, not stock imagery.

## Files

| Folder | Image | Period | Story beat |
|---|---|---|---|
| `book-of-kells/` | `kells-folio-292r-incipit-john.jpg` | c. 800 CE | The manuscript-and-monastery Church |
| `chartres-cathedral/` | `notre-dame-de-chartres.jpg` | c. 1220 | High Gothic cathedral-building |
| `hagia-sophia-mosaic/` | `christ-pantocrator-deesis-mosaic.jpg` | c. 1261 | Byzantine/Eastern Christianity, the Great Schism's own world |
| `gutenberg-bible/` | `gutenberg-bible-nypl-lenox-copy.jpg` | c. 1455 | The printing press as its own turning point |
| `wittenberg-theses-door/` | `lutherstadt-wittenberg-theses-door.jpg` | 1517 | The Reformation |
| `mother-bethel-ame/` | `mother-bethel-ame-church-philadelphia.jpg` | founded 1794 | Black American Christianity, under and after slavery |
| `yamoussoukro-basilica/` | `notre-dame-de-la-paix-yamoussoukro.jpg` | 1989 | The Global South church, as monumental architecture |
| `nigeria-congregation/` | `worship-service-word-of-life-warri-nigeria.jpg` | 2016 | The Global South church, as a gathered congregation |

Four (Kells, Chartres, Wittenberg, Yamoussoukro) came in already
identified, with their licenses said to be pre-verified via en.wikipedia.org's
own API; four (Hagia Sophia, Gutenberg, Mother Bethel, Nigeria) were
researched fresh for this pass. **All eight were independently re-verified
this pass regardless** — the four "already verified" ones are exactly as
strong as claimed, and the exercise also caught nothing wrong with them,
which is itself worth stating rather than assuming.

## Sourcing metadata — `era-spanning-media-sources.json`

Same schema as `../world-media-sources.json`: `file`, `title`, `location`,
`period`, `story`, `source_url`, `author`, `date_taken`, `license`,
`attribution`, and a `note` field per entry carrying the verification
method and any honest caveat.

**License note.** Four different license regimes appear in this set, not
just one: **CC BY-SA** (2.0 through 4.0, three images — attribution and
share-alike required), **Public domain** (two images — the Book of Kells
page and the Hagia Sophia mosaic, attribution not legally required but
credited as good practice), and the **Free Art License (FAL)** (one
image — the Wittenberg door, a copyleft license distinct from Creative
Commons that also requires attribution and share-alike). Don't drop
attribution on the CC BY-SA or FAL images when these go live.

## The download blocker

Every license, author, and date below was confirmed by a **direct fetch**
of the MediaWiki API (`action=query&prop=imageinfo&iiprop=extmetadata`) —
never assumed, never carried over from a caption. But `commons.wikimedia.org`
and `upload.wikimedia.org` are both blocked outright by this sandbox's
network egress policy (confirmed via both `curl` and the WebFetch tool,
returning an explicit `EGRESS_BLOCKED` error, not a transient rate limit) —
the same class of restriction `CLAUDE.md` already documents for the
patristic text hosts (`cic/texts/` sourcing), just extended here to
Wikimedia's own image infrastructure.

**The workaround found for verification, not for download:**
`en.wikipedia.org`'s own API is *not* blocked, and MediaWiki's federated
file-repository design means it will serve full `extmetadata` for a file
that physically lives on Commons, as if it were a local file — this is
how all seven Commons-hosted images in this set got verified. It does
**not** help with downloading the actual image bytes, since the file URL
itself still resolves to `upload.wikimedia.org`.

**What this means practically:** every folder has its real content
researched, matched, and rights-cleared, plus a `DOWNLOAD-PENDING.md`
naming the exact URL to fetch. Whoever runs this from an environment that
can reach `upload.wikimedia.org` directly (or Mark's own machine) can pull
all eight files in one pass — nothing else about the sourcing work needs
redoing.

## Honest caveats, carried over from the sourcing research

Two of these have the same kind of caveat `../World-Media/`'s own README
already flags for the Macarius and Jerome-grotto entries — the right
historical *site*, but not fully original fabric:

- **Wittenberg's door**: the visible bronze doors are an **1858
  commemorative recasting**, not the 1517 wooden original, which burned in
  the 18th century.
- **Mother Bethel**: the visible building is the **fourth structure**
  on this ground, completed in **1890** — not the 1794 original, a
  converted blacksmith's shop. The land's continuous Black ownership since
  1791 is the real continuity; the standing building is not.

Two more are worth noting for different reasons:

- **Hagia Sophia's mosaic**: the building itself returned to active use as
  a mosque in 2020; the mosaic is periodically curtained during prayer
  times. Not hidden permanently, but its current religious status is live
  and contested, not a settled museum past.
- **Yamoussoukro's basilica**: the source file is hosted **locally on
  English Wikipedia, not Wikimedia Commons** — confirmed directly via the
  file's own page, which explains that the depicted *building* may not
  clear Côte d'Ivoire's own copyright law (no confirmed freedom-of-panorama
  exception there) even though the photographer's own CC BY-SA license is
  fully free. Use the `en.wikipedia.org` file-page URL in the JSON, not a
  Commons search, if this ever needs re-verifying.

One candidate research direction was tried and is worth naming for the
next pass: a **house-church gathering in China** (per the task's own
suggested alternative to Nigeria/South Korea) was not pursued once the
Nigeria candidate — a real, VRT-permission-confirmed photograph of an
actual 2016 worship service — turned up a strong match; a Chinese
house-church photo would face real practical obstacles a Nigerian
megachurch service does not (most active house-church photography is not
freely licensed, for the same reasons those churches often meet quietly).
