class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []

        for i in range(n+1):
            count = 0
            while i:
                count += i & 1
                i >>= 1
            result.append(count)

        return result


# another solution (not mine)
class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        for i in range(n + 1):
            dp[i] = dp[i >> 1] + (i & 1) # dp[i] = dp[i // 2] + (1 if i is odd else 0)
        return dp