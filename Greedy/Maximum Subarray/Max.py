class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # add nums to total
        # if adding that num means < 0 resest
        largest = -float('inf')
        curr = 0
        
        for i in range(len(nums)):
            curr += nums[i]
            largest = max(largest, curr)
            if curr < 0:
                curr = 0

        return largest 
