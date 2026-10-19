class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP, minP = 0, prices[0]

        for price in prices:
            maxP = max(price - minP, maxP)
            minP = min(price, minP)
        return maxP