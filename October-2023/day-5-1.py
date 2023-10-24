 # Question No : 1502. Can Make Arithmetic Progression From Sequence
 
 # A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.


class Solution(object):
    def canMakeArithmeticProgression(self,arr):
        n = len(arr)
        arr.sort()
        k = arr[1] - arr[0]
        for i in range(n-1):
            if arr[i+1] - arr[i] != k:
                return False
        return True 