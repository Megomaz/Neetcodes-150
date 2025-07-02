class Solution:
    def myPow(self, x: float, n: int) -> float:
        total = 1

        if n < 0:
            for i in range(-n):
                total *= x
            return 1/total
        else:
            for i in range(n):
                total *= x
            return total