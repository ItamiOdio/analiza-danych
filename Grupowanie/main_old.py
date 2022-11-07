import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

from sklearn.datasets import make_blobs
from sklearn.datasets import make_classification

n = 1000
centra = [(-6, -6), (0, 0), (6, 6), (9, 9)]


def c1():
    X, y = make_blobs(n_samples=n, n_features=2, centers=centra, cluster_std=1, random_state=0)

    plt.scatter(X[:, 0], X[:, 1], c=y)
    plt.show()

    km = KMeans(n_clusters=4, random_state=0)
    km.fit(X)
    plt.scatter(X[:, 0], X[:, 1], c=km.labels_)
    plt.scatter(km.cluster_centers_[:,0], km.cluster_centers_[:,1], c='white')
    plt.show()


def c2():
    X, y = make_classification(n_samples=n, n_features=2, n_clusters_per_class=1, n_redundant=0, random_state=4)
    #plt.scatter(X[:, 0], X[:, 1], c=y)
    #plt.show()

    km = KMeans(n_clusters=2, random_state=0).fit(X)

    plt.scatter(X[:, 0], X[:, 1], c=km.labels_)
    plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], c='red')
    plt.show()


def c3():
    most = plt.imread('most.jpg', format='jpg')
    plt.imshow(most)
    plt.axis('off')
    plt.show()
    most.shape
    #most.reshape(427*640, 3)
    most_flat = most.reshape(-1, 3)

   # km = KMeans(n_clusters=4, random_state=0).fit(most_flat)
    km = KMeans(n_clusters=5, random_state=0).fit(most_flat)
    np.unique(km.labels_)
    print(km.cluster_centers_)

    most_flat4 = most_flat.copy()
    for i in np.unique(km.labels_):
        most_flat4[km.labels_ == i, :] = km.cluster_centers_[i]

    most4 = most_flat4.reshape(most.shape)
    #plt.imshow(most)
    plt.axis('off')


c3()

