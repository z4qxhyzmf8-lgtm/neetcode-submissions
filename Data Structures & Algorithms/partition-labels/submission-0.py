class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict()
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        sol = []
        l, r = 0, 0
        char_set = set()
        char_set.add(s[l])

        while r < len(s):
            while r < len(s) and char_set:
                char_set.add(s[r])
                freq[s[r]] -= 1
                if freq[s[r]] == 0:
                    char_set.remove(s[r])
                r += 1
            sol.append(r - l)
            if r < len(s):
                char_set.add(s[r])
            l = r
        return sol
                    


        