class Solution(object):
    def shuffle(self, nums, n):
        l = len(nums)//2
        h = [0] * len(nums)
        k = 0
        for i in range(l):
            h[k] = nums[i]
            h[k+1] = nums[i+n]
            k+=2
        return h 