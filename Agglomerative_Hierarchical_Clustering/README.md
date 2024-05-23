# Agglomerative Hierarchical Clustering From Scratch
Implementation of Agglomerative Hierarchical Clustering algorithm from scratch, 
without the use of advance libraries (such as Numpy, Pandas, Scikit-learn)

Briefly, the procedure is to:
- Initially, treat each point as a unique cluster
- Take the two nearest clusters and join to form one cluster
- Repeat until we've reached desired number of clusters

## Sample Usage
`python main.py -d data.csv -k 4 -m 0 -s output_single_linkage.csv` <br>
`python main.py -d data.csv -k 4 -m 2 -s output_wards_distance.csv`

To get help, try:
`python main.py --help`

### References
[1] Implementation for this project was based on the work of Ola Pietka's 
[Agglomerative Hiearching Clustering from Scratch](https://github.com/OlaPietka/Agglomerative-Hierarchical-Clustering-from-scratch). 
The changes I've made were to add a method that allows for [Ward Linkage](https://en.wikipedia.org/wiki/Ward%27s_method) 
, as well as the ability to save the data as a csv. <br>
