class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # hold, sold, rest
        # hold = max(hold[i-1], rest - prices[i])
        # sold = max(hold[i-1] + prices[i])
        # rest = max(rest[i-1], sold[i-1])
        hold = -prices[0]
        sold = float('-inf')
        rest = 0
        for price in prices[1:]:
            new_hold = max(hold, rest - price)
            new_sold = hold + price
            new_rest = max(rest, sold)

            hold, sold, rest = new_hold, new_sold, new_rest
        return max(hold, sold, rest)
        