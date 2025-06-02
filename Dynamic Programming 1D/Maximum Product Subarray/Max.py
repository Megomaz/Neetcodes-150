class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0

        result = cur_max = cur_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # Important: we must keep previous values before updating
            temp_max = max(num, cur_max * num, cur_min * num)
            temp_min = min(num, cur_max * num, cur_min * num)

            cur_max = temp_max
            cur_min = temp_min

            result = max(result, cur_max)

        return result


# Brute force
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxP = -float('inf')

        for i in range(len(nums)):
            total = nums[i]
            if total > maxP:
                    maxP = total
            for k in range (i+1,len(nums)):
                total *= nums[k]
                if total > maxP:
                    maxP = total
            if total > maxP:
                    maxP = total

        return maxP if maxP -float('inf') else nums[i]