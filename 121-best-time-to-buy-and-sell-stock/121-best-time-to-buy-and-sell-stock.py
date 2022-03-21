class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxdiff, low = 0, 0
        for i in range(len(prices)):
            if prices[i] < prices[low]:
                low = i
            maxdiff = max(maxdiff, prices[i]-prices[low])
        return maxdiff