import argparse
from algorithm import KMeans

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
ap.add_argument("-k", "--centroids", required=True, help="number of centroids")
ap.add_argument("-ic", "--initialization_cluster", required=True, help="initialization strategy. 0 = Random")
ap.add_argument("-m", "--maximium_iteration", required=True, help="maximum number of iterations. Try 1000.")
ap.add_argument("-t", "--tolerance", required=True, help="tolerance for convergence. Try 0.001.")
ap.add_argument("-s", "--save", required=False, help="saves to csv. Try 'output.csv'")
args = vars(ap.parse_args())

dataset = read_data(args["dataset"], seperator=',')
K = int(args["centroids"])
IC = int(args["initialization_cluster"])
max_iter = int(args["maximium_iteration"])
tol = float(args["tolerance"])

k_means = KMeans(dataset, K, IC, max_iter, tol)
k_means.run_algorithm()
k_means.print()

if args["save"]:
    k_means.write_to_csv(output_name = args["save"])