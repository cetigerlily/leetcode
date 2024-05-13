class Solution(object):
    def largestLocal(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[List[int]]
        """
        n = len(grid)
        result = [[0 for i in range(n - 2)] for i in range(n - 2)]

        for i in range(n - 2):
            for j in range(n - 2):
                max_i, max_j = i, j  # the current position of max value within window

                for r in range(3):
                    current_r = i + r
                    for c in range(3):
                        current_c = j + c
                        if grid[current_r][current_c] > grid[max_i][max_j]:
                            max_i, max_j = current_r, current_c
                result[i][j] = grid[max_i][max_j]
        return result
