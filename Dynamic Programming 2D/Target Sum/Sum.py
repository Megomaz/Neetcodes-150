# Non optimized soltuion
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        def dfs(i,total):
            if i >= len(nums) and total != target:
                return 0

            if total == target and i == len(nums):
                return 1

            add = dfs(i+1, total + nums[i])
            sub = dfs(i+1, total - nums[i])

            return add + sub

        return dfs(0,0)


# Memoziation bottom up
 n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(n):
            for total, count in dp[i].items():
                dp[i + 1][total + nums[i]] += count
                dp[i + 1][total - nums[i]] += count

        return dp[n][target]