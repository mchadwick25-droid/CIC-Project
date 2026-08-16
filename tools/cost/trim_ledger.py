S,SO=2.0,10.0; SS,SSO=3.0,15.0; H,HO=1.0,5.0
HOURS=1000; TURNS=12; TPM=HOURS*TURNS          # turns / month
STATIC=17837; DYN=4343; CONT=300; OUT=330
ADJ=0.00523; SMALL=0.0169                       # true classifier costs /turn
SAFETY=0.0029                                   # relational_safety + frame_breaker
SHADOW=0.0015
def main(pin,pout,static,dyn,sess):
    return (static*pin*0.1/1e6 + static*pin*2.0/1e6/(TURNS*sess)
            + (dyn+CONT)*pin/1e6 + OUT*pout/1e6)
def show(rows):
    print(f"{'lever':52}{'$/turn':>9}{'$/hour':>8}{'$/mo':>8}{'$/yr':>9}")
    for n,d in rows:
        print(f"{n:52}{d:9.5f}{d*TURNS:8.3f}{d*TPM:8.0f}{d*TPM*12:9,.0f}")
st,dy,sess,cl = STATIC,DYN,1,ADJ+SMALL
base = main(S,SO,st,dy,sess)+cl
print(f"BASELINE (true, isolated sessions): ${base:.4f}/turn  ${base*TURNS:.2f}/hr  "
      f"${base*TPM:,.0f}/mo  ${base*TPM*12:,.0f}/yr\n")
rows=[]
def step(name, **kw):
    global st,dy,sess,cl
    before = main(S,SO,st,dy,sess)+cl
    st=kw.get('st',st); dy=kw.get('dy',dy); sess=kw.get('sess',sess); cl=kw.get('cl',cl)
    rows.append((name, before-(main(S,SO,st,dy,sess)+cl)))
step("A  strip builder apparatus from chunks (-40%)", dy=DYN-1721)
step("B  gate safety classifiers behind lexical filter", cl=cl-SAFETY*0.92)
step("C  over-settling adjudicator 78% -> 30% fire rate", cl=cl-ADJ*0.615)
step("D  retire the two shadow-mode checks", cl=cl-SHADOW)
step("E  trim _HOW_YOU_ENGAGE by 40%", st=STATIC-2882)
step("F  pool cache writes (20 sessions / window)", sess=20)
show(rows)
son = main(S,SO,st,dy,sess)+cl
hai = main(H,HO,st,dy,sess)+cl
print(f"\n{'':52}{'$/turn':>9}{'$/hour':>8}{'$/mo':>8}{'$/yr':>9}")
for n,v in [("SONNET 5, all of A-F, intro pricing",son),
            ("SONNET 5, all of A-F, from 2026-09-01", main(SS,SSO,st,dy,sess)+cl),
            ("HAIKU 4.5, all of A-F (any date)",hai)]:
    print(f"{n:52}{v:9.5f}{v*TURNS:8.3f}{v*TPM:8.0f}{v*TPM*12:9,.0f}")
print(f"\nAnnual saving, A-F only, no voice change: ${(base-son)*TPM*12:,.0f}")
print(f"Additional annual saving if voice -> Haiku:  ${(son-hai)*TPM*12:,.0f}")
