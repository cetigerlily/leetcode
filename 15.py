class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        set_triplets = set()
        for i in range(len(nums)):
            fix = nums[i]
            start = i + 1
            end = len(nums) - 1
            matching_sum = -fix
            while start < end:
                if nums[start] + nums[end] == matching_sum:
                    set_triplets.add((nums[i], nums[start], nums[end]))
                    start += 1
                    end -= 1
                elif nums[start] + nums[end] < matching_sum:
                    start += 1
                elif nums[start] + nums[end] > matching_sum:
                    end -= 1

        return list(list(triplet) for triplet in set_triplets)
