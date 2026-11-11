# Round-1 adversarial review — person-brief pilot

You are the independent Opus reviewer. Read /tmp/claude-0/-home-user-CIC-Project/6d98dab9-13d8-521f-bb4d-c1b444ee38ce/scratchpad/pilot/BRIEF.md (the standard the drafter worked to) and CLAUDE.md's "Trust and source fidelity" and "Accessible and rigorous" sections in /home/user/CIC-Project/CLAUDE.md.

For each brief you are given (`<dir>/<id>.txt`, with its claim table `<dir>/<id>.notes.md`):

1. FIDELITY (blocking). Open the cited file at the cited lines (grep -n / sed -n; never cat whole files) and check EVERY claim. Do not trust the claim table. Flag: a claim the passage does not support or overstates; a detail added beyond the source; a contested point told as settled; a witness misnamed; a date wrong. Re-verify the quotation character for character against the file (python: compare the exact string with the file's text, allowing only line-wrap whitespace); report MATCH or the diff.
2. STANDARD. Mark (project lead): personal AND theological (what they fought for, developed, defended, against); storytelling, not fact-giving; flowing sentences, not elementary; years sound natural aloud; real named witnesses, never abstract roles. Specifically judge: is a modern translator or editor (e.g. "Robertson, who edited his works", "Gwynn", "Browne and Swallow, who translated...") being used as a story witness? That is the "his editor / the translator" problem with a name attached — flag it, and say whether the point should be told through an ancient witness, told directly (the source stays in the notes), or dropped. Flag strings of "X says" that read as a citation list; flat endings; AI tells; anything confusing to the ear; anything the listener would expect that is missing and that the Library clearly supports (name file+lines).
3. LENGTH by scope: Origen, Athanasius, Chrysostom near 2 minutes (~280–300 words); others as their sources allow.
4. Run: python3 /tmp/claude-0/-home-user-CIC-Project/6d98dab9-13d8-521f-bb4d-c1b444ee38ce/scratchpad/pilot/score.py <file> (band FK 8–10, FRE ≥ 60).

Substantial findings only: something wrong, unsupported, misleading, or against Mark's stated standard. "Could be stronger" with nothing wrong is not a finding.

Write your review to `<your review file>` with, per person: verdict (CLEARS / REVISE), numbered findings each marked BLOCKING (fidelity) or STANDARD, with file+line evidence and a concrete fix. Do not edit the drafts. Do not write in the repository. No model or web calls. Reply with a short per-person verdict list.
