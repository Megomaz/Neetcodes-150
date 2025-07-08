class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        result = [x - y for x, y in zip(gas, cost)]
        
        if sum(result) < 0:
            return -1

        def helper(l,r,total):
            while r < len(result):
                total += result[r]
                r += 1
                if total < 0:
                    return False
            x = 0
            while x < l:
                total += result[x]
                x += 1
                if total < 0:
                    return False
            return True


        for i in range(len(result)):
            if result[i] >= 0:
                if helper(i-1,i+1,result[i]):
                    return i
        return -1
    
# Better solution (not mine) - O(1) memory instead of O(n)
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        total = 0
        res = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])

            if total < 0:
                total = 0
                res = i + 1
        
        return res