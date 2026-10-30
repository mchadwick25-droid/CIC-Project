# Stage 1: the AI domain specialist and the gold set (S1-02, S1-03, S1-04)

Working notes of the specialist and gold set thread. Decisions are in
`../Decision-Log.md`; elapsed time is in `../Stage1_Ledger.md`. Code is in
`Sandbox/Answering-From-Sources/goldset/` and `engine/m3/gate_replay.py`.

## Said plainly: this is weaker than human labelling

**No human reviewed the labels in the gold set.** Mark ruled there is no human
domain specialist (Decision-Log entry 2), and on 2026-10-29 he handed the
rulings he was to make to an independent AI adjudication ("i would trust an
objective ai view"). Every label in `canon/gold_set/` says where it came from
(`label_source`) and carries `human_reviewed: false`. The gold set is labelled
by AI models, and every number measured against it inherits
that model's blind spots. A model can share a misreading with the judges it is
checking, especially when they come from one vendor. It can be confidently
wrong about a Latin idiom, an editor's note or a speaker inside a polemic, in a
way no automated check sees.

How the weakness is contained, mechanism by mechanism:

1. **Tested before trusted.** Seeded defects are planted in the labelling
   stream. The specialist's labels count only after it catches at least 19 of
   20 on a test set it has never seen. The tryout set that picks the model is
   not reused for the qualifying test.
2. **False alarms published beside catches.** Every test set carries 20
   controls, sentences copied from a record's own text and bound to it. A
   labeller that flags everything catches every seed and fails every control;
   both numbers are published together.
3. **Every verdict bound to exact words.** The labeller must copy the words that
   support or refute the sentence and name the block they come from. Code
   rejects any reply whose words are not in that block verbatim; one retry, then
   the line stays unlabelled and counts as a miss.
4. **Blind.** The labeller sees the sentence and its evidence pack only: never
   the question, the gates' decision, any judge's verdict, or which lines are
   seeds.
5. **A second, different model** labels at least a fifth of the gold set
   (S1-03). Every disagreement goes to Mark.
6. **Three independent reads where it matters, in place of Mark's.** Every
   disagreement between the two labellers, every item either put in a key
   class, and a random sample of agreements (86 items) was read three more
   times, each blind to the others: by Opus and by Fable with the full
   evidence pack, and by an outside-referee read that sees only the source
   passage, none of our records. A label stands only when two of the three
   give the same class. Otherwise the item is contested and left out of the
   gold set, counted and listed (`runs/adjudication-1/Excluded_Items.md`),
   never forced. A constructed item whose reads give another class is left
   out too. Mark keeps the right to spot-check any item on the packet page; a
   ruling of his overrides and is marked as human-reviewed.
7. **Held-out half sealed** by hash before any judge is tuned; only the trial's
   final scoring reads it (a test in CI enforces this).
8. **Outside referees** stay a second independent reading, and external human
   experts test the built system at the end, before any promotion.

What none of this fixes: a misreading the specialist, the second labeller and
all three adjudication reads share. Same-vendor models share blind spots, so
that is more likely than it would be across vendors or with a human. The seeded types cover four failure shapes, not all of them.

**Claude only, so weaker again.** Mark ruled no spend on other companies'
models (Decision-Log entry 10): specialist Opus 5.5, second labeller Fable
5.1, judges Haiku 4.5 and Sonnet 5.5, drafter Sonnet 4.5. All five are one
vendor's models and share training, so their blind spots are more likely to
coincide than a different lineage's would. The containment above stays in
full; it is the only check on that shared blind spot short of the external
human experts at the end.

**Qualifying rule** (Mark, 2026-10-29, adopting option (a)): the specialist's
labels count only after it catches at least 19 of 20 seeds AND marks at least
18 of 20 controls supported, on a test set it has not seen.

**Route.** No metered labelling (Mark: no API runs to test it). Labelling runs
inside the Claude plan: `goldset/inplan.py` writes the exact prompt a metered
labeller would get, one file per line, a Claude Code subagent on the named
model writes each reply, and the same code checks every reply. The subagent
is given the prompt files only, never the key.

## The pieces

| Piece | What it does | State |
|---|---|---|
| `engine/m3/gate_replay.py` | Replays each of the 308 saved drafts through the run's own shaper at the run's own commit, no model call, and keeps every sentence's verdict | Done: 308 of 308 shipped answers reproduced exactly, 11 worlds |
| `goldset/pool.py` | Every draft sentence bound to a record, with its binding and the gates' decision | 3,550 items (lpc 280); 10 not matched to a replay row, left out |
| `goldset/evidence.py` | Evidence pack: bound records as the voice saw them (records at the package's commit), source passage with its division, editors' notes marked, original language where the locus names it, the world's lexicon risk flags | Passage found for 236 of 280 lpc items; far fewer in worlds whose loci give section numbers, not lines (see below) |
| `goldset/labeller.py` | Prompt, reply schema, verbatim-evidence check | Done |
| `goldset/seeds.py` | Seeded defects by fixed rules, controls, three test sets | 60 defects (15 per type) and 60 controls accepted after reading (`Seed_Readings.yaml`) |
| `goldset/stream.py` | Blind stream with seeds planted, key kept apart | Tryout stream (40 lines); first lpc stream (280 items + qualifying set, 320 lines) |
| `goldset/runner.py` | Runs a labeller as a metered live test; settings and estimate first | Not to be used now (no metered runs) |
| `goldset/inplan.py` | Exports the labeller prompts to files and checks the replies a Claude Code subagent writes; no metered call | Done |
| `goldset/catch_rate.py` | Catch rate and false alarms per test set | Done |
| `goldset/split.py` | Calibration and held-out halves by hash of id; seal | Done |
| `goldset/cues.py` | Free pre-screen that draws likely candidates of the rare classes from the pool; a cue never labels | Done; every generalisation and embedded-voice cue labelled; about 1,300 negation and false-friend cues left, at a yield of one to three in a hundred |
| `goldset/agreement.py`, `goldset/packet.py` | Agreement between the two labellers, and the packets for Mark (disagreements, key classes, random sample) | Packets 1 to 3 (lpc 19, ten other worlds 47, constructed and new natural 20) |
| `goldset/build.py` | The gold set: labels joined with Mark's rulings (a ruling always wins), each item's origin, label source, bound records with source and locus, and evidence spans | Dry run 2026-10-29: 797 natural (all still the specialist's label), 173 constructed; waits for Mark's rulings |
| `goldset/constructed.py` | Constructed items for classes the natural sentences leave short, read before use (`constructed/Constructed_Readings.yaml`) | 173 accepted of 263 read |

## Natural and constructed items, counted apart

The natural sentences do not hold 40 items of each key class. After every
cue-drawn and random items were labelled (lpc 280, the ten other worlds 517,
every generalisation and embedded-voice cue among them), the specialist found: negation or modal shift 14, generalisation 12,
false friend 2, embedded voice 1. These are the specialist's labels before
Mark rules.

So the four short classes are topped up with constructed items, as ruled.
Each was written by one Opus subagent to carry one defect, bound to the
record whose own words make it certain. A different Opus subagent read each
against its record. The gold set thread then rejected six more for a second
defect, a draft or provisional record, or wording that gave it away.
Accepted: negation or modal shift 41, generalisation 40, false friend 44,
embedded voice 48. Most rejections were false friends that stated a
lexicon flag as a definition (39 of the first 45).

The accepted items were then labelled blind, mixed with 121 natural items in
one stream. The specialist found every one unsupported, and 172 of 173 in
the class it was built to carry. The one it read differently goes to Mark.

Every count keeps the two apart. A constructed item has kind "constructed"
in the stream key and in the gold set. It tests whether a judge catches a
known defect, as a seed does, and says nothing about how often the defect
occurs. Only the natural items give rates, and only the random draws among
them give natural rates.

## Known limits of the tooling

- **Passage location outside lpc.** Most worlds' record loci name a section
  ("Vita Antonii SS3", "Letter XXII, sec. 30"), not file lines. The pack then
  shows the record and says the source was not located. Located: lpc 236/280,
  gallic 365/444, witt 185/310; most others under a third. A locus resolver for
  section references (the proposal's planned `locus_ids` row field would remove
  the need) is the next tooling step before other worlds are labelled.
  Since 2026-10-29 the pack also locates a passage by a ThML division id the
  locus names, by lines given in a locus whose source record names one file,
  by any quoted run of 18 or more characters, and by a section number walked
  down the edition's own division numbering (`goldset/locus.py`: every step
  must match exactly one division or numbered paragraph, inside the one
  division whose title holds the work's name; anything ambiguous is left
  unlocated). Located now: lpc 236/280, gallic 381/444, witt 193/310,
  ijc 145/360, desert 139/341, alx 119/251, don 116/455, pahc 106/319,
  rzg 93/168, syr 51/320, hal 28/302.
- **False-friend seeds come from the lexicon flags.** They test whether the
  labeller uses the risk flags it is given, not whether it spots an archaic
  English sense nobody flagged ("prevent" for "go before"). Natural items and
  Mark's adjudication carry that class.
- **Embedded-voice seeds** are the opponents' or outsiders' words inside a
  record, voiced as the tradition's. Nine were written by hand from named
  records, since the fixed rule reaches etic records only.

## Incident: a metered attempt after the hold (2026-10-29)

At 18:17 UTC this thread started the first sample of `specialist-tryout-1`
(GPT-6.1 Sol 18:17:09.260 to 18:17:09.707, Grok 4.7 18:17:16.331 to
18:17:16.739). The coordination thread's HOLD (18:06) and Mark's Claude-only
ruling (18:07) had arrived but had not been read: the thread did not drain
its messages before the call. Bedrock refused both calls (model access not
enabled), no label was made, and AWS bills nothing for a refused call; the
guard counted the two holds ($0.1416 and $0.0869). Ledgers:
`runs/specialist-tryout-1/`. The non-Claude seam and price rows were removed
from the branch afterwards. Rule now kept: read every pending message before
any step that could call a model.

In-plan judge and labeller helpers run as `.claude/agents/judge-reader.md`, which holds Read and Write only (Mark, 2026-10-30), after helpers with wider tools wrote outside their files and reached other sessions.

## The gold set, 2026-10-30

Built by `goldset/build.py` from every label and adjudication run 1, split and
sealed into `canon/gold_set/` by `goldset/split.py` (salt `gold-split-1`; the
first seal, made before any judge saw either half).

| Origin | Items | Label source |
|---|---|---|
| Natural | 788 | AI-adjudicated 64, agreed by two labellers 102, specialist only 622 |
| Constructed | 172 | AI-adjudicated 12, by construction 160 |

Left out: 9 natural items contested, and 1 constructed item whose three reads
all gave negation or modal shift where it was built to carry embedded voice.

Natural items by class: supported 609, unsupported (other) 127, negation or
modal shift 9, generalisation 6, false friend 1, embedded voice 1, cannot judge
23, no claim 12. Constructed items by class: negation or modal shift 41,
generalisation 40, false friend 44, embedded voice 47. The two origins are
never added together.

Adjudication run 1: of the 86 items, 32 stood with all three reads agreeing,
45 with two of three, 9 contested. Opus and Fable gave the same class on 70.
The outside referee could not judge 23, mostly where no source passage could be
located; it agreed with Opus on 34 and with Fable on 37. Elapsed: prompts
written 20:13, all 258 reads in by 20:19 plus one retry, gold set built and
sealed by 20:25 UTC.
