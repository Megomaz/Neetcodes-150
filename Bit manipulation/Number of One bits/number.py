class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n:
            total += n & 1 # checks if the last (least significant) bit of n is 1.
            n >>= 1 # shifts the bits of n one position to the right (basically divides by 2 and discards the last bit)
            
        return total