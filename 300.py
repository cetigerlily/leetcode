class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = [0 for i in range(len(nums))]
        for i in range(len(dp)):
            current_max = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    new_max = dp[j] + 1
                    if new_max > current_max:
                        current_max = new_max
            dp[i] = current_max
        return max(dp)
