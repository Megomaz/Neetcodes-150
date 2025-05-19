class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        check = set(nums)
        count = 0
        for num in check:
            if num - 1 in check:
                continue

            curr = 1
            while (num + 1) in check:
                curr += 1
                num += 1
            
            count = max(curr,count)
        
        return count
            
