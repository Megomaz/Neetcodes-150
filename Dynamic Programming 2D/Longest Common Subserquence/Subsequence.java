class Solution {
    public int longestCommonSubsequence(String text1, String text2) {
        int n = text1.length();
        int m = text2.length();
        int[][] dp = new int[n+1][m+1];

        for (int i = 1; i < n + 1; i++){
            for (int k = 1; k < m + 1; k++){
                if (text1.charAt(i - 1) == text2.charAt(k - 1)){
                    dp[i][k] = 1 + dp[i-1][k-1];
                }else{
                    dp[i][k] = Math.max(dp[i-1][k],dp[i][k-1]);
                }
            }
        }
        return dp[n][m];
    }
}
