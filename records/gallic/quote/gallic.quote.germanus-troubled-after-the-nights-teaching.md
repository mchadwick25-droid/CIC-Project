---
id: gallic.quote.germanus-troubled-after-the-nights-teaching
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-I
- F1-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Documented as Cassian's own text (Conferences XIII.1, read at its locus for this record) and Widely
    Accepted as his own first-person report of his and Germanus's experience - "we returned," "we were
    puzzling," neither received tradition about a third party. The previous night's teaching this
    scruple responds to (Conference XII, On Chastity) is itself absent from the vendored edition, marked
    "Not translated"; this record carries only what Cassian says about that teaching in this chapter's
    own summary of it, not the teaching itself.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "Conferences XIII.1 (npnf211 div iv.v.iv.i, file lines 37489-37505): the scruple that arose at morning service after the previous night's discussion, and Chaeremon's arrival"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how the grace-and-effort argument actually started, or what Germanus was troubled about"
  - "participant asks whether the monks argued about grace as a practical, felt problem rather than a theory"
  prefer_instead:
  - "participant wants Chaeremon's actual answer, the husbandman argument - retrieve gallic.quote.germanus-and-chaeremon-on-the-husbandman"
  - "participant asks what Conference XII said about chastity - the vendored edition does not contain it, and the Representative must say so"
text: >-
  When after a short sleep we returned for morning service and were waiting for the old man, Abbot
  Germanus was troubled by great scruples because in the previous discussion, the force of which had
  inspired us with the utmost longing for this chastity which was till now unknown to us, the blessed old
  man had by the addition of a single sentence broken down the claims of man's exertions, adding that man
  even though he strive with all his might for a good result, yet cannot become master of what is good
  unless he has acquired it simply by the gift of Divine bounty and not by the efforts of his own toil.
  While then we were puzzling over this question the blessed Chæremon arrived at the cell, and as he saw
  that we were whispering together about something, he cut the service of prayers and Psalms shorter than
  usual, and asked us what was the matter.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  The trouble is not abstract. Two friends spend a sleepless stretch of the night turning over "a single
  sentence" from an elder's teaching, still awake enough at morning prayer that a second elder notices
  them whispering and shortens the service to ask what is wrong. The doctrine of grace and effort, as
  Cassian records its own beginning, starts as a monk's felt objection to being told his striving cannot
  make him master of the good - not as a position taken up in an argument with people across the sea.
modern_rendering: >-
  After a short sleep we came back for the morning service and waited for the old man. Abbot Germanus
  was troubled by great doubts, because of the discussion the night before. Its force had filled us with
  the deepest longing for this chastity, which until then we had not known. In it, by adding a single
  sentence, the blessed old man had broken down the claims of human effort. He added that a man may
  strive with all his might for a good result, yet still cannot make the good his own. He can have it
  only as a simple gift of God's generosity, not through the efforts of his own labor. While we were
  puzzling over this question, the blessed Chaeremon arrived at the cell. He saw that we were whispering
  together about something. So he cut the prayers and psalms shorter than usual, and asked us what was
  the matter.
relations:
- type: associated-with
  target: gallic.story.germanus-scruple-at-morning-service
use_note:
  means: "Cassian relates that Germanus was troubled at morning service by an elder's saying that no one masters the good without God's gift, until Chaeremon arrived."
  not_for:
    - "the content of Conference XII, which is untranslated in the vendored edition"
    - "Chaeremon's answer, which sits in gallic.quote.germanus-and-chaeremon-on-the-husbandman"
    - "a reply to Augustine, when Cassian presents it as a monk's felt scruple"
  years: {from: 426, to: 426}
  status: provisional
---
Verified verbatim directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "Chæremon"` locates Conference
XIII at `<div3 title="Conference XIII. The Third Conference of Abbot Chæremon..." ... id="iv.v.iv">` (line
37475); Chapter I is `<div4 title="Chapter I. Introduction." ... id="iv.v.iv.i">` (line 37483). The quoted
span is `sed -n '37489,37505p'`, from "When after a short sleep we returned for morning service..." through
"...asked us what was the matter."

Normalization: hard-wrapped lines joined with single spaces. The vendored edition prints "Chæremon" with
the ae ligature; it is spelled "Chaeremon" here in plain ASCII, matching the host record's own established
normalization. No word was added, dropped, substituted, or reordered.

speaker_or_author is gallic.figure.cassian: this is Cassian's own first-person narration, opening
Conference XIII, of what he and Germanus experienced.
