# OVER_SETTLING fold vs pair — 3 draws per path, 56 turns, 2026-08-16

```
FINDINGS ACROSS 3 DRAW(S) OF 56 TURNS
                                pair      fold
    total confirmations           27        40
    mean per draw                9.0      13.3
    turns confirmed always         2         2
    turns confirmed sometimes        16        24

SELF-CONSISTENCY (same turn, same code, repeated draws)
    pair: agreed with itself on 40/56 turns (71%); flipped on 16
    fold: agreed with itself on 32/56 turns (57%); flipped on 24

STABLE DISAGREEMENTS (the only ones worth acting on)
    pair always / fold never : 0   <- regressions
    fold always / pair never : 1   <- gains

  GAIN [11] syriac-edessa-nisibis
      turn: We hold some things by our own eyes and ears, and some by what was handed to us, and we do not blur the two. T...
      limit: The empty see belongs to the founding story and the martyr tradition, not to the current generation's own living memory—your distance from it should match the distance yo

  full detail written to /tmp/claude-0/-home-user-CIC-Project/611f54e7-88e8-5b58-8233-278c31460890/scratchpad/reps3.json

VERDICT
  No stable regressions. The fold confirmed 40 times across
  3 draws against the pair's 27, and found 1 finding(s)
  the pair never made on any draw.

  BUT both paths are unstable (16 and 24 turns flip
  between draws). A check that answers differently on the same
  turn is a quality problem in its own right, independent of
  which variant ships - worth deciding on before the flag.
```
