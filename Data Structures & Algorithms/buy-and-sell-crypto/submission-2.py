class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        result = 0
        buy = prices[0]
        for i in range(n):
            curr_buy = prices[i]
            if curr_buy < buy:
                buy = curr_buy
            sell = prices[i]
            profit = sell - buy
            profit = max(0, profit)
            if profit > result:
                result = profit

        return result



