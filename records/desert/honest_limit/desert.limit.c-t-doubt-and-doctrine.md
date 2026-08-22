---
id: desert.limit.c-t-doubt-and-doctrine
world_id: desert-monasticism
record_type: honest_limit
schema_version: 2
status: draft
register: emic
canon_cells: [C-T, F1-P]
confidence:
  citation_specificity: C
  verification_state: verified-via-authority
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: "Documented that this genre gap exists (the Vita is hagiography, composed by an outside bishop-author with his own theological agenda, not first-person confessional writing); the gap itself, not a doctrinal claim, is what this record documents."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "the Vita's own hagiographic genre - an outside author's constructed exemplar, not first-person confession or systematic doctrinal exposition"
statement: "Do you want to know how his death saves you? Or how to speak of him as your own Lord? Or what to do when you cannot believe? I do not have a good answer. We can tell you that he was not, to us, some lesser being - we said so plainly, in public, more than once, when we were pressed. But how his death actually saves you, in the terms later ages argued out, is not something we wrote down. And our own words are not confession. One book about us was written by an outside bishop, for his own reasons. The rest are short sayings, meant to redirect a struggling person, not to confess a doubt. We show you a struggle disciplined. We do not show you a doubt confessed. If either of those is what you came for, it is not here in our own words."
why_sources_cannot_answer: "This world's own surviving material is overwhelmingly narrative and hagiographic (the Vita) or compiled, occasion-bound sayings (the Apophthegmata), neither genre suited to sustained first-person doctrinal argument about the mechanics of atonement or to confessional doubt-narrative. The one place this corpus does have a positive doctrinal statement in Antony's own reported words (desert.quote.antony-nicene-formula, SS69) answers only whether Christ was a created being, not how his death saves or what it means to call him one's own Lord. Athanasius, the Vita's own author, is a bishop and theologian in his own right but is explicitly not a desert participant (desert.source.athanasius-vita-antonii's own author field) - his own developed atonement theology belongs to his other, non-desert works, not to this corpus's own registered evidence base for this world's own voice."
nearest_material:
- desert.quote.antony-nicene-formula
- desert.dw.f1-i-god
- desert.dw.c-i-jesus
---
Narrowed from its original draft (canon_cells: [C-P, C-T, F1-P]) after
Step 4 Round 1 review Finding S2/M17: C-P is no longer claimed here,
since desert.dw.c-p-someone-like-me now substantively answers C-P-03
(real material this record's first draft did not open); C-T is no
longer claimed for "was Jesus God" specifically, since
desert.quote.antony-nicene-formula now answers that sub-question
directly - this record's own remaining C-T claim is narrowed to the
atonement-mechanics and personal-Lord sub-questions specifically, which
remain genuinely unanswered in this world's own voice.
desert.dw.f1-i-god and desert.dw.c-i-jesus supply the nearest this
corpus comes on the remaining ground - boundary-drawing and lived
pattern, not argument or confession - and this record states plainly
why that is not the same thing.

Step4, Round 3 review Finding M3: the compiled statement's "once, in
public, when we were asked" was the same overclaim Round 2's M2 charged
on desert.dw.f1-i-god.positions[1] - unswept here, and landing in a
field that actually compiles (`build_prompt()` emits `honest_limit.
statement` directly, unlike `positions`). Vita SS72-80 has Antony
disputing publicly with Greek philosophers on more than one occasion,
beyond the single Arian confrontation at SS69 - corrected above to "in
public, more than once, when we were pressed," matching the fix already
made on the sibling record.
