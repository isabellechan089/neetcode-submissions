class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        if k ==1:
            return nums
        cur = max(nums[:k])
        res.append(cur)
        i = 0
        for j in range(k, len(nums)):
            if nums[j] > res[i]:
                res.append(nums[j])
            else:
                res.append(res[-1])
            i+=1
        return res