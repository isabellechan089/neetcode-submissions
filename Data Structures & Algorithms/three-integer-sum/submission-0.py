class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        right = len(nums)-1
        results = []
        for i in range(len(nums)):
            if nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)):
                sofar = nums[i] + nums[j]
                right = len(nums) -1
                while right > j:
                    if sofar + nums[right] > 0:
                        right -=1
                    elif sofar + nums[right] < 0:
                        break
                    else:
                        results.append([nums[i], nums[j], nums[right]])
                        right -=1
        return results
