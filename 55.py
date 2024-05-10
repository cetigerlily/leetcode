class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        length = len(nums)
        i = length - 1
        dp = [False] * (len(nums))

        while i >= 0:
            current_jump = nums[i]
            if current_jump >= length - 1 - i:  # can reach end on its own
                dp[i] = True
            else:
                while current_jump > 0:  # iterating through possible jumps it can do from position
                    if dp[i + current_jump]:
                        dp[i] = True
                        break
                    current_jump -= 1
            i -= 1
        return dp[0]
