L = 6.0
w = 3.0
a = 2.0

W = w * L

print("Question 1 (reactions from equilibrium):")
print(f"Given: L={L} m, w={w} kN/m, a={a} m")
print(f"UDL resultant: W = w*L = {W:.4f} kN acting at x = L/2 = {L/2:.4f} m")
print(f"RB(P) = {w*L/2:.4f} + ({a/L:.6f})*P   [kN]")
print(f"RA(P) = {w*L/2:.4f} + ({1 - a/L:.6f})*P   [kN]")
print()

def reactions(P):
    RB = (W * (L / 2.0) + P * a) / L
    RA = W + P - RB
    return RA, RB

print(f"{'P (kN)':>6}  {'RA (kN)':>10}  {'RB (kN)':>10}  {'Fy err':>10}  {'MA err':>10}")
print("-" * 60)

for P in range(1, 11):
    RA, RB = reactions(P)
    fy_err = (RA + RB) - (W + P)
    ma_err = (RB * L) - (W * (L/2.0) + P * a)
    print(f"{P:6.0f}  {RA:10.4f}  {RB:10.4f}  {fy_err:10.2e}  {ma_err:10.2e}")
