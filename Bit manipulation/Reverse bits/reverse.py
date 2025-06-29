class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0

        for i in range(32):
            bit = (n >> i) & 1 # Get the i-th bit from the right
            res += (bit << (31 - i)) # Place it in the mirrored position towards the left
        return res