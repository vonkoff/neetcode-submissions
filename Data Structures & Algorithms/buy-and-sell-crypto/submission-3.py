class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, minP = 0, prices[0]

        for price in prices:

            minP = min(price, minP)
            maxP = max(price - minP, maxP)
        return maxP