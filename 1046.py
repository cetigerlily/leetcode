import heapq


class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stone_heap = []
        for stone in stones:
            heapq.heappush(stone_heap, stone * -1)

        while len(stone_heap) > 1:
            y = heapq.heappop(stone_heap) * -1
            x = heapq.heappop(stone_heap) * -1

            if x != y:
                new_y = y - x
                heapq.heappush(stone_heap, new_y * -1)

        if len(stone_heap) > 0:
            return heapq.heappop(stone_heap) * -1
        else:
            return 0
