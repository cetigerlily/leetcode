class Solution(object):
    def numIslands(self, grid):  # DFS solution
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def dfs(root):
            neighbours = getNeighbours(root[0], root[1])
            for neighbour in neighbours:
                nr, nc = neighbour
                if not visited[nr][nc] and grid[nr][nc] == "1":
                    visited[nr][nc] = True
                    dfs(neighbour)

        def getNeighbours(r, c):
            possible_neighbours = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            valid_neighbours = []
            for neighbour in possible_neighbours:
                nr, nc = neighbour
                if 0 <= nr < rows and 0 <= nc < cols:
                    valid_neighbours.append(neighbour)
            return valid_neighbours

        island_count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j] and grid[i][j] == "1":
                    island_count += 1
                    dfs((i, j))
        return island_count

    def numIslandsBfs(self, grid):  # BFS solution
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def bfs(root):
            queue = [root]  # queue of lands
            while len(queue) != 0:
                r, c = queue.pop(0)
                neighbours = getNeighbours(r, c)

                for neighbour in neighbours:
                    nr, nc = neighbour
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        if grid[nr][nc] == '1':
                            queue.append(neighbour)

        def getNeighbours(r, c):
            possible_neighbours = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            valid_neighbours = []
            for neighbour in possible_neighbours:
                nr, nc = neighbour
                if 0 <= nr < rows and 0 <= nc < cols:
                    valid_neighbours.append(neighbour)
            return valid_neighbours

        island_count = 0
        rows = len(grid)
        cols = len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if not visited[i][j]:
                    visited[i][j] = True
                    if grid[i][j] == '1':
                        island_count += 1
                        bfs((i, j))
        return island_count
