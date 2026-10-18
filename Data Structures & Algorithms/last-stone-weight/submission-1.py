class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # maxheap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            remain = stone1 - stone2
            if remain == 0:
                continue
            else:
                heapq.heappush(stones, -abs(remain))
        return -stones[0] if stones else 0
                