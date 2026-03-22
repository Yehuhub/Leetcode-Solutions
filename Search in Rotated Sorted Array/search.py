
# optimal solution in O(logn) one pass

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] == target:
                return mid
            
            # in the if statement we basically check in which type of subarray are we in
            # are we in [3,4,5] , where l = 3 and r = 5
            # or are we in [6,0,1,2] where l = 6 and r = 2
            # that way we can check correct cases for each
            if nums[left] <= nums[mid]: 
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1

