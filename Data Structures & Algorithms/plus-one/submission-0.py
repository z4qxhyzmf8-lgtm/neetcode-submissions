class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        n = len(digits)
        for i in range(n - 1, -1, -1):
            digits[i] += 1
            carry = digits[i] // 10
            digits[i] %= 10
            if not carry:
                break
        if carry:
            return [1] + digits
        return digits

        