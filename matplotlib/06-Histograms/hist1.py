import random

import matplotlib.pyplot as plt
import numpy as np

x = [random.gauss(3, 1) for _ in range(400)]
y = [random.gauss(4, 2) for _ in range(400)]

bins = np.linspace(-10, 10, 100)

plt.hist(x, bins, alpha=0.5, label='x')
plt.hist(y, bins, alpha=0.5, label='y')
plt.legend(loc='upper right')
plt.show()

##

plt.style.use('seaborn-deep')

x = np.random.normal(1, 2, 5000)
y = np.random.normal(-1, 3, 2000)
bins = np.linspace(-10, 10, 30)

plt.hist([x, y], bins, label=['x', 'y'])
plt.legend(loc='upper right')
plt.show()

##
