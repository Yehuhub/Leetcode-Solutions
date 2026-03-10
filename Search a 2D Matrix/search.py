
# this is pretty straight forward, basically we have to use bin search to find in which row is the target present
# then we use bin search on the row to find it.
# the cool trick here is in finding the row.
# we basically ask for each mid row, is the target between both edges of the row,
# if the target is bigger than last element of the row, it means we need to update our up pointer
# if the target is smaller than the first element of the row, it means we need to update our down pointer
# in this case down means higher and up means lower.
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        up, down = 0, len(matrix) - 1

        while up <= down:
            mid = (down + up) // 2
            if matrix[mid][0] > target:
                down = mid - 1
            elif matrix[mid][-1] < target:
                up = mid + 1
            else:
                break
                
        matrix = matrix[mid]
        l, r = 0, len(matrix) - 1
        while l <= r:
            mid = (l + r) //2
            if matrix[mid] > target:
                r = mid - 1
            elif matrix[mid] < target:
                l = mid + 1
            else:
                return True
        return False
