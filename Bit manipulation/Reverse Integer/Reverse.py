class Solution:
    def reverse(self, x: int) -> int:
        signed = False

        if x < 0:
            signed = True
        num = 0
        i = 1

        x = abs(x)

        while x:
            num *= 10
            num += (x % 10) 
            x //= 10
        if num > pow(2,31):
            return 0
        if signed:
            return -(num)
        return num