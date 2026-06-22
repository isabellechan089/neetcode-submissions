class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        
        for i in range(len(nums)):
            # Your excellent duplicate check for i stays!
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Instead of a nested 'for' loop, use two pointers
            left = i + 1
            right = len(nums) - 1
            
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                
                if current_sum > 0:
                    right -= 1
                elif current_sum < 0:
                    left += 1  # Move left up to make the sum bigger
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Duplicate check for the left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                        
        return results