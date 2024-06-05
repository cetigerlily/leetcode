class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        single_number = 0
        for num in nums:
            single_number = num ^ single_number
        return single_number
