class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        final = 0

        for i in range(len(nums)):
            final += nums[i] ^ i
            if final != 0:
                return i

        return i+1

# faster solution (not mine)
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n  
        for i in range(n):
            xorr ^= i ^ nums[i]
        return xorr