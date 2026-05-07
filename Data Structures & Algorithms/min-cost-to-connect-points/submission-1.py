class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj = [[] for _ in points]
        L1 = lambda x, y: abs(x[0] - y[0]) + abs(x[1] - y[1])
        for i, x in enumerate(points):
            for j, y in enumerate(points):
                if not i - j:
                    continue
                adj[i].append((L1(x, y), j))
        cost = 0
        node = 0
        visited = set()
        h = [(0, 0)]
        while h:
            d, node = heapq.heappop(h)
            if node in visited:
                continue
            visited.add(node)
            cost += d
            for d, nb in adj[node]:
                if nb not in visited:
                    heapq.heappush(h, (d, nb))
            
        return cost
