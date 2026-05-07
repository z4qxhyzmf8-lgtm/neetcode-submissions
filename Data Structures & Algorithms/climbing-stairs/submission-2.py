class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prev2 = 1
        for i in range(n - 1):
            curr = prev
            prev = prev + prev2
            prev2 = curr

        return prev
        
        