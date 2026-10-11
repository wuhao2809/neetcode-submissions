class MedianFinder:
# minheap store large numbers; maxheap store small numbers
    def __init__(self):
        self.maxheap = []
        self.minheap = []

    def addNum(self, num: int) -> None:
        # minheap always has one more element than minheap
        heapq.heappush(self.maxheap, -num)
        curr = -heapq.heappop(self.maxheap)
        heapq.heappush(self.minheap, curr)
        if len(self.minheap) - len(self.maxheap) > 1:
            curr = -heapq.heappop(self.minheap)
            heapq.heappush(self.maxheap, curr)
        

    def findMedian(self) -> float:
        if len(self.minheap) > len(self.maxheap):
            return self.minheap[0]
        else:
            return (-self.maxheap[0] + self.minheap[0])/2
        