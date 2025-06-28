class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        arr = []
        count = 0

        for i in range(len(intervals)):
            if arr and arr[-1][1] > intervals[i][0]:
                arr[-1][0],arr[-1][1] = min(arr[-1][0],intervals[i][0]),min(arr[-1][1],intervals[i][1])
                count +=1
                continue
            arr.append((intervals[i]))
        return count
            