class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # n x n matrix
        n = len(grid)
        rows = dict()
        columns = dict()

        for i in range(n):
            curr_row = tuple(grid[i])
            curr_column = []
            for j in range(n): # getting the column which is grid[i][0 to j]
                curr_column.append(grid[j][i])
            curr_column = tuple(curr_column)

            if curr_row in rows:
                rows[curr_row].append(i)
            else:
                rows[curr_row] = [i]
            if curr_column in columns:
                columns[curr_column].append(i)
            else:
                columns[curr_column] = [i]

        num_pairs = 0
        for row in rows:
            if row in columns:
                num_pairs += len(columns[row]) * len(rows[row])
        return num_pairs
