class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        tiles = list(tiles)
        result = set()
        current_permutation = []

        def backtrack(length):
            if len(current_permutation) == length:
                tile_permutation = []
                for j in range(len(current_permutation)):
                    tile = tiles[current_permutation[j]]
                    tile_permutation.append(tile)
                result.add(''.join(tile_permutation))
                return

            for j in range(len(tiles)):
                if j not in current_permutation:
                    current_permutation.append(j)
                    backtrack(i)
                    current_permutation.pop()

        for i in range(1, len(tiles) + 1):
            backtrack(i)

        return len(result)
