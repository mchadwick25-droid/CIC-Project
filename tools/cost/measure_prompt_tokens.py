import re, json, os
from pathlib import Path
ROOT = Path("/tmp/claude-0/-home-user-CIC-Project/611f54e7-88e8-5b58-8233-278c31460890/scratchpad/tree/cic")
DEPLOY = ROOT/"deploy"
SECTION_END = ("\n---", "\n## ", "\n\n**")
QM = ("## Quick Meaning", "**Quick Meaning:**", "**Quick Meaning**")
KS = ("## Key Sources", "**Key Sources:**", "**Key Sources**")
TRAIL = ("## Final Assembly Instruction","## Related-Terms Reciprocity Note")

src = (ROOT/"runtime/app/prompts/representative_prompts.py").read_text()
HOW = re.search(r'_HOW_YOU_ENGAGE\s*=\s*"""(.*?)"""', src, re.S).group(1)

def find(body, markers):
    for m in markers:
        i = body.find(m)
        if i != -1: return i, m
    return -1, None

def truncate_at(body, markers):
    i,_ = find(body, markers)
    if i != -1: return body[:i]
    for m in TRAIL:
        j = body.find(m)
        if j != -1: return body[:j]
    return body

def excise(body, markers):
    i,m = find(body, markers)
    if i == -1: return body
    cs = i+len(m)
    ends=[body.find(e,cs) for e in SECTION_END]
    ends=[e for e in ends if e!=-1]
    end = min(ends) if ends else len(body)
    return body[:i]+body[end:]

def after_frontmatter(text):
    # indexer: content after the front-matter block
    if text.lstrip().startswith("## Retrieval Front-Matter"):
        i = text.find("\n---")
        if i!=-1: return text[i+4:]
    parts = text.split("---")
    return "---".join(parts[2:]) if len(parts)>2 else text

WORLDS = {
 "pahc":("pahc_Representative_Permanent_Prompt_Chloe.txt","pahc_World_Capsule_Core.md"),
 "syriac":("syr_Representative_Permanent_Prompt_Yausep.txt","syr_World_Capsule_Core.md"),
 "desert":("desert_Representative_Permanent_Prompt_Papnoute.txt","desert_World_Capsule_Core.md"),
 "hieronymian":("hal_Representative_Permanent_Prompt_Albina.txt","hal_World_Capsule_Core.md"),
 "alexandria":("alex_Representative_Permanent_Prompt_Theon.txt","alex_World_Capsule_Core.md"),
 "imperial_juridical":("ijc_Representative_Permanent_Prompt_Marius.txt","ijc_World_Capsule_Core.md"),
}
out={}
for w,(pp,wc) in WORLDS.items():
    static = ("# Who You Are\n"+(DEPLOY/w/pp).read_text()+"\n\n"
              "# The World You Inhabit\n"+(DEPLOY/w/wc).read_text()+"\n\n"
              "# How You Engage\n"+HOW)
    lex=[]
    for f in sorted((DEPLOY/w/"lexicon_chunks").glob("*.md")):
        b = after_frontmatter(f.read_text())
        b = truncate_at(b, KS); b = excise(b, QM)
        lex.append(len(b))
    st=[]
    for f in sorted((DEPLOY/w/"story_chunks").glob("*.md")):
        b = after_frontmatter(f.read_text())
        b = truncate_at(b, KS)
        st.append(len(b))
    lex.sort(); st.sort()
    med_lex = lex[len(lex)//2]; med_st = st[len(st)//2]
    out[w]={"static_chars":len(static),
            "lex_n":len(lex),"lex_median":med_lex,"lex_mean":sum(lex)//len(lex),
            "st_n":len(st),"st_median":med_st,"st_mean":sum(st)//len(st),
            "dynamic_chars_typ": 3*med_lex + 2*med_st + 1600}
    Path(f"/tmp/pay_{w}_static.txt").write_text(static)
print(json.dumps(out, indent=1))
