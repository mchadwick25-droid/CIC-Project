# Syriac leftovers: adversarial review, round 1

- **Reviewed:** uncommitted changes to `records/syr/world_core/syr.core.syriac.md` (`thinness`, rewritten in plain sentences) and `records/syr/honest_limit/syr.limit.f5-women-own-words.md` (new `divergence_note`, reworded source locus).
- **Method:** `git diff` of both files; each old clause matched against its new sentence for meaning; claims checked against `cic/texts/chronicle-of-edessa_cowper.txt` (entries for 684-721 Seleucid, i.e. 373-410), `cic/texts/npnf213_gregory-great-ephraim-syrus-aphrahat.xml` (1898 introduction at 11250-11254; Nisibene hymns on "my virgins" and "consecrated virgins"), and the record's own `statement` / `why_sources_cannot_answer`; gate logic read at `engine/m1/gates.py:368-385` and `engine/m1/gates_experimental.py:55-97`; readability scored with `engine.m7.turn_readability.score_turn`; `python -m engine.m10.cli regate syr --base origin/main` run on the working tree.
- **Date:** 2026-10-24
- **Reviewer:** independent Opus context (no part in drafting)

## Verdict

**PASS WITH FIXES.** Two findings are blocking because the text overstates the evidence. Both have one-sentence fixes. The divergence_note fits the gate rule. The rest is non-blocking wording.

Gate and readability: `regate syr` passes on the current text, with only base-unchanged notes. Proposed `thinness` scores FK 7.3 / FRE 61.2. Proposed divergence_note scores FK 5.6 / FRE 73.9. Neither has a hard failure. The current text scores FK 6.9 / FRE 61.7.

## Findings

| # | File / field | Severity | Finding | Exact replacement |
|---|---|---|---|---|
| 1 | core `thinness` | BLOCKING | "Ordinary lay believers have no words of their own." This says the people had no words. The old claim was that their own words do not survive in the sources. Misleading. | `No ordinary lay believer's own words survive.` |
| 2 | core `thinness` | BLOCKING | "The years 373-410 survive only as an outline of bishops in turn." The old text said thin-to-silent *beyond* the outline. "Only" goes further and is wrong: the vendored Chronicle of Edessa also records Resaina (692), Thomas's relics (705), 'Absamia's madrashe (715). "In turn" is also unclear. | `For the years 373-410 we have little beyond a list of bishops in succession.` |
| 3 | core `thinness` | Non-blocking | "heard only through men's texts" then "singing ... only through later accounts" reads as if the later accounts were not men's texts. They are: Jacob of Serugh and the Lives. The intended split (contemporary vs later) is not stated. | Replace the three sentences with: `The daughters of the covenant are heard only through men's texts. Men of their own time tell of their vows and service. Their singing is told only in later men's accounts.` |
| 4 | core `thinness` | Non-blocking | "thin to silent on other groups": the list includes a span of years and Edessa's remains, which are not groups. | `The world is thin to silent in six places.` |
| 5 | core `thinness` | Non-blocking | "The dispute is one that only Aphrahat's side records." "The dispute" has no antecedent, and the old sentence's link to the Jewish testimony is lost. | Replace both sentences with: `There is no independent Jewish testimony in a dispute that only Aphrahat's side records.` |
| 6 | core `thinness` | Non-blocking | The old "since" (remains are thin *because* the city is built over) is lost when it is split into two sentences. | `Edessa's material remains are thin, because the modern city sits on the ancient one.` |
| 7 | limit `divergence_note` | Non-blocking | Coherent with the gate: the record is `verified-direct`, so a note is not required, and a non-null note is allowed. The honest_limit is already exempt from the experimental thin-topic gate. Content matches `statement` ("Later accounts say...") and `why_sources_cannot_answer`. Ephrem's Nisibene hymns do name "my virgins with their fasts" and "consecrated virgins", which supports "as Aphrahat and Ephrem report them". Only weak point: "Their singing in the churches is different" says how it differs only in the next sentence, and does not say the rating leaves the singing out. | `The absence of any text by a woman of this world is Documented. So are the women's vows and service, as Aphrahat and Ephrem report them. This rating does not cover their singing in the churches. That rests only on later men's accounts.` |
| 8 | limit `sources[0].locus` | Non-blocking | Accurate hedge. But it suggests later accounts single out the Nisibene hymns. They speak of Ephrem's madrashe in general. | `Ephrem's madrashe, which later accounts say women's choirs sang` |
| 9 | limit record body (outside the diff) | Non-blocking, out of scope | The body still says "the choirs are attested only through men's writing". That is process commentary in a live record (CLAUDE.md, live surfaces), and it now differs from the new later-accounts scoping. Flag it for the owning thread. | Remove the body paragraph. Doc_02 SS7 already holds the verification trail. |

Confirmed unchanged in meaning: richest areas and their order (Ephrem, then Aphrahat), persecution on the Persian side, frontier civic memory (Chronicle of Edessa, Nisibis sieges), and enslaved and lower-status people with no surviving voice. Nothing is invented once findings 1 and 2 are fixed.
