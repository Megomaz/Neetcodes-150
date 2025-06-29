class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total ^=num

        return total