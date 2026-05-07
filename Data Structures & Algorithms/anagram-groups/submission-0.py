class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        for s in strs:
            letters = []
            for char in s:
                letters.append(char)
            letters.sort()
            letters_t = tuple(letters)
            if letters_t in dict:
                dict[letters_t].append(s)
            else:
                dict[letters_t] = [s]
        sol = []
        for key in dict:
            sol.append(dict[key])
        return sol

        