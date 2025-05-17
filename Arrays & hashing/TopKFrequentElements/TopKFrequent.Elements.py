class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            hashmap[num] = hashmap.get(num,0) + 1

        array = sorted(hashmap,  key=lambda v: hashmap[v])
        return array[-k:][::-1]