class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        max_l = [-1 for _ in range(n)]
        max_r = [-1 for _ in range(n)]
        max_l[0] = height[0]
        max_r[n - 1] = height[n - 1]

        for i in range(1, n):
            max_l[i] = max(max_l[i - 1], height[i])

        for i in range(n - 2, -1, -1):
            max_r[i] = max(max_r[i + 1], height[i])

        A = 0
        for i in range(n):
            A += max(min(max_l[i], max_r[i]) - height[i], 0)
        return A
        
        