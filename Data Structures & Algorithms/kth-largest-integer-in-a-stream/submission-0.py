class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.check = k
        self.ind = len(nums)
        self.h = []
        for i, num in enumerate(nums):
            heapq.heappush(self.h, (-num, i))

    def add(self, val: int) -> int:
        temp = []
        self.ind += 1
        heapq.heappush(self.h, (-val, self.ind))
        for i in range(self.check):
            temp.append(heapq.heappop(self.h))
        ans = -temp[-1][0]
        for vals in temp:
            heapq.heappush(self.h, vals)
        return ans
        
