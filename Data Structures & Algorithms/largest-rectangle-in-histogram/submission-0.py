class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left = [0] * len(heights)
        right = [0] *len(heights)
        for idx, h in enumerate(heights):
            while stack and h <= heights[stack[-1]]:
                stack.pop()
            if not stack:
                left[idx] = -1
            else:
                left[idx] = stack[-1]
            stack.append(idx)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if not stack:
                right[i] = len(heights)
            else:
                right[i] = stack[-1]
            stack.append(i)
        maxi = 0
        for h in range(len(heights)):
            area = heights[h] * (right[h]-left[h] -1)
            maxi = max(maxi, area)

        return maxi