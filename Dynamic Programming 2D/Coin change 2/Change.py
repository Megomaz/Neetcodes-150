# Memoziation Solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        dp = {}

        def dfs(i,curr):
            if i == len(coins) or curr > amount:
                return 0

            if curr == amount:
                return 1

            if (i, curr) in dp:
                return dp[(i, curr)]

            dp[(i, curr)] = (dfs(i, curr + coins[i]) + 
                              dfs(i + 1, curr))

            return dp[(i, curr)]

        return dfs(0,0)

# Dp Solution
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        size = len(coins)
        dp = [[0] * (amount+1) for _ in range(size+1)]
        
        for j in range(size+1):
            dp[j][0] = 1

        for i in range(size -1 ,-1,-1):
            for k in range(amount+1):
                # option 1: don't pick current coin
                dp[i][k] = dp[i + 1][k]

                # option 2: pick current coin if possible
                if k - coins[i] >= 0:
                    dp[i][k] += dp[i][k - coins[i]]
        return dp[0][amount]