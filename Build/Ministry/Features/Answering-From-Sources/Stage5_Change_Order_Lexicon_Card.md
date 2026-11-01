# Stage 5 change order: the lexicon card matches the rigor of the quotes and stories

Named change order. It replaces plan row 5.1, which kept the lexicon door as it is.

## Mark's words

Mark, 2026-11-01, relayed by the coordination thread: "i think the template for lexicon should match the rigor of the quotes and stories".

## What changes

- The lexicon card's content is no longer kept as it is today. It moves to a template Mark chooses from options put to him as an Artifact, matched to the quote card: labelled layers, the world's own sense kept apart from other uses, and the sources it rests on with edition and locus, with the formation confidence and the risk flag for false friends.
- The three levels stay (Settled row 12): the highlighted word, the hover for brief context, and the click page with the links to the source references and documents.

## What does not change

- Nothing is built until Mark chooses a template. Today's card stands until then.
- No layout or styling redesign beyond the chosen template (Settled row 3).
- Term records are brought to the same bar by a review of term meanings, like the rendering review, and by sources that name a vendored span; that is Library's record work, listed in the Artifact, and is not started by this order.

## Done when

Mark has chosen a template, Decision-Log records the choice, and the card and its tests change together under that choice.

## Outcome

Mark chose template B on 2026-11-01 (Decision-Log 55): labelled layers "In plain English", "In this world", "Not to be confused with" and "What it rests on", with the confidence phrase and the risk flag. A source that names no vendored span, or an edition without a held translator and date, is shown as unavailable.

Mark added on 2026-11-01 (Decision-Log 56): "b, but we need the modern misunderstanding or a contrast to how people think it means today vs in that world". Template B therefore carries a named contrast layer, "How we hear it today" beside "In this world", fed from `senses.translational` and `false_friend`; a term without a usable modern-reading field shows the layer as unavailable and nothing is invented. The contrast is not added to the quote card.


## Schema: the contrast split at the source

Coordination ruled on 2026-11-01 that the contrast is split at the source, not by sentence in code. `Schema_Change_Order_Term_Senses_Split.md` adds two optional fields to a term record's `senses`: `heard_today` (how people hear the word today) and `meant_here` (what the word means in this world). The card renders the two-column contrast from them; a term not yet split shows the whole `senses.translational` block as the fallback. No code splits `senses.translational` by sentence.

The card build registers `senses.translational`, `senses.heard_today` and `senses.meant_here` in the spoken-field registry, so the readability gate and the leak scans cover the text a participant will see on the card; they are not registered today.
