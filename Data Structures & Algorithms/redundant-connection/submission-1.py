class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        degree = [0 for _ in range(n + 1)]
        adj = [[] for _ in range(n + 1)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
            degree[i] += 1
            degree[j] += 1
        q = deque()
        cycle = [1 for _ in range(n + 1)]
        for i in range(1, n + 1):
            if degree[i] == 1:
                q.append(i)
                cycle[i] = 0
        
        while q:
            node = q.popleft()
            for nb in adj[node]:
                degree[nb] -= 1
                if degree[nb] == 1:
                    q.append(nb)
                    cycle[nb] = 0
        print(cycle)
        for k in range(n - 1, -1, -1):
            if cycle[edges[k][0]] and cycle[edges[k][1]]:
                return edges[k]
        
        