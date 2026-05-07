class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        n = len(intervals)
        if n == 0:
            return[newInterval]
        sol = []
        start = newInterval[0]
        end = newInterval[1]
        for i, interval in enumerate(intervals):
            if interval[0] <= start and end <= interval[1]:
                return intervals
            if start < interval[0]:
                index = i
                while index < n and end > intervals[index][1]:
                    index += 1
                if index == n:
                    sol.append([start, end])
                    return sol
                if intervals[index][0] <= end and end <= intervals[index][1]:
                    sol.append([start, intervals[index][1]])
                    index += 1
                else:
                    sol.append([start, end])
                    sol.append(intervals[index])
                    index += 1
                while index < n:
                    sol.append(intervals[index])
                    index += 1
                return sol
                
            elif interval[0] <= start and start <= interval[1]:
                new_start = interval[0]
                index = i + 1
                while index < n and end > intervals[index][1]:
                    index += 1
                if index == n:
                    sol.append([new_start, end])
                    return sol
                if intervals[index][0] <= end and end <= intervals[index][1]:
                    sol.append([new_start, intervals[index][1]])
                    index += 1
                else:
                    sol.append([new_start, end])
                    sol.append(intervals[index])
                    index += 1
                while index < n:
                    sol.append(intervals[index])
                    index += 1
                return sol
            else:
                sol.append(interval)
        sol.append(newInterval)
        return sol


        