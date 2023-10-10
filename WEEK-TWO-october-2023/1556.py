# Thousand Separator

# Given an integer n, add a dot (".") as the thousands separator and return it in string format.


class Solution(object):
    def thousandSeparator(self, n):
        n = str(n)                                      
        for i in range(len(n)-3, 0, -3):
            n =  str(n)[:i] + "." + str(n)[i:]
        return n