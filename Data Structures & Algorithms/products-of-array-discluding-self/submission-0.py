class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = nums[0]
        check = False
        if 0 in nums: check = True
        for i in range(1, len(nums)):
            if nums[i]!=0:
                product *= nums[i]
        result = []
        for num in nums:
            if num != 0:
                if not check:
                    result.append(int(product / num))
                else: result.append(0)
            else:
                result.append(int(product))
        return result