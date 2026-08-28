---
id: pahc.contested.egypt-exclusion
world_id: post-apostolic-house-church
record_type: contested_claim
schema_version: 2
status: draft
register: etic
canon_cells: []
confidence:
  citation_specificity: D
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Inferential-Thin
  divergence_note: "The papyrological silence argument itself is single-source (Bagnall's survey) and this build cannot independently check it against a vendored primary text. But it is not this world's only support for the exclusion: Doc_01 SS8.2 also grounds the Alexandria distinction on formation logic (household- and correspondence-based pastoral formation here, versus a teaching-relationship-based exegetical-philosophical formation there), and the Step 0 Conclusion independently dates the Alexandrian tradition's own emergence to c. 190-254 CE - a second, Bagnall-independent line, carried forward at Step 6 in pahc.force.alexandria-emergence. The exclusion rests substantially, not entirely, on the papyrological silence argument alone."
sources:
- source_id: pahc.core.house-church
  locus: "caution 7 (EGYPT EXCLUDED) - the settled scoping decision this record carries forward into participant-facing form"
  license: public-domain
claim: "Egypt and Alexandria are excluded from this world's own geographic scope - this world's own communities are Antioch/Syria, the cities of western Asia Minor, and Rome only - substantially on the strength of Roger Bagnall's papyrological survey (Early Christian Books in Egypt, Princeton, 2009), which finds Egyptian Christian evidence essentially silent before Bishop Demetrius's episcopate (189-231 CE)."
held_against:
- "An argument from documentary silence is not the same as positive evidence of absence - Egyptian Christianity could have existed and left no securely datable papyrological trace within this specific window for reasons unrelated to whether it existed (differential survival, dating uncertainty in fragmentary papyri, or simply a research gap this build has not independently verified)."
- "The papyrological silence argument specifically is a single-scholar dependency (Bagnall), structurally similar in kind to the Ignatius-corpus dependency this build already flags elsewhere, though bearing on this world's geographic boundary rather than its internal content - even though it is not the exclusion's only support (see divergence_note), it remains the one piece of this reasoning resting on a single un-corroborated survey."
concedes: "If Bagnall's own reading is wrong, or if Egyptian Christian communities existed within this window without leaving papyrological trace this survey could capture, the papyrological half of this exclusion's support would weaken - though the separate formation-logic distinction (Doc_01 SS8.2) and the Alexandrian tradition's own independently-dated later emergence (pahc.force.alexandria-emergence) would still stand on their own. This is named here as a load-bearing dependency on Bagnall specifically, per pahc.core.house-church's own caution 7's 'substantially' wording, not resolved - the exclusion is carried forward as this build's working scope, disclosed rather than defended as certain."
divergence_partners:
- pahc.force.alexandria-emergence
---
Carries forward pahc.core.house-church's own caution 7 (EGYPT EXCLUDED)
into participant-facing form. No pahc.source record exists for Bagnall's
survey because none is available: it is secondary scholarship, not a
primary text this world's registry vendors, and this record does not
manufacture a source citation to look more grounded than the underlying
dependency actually is - Bagnall stays named in the claim's own prose,
disclosed as this build's unverified dependency. sources[] instead names
pahc.core.house-church, the record whose caution this one carries
forward - the same intermediate-record citing convention the rest of the
fleet already uses (added 2026-08-28, after the live admission run's
evidence-pressure probe cited this record and M3's source-boundedness
check found it the only one of the fleet's 40 contested_claim records
with no grounding chain at all; the fix names this record's real
internal ground, it does not touch the Bagnall disclosure). This is Step 0/Doc_01's own
settled scoping decision - this record restates and discloses it in
participant-facing form, and does not propose reopening it. canon_cells
left empty: no fleet canon question asks participant-facing "why does
your own world exclude Egypt," and this is a build-scoping decision
rather than a question this world's own voice would be asked directly.

FIXED at Step 7 round-1 review, three corrections: (1) held_against and
divergence_note previously overstated this as a pure single-source
dependency with "no second, independent corroborating line" - false
against this build's own records: Doc_01 SS8.2's formation-logic
distinction and the Step 0 Conclusion's independent c. 190-254 CE dating
of the Alexandrian tradition (carried forward at Step 6 in
pahc.force.alexandria-emergence, built with no reliance on Bagnall at
all) are a second, genuinely independent line - corrected to caution 7's
own "substantially," not "entirely." (2) The former held_against[2] was
a procedural defense of the build's own scope authority, not a
counter-position, and has been removed - the same point already lives
in this note. (3) The claim's own silence-window was corrected from
this world's whole 70-200 CE span to what Doc_01 SS3 actually states:
essentially silent before Bishop Demetrius's episcopate (189-231 CE),
and the monograph is now named so the disclosure is independently
checkable. Separately: pahc.contested.didache-dating now discloses a
live tension this exclusion creates with the Didache's own unresolved
Syria/Egypt provenance - if an Egyptian provenance for the Didache is
right, this world's central catechetical text traces to the one region
this exclusion removes from scope. Neither record resolves that
tension; both now name it.
