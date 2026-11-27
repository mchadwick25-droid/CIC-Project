"""make_length.py cut <slug> <draftwords>  -> Length_Cut_Prompt.filled.md (draft over 675, back to the researcher)
   make_length.py apply <slug>...           -> Length_Apply_Prompt.filled.md (apply the cuts the long-story length ruling names)"""
import re, sys
B='Build/Ministry/Operations/Audits/2026-11-26_batch-12'
role=open('Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/researcher.md').read()
def head(slug):
    h=open(f'{B}/{slug}/Checker_Prompt.filled.md').read().split('\n---\n')[0]
    name=re.search(r'\*\*Story:\*\* (.*?) \(census',h).group(1) if slug!='era-1' else 'Era 1, The Early Church Era'
    return h.rstrip('\n'), name
def body(slug,name): return role.replace('{NAME}',name).replace('{FOLDER}',f'{B}/{slug}').replace('{SLUG}',slug)
mode=sys.argv[1]
if mode=='cut':
    slug,n=sys.argv[2],sys.argv[3]; h,name=head(slug)
    p=f'''# This pass: the length cut, with the draft in hand

Mark ruled (Mark, 2026-11-27, "Batch 12: lengths measured by the draft": "approve as recommended". This batch only.): the draft is the measure. A draft over 675 words goes back to its researcher, who cuts the outline with the draft in hand; a targeted recheck and a redraft follow. A story that cannot get under 675 without its heart goes to Mark with its draft's count and the cuts named.

Your outline and source sheet are in this folder. The writer's draft, `{slug}.brief.txt`, runs {n} words with every Cut first item out. Read it beside `Outline.md`, and see which beats, glosses and credits cost the words. Then cut `Outline.md` so that a draft of it comes to 675 or under: move items to the card or Leave out, as marked, and add each to Cut first in order. Never cut the record's force, an explanation Part 1 requires (Explain it), or the scene that carries the story's craft; cut an event before its meaning. Keep the approved heart. If it cannot reach 675 without the heart, stop and say so, with the count it can reach and what the next cuts would take.

Write `Fixes_Length.md`: each cut, where it went, and the words it saves by the draft. Do not edit the draft, commit, or edit outside your folder. Reply in under 120 words: the expected draft length, and anything that touches the heart.

For reference, your role as researcher follows.

'''
    open(f'{B}/{slug}/Length_Cut_Prompt.filled.md','w').write(h+'\n\n---\n\n'+p+'\n'+body(slug,name)); print('ok cut',slug)
else:
    for slug in sys.argv[2:]:
        h,name=head(slug)
        rl=re.search(r'\*\*Length ruling:\*\*.*',open(f'{B}/{slug}/Outline.md').read()).group(0)
        p=f'''# This pass: apply the ruled cuts at the outline

Mark ruled on this story's length (Mark, 2026-11-27, "Batch 12: the first two briefs approved, and the long stories' lengths": "approve as recommended", then "yes, both". This batch only). The outline's own line:

{rl}

Your outline, source sheet, `Cuts_Named.md` and the measuring draft `{slug}.measure.txt` are in this folder. Apply to `Outline.md` exactly the cuts the ruling names, as `Cuts_Named.md` lists them: move each item to the card or Leave out, as marked, add it to Cut first in order, and remove it from the beats, quotes, glosses and credits that carried it. Apply no cut the ruling does not name; a cut named elsewhere (an earlier recheck, a fix pass) that waited on this ruling and that the ruling does not name stays out, and you list it. Where `Cuts_Named.md` notes a conflict inside the outline (a line that keeps what a Cut first item drops), settle it to match the cut and say how. Never cut the record's force, an explanation Part 1 requires (Explain it), or the scene that carries the story's craft. Keep the approved heart. Update the outline's Length line to the ruled length.

Write `Fixes_Length.md`: each cut applied, where it went, the words it saves by the measuring draft, the expected draft length, and every line you changed besides the moves. Do not edit the measuring draft, commit, or edit outside your folder. Reply in under 120 words: the expected draft length, anything that touches the heart, and any cut you could not apply.

For reference, your role as researcher follows.

'''
        open(f'{B}/{slug}/Length_Apply_Prompt.filled.md','w').write(h+'\n\n---\n\n'+p+'\n'+body(slug,name)); print('ok apply',slug)
