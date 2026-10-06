---
id: gallic.quote.martin-funeral-procession-ranks
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    The wording is Documented as Sulpitius's own text, describing a public procession he presents as
    witnessed and ordinary in kind (no miracle claimed in this passage). Widely Accepted rather than
    Documented because it is one author's letter, not independently corroborated.
sources:
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter III, To Bassula, His Mother-in-Law (npnf211 div ii.iii.iii, file lines 2495-2500): the procession''s own ranks - old men, young soldiers, and the choir of virgins'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks who marched at Martin's funeral, or how the procession was organized
  - participant asks about "soldier of Christ" language, or about women's presence in this world
  - participant uses "veterans," "recruits," or "virgins"
  prefer_instead:
  - participant is asking about women's presence at Tours specifically, beyond this one trace - outside
    our window and evidence
  - participant wants the crowd's size, not its internal ranks - retrieve
    gallic.quote.martin-funeral-crowd-and-monks
text: >-
  Undoubtedly the shepherd was then driving his own flocks before him—the pale crowds of that saintly
  multitude—bands arrayed in cloaks, either old men whose life-labor was finished, or young soldiers who
  had just taken the oath of allegiance to Christ. Then, too, there was the choir of virgins, abstaining
  out of modesty from weeping;
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  Sulpitius orders the procession like an army under its shepherd: veterans whose service is finished,
  recruits who have just sworn allegiance, and a choir of virgins set apart by their restraint rather
  than their tears. The military language ("oath of allegiance") is not incidental color; it is the
  same soldier-of-Christ idiom the letter uses for Martin's own death.
relations:
- type: associated-with
  target: gallic.story.death-of-martin-at-condate
- type: associated-with
  target: gallic.gravity.soldier-of-christ
- type: associated-with
  target: gallic.force.army-and-rank-before
modern_rendering: >-
  No doubt the shepherd was then driving his own flocks before him. They were the pale crowds of
  that holy multitude, bands dressed in cloaks. Some were old men whose life's labor was done.
  Others were young soldiers who had just sworn their oath of loyalty to Christ. Then came the
  company of virgins too, holding back their tears out of modesty.
use_note:
  means: "Sulpitius pictures Martin's funeral procession as a shepherd driving his flocks, with old men, newly sworn soldiers of Christ and a choir of virgins."
  not_for:
    - "literal soldiers, when the oath of allegiance is to Christ"
    - "the crowd size and monk count, which sits in gallic.quote.martin-funeral-crowd-and-monks"
  years: {from: 397, to: 397}
  status: reviewed
---
Verified verbatim against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"Undoubtedly the shepherd was then driving"` returns line 2495; `grep -n "abstaining out of modesty
from weeping"` returns line 2500. Read in full at lines 2495-2500: one continuous, unbroken run of
prose. The em dashes ("before him—the pale crowds...multitude—bands arrayed") are the source's own
punctuation (confirmed with `cat -A`: U+2014 EM DASH), carried here as "—" rather than a double hyphen.

No word was added, dropped, substituted, or reordered from the source's own wording; hard line wraps
were joined with single spaces.
