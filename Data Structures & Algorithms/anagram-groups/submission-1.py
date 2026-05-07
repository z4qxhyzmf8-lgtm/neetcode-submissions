class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            freq = [0 for i in range(26)]
            for char in s:
                x = ord(char) - ord('a')
                freq[x] += 1
            
            freq_t = tuple(freq)
            if freq_t in dict:
                dict[freq_t].append(s)
            else:
                dict[freq_t] = [s]

        sol = []
        for key in dict:
            sol.append(dict[key])
        return sol

        