import numpy as np
import matplotlib.pyplot as plt

def Ixy_numeric(a, b, n, m=20001):
    x = np.linspace(0.0, a, m)
    y = b * (x / a) ** n
    f = 0.5 * x * (y ** 2)
    return np.trapz(f, x)

a = 1.0
b = 1.0

ns = np.arange(1.0, 10.0 + 0.5, 0.5)
Ixy = np.array([Ixy_numeric(a, b, n) for n in ns])

print("n\tI_xy\t\tI_xy/(a^2 b^2)")
for n, val in zip(ns, Ixy):
    print(f"{n:>3.1f}\t{val:.10f}\t{val/(a*a*b*b):.10f}")

rect = (a*a*b*b)/4.0
print("\nI_xy rectangle (a x b) =", rect)
print("I_xy at n=10 =", Ixy[-1])
print("ratio I_xy(n=10) / I_xy_rect =", Ixy[-1] / rect)

plt.plot(ns, Ixy, marker='o', linewidth=1)
plt.xlabel('n')
plt.ylabel('I_xy')
plt.grid(True, alpha=0.3)
plt.show()
