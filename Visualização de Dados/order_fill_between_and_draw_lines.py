import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure(figsize=(4, 4))

r = 1
xc = 5
yc = 5
angs = np.arange(0, 2 * np.pi, 0.0001)
x = r * np.cos(angs) + xc
circle = r * np.sin(angs) + yc
downCircle = r * np.cos(angs) + yc

plt.plot(x, circle)
plt.plot(x + 0.2, circle - 0.3)

plt.fill_between(x, circle, downCircle, alpha=1, zorder=100)

plt.plot(1.5 * x + 0.25 * circle, 0.4 + 0.5 * x + 0.75 * circle)

plt.plot(1.5 * x + 0.01 * circle, 0.01 * x + 0.45 * circle)
plt.plot(1.5 * x + 0.01 * circle, 0.4 + 0.01 * x + 0.45 * circle)

plt.fill_between(1.5 * x + 0.01 * circle, 0.4 + 0.01 * x + 0.45 * circle, 0.01 * x + 0.45 * circle)

plt.fill_between(1.5 * x + 0.01 * circle, 0.4 + 0.01 * x + 0.45 * circle, 0.01 * x + 0.45 * downCircle, alpha=1,
                 zorder=100)
plt.fill_between([min(1.5 * x + 0.01 * circle), max(1.5 * x + 0.01 * circle)],
                 [np.mean(0.4 + 0.01 * x + 0.45 * circle), np.mean(0.4 + 0.01 * x + 0.45 * circle)],
                 [np.mean(0.01 * x + 0.45 * circle), np.mean(0.01 * x + 0.45 * circle)])

# Ajusta as arestas e fica tudo bonito


# plt.axhline(6)
# plt.axhline(4)
# plt.axvline(6)
# plt.axvline(4)
# plt.fill_between(x, topCircle, downCircle)

plt.xlim([0, 15])
plt.ylim([0, 15])

plt.show()
