import math

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # hashmap approach
        elements = dict()
        for i in range(len(nums)):
            if nums[i] in elements:
                elements[nums[i]] += 1
            else:
                elements[nums[i]] = 1

        operations = 0
        for element in elements:
            pair = k - element

            if pair in elements:
                if pair != element:
                    operations += min(elements[element], elements[pair])
                else:
                    operations += int(math.floor(elements[element] / 2))
                elements[element] -= 1
                elements[pair] -= 1

        return operations

        # two pointer approach
        # start = 0
        # end = len(nums) - 1
        # operations = 0
        # nums.sort()
        #
        # while start < end:
        #     a = nums[start]
        #     b = nums[end]
        #
        #     if a + b == k:
        #         operations += 1
        #         start += 1
        #         end -= 1
        #     else:
        #         if a + b < k:
        #             start += 1
        #         elif a + b > k:
        #             end -= 1
        # return operations
