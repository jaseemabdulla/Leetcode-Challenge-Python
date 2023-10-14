# Painting the Walls

# You are given two 0-indexed integer arrays, cost and time, of size n representing the costs and the time taken to paint n different walls respectively. There are two painters available:

#A paid painter that paints the ith wall in time[i] units of time and takes cost[i] units of money.

# A free painter that paints any wall in 1 unit of time at a cost of 0. But the free painter can only be used if the paid painter is already occupied.

#Return the minimum amount of money required to paint the n walls.


class Solution(object):
    def paintWalls(self, cost, time):
        n = len(cost)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in range(n):
            for j in range(n, 0, -1):
                dp[j] = min(dp[j], dp[max(j - time[i] - 1, 0)] + cost[i])

        return dp[n]