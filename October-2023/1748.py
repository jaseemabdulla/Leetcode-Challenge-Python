# Sum of Unique Elements

# You are given an integer array nums. The unique elements of an array are the elements that appear exactly once in the array.

# Return the sum of all the unique elements of nums.


class Solution(object):
    def sumOfUnique(self, nums):
        dic = {}
        for i in nums:
            if i in dic:
                dic[i] +=1
            else:
                dic[i] = 1
        sum = 0
        for num,count in dic.items():
            if count == 1:
                sum += num
        return sum                
 