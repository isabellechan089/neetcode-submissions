class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        minl = height[l]
        minr = height[r]
        res = 0

        while l < r:
            if minl <= minr:
                l+=1
                minl = max(height[l], minl)
                res += minl- height[l]
            else:
                r-=1
                minr = max(height[r], minr)
                res += minr - height[r]

        return res