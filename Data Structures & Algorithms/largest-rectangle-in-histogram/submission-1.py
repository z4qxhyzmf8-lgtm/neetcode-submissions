class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = [-1 for _ in range(n)]
        right = [n for _ in range(n)]
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                left[i] = stack[-1]
            stack.append(i) 
        
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                right[i] = stack[-1]
            stack.append(i)
        
        A_max = 0
        for i in range(n):
            left[i] += 1
            right[i] -= 1
            A = heights[i] * (right[i] - left[i] + 1)
            A_max = max(A, A_max)
        return A_max

        