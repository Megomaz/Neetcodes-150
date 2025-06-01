class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 3:
            return max(nums)
        
        def helper(arr):
            arr = arr[:]
            n = len(arr)

            if n == 1:
                return arr[0]
            elif n == 2:
                return max(arr[0],arr[1])
            
            dp = [0] * n
            
            dp[0] = arr[0]
            dp[1] = max(arr[0], arr[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], arr[i] + dp[i-2])
            
            return dp[-1] 
        return max(helper(nums[:-1]), helper(nums[1:]))

            