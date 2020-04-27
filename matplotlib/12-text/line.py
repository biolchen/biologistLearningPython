##
import matplotlib.pyplot as plt
import matplotlib.lines as lines

fig = plt.figure()

ax = fig.add_subplot(111)

ax.set_xlim(left=0, right=10)
ax.set_ylim(bottom=0, top=10)

l1 = lines.Line2D([0, 1], [4, 5], figure=fig, color='r')
l2 = lines.Line2D([0, 8], [6, 2], figure=fig, color='k')
ax.add_line(l1)
ax.hlines(y=4, xmin=4, xmax=5, linewidth=4, color='b')
ax.add_line(l2)
ax.text(2,6,'text here')
ax.annotate('annotate', xy=(6,1), xytext=(8,4), arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate("", xy=(0.5, 0.5), xytext=(2, 2),arrowprops=dict(arrowstyle="->"))
plt.show()
##
