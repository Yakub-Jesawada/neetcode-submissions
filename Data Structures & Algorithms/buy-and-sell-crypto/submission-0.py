class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        for i,n in enumerate(prices):
            min_price = min(min_price,n)
            profit = n - min_price
            max_profit = max(max_profit,profit)
        return max_profit