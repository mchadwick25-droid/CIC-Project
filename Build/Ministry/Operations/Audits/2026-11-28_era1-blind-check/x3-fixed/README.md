# x3-fixed: three-reader blind check on two fixed briefs (2026-11-28)

This uses the same design as `x3/`. Each story was judged against the three references on `main` (`Brief-Kit/reference/`: basil-of-caesarea, epiphanius-of-salamis, john-chrysostom). Each pair had its own fresh Opus judge, with X and Y randomized. Each judge read only its two files and Kit.md Part 1. The judge prompt is `x3/pairs/p01/prompt.txt` word for word; only the file paths were changed.

Briefs:
- methodius-of-olympus: `claude/cft-release-batch12-13` @ a030d239, `Build/Ministry/Operations/Audits/2026-11-26_batch-12/methodius-of-olympus/methodius-of-olympus.brief.txt`
- josephus: `claude/cft-fix-josephus-grade` @ 6e5676b1, `Build/Ministry/Operations/Audits/2026-11-26_batch-12/josephus/josephus.brief.txt`

**Pass:** at least 2 of 3 judges give the story B− or better and don't call it clearly worse.
**Confirmed fault:** a fault named by 2 or more judges.

`key.json` maps the X/Y labels. `results.json` holds the grades and verdicts. `pairs/pNN/reply.txt` holds each judge's reply.

## Results

| Story | vs Basil | vs Epiphanius | vs Chrysostom | Result |
|---|---|---|---|---|
| methodius-of-olympus | B (story somewhat better) ✓ | C (ref clearly better) ✗ | C (ref clearly better) ✗ | FAIL (1/3) |
| josephus | C+ (ref somewhat better) ✗ | B (story somewhat better) ✓ | C+ (ref somewhat better) ✗ | FAIL (1/3) |

## Confirmed faults

methodius-of-olympus
- It is not one story in order. It switches back and forth between the Banquet and On the Resurrection (3/3).
- It tells one thing twice. "A later bishop copied his words" comes back as the full Epiphanius paragraph (3/3).
- The narrator restates the statue quote straight after it: "The flaws, that is, melt away… not lost" (3/3).
- No risk, choice or question runs through it (2/3: p01, p03).
- The Photius line ("as Photius summed it up in his reading notes centuries on") adds a name the story doesn't need and breaks the flow (2/3: p02, p03).

josephus
- The order breaks. The surrender and the Rome years come in paragraph 2, then the story goes "Back in the cave", so the surrender is told twice or more (3/3).
- "The passage itself says he was the Christ" repeats the quote and leans to one side of the dispute (3/3).
- A gloss is added on after the quote: "The Greeks are those who were not Jewish" (3/3).
- "in the north of the country" is unclear, because the country is never named (2/3: p04, p06).
