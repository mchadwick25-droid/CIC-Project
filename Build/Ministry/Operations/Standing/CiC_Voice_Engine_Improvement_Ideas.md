# Voice Engine — Improvement Ideas

Ideas for improving the voice engine that the project lead has seen and set aside, kept so they are not lost. An entry here is not approved, scheduled or built. None of it touches the engine, the records or the packages until the project lead decides to take it up.

Ground rule for every idea here, set by the project lead on 11 October 2026: improve live by cleaning up and fixing at the source. Add no layers and no API cost, and put none of the quality already reached at risk.

---

## Remove the quote index from the compiled prompt

**Status:** set aside, 12 October 2026. A branch from the live version was built and then dropped unpushed. Nothing reached GitHub or live.

**What it is.** Each world's compiled prompt carries a section, "Quotes we hold", that lists every quote record with its id, its speaker and its first few words (`engine/m2/builders.py`, `build_prompt`). The voice sees it on every turn. A quote's full wording reaches the voice separately, in the turn's evidence block, when that turn retrieves it.

**Why it is there.** The index was added because the voice had invented quote ids when it reached for a real quote it could not see. For example, it cited `ijc.quote.leo-two-natures` for the record actually named `ijc.quote.leo-tome-each-form`.

**The case for removing it.**
- **Cost, measured.** Removing it makes the fleet's compiled prompts 5.3% smaller, from 1,029,600 to 974,662 characters. It saves the most on desert (12.2%), gallic (10.8%) and ijc (8.4%). Since the prompt is cached once per conversation and read on each later turn, that is roughly 2–3% of conversation spend, about a tenth of a cent per turn.
- **Quality, not measured.** Showing every quote's opening words may tempt the voice to finish a quote from memory. That would produce reworded quotes, which the 9 October record pass staging reading found (gap class A, 22 items).

**The case against.**
- Removing it may bring back the invented quote ids it was added to stop. On the live version an invented id is not shown as a misquote. The sentence is withheld instead, so the reply has a gap.
- Whether the change reduces misquotes or adds gaps is unknown, and the only test that costs nothing is the project lead's own conversations.

**What a build would involve.** The same deletion as `aec3ab008` on `main` (PR #846), applied to the live tree without the quote-placement work from #841 that sat beside it there. That deletion covers the builder section, the deployed-prompt check, the speaker-label checks, and the gallic and cappadocian quotation notes that name the index. After it, every world's package is rebuilt and re-pinned, which makes every world's admission stale. The prompts produced were checked: the only change was the removed section and the two quotation notes.

**What would make it worth taking up.** Evidence that the index itself causes reworded quotes, rather than the voice's own habit. For example, a reading that finds reworded quotes matching the index's opening words.
