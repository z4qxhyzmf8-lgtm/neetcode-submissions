class Solution:
    def reverse(self, x: int) -> int:
        min_x = (1 << 31)
        max_x = (1 << 31) - 1
        temp = x
        ans = 0
        x = abs(x)
        while x:
            digit = x % 10
            x = x // 10
            if ans > max_x // 10 or (ans == max_x // 10 and digit > max_x % 10):
                return 0
            if ans > min_x // 10 or (ans == min_x // 10 and digit > min_x % 10):
                return 0
            ans = ans * 10 + digit
        if temp < 0:
            return -ans
        return ans

        
        