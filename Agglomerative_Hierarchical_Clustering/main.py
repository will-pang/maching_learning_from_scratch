import argparse
from clustering_algorithm import AgglomerativeHierarchicalClustering


def read_data(file_name, seperator=','):
    data = []
    with open(file_name) as input_file:
        # Skip the header
        next(input_file)
        for row in input_file.readlines():
            data.append([float(item) for item in row.split(seperator)])
    return data


ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required=True, help="path to input dataset")
ap.add_argument("-k", "--clusters", required=True, help="number of clusters")
ap.add_argument("-m", "--measure", required=True, help="distance measure. 0-single_link, 1-complete_link, 2- wards_distance, 3-average_link")
ap.add_argument("-s", "--save", required=False, help="saves to csv. Try 'output.csv'")
args = vars(ap.parse_args())

dataset = read_data(args["dataset"], seperator=',')

N = len(dataset)
K = int(args["clusters"])
M = int(args["measure"])

agg_hierarchical_clustering = AgglomerativeHierarchicalClustering(dataset, K, M)
agg_hierarchical_clustering.run_algorithm()
agg_hierarchical_clustering.print()

if args["save"]:
    agg_hierarchical_clustering.write_to_csv(output_name = args["save"])
