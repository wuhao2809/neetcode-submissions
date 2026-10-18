class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxheap = []
        for x, y in points:
            dist = x*x + y*y
            heapq.heappush(maxheap, (-dist, x, y))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        return [[x,y] for _,x,y in maxheap]