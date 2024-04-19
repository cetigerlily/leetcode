class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        def getNeighbours(r, c):
            possible_neighbours = [(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)]
            valid_neighbours = []
            for neighbour in possible_neighbours:
                nc, nr = neighbour
                if 0 <= nc < rows and 0 <= nr < cols:
                    valid_neighbours.append(neighbour)
            return valid_neighbours

        og_color = image[sr][sc]
        if og_color == color:
            return image

        rows = len(image)
        cols = len(image[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]
        queue = [(sr, sc)]
        visited[sr][sc] = True

        while len(queue) != 0:
            i, j = queue.pop(0)
            image[i][j] = color
            neighbours = getNeighbours(i, j)
            for neighbour in neighbours:
                ni, nj = neighbour
                if not visited[ni][nj] and image[ni][nj] == og_color:
                    visited[ni][nj] = True
                    queue.append(neighbour)
        return image
