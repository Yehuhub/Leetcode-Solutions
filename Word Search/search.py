
# we need to remember here that we HAVE to mark the visited letter as visited, because the next call can also
# check for that cell.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def backtrack(i, j, word_index):
            if word_index >= len(word):
                return True
            if i >= len(board) or j >= len(board[i]) or i < 0 or j < 0:
                return False
            if board[i][j] != word[word_index] or board[i][j] == '#':
                return False

            temp, board[i][j] = board[i][j], '#'
            res = (backtrack(i + 1, j, word_index + 1) or
                    backtrack(i - 1, j, word_index + 1) or
                    backtrack(i, j + 1, word_index + 1) or
                    backtrack(i, j - 1, word_index + 1))
            board[i][j] = temp
            return res

        for i in range(len(board)):
            for j in range(len(board[i])):
                if backtrack(i, j, 0):
                    return True
        return False
        