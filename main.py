import time
from graph import Graph
from generator import Generator
from algorithm import TarjansSccAlgorithm

generator = Generator(n=200, delta=10)
g = Graph(generator.vertices, generator.generate_random_graph())
algo = TarjansSccAlgorithm()

start_time_matrix = time.time()
algo.find_scc_adjacency_matrix(g.adjacency_matrix)
end_time_matrix = time.time()

execution_time = end_time_matrix - start_time_matrix
print(f"Matrix execution time: {execution_time:.4f} seconds")


start_time_list = time.time()
algo.find_scc_adjacency_list(g.adjacency_list)
end_time_list = time.time()

execution_time_list = end_time_list - start_time_list
print(f"List execution time: {execution_time_list:.4f} seconds")