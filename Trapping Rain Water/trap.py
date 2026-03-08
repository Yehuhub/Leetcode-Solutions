# this a good solution, the main trick is that if we want to calculate the amount of water in the current
# position, we have to know what is the max to the left of the right of the current position, and
# which of those is the min, that way we know how much water is there
# this runs in O(n) but it is also in O(n) space, which can be improved with two pointers
#
# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height)
#         max_left = [0] * n
#         max_right = [0] * n
#         min_l_r = [0] * n

#         for i in range(1, n):
#             max_left[i] = max(height[i-1], max_left[i-1])
        
#         for i in range(n-2, -1, -1):
#             max_right[i] = max(height[i+1], max_right[i+1])

#         for i in range(0, n):
#             min_l_r[i] = min(max_left[i], max_right[i])

#         amount = 0
#         for i in range(n):
#             temp = min_l_r[i] - height[i]
#             if temp >= 0:
#                 amount += temp
#         return amount

# this is a solution running in O(1) space, and O(n) runtime.
# we basically check the max on the fly and then on each iteration we check which is higher, left or right and calculate
# the other pointer, if max_l is taller than max_r then we calculate the right side and add it to the amount
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l,r = 0, n - 1

        max_l, max_r = height[l],height[r]
        amount = 0
        while l < r:
            if max_l < max_r:
                l += 1
                max_l = max(max_l, height[l])
                amount += max_l - height[l]
            else:
                r -= 1
                max_r = max(max_r, height[r])
                amount += max_r - height[r]
        return amount