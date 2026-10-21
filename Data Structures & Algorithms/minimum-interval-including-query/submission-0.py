class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # heap
        intervals.sort()
        sorted_queries = []
        for i, query in enumerate(queries):
            sorted_queries.append((query, i))
        sorted_queries.sort()
        res = [-1] * len(queries)
        # use a heap

        minheap = []
        interval_idx = 0
        for query, idx in sorted_queries:
            while interval_idx < len(intervals) and intervals[interval_idx][0] <= query:
                left, right = intervals[interval_idx]
                heapq.heappush(minheap, (right - left + 1, right))
                interval_idx += 1
            
            while minheap and minheap[0][1] < query:
                heapq.heappop(minheap)
            
            if minheap:
                res[idx] = minheap[0][0]
        return res
                