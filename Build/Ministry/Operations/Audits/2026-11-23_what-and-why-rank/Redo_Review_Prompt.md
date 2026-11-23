# What-and-why redo: fresh read (Opus)

You review one rewritten Church Family Tree text. You did not write it. Read `Build/Ministry/Features/Church-Family-Tree/Brief-Kit/Kit.md` (Parts 1 and 2, and "The bar" in Part 4), `Build/reference/method/Pass2-decisions/VR_1A_Writing_Standard_2026-08-09.md`, and `Redo_Writer_Prompt.md` in this folder, whose list of faults that fail on sight is part of your bar.

1. **One hearing.** Read the new text once, straight through, before anything else. Write four plain lines: who or what this is, what happened, what it was about, and why it matters. A line you cannot write is BLOCKING. List every charge, teaching, book, quarrel or decision it names; one you could not explain after one hearing is BLOCKING.
2. **Craft.** Mark every sentence that reads as generated: a summing-up or moral closer, a line that only says what is missing or what the sources do not say, a dash, colon or "not X but Y" turn used for drama, a run of one-act sentences, stock words, or reporting on the record in place of telling it. Each is BLOCKING. Say whether it sounds like an adult documentary narrator telling a story, and where it does not.
3. **Findings.** Read the packet's findings and the old text. Each finding is explained from a source or cleanly cut. A cut that leaves a hole the listener can hear is BLOCKING.
4. **Sources.** Open every file the notes cite, at the lines given, and confirm it says what the new text says. Check each quote word for word. A claim with no source, or a source that does not hold it, is BLOCKING. No modern scholar or "historians" appears in the text. Every field of a listed modern work comes from a file.
5. **Score.** Run `python -m engine.m1.profile_readability <text file>`.

Score voice, craft, rigor and accessibility from 1 to 5, each with a reason. Write the review file you are given: the four lines, the scores, PASS or REVISE, and each finding marked BLOCKING or MINOR, with the exact change. "Could be stronger" is not a finding. Do not edit the text or commit. Reply in under 150 words.
