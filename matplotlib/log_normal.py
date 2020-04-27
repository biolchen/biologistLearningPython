import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

d1 = np.random.lognormal(size=(370, 1), mean=10, sigma=2)
d2 = np.random.lognormal(size=(370, 1), mean=10, sigma=1.5)
d3 = np.random.lognormal(size=(370, 1), mean=10, sigma=1)
d4 = np.random.lognormal(size=(370, 1), mean=10, sigma=0.5)

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)
ax4 = fig.add_subplot(224)

sns.distplot(d1, ax=ax1).set_title(r"d1")
sns.distplot(d2, ax=ax2).set_title(r"d2")
sns.distplot(d3, ax=ax3).set_title(r"d3")
sns.distplot(d4, ax=ax4).set_title(r"d4")
plt.show()