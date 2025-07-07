class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False

        total //= 2
        dp = [False] * (total + 1)
        dp[0] = True
        
       # dp - dp[sum//2] - num[i] check if it exists
        for num in nums:
            for i in range(total, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        return dp[total]