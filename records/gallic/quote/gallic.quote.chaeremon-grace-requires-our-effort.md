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
    here. This record and gallic.quote.chaeremon-three-stages-of-grace together replace the former
    gallic.quote.chaeremon-on-grace-and-free-will, which spliced this passage together with the
    separate Conference XIII.18 teaching (roughly 400 lines further on) into one quote joined by an
    ellipsis, and which silently cut this passage's own contested synergist clause - the words below
    from "in such a way as sometimes even to require" onward - that make grace's co-operation ask
    something of the will in return. Each teaching now stands as its own independently verified record.
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
  The sentence the earlier, spliced record kept stopped short of Chaeremon's own point. Grace "always
  co-operates with our will," yes - but he goes on to say it sometimes "requires and look[s] for some
  efforts of good will" in return, so that its gift is never given "to one who is asleep or relaxed in
  sluggish ease." That is the actual contested claim: not that grace does everything, and not that effort
  earns it outright, but that grace waits on some real motion from the person before it is given. A
  reader who only had the first clause would miss what makes this teaching distinctive - and contested -
  at all.
modern_rendering: >-
  God's grace always works together with our will, for the will's own good. In every way it helps,
  protects, and defends the will. It even asks and looks for some effort of good will from us in return.
  That way, it does not seem to give its gifts to someone who is asleep or resting in sluggish ease. It
  looks for the chance to show that once the weight of our own sluggishness lifts, its generosity is not
  unreasonable. It gives that gift because of some desire and effort to gain it.
relations:
- type: associated-with
  target: gallic.story.germanus-scruple-at-morning-service
---
Verified verbatim directly against the vendored
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "co-operates with our will"`
returns one hit, line 38201, inside `<div4 title="Chapter XIII. How human efforts cannot be set against
the grace of God." ... id="iv.v.iv.xiii">` (line 38193). The chapter's opening paragraph, `sed -n
'38200,38207p'`, is one full sentence: "And so the grace of God ... when it bestows it on account of
some desire and efforts to gain it." - ending at the sentence's own period, not cut mid-sentence. No word
was added, dropped, substituted, or reordered.

This record replaces the first half of the former gallic.quote.chaeremon-on-grace-and-free-will, which
joined this sentence to a separate, non-adjacent Conference XIII.18 passage (see
gallic.quote.chaeremon-three-stages-of-grace) with an ellipsis, and which cut this sentence's own
contested clause short at "protects, and defends it" instead of carrying it through to its actual end.
That splice and cut were a real defect (Opus review of PR #579): this record now carries the full, single
sentence, independently verified, with nothing joined to it and nothing trimmed from it.

speaker_or_author is a plain string, not a figure id: no gallic.figure record exists for Chaeremon, and
these are his words as Cassian gives them, not Cassian's own.

modern_rendering: no Agent/subagent-spawning tool was available in this execution context (only full
Claude Code Remote sessions, which have no reliable synchronous channel back to a dispatched subagent
task) - CLAUDE.md's own rule against fabrication forbids claiming an independent Opus authoring-and-check
pair that did not actually run. The rendering above was drafted directly against the fleet's rendering
bar (every clause voiced, nothing added, one thought per sentence kept under roughly 25 words, no
misleading modern sense) and then re-checked clause by clause against this record's own verbatim `text`
in the same pass. No ellipsis or bracket applies to this quote, so R47 does not arise here. This falls
short of the task's instruction to use two independent Opus subagents; flagged so the dispatching session
(which does carry Agent/Opus access) can run that pair and replace this field if strict process
compliance is required.
