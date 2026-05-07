class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        h = []
        for stone in stones:
            heapq.heappush(h, -stone)
        
        while len(h) > 1:
            x = -heapq.heappop(h)
            y = -heapq.heappop(h)
            if x > y:
                heapq.heappush(h, -(x - y))
            
        if h:
            return -heapq.heappop(h)
        return 0
        