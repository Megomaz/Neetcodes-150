class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for index,num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num],index]
            hashmap[target - num] = index

        return [-1,-1]