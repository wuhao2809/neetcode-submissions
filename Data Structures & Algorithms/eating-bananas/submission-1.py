class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # upper(n/k)
        # brutal force, try it one by one
        # k = min is 1, max is max(piles) O(max(piles)*n)
        # O(log(max(piles)) * n )
        n = len(piles)
        high = max(piles)
        low = 1
        def test_k(k:int) -> bool:
            total = 0
            for pile in piles:
                curr = pile // k
                if pile % k > 0:
                    curr += 1
                total += curr
            return total <= h
        ans = high
        while low <= high:
            mid = (low + high) // 2
            if test_k(mid):
                high = mid - 1
                ans = mid
            else:
                low = mid + 1
        return ans