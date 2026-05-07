class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        n = len(intervals)
        sol = []
        start = intervals[0][0]
        end = intervals[0][1]
        i = 1
        while i < n:
            if end < intervals[i][0]:
                sol.append([start, end])
                start = intervals[i][0]
                end = intervals[i][1]
            elif end < intervals[i][1]:
                end = intervals[i][1]
            
            i += 1
        sol.append([start, end])
        return sol
        
        