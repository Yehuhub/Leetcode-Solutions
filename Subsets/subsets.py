
# idea here is that we never go back in the array, we either add the current element to the subset and move on
# or we just move on
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        cur_subset = []
        def backtrack(i):
            if i >= len(nums):
                res.append(cur_subset[:])
                return
            
            cur_subset.append(nums[i])
            backtrack(i+1)

            cur_subset.pop()
            backtrack(i+1)
        
        backtrack(0)
        return res