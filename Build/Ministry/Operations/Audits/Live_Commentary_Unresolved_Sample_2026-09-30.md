# Live-surface commentary: the word "unresolved" (2026-09-30)

Companion to the rule change in `tools/check_live_commentary.py` that stops treating the bare word "unresolved" as a route-cue. This records how the change was decided and the lines it stops flagging that are still process narration, so they are not lost.

## Method

1. Counted every line containing "unresolved" in the runtime and participant-facing surfaces: 221 (records 178, website 33, engine 10). All but 4 were flagged only for that word.
2. Read all 10 engine lines, 8 of 33 website lines, and 16 records lines drawn across record types.
3. Scanned all 178 records lines for process markers ("build history", "on purpose", "this build", "Doc_04", "read only for" and similar): 21 lines, 12%, a floor.
4. Applied the narrowed cue, `unresolved (here|for now|pending|on purpose|until)`, and re-scanned the whole repository.

## Findings

- **engine, 10 of 10 read:** code identifiers, a message, a docstring, test strings. None is commentary.
- **website, 8 of 33 read:** reader-facing statements of historical uncertainty. None is commentary. They come from the source records.
- **records, all 169 lines that the narrowed cue drops, read in full:** 154 state a real uncertainty, a tension a world holds, or a record id. 15 are process narration about the build's own documents.
- Whole repository: REWRITE plus ROUTE lines fell from 5,477 to 4,654 (823 lines), and no line became newly flagged. The four lines the surviving cue still catches are all real process narration.

The earlier estimate of 20 to 55 real records lines was high. The count of clear cases is 15.

## The 15 process-narration lines the narrowed cue no longer flags

| Record | Line | What it narrates |
|---|---|---|
| `records/desert/voice_craft/desert.voice.craft.md` | 114 | "unresolved in this build's own completed content", inside a derivation note that checks a prior decision |
| `records/don/contested_claim/don.contested.refusal-of-imperial-legitimacy.md` | 119-120 | "Doc_08's own Open Item 1 stands unresolved, with the vendored Gesta transcript read only for..." |
| `records/gallic/figure/gallic.figure.martin.md` | 119 | "Doc_09 §6 item 3, a recorded disagreement, carried forward unresolved" |
| `records/gallic/story/gallic.story.circuses-amid-the-ruins.md` | 86 | a Tier 1 designation "should not carry unresolved", tier reasoning |
| `records/ijc/contested_claim/ijc.contested.homoian-content.md` | 48 | "Doc_09's Validation Layer as a standing unresolved item" |
| `records/pahc/term/pahc.term.agape-label.md` | 64 | "unresolved (Doc_02 SS4). Both loci are wording-verified against vendored files" |
| `records/rzg/contested_claim/rzg.contested.zwinglis-remembrance-vs-negotiated-consensus.md` | 37 | "This world's own build history records this question as genuinely unresolved..." |
| `records/witt/voice_craft/witt.voice.craft.md` | 204 | a derivation note on how the "disagreement" note was grounded |
| `records/lpc/contested_claim/lpc.contested.cyprian-death-genre.md` | 54 | "This world's own Doc_09 names this exact question as an unresolved escalation" |
| `records/lpc/contested_claim/lpc.contested.cyprian-death-genre.md` | 61 | which of the Construction Framework's two clauses governs, "a question this world's own build record calls..." |
| `records/lpc/source/lpc.source.bevenot-de-lapsis-and-de-unitate-critical-edition.md` | 33 | "a question row 3 currently carries as unresolved" |
| `records/lpc/term/lpc.term.heresy.md` | 35 | "That row also carries an unresolved two-recension question" |
| `records/lpc/term/lpc.term.the-one-episcopate.md` | 35 | "That row also carries an unresolved two-recension question" |
| `records/lpc/term/lpc.term.the-one-episcopate.md` | 67 | "The treatise also carries an unresolved two-recension question" |
| `records/lpc/voice_craft/lpc.craft.datus-voice.md` | 68 | a derivation note citing Permanent Prompt lines and Phase Three |

## Why the lines were not rewritten one at a time

- Several sit inside longer passages of build narration, such as the derivation notes in `voice_craft` records and lpc's contested-claim arguments about the Construction Framework. Rewording one word leaves the passage.
- Seven are lpc's, whose build thread is still active.
- Each edit rebuilds and repins a package and puts the edited field under the readability gate, which several of these fields already fail.

They belong to the batched pass that moves derivation and build narration out of `records/`, not to a line-level edit.
