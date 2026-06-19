class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        count = 0
        for num in nums:
            if num - 1 not in numSet:
                i = 1
                tcount = 1
                while i < len(nums):
                    if num + i in numSet:
                        tcount +=1
                        i+=1
                    else: break
                if tcount > count: count = tcount
        return count