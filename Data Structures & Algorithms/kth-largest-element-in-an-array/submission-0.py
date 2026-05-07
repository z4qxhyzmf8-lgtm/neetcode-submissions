class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = [-num for num in nums]
        heapq.heapify(h)
        for i in range(k - 1):
            heapq.heappop(h)
        return -h[0]
        
        