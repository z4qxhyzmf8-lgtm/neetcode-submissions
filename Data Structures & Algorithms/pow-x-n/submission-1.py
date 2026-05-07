class Solution:
    def myPow(self, x: float, n: int) -> float:
        memo = {}
        if n == 1:
            return x
        if n == 0:
            return 1
        if x == 0:
            return 0
        if x == 1:
            return 1
        def dfs(n):
            nonlocal memo
            if n in memo:
                return memo[n]
            if n == 1:
                return x

            memo[n] = dfs(n // 2) * dfs(n // 2 + n % 2)
            return memo[n]
        if n > 1:
            return dfs(n)
        else:
            return 1/dfs(abs(n))
            
        