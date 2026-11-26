# Card check: The Latin Apologists (`latin-apologists`, tradition)

Checker who did not write the card. Read: `CLAUDE.md` ("Trust and source fidelity"), Kit Part 1, the tradition kind kit, the role, the final brief, `Outline.md`, `Review.md`, `Fresh_Read.md`, `latin-apologists.card.json`, `Card_Edits.md` and `Card.existing.json`. `Card.existing.json` matches the live census entry field for field.

## Verdict: FIX (four changes, below)

## What holds

- **Nothing else moved.** A field-by-field diff of `Card.existing.json` against the card shows changes only in the fields `Card_Edits.md` lists: `why`, `sourcing`, `floorNote`, `relationsSummary`, `teaser`, `voices[0]`, `voices[1]`, `legacy`, `documentedStories[0].text`, the Barnes line moved out of `documentedStories[0].sources`, and the new `uncertain`, `sources`, `briefReferences`, `quotationOriginals` and `modernWorks`. `people` and `voices[2-4]` are word for word.
- **Corrections 1-10.** Each was re-read at its lines and stands: NPNF2-3 40491-40516 (Victor and Apollonius; Severus and Caracalla; "many small works, which are not extant"), NPNF2-1 43834-43835, NPNF2-1 10272, ANF7 10174, ANF7 4470-4472, ANF7 4565-4571, NPNF2-6 14107-14116, NPNF2-6 16713-16721, Mansi 8 17220-17233 and 17301. The Montanism floorNote is quoted as the live census and the batch card now give it.
- **Quotations.** The brief quotes three spans; there are three `quotationOriginals`, each `modern` equal to its span in the brief. Each `printed` stands at its lines (Halm 826-827; Monceaux 21713-21718, line-end hyphens aside; Reifferscheid 1132-1135), and each `englishPrinted` at its lines (ANF4 17588-17589; ANF6 40667-40670). Q2's Latin is confirmed by Fotheringham 45070-45076, so printing it is right. Halm's apparatus at 862-863 reads "lucifugax Pr" as the note says. Each rendering keeps every clause and adds nothing but Q2's joining "So". All three run six words or more, so no `secondReading` and nothing "checked at card".
- **Sources.** Every file a quotation or `uncertain` item cites is in `sources`. Each modern work sits in `modernWorks`, each `note` saying what it covers. All are public domain by date.
- **Uncertain.** Its fourteen items cover every Card item in the outline (Cut first 1-6 and 9-18, Leave out: card, What came of it 1-6, Links, Ending 2) and the fresh read's notes for the card.
- **Validator.** Scratch census outside the repository, with the card fields merged into the entry at top level, the brief as `longDescription` and the entry-field changes: 629 movements, 736 edges, 0 errors (`--skip-quotes`). The full run was killed for memory, so the quotations were checked by hand as above. With the four new fields under `card`, the only error is "card is only for a person entry": placement on a tradition is release's call.

## Rulings on the writer's three flags

1. **`legacy`, "the blood of Christians is seed": out.** It is tertullian-s-voice's quote, given word for word without marks. The slate bars it in this batch, and leaving off the marks does not make it narration. "Lines that entered common Christian speech, most famously" is a later-reception judgment no held source gives. Without the line, the rest of the sentence names a thing with no explanation (Kit Part 1). The whole sentence goes (Fix 1).
2. **`voices[4]`, the tutoring: stays.** Jerome holds it ("In his extreme old age he was tutor to Crispus Cæsar a son of Constantine in Gaul", NPNF2-3 41052-41054): a Documented fact on the card. The outline keeps it out of the story for length. What the slate rates Inferential-Thin is the tradition's influence on the imperial church, which `voices[4]` does not claim. `voices` is not one of the short texts Kit Part 1 ties to the brief. "The emperor who ended it" is not contradicted: Lactantius says Constantine's "first care" was "to restore the Christians to the exercise of their worship" (ANF7 10337). No change.
3. **`end` 320 and the `people` years 205 and 250: not changed, flagged for Mark.** No held source gives any of the three. The validator needs a whole-number `end`, and a year for each named voice in date order (validate-census.mjs 92, 603, 630-631), so they cannot just be struck. Putting a year no source holds in their place would be invention. Setting timeline years for spans the sources do not date is a fleet-level call, as with Montanism's `end` and `start` this batch. One tension for his ruling: the brief runs the tradition "to the emperor Diocletian's reign", while Jerome files Arnobius under Constantine's years (JerChron 45066) and puts Lactantius tutoring Crispus "in extreme old age" (NPNF2-3 41052-41054). So the held record does not end with Diocletian either. Arnobius's 295 is consistent with Jerome's "during the reign of Diocletian" (NPNF2-3 41022-41023) and stands.

## FIX

| # | Field | Old text | New text | Evidence |
|---|---|---|---|---|
| 1 | legacy | `Tertullian left lines that entered common Christian speech, most famously that the blood of Christians is seed. And Lactantius' Latin` | `And Lactantius' Latin` | Ruling 1. Slate (batch header): "the blood of Christians is seed" is barred. The role: put a source's own words in quotation marks. Kit Part 1, Rigor and "Explain it or leave it out". |
| 2 | teaser | `and others made the same case at Rome, at Sicca, and at Nicomedia, within sight of the emperor's palace.` | `and others made the same case at Rome, at Sicca, and at Nicomedia.` | ANF7 10161 says the *church* "was within view of the palace". No source puts the making of the case there. That is a detail moved onto the wrong event (Kit Part 1, the four faults), and the brief does not tell it. |
| 3 | voices[3] | `and whom scholars have placed anywhere between the third century and the fifth` | `and whose date is not known` | The range is a modern opinion and a modern date. Kit Part 1: "A date ... that only a modern work makes ... stays out of the story and the card." The only held dating, the NPNF note to Gennadius (NPNF2-3 42424-42426), gives "250 and some nearly one hundred years later", which contradicts it. Gennadius gives no date. This also matches `uncertain` 12, "His date is not known". |
| 4 | documentedStories[0].text | `‘not merely tortured but roasted’` | `‘not only tortured, but burnt alive’` | Quotation marks on the card must enclose a cited file's words. The held text of the passage, ANF7 10174, reads "he was not only tortured, but burnt alive". The Latin is not held. |

The Card_Edits "Not found" list otherwise stands as listed. Those claims stay in place.

## Note for release (no card change)

Q2's and Q3's `modern` carry the brief's British "laboured" and "favours". The card must match the brief, and the brief is final, so the card is right as it stands. The spelling is the brief's.
