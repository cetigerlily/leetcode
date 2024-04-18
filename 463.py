class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def getNeighbours(r, c):
            possible_neighbours = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            valid_neighbours = []
            for neighbour in possible_neighbours:
                nc, nr = neighbour
                if 0 <= nc < rows and 0 <= nr < cols:
                    valid_neighbours.append(neighbour)
            return valid_neighbours

        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        queue = [(0, 0)]
        visited[0][0] = True

        total_perimeter = 0
        while len(queue) != 0:
            i, j = queue.pop(0)
            is_land = (grid[i][j] == 1)

            if is_land:
                current_perimeter = 4
            else:
                current_perimeter = 0

            neighbours = getNeighbours(i, j)
            for neighbour in neighbours:
                ni, nj = neighbour
                if grid[ni][nj] == 1 and is_land:
                    current_perimeter -= 1

                if not visited[ni][nj]:
                    visited[ni][nj] = True
                    queue.append(neighbour)
            total_perimeter += current_perimeter
        return total_perimeter
