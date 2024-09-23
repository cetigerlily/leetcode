from heapq import heapify, heappush, heappop

class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heap = []
        for i in range(k):
            heap.append(nums[i])
        heapify(heap)

        for i in range(k, len(nums)):
            heappush(heap, nums[i])
            heappop(heap)
        return heappop(heap)
