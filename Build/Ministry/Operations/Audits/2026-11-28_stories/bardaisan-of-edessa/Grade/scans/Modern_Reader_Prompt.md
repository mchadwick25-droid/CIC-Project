# Reader: modern opinion

You read pieces of the Church Family Tree once, in order, and look for one thing only: modern opinion in the text.

## The rule (Mark, 2026-11-23)

"No modern opinion, guess or reconstruction in a story." And: "more current scholors can be used as sources if they are historical and source bound, but not referenced in the text of the briefs and stories. they if they are needed then they go in the reference list after the story or brief."

The record itself is the old witnesses: writers of the time or close to it, such as Eusebius, Socrates, Jerome, Evagrius, a council's acts, a medieval chronicler. Quoting or crediting them is fine. You never flag them.

## What you flag

1. **A modern writer in the text.** Any modern scholar, editor, translator, historian or "historians", "scholars", "modern research", named or unnamed, dated or not. Examples: "a modern historian thinks", "his editors note", "an editor judges", "scholars believe", "most historians now date", "Wigram wrote in 1910".
2. **A guess told as story.** A claim the piece itself presents as a modern guess, inference or reconstruction rather than what an old source says: "probably", "it may be that", "seems to have", "is thought to", "likely", "historians have reconstructed", or a date, author or cause given as a modern judgment. Flag it only where the wording shows it is a guess or a modern view. Do not flag plain statements because you suspect them.

Not a finding: an old witness credited by name; a modern event told as an event (a manuscript found in 1945); the piece saying plainly that the old sources are silent.

Each piece may end with **Script candidates**: sentences a word search marked. They are a starting point only. Many are not faults, and the search misses some. Read the whole piece.

## How crucial each one is

First write the piece's heart in one sentence (use the **Approved heart** where the packet gives one). Then weigh each finding against it: **3 Crucial** (the heart rests on it), **2 Supporting** (a part the piece spends real time on), **1 Passing** (on the way).

## What you write

Write one file at the path you are given. For every piece, in order:

```
## <piece key>
Heart: <one sentence>
Findings: <number>
- "<the exact words, copied from the piece>" | kind: modern writer / guess | weight: 3 / 2 / 1 | who: <the modern writer or view, if named; else unnamed>
```

A piece with none gets `Findings: 0`. Copy the words exactly. Do not suggest fixes and do not read anything but the packet.
