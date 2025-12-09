import numpy as np
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices : list, edges : set):
        self.vertices = vertices
        self.num_of_vertices = len(self.vertices)
        
        self.edges = edges

        self.vtoi = {v : i for i, v in enumerate(self.vertices)}

        self.adjacency_matrix = self._create_adjacency_matrix()
        self.adjacency_list = self._create_adjacency_list()

    def _create_adjacency_matrix(self):
        adjacency_matrix = np.zeros((self.num_of_vertices, self.num_of_vertices), dtype=int)

        for u, v in self.edges:
            adjacency_matrix[self.vtoi[u]][self.vtoi[v]] = 1

        return adjacency_matrix

    def _create_adjacency_list(self):
        adjacency_list = {}

        for i in self.vertices:
            adjacency_list[i] = []

        for j in self.edges:
            if j[0] in adjacency_list.keys():
                adjacency_list[j[0]] += [j[1]]

        return adjacency_list
    
    def plot(self, show_labels=True):
        n = self.num_of_vertices
        
        if n > 50:
            show_labels = False

        theta = np.linspace(0, 2*np.pi, n, endpoint=False)
        r = 1.2
        x = r * np.cos(theta)
        y = r * np.sin(theta)

        fig, ax = plt.subplots(figsize=(8,8))

        for u, v in self.edges:
            i, j = self.vtoi[u], self.vtoi[v]
            ax.annotate(
                "",
                xy=(x[j], y[j]),
                xytext=(x[i], y[i]),
                arrowprops=dict(arrowstyle="->", lw=.7, alpha=0.4)
            )

        ax.scatter(x, y, s=20 if n>60 else 80, c='dodgerblue', alpha=0.7)

        if show_labels:
            for v, i in self.vtoi.items():
                ax.text(x[i], y[i], str(v), ha='center', va='center', fontsize=6)

        ax.axis('off')
        plt.tight_layout()
        plt.show()

    def __repr__(self):
        return f"Graph(\nadjacency_matrix=\n{self.adjacency_matrix}\nadjacency_list={self.adjacency_list})"
