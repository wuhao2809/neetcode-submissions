class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []

        for interval in intervals:
            start, end = interval
            
            if not res or res[-1][1] < start:
                res.append(interval)
            else:
                res[-1][1] = max(end, res[-1][1])
        return res