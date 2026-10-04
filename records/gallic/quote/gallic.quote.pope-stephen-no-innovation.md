---
id: gallic.quote.pope-stephen-no-innovation
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Citation_specificity B because this is Vincent's own quotation of Pope Stephen's letter, itself
    not independently extant (the editors' endnote at this locus states Stephen's letter has not come
    down to us apart from Vincent's and Cyprian's citations of it). The wording carried here is
    Documented as it stands in Vincent's own text; whether it reproduces Stephen's letter with full
    accuracy is beyond what this record can verify.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "Commonitory ch. 6 [16] (npnf211 div iii.vii, file lines 12527-12528): Vincent quotes Pope Stephen's rule against novelty"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks for an example of a Pope's own words being used as an authority against novelty"
  - "participant asks what 'no innovation' meant as a rule in this world's own terms"
  prefer_instead:
  - "participant asks about the rebaptism controversy Stephen was addressing - this record carries only the rule Vincent quotes from his letter, not the controversy's history"
text: >-
  Let there be no innovation—nothing but what has been handed down.
speaker_or_author: Pope Stephen, as quoted by Vincent of Lérins (Comm. ch. 6)
license: verbatim
modern_lens_note: >-
  Vincent introduces this line as Stephen's own rule, written to Africa during the controversy over
  re-baptizing heretics. Vincent uses a Pope's own words to make his larger point: the instinct against
  novelty is not his invention either, but something he can point to in an earlier bishop of Rome.
modern_rendering: >-
  Let nothing new be brought in - nothing except what has been handed
  down.
relations:
- type: associated-with
  target: gallic.gravity.received-not-invented
use_note:
  means: "Vincent quotes Pope Stephen's rule, written to Africa in the dispute over rebaptism, that nothing be innovated beyond what has been handed down."
  not_for:
    - "a verified text of Stephen's letter, which survives only through Vincent's and Cyprian's citations"
    - "Pope Celestine's letter to Gaul, which sits in gallic.quote.vincent-celestines-letter-and-its-reading"
    - "Vincent's own keeper-not-author teaching, which sits in gallic.quote.not-an-author-but-a-keeper"
  years: {from: 434, to: 434}
  status: reviewed
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"no innovation"` returns a hit at line 12527, inside `<div2 title="Chapter VI. The example of Pope
Stephen in resisting the Iteration of Baptism." ... id="iii.vii">`. The quoted rule runs lines
12527-12528: "Let there be no innovation—nothing but what has been handed down." Vincent's own framing
sentence ("In fine, in an epistle sent at the time to Africa, he laid down this rule:") is left outside
the `text` field as the narrator's introduction, not part of the quoted rule itself, following the same
convention this corpus's other quote records use for narrator framing.

Normalization: line breaks joined with single spaces. The source wraps the quoted rule in curly
double quotation marks; dropped here as the edition's own punctuation marking a quotation, exactly as
a quotation is lifted from a printed page. No word added, dropped, substituted, or reordered.
