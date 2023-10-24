# Question no: 1486. XOR Operation in an Array

# You are given an integer n and an integer start.

# Define an array nums where nums[i] = start + 2 * i (0-indexed) and n == nums.length.

# Return the bitwise XOR of all elements of nums.

class Solution(object):
    def xorOperation(self, n, start):
        nums = []
        result = 0 
        for i in range(n):
            nums.append(start+(2*i))
        for i in nums:
            result ^= i
        return result    