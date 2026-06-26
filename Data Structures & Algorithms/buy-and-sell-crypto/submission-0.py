class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0,0
        maxp = 0
        while j < len(prices):
            current = prices[j] - prices[i]
            if prices[j] < prices[i]:
                i = j
            maxp = max(maxp, current)
            j+=1
        return maxp