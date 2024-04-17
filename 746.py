class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        dp = [0] * len(cost)
        dp[-1] = cost[-1]
        dp[-2] = cost[-2]

        for i in range(len(cost) - 3, -1, -1):
            dp[i] = cost[i] + min(dp[i + 1], dp[i + 2])

        return min(dp[0], dp[1])  # either going from 0th or 1st step
