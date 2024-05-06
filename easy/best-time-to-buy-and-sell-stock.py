class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        if len(prices) == 1:
            return max_profit
        cheapest = prices[0]
        for i in prices[1:]:
            if i - cheapest > max_profit:
                max_profit = i - cheapest
            if i < cheapest: cheapest = i
        return max_profit
