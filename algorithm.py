class TarjansSccAlgorithm:
    def __init__(self):
        self.index = 0
        self.S = []
        self.V = None
        self.E = None
        self.on_stack = set()
        self.lowlink = {}
        self.indices = {}
        self.sccs = []
    
    def find_scc_adjacency_list(self, adj_list):
        self.E = self._get_edges_adj_list(adj_list)
        self.V = adj_list.keys()
        
        for v in self.V:
            if v not in self.indices:
                self._strongconnect(v)
                
        result = self.sccs 
        self.__init__()
        return result
    
    def find_scc_adjacency_matrix(self, adj_matrix):
        self.E = self._get_edges_adj_matrix(adj_matrix)
        self.V = list(range(adj_matrix.shape[0]))

        for v in self.V:
            if v not in self.indices:
                self._strongconnect(v)
                
        result = self.sccs 
        self.__init__()
        return result

    def _get_edges_adj_list(self, adj_list):
        edges = set()

        for k, v in adj_list.items():
            for i in v:
                edges.add((k, i))

        return edges
    
    def _get_edges_adj_matrix(self, adj_matrix):
        edges = set()

        for i, row in enumerate(adj_matrix):
            for j, element in enumerate(row):
                if element == 1:
                    edges.add((i, j))

        return edges

    def _strongconnect(self, v):
        self.indices[v] = self.index
        self.lowlink[v] = self.index
        self.index += 1
        self.S.append(v)
        self.on_stack.add(v)

        for src, w in self.E:
            if src == v:
                if w not in self.indices:
                    self._strongconnect(w)
                    self.lowlink[v] = min(self.lowlink[v], self.lowlink[w])
                elif w in self.on_stack:
                    self.lowlink[v] = min(self.lowlink[v], self.indices[w])
        
        if self.lowlink[v] == self.indices[v]:
            scc = set()

            while True:
                w = self.S.pop()
                self.on_stack.remove(w)
                scc.add(w)

                if w == v:
                    break

            self.sccs.append(scc)