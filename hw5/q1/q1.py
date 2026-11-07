import numpy as np
import matplotlib.pyplot as plt

a = 1.0
h = 1.0

x = np.linspace(0.0, a, 1001)
n_values = np.arange(0.2, 5.0 + 1e-9, 0.1)

x_path = []
y_path = []

for n in n_values:
    y = h - (h / (a ** n)) * (x ** n)
    A = np.trapz(y, x)
    x_bar = np.trapz(x * y, x) / A
    y_bar = np.trapz(0.5 * y ** 2, x) / A
    x_path.append(x_bar)
    y_path.append(y_bar)
    print(f"n = {n:.1f}, x_bar = {x_bar:.4f}, y_bar = {y_bar:.4f}")

plt.figure()

for n in [0.5, 1.0, 4.0]:
    y = h - (h / (a ** n)) * (x ** n)
    plt.plot(x, y, label=f"n = {n:g}")

plt.plot(x_path, y_path, "k-", linewidth=2, label="centroid path")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.axis("equal")
plt.show()
