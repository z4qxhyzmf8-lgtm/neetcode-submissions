class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        best_time = 0
        adj = [[] for _ in range(n + 1)]
        for time in times:
            u, v, t = time
            adj[u].append((v, t))
        h = [(0, k)]
    
        while h:
            t0, node = heapq.heappop(h)
            if node in visited:
                continue
            visited.add(node)
            best_time = t0
            for nb, t in adj[node]:
                if nb not in visited:
                    heapq.heappush(h, (t + t0, nb))

        if len(visited) - n:
            return -1
        return best_time