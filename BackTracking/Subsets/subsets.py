class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        length = len(nums)
    
        def dfs(i,curr):
            if i == length:
                result.append(curr[:])
                return


            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()
            dfs(i+1,curr)

        dfs(0,[])
        return result