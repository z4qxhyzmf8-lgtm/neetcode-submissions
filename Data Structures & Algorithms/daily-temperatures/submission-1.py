class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        result = [0 for _ in range(n)]
        stack = []
        for i in range(n):
            while stack:
                if temperatures[i] <= temperatures[stack[-1]]:
                    break
                else:
                    result[stack[-1]] = i - stack[-1]
                    stack.pop()

            stack.append(i)
        return result
        