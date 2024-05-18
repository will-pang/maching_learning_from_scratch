# K Means Clustering From Scratch
Implementation of KMeans clustering algorithm from scratch, without the use of advance libraries (such as Numpy, Pandas, Scikit-learn)

For a dynamic visualization of clustering in action, check out my [Observable Notebook](https://observablehq.com/@williampangbest1/k-means-clustering)

## Overview
The K-Means clustering algorithm groups data points to K (user-defined) clusters. The algorithm is optimized if the centroids have converged, or if the maximum number of iterations have been reached, whichever comes first.

Briefly, the procedure is to:
- Randomly pick K number of centroids
- Iterate through each point and assign each point to the nearest centroid
- Repeat until the centroids stop moving, or we've reached the maximum number of iterations

## Sample Usage
`python main.py -d data.csv -k 3 -ic 0 -m 1000 -t 0.0001 -s output.csv`

To get help, try:
`python main.py --help`

### References
[1] Inspiration for this project was based on the work of Ola Pietka's implementation of the [Agglomerative Hiearching Clustering from Scratch](https://github.com/OlaPietka/Agglomerative-Hierarchical-Clustering-from-scratch).<br>
[2] Implementation of the algorithm from scratch mostly follows [this](https://pythonprogramming.net/k-means-from-scratch-machine-learning-tutorial/) tutorial, but changes were made to improve readability and (in my opinion) better software engineering practices through the use of OOP.
