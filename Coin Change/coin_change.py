
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) # initialize the table with amount + 1, since we will never reach this amount, and size since dp[amount+1] will have the result
        dp[0] = 0 # first element is 0 since to reach 0 coins we need 0 coins

        for a in range(1, amount+1): # for each amount we check every option of coin
            for c in coins: 
                if a - c >= 0: # if a-c >= 0 meaning we calculated how to get to a-c, now we need to add a single c coin to reach the current a amount.
                    dp[a] = min(dp[a], 1 + dp[a-c]) # we have to take minimum because for each a we update for each coin

        return dp[amount] if dp[amount] != amount+1 else -1 #we return the result only if we found a solution, if we havent it will be set to the default value