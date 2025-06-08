class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = defaultdict(int)
        q = deque()

        for task in tasks:
            hashmap[task] += 1

        heap = []
        for key,value in hashmap.items():
            heapq.heappush(heap, (-value, key))

        heapq.heapify(heap)
        t = 0

        while heap or q:
            t += 1
            if heap:
                val, letter = heapq.heappop(heap)
                val += 1
                if val < 0:
                    q.append([val, letter, t + n])
            
            if q and q[0][2] == t:
                heapq.heappush(heap,(q[0][0],q[0][1]))
                q.popleft()
                
        return t

