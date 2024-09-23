class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        curr_avg = float(curr_sum / k)
        max_avg = float(curr_avg)

        start = 1
        end = start + k - 1

        while end <= len(nums) - 1:
            curr_sum = curr_sum - nums[start - 1] + nums[end]
            curr_avg = float(curr_sum / k)
            if curr_avg >= max_avg:
                max_avg = curr_avg
            start += 1
            end += 1
        return max_avg
