# first solution using memoization, I approached the problem like a dynamic programming problem
# that lead me straight into thinking in terms of table and this is the solution
# runtime is O(n) which is great, but memory is also O(n) which can be optimized
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n

        dp = [0] * n
        dp[n-1] = 1
        dp[n-2] = 1

        for i in reversed(range(n-1)):
            if i+2 < n-1:
                dp[i] = dp[i+1] + dp[i+2]
            else:
                dp[i] = 1 + dp[i+1]

        return dp[0]


# Optimized version:
# after figuring out and looking at the problem as a fibonacci sequence its easy to implement
# a more memory efficient solution
# runtime is O(n) and space is O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n

        prev1 = 1
        prev2 = 2

        for _ in range(3, n+1):
            curr = prev1 + prev2
            prev1 = prev2
            prev2 = curr
        
        return prev2