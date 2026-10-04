---
id: gallic.quote.paphnutius-the-brother-hides-his-own-book
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as Piamun's own telling (Conferences XVIII.15). The wording is Documented at its
    locus; the plot itself - the brother's scheme, hidden from every witness but Piamun's narration - is
    the tradition's own account, not something independently attested.
sources:
- source_id: gallic.source.cassian-conferences-part-iii
  locus: "Conferences XVIII.15 (npnf211 div iv.vi.ii.xv, file lines 43012-43018): the brother's scheme to
    mar Paphnutius's reputation; hiding his own book among the palm boughs in Paphnutius's cell; going to
    church as if innocent"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks exactly how the accuser framed Paphnutius, or wants the mechanics of the scheme"
  prefer_instead:
  - "participant wants the whole story in the world's own accessible voice - retrieve gallic.story.paphnutius-and-the-hidden-book"
text: >-
  And this man wanting to mar his beauty by some blemish or spot, hit on this kind of devilry, so as to
  seize an opportunity when Paphnutius had left his cell to go to Church on Sunday: and secretly entering
  his cell he slyly hid his own book among the boughs which he used to weave of palm branches, and,
  secure of his well-planned trick, himself went off as if with a pure and clean conscience to Church.
speaker_or_author: "Abbot Piamun, as Cassian records his own telling"
license: verbatim
modern_lens_note: >-
  Piamun narrates the scheme from outside, as no one in the story could have - he names the brother's own
  intent ("wanting to mar his beauty") before any accusation is made. The tradition is not neutral about
  who is guilty; it tells the plot to the listener while the desert itself is still deceived.
relations:
- type: associated-with
  target: gallic.story.paphnutius-and-the-hidden-book
modern_rendering: >-
  This man wanted to spoil his beauty with some flaw or stain. So he came up with this devilish
  trick. He waited for a chance when Paphnutius had left his cell to go to church on Sunday. Then he
  crept into the cell in secret. Slyly, he hid his own book among the palm branches that Paphnutius used
  to weave. Sure that his trick was well planned, he went off to church himself, as if his conscience
  were pure and clean.
use_note:
  means: "Piamun, in Cassian's Conferences, narrates how an envious brother hid his own book among Paphnutius's palm boughs to frame him."
  not_for:
    - "the search and the finding of the book, which sit in gallic.quote.paphnutius-accused-and-the-book-found"
    - "an independently attested event rather than the tradition's own telling"
    - "a Gallic incident, when the story is set in the Egyptian desert"
  years: {from: 426, to: 435}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n "just
as the plotter"` (used to anchor the chapter generally) and manual read confirm "And this man wanting"
begins at the end of line 43012 and runs through line 43018, `sed -n '43012,43018p'`, ending "...as if
with a pure and clean conscience to Church."

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
