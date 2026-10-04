class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if sell at curr point
        # prefix low
        curr_min = float('inf')
        res = 0
        for price in prices:
            curr_min = min(curr_min, price)
            res = max(price - curr_min, res)
        return res