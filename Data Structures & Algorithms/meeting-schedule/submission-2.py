"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # sort based
        intervals.sort(key=lambda i:i.start)
        prev = -1
        for interval in intervals:
            start = interval.start
            end = interval.end
            if start < prev:
                return False
            prev = end
        return True