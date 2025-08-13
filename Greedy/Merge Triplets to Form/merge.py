class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        visited = set()

        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue 

            for idx, val in enumerate(t):
                if val == target[idx]:
                    visited.add(idx)
        return len(visited) == 3
            
                