class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        low = prices[0]

        for p in prices:
            maxp = max(maxp, p - low)
            low = min(p, low)
            
        return maxp