
# this works with two pointer since we save the max area, and each iteration we decrease the size of the 
# tested contianer, this is way each time we move a pointer we only need to move the smaller one
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        max_area = 0
        l, r = 0, len(heights) - 1

        while l < r:
            current_area = self.find_area(heights, l, r)
            if current_area > max_area:
                max_area = current_area
            if heights[l] < heights[r]:
                l += 1
            elif heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return max_area


    def find_area(self, heights: List[int], i: int, j: int) -> int:
        return (j - i) * min(heights[i], heights[j])