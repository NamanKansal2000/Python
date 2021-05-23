class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxx += prices[i]-prices[i-1]
        return maxx
        
