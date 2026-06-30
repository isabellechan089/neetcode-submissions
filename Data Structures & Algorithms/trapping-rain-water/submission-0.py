class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        i = 0
        j = i + 1
        running = 0
        while j < len(height):
            left = height[i]
            right = height[j]
            if (i!=j and right >= left):
                i = j
                j+=1
                total += running
                running = 0
            elif i !=j  and right < left:
                running += left - right
                j+=1
        return total