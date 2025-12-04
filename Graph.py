import numpy as np

class Graph:
    def __init__(self, graph_set : set):
        self.graph_set = graph_set

        self.vertices = sorted({e for edge in graph_set for e in edge})
        self.num_of_verticies = len(self.vertices)

        self.vtoi = {v : i for i, v in enumerate(self.vertices)}

        self.incidence_matrix = self._create_incidence_matrix()
        self.adjacency_list = self._create_adjacency_list()

    def _create_incidence_matrix(self):
        incidence_matrix = np.zeros((self.num_of_verticies, self.num_of_verticies), dtype=int)

        for u, v in self.graph_set:
            incidence_matrix[self.vtoi[u]][self.vtoi[v]] = 1

        return incidence_matrix

    def _create_adjacency_list(self):
        adjacency_list = {}

        for i in self.graph_set:
            if i[0] in adjacency_list.keys():
                adjacency_list[i[0]] += [i[1]]
            else:
                adjacency_list[i[0]] = [i[1]]

        return adjacency_list

    def __repr__(self):
        return f"Graph(\nincidence_matrix=\n{self.incidence_matrix}\nadjacency_list={self.adjacency_list})"
    
graph = Graph({(1, 0), (1,2), (1, 3), (3, 1), (3, 2), (5,7)})

print(graph)