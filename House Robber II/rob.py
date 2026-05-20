
"""
so we cant have the first index with the last index, so to solve we do exactly as house robber I,
but once with the first index and without the last, and once without the last and with the first
that way we can find the best solution
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums:List[int]) -> int:

        n = len(nums)
        if not nums:
            return 0
        if n == 1:
            return nums[0]

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(dp[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        return dp[-1]
