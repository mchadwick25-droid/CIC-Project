---
id: ijc.search.f1-t-negative-sweep
world_id: imperial-juridical
record_type: search_record
schema_version: 2
status: draft
register: etic
canon_cells:
- F1-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: null
sources: []
query: "Cell F1-T (original sin; the bread and cup / transubstantiation; faith alone versus works) -
  a grep-and-read sweep of the already-vendored corpus for each of the three canon_question texts,
  run at review because the cell's honest_limit had been drafted without one"
channel: "grep against cic/texts for 'Adam', 'original sin', 'tithe' (checked here despite belonging to
  F4-T), 'This is My Body', 'Mysteries', 'faith alone', 'sola fide' - followed by direct reading of every
  hit inside the already-licensed Ambrose and Leo volumes, 2026-08-21"
result: found
found_sources: [ijc.source.leo-letters, ijc.source.ambrose-de-mysteriis]
note: "Original sin: Leo's Ep. LIX.4 (npnf212 line 7398) states the transmission of original sin to
  Adam's descendants explicitly, in an anti-Eutychian argument - found, licensed
  ijc.dw.original-sin-transmitted. The bread and cup: Ambrose's De Mysteriis IX.50-54 (npnf210 line
  33189) teaches a real change of the elements' nature by consecration, at length - found, licensed
  ijc.dw.bread-made-body. Faith alone versus works: no comparable passage exists anywhere in the
  licensed corpus framing salvation as a contest between faith and works in later Reformation terms;
  Pauline grace-language exists (quoted incidentally inside the Leo material found above) but never
  argued as this specific question. CONSEQUENCE: ijc.limit.later-questions, which previously
  claimed all three F1-T questions were unaddressed, is corrected and narrowed to the one question this
  sweep confirms genuinely has no answer."
---
Added at review (Opus canon-structure pass, 2026-08-21) as the
structural fix for Review 3's H5 finding: the root cause of the three
false honest_limit claims (F1-T original sin and eucharist; F5-T
marriage) was that no cell-scoped negative search had ever actually
been run before this build's first pass wrote those refusals. This
record and ijc.search.f5-t-negative-sweep are the searches that should
have preceded the original drafts.
