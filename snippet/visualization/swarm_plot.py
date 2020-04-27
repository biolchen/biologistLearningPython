##
import os
import sys

import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
tips = sns.load_dataset("tips")
plt.figure(1)
ax = sns.swarmplot(x=tips["total_bill"], y=tips['day'])
plt.figure(2)
ax = sns.swarmplot(x=tips["total_bill"], y=tips['sex'])
plt.show()
##
tips.head()
os.getcwd()
sys.path
print('ddd')
##
plt.figure(3)
ax = sns.violinplot(x="day", y="total_bill", data=tips, inner=None)
ax = sns.swarmplot(x="day",
                   y="total_bill",
                   data=tips,
                   color="white",
                   edgecolor="gray")
plt.show()
##
plt.figure(4)
sns.catplot(x="sex",
            y="total_bill",
            hue="smoker",
            col="time",
            data=tips,
            kind="swarm",
            height=4,
            aspect=.7)
plt.show()
##
