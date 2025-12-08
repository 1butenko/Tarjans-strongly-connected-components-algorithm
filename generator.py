import numpy as np
from graph import Graph

class Generator:
    def __init__(self, n : int, delta : int):
       self.nodes = n
       self.edges = self._calculate_edges(n, delta)
       self.p = delta / 100
    
    def _calculate_edges(self, n : int, delta : int) -> int:
        return round(delta / 100 * (n * (n - 1))) # formula of edges in graph mutliplied by delta
    
    def generate_random_graph(self):
        graph_set = set()
        
        for i in range(self.nodes):            
            for j in range(self.nodes):
                if i != j:
                    if np.random.random() < self.p:
                        graph_set.add((i, j))
        
        return graph_set
    

generator = Generator(n = 100, delta=2)
g = Graph(generator.generate_random_graph())
g.plot()