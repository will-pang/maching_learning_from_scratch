import random 

def random_initialization(data, K):
    indicies = list(range(len(data)))
    random_indicies = random.sample(indicies, K)
    return {cluster_id: data[index] for cluster_id, index in enumerate(random_indicies)}

def init_centroids(IC):
    if IC == 0:
        return random_initialization

    # Include future methods for initialization here, which could speed up convergence
    