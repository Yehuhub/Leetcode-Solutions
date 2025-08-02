
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n] * (m - 1)
        dp += [[1]*n]


        for i in reversed(range(m - 1)):
            for j in reversed(range(n)):
                if j + 1 < n:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
                else:
                    dp[i][j] = dp[i+1][j]

        return dp[0][0]



# this is a slightly better implementation, here we dont save the entire dp table
# only the current row which we care about and removed if condition
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in reversed(range(m - 1)):
            new_row = [1] * n
            for j in reversed(range(n - 1)):
                    new_row[j] = new_row[j + 1] + row[j]
            row = new_row

        return row[0]


