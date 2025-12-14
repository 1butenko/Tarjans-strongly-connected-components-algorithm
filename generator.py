import numpy as np

class Generator:
    def __init__(self, n : int, delta : int):
       self.num_of_vertices = n
       self.vertices = set(range(self.num_of_vertices))
       self.edges = self._calculate_edges(n, delta)
       self.p = delta / 100
    
    def _calculate_edges(self, n : int, delta : int) -> int:
        return round(delta / 100 * (n * (n - 1)))
    
    def generate_random_graph(self):
        graph_set = set()
        
        for i in self.vertices:            
            for j in self.vertices:
                if i != j:
                    if np.random.random() < self.p:
                        graph_set.add((i, j))
        
        return graph_set