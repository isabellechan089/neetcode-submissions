class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxA = 0
        stack = []
        for idx, h in enumerate(heights):
            if stack and h < stack[-1][1]:
                while stack and h < stack[-1][1]:
                    res = stack.pop()
                    maxA = max((idx - res[0])*res[1], maxA)
                stack.append((res[0], h))
            else:
                stack.append((idx, h))
        idx = len(heights)
        while stack:
            res = stack.pop()
            maxA = max((idx - res[0])*res[1], maxA)
        return maxA