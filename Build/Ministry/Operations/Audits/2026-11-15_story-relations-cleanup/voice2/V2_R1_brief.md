# Review brief, round 1: "How it connects" lines, new voice

You are a fresh, independent reviewer. Review the drafted "How it connects" lines for Church Family Tree story cards. You did not write them. Be exacting on fidelity, honest about craft, and do not invent problems: a line that *could* be stronger with nothing wrong in it is minor at most.

## Read first
- scratch/BRIEF.md (the drafting rules: Mark's converged decisions). Hold the lines to every rule there.
- /home/user/CIC-Project/CLAUDE.md, "Trust and source fidelity" and "Accessible and rigorous".
- /home/user/CIC-Project/Build/Ministry/Features/Church-Family-Tree/Who_Profile_Pattern.md, "Craft" and review checklist items 1-9 (the parts that apply to a short reader line).
- scratch/voice_samples.txt: the voice Mark approved.

## For each assigned story
Open the draft scratch/draft/NN_<id>.json and the packet scratch/pk/NN_<id>.json (card + linked census). Census entries not linked are at scratch/mov/<id>.json; the index is scratch/census_index.txt.
Check:
1. Fidelity (blocking if it fails): every claim in the line, including the "what it shows" sentence, is said by the card (text, teaser, caveat, sources) or a census entry. Check each support quote is really in the packet or census file, verbatim, and that it establishes at least what the line says. Hedges kept. Nothing from the old lines carried without card/census support. Traditions named correctly (right tradition, right name, not an id). No overstatement ("first", "only", "began", causal links the source doesn't make).
2. Form (blocking): exactly two sentences; first gives the connection, second what it shows; no builder or data talk; no dashes, colons, semicolons used to stretch.
3. Craft (blocking only if clearly bad; else minor): reads aloud in one breath per sentence; plain words; no AI tells (X-not-Y contrasts, aphorism/tag lines, triads, unearned adjectives, filler); no setup before the point; not a restatement of the card; adult register. Lines that read dense (heavy nested clauses, strings of proper names) should be named with a plainer suggestion. The lines currently average about 45 words; Mark's range is about 35-45, and a plainer line nearer 38-42 words is welcome where it loses no claim.
4. Common names: a name that could mean more than one person has its place at first mention.

## Output
Write scratch/rev/R1_<batch>.md with, per story: `### NN id`, verdict PASS / MINOR / BLOCKING, each finding numbered with its type (fidelity/form/craft/name), the exact words at issue, why, and a suggested fix in full replacement wording when you can give one that stays within two sentences and every claim supported (give the support quote). Then a one-paragraph summary of patterns.
Use only Read, Write, Glob and Grep. Do not edit drafts or anything in the repository. Reply with counts: PASS / MINOR / BLOCKING and the ids of the blocking ones.
