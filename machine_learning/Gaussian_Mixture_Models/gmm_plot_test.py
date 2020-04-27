import matplotlib.pyplot as plt
import numpy as np
from matplotlib import patches
from sklearn.datasets.samples_generator import make_blobs
from sklearn.mixture import GaussianMixture

##
X, y_true = make_blobs(n_samples=400,
                       centers=4,
                       cluster_std=0.60,
                       random_state=0)

rng = np.random.RandomState(13)
X1 = np.dot(X, rng.randn(2, 2))

plt.cla()
fig = plt.figure(1)
ax = fig.add_subplot(111)
gmm = GaussianMixture(n_components=4, covariance_type='full', random_state=42)
labels = gmm.fit(X1).predict(X1)

U, s, Vt = np.linalg.svd(gmm.covariances_[0])

ax.axis('equal')

angle = np.degrees(np.arctan2(U[1, 0], U[0, 0]))
width, height = np.sqrt(s) * 5

print("""
        U:{}
        s:{}
        Vt:{}
        angle: {}
        w: {}
        h: {}
        gmm_means: {}
        """.format(U, s, Vt, angle, width, height, gmm.means_))

ax.scatter(X1[:, 0], X1[:, 1], s=40, zorder=2)

e2 = patches.Arc(gmm.means_[0],
                 width=width,
                 height=height,
                 angle=angle,
                 linewidth=2,
                 fill=False,
                 zorder=2)

ax.add_patch(e2)

plt.show()
##
