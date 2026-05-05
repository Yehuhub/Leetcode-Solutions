class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if self.is_pos_safe(r, c, board):
                    board[r][c] = "Q"
                    backtrack(r + 1)
                    board[r][c] = "."

        backtrack(0)
        return res

    def is_pos_safe(self, r, c, board):
        # check for queens in the same col
        # we place queens from bottom to top so we know that in row higher there wont
        # be a queen at a higher index
        row = r - 1 
        while row >= 0:
            if board[row][c] == "Q":
                return False
            row -= 1
        
        # here we check for a diagonal left up
        row, col = r - 1, c - 1
        while row >= 0 and col >= 0:
            if board[row][col] == "Q":
                return False
            row -= 1
            col -= 1

        # here we check for diagonal right up
        row, col = r - 1, c + 1
        while row >= 0 and col < len(board):
            if board[row][col] == "Q":
                return False
            row -= 1
            col += 1

        return True


