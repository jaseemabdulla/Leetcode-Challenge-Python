# Calculate Money in Leetcode Bank

# Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

# He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

# Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.


class Solution(object):
    def totalMoney(self, n):
        total = 0
        current_money = 1 
        for day in range(1, n + 1):
            total += current_money
            current_money += 1
            if day % 7 == 0:
                current_money -= 6 
        return total