S_IN_I, S_OUT_I = 2.0, 10.0      # Sonnet 5 intro (to 2026-08-31)
S_IN_S, S_OUT_S = 3.0, 15.0      # Sonnet 5 standard (from 2026-09-01)
H_IN, H_OUT = 1.0, 5.0           # Haiku 4.5
STATIC, DYN, CONT, OUT = 17837, 4343, 300, 250
TURNS = 12
def main_cost(pin, pout, cache, write_amort=True, sessions_sharing=1):
    if cache:
        rd = STATIC*pin*0.1/1e6
        wr = (STATIC*pin*2.0/1e6)/(TURNS*sessions_sharing) if write_amort else 0
        unc = (DYN+CONT)*pin/1e6
        return rd+wr+unc+OUT*pout/1e6
    return (STATIC+DYN+CONT)*pin/1e6 + OUT*pout/1e6
MEAS_TOTAL=0.091; MEAS_MAIN=MEAS_TOTAL*0.687
ADJ=MEAS_TOTAL*0.127; OTHER=MEAS_TOTAL*0.186
rows=[]
rows.append(("S0  measured today (no cache benefit)", MEAS_TOTAL))
m1=main_cost(S_IN_I,S_OUT_I,True); c1=ADJ*0.5+OTHER
rows.append(("S1  fix caching, keep Sonnet (intro)", m1+c1))
m2=main_cost(H_IN,H_OUT,True)
rows.append(("S2  S1 + Haiku 4.5 voice", m2+c1))
c3=ADJ*0.5*0.4+OTHER*0.55
rows.append(("S3  S2 + classifier surgery", m2+c3))
rows.append(("S4  S1 + classifier surgery (Sonnet kept)", m1+c3))
m5=main_cost(S_IN_S,S_OUT_S,True)
rows.append(("S5  S4 at Sonnet STANDARD pricing (Sep 1)", m5+c3))
m6=main_cost(H_IN,H_OUT,True,sessions_sharing=20)
rows.append(("S6  S3 at scale (20 concurrent sessions/world)", m6+c3))
print(f"{'scenario':46} {'$/turn':>9} {'$/hour':>9}")
for n,v in rows: print(f"{n:46} {v:9.4f} {v*TURNS:9.2f}")
print()
print("no-cache main_response (intro/standard): %.4f / %.4f  vs measured %.4f"
      % (main_cost(S_IN_I,S_OUT_I,False), main_cost(S_IN_S,S_OUT_S,False), MEAS_MAIN))
print("cache-working main_response (intro):     %.4f" % m1)
print("delete ALL classifiers, keep S0 main:    $%.2f/hr" % ((MEAS_MAIN)*TURNS))
