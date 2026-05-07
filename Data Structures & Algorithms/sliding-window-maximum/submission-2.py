class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #max-heap solution
        n = len(nums)
        h = []
        sol = []
        for r in range(n):
            heapq.heappush(h, [-nums[r], r])
            if r >= k - 1:
                while h[0][1] <= r - k:
                    heapq.heappop(h)
                sol.append(-h[0][0])
        return sol


        
        