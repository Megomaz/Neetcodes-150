"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        heap = []

        for interval in intervals:
            heapq.heappush(heap,(interval.start,interval.end))
        
        while len(heap) > 1:
            smallest = heapq.heappop(heap)
            if smallest[1] > heap[0][0]:
                return False

        return True


# O(1) space solution
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda i: i.start)

        for i in range(1, len(intervals)):
            i1 = intervals[i - 1]
            i2 = intervals[i]

            if i1.end > i2.start:
                return False
        return True