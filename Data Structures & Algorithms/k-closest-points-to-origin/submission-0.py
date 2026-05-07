class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance_to_origin(point):
            dx = point[0] 
            dy = point[1]
            return math.sqrt(dx ** 2 + dy ** 2)
        
        h = []
        for point in points:
            h.append((distance_to_origin(point), point[0], point[1])) 
        heapq.heapify(h)
        sol = []
        for i in range(k):
            point = heapq.heappop(h)
            sol.append([point[1], point[2]])
        return sol
            

        
        