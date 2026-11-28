# Grade: Tertullian, after the fix pass (Mark, 2026-11-28, "a")

Method: Stage Two Kit section 5, run as `../Grade/` was: the same reader prompts, `merge.py`, `grade.py`, `grade_whole.py` and `score_this.py`, copied unchanged; all readers fresh Opus subagents, no metered spend. Packets carry the brief after the fix pass (`packets/S01.md`, `packets/L01.md`).

- Scans: two bare-statement readers (`scans/S01_bare_A.md`, `S01_bare_B.md`: 2 findings each, both matched), one modern reader (`S01_modern.md`: 0). `merge.py`: 2 agreed, 0 to the third read, so no third read was run (`Held_Findings.json` from `--finish`).
- Listener: `listener/L01.md` (0 test lines, opening ok, 1 bare, 0 tells, 1 thread; pulls in; listens to end; form: story).
- **Result (`Grade_Whole.json`): rigor B (load 1.7), craft C (load 3.4), overall B, "OK to keep".**
  - rigor, bare, Supporting: "Jerome, who wrote his life, says the envy and insults of the clergy of Rome drove him to the New Prophecy." (Jerome gives no further why: JER 40506–40509)
  - rigor, bare, Passing: "Later he broke from the prophets too and gathered meetings of his own." (Augustine gives no reason: AUG 2872–2873; Mark's ruling: add nothing)
  - craft, bare: the same break from the prophets
  - craft, thread (medium): "The church would forgive sins, he wrote, but it would be the church of the Spirit, through a spiritual man, and not the church that is a number of bishops."
- Blind comparison: `Blind_Result.md` (passes, B / C+ / B).
