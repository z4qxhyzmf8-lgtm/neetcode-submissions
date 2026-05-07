class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegrees = [0 for _ in range (numCourses)]
        edges = defaultdict(list)
        for c, pre in prerequisites:
            indegrees[c] += 1
            edges[pre].append(c)

        q = deque()
        for i in range(numCourses):
            if indegrees[i] == 0:
                q.append(i)
        count = 0
        while q:
            node = q.popleft()
            count += 1
            for next_node in edges[node]:
                indegrees[next_node] -= 1
                if indegrees[next_node] == 0:
                    q.append(next_node)
        return count == numCourses
        
        
        


        