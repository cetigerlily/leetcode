class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        current_permutation = []

        def backtrack():
            if len(current_permutation) == len(nums):
                result.append(current_permutation[:])  # can't just do current_permutation, as it will be edited with popo()
                return

            for num in nums:
                if num not in current_permutation:  # able to do this because the integers are unqiue
                    current_permutation.append(num)
                    backtrack()
                    current_permutation.pop()

        for i in range(len(nums)):
            current_permutation = [nums[i]]
            backtrack()

        return result
