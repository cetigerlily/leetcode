class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = {}  # <element, frequency of element>

        for i in range(len(nums)):
            element = nums[i]
            if element not in frequency:
                frequency[element] = 0
            frequency[element] += 1

        sorted_items = list(frequency.items())
        sorted_items.sort(reverse=True, key=lambda x: x[1])

        result = []
        for i in range(k):
            result.append(sorted_items[i][0])
        return result
