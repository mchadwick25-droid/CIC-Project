"""make_review_fix.py <slug> "<items>"  -> Review_Fix_Prompt.filled.md (the outline fixes a review needs)"""
import re, sys
B='Build/Ministry/Operations/Audits/2026-11-26_batch-12'
slug,items=sys.argv[1],sys.argv[2]
cp=open(f'{B}/{slug}/Checker_Prompt.filled.md').read()
head=cp.split('\n---\n')[0].rstrip('\n')
name=re.search(r'\*\*Story:\*\* (.*?) \(census',head).group(1) if slug!='era-1' else 'Era 1, The Early Church Era'
role=open('Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/researcher.md').read().replace('{NAME}',name).replace('{FOLDER}',f'{B}/{slug}').replace('{SLUG}',slug)
p=f'''# This pass: the outline fixes the review needs

The review (`Review.md` in this folder) found errors the outline itself holds or lacks, marked "needs the outline": {items}. Apply those to `Outline.md` only, with the smallest change that meets each, checking what you write in the cited file at its lines, and add the review's Do not say lines for them word for word. Change nothing else, and keep to the outline's length. Write `Fixes_Review.md` with three lists: Applied verbatim, Worded by me (exact new text and its file lines), Not applied (with the lines that show why). Do not edit the brief, commit, or edit outside your folder. Reply in under 100 words.

For reference, your role as researcher follows.

'''
open(f'{B}/{slug}/Review_Fix_Prompt.filled.md','w').write(head+'\n\n---\n\n'+p+'\n'+role); print('ok',slug)
