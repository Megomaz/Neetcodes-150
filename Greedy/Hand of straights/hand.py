# Not my solution
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        hashmap = {}
        for num in hand:
            hashmap[num] = hashmap.get(num, 0) + 1

        heap = list(hashmap.keys())
        heapq.heapify(heap)

        while heap:
            first = heap[0]

            # Try to build a group of size groupSize starting from `first`
            for val in range(first, first + groupSize):
                if val not in hashmap:
                    return False # Card needed for a group is missing
                
                hashmap[val] -= 1

                if hashmap[val] == 0:
                    # If the card count drops to 0, remove it from the heap
                    # BUT: it must be the smallest element (top of the heap)
                    if val != heap[0]:
                        return False # Cards are out of order or missing
                    heapq.heappop(heap)
        return True
        
        
