class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
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

        def bfs(root):
            queue = [root]
            coordinates = [root[0], root[1], root[0], root[1]]

            while len(queue) != 0:
                r, c = queue.pop(0)

                r1, c1, r2, c2 = coordinates
                if r < r1 or c < c1:
                    coordinates[0] = r
                    coordinates[1] = c
                elif r > r2 or c > c2:
                    coordinates[2] = r
                    coordinates[3] = c

                neighbours = get_neighbours((r, c))
                for neighbour in neighbours:
                    nr, nc = neighbour

                    if neighbour not in visited:
                        visited.add(neighbour)
                        if land[nr][nc] == 1:  # continue exploring the neighbour if it's land
                            queue.append(neighbour)
            return coordinates

        rows = len(land)
        cols = len(land[0])

        visited = set()
        groups = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visited:
                    visited.add((i, j))

                    if land[i][j] == 1:
                        group = bfs((i, j))
                        groups.append(group)
        return groups
