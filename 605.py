class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        available_count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                is_left_empty = (i == 0) or (flowerbed[i - 1] == 0)
                is_right_empty = (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0)

                if is_left_empty and is_right_empty:
                    flowerbed[i] = 1
                    available_count += 1
        return n <= available_count
