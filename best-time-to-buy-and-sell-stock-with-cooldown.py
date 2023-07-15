class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sell,hold,prev = 0 , float("-inf"), 0

        for price in prices:
            temp = sell
            sell = max(sell, hold + price)
            hold = max(hold, prev - price)
            prev = temp

        return sell