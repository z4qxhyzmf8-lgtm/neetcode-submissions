class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {'2': ['a', 'b', 'c'],
                     '3': ['d', 'e', 'f'],
                     '4': ['g', 'h', 'i'],
                     '5': ['j', 'k', 'l'],
                     '6': ['m', 'n', 'o'],
                     '7': ['p', 'q', 'r', 's'],
                     '8': ['t', 'u', 'v'],
                     '9': ['w', 'x', 'y', 'z']
                    }
        sol = []
        sub = []
        n = len(digits)
        if not n:
            return []

        def back(i):
            nonlocal sol
            nonlocal sub
            nonlocal n
            nonlocal digit_map

            if i >= n:
                sol.append(''.join(sub))
                return
    
            for char in digit_map[digits[i]]:
                sub.append(char)
                back(i + 1)
                sub.pop()
        back(0)
        return sol
