import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df1 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
fig = plt.figure()
ax1 = fig.add_subplot(2, 3, 1)
ax2 = fig.add_subplot(2, 3, 2)
ax3 = fig.add_subplot(2, 3, 3)
ax4 = fig.add_subplot(2, 3, 4)
ax5 = fig.add_subplot(2, 3, 5)
ax6 = fig.add_subplot(2, 3, 6)
ax1.bar(range(5), range(5))
ax2.plot(range(4))
ax3.plot(range(3))
ax4.plot(range(3))
ax5.plot(range(4))
ax6.plot(range(4))
plt.show()
