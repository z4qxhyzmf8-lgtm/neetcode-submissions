class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        for num in nums: 
            dict[num] = dict.get(num, 0) + 1
        
        n = len(nums)
        freq = [[] for i in range(n + 1)]
        for key in dict:
            freq[dict[key]].append(key)

        sol = []
        count = k
        for i in range(n + 1):
            j = n - i
            if freq[j] != []:
                for num in freq[j]:
                    sol.append(num)
                    count -= 1
                    if count == 0:
                        break
            if count == 0:
                break
        return sol
                


        



            
        

        
        