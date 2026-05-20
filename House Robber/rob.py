"""
dp solution
idea here is that we either take the best value we picked last or the current value+last avaialable house

"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]

        for i in range(1, n):
            if i-2 >= 0:
                dp[i] = max(dp[i - 1], nums[i] + dp[i-2])
            else:
                dp[i] = max(dp[i - 1], nums[i])
        
        return dp[-1]