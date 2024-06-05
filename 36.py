class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        def check_square(start_index):
            i, j = start_index
            square = []
            for m in range(i, i + 3):
                for n in range(j, j + 3):
                    square.append(board[m][n])
            square = list(filter(lambda cell: cell != ".", square))

            set_square = set(square)
            if len(set_square) < len(square):
                return False
            return True

        def check_row(row_index):
            row = board[row_index]
            row = list(filter(lambda cell: cell != ".", row))
            set_row = set(row)
            if len(set_row) < len(row):  # there are duplicates
                return False
            return True

        def check_column(column_index):
            column = []
            for i in range(len(board)):
                column.append(board[i][column_index])
            column = list(filter(lambda cell: cell != ".", column))
            set_column = set(column)
            if len(set_column) < len(column):
                return False
            return True

        square_indices = [(0, 0), (0, 3), (0, 6),
                          (3, 0), (3, 3), (3, 6),
                          (6, 0), (6, 3), (6, 6)]

        for square_index in square_indices:
            if not check_square(square_index):
                return False

        for i in range(9):  # for each row
            if not check_row(i):
                return False

        for i in range(9):
            if not check_column(i):
                return False
        return True
