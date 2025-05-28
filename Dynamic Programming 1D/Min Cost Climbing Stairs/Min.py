class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        total = 0
        size = len(cost) - 1

        if cost[size - 1] <= cost[size]:
            size -= 1
        
        while ( size >= 0):
            total += cost[size]
            if size -2 >= 0 and cost[size - 2] + total <= cost[size - 1] + total:
                size -= 2
            elif (size -2 < 0):
                return total 
            else:
                size -= 1
        return total
