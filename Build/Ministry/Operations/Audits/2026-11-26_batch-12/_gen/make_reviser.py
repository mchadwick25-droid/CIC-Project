"""make_reviser.py <slug> ["<extra header line>"] -> Reviser_Prompt.filled.md"""
import re, sys
B='Build/Ministry/Operations/Audits/2026-11-26_batch-12'
LONG={'josephus':725,'cyprian-of-carthage':965,'origen':950,'eusebius-of-caesarea':850,'era-1':730}
slug=sys.argv[1]; extra=sys.argv[2] if len(sys.argv)>2 else ''
h=open(f'{B}/{slug}/Reviewer_Prompt.filled.md').read().split('\n---\n')[0]
h='\n'.join(l for l in h.split('\n') if not l.startswith('- **Length (Mark') and not l.startswith('- **The live text') and not l.startswith('- **Variety'))
name=re.search(r'\*\*Story:\*\* (.*?) \(census',h).group(1) if slug!='era-1' else 'Era 1, The Early Church Era'
ceil=LONG.get(slug,675)
ln=f'- **Length:** the ceiling is {ceil} words' + (' (the long stories\' length ruling, Mark, 2026-11-27).' if slug in LONG else ' (Mark, 2026-11-27, "Batch 12: lengths measured by the draft").') + ' If the review\'s fixes take it past the ceiling, say so with the count; do not cut what the review did not name.\n'
hw='- **Heart wording (this batch):** a review finding that changes wording the approved essence or heart holds is applied as the review gives it, and goes to Mark as a report with the brief. Fixes the review needed at the outline are already in `Outline.md` (`Fixes_Review.md`, `Recheck_Review.md`, `Recheck_Review_Applied.md` where present): use the outline as it now stands.\n'
role=open('Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/reviser.md').read().replace('{NAME}',name).replace('{FOLDER}',f'{B}/{slug}').replace('{SLUG}',slug)
open(f'{B}/{slug}/Reviser_Prompt.filled.md','w').write(h.rstrip('\n')+'\n\n'+hw+ln+(extra+'\n' if extra else '')+'\n---\n\n'+role); print('ok',slug,ceil)
