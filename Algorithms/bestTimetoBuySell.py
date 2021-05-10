class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = float("inf")
        
        for price in prices:
            if buy_price > price:
                buy_price = price
            else:
                profit = max(profit,price-buy_price)
        
        return profit