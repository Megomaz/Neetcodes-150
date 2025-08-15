class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            Sum = 0

            while n != 0:
                Sum += (n%10) * (n%10)
                n //= 10

            if Sum in seen:
                return False
            
            seen.add(Sum)

            n = Sum


        return True