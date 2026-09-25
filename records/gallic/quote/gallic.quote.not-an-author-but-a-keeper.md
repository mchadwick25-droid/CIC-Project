---
id: gallic.quote.not-an-author-but-a-keeper
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Vincent's own exposition of 1 Tim. vi. 20 ("Keep the deposit") in the Commonitory
    (ch. 22 [53]).
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "Commonitory ch. 22 [53] (npnf211 div iii.xxiii, file lines 13769-13774): Vincent expounds 'Keep the deposit' (1 Tim. vi. 20)"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks how Vincent understood the role of a teacher or guardian of doctrine"
  - "participant asks what 'the deposit' meant to Vincent, and what it means to keep it rather than invent it"
  prefer_instead:
  - "participant asks about 1 Tim. vi. 20 as Scripture in general - this record carries Vincent's own exposition of the verse, not a general commentary on the epistle"
text: >-
  That which has been intrusted to thee, not that which thou hast
  thyself devised: a matter not of wit, but of learning; not of private
  adoption, but of public tradition; a matter brought to thee, not put
  forth by thee, wherein thou art bound to be not an author but a
  keeper, not a teacher but a disciple, not a leader but a follower.
speaker_or_author: gallic.figure.vincent
license: verbatim
modern_lens_note: >-
  Vincent builds this as a series of contrasts - not wit but learning, not private but public, not
  author but keeper, not teacher but disciple, not leader but follower - each one narrowing the same
  point: a guardian of doctrine adds nothing of his own. The line names, in Vincent's own words, the
  posture this whole world takes toward its own inheritance.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.gravity.received-not-invented
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"not an author but a keeper"` returns one hit, line 13773, inside `<div2 title="Chapter XXII. A more
particular Exposition of 1 Tim. vi. 20." ... id="iii.xxiii">`. The passage runs lines 13769-13774:
"That which has been intrusted to thee, not that which thou hast thyself devised: a matter not of
wit, but of learning; not of private adoption, but of public tradition; a matter brought to thee, not
put forth by thee, wherein thou art bound to be not an author but a keeper, not a teacher but a
disciple, not a leader but a follower." Vincent's own preceding rhetorical question ("'Keep the
deposit.' What is 'The deposit'?") is left outside the `text` field as framing, not part of the answer
itself.

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
