class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        num_white = 0
        num_black = 0

        for i in range(k):
            if blocks[i] == "W": num_white += 1
            else: num_black += 1
        min_recolors = num_white

        for i in range(1, len(blocks) - k + 1):
            # removing old block from count
            if blocks[i - 1] == "W": num_white -= 1
            else: num_black -= 1

            # adding new block to count
            if blocks[i + k - 1] == "W": num_white += 1
            else: num_black += 1

            min_recolors = min(min_recolors, num_white)

        return min_recolors
