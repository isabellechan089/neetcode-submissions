class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}

        def helper(i):
            if i >= len(nums):
                return 0
            if i in memo:
                return memo[i]
            rob = nums[i] + helper(i+2)
            notrob = helper(i+1)
            memo[i] = max(rob,notrob)
            return memo[i]
        return helper(0)