# main trick is how to set up the box index, basically we need to index each box
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        seen_row = defaultdict(set)
        seen_col = defaultdict(set)
        seen_box = defaultdict(set)

        for i in range(n):
            for j in range(n):
                curr = board[i][j]
                box_index = (i // 3, j // 3)
                if curr == ".":
                    continue
                if curr in seen_row[i] or curr in seen_col[j] or curr in seen_box[box_index]:
                    return False
                seen_row[i].add(curr)
                seen_col[j].add(curr)
                seen_box[box_index].add(curr)
        return True

