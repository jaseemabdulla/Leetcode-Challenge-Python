# Find First and Last Position of Element in Sorted Array

# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.


class Solution(object):
    def searchRange(self, nums, target):
        def findFirst(nums, target):
            left, right = 0, len(nums) - 1
            first = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    first = mid
                    right = mid - 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return first

        def findLast(nums, target):
            left, right = 0, len(nums) - 1
            last = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    last = mid
                    left = mid + 1  
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return last
        
        first = findFirst(nums, target)
        last = findLast(nums, target)

        return [first,last]    