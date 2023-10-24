# Question No : 229. Majority Element 
# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

class Solution(object):
    def majorityElement(self, nums):
        dic = {}
        res =[]
        n = len(nums)
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for item,count in dic.items():
            if count > n/3:
                res.append(item)
        return res      