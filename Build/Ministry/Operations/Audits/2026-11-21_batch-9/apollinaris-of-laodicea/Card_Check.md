# Card check: Apollinaris of Laodicea (`apollinaris-of-laodicea`)

**FIX** (one change).

## Checked

- Starting card: `Card.existing.json` equals the census card. Every field not listed in `Card_Edits.md` is word for word. The added list items come after the old ones, in order. The only other changes are the three `sources.about` titles, each extended as listed.
- Validator, on a scratch census with the card and brief set in: no errors for this entry except the ones the release step clears (no `secondReading` on the four quotations, each six words or more; the modern quotations not yet in `tools/quote_renderings.json`). Keys allowed; four `quotationOriginals`, one for each of the brief's quoted spans. Every cited file is in `sources`, including Jerome's Letter 84 (`npnf206`) and Gregory's Letter 101 (`npnf207`) behind `briefReferences`.
- Greek checked by hand:
  - Fragment 81 (Lietzmann 11480-11481): καὶ εἰ ἀνθρώπῳ (φησὶ) συνήφθη ὁ θεός, τέλειος τελείῳ, δύο ἂν ἦσαν, εἷς μὲν φύσει υἱὸς θεοῦ εἷς δὲ θετός. The rendering is faithful, and φησί is rightly noted as Gregory's.
  - Lietzmann 12986-12987: μίαν φύσιν τοῦ θεοῦ λόγου σεσαρκωμένην.
  - Justinian (Lietzmann 5754-5756): verbatim, and the rendering holds.
  - Sozomen 6.25 is printed in English alone (`npnf202` 39027-39028), verbatim. That is right, since its Greek is a damaged scan.
- New items spot-checked against their lines: Philostorgius 472; Basil, Letter 263 (`npnf208` 43311-43314); the Theodosian Code dates (3 Dec 383, 21 Jan 384, 10 Mar 388, 397; 7075-7080, 7126); Hefele v3 876-893 (not genuine, "rather to Apollinaris"; Cyril and Dioscurus; "watchword of orthodoxy"). All hold. American spelling is used in the card.
- No existing claim was found wrong. The Leontius dating is stated as Pusey gives it, which is right.

## Change

1. `quotationOriginals[3].uncertain` misspells the Greek verb. The print reads ἐπιτιθέασι (Lietzmann 5756). Old: "renders epitithesin as they put." New: "renders epititheasi as they put."

## Aside, outside the card

The brief (line 15) has the British spelling "honoured bishops' names". The card uses "honored". This is not a card fix: it is flagged for whoever owns the brief.
