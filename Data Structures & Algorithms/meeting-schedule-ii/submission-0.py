"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        n = len(intervals) # [(15,20)] 3
        if n <= 1:
            return n
        intervals.sort(key=lambda x:x.start)
        min_heap = [] # 15, 40
        for interval in intervals:
            start, end = interval.start, interval.end #1
            if min_heap and min_heap[0] <= start:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap,end)
            else:
                heapq.heappush(min_heap,end)
        return len(min_heap)
        
        