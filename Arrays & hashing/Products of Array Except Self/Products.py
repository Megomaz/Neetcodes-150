class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        postfix = [1] * n
        prefix = [1] * n

        #prefix
        for i in range(1,n):
            prefix[i] = prefix[i-1] * nums[i-1]
        
        #postfix
        for i in range(n-2,-1,-1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(n):
            nums[i] = postfix[i] * prefix[i]

        return nums

# 1st solution (did not meet O(n) requirement):
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = []
        def Sum(arr):
            if len(arr) == 1:
                return arr[0]

            total = arr[0]
            for i in range(1,len(arr)):
                total *= arr[i]

            return total
            
        for i in range(len(nums)):
            result.append(Sum(nums[:i] + nums[i+1:]))

        return result
        