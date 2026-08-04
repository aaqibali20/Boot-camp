class Solution:
    def maxProfit(self, prices):
        b = prices[0]
        pf = 0

        for i in range(1, len(prices)):
            pf = max(pf, prices[i] - b)
            b = min(b, prices[i])

        return pf
