class DSU:
    def __init__(self, n):
        #start with n connected compoents, one for each vertex
        self.components = n
        #each vertex is it's own parent
        self.parent = list(range(n + 1))
        #size of each connected compoents
        self.size = [1 for _ in range(n + 1)]
    
    #finds parent of node
    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    #combine connected compoents of two nodes
    def union(self, u , v):
        pu = self.find(u)
        pv = self.find(v)

        #if u and v in same conncected compoent nothing to do
        if pu == pv:
            return False
        
        self.components -= 1
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.size[pu] += self.size[pv]
        self.parent[pv] = pu
        return True
    
    
        


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #failure to be a tree:
        #1)multiple connected compoents
        #2)cycles
        graph = DSU(n)
        for u, v in edges:
            ok = graph.union(u, v)
            if not ok:
                return False
        return graph.components == 1 
        
        

        