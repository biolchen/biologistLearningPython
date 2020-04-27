import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import namedtuple
n_groups = 5
means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)
means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)
plt.figure(num=3, figsize=(7, 4.5),)
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.35
opacity = 1
error_config = {'#999999': '0.3'}
rects1 = ax.bar(index, means_men, bar_width,
                alpha=opacity, color='#0F73B0',
                yerr=std_men, error_kw=error_config,
                label='Men')
rects2 = ax.bar(index + bar_width, means_women, bar_width,
                alpha=opacity, color='#D45E1A',
                yerr=std_women, error_kw=error_config,
                label='Women')
ax.set_xlabel('Group', fontsize=14)
ax.set_ylabel('Scores', fontsize=14)
ax.set_xticks(index + bar_width / 2)
ax.set_xticklabels(('amoa', 'amya', 'mcra', 'mcraA', 'mcraD'), fontsize=14)
plt.yticks(fontsize=14)
ax.grid(linewidth=0.25, linestyle='--')
ax.legend(fontsize=14)
# plt.savefig("plt4_menwomen_1.pdf",bbox_inches="tight")
plt.show()