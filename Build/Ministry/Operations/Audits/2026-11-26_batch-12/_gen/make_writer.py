import re, sys
B='Build/Ministry/Operations/Audits/2026-11-26_batch-12'
role=open('Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/writer.md').read()
for slug in sys.argv[1:]:
    cp=open(f'{B}/{slug}/Checker_Prompt.filled.md').read()
    header=cp.split('\n---\n')[0]
    name=re.search(r'\*\*Story:\*\* (.*?) \(census',header).group(1) if slug!='era-1' else 'Era 1, The Early Church Era'
    header=re.sub(r'  - A new source sheet and outline from the Library\..*?\n', f'  - The live wording is not kept (slate decision 2). Do not open `{slug}.brief.live.txt` in your folder, any other version of the live story, or the census `longDescription` for this entry.\n', header)
    LONG={'josephus':725,'cyprian-of-carthage':965,'origen':950,'eusebius-of-caesarea':850,'era-1':730}
    if slug in LONG:
        header+=f'\n- **Length (Mark, 2026-11-27, "Batch 12: the first two briefs approved, and the long stories\' lengths": "approve as recommended", then "yes, both". This batch only.):** about {LONG[slug]} words, the outline\'s Length ruling line; the ruled cuts are already in its Cut first list. {LONG[slug]} is the ceiling for this story: if your draft runs past it with every Cut first item out, stop and say so, with the count.\n'
    else:
        header+='\n- **Length (Mark, 2026-11-27, "Batch 12: lengths measured by the draft": "approve as recommended". This batch only.):** the draft is the measure, and 675 words is the ceiling. If your draft runs past the outline\'s approved length but stays at or under 675 with every Cut first item out, finish it and report the count; stop only past 675.\n'
    body=role.replace('{NAME}',name).replace('{FOLDER}',f'{B}/{slug}').replace('{SLUG}',slug)
    open(f'{B}/{slug}/Writer_Prompt.filled.md','w').write(header+'\n\n---\n\n'+body)
    print('ok',slug, 'live-bar' in header or 'Do not open' in header)
