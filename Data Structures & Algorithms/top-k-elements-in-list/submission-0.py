class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        heap = []
        for val, frequency in freq.items():
            heapq.heappush(heap, (-frequency, val))
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res