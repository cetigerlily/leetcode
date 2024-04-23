class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        def get_neighbours(root):
            valid_neighbours = []
            r, c = root
            possible_moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for move in possible_moves:
                nr = r + move[0]
                nc = c + move[1]

                if 0 <= nr < rows and 0 <= nc < cols:
                    valid_neighbours.append((nr, nc))
            return valid_neighbours

        rows = len(grid)
        cols = len(grid[0])

        visited = set()
        rotten_oranges = []  # sources of rotten oranges as starting points
        fresh_count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 0:
                    visited.add((i, j))

                if grid[i][j] == 1:
                    fresh_count += 1

                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))

        if fresh_count == 0:
            return 0
        else:
            if len(rotten_oranges) == 0:
                return -1

        min_durations = set()
        queue = []
        for rotten_orange in rotten_oranges:
            visited.add(rotten_orange)
            queue.append((rotten_orange, 0))

        duration = 0
        while len(queue) != 0:
            current_root, current_duration = queue.pop(0)
            print(current_root)
            r, c = current_root

            neighbours = get_neighbours((r, c))
            for neighbour in neighbours:
                nr, nc = neighbour

                if neighbour not in visited:
                    visited.add(neighbour)
                    if grid[nr][nc] != 0:
                        queue.append((neighbour, current_duration + 1))
                    duration = current_duration + 1
        min_durations.add(duration)

        if len(visited) == (rows * cols):
            return max(min_durations)
        else:
            return -1
