class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        prev2 = 2

        if n == 1:
            return prev
        elif n == 2:
            return prev2


        for i in range (2,n):
            temp = prev
            prev = prev2
            prev2 = temp + prev

        return prev2