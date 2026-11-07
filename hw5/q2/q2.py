import numpy as np
import matplotlib.pyplot as plt

r = 1.0

L1 = r
L2 = np.pi * r
Ltot = L1 + L2

theta_deg = np.arange(0.0, 90.0 + 0.5, 0.5)
theta_rad = np.deg2rad(theta_deg)

x_bar = []

for th_deg, th in zip(theta_deg, theta_rad):
    x1 = -0.5 * r * np.cos(th)
    x2 = 2.0 * r / np.pi - r * np.cos(th)
    x_tot = (x1 * L1 + x2 * L2) / Ltot
    x_bar.append(x_tot)
    print(f"theta = {th_deg:5.1f} deg  "
          f"x1 = {x1: .4f}  x2 = {x2: .4f}  x_bar = {x_tot: .4f}")

x_bar = np.array(x_bar)

idx = np.argmin(np.abs(x_bar))
theta_eq_deg = theta_deg[idx]
x_eq = x_bar[idx]

print("\nEquilibrium angle (x_bar ≈ 0):")
print(f"theta_eq = {theta_eq_deg:.2f} deg,  x_bar = {x_eq:.6f}")

plt.plot(theta_deg, x_bar, label="x̄(θ)")
plt.axhline(0.0, color="k", linewidth=0.8)
plt.axvline(theta_eq_deg, color="r", linestyle="--",
            label=f"θ ≈ {theta_eq_deg:.1f}°")
plt.xlabel("θ (deg)")
plt.ylabel("x̄")
plt.grid(True)
plt.legend()
plt.show()
