class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0,1]
        nums_set = {}
        for index, num in enumerate(nums):
            othernum = target - num
            if othernum in nums_set:
                return [nums_set[othernum], index]
            else:
                nums_set[num] = index