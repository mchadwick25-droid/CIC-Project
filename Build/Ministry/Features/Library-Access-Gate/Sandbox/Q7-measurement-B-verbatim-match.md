# Q7 — Measurement: does Direction B's verbatim-in-shelf gate actually match?

**Sandbox artifact, 2026-09-15.** A commissioned measurement, not a design
document and not a ruling. Mark approved running this before the design
converges, because it decides whether Direction B (`D1-Directions.md` §3,
"Bytes, not pointers") is viable before anyone costs it out further. This
answers D2's own open item 7(b) (`D2-Struggle.md` §6, item 7): *"run B's
verbatim window-match against the 225 emic quotes before costing B — a low
match rate is either a real finding about the records or proof the gate
cannot be blocking."*

This is a real measurement, run against the real checkout on 2026-09-15: 117
vendored files under `cic/texts/`, all 55 real `cic/corpus-map/` buckets, and
every emic, verbatim-licensed quote record in the nine built worlds. Nothing
below is estimated or extrapolated from a sample.

---

## 1. Methodology actually used

**Population.** Every `record_type: quote` file under `records/<world>/quote/`
for the nine formation worlds with a real `census_id` in `records/worlds.yaml`
(`alx, cappadocian, desert, don, gallic, hal, ijc, pahc, syr` — `fix` excluded,
its `census_id` is `null`, per the charter's own instruction), filtered to
`register: emic` and `license: verbatim`. That is **221 records**, out of 222
emic quote records in those nine worlds (the 222nd is the fleet's one
`license: do-not-voice` emic quote, out of scope for a *verbatim* gate) and
243 quote records total.

This cross-checks cleanly against both D1 and D2's own counts without any
adjustment: 243 total quote records across the nine worlds matches D1's table
exactly; 243 − 222 = 21 etic quotes, matching D2's independently-confirmed "21
`etic`" fleet figure exactly; and D1's fleet-wide "225 emic quotes" (which
includes `fix`, per D2's reconciliation) is 222 + 3, consistent with `fix`
contributing 3 more. The population this measurement runs against is the same
population the design docs are citing, not a differently-assembled subset.

**Own shelf vs. complement vs. neither — exactly D1's own described
mechanism, reused, not reinterpreted.** D1 §3 Direction B states
`gate_quote_in_shelf` precisely: a verbatim quote "must window-match... inside
its own world's extract"; a quote "that matches only in units tagged
`context`/`antecedent`/`transmission` may not be `register: emic`"; a quote
"that matches nowhere in the extract fails, whatever its `source_id` says."
That gives four possible outcomes, which this measurement computes directly
per quote, **ignoring what the quote's own `sources[].source_id` claims** —
exactly as the gate is specified to:

1. **own-shelf-tradition** — the quote's text window-matches inside a file
   assigned `role: tradition` in the quote's own world's corpus-map bucket
   (`cic/corpus-map/<census_id>.yaml`). Clean pass: I1, I2 (at file grain —
   see the caveat below), I4, and I3 all hold.
2. **own-shelf-other-role** — no match in a `tradition`-role file of the
   world's own bucket, but a match inside a file the same bucket assigns
   `context`, `antecedent`, or `transmission`. This is D1's own I3 case:
   the bytes are genuinely on the world's own shelf, but in a unit tagged
   evidence-only — the gate as specified would withhold this quote from
   voicing as `register: emic`.
3. **complement-only** — no match anywhere in the world's own bucket (any
   role), but a match somewhere else among the 117 vendored files — i.e.
   inside a file that is either assigned to a *different* tradition's
   bucket, or not assigned to any bucket at all. This is "matches only in
   material this world's own shelf does not include."
4. **no-match** — no match anywhere in the vendored library at all.

**The matcher itself is reused unmodified, not reimplemented.**
`_normalize()` is imported directly from `engine/m4/grounding_net.py`
(`re.sub` lowercasing/stripping to `[a-z0-9\s]`, collapsed whitespace). The
window logic is the same shape as `grounding_net._span_in_records`: split the
normalized quote text into words, take the whole string as one window if it
is ≤6 words, else every 6-word sliding window, and check `window in haystack`
— the identical rule the runtime net already uses to decide whether a quoted
span in a live turn may stream. The only difference from
`_span_in_records` itself is what the haystack is built from: the runtime
checks against a *record's* own tagged text (`all_text(record)`); this
measurement checks against a *shelf extract* — the world's assigned
`cic/texts/` files — because that is what Direction B proposes checking
against instead. The haystack text itself comes from
`cic/engine/corpus_index.passage_units()`, the exact extractor D1 §3.B step 1
names ("`corpus_index.passage_units` already yields `{locus, title,
apparatus, text}` per `div`") — ThML tag-stripped per-div text for the 38 XML
files, single whole-file text for the 79 plain-text files with no div
markup, unchanged from what that function already does for the real index.

Bucket membership comes from `cic/engine/corpus_map.load()` (real
`yaml.safe_load` over all 55 bucket files), **not** `tools/gen_shelf.py`'s
`parse_bucket` — D2 §1.3(a) found that reader silently truncates 30% of bucket
rows' fields, and this measurement does not want to inherit that defect.

**The grain limitation, stated plainly, per the task's own instruction to say
so rather than approximate.** D1 and D2 both flag that locus-grain
confinement needs a `locus_ids` field on staging rows that does not exist yet
— today a bucket's `locus` is free prose ("`div2 5.4 — On Baptism, Against the
Donatists (7 books)`"), not a resolvable set of div ids. Building that
resolver was out of scope for this measurement (it is real, uncosted design
work in its own right, named by both D1 and D2 as one of the two things "two
of five directions depend on"). So **this measurement operates at file
grain**: "own shelf" means the quote's world assigns the *file* the quote
matched in, at whatever role, not that the match falls inside the
specific locus the bucket row names within that file. This makes the
own-shelf match rate below an **optimistic upper bound** on what a real,
locus-grain `gate_quote_in_shelf` would pass — a match that lands in the
right file but in a different part of it than the bucket row's stated locus
would still count here as "own-shelf" but might fail a true locus check.
I did not attempt to hand-verify locus placement for all 217 own-shelf
matches; that would be the next, more expensive measurement if this one's
result makes it worth running.

No step was blocked. The matcher was reusable as described, the extractor was
reusable as described, the bucket loader was reusable as described (once the
broken `gen_shelf.py` reader was avoided), and the records were exactly where
the D1/D2 docs said the counts came from.

---

## 2. The tally

| tier | count | % of 221 |
|---|---:|---:|
| own-shelf, tradition-role | 208 | 94.1% |
| own-shelf, other-role (context/antecedent/transmission) | 9 | 4.1% |
| complement-only (matches, but only off this world's own shelf) | 3 | 1.4% |
| no-match anywhere in the vendored library | 1 | 0.5% |
| **total** | **221** | **100%** |

Combined: **217/221 (98.2%) match somewhere on the quote's own world's
shelf** (tradition- or other-role); **220/221 (99.5%) match somewhere in the
vendored library at all.**

By world:

| world | n | tradition | other-role | complement | no-match |
|---|---:|---:|---:|---:|---:|
| alx | 25 | 24 | 1 | 0 | 0 |
| cappadocian | 19 | 19 | 0 | 0 | 0 |
| desert | 53 | 53 | 0 | 0 | 0 |
| don | 5 | 2 | 2 | 0 | 1 |
| gallic | 3 | 3 | 0 | 0 | 0 |
| hal | 28 | 27 | 0 | 1 | 0 |
| ijc | 37 | 36 | 1 | 0 | 0 |
| pahc | 20 | 19 | 1 | 0 | 0 |
| syr | 31 | 25 | 4 | 2 | 0 |

**Donatism is the outlier, sharply.** 3 of its 5 verbatim emic quotes (60%)
either match only in `context`-tagged material or don't match at all — a
rate strikingly close to D2's own, independently derived, 61%-of-Donatism
figure (`D2-Struggle.md` §2), even though that number came from a completely
different method (resolving each citation's `source_id` → file → bucket
role, not brute-force text matching against the shelf). Two unrelated
measurements, two different techniques, landing on the same number for the
same world is a real cross-check, not a coincidence worth explaining away.

## 3. Examples

**own-shelf-tradition (clean pass)** — the large majority, e.g.
`alx.quote.a-doctrine-they-would-not-have-taught`, `desert` quotes broadly,
`cappadocian` quotes broadly: ordinary verbatim citations that match inside
the world's own tradition-tagged shelf material.

**own-shelf-other-role (the I3 case, reproduced at byte level)**

- `don.quote.deo-laudes` — text `DEO LAVDES`. This is the record D1/D2 both
  flag as the one witness in Donatism's whole corpus with no hostile hand
  between the reader and the words (a Donatist acclamation carved on stone,
  CIL VIII). It matches verbatim inside
  `cil8-supplementum-numidiae_cagnat-schmidt1894.txt` — which is assigned
  `role: context` in `donatism.yaml`, not `tradition`. The one inscription
  that is genuinely, unmediatedly the Donatists' own words is shelved as
  "someone else's evidence" under the current role vocabulary.
- `don.quote.donatus-quid-est-imperatori` — `"Quid est imperatori cum
  ecclesia?"` ("What has the Emperor to do with the Church?"), the movement's
  founder's own words, transmitted inside Optatus's anti-Donatist polemic
  (`optatus_against-the-donatists.txt`, also `role: context`).
- `syr.quote.the-temple-of-the-church-of-the-christians` and
  `syr.quote.symeon-and-usthazanes` — Syriac Christians' own experience under
  Persian persecution, surviving only inside a Greek ecclesiastical history
  (context-tagged for `syr`).
- `alx.quote.dionysius-nepos`, `pahc.quote.two-female-slaves-...`,
  `ijc.quote.the-reading-of-all-the-documents` — the same shape: a genuine
  primary voice (Dionysius of Alexandria; the two tortured deaconesses named
  in Pliny's own letter; a council's own recorded acclamations) surviving
  only inside a work the corpus map tags as another party's document.

Every one of these is the "embedded voice" / "attested-by" case
`cic/engine/corpus_map.py`'s own docstring already names and explicitly
declines to encode as a role. This measurement finds it independently, by
matching actual bytes rather than resolving pointers, in 9 of 221 real
verbatim quotes — not a hypothetical, a *measured* 4.1% of the population a
literal reading of `gate_quote_in_shelf` would withhold from voicing on day
one.

**complement-only** (all 3)

- `hal.quote.a-man-truly-catholic` matches inside
  `npnf211_sulpitius-severus-vincent-lerins-cassian.xml` — a file assigned
  in seven *other* census buckets (desert, gallic, ijc, early-benedictine,
  apocrypha, antiochene-exegetical, priscillianist) but **not in `hal`'s own
  bucket at all.** Genuinely off `hal`'s own shelf.
- `syr.quote.palladius-hospitaller` matches inside
  `palladius_lausiac-history_clarke1918.txt`, assigned only to
  `desert-monasticism` — not to `syriac-edessa-nisibis`.
- `syr.quote.theodoret-gnats` matches inside
  `npnf203_theodoret-jerome-gennadius-rufinus.xml`, assigned to nine other
  census entries (including, notably, both `context` *and* `tradition` roles
  for `hal` itself) but not to `syr`.

**no-match** (the only one)

- `don.quote.emeritus-magno-argumento` — text `"Magno argumento veritas
  occultatur; ut cum ad inquisitionem nostram modicum quid ex parte adversa
  prolatum sit, cetera sileantur."` The record's own `divergence_note`
  already says this quote was "independently re-confirmed this session by
  reading the raw file directly at line 126834" of
  `pl11-zeno-optatus-collatio-carthaginiensis_migne.txt`, and names that
  scan's OCR as "notably poor even by this corpus's own standards." Checked
  directly: line 126834 of the vendored file reads *"Emeritus episcopus
  dtxii. Magno irgnmento vc-rilas occullaiur; ut cuui ad Inquhritionem
  noslram niodicum quid ex parte adversa prolatum sit, ca-lera sileanttir."*
  The quote is there — a human already verified it, on this exact line — but
  the vendored text is OCR-garbled enough (`irgnmento`/`argumento`,
  `vc-rilas`/`veritas`, `occullaiur`/`occultatur`, `noslram`/`nostram`,
  `ca-lera`/`cetera`) that no 6-word normalized window from the record's
  critically-corrected Latin appears verbatim in the scan. This is not a
  fabricated or misattributed quote; it is a real quote defeated by a real
  scan-quality problem the project's own build session had already flagged
  before this measurement ever ran.

---

## 4. Verdict

Both things asked for are true at once, and neither should be shaded to
favor the other.

**The core claim behind Direction B holds up well.** 98.2% of the fleet's
emic, verbatim-licensed quotes are, in fact, present as real bytes somewhere
on their own world's own corpus-map shelf — not fabricated, not
systematically pointing at the wrong tradition's material, not a body of
citations resting on trust rather than text. Given that this project
believed, incorrectly, that a verbatim-against-file check already existed
(D1 §1.3, D2 §1.1's independent confirmation of the correction), there was a
real possibility this measurement would turn up widespread drift between
what quote records claim and what the vendored files actually contain. It
did not. **A window-match gate built the way D1 describes it would, on the
data as it exists today, pass the overwhelming majority of the fleet's real
verbatim quotes without alteration.** That is a genuine, positive finding
about the fleet's citation discipline, independent of which direction Mark
eventually picks — it means the "never invent" discipline this project holds
itself to has, in fact, been mostly followed at the byte level, checked
mechanically for the first time.

**At the same time, this measurement reveals two real, distinct data
problems that exist regardless of which direction converges, and a
specification problem D2 already found by a different route.**

1. **The I3 role-vocabulary problem is real, and now confirmed twice, by two
   independent methods.** 9 of 221 quotes (4.1%, rising to 40% of
   Donatism's own 5) are genuinely on their own world's shelf, byte-verified,
   and would still be withheld from voicing under a literal reading of
   `gate_quote_in_shelf`'s I3 clause — because corpus-map's `role` describes
   a *work*, and voicing permission is a property of the *speaker quoted
   inside it*, exactly as `cic/engine/corpus_map.py`'s own docstring already
   says and exactly as D2 §2 already found by resolving citations instead of
   matching bytes. This is not a measurement artifact of one method; it is
   the same finding arrived at twice, independently. **Any direction that
   maps corpus-map role directly onto voicing permission — which is all five
   in D1 — inherits this, not just Direction B.**
2. **A small number of quotes are cited from material genuinely absent from
   their own world's shelf.** 3 of 221 (1.4%) — real, findable, correctly
   quoted text, but the file it lives in simply isn't assigned to that
   world's own bucket, while it is assigned to others'. This is a
   corpus-map completeness question (some buckets are missing rows for
   material their own world's records already legitimately cite), not a
   fabrication question and not something any of the five directions'
   *enforcement* design can fix on its own — it needs bucket rows added, the
   classification work the charter puts out of this workstream's scope but
   which D2 §5.3 already flagged as unavoidable for any direction that goes
   blocking.
3. **At least one vendored scan's OCR quality is bad enough to defeat exact
   verbatim matching even on a quote a human has already hand-verified
   against that exact line of that exact file.** 1 of 221 (0.5%) fleet-wide,
   but concentrated in Donatism (whose whole documentary base leans on a
   small number of difficult scans, per D2 §3/B), this is a corpus/vendoring
   data-quality issue, not a records issue and not a gate-design issue — a
   window-match gate here would need either a normalization tolerance wide
   enough to survive this OCR's noise (which D2 §3/B's "normalization trap"
   already warns is its own source-fidelity risk) or a re-scan/re-OCR of the
   file, and the honest answer, per the same discipline, is to say so rather
   than quietly widen the matcher's tolerance until it passes.

**So: this is not a case where the answer shades one way.** The match rate
says Direction B's central bet — that the fleet's verbatim quotes really are,
in bytes, where they claim to be — is sound and measurably so, at a rate high
enough that a locus-grain version of this gate looks buildable as a
*matching* mechanism, once the locus resolver (already known and separately
costed in both D1 and D2) exists. But the same measurement, run honestly,
surfaces a real 5.5% (12 of 221) of the fleet's existing verbatim quotes that
a literally-implemented `gate_quote_in_shelf` would refuse or withhold today
— for three different, genuine reasons (role-vocabulary mismatch, bucket
incompleteness, scan quality) that have nothing to do with whether Direction
B is the right architecture and everything to do with data the project needs
to fix, or a specification the project needs to revise, before *any*
role-gated or shelf-gated mechanism can go blocking without producing false
refusals on real, honest, already-verified scholarship. That fix is
classification and vendoring work this workstream's own charter puts out of
scope — which is exactly the fork D2 §5.3 already named for Mark.

**One caveat on the number itself, restated:** because this ran at file
grain (no `locus_ids` resolver exists yet), 94.1%/98.2% is an *optimistic*
reading of "own-shelf, tradition-role" — a locus-grain gate could find some
of those 208 matches land in the right file but the wrong part of it. That
would only move quotes from "clean pass" toward "own-shelf-other-role" or
"complement," i.e. it can only make the picture in §4 above more conservative,
never less.
