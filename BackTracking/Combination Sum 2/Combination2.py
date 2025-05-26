class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        curr = []
        length = len(candidates)
        candidates.sort()
       
        def dfs(i,curr,total):
            if total == target:
                result.append(curr[:])
                return 
            
            if i >= length or total > target:
                return
            
            #add [i]
            curr.append(candidates[i])
            dfs(i+1,curr,total + candidates[i])
            curr.pop()

            #skip [i]
            while(i+1 < length and candidates[i] == candidates[i+1]):
                i += 1
            dfs(i+1,curr,total)
           

        dfs(0,[],0)
        return result