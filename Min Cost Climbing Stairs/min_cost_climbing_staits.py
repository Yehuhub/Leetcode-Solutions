
"""
this is a brute force recursive solution, basically we calculate at each step the lowest cost, i+1 or i+2
until we reach the end.
then we run the dfs on both 0 and 1 indices since we can start at either
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def dfs(i):
            if i >= len(cost):
                return 0
            return cost[i] + min(dfs(i+1), dfs(i+2))

        return min(dfs(0), dfs(1))

"""
this is the correct solution
since we can choose to start at either index 0 or 1 we initialize them to zero, then to each step we get
we take the min of the cached values
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp= [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(dp[i-2] + cost[i-2], dp[i-1] + cost[i-1])

        return dp[n]