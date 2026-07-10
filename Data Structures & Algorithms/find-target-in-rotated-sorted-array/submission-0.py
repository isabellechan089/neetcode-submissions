class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        idx = -1
        while left <= right:
            l = nums[left]
            r = nums[right]
            mid = (left+right) //2
            m = nums[mid]
            if m == target:
                return mid
            if l <= m:
                if l <= target <= m:
                    right = mid -1
                else:
                    left= mid +1
            else:
                if m <= target <= r:
                    left = mid+1
                else:
                    right = mid - 1
                
        return -1
