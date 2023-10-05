# Question
# 1512. Number of Good Pairs
# Given an array of integers nums, return the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.


class Solution(object):
    def numIdenticalPairs(self, nums):
        n = len(nums)
        count =0
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]==nums[j]:
                    count+=1
        return count   