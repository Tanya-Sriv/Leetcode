class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         p = dict(zip(prices, range(len(prices))))
#         s = sorted(p)
#         print(s)
#         for i in s:
        maxdiff = 0
        low = prices[0]
        for i in range(len(prices)):
            if prices[i] < low:
                low = prices[i]
            maxdiff = max(maxdiff, prices[i]-low)
            print(maxdiff)
        return maxdiff