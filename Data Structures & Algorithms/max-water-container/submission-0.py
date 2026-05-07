class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        A_max = 0
        l = 0
        r = n - 1
        while l < r:
            m = min(heights[l], heights[r])
            A = m * (r - l)
            A_max = max(A, A_max)
            if m == heights[l]:
                l += 1
                continue
            if m == heights[r]:
                r -= 1
                continue
        return A_max

        