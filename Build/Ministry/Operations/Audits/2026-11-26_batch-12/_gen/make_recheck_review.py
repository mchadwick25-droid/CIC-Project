"""make_recheck_review.py <slug> -> Recheck_Review_Prompt.filled.md (targeted recheck of the researcher's review fixes)"""
import sys
B='Build/Ministry/Operations/Audits/2026-11-26_batch-12'
slug=sys.argv[1]
head,body=open(f'{B}/{slug}/Checker_Prompt.filled.md').read().split('\n---\n',1)
p='''# This pass: the targeted recheck of the review fixes

The review (`Review.md`) found errors the outline held or lacked, and the researcher fixed them in `Outline.md` (`Fixes_Review.md`). Read `Review.md`, `Fixes_Review.md`, `Outline.md` and `Source_Sheet.md`, and check only these: each item under **Worded by me**, at its cited lines, says no more than its source, with the right confidence and witness kind; each "needs the outline" finding is now met; each item under **Not applied** is judged, by its cited lines; and the beats still follow the story once, in order, with the approved heart kept. Report the outline's expected length after the fixes.

Write `Recheck_Review.md`: PASS, or FIX with the exact replacement text for each finding, marked BLOCKING or MINOR. Do not edit the outline or commit. Reply in under 120 words.

For reference, your role as checker follows.
'''
open(f'{B}/{slug}/Recheck_Review_Prompt.filled.md','w').write(head.rstrip('\n')+'\n\n---\n\n'+p+'\n'+body); print('ok',slug)
