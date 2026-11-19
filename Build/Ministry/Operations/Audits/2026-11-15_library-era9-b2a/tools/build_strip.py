import re
GP = re.compile(r"This is a digital copy of a book|Dit is een digitale kopie|Ceci est une copie num|Dies ist ein digitales Exemplar|Esta es una copia digital|Esta . uma c.pia digital|Questa . la copia digitale|Informazioni su questo libro|About this book|.ber dieses Buch|Acerca de este libro|. propos de ce livre", re.I)
WM = re.compile(r"\W*(Digiti[sz]ed by \S{3,12}|Hosted by Google)\W*", re.I)
def strip_host(L):
    L, d1 = strip_pre(L)
    n = len(L); L = [x for x in L if not WM.fullmatch(re.sub(r"\s+", " ", x).strip())]
    d2 = f"{n-len(L)} lines that hold only the scanner's page mark ('Digitized by ...' or 'Hosted by Google')" if n != len(L) else None
    d = "; and ".join(x for x in (d1, d2) if x)
    return L, (d or None)
def strip_pre(L):
    """Remove Google's preamble: from the first preamble line in the first 60 lines to the last books.google.com line in the first 160. Returns (lines, description or None)."""
    N = [re.sub(r"\s+", " ", x) for x in L[:200]]
    a = next((k for k in range(min(60, len(N))) if GP.search(N[k])), None)
    if a is None: return L, None
    zs = [k for k in range(a, min(160, len(N))) if re.search(r"books ?\. ?[gqGQ]oo[gq]le ?\. ?com", N[k], re.I)]
    if not zs: return L, None
    z = zs[-1]
    while a > 0 and (not L[a-1].strip() or re.fullmatch(r"\W*(Google|Go.?gle)\W*", L[a-1].strip())): a -= 1
    while z + 1 < len(L) and not L[z+1].strip(): z += 1
    return L[:a] + L[z+1:], f"Google's preamble about the scan (host OCR lines {a+1}-{z+1}, {z+1-a} lines, from '{N[next(k for k in range(a, z+1) if N[k].strip())].strip()[:50]}' to the last line naming books.google.com)"
