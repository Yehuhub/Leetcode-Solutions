
# my main point to remember heare is that when finding nexr r/l we need to increase or decrease them,
# also our condition for the while loop is l <= r, because we could get a case when we reach l == r
# and it is the last element we need to check and it could be the target.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1
