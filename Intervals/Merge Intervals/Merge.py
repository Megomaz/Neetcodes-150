class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        arr = []

        for i in range(len(intervals)):
            if arr and arr[-1][1] >= intervals[i][0]:
                arr[-1][0], arr[-1][1] = min(arr[-1][0],intervals[i][0]), max(arr[-1][1],intervals[i][1])
                continue
            arr.append((intervals[i]))
        return arr