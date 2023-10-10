# Minimum Number of Operations to Make Array Continuous

# You are given an integer array nums. In one operation, you can replace any element in nums with any integer.

# nums is considered continuous if both of the following conditions are fulfilled:

# All elements in nums are unique.

#The difference between the maximum element and the minimum element in nums equals nums.length - 1.

# For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

# Return the minimum number of operations to make nums continuous.


class Solution(object):
    def minOperations(self, nums):
        nums.sort()
        
        unique_len = 1
        ans = len(nums)
        
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[unique_len] = nums[i]
                unique_len += 1
        
        i, j = 0, 0
        
        for i in range(unique_len):
            while j < unique_len and nums[j] - nums[i] <= len(nums) - 1:
                j += 1
            ans = min(ans, len(nums) - (j - i))
        
        return ans