---
id: cappadocian.quote.basil-to-the-chorepiscopi
world_id: cappadocian-trinitarian
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: cappadocian.source.basil-chorepiscopoi-letters
  locus: "Letter LIII (Ep. 53), To the Chorepiscopi (npnf208_basil-letters-select-works.xml)"
  license: public-domain
text: >-
  It is a lighter sin to wish in ignorance to buy, than it is to sell,
  the gift of God. A sale it was; and if you sell what you received as
  a free gift you will be deprived of the boon, as though you were
  yourself sold to Satan. You are obtruding the traffic of the huckster
  into spiritual things and into the Church where we are entrusted with
  the body and blood of Christ. These things must not be.
speaker_or_author: cappadocian.figure.basil
license: verbatim
modern_lens_note: >-
  This excerpt is the back half of the letter's opening paragraph, after
  Basil has already stated the charge he is writing about: "There is a
  report that some of you take money from candidates for ordination,
  and excuse it on grounds of religion." A modern reader may take "the
  traffic of the huckster" as loose insult; in context it names a
  specific offense - selling ordination itself, the office of the
  ministry, for money, what later canon law calls simony - and Basil's
  point is a legal one: because the gift was received free, selling it
  voids the transaction and forfeits the office, "as though you were
  yourself sold to Satan." This is a metropolitan bishop writing to the
  chorepiscopoi under his own authority to stop a reported practice, not
  a general sermon against greed.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks who held authority among this world's people, or how anyone came to have it"
  - "participant asks how this world's faith first spread to the region"
  - "participant asks whether bishops were appointed, elected, or something else"
relations:
- type: associated-with
  target: cappadocian.dw.authority-and-spread
modern_rendering: >-
  It is a lesser sin to try, out of ignorance, to buy God's gift than it
  is to sell it. What happened here was a sale - and if you sell what
  you were given for free, you will lose it, as though you yourself had
  been sold to Satan. You are dragging the huckster's trade into sacred
  things, into the Church itself, where we are entrusted with the body
  and blood of Christ. This cannot be allowed to stand.
use_note:
  means: "Basil, writing early in his episcopate to his village bishops, condemns taking money for ordination as selling God's free gift."
  not_for:
    - "evidence of how the faith first reached the region, which rests on the legend in cappadocian.story.thaumaturgus-legend"
    - "a claim that simony was widespread, when the letter answers one report"
    - "a general sermon against greed rather than a metropolitan's ruling to his own subordinates"
  years: {from: 370, to: 372}
  status: reviewed
---
Verified verbatim directly against the vendored
npnf208_basil-letters-select-works.xml. `grep -n 'id="ix\.liv"\|id="ix\.lv"'`
locates both letters titled "To the Chorepiscopi": div id="ix.liv" at
line 27491 and div id="ix.lv" at line 27582. Both div ids are one Roman
numeral higher than the letter's own printed heading: id="ix.liv"
carries the printed heading "Letter LIII." (line 27493), and id="ix.lv"
carries "Letter LIV." (line 27584) - matching this world's own
cappadocian.source.basil-chorepiscopoi-letters record, whose `work`
field already names these as "Epp. 53, 54." This record cites Letter
LIII (Ep. 53, div id="ix.liv").

Both letters were read in full before choosing. Letter LIII (id="ix.liv",
lines 27491-27580) opens "My soul is deeply pained at the enormity of
the matter on which I write" (line 27528) and states the charge
directly two sentences later: "There is a report that some of you take
money from candidates for ordination, and excuse it on grounds of
religion" (lines 27535-27537) - this is the paid-ordination letter.
Letter LIV (id="ix.lv", lines 27582-27711) is a different offense: lax,
unexamined admission of unworthy candidates by presbyters through
favoritism ("by mere favoritism, on the score of relationship or some
other tie," lines 27668-27669) and Basil's order restoring the roll-and-
examination procedure - it never mentions money changing hands. Only
Letter LIII addresses paid ordination in checkable, quotable prose, so
it is the sole source for this record.

The quoted text is drawn verbatim from lines 27548-27555, a single
contiguous, note-free run of running text (no endnote markers fall
inside it): "It is a lighter sin to wish in ignorance to buy, than it is
to sell, the gift of God." through "These things must not be." Chosen
over the earlier sentences in the same paragraph (the initial "report,"
and the Simon Magus allusion "Thy money perish with thee") because this
stretch is where Basil states the prohibition itself, in his own words,
without an intervening endnote reference - naming the offense as a sale
("A sale it was"), stating its consequence (forfeiture of the office,
"deprived of the boon"), and closing with the flat prohibition "These
things must not be." Double-spacing in the source file's own
typesetting normalized to single spaces; no wording added, dropped, or
reordered.

Chosen for F3-I specifically because it is Basil's own letter making,
in his own words, exactly the claim cappadocian.dw.authority-and-spread
states about him in summary - that "Basil's own letters discipline that
office [the chorepiscopoi] directly, forbidding ordinations sold for
money." This is that discipline in Basil's own voice: written by the
metropolitan to the village-level bishops under him, naming the sale of
ordination as the offense and forbidding it outright.

The spoken form is a modern-English translation, never the archaic original; the original stays as the record's own text field, shown at Level 3.
