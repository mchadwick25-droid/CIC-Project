import sys
B='Build/Ministry/Operations/Audits/2026-11-26_batch-12'
LR='Mark, 2026-11-27, "Batch 12: lengths measured by the draft": "approve as recommended". This batch only.'
for s in sys.argv[1:]:
    target = 525 if s=='era-1' else 675
    rp=open(f'{B}/{s}/Researcher_Prompt.filled.md').read()
    head,body=rp.split('\n---\n',1)
    task=f"""

---

# This pass: name the cuts, with the measuring draft in hand

Mark ruled ({LR}): this story was drafted to measure only, and its researcher names the cuts that would bring the draft to {target} words, and what each would take from the heart. The real counts and those cuts go to Mark on one page.

Read `{s}.measure.txt` (the measuring draft, every Cut first item already out) beside `Outline.md` and the outline's "Approved heart and length" section. Do not edit the outline or the draft. Write `Cuts_Named.md` in this folder:
1. The draft's word count (`wc -w`).
2. The cuts that cost nothing of the heart, in order, each with the words it saves by the draft and where it goes (card or Leave out), and the count after them.
3. If that does not reach {target}: the further cuts, in order, each naming exactly which part of the approved heart, the Never cut list or the record's force it takes, the words it saves, and the count after each. Stop at {target}.
4. Your recommendation in two or three sentences: the length this story needs to keep its heart, and which cuts, if any, you would make.

Keep within Part 1's rules: never cut an explanation Part 1 requires without the thing it explains, and cut an event before its meaning. Do not commit or edit outside your folder. Reply in under 120 words: the draft count, the count after the free cuts, and your recommended length.

For reference, your role as researcher follows."""
    open(f'{B}/{s}/Cuts_Prompt.filled.md','w').write(head+task+'\n\n'+body.split('## The fix pass')[0])
    print('ok',s)
