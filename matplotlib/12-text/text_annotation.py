##
import matplotlib.pyplot as plt
import numpy.random

fig = plt.figure(1, figsize=(5, 5))
fig.clf()
ax = fig.add_subplot(111)
ax.set_aspect(1)

x1 = -1 + numpy.random.randn(100)
y1 = -1 + numpy.random.randn(100)
x2 = 1. + numpy.random.randn(100)
y2 = 1. + numpy.random.randn(100)

ax.scatter(x1, y1, color="r")
ax.scatter(x2, y2, color="g")

bbox_props = dict(boxstyle="round", fc="w", ec="0.5", alpha=0.9)
ax.text(-2, -2, "Sample A", ha="center", va="center", size=20, bbox=bbox_props)
ax.text(2, 2, "Sample B", ha="center", va="center", size=20, bbox=bbox_props)

bbox_props = dict(boxstyle="rarrow", fc=(0.8, 0.9, 0.9), ec="b", lw=2)
t = ax.text(0,
            0,
            "Direction",
            ha="center",
            va="center",
            rotation=45,
            size=15,
            bbox=bbox_props)

bb = t.get_bbox_patch()
bb.set_boxstyle("rarrow", pad=0.6)
ax.set_xlim(-4, 4)
ax.set_ylim(-4, 4)
plt.show()
##
s = 'matplotlib'
fig = plt.figure(1, figsize=(5, 5))
ax1 = fig.add_subplot(221)
ax1.text(0.5,
         0.5,
         s,
         fontsize=14,
         horizontalalignment='center',
         verticalalignment='center',
         transform=ax1.transAxes)
ax2 = fig.add_subplot(222)
ax2.text(0.5,
         0.5,
         s,
         fontsize=14,
         size=10,
         rotation=30,
         ha="center",
         va="center",
         bbox=dict(boxstyle="round", ec=(1., 0.5, 0.5), fc=(1., 0.8, 0.8)),
         transform=ax2.transAxes)
ax3 = fig.add_subplot(223)
ax3.text(0.5, 0.5, s, bbox=dict(facecolor='red', alpha=0.5))
plt.show()
##
