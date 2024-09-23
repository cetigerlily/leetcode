class Solution(object):
    def getNeighbors(self, m, n, index):  # m = rows, n = columns
        valid_neighbors = []
        moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        r, c = index
        for move in moves:
            if 0 <= r + move[0] < m and 0 <= c + move[1] < n:
                valid_neighbors.append((r + move[0], c + move[1]))
        return valid_neighbors


    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        queue = [(entrance[0], entrance[1])]
        visited = [[False for i in range(len(maze[0]))] for i in range(len(maze))]
        visited[entrance[0]][entrance[1]] = True
        length = [[0 for i in range(len(maze[0]))] for i in range(len(maze))]

        while len(queue) != 0:
            current = queue.pop(0)
            is_exit = current[0] == 0 or current[1] == 0 or current[0] == len(maze) - 1 or current[1] == len(maze[0]) - 1
            is_entrance = current[0] == entrance[0] and current[1] == entrance[1]
            if is_exit and not is_entrance:
                return length[current[0]][current[1]]

            valid_neighbors = Solution().getNeighbors(len(maze), len(maze[0]), current)
            for neighbor in valid_neighbors:
                if not visited[neighbor[0]][neighbor[1]] and maze[neighbor[0]][neighbor[1]] != '+':
                    visited[neighbor[0]][neighbor[1]] = True
                    queue.append((neighbor[0], neighbor[1]))
                    length[neighbor[0]][neighbor[1]] = length[current[0]][current[1]] + 1

        return -1
