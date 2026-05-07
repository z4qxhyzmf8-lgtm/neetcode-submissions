class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        #max-heap solution
        #relies strictly on heap property (first element of heap is max)
        #we do a heap on the pair [value, index]
        #O(nlogn) due to heap push
        #
        #n = len(nums)
        #h = []
        #sol = []
        #for r in range(n):
        #    heapq.heappush(h, [-nums[r], r])
        #    if r >= k - 1:
        #        while h[0][1] <= r - k:
        #            heapq.heappop(h)
        #        sol.append(-h[0][0])
        #return sol
        #
        #deque solution
        #our deque holds indices of elemensts in decreasing order of value
        #we achieve this by poping to the right all elements that
        #are smaller than the current one since they can't be future
        #maximas;
        n = len(nums)
        sol = []
        q = deque([])
        for r in range(n):
            while q and nums[q[-1]] <= nums[r]:
                q.pop()
            q.append(r)
            if q[0] < r - k + 1:
                q.popleft()
            if r >= k - 1:
                sol.append(nums[q[0]])


        return sol



        
        