class Solution:
    def isHappy(self, n: int) -> bool:
        def next(n):
            s = 0 
            while n:
                s += (n % 10) * (n % 10) 
                n //= 10
            return s
        slow = n
        fast = next(n)
        while slow != fast:
            slow = next(slow)
            fast = next(next(fast))
            if slow == 1 or fast == 1:
                return True
        if slow == 1 or fast == 1:
            return True
        return False
        