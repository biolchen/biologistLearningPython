##
import numpy as np
import matplotlib.pyplot as plt

from matplotlib.colors import ListedColormap
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_moons, make_circles, make_classification
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.mixture import GaussianMixture as GMM
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.discriminant_analysis import QuadraticDiscriminantAnalysis as QDA

from sklearn.cluster import AgglomerativeClustering 
from sklearn.cluster import KMeans 
##


# data generation

covar = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

dat_threedee = np.vstack((np.random.multivariate_normal([1, 1, 1], covar, 250), 
                          np.random.multivariate_normal([1, 5, 1], covar, 250),
                          np.random.multivariate_normal([3, 2, 1], covar, 250)))

dat_twodee = np.vstack((np.random.multivariate_normal([0, 0], [[10, 0], [0, 1]], 100),
                        np.random.multivariate_normal([0, 5], [[1, 2], [2, 1]], 100),
                        np.random.multivariate_normal([5, 5], [[5, 3], [3, 2]], 100)))

dat_twodee_simple = np.vstack((np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]], 100),
                               np.random.multivariate_normal([0, 5], [[1, 0], [0, 1]], 100),
                               np.random.multivariate_normal([5, 5], [[2, 0], [0, 2]], 100)))

dat_twodee_headache = np.vstack((np.random.multivariate_normal([0, 0], [[1, 0], [0, 1]], 100),
                                 np.random.multivariate_normal([0, 1], [[1, 0], [0, 1]], 100),
                                 np.random.multivariate_normal([1, 1], [[2, 0], [0, 2]], 100)))

comps = 2
gm_mod = GMM(n_components = comps)

gm_mod.fit(dat_twodee)
y_hat = gm_mod.predict(dat_twodee)

print("The mean(s) estimated with this {} component GMM: \n {}".format(comps, gm_mod.means_))
print("\n\nThe covariances [SEE THE DOCS] estimated with this {} component GMM: \n {}".format(comps, gm_mod.covariances_))
plt.cla()
cm_bright = ListedColormap(['#FF0000', '#0000FF'])
fig = plt.figure(1)
plt.subplot(1, 1, 1)
plt.scatter(dat_twodee[:, 0], dat_twodee[:, 1], c=y_hat, cmap=cm_bright)
plt.title("Mysterious Rabbit Data")
plt.show()
##

'''

## GMM vs Kmeans vs Agglomerative Clustering

The goal of this question is to directly compare GMMs to other clustering techniques, and get an intuitive sense of the differences.

Links to docs for kmeans and agglomerative clustering:
http://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html#sklearn.cluster.KMeans
http://scikit-learn.org/stable/modules/generated/sklearn.cluster.AgglomerativeClustering.html#sklearn.cluster.AgglomerativeClustering

1. Compare the results you see with GMM, KMeans, and AgglomerativeClustering (use all the three linkage types). Some demos are provided below. Try different numbers of clusters for all these algorithms. What differences do you see between the methods? Which one would you recommend using? Don't worry about trying to numerically score the models here, just use plots and your visual judgement.

2. Try this again with the data: dat_twodee_simple and dat_twodee_headache; do you see any differences?
'''

##
def proc(dat):
    km = KMeans(n_clusters=2)
    km.fit(dat)

    gm_mod = GMM(n_components = 2)
    gm_mod.fit(dat)

    ag = AgglomerativeClustering(n_clusters = 2, linkage = "complete")

    cm_bright = ListedColormap(['#FF0000', '#0000FF', '#FFFFFF','#00FF00'])

    fig = plt.figure(2, figsize=(12, 4))

    plt.subplot(1, 3, 1)
    plt.scatter(dat[:, 0], dat[:, 1], c=km.predict(dat), cmap=cm_bright)
    plt.title('KMeans') 

    plt.subplot(1, 3, 2)
    plt.scatter(dat[:, 0], dat[:, 1], c=gm_mod.predict(dat), cmap=cm_bright)
    plt.title('GMM') 

    plt.subplot(1, 3, 3)
    plt.scatter(dat[:, 0], dat[:, 1], c=ag.fit_predict(dat), cmap=cm_bright)
    plt.title('Agglomerative(complete)') 
    plt.show()
    
proc(dat_twodee)

##
