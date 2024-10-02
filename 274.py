import math

class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort()
        num_citations = len(citations)
        if num_citations <= 2:
            h_index = 0
            for i in range(num_citations):
                new_h_index = min(num_citations - i, citations[i])
                if new_h_index > h_index:
                    h_index = new_h_index
            return h_index

        start, end = 0, len(citations) - 1
        h_index = 0

        while start <= end:
            mid = int(math.floor((start + end) / 2))

            if num_citations - mid <= citations[mid]:
                h_index = max(h_index, num_citations - mid)
                end = mid - 1
            else:
                start = mid + 1

        return h_index
