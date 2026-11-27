import re, sys
B='Build/Ministry/Operations/Audits/2026-11-26_batch-12'
role=open('Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/reviewer.md').read()
LONG={'josephus':725,'cyprian-of-carthage':965,'origen':950,'eusebius-of-caesarea':850,'era-1':730}
for slug in sys.argv[1:]:
    wp=open(f'{B}/{slug}/Writer_Prompt.filled.md').read()
    header=wp.split('\n---\n')[0]
    header=re.sub(r'\n- \*\*Length \(Mark, 2026-11-27, "Batch 12: lengths measured by the draft".*?\n','\n',header)
    header='\n'.join(l for l in header.split('\n') if 'stop and say so' not in l and 'stop only past 675' not in l)
    header=re.sub(r'\n- \*\*Redraft \(.*?\n','\n',header)
    name=re.search(r'\*\*Story:\*\* (.*?) \(census',header).group(1) if slug!='era-1' else 'Era 1, The Early Church Era'
    n=len(open(f'{B}/{slug}/{slug}.brief.txt').read().split())
    if slug in LONG:
        ln=(f'- **Length (Mark, 2026-11-27, "Batch 12: the first two briefs approved, and the long stories\' lengths": "approve as recommended", then "yes, both". This batch only.):** about {LONG[slug]} words. This draft runs {n}: judge it at its length, and flag only what the heart does not need.\n')
    else:
        m=re.search(r'\*\*(\d+) words\*\*',header); a=int(m.group(1))
        ln=(f'- **Length (Mark, 2026-11-27, "Batch 12: lengths measured by the draft": "approve as recommended". This batch only.):** the draft is the measure; a draft at 675 or under goes on to review as written. This draft runs {n} against the approved {a}: judge it at its length, and flag only what the heart does not need.\n')
    live=(f'- **The live text (this batch):** an earlier hand may have seen parts of the live story in the census by accident. The second trust reader also opens `{slug}.brief.live.txt` in this folder once, after the read, and lists any sentence of the new brief that echoes its wording (an echo is a finding only where the outline does not hold the wording itself).\n')
    body=role.replace('{NAME}',name).replace('{FOLDER}',f'{B}/{slug}').replace('{SLUG}',slug)
    open(f'{B}/{slug}/Reviewer_Prompt.filled.md','w').write(header.rstrip('\n')+'\n\n'+ln+live+"- **Variety across the batch:** `Build/Ministry/Operations/Audits/2026-11-26_batch-12/Variety_Report_Wave3.txt` counts the moves that repeat across the briefs written so far. It is a report for the reviewer and Mark: nothing is recast because of it.\n"+'\n\n---\n\n'+body)
    print('ok',slug,n)
