"""make_recheck.py <slug> [--with-fix]  -> Recheck_Length_Prompt.filled.md
--with-fix: the outline recheck of the fix pass (Fixes.md) that waited on the length ruling is done in the same pass."""
import sys
B='Build/Ministry/Operations/Audits/2026-11-26_batch-12'
slug=sys.argv[1]; withfix='--with-fix' in sys.argv
cp=open(f'{B}/{slug}/Checker_Prompt.filled.md').read()
head,body=cp.split('\n---\n',1)
extra=('\n\nThis pass also does the recheck of the fix pass that waited on the length ruling: read `Outline_Check.md` and `Fixes.md` as the role\'s recheck pass says, and check what it names there as well. Give those findings in the same file, marked "fix pass".' if withfix else '')
p=f'''# This pass: the targeted recheck of the length cut

The researcher has cut `Outline.md` for length and listed each change in `Fixes_Length.md` (the ruling behind it is quoted there and in the outline's Length or Length ruling line). Read `Fixes_Length.md`, `Outline.md` and `Source_Sheet.md`, and check only these: each cut went to the card or Leave out as marked and is gone from the beats, quotes, glosses and credits; no cut takes the record's force, an explanation Part 1 requires (Explain it), the scene that carries the story's craft, or the approved heart; each line the researcher changed or wrote besides the moves says no more than its cited source, with the right confidence and witness kind; nothing the cuts left behind still points to a cut item; and the beats still follow the story once, in order. Check the expected draft length against the ruling.{extra}

Write `Recheck_Length.md`: PASS, or FIX with the exact replacement text for each finding, marked BLOCKING or MINOR. Do not edit the outline or commit. Reply in under 120 words.

For reference, your role as checker follows.
'''
open(f'{B}/{slug}/Recheck_Length_Prompt.filled.md','w').write(head.rstrip('\n')+'\n\n---\n\n'+p+'\n'+body)
print('ok',slug,withfix)
