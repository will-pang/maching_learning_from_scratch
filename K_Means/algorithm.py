import math
from initialization import init_centroids
from metrics import calculate_euclidean_distance

class KMeans:
    def __init__(self, data, K, IC, max_iter, tol):
        self.data = data
        self.K = K
        self.IC = IC
        self.max_iter = max_iter
        self.tol = tol
        self.counter = 0
        self.centroids = self.init_centroids()
    
    def init_centroids(self):
        get_initial_centroids = init_centroids(self.IC)
        return get_initial_centroids(self.data, self.K)

    def classify_points(self):
        self.classifications = {}

        for i in range(self.K):
            self.classifications[i] = []

        for i in range(len(self.data)):
            min_dist = math.inf
            sort_into_centroid_id = 0
            
            for centroid_id in list(self.centroids.keys()):
                dist = calculate_euclidean_distance(self.data[i], self.centroids[centroid_id])
                if dist < min_dist:
                    min_dist = dist
                    sort_into_centroid_id = centroid_id
            self.classifications[sort_into_centroid_id].append(self.data[i])

        return self.classifications
    
    def update_centroids(self):
        self.prev_centroids = dict(self.centroids)
        for centroid_id in list(self.centroids.keys()):
            self.centroids[centroid_id] = [sum(x)/len(x) for x in zip(*self.classifications[centroid_id])]
        
    def run_algorithm(self):
        while self.max_iter > self.counter:
            self.classifications = self.classify_points()
            self.update_centroids()

            optimized = True

            for centroid_id in self.centroids:
                original_centroid = self.prev_centroids[centroid_id]
                current_centroid = self.centroids[centroid_id]
            
                if calculate_euclidean_distance(original_centroid, current_centroid) > self.tol:
                    optimized = False
                
            if optimized:
                    break
            
            self.counter +=1

    def print(self):
        print(f"Optimized in {self.counter} iterations\n")
        for centroid_id, points in self.classifications.items():
            print(f"Centroid: {centroid_id}")
            for point in points:
                print(point)

    def write_to_csv(self, output_name):
        with open(output_name, 'w') as file:
            # Column header
            file.write("cluster,x,y")
            file.write('\n')
            # Iterate over all clusters
            for id, points in self.classifications.items():
                # Iterate over each coordinate(s) belonging to the cluster
                for point in points:
                    file.write(str(id))
                    file.write(',')
                    # Iterate over value of a point (e.g., in 2D, that would be x and y)
                    for i, item in enumerate(point):
                        file.write(str(item))
                        if i < len(point)-1:
                            file.write(',')
                    file.write('\n')














