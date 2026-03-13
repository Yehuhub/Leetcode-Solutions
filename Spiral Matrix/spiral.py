
# as simple as it gets 
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_row = 0
        bot_row = len(matrix) - 1
        left_col = 0
        right_col = len(matrix[0]) - 1
        res = []


        while top_row <= bot_row and left_col <= right_col:
            # append top row
            for i in range(left_col, right_col + 1):
                res.append(matrix[top_row][i])

            #append right column
            for i in range(top_row + 1, bot_row + 1):
                res.append(matrix[i][right_col])

            # the if statements here basically check for the last center elements we append,
            if top_row < bot_row:
                # append bot row
                for i in range(right_col - 1, left_col - 1 , -1):
                    res.append(matrix[bot_row][i])

            if left_col < right_col:
                # append left col
                for i in range(bot_row - 1, top_row, -1):
                    res.append(matrix[i][left_col])
            top_row += 1
            bot_row -= 1
            left_col += 1
            right_col -= 1
        return res

