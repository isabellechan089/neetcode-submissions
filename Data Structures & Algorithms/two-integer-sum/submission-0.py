class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 2: return [0,1]
        nums_set = set(nums)
        for index, num in enumerate(nums):
            othernum = target - num
            if othernum in nums:
                otherind = nums.index(othernum)
                if index != otherind:
                    return [index, otherind]
            del nums[index]