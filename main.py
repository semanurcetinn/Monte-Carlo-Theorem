import numpy as np
import matplotlib.pyplot as plt

n = 1000
x = np.linspace(0, 450, n)
y = np.cos(np.deg2rad(x))

x_random = np.random.rand(n) * 450
y_random = np.random.rand(n)

under_filter = y_random < np.cos(np.deg2rad(x_random))

# plt.scatter(x_random, y_random, color="black")
plt.scatter(x_random[under_filter], y_random[under_filter], color="red")
plt.plot(x, y, "r-", linewidth=3)
plt.show()
print(len(x_random[under_filter]) * 450 / n)
