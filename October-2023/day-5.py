# Question No : 343. Integer Break

# Given an integer n, break it into the sum of k positive integers, where k >= 2, and maximize the product of those integers.

#Return the maximum product you can get.

class Solution(object):
    def integerBreak(self, n):
        if n == 2:
            return 1
        if n == 3:
            return 2

        dp = [0] * (n + 1)    

        dp[2] = 2
        dp[3] = 3
        for i in range(4, n + 1):
            max_product = 0
            for j in range(2, i // 2 + 1):
                max_product = max(max_product, dp[j] * dp[i - j])
            dp[i] = max_product
        return dp[n]  