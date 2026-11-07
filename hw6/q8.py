import numpy as np
import matplotlib.pyplot as plt

L = 6.0
w0 = 2.0

N = 2001
x = np.linspace(0.0, L, N)
dx = x[1] - x[0]

w = w0 * (1.0 + x / L)

W = np.trapz(w, x)
x_bar = np.trapz(x * w, x) / W

RB = W * x_bar / L
RA = W - RB

area_w = np.zeros_like(x)
area_w[1:] = np.cumsum(0.5 * (w[:-1] + w[1:]) * dx)
V = RA - area_w

area_V = np.zeros_like(x)
area_V[1:] = np.cumsum(0.5 * (V[:-1] + V[1:]) * dx)
M = area_V

print("Q1) Support reactions")
print(f"W = {W:.6f} kN, x_bar = {x_bar:.6f} m")
print(f"RA = {RA:.6f} kN, RB = {RB:.6f} kN")
print()

print("Q2) Numerical V(x) and M(x) at sample points")
print(f"{'x(m)':>6}  {'w(kN/m)':>10}  {'V(kN)':>10}  {'M(kN*m)':>12}")
print("-" * 44)

sample_x = np.arange(0.0, L + 1e-9, 0.5)
idx = np.round(sample_x / dx).astype(int)
for i in idx:
    print(f"{x[i]:6.2f}  {w[i]:10.4f}  {V[i]:10.4f}  {M[i]:12.4f}")
print()

i_max = int(np.argmax(M))
x_max = x[i_max]
M_max = M[i_max]

print("Q4) Maximum bending moment (numerical)")
print(f"M_max = {M_max:.6f} kN*m at x = {x_max:.6f} m")
print()

Fy_err = (RA + RB) - W
MA_err = (RB * L) - (W * x_bar)
print("Equilibrium check")
print(f"SumFy error = {Fy_err:.3e}")
print(f"SumM_A error = {MA_err:.3e}")
print()

data = np.column_stack([x, w, V, M])
np.savetxt("beam_results.csv", data, delimiter=",",
           header="x_m,w_kN_per_m,V_kN,M_kN_m", comments="")

plt.figure(figsize=(9, 4))
plt.plot(x, V, linewidth=2)
plt.axhline(0, color="k", linewidth=1)
plt.xlabel("x (m)")
plt.ylabel("V(x) (kN)")
plt.title("Shear Force Diagram (SFD)")
plt.grid(True)

plt.figure(figsize=(9, 4))
plt.plot(x, M, linewidth=2)
plt.axhline(0, color="k", linewidth=1)
plt.xlabel("x (m)")
plt.ylabel("M(x) (kN·m)")
plt.title("Bending Moment Diagram (BMD)")
plt.grid(True)
plt.scatter([x_max], [M_max], zorder=3)
plt.text(x_max, M_max, f"  max at x={x_max:.3f} m", va="bottom")

plt.show()
