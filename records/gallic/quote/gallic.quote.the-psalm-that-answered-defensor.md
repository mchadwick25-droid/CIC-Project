---
id: gallic.quote.the-psalm-that-answered-defensor
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted at the narrative level: Documented as Sulpitius's own text (Vita ch. IX, read at
    its locus for this record). The reading of the psalm as "chosen by Divine ordination" is explicitly
    reported by Sulpitius as what "was believed," and is carried here as the crowd's and the author's
    own framing, not asserted as fact.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. IX (npnf211 div ii.ii.x, file lines 1088-1108): the objecting bishop Defensor, the absent reader, the psalm opened at random, and what was believed of it"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks how the objecting bishops were answered, or what happened when the reader failed to appear"
  - "participant asks about scripture opened at random, or a psalm treated as a sign"
  prefer_instead:
  - "participant wants the ambush and the vote that came before this - retrieve gallic.quote.ruricius-and-the-vote-for-tours instead, or alongside"
  - "participant wants a doctrine of scripture as oracle stated plainly - this record carries one narrated instance, not a general claim"
text: >-
  Among the bishops, however, who had been present, a certain one of the name Defensor is said to have
  specially offered opposition; and on this account it was observed that he was at the time severely
  censured in the reading from the prophets. For when it so happened that the reader, whose duty it was
  to read in public that day, being blocked out by the people, failed to appear, the officials falling
  into confusion, while they waited for him who never came, one of those standing by, laying hold of
  the Psalter, seized upon the first verse which presented itself to him. Now, the Psalm ran thus: 'Out
  of the mouth of babes and sucklings thou hast perfected praise because of thine enemies, that thou
  mightest destroy the enemy and the avenger.' On these words being read, a shout was raised by the
  people, and the opposite party were confounded. It was believed that this Psalm had been chosen by
  Divine ordination, that Defensor might hear a testimony to his own work, because the praise of the
  Lord was perfected out of the mouth of babes and sucklings in the case of Martin, while the enemy was
  at the same time both pointed out and destroyed.
speaker_or_author: gallic.figure.sulpitius
license: verbatim
modern_lens_note: >-
  A modern reader might expect the crowd's shout to settle the argument by force of numbers. Sulpitius
  gives it a different logic: the psalter was opened at random because the appointed reader could not
  get through the crowd, and the verse that came up happened to name an "enemy" and a "defensor" -
  Defensor's own name. Sulpitius reports this as what the crowd believed, not as his own proof; the
  belief is the story's evidence, not the event's certainty.
relations:
- type: associated-with
  target: gallic.story.election-at-tours
---
Verified directly against the vendored cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml,
same chapter as gallic.quote.ruricius-and-the-vote-for-tours (`ii.ii.x-p2`). `grep -n "Defensor"`
returns hits at lines 1089, 1102, and 1105-1106. The excerpt is one continuous run, verbatim and
unbroken, from "Among the bishops, however, who had been present" (line 1088) through "both pointed out
and destroyed." (line 1108); no material internal to this span was omitted or elided. Two editorial
endnotes fall inside it: n. 24 (Ps. viii. 3, the scripture reference) after the psalm verse, and n. 25
(Roberts's note that the Vulgate's "defensor" corresponds to the English "avenger," so that the man
would have seemed expressly named) attached to "Defensor" at line 1102 - both dropped as apparatus, the
second one not adopted as Sulpitius's own claim.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single spaces.
The source wraps the psalm verse in curly double quotation marks; these are replaced here with single
quotation marks, marking it as Sulpitius's own citation of scripture within his narration (the same
convention used for the elder's scripture citation in gallic.quote.receiving-christ-in-you), rather than
dropped outright as speech-marking. No word was added, dropped, substituted, or reordered.

speaker_or_author is gallic.figure.sulpitius: this is Sulpitius's own narration in the Life of Martin.
