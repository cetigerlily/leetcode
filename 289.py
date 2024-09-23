class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])

        def get_neighbors(r, c):
            all_possible = [(r - 1, c - 1), (r - 1, c), (r - 1, c + 1),
                        (r, c - 1), (r, c + 1),
                        (r + 1, c - 1), (r + 1, c), (r + 1, c + 1)]

            result = []
            for possible in all_possible:
                if 0 <= possible[0] < m and 0 <= possible[1] < n:
                    result.append((possible[0], possible[1]))
            return result

        neighbors_count = {}  # <(i, j), {0: count 0s in neigh, 1: count 1s in neigh}
        for i in range(m):
            for j in range(n):
                neighbors_count[(i, j)] = {0: 0, 1: 0}
                current_neighbors = get_neighbors(i, j)
                for neighbor in current_neighbors:
                    if board[neighbor[0]][neighbor[1]] == 1:
                        neighbors_count[(i, j)][1] += 1
                    else:
                        neighbors_count[(i, j)][0] += 1

        for i in range(m):
            for j in range(n):
                count = neighbors_count[(i, j)]
                if board[i][j] == 1:
                    if count[1] < 2 or count[1] > 3:
                        board[i][j] = 0
                else:
                    # lives only if count [1] == 3
                    if count[1] == 3:
                        board[i][j] = 1


def main():
    # board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    board = [[1, 1], [1, 0]]
    Solution().gameOfLife(board)


if __name__ == "__main__":
    main()
