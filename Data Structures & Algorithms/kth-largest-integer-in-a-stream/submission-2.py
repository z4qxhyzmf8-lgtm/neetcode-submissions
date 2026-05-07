class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.check = k
        self.h = []
        for i, num in enumerate(nums):
            heapq.heappush(self.h, num)
            if i >= self.check:
                heapq.heappop(self.h)

    def add(self, val: int) -> int:
        heapq.heappush(self.h, val)
        if len(self.h) > self.check:
            heapq.heappop(self.h)
        return self.h[0]
        
