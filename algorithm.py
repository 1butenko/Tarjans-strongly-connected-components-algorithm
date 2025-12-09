class TarjansSccAlgorithm:
    def __init__(self):
        self.index = 0
        self.S = []
        self.graph = None
        self.on_stack = set()
        self.lowlink = {}
        self.indices = {}
        self.sccs = []
    
    def find_scc_adjacency_list(self, adj_list):
        self.graph = adj_list
        self._reset()
        
        for v in adj_list.keys():
            if v not in self.indices:
                self._strongconnect_list(v)
                
        return self.sccs
    
    def find_scc_adjacency_matrix(self, adj_matrix):
        self.graph = adj_matrix
        self._reset()

        n = len(adj_matrix)

        for v in range(n):
            if v not in self.indices:
                self._strongconnect_matrix(v)
                
        return self.sccs
    
    def _reset(self):
        self.index = 0
        self.S = []
        self.on_stack = set()
        self.lowlink = {}
        self.indices = {}
        self.sccs = []

    def _strongconnect_list(self, v):
        self.indices[v] = self.index
        self.lowlink[v] = self.index
        self.index += 1
        self.S.append(v)
        self.on_stack.add(v)

        for w in self.graph.get(v, []):
            if w not in self.indices:
                self._strongconnect_list(w)
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

    def _strongconnect_matrix(self, v):
        self.indices[v] = self.index
        self.lowlink[v] = self.index
        self.index += 1
        self.S.append(v)
        self.on_stack.add(v)

        for w, has_edge in enumerate(self.graph[v]):
            if has_edge:
                if w not in self.indices:
                    self._strongconnect_matrix(w)
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