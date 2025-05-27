class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        curr = []
        length = len(nums)
        result = []
    
        def dfs(i,curr):
            if i == length:
                result.append(curr[:])
                return


            curr.append(nums[i])
            dfs(i+1,curr)
            curr.pop()
            dfs(i+1,curr)

        dfs(0,[])

        unique = set(tuple(sorted(lst)) for lst in result)
        final = [list(arr) for arr in unique]
        return final