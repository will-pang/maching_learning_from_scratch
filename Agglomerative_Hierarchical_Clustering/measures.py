import math


def distance(p, q):
    return math.sqrt(sum([(pi - qi)**2 for pi, qi in zip(p, q)]))

def squared_euclidean_distance(p, q):
    return sum([(pi - qi) ** 2 for pi, qi in zip(p, q)])

def single_link(ci, cj):
    return min([distance(vi, vj) for vi in ci for vj in cj])


def complete_link(ci, cj):
    return max([distance(vi, vj) for vi in ci for vj in cj])


def average_link(ci, cj):
    distances = [distance(vi, vj) for vi in ci for vj in cj]
    return sum(distances) / len(distances)

def within_cluster_variance(cluster):
    centroid = [sum(coord) / len(coord) for coord in zip(*cluster)]
    return sum(squared_euclidean_distance(point, centroid) for point in cluster)


def wards_distance(ci, cj):
    return math.sqrt(2 * (within_cluster_variance(ci + cj) - within_cluster_variance(ci) - within_cluster_variance(cj)))


def get_distance_measure(M):
    if M == 0:
        return single_link
    elif M == 1:
        return complete_link
    elif M == 2:
        return wards_distance
    else:
        return average_link
