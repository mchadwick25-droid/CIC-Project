# Notes relocated out of records

These passages were build narration sitting in live records. The commentary check flags them on the promotion PR. Each is kept here word for word, with its source file. The record now carries only what describes the world or the source.

## records/witt/world_core/witt.core.witt.md

Removed: lines 235-251: the LIVING_TRADITIONS migration paragraph.

```text
LIVING_TRADITIONS - RESOLVED, migrated to the real .living_traditions frontmatter field above
(Open_Gaps_Tracking.md OG-45/OG-48/OG-49; see the updated B-7a note above for the full trace). This
paragraph originally carried the content as uncompiled body prose, authored before the schema field
existed, and its own status line read "Article 29 confirmation... is PENDING" - stale even at the time
of this update, since Doc_10 Section 6 and World Profile Section 9 both already recorded the actual
determination: **CONFIRMED**, the project lead's direct word, in session, 2026-09-19: "Confirm as
drafted." That determination - correspondence YES (a confessional family, per World Profile Section 9);
the three documented divergences (the territorial prince-and-council church not carried forward; the
evidential window closing by 1545-46 against the declared 1580 window, with the living tradition's own
history continuing for centuries beyond that, undocumented here; the 1543 treatise's existence disclosed
in .thinness/.cautions/.thin_topics as existence-only, with present-day engagement with it not
characterized, and the founder's own contested standing on this specific point per Doc_10 Section 6,
"Figures of Contested Standing," carried in witt.contested.1543-treatise-later-effect rather than
repeated here); and Version A runtime handling (this world does correspond to a living tradition, so the
Representative's own closing paragraph says so, per Doc_10 Section 6's own choice between the template's
Version A and Version B) - is now spoken directly in .living_traditions above, in the same we-voice as
.horizon/.formation_logic/.thinness/.cautions, rather than described about it here.
```

## records/witt/world_core/witt.core.witt.md

Removed: lines 184-215: the B-7a gap disclosure and its 2026-09-28 update.

```text
B-7a (S2.7a) FACILITATION GUIDANCE, added in the same authoring pass as B-7 (witt.voice.craft) above.
Per the process document's own B-7a row (CiC_Record_Native_World_Build_Process_V1_4.md, Phase B step
table): "Pairings riding LIVE partner claims with built-in cautions (ending-not-read-back both ways;
contemporaries-not-stages; the handoff containment class); telos (provisional/Art-31); living_traditions
(provisional for M2)." At authoring time, a genuine structural gap was disclosed before this content,
rather than silently worked around: no world_core record anywhere in the fleet carried telos,
living_traditions, or pairings as a schema field (checked directly: no hit for any of the three anywhere
under records/, and gallic.core.gallic's own record, the nearest B-7-adjacent precedent, had no B-7a
section at all). engine/m1/schemas.py's world_core TYPE_PROPERTIES had no telos, living_traditions, or
pairings property, and world_core's build_schema sets additionalProperties: False, so writing these
directly into this record's own frontmatter would have failed gate_schema_validation outright. Adding
the fields to the schema was an engine/ change, explicitly out of that authoring task's own scope (no
gate file, no engine file could be touched there).

**Update, 2026-09-28 (Open_Gaps_Tracking.md OG-45/OG-48/OG-49):** that gap is now closed for
living_traditions only. A Round 3 review found this exact content, approved and CONFIRMED
(witt_World_Profile.md Section 9; witt_Doc_10_Representative_Construction_Notes_Nikolaus.md Section 6;
2026-09-19, "Confirm as drafted"), was never reaching the deployed prompt, because the schema gap this
note disclosed at authoring time had never been closed. The project lead authorized the fix:
engine/m1/schemas.py's world_core TYPE_PROPERTIES now carries a real, optional, additive
living_traditions field (backward-compatible - existing world_core records validate unchanged without
it), engine/m2/builders.py's build_prompt() compiles it into the voice's own system prompt under a
"Living traditions" heading exactly as it already does for Horizon/Formation logic/Thinness/Cautions,
and this record's own living_traditions content above is that field - migrated out of the body prose
that used to carry it here, not newly authored (see the LIVING_TRADITIONS note below, kept as a pointer
rather than deleted, per this project's own append-only discipline for what a record's body once said).
telos and pairings remain genuinely open, fleet-wide, exactly as this note originally found them -
carried below in the body per this project's own file-discipline birth condition (dated build notes and
craft reasoning belong in the body, never invented as an unlisted frontmatter field), pending their own
future schema change-orders, the same way living_traditions itself just was. Flagged for the build
thread and for the schema's own maintainer, the same way the quote/doctrinal_witness gap is flagged in
witt.voice.craft's own body note rather than silently worked around.
```

## records/witt/world_core/witt.core.witt.md

Removed: lines 182-182: the derivation paragraph.

```text
world_core.horizon/.formation_logic/.thinness/.cautions/.thin_topics are all built directly from witt_World_Profile.md Section 1 (World Identity, temporal scope), Section 3 (Formation Logic, itself drawn verbatim in substance from witt_Doc_07_Integrated_Ecology_Analysis.md SS4.2), and Section 8 (Honest Limits, all six domains carried into .thinness and, split by topic, into .thin_topics); witt_Doc_01_World_Identification_Boundaries_Orientation.md SS2.1-SS2.3 (the declared 1517-1580 window, argued directly against its own strongest counter-candidates, 1555 and 'into the next generation'); witt_Doc_08_Forces_Document.md Discipline 2 (the declared-vs-evidential-window distinction, carried into .horizon and into confidence.divergence_note); witt_Doc_09_Story_Inventory.md SS5 (Absent Stories -- the tested witt-ABS-01 candidate plus the five-item wider pattern, all six carried into .thin_topics here); witt_Doc_02_Source_Ecology.md SS12.1-SS12.4 (Missing Voices; the binding disclosures on the 1525 and 1543 texts, carried into both .thinness and .cautions); and the Source Registry's own Named Comparanda (rows 55, 57, 58, 94), carried into .cautions. world_core.living_traditions is built directly from witt_World_Profile.md Section 9 (Living Tradition Status) and witt_Doc_10_Representative_Construction_Notes_Nikolaus.md Section 6 (Living Tradition Documentation): the correspondence determination (YES, a confessional family), the three documented divergences, and Version A runtime handling, all CONFIRMED by the project lead (Mark Chadwick) in session, 2026-09-19 ("Confirm as drafted") -- rendered in the same we-voice as .horizon/.formation_logic/.thinness/.cautions and drawn from the Permanent Prompt's own Living Traditions closing paragraph once it cleared the identical voice-perspective bar (converted from that paragraph's you/your address to this record's own we/our register, the same conversion already applied to paragraphs 4, 6-8, 17, 19, 23, 31, 33 below). Added to the schema and compiled for the first time in this authoring pass, per Open_Gaps_Tracking.md OG-45/OG-48 -- the field did not exist when this record was first authored, so this content originally sat below as uncompiled body prose; see the B-7a note below for the full disclosure and its own now-updated status. Phrasing in the spoken fields draws directly, where it already cleared the identical voice-perspective bar, from witt_Representative_Permanent_Prompt_Nikolaus.txt (paragraphs 4, 6-8, 17, 19, 23, 31, 33) -- confirmed by the identity decision (witt_Representative_Identity_Decision.md: Nikolaus, sexton-schoolmaster) to speak for this world's whole documented life, never anchored to one moment. time_window {1517, 1580} is Doc_01 SS2.2's own working ceiling (the Book of Concord as this world's most complete confessional self-definition), argued directly against 1555 (the Peace of Augsburg) as a real but non-competing internal-transition marker (Doc_01 SS2.3) -- not the narrower 1517-1545 evidential window World Profile Section 1 also names; that distinction is carried explicitly in .horizon, .thinness, and confidence.divergence_note rather than folded silently into one field. The six sources[] entries are this build's own judgment call for 'the most load-bearing Native rows' (Registry rows 2, 15, 25, 26, 37, 38): the founding act, the one documented internal crisis (1522), both catechisms, and both confessional documents -- chosen to span this world's own formation mechanism (G2-G5, G11) rather than its polemical or biographical registers, which are thinner and less load-bearing by the World Profile's own account (Section 2).
```

## records/rzg/source/rzg.source.ecclesiastical-ordinances-1541.md

Removed: divergence_note.

```text
  divergence_note: 'STALE, 2026-09-29: this record still describes the pre-2026-09-25 unacquired state
    for the 1541/1561 wording verbatim, which indeed remains unacquired. But a genuine PD alternative - the
    1576 Geneva Council revision of the same living ordinances, 1735 printing - was vendored 2026-09-25 as
    `calvin-geneva-council_ordonnances-ecclesiastiques-fra_tournes1735.txt` (Source_Registry.md row 18,
    Manifest G1 now CLOSED via that alternative). This record intentionally still names ONLY the unacquired
    1541/1561 verbatim text, not row 18''s later revision - a new source record for row 18 itself, and any
    consequent Doc_04 SS7 re-test of G4 (Consistorial Church Discipline) against it, is real work for a
    future pass, not performed here.'
```

## records/rzg/source/rzg.source.genevan-psalter.md

Removed: divergence_note.

```text
  divergence_note: 'STALE, 2026-09-29: this record still describes the pre-2026-09-25 unacquired state.
    The complete 1562 Psalter (French) was vendored 2026-09-25 as `marot-beze_pseaumes-mis-en-rime-francoise-fra_1562.txt`
    (Source_Registry.md row 19, Manifest G2 now CLOSED) - not reflected in this record''s own fields below,
    left as a disclosed staleness rather than silently rewritten, since updating `edition`/`rights_status`/`kind`
    to match row 19 and adding this record to any citing gravity/lexicon record''s `sources[]` is real package-layer
    work for a future pass, not performed here.'
```

## records/rzg/gravity/rzg.gravity.council-led-authority-vs-consistorial-independence.md

Removed: body paragraph.

```text
Built from Doc_04_Gravity_Discovery.md SS3 (Approved to proceed, Revision 2), carrying that document's own classification and reasoning directly. `relations` mirrors Doc_08 Section 5's own 'Connected forces' list for this gravity exactly, per that document's own explicit caution against force-fitting a connection its own words do not support. `sources` left empty deliberately (2026-09-29 Tier 4 sourcing pass): Doc_04 SS3.5/SS5 tests this tension against Doc_01's own already-confirmed institutional-historical characterization of each pole (Zurich's council-led governance; Geneva's 1541 Ordinances and the Perrinist crisis), not against a specific quoted locus in a vendored primary text - citing `rzg.source.ecclesiastical-ordinances-1541` here would misrepresent an unacquired (Confidence E) source as licensing this record's claim. `Source_Registry.md` row 18 (the 1576/1735 Ordonnances revision, vendored 2026-09-25) may supply a genuine direct-text locus for Geneva's pole on a future pass; not added here without re-testing against the actual text.
```

## Build/worlds/rzg/Source_Registry.md

Removed: the reconciliation narration in the closing paragraph, line 40.

```text
**rows 18–25 are newly added by this Tier 4 reconciliation pass (2026-09-29) and are not yet cited by any Doc_02/Doc_04/Doc_06 claim** — they were vendored into `cic/texts/` and the corpus-map on 2026-09-25 but never previously entered into this world's own Source Registry, a documentation gap this pass closes, not a new acquisition.
```

Also removed from the same file: the date 2026-09-25 from the rights re-verification notes of rows 28 and 29 (it stays in each row's vendored-date cell), and "yet" from "has not yet been located" (row 24) and "not yet acquired" (line 40).

## Promotion-PR wording edits that did not move text

The Build/worlds construction documents for witt and cappadocian, and engine comments and docstrings, lost only dates, "Mark, <date>" attributions and review-round or open-item wording. The meaning is unchanged. No passage was deleted in those files. The git history holds the original wording.
