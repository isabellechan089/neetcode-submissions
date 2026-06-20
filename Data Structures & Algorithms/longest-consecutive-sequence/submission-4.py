class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        longest = -float('inf')
        left, right = 0,0
        nums = sorted(list(set(nums)))
        while right < len(nums) - 1:
            current = nums[right]
            nextNum = nums[right+1]
            right +=1
            if nextNum - current == 1:
                current = nextNum
                diff = right - left +1
                if diff > longest:
                    longest = diff
            else:
                left = right
        return longest if longest != -float('inf') else 0