class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [-1] * len(nums)

        def get_rob_sum(nums, i):
            if i < 0:
                return 0

            if dp[i] != -1:
                return dp[i]

            result = max(get_rob_sum(nums, i - 2) + nums[i], get_rob_sum(nums, i - 1))
            dp[i] = result
            return dp[i]

        return get_rob_sum(nums, len(nums) - 1)
