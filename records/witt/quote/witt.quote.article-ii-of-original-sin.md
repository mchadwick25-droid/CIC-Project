---
id: witt.quote.article-ii-of-original-sin
world_id: lutheran-wittenberg-and-its-congregations
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F1-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Article II of the Augsburg Confession, the same signed 1530 confession
    witt.story.diet-of-augsburg-1530 verifies. Consistent with witt.term.sin's own informational sense
    (already carrying this same article's own language, "born with sin... without the fear of God,
    without trust in God, and with concupiscence"), read here at its own fuller span including the
    condemnation clause that term record's own coverage note discloses it had not separately gathered.
sources:
- source_id: witt.source.melanchthon-augsburg-confession
  locus: "Article II: Of Original Sin (cic:melanchthon_augsburg-confession_anon-pg275.txt lines 192-203): 'all men begotten in the natural way are born with sin... bringing eternal death upon those not born again through Baptism and the Holy Ghost' through 'argue that man can be justified before God by his own strength and reason'"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what we believed about original sin, or whether people are born already guilty"
  do_not_retrieve_when:
  - "participant means a single wrongful act, not the doctrinal condition -- retrieve the sin term instead"
text: >-
  Also they teach that since the fall of Adam all men begotten in the
  natural way are born with sin, that is, without the fear of God, without
  trust in God, and with concupiscence; and that this disease, or vice
  of origin, is truly sin, even now condemning and bringing eternal death
  upon those not born again through Baptism and the Holy Ghost.

  They Condemn the Pelagians and others who deny that original depravity
  is sin, and who, to obscure the glory of Christ's merit and benefits,
  argue that man can be justified before God by his own strength and
  reason.
speaker_or_author: "the Augsburg Confession, Article II -- the same confession read before the Emperor at the 1530 Diet of Augsburg"
license: verbatim
modern_lens_note: >-
  A modern reader may hear "born already guilty" as a claim about a baby's own moral blame -- something a
  newborn has personally done wrong. We do not mean that. The condition named here is not an act; it is a
  state we are born into, described by what is missing rather than what is done: no fear of God, no trust
  in God, and a disordered desire turned toward the self instead. It is named a "disease" and a "vice of
  origin" -- something we are born carrying, not something any infant has chosen. And the remedy named in
  the same breath is not effort but a new birth, through baptism and the Holy Spirit -- the same claim
  witt.quote.article-ix-of-baptism states from baptism's own side.
modern_rendering: >-
  We also teach this: ever since Adam fell, everyone born the ordinary way is born already carrying sin.
  They are born without fear of God. They are born without trust in God. Their desires are turned the
  wrong way. This flaw we are born with is truly sin. Even now it brings condemnation. It brings death
  without end, on everyone not born again through baptism and the Holy Spirit.

  We reject what the Pelagians and others teach: that this inborn flaw is not really sin, and that a
  person could obscure Christ's own merit by claiming to be made right with God through their own
  strength and reason instead.
relations:
- type: associated-with
  target: witt.dw.born-in-sin-fed-at-the-table
- type: associated-with
  target: witt.dw.a-death-begun-that-a-child-receives
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between B-7a and B-8) directly against
the vendored cic/texts/melanchthon_augsburg-confession_anon-pg275.txt. `grep -n "Article II: Of Original
Sin\|bringing eternal death upon those not born again\|They Condemn the Pelagians"` returns the article
heading at line 192, "of origin, is truly sin, even now condemning and bringing eternal death" at line
197, and "They Condemn the Pelagians and others who deny that original depravity" at line 200. `sed -n
'192,203p'` confirms the whole span: heading at 192, the article's own definition at 194-198 (opening
"Also they teach that since the fall of Adam" at 194, closing "the Holy Ghost." at 198), and the full
condemnation clause at 200-203 ("They Condemn the Pelagians and others who deny that original depravity /
is sin, and who, to obscure the glory of Christ's merit and benefits, / argue that man can be justified
before God by his own strength and reason."). The `text` field quotes the condemnation clause to the
sentence's own actual end. No word added, dropped, substituted, or reordered within the quoted span.

CORRECTION (go-live adversarial review, Round 1, 2026-09-20; M-2, MEDIUM): this record's `text` field
previously closed the condemnation clause at "is sin," with no ellipsis and a substituted terminal
period, silently dropping the sentence's own continuation into the second Pelagian error (denying that
Christ's own merit, not human strength and reason, justifies) - the more load-bearing half for a
Lutheran confession, and this world's own central conviction (faith alone, apart from works). The prior
body note characterized the cut clause as "a separate charge... not needed to state the doctrine itself"
and disclosed it in full - this was not the rzg-class defect (no invented composite, no splice across
distant loci) - but a silently re-punctuated boundary in a participant-facing `text` field is a defect
under this project's own "every quote is re-verified verbatim" rule even when disclosed elsewhere, per
CLAUDE.md's own explicit instruction not to resolve this by strengthening the body note. Fixed by
extending the quotation to the sentence's actual end, in `text` and `modern_rendering` both, rather than
adding an ellipsis - the continuation is short, directly bears on this world's own faith-alone conviction,
and a closed sentence reads more cleanly to a participant than a mid-sentence ellipsis would.

This is the fuller span behind witt.term.sin's own informational sense, which already carries "born with
sin, that is, without the fear of God, without trust in God, and with concupiscence" from this same
article (F1-I) but whose own divergence_note discloses "the Apology's own Article II... remains unread by
this build" and that the confessional definition's own condemnation clause was not separately verified at
that authoring pass. This record verifies that fuller clause directly and grounds it as its own record,
without editing witt.term.sin. Ground for witt.dw.born-in-sin-fed-at-the-table (F1-T: original sin,
alongside faith alone and the bread and cup) and, via the baptism/new-birth clause in the same sentence,
for witt.dw.a-death-begun-that-a-child-receives (F4-T: infant baptism and being "born again"). Reciprocal
associated-with declared on both.

CORRECTION (Phase C recon, 2026-09-19): speaker_or_author's own raw reference to
"witt.story.diet-of-augsburg-1530" replaced with plain prose ("read before the Emperor at the 1530 Diet
of Augsburg") -- caught by engine.m1.cross_world's check_quote_speaker_labels, which correctly flags this
field as one both the Level-3 citation card and the compiled prompt's quote index print verbatim to a
participant. Substance unchanged, only the internal record-id reference removed.
