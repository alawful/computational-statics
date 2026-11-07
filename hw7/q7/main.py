import numpy as np
import matplotlib.pyplot as plt

a = 1.0

Ix = (np.pi / 8.0) * a**4
Iy = (np.pi / 2.0) * a**4
Ixy = 0.5 * a**4

print("Ix =", Ix)
print("Iy =", Iy)
print("Ixy =", Ixy)

step = 0.5
theta_deg = np.arange(-90.0, 90.0 + step, step)
th = np.deg2rad(theta_deg)

c2 = np.cos(2.0 * th)
s2 = np.sin(2.0 * th)

Ix_p = 0.5 * (Ix + Iy) + 0.5 * (Ix - Iy) * c2 - Ixy * s2
Iy_p = 0.5 * (Ix + Iy) - 0.5 * (Ix - Iy) * c2 + Ixy * s2
Ixy_p = 0.5 * (Ix - Iy) * s2 + Ixy * c2

fig, ax = plt.subplots(2, 1, figsize=(7, 7), sharex=True)
ax[0].plot(theta_deg, Ix_p)
ax[0].set_ylabel("I_x'")
ax[0].grid(True, alpha=0.3)

ax[1].plot(theta_deg, Ixy_p)
ax[1].set_ylabel("I_x'y'")
ax[1].set_xlabel("theta (deg)")
ax[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig("q7.png", dpi=200)
plt.show()

def wrap_pm90(x):
    return ((x + 90.0) % 180.0) - 90.0

theta_p = 0.5 * np.arctan2(2.0 * Ixy, (Ix - Iy))
theta_p_deg = np.rad2deg(theta_p)
t1 = wrap_pm90(theta_p_deg)
t2 = wrap_pm90(theta_p_deg + 90.0)

print("principal angle in [-90,90] (deg) =", t1)
print("other principal angle in [-90,90] (deg) =", t2)

zeros = []
for i in range(len(theta_deg) - 1):
    y1 = Ixy_p[i]
    y2 = Ixy_p[i + 1]
    if y1 == 0.0:
        zeros.append(theta_deg[i])
    elif y1 * y2 < 0.0:
        t = theta_deg[i] + (0.0 - y1) * (theta_deg[i + 1] - theta_deg[i]) / (y2 - y1)
        zeros.append(t)

if len(zeros) == 0:
    i0 = np.argmin(np.abs(Ixy_p))
    print("no sign-change zero found; closest:", theta_deg[i0], "deg, I_x'y' =", Ixy_p[i0])
else:
    print("I_x'y' = 0 occurs near (deg):", ", ".join([f"{z:.4f}" for z in zeros]))

imax = int(np.argmax(Ix_p))
imin = int(np.argmin(Ix_p))

print("Ix' max =", Ix_p[imax], "at theta =", theta_deg[imax], "deg")
print("Ix' min =", Ix_p[imin], "at theta =", theta_deg[imin], "deg")
print("Iy' max =", Iy_p[imin], "at theta =", theta_deg[imin], "deg")
print("Iy' min =", Iy_p[imax], "at theta =", theta_deg[imax], "deg")
