class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0] * (m + 1) for _ in range (n + 1)]
        

        for i in range(1,n+1):
            for k in range(1,m+1):
                if text1[k-1] == text2[i-1]:
                    dp[i][k] = 1 + dp[i-1][k-1]
                else:
                    dp[i][k] = max(dp[i-1][k],dp[i][k-1])
                    
       
        return dp[i][k]