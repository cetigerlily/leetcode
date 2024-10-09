class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        total_houses = len(nums)
        if total_houses <= 2:
            return max(nums)

        def helper(sub_nums):
            num_houses = len(sub_nums)
            if num_houses < 2:
                return nums[0]

            dp = [0 for i in range(num_houses)]
            dp[0], dp[1] = sub_nums[0], max(sub_nums[0], sub_nums[1])

            for i in range(2, num_houses):
                dp[i] = max(dp[i - 1], dp[i - 2] + sub_nums[i])
            return max(dp)

        return max(helper(nums[0:len(nums) - 1]), helper(nums[1:len(nums)]))
