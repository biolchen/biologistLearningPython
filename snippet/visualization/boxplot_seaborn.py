##
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from matplotlib.lines import Line2D

plt.clf()
fig = plt.figure(1)

ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

sns.set_style("whitegrid")
tips = sns.load_dataset("tips")

sns.boxplot(x="day",
            y="total_bill",
            hue="smoker",
            data=tips,
            palette="Set1",
            ax=ax1)
sns.boxplot(x="day",
            y="total_bill",
            hue="smoker",
            data=tips,
            palette="Set1",
            ax=ax2)

for i, artist in enumerate(ax2.artists):
    print(i, artist, artist.get_facecolor())
    col = artist.get_facecolor()
    artist.set_edgecolor(col)
    artist.set_facecolor('None')

    for j in range(i * 6, i * 6 + 6):
        print(j)
        line = ax2.lines[j]
        print(line)
        line.set_color(col)
        line.set_mfc('m')
        line.set_mec('r')

for legpatch in ax2.get_legend().get_patches():
    col = legpatch.get_facecolor()
    legpatch.set_edgecolor(col)
    legpatch.set_facecolor('None')

plt.show()
##

plt.clf()
fig = plt.figure(2)

ax = fig.add_subplot(111)
x = np.array([1, 1, 3, 3, 1])
y = np.array([1, 3, 3, 1, 1])
line1 = Line2D(x, y)
line2 = Line2D(x + 3, y)
ax.add_line(line1)
ax.add_line(line2)
ax.set_xlim(-10, 20)
ax.set_ylim(-10, 20)
plt.show()
##
