class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx = float('-inf')
        minprice = prices[0]
        for p in prices:
            maxx = max(maxx, p-minprice)
            minprice = min(minprice, p)
        return maxx
