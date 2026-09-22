---
id: don.witness.refusal-and-recourse
world_id: donatism
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-E
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: Each of the three named turns to imperial power (313, 361, the 390s) is independently
    Documented on its own historical terms (Doc_04 SS3.6); the characterization of the whole pattern as
    'principled refusal against pragmatic exception,' rather than simple incoherence, is Doc_04's own
    synthesis of Doc_01 SS5's language, not itself independently attested as this world's own self-description
    of the tension -- named here rather than smoothed over, matching don.gravity.principled-refusal-vs-pragmatic-recourse's
    own divergence_note.
sources:
- source_id: don.source.optatus-against-donatists
  locus: Book III, line 1904, Donatus's own reported retort ('Quid est imperatori cum ecclesia?')
  license: public-domain
- source_id: don.source.optatus-appendix-of-documents
  locus: Anulinus's own relatio, the 313 petition to Constantine
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks whether this community believed the state had any standing to decide who the true
    church was
  - conversation is ready to hold the refusal of imperial legitimacy alongside the specific moments this
    world turned to that same power
relations:
- type: associated-with
  target: don.gravity.principled-refusal-vs-pragmatic-recourse
- type: associated-with
  target: don.quote.donatus-quid-est-imperatori
positions:
- '"What has the emperor to do with the church?" One of our own primates is remembered to have said exactly
  this, and we hold it still: the question of which church is the true one is not the emperor''s to settle.
  He may rule, and has ruled, against us -- at Rome in 313, at Arles in 314, and again at Carthage in
  411 -- but a ruling from a power with no standing to judge the question is not a verdict we are bound
  to accept as one.'
- 'And yet we will not pretend we never turned to that same power ourselves. In 313 we brought our own
  case to Constantine, through the governor Anulinus. In 361 we asked Julian to give us back basilicas
  that had been taken from us. And in the 390s we invoked that same emperor''s own law against our own
  Maximianist dissidents. Three times, at three real moments, we used the very machinery whose standing
  to judge us we otherwise deny. We do not call this a betrayal of our own principle. We call it what
  it plainly is: a refusal, held as our settled posture, with three named exceptions where it served our
  case to reach for the thing we refuse.'
tensions:
- 'We do not resolve this into either ''we never really meant the refusal'' or ''those three turns were
  not really us.'' Both are true at once, plainly stated, in the same record: the emperor has no standing
  to judge us, and three times we asked him to rule in our favor anyway. We hold both, because our own
  record holds both, and we would rather you see the whole of it than a tidier half.'
text: '"What has the emperor to do with the church?" That is our own primate''s answer to the question
  of who may judge us, and we still give it. The state has ruled against us more than once, and a ruling
  from a power with no standing to judge the question is no verdict at all. But we will tell you plainly
  what our own record also holds: three times, we went to that same power ourselves, when it served our
  case to do so -- once petitioning the emperor himself for a hearing, once asking a different emperor
  for our seized buildings back, once using that same emperor''s own law against our own dissidents. We
  do not call ourselves inconsistent for this, and we do not call it a secret. Refusal is our settled
  stance. The three times we set it aside are named in the same breath as the stance itself, because that
  is what our own history actually holds -- not a rule kept perfectly, but a rule stated honestly, exceptions
  and all.'
---
Grounded in Doc_04_Gravity_Discovery.md SS3.6 (T1, Principled Refusal vs. Pragmatic Recourse to Imperial Power: three named, dated instances -- 313, 361, the 390s -- each independently Documented) and Doc_07 SS4/SS6 ('the doctrine's own qualifications are not random lapses; they track the forces exactly'; 'this world's own three qualified turns to imperial power... are not embarrassments quietly managed but facts this world's own record states plainly'). Donatus's own retort is quoted verbatim from the already-cleared don.quote.donatus-quid-est-imperatori record (text field, matching that record's own verbatim license exactly, not re-translated here). T1 already has a classified gravity record (don.gravity.principled-refusal-vs-pragmatic-recourse, register etic) and a cleared quote, but no record states T1 in first-person doctrinal-witness voice with its own position/tension structure -- this is the first. canon_cells=['F1-E'] ('When belief was disputed, who had the right to decide -- and how do we know how that worked?') is a strong direct fit: T1 is precisely a dispute over who has the right to decide ecclesial legitimacy. relations[] links to the T1 gravity and the Donatus quote -- reciprocal edges added directly to don.gravity.principled-refusal-vs-pragmatic-recourse.md and don.quote.donatus-quid-est-imperatori.md after this script runs.
