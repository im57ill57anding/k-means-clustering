import math

import numpy as np
import matplotlib.pyplot as plt


def distance(a: list, b: list) -> float:
    return math.sqrt(
        ((a[0]-b[0])**2)
        +
        ((a[1]-b[1])**2)
    )


def recalculate_clusters(points: list, centroids: list, k: int) -> dict:
    clusters: dict = {}

    for i in range(k):
        clusters[i] = []

    for data in points:
        euc_dist: list = []
        for j in range(k):
            euc_dist.append(distance(data, centroids[j]))

        clusters[euc_dist.index(min(euc_dist))].append(data)

    return clusters


def recalculate_centroids(centroids, clusters, k) -> list:
    for i in range(k):
        centroids[i] = np.average(clusters[i], axis=0)
    return centroids


def k_means_clustering(points: list, k: int):
    centroids: list = []
    for index in range(k):
        centroids.append(points[index])

    clusters: dict = {}
    for iteration in range(1000):
        clusters: dict = recalculate_clusters(points, centroids, k)
        centroids: list = recalculate_centroids(centroids, clusters, k)

    for index in range(k):
        print(f'cluster #{index}:', end=' ')
        for to in clusters[index]:
            print(to, end=' ')
        print('\n')
