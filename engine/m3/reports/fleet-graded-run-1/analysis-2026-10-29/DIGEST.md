# Fleet run 1: one-page digest for the design pass

Read this instead of the raw reports.

## The seven failure families (shared across worlds)
1. **Cut leaves damage.** The engine removes sentences it cannot place (quote lead-in without a speaker 81, typed quotation 42, unplaced quote tag 32, untold story 28, attribution without quote 24, quote mismatch 23). Nothing repairs what pointed at them. About 55 to 60 true orphans; some change meaning (pahc: "He meant it as mockery" now points at the wrong man; lpc: Cyprian's phrase "contagion of the ancient death" ends up in Augustine's mouth). 30 true, well-cited sentences were cut.
2. **False silence.** The voice says "no source exists" where the period's sources exist. Seen in lpc, rzg, pahc, witt, ijc, don, cappadocian, desert, gallic, alx.
3. **Right record not offered / no record for the question type.** don 16/28, pahc 13/28 turns had no record written for that question. Gaps: original sin, fate of outsiders, being born again, apostolic practice, survival today.
4. **Build talk reaches the reader.** "this turn", "the records I am holding", "vendored", "THIN GROUND", raw `[[tags]]`, and stock lines such as "The short answer first. Yes."
5. **After-window knowledge.** Later churches and councils named as known events (first-pass reviews: lpc, ijc, hal, syr, pahc, don). The outside referees' alx and rzg window findings are withdrawn: I gave them wrong windows (alx is 150 to 400, rzg 1519 to 1650).
6. **Cautions misused.** They compile as citable text written as instructions to the builder. Read aloud (lpc caution 17) or read as denials.
7. **Padding.** Whole records pasted in; stock passages repeated; answers of 400 to 840 words. 1,400 to 3,000 unneeded words per world.

## The test
It used the admission harness, not the live path. Skipped: live directive, gate and reader, recitation retry, self-revision, length limit. Its checks passed 336 of 336. 12 worlds ran at 11 commits. Cut-step replay on saved drafts reproduces shipped answers 308 of 308 for free.

## Per world (second pass ship/fix/block; outside rejects of 10 seen; alx's 2 void)
lpc 11/11/6 (4); gallic 16/8/4 (2); desert 16/10/2 (3); ijc 20/4/4 (3); alx 20/6/2 (0, 2 void); witt 20/7/1 (3); rzg 16/8/4 (4); pahc 18/6/4 (4); hal 16/10/2 (1); syr 18/8/2 (0); cappadocian 17/9/2 (2); don 18/10/0 (1).

## Concrete examples a design must handle
- lpc F4-T: "We would not use those exact words… not the way our own record speaks of it." False. Two records quote "not regenerated" and "born of God"; Cyprian's *secunda nativitas*. No record says how this world names baptismal rebirth.
- lpc F5-E: "Augustine wrote to the people of Fussala about a basilica." The core record says only "a pastoral letter describes an apse".
- lpc F3-I: "No text a woman wrote herself survives." Perpetua, Carthage 203.
- cappadocian F6-T: "our records are silent on the fate of outsiders." Gregory of Nyssa, De infantibus; Nazianzen Or. 40.23; Basil Reg. brev. 267.
- desert F6-E: reads the build back ("this turn's ground", "THIN GROUND notes") and adds `[[thin:liturgy]]`.
- pahc n26: Pliny's worship details said to come from torture; `pahc.witness.outsider-view` says they came from the believers he questioned.

## Library facts that matter (from the frozen D3 design and the repo)
- Shelf is computed at compile time from `cic/corpus-map` and written into the package. `engine/m9` checks quotes byte for byte against it. Covers about a third of voiced material.
- Voicing of non-tradition rows needs a pair relationship plus a per-row `documented_exchange` tag. About 115 source records are unvendored and etic-only.
- Every `cic/texts` or corpus-map merge stales affected worlds. A workflow opens one repin PR per world.
- Wants register (PR 1241) has 15 unclassified rows awaiting a decision.
- Repo is 3 GB, `cic/texts` about 1.9 GB (1,528 files).

## Open, unverified (see brief 4D)
Voicing gate causing false silence; archaeology wants row feeding "nothing physical survives"; shared single-unit files limiting locus.
