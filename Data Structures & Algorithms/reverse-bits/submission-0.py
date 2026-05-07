class Solution:
    def reverseBits(self, n: int) -> int:
        mask = 0
        for i in range(32):
            if n & (1 << i):
                mask ^= (1 << (32 - i - 1))
        return mask
        