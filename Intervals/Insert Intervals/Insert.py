class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        arr = []

        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[1]:
                return arr + [newInterval] + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                arr.append(intervals[i])
            else:
                newInterval[0],newInterval[1] = min(newInterval[0],intervals[i][0]),max(newInterval[1],intervals[i][1])
        arr.append((newInterval))
                
                
        return arr
