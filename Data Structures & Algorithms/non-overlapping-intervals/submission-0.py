class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # sort by end
        intervals.sort(key= lambda x:(x[1], x[0]))
        res = 0
        prev_end = intervals[0][1]
        for i in range(1, len(intervals)):
            start,end = intervals[i]
            if prev_end > start:
                res += 1
            else:
                prev_end = end
        return res