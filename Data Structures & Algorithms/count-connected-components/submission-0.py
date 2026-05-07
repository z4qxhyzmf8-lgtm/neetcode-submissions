class DSU:
    def __init__(self, n):
        self.components = n
        self.parent = list(range(n))
        self.size = [1 for _ in range(n)]

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node] 
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)

        if pu == pv:
            return
        
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        
        self.components -= 1
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = DSU(n)
        for i, j in edges:
            graph.union(i, j)
        return graph.components
        