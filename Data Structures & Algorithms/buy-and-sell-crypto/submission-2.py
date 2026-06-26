class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxp = 0
        low = prices[0]

        for p in prices:
            
            low = min(p, low)
            maxp = max(maxp, p - low)
            
        return maxp