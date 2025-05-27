class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        curr = []
        length = len(nums)
    
        def dfs(i,curr):
            if i == length:
                result.append(curr[:])
                return


            for k in range(i,length):
                curr.append(nums[k])
                nums[i],nums[k] = nums[k], nums[i]
                dfs(i+1,curr)
                curr.pop()
                nums[i],nums[k] = nums[k], nums[i]


        dfs(0,[])
        return result