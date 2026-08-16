# OVER_SETTLING fold vs pair — 3 draws per path, 56 turns, monitoring temperature 0.0

Prior run at the API default temperature: 2026-08-16_over_settling_reps3.md

```
FINDINGS ACROSS 3 DRAW(S) OF 56 TURNS
                                pair      fold
    total confirmations           22        44
    mean per draw                7.3      14.7
    turns confirmed always         3         6
    turns confirmed sometimes        12        19

SELF-CONSISTENCY (same turn, same code, repeated draws)
    pair: agreed with itself on 44/56 turns (79%); flipped on 12
    fold: agreed with itself on 37/56 turns (66%); flipped on 19

STABLE DISAGREEMENTS (the only ones worth acting on)
    pair always / fold never : 1   <- regressions
    fold always / pair never : 4   <- gains

  REGRESSION [48] post-apostolic-house-church
      turn: There was a moment. The water.

Before it comes teaching. We lay out the two ways before a person — a way of l...
      limit: The material distinguishes the water as the entry-point ("the washing that marks a person's entry into the community") and the table as what forms ongoing belonging ("the

  GAIN [11] syriac-edessa-nisibis
      turn: We hold some things by our own eyes and ears, and some by what was handed to us, and we do not blur the two. T...
      limit: The permanent prompt states plainly that "what the vow's daily inside was, and what shape the order carried beyond its existence, our record does not tell us," yet the re

  GAIN [14] syriac-edessa-nisibis
      turn: A vowed one and a married one keep near the same week, in the same streets. Both rise before dawn for the vigi...
      limit: The material explicitly flags that Ephrem's personal founding and direction of the bnat qyama choirs is "this later tradition's own claim" (Jacob of Serugh's sixth-centur

  GAIN [26] post-apostolic-house-church
      turn: The workday owns us, same as it owns everyone in this city. Shops open at first light. Labor is hired by the d...
      limit: Pliny's account comes from interrogation of arrested members under threat, and what he recorded was what those members told him they did — not an independent observation 

  GAIN [56] post-apostolic-house-church
      turn: One thing. Come to the table.

Whatever else we have argued about, and we have argued, that is where we return...
      limit: The material holds three genuinely different thanksgiving orders (the Didache's order with cup first and no supper narrative, Rome's order with reading and discourse firs

  full detail written to /tmp/claude-0/-home-user-CIC-Project/611f54e7-88e8-5b58-8233-278c31460890/scratchpad/temp0.json

VERDICT
  BLOCKED. 1 turn(s) where the pair confirmed on every
  draw and the fold on none. That is a stable loss, not variance.
  Read the limits above: if the fold's Phase 1 never enumerated
  the claim, the enumeration instruction needs work, not the ruling.
```
