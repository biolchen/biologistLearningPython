##
from matplotlib import pyplot as plt

time = [0, 1, 2, 3, 4]
revenue = [200, 400, 650, 800, 850]
costs = [150, 500, 550, 550, 560]

plt.plot(revenue, time, color='purple',linestyle='--')

plt.plot(costs, time, color='#82edc9',marker='s')
plt.show()
##
