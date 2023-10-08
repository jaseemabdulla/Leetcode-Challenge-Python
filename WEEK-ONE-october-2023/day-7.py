# Question No : 1458. Max Dot Product of Two Subsequences

# Given two arrays nums1 and nums2.

# Return the maximum dot product between non-empty subsequences of nums1 and nums2 with the same length.

# A subsequence of a array is a new array which is formed from the original array by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, [2,3,5] is a subsequence of [1,2,3,4,5] while [1,5,3] is not).


class Solution(object):
    def maxDotProduct(self, nums1, nums2):
        m, n = len(nums1), len(nums2)
        current = [float('-inf')] * (n + 1)
        previous = [float('-inf')] * (n + 1)

        for i in range(1, m+1):
            for j in range(1, n+1):
                curr_product = nums1[i-1] * nums2[j-1]

                current[j] = max(curr_product, previous[j], current[j-1], curr_product + max(0, previous[j-1]))
            current, previous = previous, current
        return previous[n]  