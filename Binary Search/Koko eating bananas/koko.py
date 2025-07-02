class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1,max(piles)

        while l <= r:
            temp = 0
            mid = (l+r)//2
            for num in piles:
                temp += math.ceil(num / mid)
            if temp > h:
                l = mid + 1
            else:
                r = mid - 1
        return l
    
        
