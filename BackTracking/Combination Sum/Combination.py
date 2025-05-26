class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        result = []
        curr = []

        def dfs(i,curr,total):
            if total == target:
                result.append(curr[:])
                return

            if total > target or i >= length:
                return 

            curr.append(nums[i])
            dfs(i,curr,total + nums[i])
            curr.pop()
            dfs(i+1,curr,total)

        dfs(0,[],0)
        return result