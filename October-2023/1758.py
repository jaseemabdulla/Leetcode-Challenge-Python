# Minimum Changes To Make Alternating Binary String

# You are given a string s consisting only of the characters '0' and '1'. In one operation, you can change any '0' to '1' or vice versa.

# The string is called alternating if no two adjacent characters are equal. For example, the string "010" is alternating, while the string "0100" is not.

# Return the minimum number of operations needed to make s alternating.


class Solution:
    def minOperations(self, s):
        return min(self.alt("0",s),self.alt("1",s))
        
    def alt(self,num,string):
        count = 0
        for s in string:
            if s != num:
                count +=1
            num = "0" if num == "1" else "1"
        return count