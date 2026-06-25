class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        prefix = []
        suffix = []
        ma = 0
        for h in height:
            if h > ma:
                ma = h
            prefix.append(ma)
        ma = 0
        for j in height[::-1]:
            if j > ma:
                ma = j
            suffix.append(ma)
        suffix = suffix[::-1]
        for i in range(len(height)):
            total += min(prefix[i], suffix[i]) - height[i]
        return total