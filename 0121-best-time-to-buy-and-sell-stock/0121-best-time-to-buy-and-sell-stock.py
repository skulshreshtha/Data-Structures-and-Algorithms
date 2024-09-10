class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought, max_profit = float("inf"), 0
        # bought = 1, max_profit = 4
        for p in prices:
            if p < bought:
                bought = p
                print(f"set bought to {p}")
                continue
            profit = p - bought
            print(profit)
            max_profit = max(profit, max_profit)
        return max_profit