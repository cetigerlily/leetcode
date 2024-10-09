class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # contact police if 2 adjacent houses are broken into
        # find maximum amount rob without alerting police

        # i.e. max sum s.t. no two adjacent values
        num_houses = len(nums)
        if num_houses < 2:
            return nums[0]

        dp = [0 for i in range(num_houses)]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, num_houses):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        print(dp)
        return max(dp)
