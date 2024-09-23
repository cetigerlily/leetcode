class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start, end = 0, len(nums) - 1
        while start <= end:
            middle = int(floor((start + end) / 2))
            left = nums[middle - 1] if middle > 0 else float('inf')
            right = nums[middle + 1] if middle < len(nums) - 1 else float('inf')

            if left < nums[middle] and right < nums[middle]:
                return middle
            elif left > nums[middle]:  # when only left greater or both greater
                end = middle - 1
            elif right > nums[middle]:
                start = middle + 1
        return nums.index(max(nums))
