import numpy as np
from matplotlib import pyplot as plt

t = np.linspace(0, 8*np.pi, 1000)

r1 = np.random.rand()
r2 = np.random.rand()

x = np.cos(r1 * t)
y = np.sin(r2 * t)

x = np.append(x, x[0])
y = np.append(y, y[0])

plt.plot(x,y)
plt.show()
