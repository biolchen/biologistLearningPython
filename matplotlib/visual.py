import matplotlib.pyplot as plt
import numpy as np
plt.plot([1, 2, 3, 4])  # If you provide a single list or array to the plot() command, matplotlib assumes it is a sequence of y values
plt.ylabel('some numbers')
plt.show()
##
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()
##
fig = plt.figure()
ax1 = fig.add_axes([0.1, 0.45, 0.8, 0.5])
# rect[left, bottom, width, height]
ax2 = fig.add_axes([0.1, 0.1, 0.8, 0.2])
plt.show()
##
plt.rc('font', family='serif')
plt.rc('xtick', labelsize='x-small')
plt.rc('ytick', labelsize='x-small')
fig = plt.figure(figsize=(4, 3))
ax = fig.add_subplot(111)
plt.plot([1, 2, 3, 4])
ax.set_xlabel('The x values')
ax.set_ylabel('The y values')
plt.show()
##
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (5,3)
fig = plt.figure()
fig.add_subplot(241)
fig.add_subplot(242)
ax = fig.add_subplot(223)
ax.set_title("subplots")
fig.add_axes([0.77,.3,.2,.6])
ax2 =fig.add_axes([0.67,.5,.2,.3])
fig.add_axes([0.6,.1,.35,.3])
ax2.set_title("random axes")
plt.tight_layout()
plt.show()
##
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
df1 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
fig = plt.figure(2)
ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,3,4)
ax5 = fig.add_subplot(2,3,5)
ax6 = fig.add_subplot(2,3,6)
ax1.bar(range(5),range(5))
ax2.plot(range(4))
ax3.plot(range(3))
ax4.plot(range(3))
ax5.plot(range(4))
ax6.plot(range(4))
plt.show()
##
plt.clf()
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
ax4=df2.plot.bar()
plt.savefig('/Users/liangchen/Downloads/test1.png')
##
import random
import matplotlib.pyplot as plt
from matplotlib import style

style.use('ggplot')
fig = plt.figure()

def create_plots():
    xs = []
    ys = []

    for i in range(10):
        x = i
        y = random.randrange(10)

        xs.append(x)
        ys.append(y)
    return xs, ys

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(212)
plt.savefig('/Users/liangchen/Downloads/test1.png')
##
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
plt.figure()
gs = gridspec.GridSpec(1, 2)
ax1=plt.subplot(gs[0,0])
ax2=plt.subplot(gs[0,1])
df.plot.box(ax=ax1)
df.plot.box(ax=ax2)
plt.savefig('/Users/liangchen/Downloads/test1.png')
##
import numpy as np
import scipy.stats as stats
x1 = np.array([-7, -5, 1, 4, 5.])
kde = stats.gaussian_kde(x1)
xs = np.linspace(-10, 10, num=50)
y1 = kde(xs)
kde.set_bandwidth(bw_method='silverman')
y2 = kde(xs)
kde.set_bandwidth(bw_method=kde.factor / 3.)
y3 = kde(xs)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.plot(x1, np.ones(x1.shape) / (4. * x1.size), 'bo', label='Data points (rescaled)')
ax.plot(xs, y1, label='Scott (default)')
ax.plot(xs, y2, label='Silverman')
ax.plot(xs, y3, label='Const (1/3 * Silverman)')
ax.legend()
plt.savefig('/Users/liangchen/Downloads/test1.png')
##
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r,extent=[xmin, xmax, ymin, ymax])
ax.plot(m1, m2, 'k.', markersize=2)
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
plt.savefig('/Users/liangchen/Downloads/test1.png')
##
from scipy import stats
def measure(n):
    m1 = np.random.normal(size=n)
    m2 = np.random.normal(scale=0.5, size=n)
    return m1+m2, m1-m2

m1, m2 = measure(2000)
xmin = m1.min()
xmax = m1.max()
ymin = m2.min()
ymax = m2.max()

X, Y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([X.ravel(), Y.ravel()])
values = np.vstack([m1, m2])
kernel = stats.gaussian_kde(values)
Z = np.reshape(kernel(positions).T, X.shape)

import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.imshow(np.rot90(Z), cmap=plt.cm.gist_earth_r,
          extent=[xmin, xmax, ymin, ymax])
ax.plot(m1, m2, 'k.', markersize=2)
ax.set_xlim([xmin, xmax])
ax.set_ylim([ymin, ymax])
plt.savefig('/Users/liangchen/Downloads/test1.png')
##

