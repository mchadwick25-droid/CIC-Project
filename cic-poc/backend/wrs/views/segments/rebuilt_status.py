"""Voice Rebuild (2026-08-08) - which worlds have completed their Phase 2
pass: voice authored FRESH from source records, not a Phase-0 port of
the current deployed prompt (which is what every world's craft table
is today, including Desert's - a faithful transcription, never a
rewrite; see craft.py's and craft_pahc.py's own docstrings).

Read by every assembler's readability-gate wiring (Blueprint 0.3) to
decide warn-only vs enforce: enforcing the floor against un-rebuilt
text would go red on content only Phase 2 fixes (confirmed: 4 of 6
worlds' current text fails the floor somewhere). One flag per world,
one place - Phase 2 flips a world's entry to True in the same commit
that lands its freshly-authored craft table, so there is exactly one
place to remember, not six assembler files."""

# Flipped for the three worlds whose Phase 2 pass has landed. This was
# MISSED on Albina's and Marius's own commits - the docstring above says
# Phase 2 flips a world "in the same commit that lands its freshly-authored
# craft table", and neither did, so both shipped with their readability gate
# still warn-only. Corrected here for all three at once; each was verified
# to pass the floor under enforcement before its flag moved.
REBUILT = {
    "desert-monasticism": False,
    "post-apostolic-house-church": True,
    "syriac-edessa-nisibis": True,
    "alexandria-catechetical": True,
    "imperial-juridical-christianity": True,
    "hieronymian-ascetic-literary": True,
}
