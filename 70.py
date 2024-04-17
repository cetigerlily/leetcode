class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n == 1 or n == 2:
            return n

        dp_table = dict()

        dp_table[1] = 1
        dp_table[2] = 2

        for i in range(3, n + 1):
            dp_table[i] = dp_table[i - 1] + dp_table[i - 2]
        return dp_table[n]
