class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0 for _ in range(numCourses)]
        edges = defaultdict(list)
        for c, pre in prerequisites:
            indegree[c] += 1
            edges[pre].append(c)

        q = deque()
        count = 0
        for i in range(numCourses):
            if not indegree[i]:
                q.append(i)
        sol = []
        while q:
            node = q.popleft()
            sol.append(node)
            count += 1
            for next_node in edges[node]:
                indegree[next_node] -= 1
                if not indegree[next_node]:
                    q.append(next_node)
        if count == numCourses:
            return sol
        return [] 
        