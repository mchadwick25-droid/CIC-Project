---
id: gallic.quote.chaeremon-grace-requires-our-effort
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
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Documented as Cassian's own text (Conference XIII.13, read at its locus for this record). Widely
    Accepted as Cassian's report of Chaeremon's teaching; its doctrinal content is Contested [CT] for
    its meaning relative to Augustine and for the fairness of the label "semi-Pelagian" - the same
    caveat carried by this quote's companion records, gallic.quote.germanus-and-chaeremon-on-the-
    husbandman and gallic.quote.chaeremon-three-stages-of-grace, and neither depended on nor resolved
    here. This record carries the full sentence through its own contested synergist clause - the words
    below from "in such a way as sometimes even to require" onward - that make grace's co-operation ask
    something of the will in return; that clause is Conference XIII.13's own content, not joined here to
    Conference XIII.18's separate teaching, which stands on its own in
    gallic.quote.chaeremon-three-stages-of-grace.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "Conference XIII.13 (npnf211 div iv.v.iv.xiii, file lines 38200-38207): Chaeremon's statement that God's grace always co-operates with the will and sometimes requires some effort of good will from it in return, so its bounty is not unreasonable when it is given on account of some desire and effort to gain it"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether grace does everything, or still expects something from the person's own effort"
  - "participant asks how this world held together grace and free will, without collapsing either one"
  prefer_instead:
  - "participant wants the argument's origin and the husbandman analogy - retrieve gallic.quote.germanus-and-chaeremon-on-the-husbandman"
  - "participant wants the three-stage account of how grace and free will divide the work between them - retrieve gallic.quote.chaeremon-three-stages-of-grace"
  - "participant wants the doctrine argued at full theological depth - retrieve gallic.term.grace, gallic.term.free-will"
text: >-
  And so the grace of God always co-operates with our will for its advantage, and in all things assists,
  protects, and defends it, in such a way as sometimes even to require and look for some efforts of good
  will from it that it may not appear to confer its gifts on one who is asleep or relaxed in sluggish
  ease, as it seeks opportunities to show that as the torpor of man's sluggishness is shaken off its
  bounty is not unreasonable, when it bestows it on account of some desire and efforts to gain it.
speaker_or_author: "Abbot Chaeremon, as Cassian records him (Conference XIII.13)"
license: verbatim
modern_lens_note: >-
  Grace "always co-operates with our will," Chaeremon says - but he does not stop there. He goes on to
  say it sometimes "requires and look[s] for some efforts of good will" in return, so that its gift is
  never given "to one who is asleep or relaxed in sluggish ease." That is the actual contested claim: not
  that grace does everything, and not that effort earns it outright, but that grace waits on some real
  motion from the person before it is given.
modern_rendering: >-
  And so God's grace always works together with our will, for the will's own good. In all things it
  helps, protects, and defends the will. But it does this in a way that sometimes even requires and looks for
  some effort of good will from it. That way, grace does not seem to give its gifts to someone who is
  asleep, or lying back in sluggish ease. Grace looks for chances to show this: once the dullness of human
  sluggishness is shaken off, its generosity is not unreasonable. It gives because of some desire and
  effort to gain it.
relations:
- type: associated-with
  target: gallic.story.germanus-scruple-at-morning-service
- type: associated-with
  target: gallic.gravity.grace-and-effort
- type: associated-with
  target: gallic.force.africa-and-rome-pressure
use_note:
  means: "Cassian reports Abbot Chaeremon teaching that God's grace always cooperates with the will and sometimes looks for some effort of good will before giving."
  not_for:
    - "a settled verdict that the teaching is semi-Pelagian, when that label is contested"
    - "the three stages of grace, which sit in gallic.quote.chaeremon-three-stages-of-grace"
    - "a claim that effort earns grace outright"
  years: {from: 426, to: 426}
  status: provisional
---
Verified verbatim directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "co-operates with our will"`
returns one hit, line 38201, inside `<div4 title="Chapter XIII. How human efforts cannot be set against
the grace of God." ... id="iv.v.iv.xiii">` (line 38193). The chapter's opening paragraph, `sed -n
'38200,38207p'`, is one full sentence: "And so the grace of God ... when it bestows it on account of
some desire and efforts to gain it." - ending at the sentence's own period, not cut mid-sentence. No word
was added, dropped, substituted, or reordered.

This record carries the full sentence, independently verified, with nothing joined to it and nothing
trimmed from it - including the contested clause through to its actual end ("protects, and defends
it... when it bestows it on account of some desire and efforts to gain it"). Conference XIII.18's own,
separate passage is carried on its own in gallic.quote.chaeremon-three-stages-of-grace, not joined to
this one - the two are non-adjacent chapters of the same Conference.

speaker_or_author is a plain string, not a figure id: no gallic.figure record exists for Chaeremon, and
these are his words as Cassian gives them, not Cassian's own.

modern_rendering: authored against the verbatim `text`, then independently checked clause by clause in a
separate pass - the sentence on "its generosity is not unreasonable ... once the torpor is shaken off ...
it gives on account of desire and effort" folds the condition into a single sentence ahead of the one
claim, so it states that claim once, matching the source's own one integrated thought. No ellipsis or
bracket applies to this quote, so the bracket-voicing rule for finishing a true ellipsis does not arise
here.
