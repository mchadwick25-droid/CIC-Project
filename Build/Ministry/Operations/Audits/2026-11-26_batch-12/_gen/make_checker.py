import re, sys
B='Build/Ministry/Operations/Audits/2026-11-26_batch-12'
role=open('Build/Ministry/Features/Church-Family-Tree/Brief-Kit/roles/checker.md').read()
HRUL='Mark, 2026-11-27, "Batch 12: hearts and lengths approved": "approve as recommended". This batch only.'
for slug in sys.argv[1:]:
    rp=open(f'{B}/{slug}/Researcher_Prompt.filled.md').read()
    header=rp.split('\n---\n')[0]
    name=re.search(r'\*\*Story:\*\* (.*?) \(census',header).group(1) if slug!='era-1' else 'Era 1, The Early Church Era'
    out=open(f'{B}/{slug}/Outline.md').read()
    sec=out.split('## Approved heart and length',1)[1].strip()
    header=re.sub(r'- \*\*Heart and length:\*\*.*', f'- **Heart and length ({HRUL}):** the heart as `Outline.md` gives it, and the section "Approved heart and length" at its end: {sec}', header)
    header=header.replace('# Batch header','# Batch header',1)
    if slug=='era-1':
        header=header.replace('Do not read the live person stories; their outlines replace them.','Do not read the live person stories; their outlines replace them. The era kit\'s own source rule (broad historical scholarship allowed, no historian named, Inferential-Thin out) governs check 1.')
    body=role.replace('{NAME}',name).replace('{FOLDER}',f'{B}/{slug}')
    open(f'{B}/{slug}/Checker_Prompt.filled.md','w').write(header+'\n\n---\n\n'+body)
    print('ok',slug)
