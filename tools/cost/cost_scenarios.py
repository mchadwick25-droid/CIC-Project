# Sonnet 5 = $2/$10 per MTok, flat (verified live 2026-08-16, no expiry).
S_I,SO_I=2.0,10.0; H,HO=1.0,5.0
STATIC=17837; DYN=4343; CONT=300; OUT=330; TURNS=12
def main(pin,pout,dyn=DYN,sess=1):
    return (STATIC*pin*0.1/1e6                      # cache read
          + STATIC*pin*2.0/1e6/(TURNS*sess)         # 1h write, amortised
          + (dyn+CONT)*pin/1e6                      # uncached
          + OUT*pout/1e6)
def naive(pin,pout):
    tot=STATIC+DYN+CONT
    return (tot*pin/1e6 + STATIC*pin*0.1/1e6 + (STATIC/TURNS)*pin*2.0/1e6 + OUT*pout/1e6)
ADJ_T=0.00523; SMALL=0.0169                          # true adjudication, measured smalls
CL_NOW=ADJ_T+SMALL; CL_CUT=ADJ_T*(30/78)+0.011
print("RECONCILIATION")
print("  naive main_response model      $%.4f/turn   (reported was $0.0625)"%naive(S_I,SO_I))
print("  true  main_response            $%.4f/turn"%main(S_I,SO_I))
print("  overstatement                  %.2fx\n"%(naive(S_I,SO_I)/main(S_I,SO_I)))
rows=[
 ("R0  reported (double-counted)",                      0.0910),
 ("T0  TRUE today, no changes",                         main(S_I,SO_I)+CL_NOW),
 ("T1  + classifier surgery",                           main(S_I,SO_I)+CL_CUT),
 ("T2  T1 at pilot scale (20 sess/world)",              main(S_I,SO_I,sess=20)+CL_CUT),
 ("T3  T2 + retrieval halved",                          main(S_I,SO_I,dyn=DYN/2,sess=20)+CL_CUT),
 ("T4  T1 + Haiku voice",                               main(H,HO)+CL_CUT),
 ("T5  T4 at pilot scale",                              main(H,HO,sess=20)+CL_CUT),
]
print(f"{'scenario':44}{'$/turn':>9}{'$/hour':>9}  target")
for n,v in rows:
    print(f"{n:44}{v:9.4f}{v*TURNS:9.2f}  {'MEETS' if v*TURNS<=0.30 else ''}")
