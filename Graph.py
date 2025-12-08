import numpy as np
import matplotlib.pyplot as plt

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
    
    def plot(self):
        theta = np.linspace(0, 2*np.pi, self.num_of_verticies, endpoint=False)
        x = np.cos(theta)
        y = np.sin(theta)

        fig, ax = plt.subplots()

        for u, v in self.graph_set:
            i, j = self.vtoi[u], self.vtoi[v]

            ax.annotate(
                "", 
                xy=(x[j], y[j]), 
                xytext=(x[i], y[i]), 
                arrowprops=dict(arrowstyle="->", lw=1.5)
            )

        ax.scatter(x, y, s=250, c='skyblue')

        for v,i in self.vtoi.items():
            ax.text(x[i], y[i], str(v), ha='center', va='center')

        ax.axis('equal')
        plt.show()


    def __repr__(self):
        return f"Graph(\nincidence_matrix=\n{self.incidence_matrix}\nadjacency_list={self.adjacency_list})"